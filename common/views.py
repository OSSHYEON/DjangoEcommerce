import os, requests
from django.contrib.auth import authenticate, login
from django.contrib.sites import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
import requests
from django.contrib.auth.models import User
from shop.models import Customer, Order
from board.models import Question, Answer
from django.contrib import messages
from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            raw_password = request.POST['password1']
            email = request.POST['email']
            print(username, raw_password, email)
            user = User.objects.create_user(username, password=raw_password)
            customer = Customer()
            customer.user = user
            customer.name = username
            customer.email = email
            customer.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')

    else:
        form = UserForm()
        print('회원가입페이지')
    return render(request, 'common/signup.html', {'form': form})


def mypage(request):
    customer = request.user.customer
    orders = Order.objects.filter(customer_id=customer.id).order_by('-date_ordered')

    questions = Question.objects.filter(author_id=customer.id).order_by('-create_date')

    context = {
        'orders':orders,
        'questions':questions
    }
    return render(request, 'common/mypage.html', context)



#=======================================================================================================================
# 소셜로그인

def kakao_login(request):
    try:
        client_id = ""
        redirect_uri = "http://127.0.0.1:8010/common/kakaologin/callback/"
        return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")

    except Exception as error:
        messages.error("로그인 로직 에러발생", request, error)
        return redirect('/')




def kakao_login_callback(request):
    code = request.GET.get("code")
    if code is None:
        print("코드를 받을 수 없습니다")
    client_id = ""
    redirect_uri = "http://127.0.0.1:8010/common/kakaologin/callback/"
    request_access_token = requests.post(f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}', headers={"Accept": "application/json"})
    access_token_result = request_access_token.json()

    access_token = access_token_result.get('access_token')
    headers = {"Authorization" : f"Bearer {access_token}"}
    profile_request = requests.post("https://kapi.kakao.com/v2/user/me", headers=headers,)
    profile_json = profile_request.json()
    kakao_account = profile_json.get('kakao_account')

    profile = kakao_account.get('profile')
    username = profile.get('nickname')
    email = kakao_account.get("email")

    user = User.objects.filter(email=email).first()

    if not user:
        user = User.objects.create_user(
            email=email,
            username=username
        )
        user.set_unusable_password()
        user.save()

        customer = Customer()
        customer.user = user
        customer.name = username
        customer.email = email
        customer.save()

        login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')

    else:
        login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')

    return redirect('/')

