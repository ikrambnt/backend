# from django.contrib import admin
# from .models import Post

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'created_at')
#     search_fields = ['title', 'author__email']

#     def has_change_permission(self, request, obj=None):
#         # Prevent admin from editing posts
#         return False

#     def has_add_permission(self, request):
#         # Prevent admin from creating new posts
#         return False

#     def has_delete_permission(self, request, obj=None):
#         # Allow admin to delete posts
#         return True if request.user.is_superuser else False

 
#     def save_model(self, request, obj, form, change):
#     # Automatically set the author to the logged-in user when creating a new post
#          if not change:  # Check if it's a new post
#             obj.author = request.user
#          super().save_model(request, obj, form, change)

# admin.site.register(Post, PostAdmin)
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ['title', 'author__email']

    def has_change_permission(self, request, obj=None):
        # Prevent admin from editing posts
        return False

    def has_add_permission(self, request):
        # Prevent admin from creating new posts
        return False

    def has_delete_permission(self, request, obj=None):
        # Allow admin to delete any posts
        return True if request.user.is_superuser else False

    def save_model(self, request, obj, form, change):
        # Automatically set the author to the logged-in user when creating a new post
        if not change:  # Check if it's a new post
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
