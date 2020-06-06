from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index2(request):
    my_dict={'inserted_me':"Hey you did it again"}
    return render(request,'help_app/help.html',context=my_dict)
