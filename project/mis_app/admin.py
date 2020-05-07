from django.contrib import admin
from .models import *
# Register your models here.
[admin.site.register(c) for c in [
        Admin,
        Attendance,
        Authentication,
        Batch,
        BatchHasPayment,
        CenterSite,
        Contact,
        Course,
        Employer,
        Exam,
        ExamResults,
        Holidays,
        Payment,
        PaymentMethod,
        Placement,
        Student,
        StudentInBatch,
        TermPeriod,
        Trainer
]]