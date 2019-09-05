from django import forms
from .models import Message, Employe

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('text', 'recepient_no',)



class EmployeForm(forms.ModelForm):

    class Meta:
        model = Employe
        fields = ('name', 'designation', 'phone_no')