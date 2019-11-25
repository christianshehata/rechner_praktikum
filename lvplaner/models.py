from django.db import models


# Create your models here.

# Major = STUDIENRICHTUNG
# Subject = FACH
# Course = LV

# RELATIONS

# Student - Course 1 to n
# Subject - Major n to n
# Major - Student 1 to n
# Course - Student n to n


class Major(models.Model):
    major_name = models.CharField(verbose_name="Studienrichtung", max_length=30, primary_key=True)

    def __str__(self):
        return self.major_name


class Subject(models.Model):
    title = models.CharField(verbose_name="Fachbezeichung", primary_key=True, max_length=40)
    major_name = models.ForeignKey(Major, on_delete=models.PROTECT)

    def __str__(self):
        template = '{0.title}'
        return template.format(self)


class Student(models.Model):
    m_nr = models.IntegerField(max_length=8, verbose_name='Matrikelnummer', primary_key=True)
    first_name = models.CharField(verbose_name="Vorname", max_length=20)
    last_name = models.CharField(verbose_name="Nachname", max_length=20)
    major_name = models.ForeignKey(Major, on_delete=models.PROTECT)

    def __str__(self):
        template = '{0.first_name}, {0.last_name} ({0.m_nr}) - {0.major_name}'
        return template.format(self)


class Course(models.Model):
    course_id = models.IntegerField(max_length=4, verbose_name="LV-Nummer", primary_key=True)
    time = models.TimeField(verbose_name='Uhrzeit Beginn')
    end_time = models.TimeField(verbose_name='Uhrzeit Ende', default='18:30')
    date = models.DateField(verbose_name='Datum')
    lecturer = models.CharField(verbose_name='Dozent', max_length=40)
    subject_title = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self):
        template = '{0.course_id} - {0.subject_title}'
        return template.format(self)
