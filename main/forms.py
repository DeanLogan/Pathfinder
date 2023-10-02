from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    # captcha = ReCaptchaField() # Add the reCAPTCHA field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'inputField', 'placeholder': 'Enter Student Number', 'id': 'username'})
        self.fields['password'].widget.attrs.update({'class': 'inputField', 'placeholder': 'Enter Password', 'id': 'password'})
        self.fields['remember_me'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['captcha'] = ReCaptchaField()
