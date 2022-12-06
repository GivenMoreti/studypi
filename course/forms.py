from django.forms import ModelForm
from .models import Student
from .models import UserMessage


class StudentForm(ModelForm):
  class Meta:
    # line underneath select the corresponding class
    model = Student
    fields="__all__"
   
   

class UserMessageForm(ModelForm):
  class Meta:
    model = UserMessage
    fields="__all__"