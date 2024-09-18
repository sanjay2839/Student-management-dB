from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Student
from .forms import StudentForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render

def my_view(request):
    # Assuming you have logic to get the logged-in user
    logged_in_user = request.user  # Assuming you're using Django's authentication system
    context = {'logged_in_user': logged_in_user}
    return render(request, 'my_template.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'students/signup.html', {'form': form})

def return_base(request): return render(request, 'students/base.html')

def return_login(request): return render(request, 'students/login.html')

def login_view(request):
 return render(request, 'students/login.html')




def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      new_student = Student(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))

# def index(request):
#     # Get all students from the database
#     students = Student.objects.all()

#     # Check if the 'sort' parameter is passed in the URL
#     sort_by = request.GET.get('sort')

#     # Sort students based on CGPA if 'sort' parameter is 'cgpa'
#     if sort_by == 'cgpa':
#         students = students.order_by('-gpa')

#     return render(request, 'students/index.html', {
#         'students':Student.objects.new_gpa})

def logout(request):
    return redirect('http://127.0.0.1:8000/')