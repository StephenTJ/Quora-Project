from django.shortcuts import render

# Create your views here.
def Login_Page(request):
    return render(request, 'login_page.html')