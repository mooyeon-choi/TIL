# Git

`Git`은 `분산형 버전관리시스템(DVCS)` 이다.

* window에서 `Git`을 사용하기 위해서는 `Git bash`를 반드시 설치해야 함.

* 참고자료
  * [Git Scm](https://git-scm.com/book/ko/v2)
  * [누구나 쉽게 이해할 수 있는 Git 입문](https://backlog.com/git-tutorial/kr/intro/intro1_1.html)

## Git 기본 명령어(로컬)

* 로컬에서 처음 Git을 활용하는 경우 아래의 설정을 해줘야 한다.

  ```bash
  $ git config --global user.name '<Github username>'
  $ git config --global user.email '<Github email>'
  ```

  커밋하는 사람(author)이 누구인지 설정! 

  Github email이랑 다르면, Github에서 다른 사람이 커밋한 것으로 인식됨!

  *컴퓨터에서 한번만 설정해주면 된다.*

1. Git 저장소 설정

   ```bash
   $ git init
   Initialized empty Git repository in C:/Users/student/Desktop/새 폴더/.git/
   
   student@DESKTOP MINGW64 ~/Desktop/새 폴더 (master)
   ```

   * `git init`명령어를 입력하면, 해당 디렉토리에 `.git/` 폴더가 생성된다.

   * 모든 git과 관련된 내용은 해당 폴더에 담겨있다.

   * 저장소로 설정되었다면, `git bash`에서 `(master)`가 나타난다.

     > `(master)`폴더 안에서 git init을 하면 `.git/`안에 또 다시 `.git/`이 생성되므로 하지 않는다.

2. Staging area(커밋 대상 목록)에 담기

   ```bash
   $ git add .
   $ git add a.txt
   $ git add startcamp/
   ```

   * `git add` 명령어를 통해 `Staging Area`로 특정 파일 혹은 폴더를 `commit`할 목록 `(staging area, INDEX)`에 담아놓는다.

   * 반드시 `git status` 명령어를 통해 내가 원하는 파일이 반영되었는지 확인한다.

     ```bash
     $ git status
     ...
     Changes to be committed:
       (use "git rm --cached <file>..." to unstage)
     
             new file:   a.txt
     ```

3.  이력 남기기(`commit`)

   ```bash
   $ git commit -m '커밋메시지'
   ```

   * `commit`은 현재 소스코드의 상태를 **스냅샷** 찍는 것과 동일하다.
   * `Staging Area`에 담겨있는 내용을 이력으로 남긴다.
   * 커밋메시지는 반드시 해당 이력의 내용을 정확하게 표현해야 한다. (보통 오픈소스프로젝트, 회사 내에서 관련된 컨벤션이 존재함.)

   

4. 커밋이력 확인하기

   ```bash
   $ git log
   commit 65d8afaf4c30c728175c7078d90c5df07ee58248 (HEAD -> master)
   Author: mooyeon-choi <dus1208@ajou.ac.kr>
   Date:   Tue Jul 9 11:05:03 2019 +0900
   
       테스트
   ```

   * `git log -n` 옵션을 주면, 최근 n개의 커밋을 보여준다.

   * 커밋 이력을 남긴 이후에 커밋 메시지 변경, 삭제 등을 할 수 있는데 이 경우는 매우 조심해야 한다!

      

5. **git 상태 확인**

   **항상 모든 명령어를 입력하기 전에 아래의 명령어를 입력하는 습관을 들이자!**

   ```bash
   $ git status
   ```



## Git 원격 저장소 활용하기

원격 저장소 (`remote repository`)는 `github`, `gitlab`, `bitbucket` 등 다양한 서비스를 활용할 수 있다.

> `github` : 오픈소스가 많다, 큰용량 업로드 불가
>
> `bitbucket` : 큰용량 업로드 가능

1. 원격 저장소(`remote repository`) 설정

   ```bash
   $ git remote add origin __https://github.com__
   ```

   * 로컬 저장소에 최초에 한번만 등록하면 된다.
   * `원격 저장소(remote)`를 `origin` 이라는 이름으로 정해진 `url`을 `등록(add)` 하는 것이다. 

2.  원격 저장소로 `push`

   ```bash
   $ git push origin master
   ```

   * `origin`으로 설정된 원격 저장소에 `push` 한다.