from django.db import models

# Create your models here.
# 签名管理模型
class Sign(models.Model):
    sign_id = models.AutoField(primary_key=True, null=False)  # 签名ID
    sign_name = models.CharField(max_length=50)              # 签名名称
    description = models.CharField(max_length=100)           # 签名描述

    def __str__(self):
        return self.sign_name

#  项目模型
class Project(models.Model):
    prj_id = models.AutoField(primary_key=True, null=False)   # 项目ID
    prj_name = models.CharField(max_length=50)                # 项目名称
    sign = models.ForeignKey('Sign', on_delete=models.CASCADE)  # 关联的签名信息（外键）
    description = models.CharField(max_length=100)           # 项目描述

    def __str__(self):
        return self.prj_name

#  测试环境模型
class Environment(models.Model):
    env_id = models.AutoField(primary_key=True, null=False)   # 环境ID
    env_name = models.CharField(max_length=50)                # 环境名称（如测试/生产）
    project = models.ForeignKey('Project', on_delete=models.CASCADE)  # 所属项目（外键）
    description = models.CharField(max_length=100)           # 环境描述
    url = models.CharField(max_length=100)                   # 环境基础URL
    private_key = models.CharField(max_length=50)            # 环境私有密钥

    def __str__(self):
        return self.env_name

#  接口模型
class Interface(models.Model):
    if_id = models.AutoField(primary_key=True, null=False)    # 接口ID
    if_name = models.CharField(max_length=50)                 # 接口名称
    url = models.CharField(max_length=50)                     # 接口路径
    method = models.CharField(max_length=4)                   # 请求方法（GET/POST等）
    data_type = models.CharField(max_length=4)                # 数据类型（如JSON/XML）
    project = models.ForeignKey('Project', on_delete=models.CASCADE)  # 所属项目（外键）
    is_sign = models.IntegerField()                           # 是否需要签名（0/1标识）
    description = models.CharField(max_length=100)           # 接口描述
    request_header_param = models.TextField()                 # 请求头参数（JSON格式）
    request_body_param = models.TextField()                   # 请求体参数（JSON格式）
    response_header_param = models.TextField()                # 响应头示例（JSON格式）
    response_body_param = models.TextField()                  # 响应体示例（JSON格式)

    def __str__(self):
        return self.if_name

# 用例模型
class Case(models.Model):
    case_id = models.AutoField(primary_key=True, null=False)  # 用例ID
    case_name = models.CharField(max_length=50)               # 用例名称
    project = models.ForeignKey('Project', on_delete=models.CASCADE)  # 所属项目（外键）
    description = models.CharField(max_length=200)           # 用例描述
    content = models.TextField()                             # 用例执行内容（JSON格式）

    def __str__(self):
        return self.case_name

# 计划模型
class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True, null=False)  # 计划ID
    plan_name = models.CharField(max_length=50)               # 计划名称
    project = models.ForeignKey('Project', on_delete=models.CASCADE)  # 所属项目（外键）
    environment = models.ForeignKey('Environment', on_delete=models.CASCADE)  # 执行环境（外键）
    description = models.CharField(max_length=200)           # 计划描述
    content = models.TextField()                             # 计划执行内容（JSON格式）

    def __str__(self):
        return self.plan_name

#  报告模型
class Report(models.Model):
    report_id = models.AutoField(primary_key=True, null=False)  # 报告ID
    report_name = models.CharField(max_length=255)             # 报告名称
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)  # 关联的测试计划（外键）
    content = models.TextField()                               # 报告详细内容（JSON格式）
    case_num = models.IntegerField(null=True)                  # 总用例数
    pass_num = models.IntegerField(null=True)                  # 通过用例数
    fail_num = models.IntegerField(null=True)                  # 失败用例数
    error_num = models.IntegerField(null=True)                 # 错误用例数

    def __str__(self):
        return self.report_name