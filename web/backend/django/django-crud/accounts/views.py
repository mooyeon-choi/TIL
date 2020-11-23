from IPython import embed
from django.shortcuts import render, redirect
# model, modelform을 불러옴
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        # request에 모든 정보가 담겨있으므로 request를 넣어줘야함
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인
            user = form.get_user()
            auth_login(request, user) # 로그인!
            # auth_login(request, form.get_user())로 한번에 쓸수도 있음
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        # 1. 사용자가 보낸 내용 담아서
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # 2. 검증
        if form.is_valid():
            # 3. 반영
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context  = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def profile(request, account_pk):
    # user = User.objects.get(pk=account_pk)
    User = get_user_model()
    user = get_object_or_404(User, pk=account_pk)
    context = {
        'user_profile': user
    }
    return render(request, 'accounts/profile.html', context)

def follow(request, account_pk):
    User = get_user_model()
    obama = get_object_or_404(User, pk=account_pk)
    if obama != request.user:
        # 이 사람을 팔로우 한 적 있다면
        if request.user in obama.followers.all():
            # 취소
            obama.followers.remove(request.user)
        # 아니면
        else:
            # 팔로우
            obama.followers.add(request.user)
            