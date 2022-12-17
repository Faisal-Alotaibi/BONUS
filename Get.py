import requests

apiurl = "https://reqres.in/api/users?page=2"

response = requests.get(apiurl)
response.status_code

if response.status_code == 200 : 
    print("200 response: OK")
    
elif response.status_code == 404 :
    print("404 response: Not Found")
    
elif response.status_code == 400 :
    print("400 response: Bad Request")