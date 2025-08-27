from django.shortcuts import render

# Create your views here.

def welcome(request):
    
    return render(request,'welcome.html')

# 1. create the view function
# 2. add the view function to your urls.py
# 3. create the html file