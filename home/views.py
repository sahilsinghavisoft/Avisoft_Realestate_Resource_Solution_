from django.shortcuts import render,HttpResponse
import joblib
model=joblib.load('static/RandomForestClassifier')
#model=joblib.load('static/LogisticRegression')
# Create your views here.
#view for homepage
def index(request):
   # return HttpResponse("this is home page")
    return render(request,'index.html')
#view for about
def about(request):
    return render(request,'about.html')
#view for contact
def contact(request):
       # return HttpResponse("this is home page")
    return render(request,'contact.html')
#view for prediction
def prediction(request):
       # return HttpResponse("this is home page")
    if request.method=='POST':
        Gender=int(request.POST.get('Gender'))
        Married=int(request.POST.get('Married'))
        Education=int(request.POST.get('Education'))
        Self_Employed=int(request.POST.get('Self_Employed'))
        Credit_History=int(request.POST.get('Credit_History'))
        Property_Area=int(request.POST.get('Property_Area'))
        ApplicantIncome=int(request.POST.get('ApplicantIncome'))
        print(Gender,Married,Education,Self_Employed,Credit_History,Property_Area,ApplicantIncome)
        pred=model.predict([[Gender,Married,Education,Self_Employed,Credit_History,Property_Area,ApplicantIncome]])
        print(pred)
        output={
            "output":pred
        }
        return render(request,'prediction.html',output)
    else:
        return render(request,'prediction.html',{'error_message': 'Please enter all details.'})

