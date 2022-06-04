from email import message
from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    email_to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)