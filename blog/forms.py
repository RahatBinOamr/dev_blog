from django import forms

from .models import Contact
from .models import Comment,Subscribe



class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        widgets={
            'comment':forms.TextInput({'class': 'form-control'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['name', 'email', ]