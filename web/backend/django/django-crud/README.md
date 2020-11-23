# Django - CRUD

> Django ORM을 활용하여 게시판 기능 구현하기

## 1. 환경설정

* 가상환경(venv)

  * python 3.7.4에서 가상환경 생성

    ```bash
    $ python -V
    python 3.7.4
    $ python -m venv venv
    ```

  * 가상환경 실행

    ```bash
    $ source venv/Scripts/activate
    (venv) $
    ```

    

* pip - `requirements.txt` 확인

  * 현재 패키지 리스트 작성

    ```bash
    $ pip freeze > requirements.txt
    ```

  * 만약, 다른 환경에서 동일하게 설치한다면

     ```bash
    $ pip install -r requirements.txt
    ```

* django app - `articles`

## 2. Model 설정

### 1. `Article` 모델 정의

```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

* 클래스 정의할 때는 `models.Model` 을 상속받아 만든다.

* 정의하는 변수는 실제 데이터베이스에서 각각의 필드(column)을 가지게 된다.

* 주요 필드

  * `CharField(max_length)`
    * 필수 인자로 `max_length` 를 지정하여야 한다.
    * 일반적으로 데이터베이스에서 `VARCHAR` 로 지정한다.
    * `<input type="text">`
  * `TextField()`
    * 일반적으로 데이터베이스에서 `TEXT` 으로 지정된다.
    * `CharField` 보다 더 많은 글자를 저장할 때 사용된다.
    * `<textarea>`
  * `DateTimeField()`
    * 파이썬의 `datetime` 객체로 활용된다.
    * 옵션
      * `auto_now_add=True` : 생성시에 자동으로 저장(작성일)
      * `auto_now=True` : 변경시에 자동으로 저장(수정일)
  * `BooleanField()`, `FileField()`, `IntegerField()` 등 다양한 필드를 지정할 수 있다.

* `id` 값은 자동으로 `INTEGER` 타입으로 필드가 생성되고, 이는 `PK(Primary Key)` 이다.

* 모든 필드는 `NOT NULL` 조건이 선언되며, 해당 옵션을 수정하려면 아래와 같이 정의할 수 있다.

  ```python
  username = models.CharField(max_length=10, null=True)
  ```

### 2. 마이그레이션(migration) 파일 생성

> 마이그레이션(migration)은 모델에 정의한 내용(데이터베이스의 스키마)의 변경사항을 관리한다. 
>
> 따라서, 모델의 필드 수정 혹은 삭제 등이 변경될 때마다 마이그레이션 파일을 생성하고 이를 반영하는 형식으로 작업한다.

```bash
$ python manage.py makemigrations
Migrations for 'articles':
  articles\migrations\0001_initial.py
    - Create model Article
```

* 만약, 현재 데이터베이스에 반영되어 있는 마이그레이션을 확인하고 싶다면 아래의 명령어를 활용한다.

  ```bash
  $ python manage.py showmigrations
  articles
   [ ] 0001_initial
  ```

### 3. DB 반영(migrate)

> 만들어진 마이그레이션 파일을 실제 데이터베이스에 반영한다.

```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
```

* 만약 특정 app의 마이그레이션 혹은 특정 버전만 반영하고 싶다면 아래의 명령어를 활용한다.

  ```bash
  $ python manage.py migrate articles
  $ python manage.py migrate articles 0001
  ```

* 특정 마이그레이션 파일이 데이터베이스에 반영될 때 실행되는 쿼리문은 다음과 같이 확인할 수 있다.

  ```bash
  $ python manage.py sqlmigrate articles 0001
  BEGIN;
  --
  -- Create model Article
  --
  CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
  COMMIT;
  ```

* 데이터베이스에 테이블을 만들 때, 기본적으로 `app이름_model이름` 으로 생성된다.

## 3. Django Query Methods

> Django ORM을 활용하게 되면, 파이썬 객체 조작으로 데이터베이스 조작이 가능하다.
>
> ORM(Object-Relational-Mapping)에서는 주로 활용되는 쿼리문들이 모두 method로 구성되어 있다.

```bash
$ python manage.py shell
$ python manage.py shell_plus
```

* `shell` 에서는 내가 활용할 모델 import 해야 한다.

  ```python
  from articles.models import Article
  ```

* `shell_plus` 는 `django+extensions` 를 설치 후 `INSTALLED_APPS` 에 등록하고 활용해야 한다.

  ```bash
  $ pip install django-extensions
  ```

  ```python
  # crud/settings.py
  INSTALLED_APPS = [
      'django_extensions',
      ...
  ]
  ```

  

### 1. Create

```python
# 1. 인스턴스 생성 및 저장
article = Article()
article.title = '1번글'
article.content = '1번내용'
# article = Article(title='글', content='내용')
article.save()

# 2. create 메서드 활용
article = Article.objects.create(title='글', content='내용')
```

* 데이터베이스에 저장되면, `id` 값이 자동으로 부여된다. `save()` 호출하기 전에는 `None` 이다.

### 2. Read

* 모든 데이터 조회

  ```python
  Article.objects.all()
  ```

  * 리턴되는 값은 `QuerySet` 오브젝트
  * 각 게시글 인스턴스들을 원소로 가지고 있다.

* 특정(단일) 데이터 조회

  ```python
  Article.objects.get(pk=1)
  ```

  * 리턴되는 값은 `Article` 인스턴스
  * `.get()` 은 그 결과가 여러개 이거나 없는 경우 오류를 발생시킴.
  * 따라서, 단일 데이터 조회시(Primary Key를 통해)에만 사용한다.

* 특정 데이터 조회

  ```python
  Article.objects.filter(title='제목1')
  Article.objects.filter(title__contains='단어') # '단어'가 들어간 제목
  Article.objects.filter(title__endswith='단어') # '단어'로 끝나는 제목
  ```

  * 리턴되는 값은 `QuerySet` 오브젝트
  * `.filter()` 는 없는 경우/하나인 경우/여러개인 경우 모두 `QuerySet` 리턴

### 3. Update

```python
article = Article.objects.get(pk=1)
article.content = '내용 수정'
article.save()
```

* 수정은 특정 게시글을 데이터베이스에서 가져와서 인스턴스 자체를 수정한 후 `save()` 호출.

### 4. Delete

```python
article = Article.objects.get(pk=1)
article.delete()
```

### 5. 기타

#### 1. Limiting

```python
Article.objects.all()[0] # LIMIT 1 : 1개만
Article.objects.all()[2] # LIMIT 1 OFFSET 2
Article.objects.all()[:3]
```

#### 2. Ordering

```python
Article.objects.order_by('-id') # id를 기준으로 내림차순 정렬
Article.objects.order_by('title') # title을 기준으로 오름차순 정렬
```

## 4. Set URL namespace

### 1. app_name 추가 (articles/urls.py)

```python
app_name = 'articles' # app_name 추가

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/update/', views.update, name='update'),
]
```

* `app_name` 을 만들어준 후에 각각의 `urlpatterns`의  `path` 에 `name` 을 설정

### 2. App_name으로 Url을 표시하는 법

```python
# 바꾸기전
return redirect(f'/articles/{article.pk}/')
# 바꾼 후
return redirect('articles:detail', article.pk)
```

## 5. Django Authentication

> * 장고는 User 관련 기능이 내부적으로 있다.
>
>   -> 가져다가 쓰면 됨.
>
> * django.contrib.auth.models.User 변경할 상황에서
>
>   -> 상속받아서 내가 만들면 됨
>
>   -> DB와 연결되어있음. 다 바꿔야함 나중에
>
>   -> 프로젝트 만들면서 미리해라: django 추천!!
>
>   -> 바꿨는데. 그러면 장고 내부에서 어떻게 알지? -> settings 설정의 AUTH_USER_MODEL
>
>   -> User 클래스를 어떻게 가져다 쓰는데? -> get_user_model(): settings 설정을 봄.
>
> * models.py에서도 get_user_model() 쓸 수 있음?
>
>   -> 아닐 수 있다 . 장고가 명령어를 수행할 때, INSTALLED_APPS -> models / apps
>
>   -> User 클래스가 아직 없을 수 있다. (이름)
>
>   -> 그땐 그냥 settings.AUTH_USER_MODEL로 문자열을 찍어놓으면, 알아서 바꿔준다.
>
> * 근데 왜 갑자기 UserCreationForm 못씀?
>
>   -> 실제로 내부 코드 보면 바보 같이 User를 그대로 import해서 씀
>
>   (from django.contrib.auth.models import User)
>
>   -> 혼나야함. get_user_model()로 써야하는데
>
>   -> 그럼 어떻게 바꾼다? -> 상속 받아서 덮어쓰자
>
> ! 프로젝트 시작하면 User 모델 빼자.
>
> 	User 클래스가 필요하면, get_user_model()  호출해서 쓰자.
> 	
> 	models.py에서만 settings.AUTH_USER_MODEL 쓰자.

### 1. 'User' Class

> django에서는 프로젝트를 시작할 때, 항상 `User` Class를 직접 만드는 것을 추천함! [링크]()
>
> django의 기본 Authentication과 관련된 설정 값들을 활용하기 위해 `accounts`앱으로 시작하는 것을 추천함! (예 - LOGIN_URL = '/accounts/login/')

1. models.py

   ```python
   # accounts/models.py
   from django.contrib.auth.models import AbstractUser
   
   class User(AbstractUser):
       pass
   ```

   * django 내부에서 `User`를 기본적으로 사용한다. 예) `python manage.py createsuperuser`
   * 확장 가능성(변경)을 위해 내가 원하는 앱에 class를 정의!
   * `User` 상속 관계 [Github 링크]() [공식문서 링크]()
     * `AbstactUser`: `username`, `last_name`, `first_name`, `email`, ...
     * ``AbstactBaseUser`: `password`, `last_login`
     * `models.Model`

2. `settings.py`

   ```python
   # project/settings.py
   
   AUTH_USER_MODEL = 'accounts.User'
   ```

   * `User` 클래스를 활용하는 경우에는 `get_user_model()` 을 함수를 호출하여 사용한다.

     ```python
     # accounts/forms.py
     from django.contrib.auth import get_user_model
     
     class CustomUserCreationForm(UserCreationForm):
         class Meta:
             model = get_user_model()
     ```

     

   * 단, `models.py` 에서 사용하는 경우에는 `settings.AUTH_USER_MODEL` 을 활용한다.

     ```python
     # articles/models.py
     
     class Article(models.Model):
         user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     ```

3. `admin.py`

   * admin 페이지를 활용하기 위해서는 직접 작성을 해야 한다.

   * `UserAdmin` 설정을 그대로 활용할 수 있다.

     ```python
     # account/admin.py
     from django.contrib.auth.admin import UserAdmin
     from .models import User
     
     admin.site.register(User, UserAdmin)
     ```

     

### 2. Authentication Forms

#### 1. `UserCreationForm` - `ModelForm`

* custom user를 사용하는 경우 직접 사용할 수 없음.
  * 실제 코드 상에 `User`가 직접 `import` 되어 있기 때문. [Github 링크]()

```python
# accounts/forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm 

class CustomUserCreationForm(UserCreationForm):
     class Meta:
        model = get_user_model()
        fields = ('username',)
```

* `ModelForm` 이므로 활용 방법은 동일하다.

#### 2. `UserChangeForm` - `ModleForm`

* custom user를 사용하는 경우 직접 사용할 수 없음.
* 그대로 활용하는 경우 `User`와 관련된 모든 내용을 수정하게 됨.
  * 실제 코드 상에 필드가 `'__all__'` 로 설정되어 있음. [Github 링크]()

```python
# accounts/forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm 

class CustomUserCreationForm(UserChangeForm):
     class Meta:
        model = get_user_model()
        fields = ('username',)
```

#### 3. `AuthenticationForm`

* `ModelForm` 이 아님! **인자 순서를 반드시 기억하자!**
* `AuthenticationForm(request, data, ...)`

```python
form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
```

* 로그인에 성공한 `user`의 인스턴스는 `get_user()` 메소드를 호출하여 사용한다.
* 실제 로그인은 아래의 함수를 호출하여야 한다.

```python
from django.contrib.auth import login as auth_login
auth_login(request, user)
```



#### 4. `PasswordChangeForm`

* `ModelForm` 이 아님! **인자 순서를 반드시 기억하자!**
* `PasswordChangeForm(user, data)`

```python
if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.data)
else:
    form = PasswordChangeForm(request.user)
```

* 비밀번호가 변경이 완료된 이후에는 기존 세션 인증 내역이 바뀌어서 자동으로 로그아웃이 된다. 아래의 함수를 호출하면, 변경된 비밀번호로 세션 내역을 업데이트한다.

```python
from django.contrib.auth import update_session_auth_hash
update_session_auth_hash(request, form.user)
```

### 3. Appendix.import

```python
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstactUser
from django.contrib.auth.models import AbstactBaseUser
from django.contrib.auth.decorators import login_required
```

```python
from django.conf import settings
```

```python
from django.db import models # models.Model, models.CharField().....
from django import forms # forms.ModelForm, forms,Form
```

```python
from django.shortcut import render
from django.shortcut import redirect
from django.shortcut import get_object_or_404
from django.views.decorators.http import require_POST
```

## 6. M:N Many to many

### 1. 중개 모델

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

1. 예약 만들기

   ```shell
   d1 = Doctor.objects.create(name='kim')
   p1 = Patient.objects.create(name='taewoo')
   Reservation.objects.create(doctor=d1, patient=p1)
   ```

2. 1번 환자의 예약 목록

   ```shell
   p1.reservation_set.all()
   ```

3. 1번 의사의 예약 목록

   ```shell
   d1.reservation_set.all()
   ```

4. 1번 의사의 환자 목록

   * 지금 상태에서 바로 의사가 해당하는 환자들로 접근을 할 수는 없다.

   ```shell
   for r in d1.reservation_set.all():
   	print(r.patient)
   ```

### 2. 중개 모델(through 옵션)

> 의사 -> 환자들 / 환자 -> 의사들로 접근을 하기 위해서는 `ManyToManyField`를 사용한다.
>
> `Reservation` 모델을 활용하려면 `through` 옵션을 사용한다.
>
> `through` 옵션이 없으면, 기본적으로 `앱이름_patient_doctor`라는 이름의 테이블을 생성한다.

```python
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()
    doctor = models.ManyToManyField(Doctor, through='Reservation')

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

* 마이그레이션 파일을 만들거나 마이그레이트를 할 필요가 없다!
* 즉, 데이터베이스는 전혀 변경되는 것이 없다.

1. 1번 의사의 예약 목록

   ```shell
   d1.reservation_set.all()
   ```

2. 1번 의사의 환자 목록

   >`Doctor` 는 `Patient` 의 역참조이므로, naming convention에 따라 아래와 같이 접근

   ```shell
   d1.patient_set.all()
   ```

3. 1번 환자의 의사 목록

   * `Patient` 는 `Doctor` 는 직접 참조(`doctors`)하므로, 아래와 같이 접근!

   ```shell
   p1.doctors.all()
   ```

### 2.1. `related_name`

```shell
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()
    doctor = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

* 역참조시 `related_name` 옵션으로 직접 설정할 수 있다.
  * 설정하지 않으면 기본적으로 `Model명_set` 으로 된다.
* 반드시 설정할 필요는 없지만, 필수적인 상황이 발생할 수 있다.
  * 예) `User` - `Article`
* 따라서, `ManyToManyField`를 쓸 때에는 항상 `related_name`을 설정하고, 모델의 복수형으로 표기하자.

1. 1번 의사 환자 목록

   ```shell
   d1.patient.all()
   ```

### 3. 중개 모델 없이 작성

```python
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()
    doctor = models.ManyToManyField(Doctor, related_name='patients')
```

* `앱이름_patient_doctors` 로 테이블이 자동으로 생성된다.
* 별도의 칼럼이 필요 없는 경우는 위와 같이 작성한다.
* 만약, 예약시 추가정보 (예 - 시간, 담당자, ...)를 담기 위해서라면 반드시 중개 모델이 필요하다!

1. 예약 생성

   ```shell
   d2 = Doctor.object.create(name='Kim')
   p2 = Patient.object.create(name='Kim')
   
   d2.patients.add(p2)
   ```


## 7.

```python
user.like_articles.all() # related_name (M2M)
# => Queryset (Article instance 담겨있는)
user.article_set.all() # related_name X (FK 1:N)
# => Queryset (Article instance 담겨있는)
article.user # FK (1:N)
# => User instance
article.like_users.all() # M2M
# => Queryset (User instance 담겨있는)
```

```html
<p>{{ article.like_users.count }}명이 이 글을 좋아합니다.</p>
<h4>댓글 수: {{ article.comment_set.count }}</h4>
```

수업중 질문

1. login을 안하고 좋아요 버튼을 눌렀을때 오류가 나는 이유

   * `article.like_users.add(request.user)` 에 유저 정보가 아닌 임의의 user 객체가 들어가있는데 이 값은 pk값을 가지지 않으므로 오류가 발생하게 된다.

     -> `@login_required` 를 사용해서 예외처리를 해줘야함.

2. `@require_POST` \ `@login_required` 를 같이 써주면 에러가 발생하는 이유

   * POST URL을 사용하여 redirect 할 수는 없음.

     -> `@login_required` 대신 아래의 코드를 사용하여 예외처리

     ```python
     if request.user.is_authenticated:
         pass
     else:
         return HttpResponse('Unauthorized', status=401)
     ```