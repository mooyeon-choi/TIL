import requests, json

url = '' // 요청 url

// data : json 형태로
data = json.dumps({
  })

// headers : dictionary 형태로
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
  }

r = requests.post(url, data = data, headers = headers).json()

print(r)