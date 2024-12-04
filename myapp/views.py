from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Part
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Aircraft
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import UserProfile
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            team = form.cleaned_data.get('team')
            UserProfile.objects.create(user=user, team=team)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
class PartListView(ListView):
    model = Part
    template_name = 'parts_list.html'
    context_object_name = 'parts'
# Create your views here.
# List all Aircrafts
class AircraftListView(ListView):
    model = Aircraft
    template_name = 'aircraft_list.html'
    context_object_name = "aircrafts"

# Create a new Aircraft
class AircraftCreateView(CreateView):
    model = Aircraft
    fields = ['name', 'type']
    template_name = "templates/aircraft_form.html"
    success_url = reverse_lazy('aircraft_list')

# View details of a specific Aircraft
class AircraftDetailView(DetailView):
    model = Aircraft
    template_name = 'aircraft_detail.html'

# Update an existing Aircraft
class AircraftUpdateView(UpdateView):
    model = Aircraft
    fields = ['name', 'type']
    template_name = 'aircraft_form.html'
    success_url = reverse_lazy('aircraft_list')

# Delete an Aircraft
class AircraftDeleteView(DeleteView):
    model = Aircraft
    template_name = 'aircraft_confirm_delete.html'
    success_url = reverse_lazy('aircraft_list')
    

    