#_*_coding:utf-8_*_
from django.contrib import admin
from blog.models import  *
# 注册文章模块
class ArtictleAdmin(admin.ModelAdmin):
    list_display = ('title','desc','date_publish','user')
    list_display_links = ('title',)
    list_editable = ('desc',)
    list_filter = ('category',)
    fieldsets = (
        ('内容编辑',{
            'fields':('title','desc','content','is_recommend','tag','category')
    }),
        ('属性编辑',{
            'classes':('collapse'),
            'fields':('click_count','user')
    }),
    )

#注册评论模块
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','username','content',)
    list_display_links = ('article',)
    list_editable = ('username',)
    list_filter = ('article',)
    fieldsets = (
        ('内容编辑', {
            'fields': ('content','article','pid')
        }),
        ('属性编辑', {
            'classes': ('collapse'),
            'fields': ('username','email','url','user',)
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','index')
    list_display_links = ('name',)
    list_editable = ('index',)
admin.site.register(User)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Article,ArtictleAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Links)
