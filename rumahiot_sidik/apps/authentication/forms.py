from django import forms

class EmailLoginForm(forms.Form):
    email = forms.EmailField(required=True,max_length=254)
    password = forms.CharField(required=True,max_length=32)

class EmailRegistrationForm(forms.Form):
    full_name = forms.CharField(required=True,max_length=70)
    email = forms.EmailField(required=True,max_length=254)
    password = forms.CharField(required=True,max_length=50)
    retype_password = forms.CharField(required=True, max_length=50)

    def clean(self):
        if 'password' in self.cleaned_data and 'retype_password' in self.cleaned_data and 'full_name' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['retype_password']:
                # TODO : Please do backup validation in frontend & sent the error into the view
                raise forms.ValidationError('Password Missmatch')
            else:
                return self.cleaned_data
        else:
            raise forms.ValidationError('Invalid parameter')

class TokenValidationForm(forms.Form):
    token = forms.CharField(required=True,max_length=500)
