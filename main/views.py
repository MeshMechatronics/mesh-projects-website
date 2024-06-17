from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Material, Company, Project
from .forms import LoginForm
from .forms import QuoteForm, CompanyForm, ProjectForm, ProjectDetailForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    return render(request, 'main/index.html')

@login_required
def materials(request):
    if request.method == 'POST' and request.user.role == 'admin':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        Material.objects.create(name=name, quantity=quantity)
    materials = Material.objects.all()
    return render(request, 'main/material_list.html', {'materials': materials})

@login_required
def create_quote(request):
    return render(request, 'main/create_quote.html')

# @login_required
# def projects(request):
#     companies = Company.objects.all()
#     return render(request, 'main/projects.html', {'companies': companies})


@login_required
def projects(request):
    companies = Company.objects.all()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = CompanyForm()
    return render(request, 'main/projects.html', {'companies': companies, 'form': form})

@login_required
def company_projects(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    projects = Project.objects.filter(company=company)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.company = company
            project.save()
            return redirect('company_projects', company_id=company_id)
    else:
        form = ProjectForm()

    return render(request, 'main/company_projects.html', {'company': company, 'projects': projects, 'form': form})

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectDetailForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectDetailForm(instance=project)
    return render(request, 'main/project_detail.html', {'project': project, 'form': form})

def create_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Oluşturulan teklif başarıyla kaydedildiğinde anasayfaya yönlendir
    else:
        form = QuoteForm()
    return render(request, 'main/create_quote.html', {'form': form})

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CompanyForm()
    return render(request, 'main/create_company.html', {'form': form})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'main/create_project.html', {'form': form})

def view_companies(request):
    companies = Company.objects.all()
    return render(request, 'main/view_companies.html', {'companies': companies})

def view_projects(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    projects = Project.objects.filter(company=company)
    return render(request, 'projects.html', {'company': company, 'projects': projects})


def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main/edit_project.html', {'form': form})
