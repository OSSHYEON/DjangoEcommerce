from django import forms
from .models import Question, Answer, Comment, User

class QustionForm(forms.ModelForm):
    class Meta:
        model = Question
        field = [
            'author',
            'title',
            'content'
        ]

        widgets = {
            'author' : User.username,
            'title' : forms.TextInput(),
            'content' : forms.TextInput()
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        field = [
            'author',
            'title',
            'content'
        ]
        widgets = {
            'author' : User.username,
            'title' : forms.TextInput(),
            'content' : forms.TextInput()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']