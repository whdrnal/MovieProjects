from django import forms
from . import models


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = [
            "content",
            "score",
        ]
        labels = {
            'content': '',
            'score': '',
        }
