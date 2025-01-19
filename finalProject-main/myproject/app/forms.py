from django import forms


class RegistrationForm(forms.Form):
    firstname=forms.CharField(label='firstname')
    lastname=forms.CharField(label='lastname')
    email= forms.EmailField(label='email')
    
class CreateventForm(forms.Form):
    date=forms.CharField(label='date')
    time=forms.CharField(label='time')
    location= forms.EmailField(label='location')
    description= forms.EmailField(label='description')
    email= forms.EmailField(label='email')
    

class TasksForm(forms.Form):
    task=forms.CharField(label='task')
    date=forms.CharField(label='date')
    email= forms.EmailField(label='email')
    
