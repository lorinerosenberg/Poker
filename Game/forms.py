from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model, logout
from django import forms
from Game.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','email','password']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist. Please register to continue.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password.")
        return super(UserLoginForm, self).clean(*args, **kwargs)



class CreateProfileForm(forms.ModelForm):

     class Meta:
         model = UserProfile
         fields = ['first_name','last_name','country','chips','profile_pic_url']
