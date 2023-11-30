# # # posts/views.py
# # from django.shortcuts import render, get_object_or_404, redirect
# # from django.contrib.auth.decorators import login_required
# # from .models import Post
# # from .forms import PostForm

# # @login_required
# # def post_list(request):
# #     posts = Post.objects.all()
# #     return render(request, 'posts/post_list.html', {'posts': posts})

# # @login_required
# # def post_detail(request, pk):
# #     post = get_object_or_404(Post, pk=pk)
# #     return render(request, 'posts/post_detail.html', {'post': post})

# # @login_required
# # def post_create(request):
# #     if request.method == 'POST':
# #         form = PostForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             post = form.save(commit=False)
# #             post.author = request.user
# #             post.save()
# #             return redirect('posts:post_list')
# #     else:
# #         form = PostForm()
# #     return render(request, 'posts/post_form.html', {'form': form, 'action': 'Create'})


# # def post_list(request):
# #     if request.user.is_authenticated:
# #         # Show public posts and the user's private posts
# #         posts = Post.objects.filter(is_public=True) | Post.objects.filter(author=request.user)
# #     else:
# #         # Show only public posts to non-authenticated users
# #         posts = Post.objects.filter(is_public=True)

# #     return render(request, 'posts/post_list.html', {'posts': posts})

# # @login_required
# # def post_edit(request, pk):
# #     post = get_object_or_404(Post, pk=pk)
# #     if request.user == post.author:
# #         if request.method == 'POST':
# #             form = PostForm(request.POST, request.FILES, instance=post)
# #             if form.is_valid():
# #                 form.save()
# #                 return redirect('posts:post_list')
# #         else:
# #             form = PostForm(instance=post)
# #         return render(request, 'posts/post_form.html', {'form': form, 'action': 'Edit'})
# #     else:
# #         return render(request, 'posts/access_denied.html')


# # @login_required
# # def post_delete(request, pk):
# #     post = get_object_or_404(Post, pk=pk)
    
# #     # Check if the logged-in user is a superuser or the author of the post
# #     if not request.user.is_superuser and request.user != post.author:
# #         return redirect('posts:post_list')  # Redirect if not a superuser or post author
    
# #     if request.method == 'POST':
# #         post.delete()
# #         return redirect('posts:post_list')
    
# #     return render(request, 'posts/post_delete.html', {'post': post})

# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Post
# from .forms import PostForm

# @login_required
# def post_list(request):
#     if request.user.is_authenticated:
#         # Show public posts and the user's private posts
#         posts = Post.objects.filter(is_public=True) | Post.objects.filter(author=request.user)
#     else:
#         # Show only public posts to non-authenticated users
#         posts = Post.objects.filter(is_public=True)

#     return render(request, 'posts/post_list.html', {'posts': posts})

# @login_required
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'posts/post_detail.html', {'post': post})

# @login_required
# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('posts:post_list')
#     else:
#         form = PostForm()
#     return render(request, 'posts/post_form.html', {'form': form, 'action': 'Create'})

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.user == post.author:
#         if request.method == 'POST':
#             form = PostForm(request.POST, request.FILES, instance=post)
#             if form.is_valid():
#                 form.save()
#                 return redirect('posts:post_list')
#         else:
#             form = PostForm(instance=post)
#         return render(request, 'posts/post_form.html', {'form': form, 'action': 'Edit'})
#     else:
#         return render(request, 'posts/access_denied.html')

# # @login_required
# # def post_delete(request, pk):
# #     post = get_object_or_404(Post, pk=pk)
    
# #     # Check if the logged-in user is the author of the post
# #     if request.user == post.author:
# #         if request.method == 'POST':
# #             post.delete()
# #         return redirect('posts:post_list')
# #     else:
# #         return render(request, 'posts/access_denied.html')

# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     # Check if the logged-in user is the author of the post or is an admin
#     if request.user == post.author or request.user.is_superuser:
#         if request.method == 'POST':
#             post.delete()
#             return redirect('posts:post_list')
#         return render(request, 'posts/post_delete.html', {'post': post})
#     else:
#         return render(request, 'posts/access_denied.html')


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment, Post
from .forms import CommentForm,  PostForm


def post_list(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(is_public=True) | Post.objects.filter(author=request.user)
    else:
        posts = Post.objects.filter(is_public=True)
    
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('posts:post_detail', pk=post.pk)

    else:
        comment_form = CommentForm()

    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_list')
    else:
        form = PostForm()
    
    return render(request, 'posts/post_form.html', {'form': form, 'action': 'Create'})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user == post.author:
        if request.method == 'POST':
           
            form = PostForm(request.POST, request.FILES, instance=post)
            print(f"Post Content in view: {post.is_public}")
            var = post.content
            if form.is_valid():
                form.save()
                return redirect('posts:post_list')
        else:
            # Passez l'instance au formulaire lors de l'initialisation
            form = PostForm(instance=post)
            
        return render(request, 'posts/post_form.html', {'form': form, 'action': 'Edit', 'post': post,'var': var})
    else:
        return render(request, 'posts/access_denied.html')
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user == post.author or request.user.is_superuser:
        if request.method == 'POST':
            post.delete()
            return redirect('posts:post_list')
        return render(request, 'posts/post_delete.html', {'post': post})
    else:
        return render(request, 'posts/access_denied.html')
    
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    # Check if the logged-in user is the author of the comment or is an admin
    if request.user == comment.user or request.user.is_superuser:
        comment.delete()
        return redirect('posts:post_detail', pk=comment.post.pk)
    else:
        return render(request, 'posts/access_denied.html')