# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# Created with inspectdb

from django.db import models


class Admin(models.Model):
    authentication = models.ForeignKey('Authentication', models.DO_NOTHING)
    center_site = models.ForeignKey('CenterSite', models.DO_NOTHING)
    contact = models.ForeignKey('Contact', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin'


class Attendance(models.Model):
    id = models.OneToOneField('Batch', models.DO_NOTHING, db_column='id', primary_key=True)
    attended = models.IntegerField(blank=True, null=True)
    contact = models.ForeignKey('Contact', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attendance'


class Authentication(models.Model):
    user_name = models.CharField(max_length=45, blank=True, null=True)
    password_hash = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authentication'


class Batch(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    trainer_id_trainer = models.ForeignKey('Trainer', models.DO_NOTHING, db_column='trainer_id_trainer')
    term_period = models.ForeignKey('TermPeriod', models.DO_NOTHING)
    cost = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey('Course', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'batch'


class BatchHasPayment(models.Model):
    payment = models.ForeignKey('Payment', models.DO_NOTHING)
    student_in_batch = models.ForeignKey('StudentInBatch', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'batch_has_payment'


class CenterSite(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'center_site'


class Contact(models.Model):
    first = models.CharField(max_length=45, blank=True, null=True)
    government_id = models.CharField(max_length=45, blank=True, null=True)
    primary_email = models.CharField(max_length=255, blank=True, null=True)
    primary_phone = models.CharField(max_length=45, blank=True, null=True)
    nickname = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.first + ' (' + self.nickname + ')'

    class Meta:
        managed = False
        db_table = 'contact'


class Course(models.Model):
    subject = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Employer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employer'


class Exam(models.Model):
    name = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Course, models.DO_NOTHING)
    score_cut_off = models.IntegerField(blank=True, null=True)
    examcol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam'


class ExamResults(models.Model):
    id = models.OneToOneField('StudentInBatch', models.DO_NOTHING, db_column='id', primary_key=True)
    exam = models.ForeignKey(Exam, models.DO_NOTHING)
    student_has_course_student_id = models.PositiveIntegerField()
    student_has_course_course_id = models.PositiveIntegerField()
    score = models.IntegerField(blank=True, null=True)
    pass_field = models.IntegerField(db_column='pass', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'exam_results'


class Holidays(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    term_period = models.ForeignKey('TermPeriod', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'holidays'


class Payment(models.Model):
    amount = models.IntegerField(blank=True, null=True)
    received = models.DateField(blank=True, null=True)
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment'


class PaymentMethod(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'payment_method'


class Placement(models.Model):
    employer = models.ForeignKey(Employer, models.DO_NOTHING)
    student = models.ForeignKey('Student', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement'


class Student(models.Model):
    authentication = models.ForeignKey(Authentication, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)

    def __str__(self):
        return self.contact.__str__()

    class Meta:
        managed = False
        db_table = 'student'


class StudentInBatch(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING)
    course = models.ForeignKey(Batch, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student_in_batch'


class TermPeriod(models.Model):
    year = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=2, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'term_period'


class Trainer(models.Model):
    authentication = models.ForeignKey(Authentication, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'trainer'
