from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'user_id'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-1'}),
            'body': forms.Textarea(attrs={'class': 'form-control my-1'})
        }

        # If I was using a regular form, not a model form
        # title = forms.CharField(max_length=120, required=True),
        # body = forms.CharField(max_length=500, required=True)