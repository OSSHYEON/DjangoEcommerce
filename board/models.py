from django.db import models

from django.db import models
from django.contrib.auth.models import User
from shop.models import Customer

#=======================================================================================================================
# 게시판

# 공지사항
class Notice(models.Model):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

#=======================================================================================================================
# Q&A 게시판

# 질문
class Question(models.Model):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)


# 답변
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

# 댓글
class Comment(models.Model):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
