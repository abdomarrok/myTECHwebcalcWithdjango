from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request,"index.html")

def calc(request):
  try:
    res=request.POST.get('res')   
  except SyntaxError:
    pass
  except ValueError:
    pass
  finally:
    return HttpResponse(eval(res)) 
   

