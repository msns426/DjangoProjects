from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from mysite.models import CustomUser, Courses, Trainers, Students, SessionModel, \
    FeedBackStudent, FeedBackTrainer, LeaveReportStudent, LeaveReportTrainer, Attendance, AttendanceReport
from .forms import AddStudentForm, EditStudentForm


def admin_home(request):
    all_student_count = Students.objects.all().count()
    course_count = Courses.objects.all().count()
    trainer_count = Trainers.objects.all().count()

    # Total Subjects and students in Each Course
    course_all = Courses.objects.all()
    course_name_list = []
    student_count_list_in_course = []

    for course in course_all:
        students = Students.objects.filter(course_id=course.id).count()
        course_name_list.append(course.course_name)
        student_count_list_in_course.append(students)

    trainer_attendance_list = []
    trainer_attendance_leave_list = []
    trainer_name_list = []

    trainers = Trainers.objects.all()
    for trainer in trainers:

        attendance = Attendance.objects.filter(course_id=course.id).count()
        leaves = LeaveReportTrainer.objects.filter(trainer_id=trainer.id, leave_status=1).count()
        trainer_attendance_list.append(attendance)
        trainer_attendance_leave_list.append(leaves)
        trainer_name_list.append(trainer.admin.first_name)

    # For Students
    student_attendance_list = []
    student_attendance_leave_list = []
    student_name_list = []

    students = Students.objects.all()
    for student in students:
        attendance = AttendanceReport.objects.filter(student_id=student.id, status=True).count()
        absent = AttendanceReport.objects.filter(student_id=student.id, status=False).count()
        leaves = LeaveReportStudent.objects.filter(student_id=student.id, leave_status=1).count()
        student_attendance_list.append(attendance)
        student_attendance_leave_list.append(leaves + absent)
        student_name_list.append(student.admin.first_name)

    context = {
        "all_student_count": all_student_count,
        "course_count": course_count,
        "trainer_count": trainer_count,
        "course_name_list": course_name_list,
        "student_count_list_in_course": student_count_list_in_course,
        "trainer_attendance_list": trainer_attendance_list,
        "trainer_attendance_leave_list": trainer_attendance_leave_list,
        "trainer_name_list": trainer_name_list,
        "student_attendance_list": student_attendance_list,
        "student_attendance_leave_list": student_attendance_leave_list,
        "student_name_list": student_name_list,
    }
    return render(request, "Admin/home_content.html", context)


def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        "user": user
    }
    return render(request, 'hod_template/admin_profile.html', context)


def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')





