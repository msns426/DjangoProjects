from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Admin, Trainers, Courses, Students, Attendance, AttendanceReport, LeaveReportStudent
from .models import LeaveReportTrainer, FeedBackStudent, NotificationStudent, NotificationTrainer,FeedBackTrainer


# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)

admin.site.register(Admin)
admin.site.register(Courses)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportTrainer)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackTrainer)
admin.site.register(NotificationStudent)
admin.site.register(NotificationTrainer)
