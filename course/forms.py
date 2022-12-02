from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
  class Meta:
    # line underneath select the corresponding class
    model = Student
    fields="__all__"
    # widgets={
    #   'student_name': forms.TextInput(attrs={'class': 'form-control'}),
    # }
