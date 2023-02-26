from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.

posts=[
    {
        "id": 1,
        "tittle":"learn Django",
        "author":"okorie daniel"
    },
    {
        "id": 2,
        "tittle":"learn bootstrap",
        "author":"okorie daniel"
    },
    {
        "id": 3,
        "tittle":"learn html",
        "author":"okorie daniel"
    },
    
]


def index(request:HttpRequest):
    return HttpResponse("Hello World!")


def greet(request:HttpRequest):
    name = request.GET.get("name") or "World"
    
    return HttpResponse(f"Hello {name}")
    
def return_all_posts(request:HttpRequest):
    return HttpResponse(str(posts))

def return_one_post(request:HttpRequest, post_id):
    for post in posts:
        if post["id"] == post_id:
            return HttpResponse(str(post))
    
    return HttpResponse("Not found")