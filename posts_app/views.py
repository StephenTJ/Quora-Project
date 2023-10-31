from django.shortcuts import render

def Home_Page(request):
    return render(request, 'home_page.html')

def Questions_Page(request):
    return render(request, 'questions_page.html')