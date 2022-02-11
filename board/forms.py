from django import forms
from .models import Question, Answer, Comment, User

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
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
        fields = [
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