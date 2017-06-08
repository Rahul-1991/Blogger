from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:

        model = Blog
        fields = ('content', )

        widgets = {
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }