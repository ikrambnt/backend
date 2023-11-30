# posts/models.py
from django.db import models
from accounts.models import User

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to="post_images", blank=True, null=True)

#     def __str__(self):
#         return self.title

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to="post_images", blank=True, null=True)
#     is_public = models.BooleanField(default=True)  # New field
#     def __str__(self):
#         return self.title
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="post_images", blank=True, null=True)
    is_public = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  
    text = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.text}'