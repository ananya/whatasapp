from django.shortcuts import render
from .forms import MessageForm

def send_msg(request):
    form = MessageForm()
    return render(request, 'whatsappweb/send_msg.html', {'form':form}) 