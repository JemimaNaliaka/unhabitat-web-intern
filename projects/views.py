from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Project
from django.db import models
from django import forms
from django.http import HttpResponse
from .forms import ProjectForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all()

    per_page = request.GET.get('per_page', 10)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 10

    paginator = Paginator(projects, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'per_page': per_page
    }
    return render(request, 'projects/project_list.html', context)
    


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')  
    else:
        form = ProjectForm(instance=project)

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def project_list_api(request):
    data = list(Project.objects.values())
    return JsonResponse(data, safe=False)


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list') 
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')  # Redirect to the list after deletion

    return render(request, 'projects/project_confirm_delete.html', {'project': project})

def my_view(request):
    from .models import Country  
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})


# --- CRUD VIEWS ---
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

#class ProjectDetailView(DetailView):
    #model = Project
    #template_name = 'projects/project_detail.html'
    #context_object_name = 'project'

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description', 'location', 'start_date', 'end_date']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')
        

class ProjectUpdateView(UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')


# --- DASHBOARD VIEW ---
def dashboard_view(request):
    total_projects = Project.objects.count()
    total_budget = Project.objects.all().aggregate(total=models.Sum('budget'))['total'] or 0

    return render(request, 'projects/dashboard.html', {
        'total_projects': total_projects,
        'total_budget': total_budget
    })


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'location', 'start_date', 'end_date']


    def clean(self):
        cleaned_data = super().clean()
        if 'budget' not in cleaned_data:
            cleaned_data['budget'] = 0.00
        return cleaned_data

def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})

# --- JSON API VIEW ---
    
class ProjectJsonView(View):
    def get(self, request):
        projects = list(Project.objects.values())
        return JsonResponse(projects, safe=False)
                                                                                        