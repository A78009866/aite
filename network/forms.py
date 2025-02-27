from django import forms
from .models import Post, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'image']

class ProfileUpdateForm(forms.ModelForm):  # جديد
    class Meta:
        model = User
        fields = ['username', 'profile_picture']