from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from common.forms import UserForm, FindUsernameForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password, first_name=first_name)  # 사용자 인증
            login(request, user)  # 로그인
            messages.success(request, "회원가입 완료되었습니다.")
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def find_username(request: HttpRequest):
    if request.method == 'POST':
        form = FindUsernameForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']

            qs: QuerySet = User.objects.filter(email=email, first_name=first_name)

            if not qs.exists():
                messages.warning(request, "일치하는 회원이 존재하지 않습니다.")
            else:
                user: User = qs.first()
                messages.success(request, f"해당회원의 아이디는 {user.username} 입니다.")
                return redirect(reverse("common:login") + '?first_name=' + user.first_name)
    else:
        form = FindUsernameForm()

    return render(request, 'common/find_username.html', {
        'form': form,
    })

