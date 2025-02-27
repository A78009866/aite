from django import forms
from .models import Post, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'image']
<<<<<<< HEAD

class ProfileUpdateForm(forms.ModelForm):  # جديد
    class Meta:
        model = User
        fields = ['username', 'profile_picture']
=======
from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'cover_photo', 'bio', 'location']
>>>>>>> 2aa59cd686b20bd9b1ab5b8b7dda1a956fc18380
