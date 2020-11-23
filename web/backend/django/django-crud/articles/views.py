from IPython import embed
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST
# from accounts.models import User
from django.contrib.auth import get_user_model
from .forms import ArticleForm, CommentForm
from .models import Article, Comment, HashTag

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-id')
    # embed()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

@login_required
def create(request):
    if request.method == 'POST':
        # embed()
    # POST 요청 -> 검증 및 저장
        article_form = ArticleForm(request.POST, request.FILES)
        # embed()
        if article_form.is_valid():
        # 검증에 성공하면 저장하고,
            # title = article_form.cleaned_data.get('title')
            # content = article_form.cleaned_data.get('content')
            # article = Article(title=title, content=content)
            article = article_form.save(commit=False)
            article.user = request.user # user 인스턴스!
            article.save()
            for word in article.content.split():
                if word[0] == '#':
                    # 만들어진 값인지 있던 값인지 확인해줘서 튜플형태로 표시해준다.
                    # try:
                    #     hashtag = HashTag.objects.get(content=word)
                    # except:
                    #     hashtag = HashTag.objects.creat(content=word)
                    # 와 같이 동작하는 것을 줄여서 쓴것
                    hashtag, created = HashTag.objects.get_or_create(content=word)
                    # if HashTag.objects.filter(content=word).exists():
                    #     HashTag.objects.get(content=word)
                    # if word[1:] in article.hashtags.all():
                    #     hashtag = HashTag.objects.get(content=word[1:])
                    #     article.hashtags.add(hashtag)
                    # else:
                    #     hashtag = HashTag.objects.creat(content=word[1:])
                    article.hashtags.add(hashtag)
            # redirect
            return redirect('articles:detail', article.pk)
    else:
    # GET 요청 -> Form
        article_form = ArticleForm()
    # GET -> 비어있는 Form context
    # POST -> 검증 실패시 에러메세지와 입력값 채워진 Form context
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comments' : comments,
        'comment_form' : comment_form
    }
    return render(request, 'articles/detail.html', context)
    
from django.views.decorators.http import require_POST

@require_POST
@login_required
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.user == request.user:
        article.delete()
        return redirect('articles:index')
    else:
        raise PermissionDenied

# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     context = {
#         'article' : article,
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.get_object_or_494(pk=article_pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article = article_form.save()
            # 해시태그 수정
            article.hashtags.clear()
            for word in article.content.split():
                if word[0] == '#':
                    hashtag, created = HashTag.objects.get_or_create(content=word)
                    article.hashtags.add(hashtag)
            return redirect('articles:detail', article_pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/form.html', context)

@require_POST
def comment_create(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        # 1. modelform에 사용자 입력값 넣고
        comment_form = CommentForm(request.POST)
        # 2. 검증하고,
        if comment_form.is_valid():
        # 3. 맞으면 저장!
            # 3-1. 사용자 입력값으로 comment instance 생성 (저장은 X)
            comment = comment_form.save(commit=False)
            # 3-2. FK 넣고 저장
            comment.article = article
            comment.user = request.user
            comment.save()
        # 4. return redirect
        else:
            messages.success(request, '댓글이 형식이 맞지 않습니다.')
        return redirect('articles:detail', article_pk)
    else:
        return HttpResponse('Unauthorized', status=401)

    # comment = Comment()
    # comment.content = request.POST.get('content')
    # comment.article = article
    # comment.save()
    # return redirect('articles:detail', article_pk)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        # messages.add_message(request, messages.INFO, '댓글이 삭제 되었습니다.')
        messages.success(request, '댓글이 삭제되었습니다.')
        return redirect('articles:detail', article_pk)
    else:
        return HttpResponseForbidden()

@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 좋아요를 누른적이 있다면?
    # article.like_users.filter() 를 써서 확인하면서 할 수 있다. => get()을 쓰면 없을때 오류가 발생하므로 반드시 filter로
    # if article.like_users.filter(id=request.user.id).exist(): 로 써도 똑같음
    if request.user in article.like_users.all():
        # 좋아요 취소 로직
        article.like_users.remove(request.user)
    # 아니면
    else:
        # 좋아요 로직
        article.like_users.add(request.user)
    return redirect('articles:detail', article_pk)

def hashtag(request, hashtag_pk):
    hashtag = get_object_or_404(HashTag, pk=hashtag_pk)
    context = {
        'hashtag': hashtag
    }
    return render(request, 'articles/hashtag.html', context)