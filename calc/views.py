from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html',{'name': 'Mathan'})
"""
def add(request):
    result = int(request.GET['num1']) + int(request.GET['num2'])
    return render(request, 'result.html', {'result': result})

def mul(request):
    multied = int(request.GET['num1']) * int(request.GET['num2'])
    return render(request, 'result.html', {'multied': multied})
"""

#this function is written to have multiple submit buttons in single form or you can have individual methods
def cal(request):
    if 'add' in request.POST:
        result = int(request.POST['num1']) + int(request.POST['num2'])
        return render(request, 'result.html', {'result': result})
    elif 'multi' in request.POST:
        multied = int(request.POST['num1']) * int(request.POST['num2'])
        return render(request, 'result.html', {'multied': multied})
    elif 'divide' in request.POST:
        divided = float (int(request.POST['num1']) / int(request.POST['num2']))
        return render(request, 'result.html', {'divided': divided})
