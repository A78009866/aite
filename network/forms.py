from django import forms
from .models import Post, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'image']
from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'cover_photo', 'bio', 'location']
