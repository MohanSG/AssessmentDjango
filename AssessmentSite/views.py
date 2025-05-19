from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from assessments.models import Teacher, SchoolClass
# Create your views here.
class MyLoginView(LoginView):
    template_name= 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Enter your details"
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, "Incorrect username or password. Please try again.", "danger")
        return super().form_invalid(form)
    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect
        else: 
            context =  {"error" : "Invalid credentials"}
            print("context is",context)
            return render(request, 'registration/registration_form.html', context)
    else:
        context = {"message" : "Enter your details"}
        print(context)
        return render(request, "registration/login.html", context)

class MyRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('login')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid data entered, please check fields again", "danger")
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, "Registration successful! Please log in to continue")
        response = super().form_valid(form)
        Teacher.objects.create(user=self.object, name="name", assigned_class = SchoolClass.objects.get(id=1))
        return response