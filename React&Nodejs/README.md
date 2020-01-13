# 1. 설치 및 환경설정

> PowerShell 과 Chocolatey를 사용하여

## 설치

### Chocolatey 설치

1. `choco -v` 를 입력하여 Chocolatey 가 설치되어 있는지 확인

   ```powershell
   C:\windows\system32>choco -v
   ```

2. `choco` 설치

   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString(‘https://chocolatey.org/install.ps1‘))
   ```

3.  `choco -v` 를 입력하여 설치 확인

   ```powershell
   C:\windows\system32>choco -v
   ```

### Node.js 설치

1. `node -v` 를 입력하여 Nodejs 가 설치되어 있는지 확인

   ```powershell
   C:\windows\system32>node -v
   ```

2. Nodejs 설치

   ```powershell
   choco install nodejs
   ```

3. `node -v`, `npm -v` 를 입력하여 Nodejs가 설치되어 있는지 확인

   ```powershell
   C:\windows\system32>node -v
   C:\windows\system32>npm -v
   ```

## VS Code 환경설정

### Extension 설치

* ESLint
* ES7 React/Redux/GraphQL/React-Native snippets
* Prettier - Code formatter
* Rainbow Breackets

# 2. React App, Base 생성

1. React App 생성

   ```bash
   npm install -g create-react-app
   ```

2. React Base 생성

   ```bash
   npx create-react-app react-base
   ```

   