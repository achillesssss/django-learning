from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Message
from .forms import MessageForm

def conversation(request):
    current_user = request.user
    messages =  Message.objects.filter(snder=current_user).order_by('created_date')
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.snder = request.user
            msg.created_date = timezone.now()
            msg.save()
            form = MessageForm()
            return render(request, 'chat/chat.html',{'msgs': messages, 'form': form})
    else:
        form = MessageForm()
        # current_user = request.user
        # messages = 	Message.objects.filter(snder=current_user).order_by('created_date')
    return render(request, 'chat/chat.html',{'msgs': messages,'form': form})

