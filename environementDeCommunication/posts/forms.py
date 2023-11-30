# # posts/forms.py
# from django import forms
# from .models import Post


from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'is_public'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # Add 'form-control' class to all form fields
            field.widget.attrs['class'] = 'form-control'
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }