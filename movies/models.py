from audioop import reverse
from distutils.command.upload import upload
from django.db import models
from datetime import date
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=255, unique=True,db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Actor(models.Model):

    name = models.CharField("Имя", max_length=100)
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры и режисеры"
        verbose_name_plural = "Актеры и режисеры"

class Genre(models.Model):
    name = models.CharField("Имя", max_length=100)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Video(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Изображение", upload_to="images/movie_shots/", blank=True)
    
    file = models.FileField(
        upload_to="video/",
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])], 
        verbose_name="Путь к файлу", 
        unique=True
    )
    create_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

class Movie(models.Model):
    
    title =  models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    descriptions = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="images/movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="Режиссер", related_name="film_director")
    actor = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    world_premiere = models.DateField("Премьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="указывать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField("Сборы в сша", default=0, help_text="указывать сумму в долларах")
    fees_in_world = models.PositiveIntegerField("Сборы в мире", default=0, help_text="указывать сумму в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True, verbose_name="URL")
    video = models.ForeignKey(Video, verbose_name="Видео", on_delete=models.CASCADE, related_name="film_video")
    data_published = models.DateTimeField("Дата публикации", auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('film', kwargs={slug: self.url})


    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class RatingStar(models.Model):

    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"

class Rating(models.Model):

    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):

    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movies = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

