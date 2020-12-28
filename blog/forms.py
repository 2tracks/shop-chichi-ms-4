from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'article']

    # https://stackoverflow.com/questions/11947001/change-the-name-attribute-of-form-field-in-django-template-using
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['article'].label = "Comment"
