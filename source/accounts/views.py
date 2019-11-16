from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             user = User(
#                 username=form.cleaned_data['username'],
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 email=form.cleaned_data['email']
#             )
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             # UserProfile.objects.create(user=user)
#             # login(request, user)
#             return redirect('webapp:index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'user_create.html', context={'form': form})

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'create_user.html', context={'form': form})