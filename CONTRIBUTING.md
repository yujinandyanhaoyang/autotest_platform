# 贡献指南

感谢您对 Autotest Platform 项目的关注！我们欢迎各种形式的贡献，包括但不限于代码、文档、问题报告和功能建议。

## 🤝 如何贡献

### 报告问题

如果您发现了 bug 或有功能建议，请：

1. 检查 [现有的 Issues](https://github.com/yujinandyanhaoyang/autotest_platform/issues) 确保问题没有被重复报告
2. 使用清晰的标题和详细的描述创建新的 Issue
3. 如果是 bug，请提供：
   - 操作系统和 Python 版本
   - 重现步骤
   - 期望行为和实际行为
   - 相关的错误日志或截图

### 提交代码

1. **Fork 项目**
   ```bash
   # 点击 GitHub 页面右上角的 Fork 按钮
   ```

2. **克隆您的 Fork**
   ```bash
   git clone https://github.com/yujinandyanhaoyang/autotest_platform.git
   cd autotest_platform
   ```

3. **创建新分支**
   ```bash
   # 功能分支
   git checkout -b feature/add-new-feature
   
   # 修复分支
   git checkout -b fix/fix-issue-123
   
   # 文档分支
   git checkout -b docs/update-readme
   ```

4. **进行更改**
   - 遵循项目的编码规范
   - 添加必要的测试
   - 更新相关文档

5. **测试您的更改**
   ```bash
   # 运行测试
   python manage.py test
   
   # 检查代码风格
   flake8 .
   
   # 启动服务器确保功能正常
   python manage.py runserver
   ```

6. **提交更改**
   ```bash
   git add .
   git commit -m "Add: 新功能的简短描述"
   ```

7. **推送到您的 Fork**
   ```bash
   git push origin feature/add-new-feature
   ```

8. **创建 Pull Request**
   - 返回 GitHub 上您的 Fork 页面
   - 点击 "New Pull Request" 按钮
   - 填写 PR 标题和详细描述
   - 等待代码审查

## 📝 编码规范

### Python 代码规范

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范
- 使用 4 个空格缩进
- 行长度不超过 100 字符
- 使用有意义的变量和函数名

```python
# ✅ 好的示例
def calculate_test_success_rate(total_cases, passed_cases):
    """计算测试成功率"""
    if total_cases == 0:
        return 0
    return (passed_cases / total_cases) * 100

# ❌ 不好的示例  
def calc(t, p):
    return p/t*100 if t else 0
```

### Django 规范

- 视图函数使用下划线命名: `project_list_view`
- 模型类使用驼峰命名: `TestProject`
- URL 名称使用连字符: `project-detail`
- 模板文件使用下划线: `project_list.html`

### JavaScript 规范

- 使用 2 个空格缩进
- 使用分号结尾
- 使用驼峰命名

```javascript
// ✅ 好的示例
function handleSidebarToggle() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('active');
}

// ❌ 不好的示例
function toggle(){sidebar.classList.toggle('active')}
```

### CSS 规范

- 使用 2 个空格缩进
- 属性按字母顺序排列
- 使用有意义的类名

```css
/* ✅ 好的示例 */
.sidebar-nav-item {
    background-color: #f8f9fa;
    color: #6c757d;
    padding: 15px 20px;
    transition: all 0.3s ease;
}

/* ❌ 不好的示例 */
.item{background:#f8f9fa;color:#6c757d;padding:15px 20px;}
```

## 🧪 测试指南

### 运行测试

```bash
# 运行所有测试
python manage.py test

# 运行特定应用的测试
python manage.py test platformpage

# 运行特定测试类
python manage.py test platformpage.tests.TestProjectViews

# 运行特定测试方法
python manage.py test platformpage.tests.TestProjectViews.test_project_creation
```

### 编写测试

每个新功能都应该包含相应的测试：

```python
from django.test import TestCase
from django.urls import reverse
from platformpage.models import TestProject

class TestProjectViews(TestCase):
    def setUp(self):
        """在每个测试方法前运行"""
        self.project = TestProject.objects.create(
            name="测试项目",
            description="这是一个测试项目"
        )
    
    def test_project_list_view(self):
        """测试项目列表视图"""
        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "测试项目")
    
    def test_project_creation(self):
        """测试项目创建"""
        data = {
            'name': '新项目',
            'description': '新项目描述'
        }
        url = reverse('project-create')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # 重定向
        self.assertTrue(TestProject.objects.filter(name='新项目').exists())
```

## 📚 文档规范

### 代码注释

```python
def process_test_case(case_data):
    """
    处理测试用例数据
    
    Args:
        case_data (dict): 包含用例信息的字典
            - name (str): 用例名称
            - steps (list): 测试步骤列表
            - expected (str): 期望结果
    
    Returns:
        dict: 处理后的用例数据
        
    Raises:
        ValueError: 当用例数据格式不正确时
    """
    if not isinstance(case_data, dict):
        raise ValueError("用例数据必须是字典格式")
    
    # 验证必填字段
    required_fields = ['name', 'steps', 'expected']
    for field in required_fields:
        if field not in case_data:
            raise ValueError(f"缺少必填字段: {field}")
    
    # 处理逻辑...
    return processed_data
```

### README 更新

如果您的更改影响了用户使用方式，请更新 README.md：

- 新功能的使用说明
- 配置选项的变更
- 依赖项的更新

## 🔄 提交信息规范

使用清晰的提交信息，遵循以下格式：

```
类型: 简短描述 (不超过 50 字符)

详细描述 (如果需要)
- 说明更改的原因
- 描述具体的更改内容
- 提及相关的 Issue 编号

Fixes #123
```

### 提交类型

- `Add:` 新增功能
- `Fix:` 修复 bug
- `Update:` 更新现有功能
- `Remove:` 删除功能
- `Docs:` 文档更新
- `Style:` 代码格式化
- `Refactor:` 代码重构
- `Test:` 测试相关
- `Chore:` 构建过程或辅助工具的变更

### 示例

```bash
# 好的提交信息
git commit -m "Add: 用户认证功能

- 添加用户登录和注册页面
- 实现 JWT 令牌验证
- 添加权限装饰器

Fixes #45"

# 不好的提交信息
git commit -m "修改了一些东西"
git commit -m "bug fix"
```

## 🎯 开发环境设置

### 1. 安装依赖

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装项目依赖
pip install -r requirements.txt

# 安装开发依赖
pip install flake8 black pytest-django
```

### 2. 数据库设置

```bash
# 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser
```

### 3. 静态文件收集

```bash
python manage.py collectstatic
```

### 4. 启动开发服务器

```bash
python manage.py runserver
```

## 🚀 发布流程

维护者会定期创建新版本：

1. 更新 `CHANGELOG.md`
2. 更新版本号
3. 创建 Git 标签
4. 发布 GitHub Release

## 🆘 获取帮助

如果您有任何问题，可以通过以下方式获取帮助：

- 📧 发送邮件到: your-email@example.com
- 💬 在 [GitHub Discussions](https://github.com/yujinandyanhaoyang/autotest_platform/discussions) 中提问
- 🐛 在 [Issues](https://github.com/yujinandyanhaoyang/autotest_platform/issues) 中报告问题

感谢您的贡献！🎉
