# Day5

## Telegram API 활용하기

### 텔레그램 메시지 보내기

* 텔레그램 API의 기본 URL은 다음과 같다.

  ```python
  https://api.telegram.org/bot{token}/{method_name}
  ```

* 메시지 보내기

  ```python
  https://api.telegram.org/bot{token}/sendMessage
  ```

  * 필수 파라미터
    * `text` : 보낼 메시지 내용
    * `chat_id` : 사용자 id

  ```python
  import requests
  from decouple import config
  
  token = config('TELEGRAM_TOKEN')
  base_url = f'https://api.telegram.org/bot{token}'
  chat_id = #chat_id
  text = '안녕하세요'
  url =f'{base_url}/sendMessage?chat_id={chat_id}&text={text}'
  requests.get(url)
  ```

  * 주의사항!!! `token` 값은 별도의 환경변수로 관리해야 함.

    * `python-decouple` 설치

    ```bash
    $ pip install python-decouple
    ```

    * `.env` 파일 생성

      ```
      TELEGRAM_TOKEN='sdfasdfasdfdsafdsafdasfsadfsa'
      ```

    * `.gitignore` 에 추가

      ```
      .env
      ```

    * 활용

      ```python
      from decouple import config
      token = config('TELEGRAM_TOKEN')
      ```

## Telegram webhook 설정

`webhook` 은 텔레그램 서버에서 내가 설정한 서버의 url로 메시지를 전달해주는 설정을 뜻한다.

여기서 주의할 점은, 반드시 url이 `https` 가 설정되어야 하는데, 이를 위해서 개발 단계에서는 `ngrok` 를 설치하여 활용하자.

* `ngrok` 활용법

  * `ngrok.exe` 파일을 다운로드 받는다.

  * `cmd` 를 열어 해당 파일 경로로 이동한다.

  * 아래의 명령어를 입력한다.

    ```bash
    $ ngrok http 5000
    ```

* webhook url 설정

  아래의 텔레그램 API url에 요청을 보낸다.

  ```
  https://api.telegram.org/bot{token}/setwebhook?url={url}
  ```

  주의할 점은 `url` 을 전부 작성해야 한다. 

  요청은 크롬 주소창에 만들어진 URL을 입력하는 것으로 대체한다.

  예) `https://123.io/token실제값을여기에추가`

  

## Heroku 배포

`heroku` 는 무료로 서버에 배포하는 것을 도와주며 `https` 를 지원하여, 쉽고 빠르게 할 수 있다.

1. pip 패키지 정보 추가

   ```bash
   $ pip freeze > requirements.txt
   ```

2. `runtime.txt` 추가

   ```
   python-3.7.3
   ```

3. `procfile` 추가

   ```
   web: python app.py
   ```

4. `app.py` 변경

   ```python
   if __name__ == '__main__':
       import os
       port = int(os.environ.get("PORT", 5000))
       app.run(host = '0.0.0.0', debug=True)
   ```

5. `commit`

   ```bash
   $ git init
   $ git add .
   $ git commit -m 'init'
   ```

6. `heroku cli` 다운로드

   구글에 heroku cli를 검색하여 다운로드 한다.

7. heroku app 설정 - 최초에 한번

   ```bash
   $ heroku login
   $ heroku create __프로젝트 이름을 여기에 작성__ 
   ```

8. `push`

   ```bash
   git push heroku master
   ```

   

