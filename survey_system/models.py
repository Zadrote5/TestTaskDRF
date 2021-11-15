from django.db import models


# Модель опроса
class Survey(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата старта')
    end_date = models.DateTimeField(null=True, verbose_name='Дата окончания')
    description = models.TextField(null=True, max_length=1500, verbose_name='Описание')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


# Модель вопроса
class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField(max_length=500, verbose_name="Вопрос")
    answer_type = models.TextField(max_length=150, verbose_name="Тип ответа")

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question


# Прохождение опроса
class Passing(models.Model):
    user = models.IntegerField(unique=True, verbose_name='Уникальный номер пользователя')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос')


# Ответ на вопрос
class Answer(models.Model):
    passing = models.ForeignKey(Passing, on_delete=models.CASCADE, verbose_name='Прохождение опроса', related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    answer = models.TextField(max_length=500, verbose_name="Ответ")
