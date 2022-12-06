from django.forms import ModelForm
from .models import userMessage


class UserMessageForm(ModelForm):
  class Meta:
    model = UserMessages
    fields=['heading','text_message','user']