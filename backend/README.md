# Back-end

## 목차

## SQL

### 1. SQL이란?

> **SQL(Structured Query Language)**

- SQL은 데이터를 보다 쉽게 검색하고 추가, 삭제, 수정 같은 조작을 할 수 있도록 고안된 컴퓨터 언어입니다.
- 관계형 데이터베이스에서 데이터를 조작하고 쿼리하는 표준 수단입니다.
- DML (Data Manipulation Language): 데이터를 조작하기 위해 사용합니다.
  INSERT, UPDATE, DELETE, SELECT 등이 여기에 해당합니다.
- DDL (Data Definition Language): 데이터베이스의 스키마를 정의하거나 조작하기 위해 사용합니다.
  CREATE, DROP, ALTER 등이 여기에 해당합니다.
- DCL (Data Control Language) : 데이터를 제어하는 언어입니다.
  권한을 관리하고, 테이터의 보안, 무결성 등을 정의합니다.
  GRANT, REVOKE 등이 여기에 해당합니다.

### 2. MySQL

#### MySQL 설치

##### Window10에서 MySQL 설치하기

1. 설치 프로그램 다운로드

   [https://www.mysql.com/downloads/](https://www.mysql.com/downloads/)

   ![download 1](./images/MySQL_download1.png)

   ![download 2](./images/MySQL_download2.png)

   ![download 3](./images/MySQL_download3.png)

2. 환경변수 설정

   ![env setting](./images/MySQL_download4.png)

#### Database 생성하기

* 콘솔에서 명령어 실행

  > MySQL 관리자 계정인 `root`로 데이터베이스 관리 시스템에 접속

  ```bash
  mysql -u root -p
  Enter password: ****
  ```

* Database 생성 (I)

  > 관리자 계정으로 MySQL에 접속했을 경우

  - Database 생성

    ```bash
    mysql> create database `DB이름`;
    ```

  * Database 사용자 생성과 권한 주기

    * Database를 생성했다면, 해당 데이터베이스를 사용하는 계정을 생성해야 합니다.
    * 또한, 해당 계정이 데이터베이스를 이용할 수 있는 권한을 줘야 합니다.
    * 아래와 같은 명령을 이용해서 사용자 생성과 권한을 줄 수 있습니다.
    ```bash
    '8.0ver 이상에서는 create user를 먼저 해줘야함'
    create user '계정이름'@'localhost' identified by '암호'; // '8.0이상'
    
    grant all privileges on db이름.* to '계정이름'@'localhost' with grant option;
    
    flush privileges;
    ```


    * db이름 뒤의 * 는 모든 권한을 의미한다.
    * `@’%’`

      * 어떤 클라이언트에서든 접근 가능하다는 의미
    * `@’localhost’`

      * 해당 컴퓨터에서만 접근 가능하다는 의미
    * `ALL PRIVILEGES`

      * 모든 권한 추가
      * `SELECT, INSERT, UPDATE, DELETE, ... ` 으로 일부분만 추가 가능
    * `flush privileges` 

        * DBMS에게 적용
    * 해당 명령을 반드시 실행해줘야 합니다.
