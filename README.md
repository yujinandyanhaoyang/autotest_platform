# Autotest Platform

一个基于 Django 的自动化测试管理平台，提供项目管理、接口测试、用例管理和测试报告等功能。

## 🚀 功能特性

- **项目管理**: 支持多项目管理，项目间数据隔离
- **环境管理**: 测试环境配置和切换
- **接口管理**: RESTful API 接口管理和测试
- **用例管理**: 测试用例编写、执行和管理
- **测试计划**: 批量测试执行和计划调度
- **报告系统**: 详细的测试报告和统计分析
- **签名验证**: 支持多种 API 签名方式
- **响应式设计**: 支持桌面和移动端访问

## 🛠️ 技术栈

- **后端**: Django 5.1.3 + Python 3.10+
- **前端**: Bootstrap + jQuery + Font Awesome
- **数据库**: SQLite (可扩展为 MySQL/PostgreSQL)
- **样式**: 现代化简洁 UI 设计

## 📦 项目结构

```
Autotest_platform/
├── Autotest_platform/          # 主应用配置
│   ├── settings.py             # Django 设置
│   ├── urls.py                 # 主路由配置
│   └── views.py                # 主视图
├── platformpage/               # 核心业务应用
│   ├── models.py               # 数据模型
│   ├── urls.py                 # 业务路由
│   └── views/                  # 业务视图模块
│       ├── case_views.py       # 用例管理
│       ├── env_views.py        # 环境管理
│       ├── interface_views.py  # 接口管理
│       ├── plan_views.py       # 测试计划
│       ├── project_views.py    # 项目管理
│       ├── report_views.py     # 报告系统
│       └── sign_views.py       # 签名管理
├── lib/                        # 工具库
│   ├── excel_case_processor.py # Excel 用例处理
│   ├── execute.py              # 测试执行引擎
│   └── signtype.py             # 签名算法
├── static/                     # 静态资源
│   ├── css/                    # 样式文件
│   ├── scripts/                # JavaScript 文件
│   ├── img/                    # 图片资源
│   └── vendor/                 # 第三方库
├── templates/                  # 模板文件
│   ├── index.html              # 主页模板
│   └── platformpage/           # 业务模板
└── download_report/            # 报告下载目录
```

## 🔧 安装部署

### 环境要求

- Python 3.10 或更高版本
- pip 包管理器
- Git (用于克隆项目)

### 快速开始

1. **克隆项目**
```bash
git clone https://github.com/yujinandyanhaoyang/autotest_platform.git
cd autotest_platform
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **数据库迁移**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **创建超级用户 (可选)**
```bash
python manage.py createsuperuser
```

5. **启动服务**
```bash
python manage.py runserver
```

6. **访问应用**
打开浏览器访问 `http://127.0.0.1:8000`

## 🎯 使用指南

### 项目管理
1. 登录系统后，点击左侧菜单 "基础信息" -> "项目管理"
2. 点击 "新增项目" 创建测试项目
3. 填写项目名称、描述等基本信息

### 环境配置
1. 进入 "测试环境管理" 页面
2. 配置不同的测试环境 (开发、测试、生产)
3. 设置环境的基础 URL 和相关参数

### 接口管理
1. 在 "接口管理" 中添加 API 接口
2. 配置接口的 URL、请求方法、参数等
3. 可以直接在界面中测试接口

### 用例编写
1. 进入 "用例管理" 创建测试用例
2. 支持手动编写或 Excel 批量导入
3. 可以组合多个接口形成测试场景

### 测试执行
1. 在 "测试计划管理" 中创建执行计划
2. 选择要执行的用例和环境
3. 执行完成后可查看详细报告

## 🔐 签名支持

平台支持多种 API 签名方式:
- MD5 签名
- SHA1 签名  
- SHA256 签名
- HMAC 签名
- 自定义签名算法

## 📊 报告功能

- **实时报告**: 测试执行过程中实时查看结果
- **统计分析**: 成功率、失败率等统计图表
- **详细日志**: 每个用例的执行详情和错误信息
- **导出功能**: 支持 PDF、Excel 等格式导出

## 🎨 界面优化

- **响应式设计**: 适配桌面和移动设备
- **现代化风格**: 简洁清爽的 UI 设计语言
- **浅色主题**: 柔和的配色方案，减少视觉疲劳
- **快速加载**: 优化静态资源，提升页面加载速度

## 🤝 贡献指南

我们欢迎所有形式的贡献，包括但不限于:

1. **报告 Bug**: 在 Issues 中报告发现的问题
2. **功能建议**: 提出新功能或改进建议
3. **代码贡献**: 提交 Pull Request
4. **文档完善**: 改进项目文档

### 提交 Pull Request 流程

1. Fork 本项目到你的 GitHub 账户
2. 创建新的分支: `git checkout -b feature/your-feature-name`
3. 提交你的修改: `git commit -am 'Add some feature'`
4. 推送到分支: `git push origin feature/your-feature-name`
5. 创建 Pull Request

## 📝 开发规范

- 遵循 PEP 8 Python 代码规范
- 使用有意义的变量和函数名
- 为复杂逻辑添加注释
- 新功能需要添加相应的测试用例
- 提交信息使用英文，格式清晰

## 🐛 常见问题

**Q: 如何修改默认端口?**
A: 使用 `python manage.py runserver 0.0.0.0:端口号`

**Q: 数据库文件在哪里?**
A: 项目根目录的 `db.sqlite3` 文件

**Q: 如何重置数据库?**
A: 删除 `db.sqlite3` 文件，然后重新执行迁移命令

**Q: 静态文件无法加载?**
A: 检查 `settings.py` 中的 `STATICFILES_DIRS` 配置

**Q: 如何部署到生产环境?**
A: 建议使用 nginx + gunicorn 的方式部署，详见部署文档

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)，你可以自由使用、修改和分发本项目。

## 📞 联系我们

- **项目主页**: https://github.com/yujinandyanhaoyang/autotest_platform
- **问题反馈**: https://github.com/yujinandyanhaoyang/autotest_platform/issues
- **邮件联系**: your-email@example.com

## 🙏 致谢

感谢所有为本项目贡献代码和建议的开发者们！

---

如果这个项目对你有帮助，请给我们一个 ⭐ Star！
