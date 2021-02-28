from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pical_app/index.html')
    
def blog(request):
    return render(request,'pical_app/blog')

def blog_single(request):
    return render(request,'pical_app/blog-single.html')

def inner_page(request):
    return render(request,'pical_app/inner-page.html')

def ourworks(request):
    return render(request,'pical_app/ourworks-details.html')
