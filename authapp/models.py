from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from mainapp.models import Tag


class SchoolUser(AbstractUser):
    class Sexes(models.TextChoices):
        MALE = 'm', _('Мужской')
        FEMALE = 'f', _('Женский')

    birth_date = models.DateField(verbose_name='День рождения', null=True)
    sex = models.CharField(verbose_name='Пол', choices=Sexes.choices, max_length=1)
    about_me = models.TextField(verbose_name='Про меня')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
