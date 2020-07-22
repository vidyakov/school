from django.test import TestCase, Client
from django.urls import reverse

from mainapp.models import Author, Tag


class AuthorCreationTests(TestCase):
    def setUp(self):
        python_tag = Tag(name='python_tag')
        python_tag.save()

    def dropDown(self):
        python_tag = Tag.objects.get(name='python_tag')
        python_tag.delete()

    def test_author_creation(self):
        python_tag = Tag.objects.get(name='python_tag')
        new_author = Author(
            first_name='Sasha',
            second_name='Vidyakov',
            description='Python Junior Web Developer',
            tag=python_tag
        )

        assert new_author.full_name == 'Sasha Vidyakov'


class AllCoursesViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status_code(self):
        response = self.client.get(reverse('main:index'))
        assert response.status_code == 200
