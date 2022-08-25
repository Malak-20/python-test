from urllib.request import urlopen,Request
from urllib.parse import urlencode
import json


def fetch_user(id):
    url=f"https://reqres.in/api/users/{id}"
    req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
    response=urlopen(req)
    data=json.loads(response.read())
    return data

def fetch_users(page,per_page):
    url=f"https://reqres.in/api/users?page={page}&per_page={per_page}"
    request=Request(url,headers={'User-Agent':'Mozilla/5.0'})
    response=urlopen(request)
    data=json.loads(response.read())
    return data
def create_user(first_name,last_name,email):
    data = {
        "first_name":first_name,
        "last_name":last_name,
        "email":email
    }

    url = "https://reqres.in/api/users"


    encoded_data = urlencode(data)
    post_data = encoded_data.encode("utf-8")

    request = Request(url,headers={'User-Agent':'Mozilla/5.0'},data=post_data)

    response = urlopen(request)

    data = json.loads(response.read())

    return data

print(fetch_user(7))
print(fetch_users(1,12))
print(create_user("malak","ghoul","mmalak@ghoull.com"))