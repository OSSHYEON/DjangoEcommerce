from django.shortcuts import render, get_object_or_404
from board.models import Notice, Question
from django.contrib.auth.decorators import login_required
from .forms import QustionForm
from django.core.paginator import Paginator


def notice_list(request):
    page = request.GET.get('page', '1')
    notice_list = Notice.objects.order_by('create_date')
    paginator = Paginator(notice_list, 10)
    page_object = paginator.get_page(page)
    return render(request, 'board/notice.html', {'notice_list':page_object})

def notice_detail(request, pk):
    notice_detail = get_object_or_404(Notice, id=pk)
    context = {
        'notice_detail' : notice_detail
    }
    return render(request, 'board/notice_detail.html', context)


def question_list(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)
    page_object = paginator.get_page(page)
    return render(request, 'board/question_list.html', {'question_list':page_object})


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    return render(request, 'board/question_detail.html', {'question':question})



@login_required(login_url='common:login')
def question_create(request):
    question = QustionForm()
    return render(request, 'board/question_create.html',{'question':question})

@login_required(login_url='common:login')
def answer_create(request, answer_id):
    pass

@login_required(login_url='common:login')
def comment_create(request, comment_id):
    pass


def company_info(request):
    return render(request, 'board/company_info.html')