from django.contrib import admin
from .models import Notice, Question

class NoticeAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Question, QuestionAdmin)