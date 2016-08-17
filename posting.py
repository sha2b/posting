import requests
payload={'value1':'value','value2':'value'}
r=requests.post("yourposturl",data=payload)

print r.url
print r.text
