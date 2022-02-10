from django.shortcuts import render, get_object_or_404
from board.models import Notice, Question
from django.contrib.auth.decorators import login_required


def notice_list(request):
    notice_list = Notice.objects.order_by('create_date')
    return render(request, 'board/notice.html', {'notice_list':notice_list})

def notice_detail(request, pk):
    notice_detail = get_object_or_404(Notice, id=pk)
    context = {
        'notice_detail' : notice_detail
    }
    return render(request, 'board/notice_detail.html', context)


def question_list(request):
    question_list = Question.objects.order_by('-create_date')
    return render(request, 'board/question_list.html', {'question_list':question_list})


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    return render(request, 'board/question_detail.html', {'question':question})



@login_required(login_url='common:login')
def question_create(request, question_id):
    pass

@login_required(login_url='common:login')
def answer_create(request, answer_id):
    pass

@login_required(login_url='common:login')
def comment_create(request, comment_id):
    pass


def company_info(request):
    return render(request, 'board/company_info.html')