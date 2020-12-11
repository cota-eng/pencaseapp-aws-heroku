from django import forms
from allauth.account.forms import SignupForm
class ProfileForm(forms.Form):
    nickname = forms.CharField(label="nickname", max_length=10, required=False)

class SignupCustomForm(SignupForm):
    nickname = forms.CharField(max_length=10, required=False)
    def save(self, request):
        user = super(SignupCustomForm, self).save(request)
        user.nickname = self.cleaned_data['nickname']
        user.save()
        return user