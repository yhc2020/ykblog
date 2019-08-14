import xadmin
from xadmin import views
from .models import Post


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "yk的博客后台"  # 设置站点标题
    site_footer = "Blog - YK"  # 设置站点的页脚


xadmin.site.register(views.CommAdminView, GlobalSettings)

class PostAdmin(object):
    list_display = ['id', 'title','author', 'timestamp', 'views','comments_count','likers_count']
    list_editable=['title']
    show_detail_fields = ['title']
    list_filter=['timestamp']
    readonly_fields = ['timestamp', 'views','comments_count','likers_count']
    search_fields = ('title',)


xadmin.site.register(Post, PostAdmin)