#!/usr/bin/python
# coding:utf-8
__author__ = 'yj'


from base.models import Project, Sign, Environment, Interface, Case
import requests
import re
import json
from lib.signtype import get_sign

class Execute():
    def __init__(self, case_id, env_id):
        # 初始化参数
        self.case_id = case_id
        self.env_id = env_id
        self.prj_id, self.env_url, self.private_key = self.get_env(self.env_id)
        self.sign_type = self.get_sign(self.prj_id)
        self.extract_dict = {}
        self.glo_var = {}
        self.step_json = []

    # 获取测试环境
    def get_env(self, env_id):
        env = Environment.objects.get(env_id=env_id)
        prj_id = env.project.prj_id
        return prj_id, env.url, env.private_key

    # 获取签名方式
    def get_sign(self, prj_id):
        prj = Project.objects.get(prj_id=prj_id)
        sign_type = prj.sign.sign_id
        return sign_type

    # 单条测试用例执行起点
    def run_case(self):
        #print(f'开始执行测试用例:{self.case_id}')
        case = Case.objects.get(case_id=self.case_id)
        step_list = json.loads(case.content)

        #print(f'setep_list中的内容是{step_list}')
        case_run = {"case_id": self.case_id, "case_name": case.case_name, "result": "pass"}
        #print(f'执行的是{case.case_name}，执行结果为:{case_run["result"]}')
        case_step_list = []

        for step in step_list:
            # 执行单条测试用例
            step_info = self.step(step)
            # 添加单条测试用例结果
            case_step_list.append(step_info)
            if step_info["result"] == "fail":
                case_run["result"] = "fail"
                break
            if step_info["result"] == "error":
                case_run["result"] = "error"
                break
        case_run["step_list"] = case_step_list
        return case_run

    # 执行单个步骤
    def step(self, step_content):
        if_id = step_content["if_id"]
        interface = Interface.objects.get(if_id=if_id)
        var_list = self.extract_variables(step_content)
        if var_list:
            for var_name in var_list:
                # 获取变量值
                var_value = self.get_param(var_name, step_content)
                if var_value is None:
                    # 获取全局变量值
                    var_value = self.get_param(var_name, self.step_json)

                if var_value is None:
                    # 获取提取变量值
                    var_value = self.extract_dict[var_name]
                # 替换变量
                step_content = json.loads(self.replace_var(step_content, var_name, var_value))
        if_dict = {"url": interface.url, "header": step_content["header"], "body": step_content["body"]}
        # 签名
        if interface.is_sign:
            if_dict["body"] = get_sign(self.sign_type, if_dict["body"], self.private_key)
        # 合成请求，拼接环境的根地址+接口地址
        if_dict["url"] = self.env_url + interface.url
        #print(f'发送的完整地址{if_dict["url"]}\n')
        if_dict["if_id"] = if_id
        if_dict["if_name"] = step_content["if_name"]
        if_dict["method"] = interface.method
        if_dict["data_type"] = interface.data_type

        try:
            # 发送请求
            res = self.call_interface(if_dict["method"], if_dict["url"], if_dict["header"],
                                     if_dict["body"], if_dict["data_type"])
            if_dict["res_status_code"] = res.status_code
            if_dict["res_content"] = res.text
        except requests.RequestException as e:
            if_dict["result"] = "Error"
            if_dict["msg"] = str(e)
            return if_dict
        # 提取变量
        if step_content["extract"]:
            self.get_extract(step_content["extract"], if_dict["res_content"])
        if step_content["validators"]:
            if_dict["result"], if_dict["msg"] = self.validators_result(step_content["validators"], if_dict["res_content"])
        else:
            if_dict["result"] = "pass"
            if_dict["msg"] = {}
        return if_dict

    # 从内容中提取所有变量名
    def extract_variables(self, content):
        variable_regexp = r"\$([\w_]+)"
        if not isinstance(content, str):
            content = str(content)
        try:
            return re.findall(variable_regexp, content)
        except TypeError:
            return []


    # 在内容中获取某一参数的值
    def get_param(self, param, content):
        param_val = None
        if isinstance(content, str):
            try:
                content = json.loads(content)
            except:
                content = ""
        if isinstance(content, dict):
            param_val = self.get_param_reponse(param, content)
        if isinstance(content, list):
            dict_data = {}
            for i in range(len(content)):
                try:
                    dict_data[str(i)] = eval(content[i])
                except:
                    dict_data[str(i)] = content[i]
            param_val = self.get_param_reponse(param, dict_data)
        if param_val is None:
            return param_val
        else:
            if "$" + param == param_val:
                param_val = None
            return param_val
    # 替换内容中的变量
    def replace_var(self, content, var_name, var_value):
        if not isinstance(content, str):
            content = json.dumps(content)
        var_name = "$" + var_name
        content = content.replace(str(var_name), str(var_value))
        return content

    # 发送请求
    def call_interface(self, method, url, header, data, content_type='json'):
        print(url, header, data)
        if method == "post":
            if content_type == "json":
                res = requests.post(url=url, json=data, headers=header, verify=False)
            if content_type == "data":
                res = requests.post(url=url, data=data, headers=header, verify=False)
        if method == "get":
            res = requests.get(url=url, params=data, headers=header, verify=False)
        print(res.status_code, res.text)
        return res

    # 验证结果
    def validators_result(self, validators_list, res):
        msg = ""
        result = ""
        for var_field in validators_list:
            check_filed = var_field["check"]
            expect_filed = var_field["expect"]
            check_filed_value = self.get_param(check_filed, res)
            if check_filed_value == expect_filed:
                result = "pass"
                msg = ""
            else:
                result = "fail"
                msg = "字段: " + check_filed + " 实际值为：" + str(check_filed_value) + " 与期望值：" + expect_filed + " 不符"
                break
        return result, msg


    # 在response中提取参数
    def get_extract(self, extract_dict, res):
        for key, value in extract_dict.items():
            key_value = self.get_param(key, res)
            self.extract_dict[key] = key_value

    def get_param_reponse(self, param_name, dict_data, default=None):
        for k, v in dict_data.items():
            if k == param_name:
                return v
            else:
                if isinstance(v, dict):
                    ret = self.get_param_reponse(param_name, v)
                    if ret is not default:
                        return ret
                if isinstance(v, list):
                    for i in v:
                        if isinstance(i, dict):
                            ret = self.get_param_reponse(param_name, i)
                            if ret is not default:
                                return ret
                        else:
                            pass
        return default