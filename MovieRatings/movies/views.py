from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Movie
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    all_movies = Movie.objects.all()

    context = {
        'all_movies': all_movies,
    }

    return render(request, 'movies/index.html', context)

def search(request):
    all_movies = Movie.objects.all()

    context = {
        'all_movies': all_movies,
    }

    return render(request, 'movies/search.html', context)

# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'movies/register.html'
#
#     # display registration form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name,{'form':form})
#
#     # Add form data to database
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save(comit=False)
#
#             # clean up data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             # return user if credentials are good
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('movies:index')
#
#         return render(request, self.template_name, {'form': form})




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('movies:index')
    else:
        form = UserCreationForm()
    return render(request, 'movies/register.html', {'form': form})