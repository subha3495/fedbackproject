from django.shortcuts import render
from .import forms
# Create your views here.
def thankyou_view(request):
        return render(request,'testapp/thankyou.html')
def feedback_view(request):
    if request.method=='GET':
        form=forms.FeedbackForm()
        return render(request,'testapp/fedback.html',{'form':form})
    if request.method=='POST':
        form=forms.FeedbackForm(request.POST)
        if forms.is_valid():
            print('Validation completed..... printing feedback info')
            print('students Name:',form.cleaned_data['name'])
            print('students Rollno:', form.cleaned_data['rollno'])
            print('students Email:', form.cleaned_data['email'])
            print('students Feedback:', form.cleaned_data['feedback'])
            return thankyou_view(request)
