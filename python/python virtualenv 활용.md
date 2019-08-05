# python virtualenv 활용

> 가상환경을 사용하는 이유는 패키지를 독립적으로 환경별로 관리하기 위해서이다.
>
> 예) A 프로젝트 : B패키지의 버전을 3.2 를 쓰는데, C 프로젝트 : B 패키지의 버전을 2.8을 쓰는 경우 매번 설치 / 삭제를 할 수 없으므로 독립된 가상환경을 만들어준다.
>
> 파이썬에서는 가상환경을 만들어주는 다양한 패키지들이 있는데 우리는 python에 내장되어있는 venv를 사용한다.

## 1. 가상환경 폴더 만들기

```bash
$ mkdir ~/내가원하는폴더위치
```

```bash
$ python -m venv ~/특정위치/버전명(혹은 가상환경 명)
```

해당 폴더를 열어보면, 아래와 같은 파일들이 있다.

```
activate	 # git bash용 (3.6+)
activate.bat # cmd용
activate.ps1 # power shell용
```

## 2. 가상환경 실행 및 종료

### 1. 실행

```bash
$ source ~/특정위치/버전명(혹은 가상환경명)/activate
(3.7.4) (버전명 혹은 가상환경명)
$
```

### 2. 종료

```bash
$deactivate
```

## Tip

`.bashre` 를 활용하면, 조금 더 편리하게 가상환경을 실행할 수 있다. 

`.bashre` 는 bash shell를 켜면 실행되는 스크립트이다. 윈도우에서 시작프로그램이랑 유사하다.

```bash
$ vi ~/.bashrc
```

vim을 통해서 수정이 가능하다. 편집 모드는 `i` 저장 및 종료는 `esc + :wq` 이다.

작성을 완료한 이후에는 새로 git bash 창을 열거나 아래의 명령어를 입력한다.

```bash
$ source ~/.bashrc
```

* 수업용 스크립트 파일

```shell
# ~/.bashrc
alias venv="source ~/python-virtualenv/3.7.4/Scripts/activate"
venv
```

