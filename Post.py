import requests
apiurl = "https://reqres.in/api/login"
todo = {
    "email": "eve.holt@reqres.in",
    "password": ""
}
response = requests.post(apiurl, json=todo)
print(response.json())
response.status_code

if response.status_code == 201 : 
    print("201 response: Created success")
    
elif response.status_code == 200 :
    print("200 response: OK success")
    
elif response.status_code == 400 :
    print("400: Bad Request")