from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Tag
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'get_tags', 'status', 'created_on')
    # list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    def get_tags(self, obj):
        return ",".join([tag.title for tag in obj.tag.all()])
    get_tags.short_description = "TAGS"
    

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Tag, TagAdmin)
