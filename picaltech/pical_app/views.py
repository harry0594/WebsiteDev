from django.shortcuts import render, HttpResponse
from pical_app.models import UserDetail

# Create your views here.
def index(request):
    if request.method =='POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(name,phone,email,message)
        ins = UserDetail(name=name,phone=phone,email=email,message=message )
        ins.save()
        print('Contact Details saved to database Successfully!')
        
    return render(request,'pical_app/index.html',{})


    
def blog(request):
    return render(request,'pical_app/blog')

def blog_single(request):
    return render(request,'pical_app/blog-single.html')

def inner_page(request):
    return render(request,'pical_app/inner-page.html')

def ourworks(request):
    return render(request,'pical_app/ourworks-details.html')
