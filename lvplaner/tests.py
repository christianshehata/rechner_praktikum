from django.test import TestCase
from django.utils import timezone

# Create your tests here.

from .models import Subject, Major, Student, Course
from django.urls import reverse


# MODEL TESTING

class MajorModelsTests(TestCase):
    @staticmethod
    def test_major_creation():
        major = Major.objects.create(
            major_name='BW'
        )

    def test_string_representation(self):
        major = Major(major_name='WINF')
        self.assertEqual(str(major), major.major_name)


class SubjectModelsTests(TestCase):
    @staticmethod
    def test_subject_creation():
        major = Major.objects.create(major_name='BW')
        Subject.objects.create(
            title='Finanzierung',
            major_name=major
        )

    def test_string_representation(self):
        major = Major.objects.create(major_name='BW')
        subject = Subject(title='Finanzierung', major_name=major)
        self.assertEqual(str(major), major.major_name)


class StudentModelsTests(TestCase):
    @staticmethod
    def test_subject_creation():
        major = Major.objects.create(major_name='BW')
        Student.objects.create(
            m_nr='01607903',
            first_name='Christian',
            last_name='Shehata',
            major_name=major
        )


class CourseModelsTest(TestCase):
    @staticmethod
    def test_subject_creation():
        major = Major.objects.create(major_name='BW')
        subject = Subject.objects.create(title='Soziale Kompetenz', major_name=major)
        Course.objects.create(
            course_id='1245',
            time='13:30:00',
            end_time='14:30:00',
            date='2020-11-03',
            lecturer='Shehata',
            subject_title=subject
        )
