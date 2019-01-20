from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def AgeProfile(request):
	return HttpResponse("Age Profile page :)")

# def age(request):
# 	return HttpResponse("Age Profile page")