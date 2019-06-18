from django.shortcuts import render
from django.http import  HttpResponse
from appTwo.models import User
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    helpdict={'help_page': "HELP PAGE"}
    return render(request, 'appTwo/help.html', context=helpdict)
def users(request):
    user_List = User.objects.order_by('firstName')
    user_dict={'user_page': user_List}
    return render(request, 'appTwo/users.html', context=user_dict)
