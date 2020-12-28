from django.db import models
from django.contrib.auth.models import UserManager

class Course(models.Model):
    courseid = models.CharField(primary_key=True,max_length=100)
    course_name = models.CharField(max_length=100)
    credit_hours = models.CharField(max_length=100)

    objects = UserManager()
    class Meta:
        db_table = "course"

class Student(models.Model):
    studentid = models.CharField(primary_key=True,max_length=100)
    student_first_name = models.CharField(max_length=100)
    student_last_name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    student_primary_emailid = models.CharField(max_length=100)
    class Meta:
        db_table = "student"

class Instructor(models.Model):
    instructorid = models.CharField(primary_key=True,max_length=100)
    instructor_first_name = models.CharField(max_length=100)
    instructor_last_name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    instructor_primary_emailid = models.CharField(max_length=100)
    class Meta:
        db_table = "instructor"

class StudentEnrolment(models.Model):
    #studentid = models.ForeignKey(Student, on_delete=models.CASCADE, primary_key=True)
    #courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    studentid = models.CharField(primary_key=True,max_length=100)
    courseid = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    class Meta:
        unique_together = (('studentid', 'courseid'),)
        db_table = "student_enrolment"

class InstructorEnrolment(models.Model):
    instructorid = models.CharField(primary_key=True,max_length=100)
    courseid = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    class Meta:
        unique_together = (('instructorid', 'courseid'),)
        db_table = "instructor_enrolment"
