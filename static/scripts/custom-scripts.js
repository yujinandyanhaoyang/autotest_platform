// 自定义JavaScript - 移动到外部文件以提升性能

// 自定义 contains 函数
function getElementsByText(selector, text) {
    const elements = document.querySelectorAll(selector);
    return Array.from(elements).filter(element => element.textContent.includes(text));
}

document.addEventListener('DOMContentLoaded', function () {
    const aName = document.querySelector('a.this')?.textContent;
    const pageName = document.querySelector('a.this-page')?.textContent;

    if (aName) {
        getElementsByText('span', aName).forEach(span => {
            const aElement = span.parentElement.closest('a');
            if (aElement) {
                aElement.classList.remove('collapsed');
                aElement.classList.add('active');
            }
        });

        if (pageName) {
            getElementsByText('a', pageName).forEach(a => {
                const divElement = a.closest('li').closest('ul').closest('div');
                if (divElement) {
                    divElement.classList.remove('collapse');
                    divElement.classList.add('collapse', 'in');
                }
                a.classList.add('active');
            });
        }
    }
    
    // 添加平滑滚动效果
    document.querySelectorAll('a[href^="#"]:not([data-toggle="collapse"])').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href'))?.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // 添加悬停效果
    const navItems = document.querySelectorAll('.sidebar .nav > li > a');
    navItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            if (!this.classList.contains('active')) {
                this.style.paddingLeft = '23px';
                this.style.transition = 'all 0.3s';
            }
        });
        
        item.addEventListener('mouseleave', function() {
            if (!this.classList.contains('active')) {
                this.style.paddingLeft = '20px';
            }
        });
    });
    
    // 侧边栏折叠/展开功能增强
    document.querySelectorAll('[data-toggle="collapse"]').forEach(toggleBtn => {
        toggleBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            const target = document.querySelector(this.getAttribute('href'));
            const icon = this.querySelector('.icon-submenu');
            
            if (target.classList.contains('in')) {
                target.classList.remove('in');
                this.classList.add('collapsed');
                if (icon) {
                    icon.style.transform = 'rotate(0deg)';
                }
            } else {
                // 关闭其他展开的菜单
                document.querySelectorAll('.sidebar .collapse.in').forEach(openCollapse => {
                    if (openCollapse !== target) {
                        openCollapse.classList.remove('in');
                        const relatedBtn = document.querySelector(`[href="#${openCollapse.id}"]`);
                        if (relatedBtn) {
                            relatedBtn.classList.add('collapsed');
                            const relatedIcon = relatedBtn.querySelector('.icon-submenu');
                            if (relatedIcon) {
                                relatedIcon.style.transform = 'rotate(0deg)';
                            }
                        }
                    }
                });
                
                target.classList.add('in');
                this.classList.remove('collapsed');
                if (icon) {
                    icon.style.transform = 'rotate(90deg)';
                }
            }
        });
    });
    
    // 移动端侧边栏切换
    const toggleBtn = document.querySelector('.btn-toggle-fullwidth');
    const sidebar = document.querySelector('.sidebar');
    
    if (toggleBtn && sidebar) {
        toggleBtn.addEventListener('click', function() {
            sidebar.classList.toggle('active');
            
            // 添加遮罩层
            if (sidebar.classList.contains('active')) {
                const overlay = document.createElement('div');
                overlay.className = 'sidebar-overlay';
                overlay.style.cssText = `
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(0,0,0,0.5);
                    z-index: 999;
                    display: block;
                `;
                document.body.appendChild(overlay);
                
                // 点击遮罩关闭侧边栏
                overlay.addEventListener('click', function() {
                    sidebar.classList.remove('active');
                    document.body.removeChild(overlay);
                });
            } else {
                const overlay = document.querySelector('.sidebar-overlay');
                if (overlay) {
                    document.body.removeChild(overlay);
                }
            }
        });
    }
});
