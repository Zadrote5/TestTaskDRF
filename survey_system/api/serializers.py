from django.db.models.query import QuerySet
from rest_framework import fields, serializers
from ..models import Survey, Question, Passing, Answer


# Сериализатор вопросов
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


# Сериализатор опросов
class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = '__all__'


# Сериализатор ответов
class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


# Сериализатор прохождение опроса
class PassingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passing
        fields = ['user', 'survey']
