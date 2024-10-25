from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    parent_contact = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    ATTENDANCE_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
