from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["message"].widget.attrs = {
            "placeholder": "메세지를 입력해 주세요",
            "rows": 3,
            "cols": 60,
        }
