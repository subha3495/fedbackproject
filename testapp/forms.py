from django import forms
class FeedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError('the length of name filed should greate 4')
        return inputname
    def clean_rollno(self):
        inputrollno=self.cleaned_data['rollno']
        print('validating rollno')
        return inputrollno
    def clean_email(self):
        inputemail=self.cleaned_data['email']
        print('validating email')
        return inputemail
    def clean_feedback(self):
        inputfeedback=self.cleaned_data['feedback']
        print('validating feedback')
        return inputfeedback