from django import forms
from blog.models import Post
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' 
        widgets = {
            'title': forms.TextInput({'class': 'form-control'}),
            'image': forms.FileInput({'class': 'form-control'}),
            'description': RichTextField(),
            'sub_category': forms.Select({'class': 'form-control'}),
            'category': forms.Select({'class': 'form-control'}),
            'status': forms.Select({'class': 'form-control'}),
            'likes': forms.NumberInput({'class': 'form-control'}),
            'comments': forms.NumberInput({'class': 'form-control'}),
            'bookmarks': forms.NumberInput({'class': 'form-control'}),
            'isLike': forms.RadioSelect({'class': 'form-control'}),
            'isBookmark': forms.RadioSelect({'class': 'form-control'}),

        } 
