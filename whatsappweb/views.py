from django.shortcuts import render, redirect
from .forms import MessageForm, EmployeForm
from django.utils import timezone

def initial_page(request):
    return render(request, 'whatsappweb/initial_page.html')

def send_msg(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            created_at = timezone.now()
            return redirect('initial_page')
            
    else:
        form = MessageForm()    
    return render(request, 'whatsappweb/send_msg.html', {'form':form}) 

def new_employe(request):
    if request.method == "POST":
        form = EmployeForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            return redirect('initial_page')
            
        else:
            form = EmployeForm()    
        return render(request, 'whatsappweb/send_msg.html', {'form':form}) 
