from django import forms
from .models import SignUp

class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
      "type": "email",
      "name": "email",
      "id": "email",
      "placeholder": "Type your email address"
    }), label="")
    class Meta:
        model = SignUp
        fields = ('email', )