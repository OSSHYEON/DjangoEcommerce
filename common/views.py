import os, requests
from django.contrib.auth import authenticate, login
from django.contrib.sites import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
import requests
from django.contrib.auth.models import User
from shop.models import Customer
from django.contrib import messages
from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        try:
            if form.is_valid():
                user_form = form.save(commit=False)
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                email = form.cleaned_data.get('email')
                print(username, raw_password, email)
                if request.POST['password1'] == request.POST['password2']:
                    user = User.objects.create_user(username=username, password=raw_password, email=email)
                user_form.save()

                customer = Customer.objects.create(
                    name = user.username,
                    email = email,
                    user = user.id
                )
                customer.save()
                return redirect('/')

        except Exception as error:
            print(error)
            return redirect('common:signup')
    else:
        form = UserForm()
        print('회원가입페이지')
    return render(request, 'common/signup.html', {'form': form})


def mypage(requset):
    return render(requset, 'common/mypage.html')

def kakao_login(request):
    try:
        client_id = ""
        redirect_uri = "http://127.0.0.1:8010/common/kakaologin/callback/"
        return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")

    except Exception as error:
        messages.error("로그인 로직 에러발생", request, error)
        return redirect('/')

def kakao_login_callback(request):
    try:
        code = request.GET.get("code")
        if code is None:
            print("코드를 받을 수 없습니다")
        client_id = ""
        redirect_uri = "http://127.0.0.1:8010/common/kakaologin/callback/"
        request_access_token = requests.post(f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}', headers={"Accept": "application/json"})
        access_token_result = request_access_token.json()
        print(access_token_result)
        error = access_token_result.get('error')
        if error is not None:
            print(error)

        access_token = access_token_result.get('access_token')
        headers = {"Authorization" : f"Bearer {access_token}"}
        profile_request = requests.post("https://kapi.kakao.com/v2/user/me", headers=headers,)
        profile_json = profile_request.json()
        kakao_account = profile_json.get('kakao_account')
        profile = kakao_account.get('profile')
        username = profile.get('nickname')
        email = kakao_account.get("email")
        user = User.objects.get_or_none(email=email)
        if user is not None:
            print("이미 가입된 회원입니다. 로그인해주세요")
        else:
            user = User.objects.create_user(email=email, username=username)
            user.set_unusable_password()
            user.save()
        messages.success(request, "카카오 회원가입 완료")
        login(request, user)
        return redirect('/')

    except Exception as error:
        messages.error(request, error)
