from django.shortcuts import render, redirect
from .models import Employee, Student, Attendance

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'management/employee_list.html', {'employees': employees})

def employee_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        designation = request.POST['designation']
        department = request.POST['department']
        contact = request.POST['contact']
        Employee.objects.create(name=name, designation=designation, department=department, contact=contact)
        return redirect('employee_list')
    return render(request, 'management/employee_register.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'management/student_list.html', {'students': students})

def student_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        grade = request.POST['grade']
        parent_contact = request.POST['parent_contact']
        address = request.POST['address']
        Student.objects.create(name=name, grade=grade, parent_contact=parent_contact, address=address)
        return redirect('student_list')
    return render(request, 'management/student_register.html')
