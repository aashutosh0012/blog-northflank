from django.contrib import admin


from blog.models import Post, Tag
#admin.site.register(Post)
admin.site.register(Tag)


#Action Menu function in Django Admin
@admin.action(description='Approve Selected Posts')
def approve_Posts(modeladmin, request, queryset):
    queryset.update(is_approved='True')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','is_approved','updated','created','slug', 'created',] 
    list_filter = ['is_approved','tag']
    actions = [approve_Posts]

