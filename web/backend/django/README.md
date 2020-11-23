# Django

## 목차

* [시작하기](#시작하기)
* [작성흐름](#작성흐름)
* [Django CRUD](#django-crud)

## 시작하기

```bash
$ pip install django
```

* 현재 활용하고 있는 버전은 다음과 같다.
  * python 3.7.4
  * django 2.2.4

### 0. 가상환경 실행 + .gitignore!

> 가상환경을 사용하는 이유는 프로젝트마다 활용되는 라이브러리가 다르고, 동일한 라이브러리라도 버전이 다를 수 있다.
>
> 따라서, 프로젝트 하면서 라이브러리 삭제 혹은 변경을 하는 것이 아니라 각 프로젝트마다 독립된 가상환경을 부여하여 의존성을 없앤다.
>
> 항상 django 실행할 때마다 가상환경을 활성화 시키는 것을 습관화 하자!
>
> 추후에 DS/ML/DL(데이터사이언스/머신러닝/딥러닝) 학습 시에는 anaconda를 활용하기도 한다!

가상환경은 python에서 기본으로 제공하고 있는 [`venv`](https://docs.python.org/ko/3/tutorial/venv.html)를 활용한다.

1. 가상환경 생성

   원하는 디렉토리에서 아래의 명령어를 입력한다.

   ```bash
   $ python -m venv __venv__
   ```

   * `__venv__` 여기에 가상환경 이름을 작성하는데, 보통 `venv`라고 설정한다. (python 3.5+)
   * `__venv__` 폴더가 생성되는데, 구조는 다음과 같다.
     * `Lib` : 가상환경에 설치된 라이브러리 모음.
     * `Scripts` : 가상환경 실행과 관련된 파일

2. 가상환경 실행

   ```bash
   $ ls
   venv/ ...
   $ source venv/Scripts/activate
   (venv)
   $ python -V
   Python 3.7.4
   ```

   * 반드시 해당 명령어는 `venv` 폴더가 있는 곳에서 실행시킨다.
   * `bash shell` 에서는 `activate` 파일을 실행하여야 한다.
     * `cmd` : `activate.bat`
     * `power shell` : `activate.psl`

3. 가상환경 종료

   ```bash
   $ deactivate
   ```

4. `.gitignore` 등록

   ```shell
   venv/
   ```

   * 추가적으로 visual studio code를 활용하는 경우에는 `.vscode/`
   * python 환경에서는 `__pycache__`
   * pycharm 환경에서는 `.idea/`

   위의 폴더들은 `.gitignore` 에 등록하는 습관을 가지자! 잘 모르겠으면 [gitignore.io](https://gitignore.io)에서 찾아서 복사하자 :)

### 1. Django 프로젝트 시작

```bash
$ mkdir __프로젝트 이름/폴더 이름__
$ cd __프로젝트 이름/폴더 이름__
```



```bash
$ django-admin startproject __프로젝트이름__ .
```

* 프로젝트 이름으로 구성된 폴더와, `manage.py` 가 생성된다.
  * `__init__.py` : 해당 폴더가 패키지로 인식될 수 있게끔 작성 되는 파일
  * `settings.py` : **django 설정과 관련된 파일**
  * `urls.py` : **url 관리**
  * `wsgi.py` : 배포시 사용(web server gateway interface : 파이썬에서 사용되는 웹 서버 구성)
  * `manage.py` : **django 프로젝트와 관련된 커맨드라인(명령어) 유틸리티**

### 2. 서버실행

```bash
$ python manage.py runserver
```

* `localhost:8000` 으로 들어가서 로켓 확인!

### 3. App 생성

```bash
$ python manage.py startapp __app이름__
```

* `app 이름` 인 폴더가 생성되며, 구성하고 있는 파일은 다음과 같다.

  * `admin.py` : 관리자 페이지 설정

  * `apps.py` : app의 정보 설정. 직접 수정하는 경우 별로 없음.

  * `models.py` : **MTV - Model을 정의 하는 곳**

  * `tests.py` : 테스트 코드를 작성하는 곳.

  * `views.py` : **MTV - View를 정의 하는 곳.**

    * 사용자에게 요청이 왔을 때, 처리되는 함수

      ```python
      def index(request):
          return render(request, index.html)
      ```

**app을 만들고 나서 반드시 `settings.py` 에서 `INSTALLED_APPS`에 app을 등록한다.**

```python
# first_django/settings.py
#..
INSTALLED_APPS = [
    'pages',
    'django.contrib.admin',
    #...
]
#..
```

## 작성 흐름

### 1. URL 정의

```python
# first_django/urls.py
from pages import views

urlpatterns = [
    path('', views.index), # 항상 마지막에 ',' 를 적어준다
]
```

* `urls.py`는 우리의 웹 어플리케이션 경로들을 모두 관리한다.
* 요청이 들어오면 `urls.py` 의 `urlpatterns` 에 정의된 경로로 매핑한다.
* path(`경로`, `views에 정의된 함수`)

### 2. View 정의

```python
# pages/views.py

def index(request):
    return render(request, 'index.html')
```

* `views.py`는 MTV에서 View에 해당한다.
* 일종의 중간관리자로 Model, Template 등의 처리를 담당한다.



### 3. Template 정의

* 기본적으로 app을 생성하면, `templataes` 폴더가 없으므로 직접 생성해야 한다.

```html
<!-- pages/templates/index.html -->
<h1>
    장고 안녕!
</h1>
```



### 4. 서버 실행 및 확인

```bash
$ python manage.py runserver
```

`localhost:8000` 에서 확인 해보자!



### 5. 가상환경 새로 만들기 순서

1. 폴더 만들고

   ```bash
   mkdir __
   ```

2. 가상환경 만들고

   ```bash
   python -m venv venv
   ```

3. .gitignore에 venv/ 추가

4. 가상환경 실행 후

   ```bash
   source venv/Scripts/activate
   ```

5. 원하는 django 버전 설치

   ```bash
   pip install django
   ```

6. 프로젝트 생성

   ```bash
   django-admin startproject ____ .
   ```

7. app 생성 및 등록

8. url 설정

9. views.py 설정

10. templates 설정

11. 서버 실행

## Django CRUD

* [바로가기](./django-crud)