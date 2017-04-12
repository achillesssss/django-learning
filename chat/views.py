from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.shortcuts import redirect

from .models import Message
from .forms import MessageForm, UserForm


def conversation(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    current_user = request.user
    users = User.objects.all()
    messages =  Message.objects.order_by('-created_date')
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.snder = request.user
            msg.created_date = timezone.now()
            msg.save()
            form = MessageForm()
            return render(request, 'chat/chat.html',{'msgs': messages, 'form': form, 'users': users})
    else:
        form = MessageForm()
    return render(request, 'chat/chat.html',{'msgs': messages,'form': form, 'users': users})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('conversation')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


