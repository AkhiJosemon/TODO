from django import forms
from .models import Account  # Import your custom user model
from django import forms

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    

    class Meta:
        model = Account  # Use your custom user model
        fields = ['first_name', 'last_name', 'email']
        

    # def clean_confirm_password(self):
    #     password = self.cleaned_data.get("password")
    #     confirm_password = self.cleaned_data.get("confirm_password")

    #     if password and confirm_password and password != confirm_password:
    #         raise forms.ValidationError("Passwords do not match.")
        
    #     return confirm_password

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
    #     return user




class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
