from django.core.management import BaseCommand
import factory

from mainapp.models import Tag, Author, Course


class TagFactory(factory.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker('word')


class AuthorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Faker('first_name')
    second_name = factory.Faker('last_name')
    description = factory.Faker('paragraph')
    tag = factory.SubFactory(TagFactory)


class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.Faker('first_name')
    description = factory.Faker('paragraph')
    img = factory.Faker('word')
    price = factory.Faker('pyint', min_value=500, max_value=2000)
    level = factory.Iterator([Course.Levels.EASY, Course.Levels.NORMAL, Course.Levels.HARD])
    date = factory.Faker('date')
    author = factory.SubFactory(AuthorFactory)
    tag = factory.SelfAttribute('author.tag')


class Command(BaseCommand):
    def handle(self, *args, **options):
        CourseFactory.create_batch(10)
