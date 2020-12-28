from django.shortcuts import render
from university.models import Student, StudentEnrolment, Course, Instructor, InstructorEnrolment
from django.http import HttpResponse, HttpResponseRedirect
import logging
logger = logging.getLogger("mylogger")


def loadcourseids():
    courses = Course.objects.all().order_by('courseid')
    print('Im in loadcourseids function')
    return courses

def redirect_login(request):
    print('In Redirect Login \n')
    id = request.POST.get("id")
    print('id', id, '\n')
    #request.user.is_authenticated = True
    if request.user is not None:
        if (id.startswith("I")):
            return show_instructor_data(request)
        else:
            return show_student_data(request)

def show_student_data(request):
    #id = request.POST.get("id")
    student_results = Student.objects.get(studentid='S001')
    student_enrolment_results = StudentEnrolment.objects.all().order_by('-year').order_by('-term')
    course_results__in = Course.objects.filter(courseid__in = StudentEnrolment.objects.values('courseid')).order_by('courseid')
    courses = loadcourseids()

    #return render(request, 'student.html')
    return render(request,'student.html',{"student_data":student_results, "student_enrolment": student_enrolment_results, "course": course_results__in, "courses": courses})

def show_instructor_data(request):
    instructor_results = Instructor.objects.get(instructorid='I001')
    instructor_enrolment_results = InstructorEnrolment.objects.all().order_by('-year').order_by('-term')
    course_results__in = Course.objects.filter(courseid__in = InstructorEnrolment.objects.values('courseid')).order_by('courseid')
    courses = loadcourseids()

    #return render(request, 'student.html')
    return render(request,'instructor.html',{"instructor_data":instructor_results, "instructor_enrolment": instructor_enrolment_results, "course": course_results__in, "courses": courses})


def delete_student_enrolment(request, sid, cid):
    print('Im here:')
    logger.info("Whatever to log")
    s = StudentEnrolment.objects.filter(studentid=sid, courseid=cid).delete()

    student_results = Student.objects.get(studentid='S001')
    student_enrolment_results = StudentEnrolment.objects.all().order_by('-year').order_by('-term')
    course_results__in = Course.objects.filter(courseid__in = StudentEnrolment.objects.values('courseid'))
    courses = loadcourseids()

    #return HttpResponse('<h1>This is a test page with sid {} and cid {}</h1>'.format(sid, cid))
    return render(request,'student.html',{"student_data":student_results, "student_enrolment": student_enrolment_results, "course": course_results__in, "courses": courses})

def delete_instructor_enrolment(request, iid, cid, term, year):
    print('Im here:')
    logger.info("Whatever to log")
    s = InstructorEnrolment.objects.filter(instructorid=iid, courseid=cid, term=term, year=year).delete()

    instructor_results = Instructor.objects.get(instructorid='I001')
    instructor_enrolment_results = InstructorEnrolment.objects.all().order_by('-year').order_by('-term')
    course_results__in = Course.objects.filter(courseid__in = InstructorEnrolment.objects.values('courseid')).order_by('courseid')
    courses = loadcourseids()

    #return HttpResponse('<h1>This is a test page with sid {} and cid {}</h1>'.format(sid, cid))
    return render(request,'instructor.html',{"instructor_data":instructor_results, "instructor_enrolment": instructor_enrolment_results, "course": course_results__in, "courses": courses})


def update_student_email(request):
    print('In Update Email \n')
    eid = request.POST.get("email_editable")
    s = Student.objects.get(studentid='S001')
    s.student_primary_emailid = eid
    print('eid', eid)
    s.save()

    student_results = Student.objects.get(studentid='S001')
    student_enrolment_results = StudentEnrolment.objects.all().order_by('-year').order_by('-term')
    course_results__in = Course.objects.filter(courseid__in = StudentEnrolment.objects.values('courseid'))
    courses = loadcourseids()

    return render(request,'student.html',{"student_data":student_results, "student_enrolment": student_enrolment_results, "course": course_results__in, "courses": courses})

def update_instructor_email(request):
    print('In Update Email \n')
    eid = request.POST.get("email_editable")
    s = Instructor.objects.get(instructorid='I001')
    s.instructor_primary_emailid = eid
    print('eid', eid)
    s.save()

    instructor_results = Instructor.objects.get(instructorid='I001')
    instructor_enrolment_results = InstructorEnrolment.objects.all().order_by('-year').order_by('-term')
    course_results__in = Course.objects.filter(courseid__in = InstructorEnrolment.objects.values('courseid')).order_by('courseid')
    courses = loadcourseids()

    return render(request,'instructor.html',{"instructor_data":instructor_results, "instructor_enrolment": instructor_enrolment_results, "course": course_results__in, "courses": courses})


def add_student_enrolment(request):
    print('Im here:')
    cid = request.POST.get("courseid")
    semester = request.POST.get("semester")
    term = request.POST.get("term")
    year = request.POST.get("year")

    s = StudentEnrolment.objects.create(studentid='S001', courseid=cid, semester=semester, grade='',term=term, year=year)

    student_results = Student.objects.get(studentid='S001')
    student_enrolment_results = StudentEnrolment.objects.all().order_by('-year').order_by('-term')
    course_results__in = Course.objects.filter(courseid__in = StudentEnrolment.objects.values('courseid'))
    courses = loadcourseids()

    #return HttpResponse('<h1>This is a test page with sid {} and cid {}</h1>'.format(sid, cid))
    return render(request,'student.html',{"student_data":student_results, "student_enrolment": student_enrolment_results, "course": course_results__in, "courses": courses})


def add_instructor_enrolment(request):
    print('Im here:')
    cid = request.POST.get("courseid")
    term = request.POST.get("term")
    year = request.POST.get("year")

    s = InstructorEnrolment.objects.create(instructorid='I001', courseid=cid, term=term, year=year)

    instructor_results = Instructor.objects.get(instructorid='I001')
    instructor_enrolment_results = InstructorEnrolment.objects.all().order_by('-year').order_by('-term')
    course_results__in = Course.objects.filter(courseid__in = InstructorEnrolment.objects.values('courseid')).order_by('courseid')
    courses = loadcourseids()

    #return HttpResponse('<h1>This is a test page with sid {} and cid {}</h1>'.format(sid, cid))
    return render(request,'instructor.html',{"instructor_data":instructor_results, "instructor_enrolment": instructor_enrolment_results, "course": course_results__in, "courses": courses})
