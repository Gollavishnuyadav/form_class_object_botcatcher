from typing import Any, Dict
from django import forms
from django.http import HttpResponse
# def check_name(value):
#     if value[0].lower()=='a':
#         raise forms.ValidationError('Not Valid')
class StudentForm(forms.Form):
    Name=forms.CharField(max_length=100)
    Password=forms.CharField(max_length=100)
    Re_Enter_password=forms.CharField(max_length=100)
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)


    def clean_method(self):
        bot=self.cleaned_data.get('botcatcher')
        if len(bot)>0:
            raise forms.ValidationError('Not By Human')

    def clean(self):
        c=self.cleaned_data.get('Name')
        if c[0].lower()=='a':
            raise forms.ValidationError('Not starts with a')
        a=self.cleaned_data.get('Password')
        b=self.cleaned_data.get('Re_Enter_password')
        if a!=b:
            raise forms.ValidationError('Check')
        else:
            return HttpResponse('Date Correct')