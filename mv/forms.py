from django import forms
from . import models


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = [
            "content",
        ]
        labels = {
            'content': '',
        }


class ReviewForm(forms.Form):
    score = forms.IntegerField(
        label='한줄평',
        widget=forms.NumberInput(attrs={
            'class': 'score',
        })
    )
