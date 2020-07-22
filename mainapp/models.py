from django.db import models


class AbstractModel(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        properties = [f'{k}={v}' for k, v in self.__dict__.items() if not k.startswith('_')]
        return f'{self.__class__.__name__}({", ".join(properties)})'

    def __repr__(self):
        return str(self)


class Tag(AbstractModel):
    name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Название'
    )


class Author(models.Model):
    first_name = models.CharField(
        max_length=512,
        blank=True,
        verbose_name='name'
    )
    second_name = models.CharField(
        max_length=512,
        blank=True,
        verbose_name='second name'
    )
    description = models.TextField(
        blank=True,
        verbose_name='description'
    )
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    @property
    def full_name(self):
        return f'{self.first_name} {self.second_name}'


class Course(AbstractModel):

    class Levels(models.TextChoices):
        EASY = 'e'
        NORMAL = 'n'
        HARD = 'h'

    name = models.CharField(
        max_length=512,
        blank=True,
        verbose_name='название',
        unique=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='описание'
    )
    img = models.CharField(
        max_length=32,
        blank=True,
        verbose_name="фото",
    )
    price = models.IntegerField(
        null=False,
        verbose_name='цена',
        default=999
    )
    level = models.CharField(
        max_length=1,
        choices=Levels.choices,
        default=Levels.EASY
    )
    date = models.DateField(
        auto_created=True,
        verbose_name='дата создания'
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
