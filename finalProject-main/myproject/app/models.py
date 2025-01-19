from django.db import models
from django.core.mail import send_mail
from .utils import send_registration_email,send_createvent_email
 

class Events(models.Model):
  date = models.DateField()
  time= models.TimeField()
  location= models.CharField(max_length=200, blank=True, null=True)
  description= models.CharField(max_length=255, blank=True, null=True)
  email=models.CharField(max_length=255, blank=True, null=True)
 
        
  def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_createvent_email(self.email)

        
class Profile(models.Model):
  firstname = models.CharField(max_length=100, blank=True, null=True)
  lastname= models.CharField(max_length=100,blank=True,null=True)
  email= models.EmailField(max_length=200,blank=True,null=True)
  def __str__(self):
        return self.firstname
 
  def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_registration_email(self.email)







class Tasks(models.Model):
  task=models.CharField(max_length=100)
  date = models.DateField()
  email=models.EmailField()
  def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_tasks_email(self.email,self.task,self.date)







def send_tasks_email(email,task,date):
    subject = 'Your To-Do list'
    message = f'here you can see the tasks you have to manage before event:\n\
        {str(task)} and the date that you have to do it will be {str(date)} '
    from_email = 'eventsorojecttz@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)



