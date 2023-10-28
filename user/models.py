from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=20) # Поле и длина под вопросом
    photo = models.ImageField() #upload_to
    subs = models.ManyToManyField('user.User')
    likes = models.ManyToManyField('lesson.Lesson',
                                   related_name='liked_lessons')
    favorites = models.ManyToManyField('lesson.Lesson',
                                       related_name='favorite_lessons')

class History(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    lesson = models.ForeignKey('lesson.Lesson',
                               on_delete=models.CASCADE)
    # Одна запись - один урок в истории, легко сортировать по дате просмотра
    ########## Или
    # Одна запись - все уроки, не знаю как будет проходить сортировка по дате
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # lessons = models.ManyToManyField(Lesson)