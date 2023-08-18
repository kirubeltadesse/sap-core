from django.test import TestCase
from django.contrib.auth.models import User
from backend.models import Event, Category, Student
from django.utils import timezone


class TestCreateEvent(TestCase):

    @classmethod
    def setUpTestData(self):
        test_category = Category.objects.create(name='django')

        studentUser = User.objects.create_user(
            username='test_user1', password='123456789')

        mentorUser = User.objects.create_user(
            username='test_user2', password='123456789')

        # create some data for testing
        test_event = Event.objects.create(
            category_id=1, title='Event Title', content='Event Content', 
            slug='event-title', student =studentUser, mentor=mentorUser, 
            start_date = timezone.now(), end_date=timezone.now(), status='published')
        
    # do some testing
    def test_event_content(self):
        event = Event.eventobjects.get(id=1)
        category = Category.objects.get(id=1)
        student_user = User.objects.get(id=1)
        mentor_user = User.objects.get(id=2)
        self.assertEqual(f'{event.title}', 'Event Title')
        self.assertEqual(f'{event.content}', 'Event Content')
        self.assertEqual(f'{event.slug}', 'event-title')
        self.assertEqual(f'{event.student}', 'test_user1')
        self.assertEqual(f'{event.mentor}', 'test_user2')
        self.assertEqual(f'{event.status}', 'published')
        self.assertEqual(f'{category.name}', 'django')
        self.assertEqual(f'{student_user.username}', 'test_user1')
        self.assertEqual(f'{mentor_user.username}', 'test_user2')

        self.assertEqual(str(event), 'Event Title')
        self.assertEqual(str(category), 'django')

    def test_student(self):
        test_user = Student.objects.create(first_name='Robera',last_name='Melaek',email='email@gmail.com')
        username = Student.objects.get(id=1)
        assert(username.first_name,'Robera')





