from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from board.models import Notice, Question, Answer
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, AnswerForm
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
    notice_detail.hits += 1
    notice_detail.save()
    return render(request, 'board/notice_detail.html', context)


def question_list(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)
    page_object = paginator.get_page(page)
    return render(request, 'board/question_list.html', {'question_list':page_object})


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    answer = Answer.objects.filter(question_id=pk).order_by('-create_date')
    context = {
        'question':question,
        'answer':answer
    }
    question.hits += 1
    question.save()
    return render(request, 'board/question_detail.html', context)



@login_required(login_url='common:login')
def question_create(request):
    form = QuestionForm()
    if request.method == "POST":
        question = form.save(commit=False)
        question.title = request.POST['title']
        question.content = request.POST['content']
        question.create_date=timezone.now()
        question.author = request.user.customer
        question.save()
        return redirect('board:question_list')
    return render(request, 'board/question_create.html', {'form':form})

@login_required(login_url='common:login')
def answer_create(request, pk):
    question = get_object_or_404(Question, id=pk)
    form = AnswerForm()
    if request.method == "POST":
        answer = form.save(commit=False)
        answer.content = request.POST['content']
        answer.create_date = timezone.now()
        answer.author = request.user.customer
        answer.question = question
        answer.save()
        return redirect('board:question_detail', pk=question.id)
    return render(request, 'board/answer_create.html', {'form':form})



def company_info(request):
    return render(request, 'board/company_info.html')