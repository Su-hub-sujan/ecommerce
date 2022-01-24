from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
     return render(request,'cart/index.html')

def about(request):
     return HttpResponse("hello this")
def contact(request):
     return HttpResponse("hello this is")
def tracker(request):
     return HttpResponse("hello this is  tracker")
def checkout(request):
     return HttpResponse("hello this is checkout")
def productview(request):
     return HttpResponse("hello this is product view")
def search(request):
     return HttpResponse("hello this is request")
