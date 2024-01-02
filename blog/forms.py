from django import forms
from .models import Comment



class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        widgets={
            'comment':forms.TextInput({'class': 'form-control'})
        }