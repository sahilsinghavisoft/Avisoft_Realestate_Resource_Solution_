from django.shortcuts import render,HttpResponse

# Create your views here.
#view for homepage
def index(request):
   # return HttpResponse("this is home page")
    return render(request,'index.html')
#view for about
def about(request):
    return render(request,'about.html')
#view for prediction
def prediction(request):
       # return HttpResponse("this is home page")
    return render(request,'prediction.html')
#view for contact
def contact(request):
       # return HttpResponse("this is home page")
    return render(request,'contact.html')
