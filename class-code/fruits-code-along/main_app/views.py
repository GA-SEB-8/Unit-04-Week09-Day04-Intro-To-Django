from django.shortcuts import render

# Create your views here.

def welcome(request):
    
    return render(request,'welcome.html')

# 1. create the view function
# 2. add the view function to your urls.py
# 3. create the html file



# Exercise 1:
'''
1. Create an about view in your views.py
2. Create a corresponding about.html file in the templates folder with the following:
    a. h1 with your name
    b. ol: of all the technologies you learned
3. Add the view in the urls.py
4. Test if the page loads when you go to /about
'''
