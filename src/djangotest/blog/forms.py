from django import forms

class NewPostForm(forms.Form):
    
    title = forms.CharField(max_length=120, required=True)
    body = forms.CharField(max_length=500, required=True)