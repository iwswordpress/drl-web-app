# from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse


def main(request):
    return render(request, 'main.html')


def predict(request):
    return HttpResponse('<h2 style="color:red">PREDICT</h2>')


def info(request):
    return HttpResponse('<h2 style="color:blue">Welcome to INFO...</h2>')
