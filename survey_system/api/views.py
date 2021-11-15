from django.contrib.auth.models import User
from django.http import request
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import SurveySerializer, QuestionSerializer, PassingSerializer, AnswerSerializer
from ..models import Survey, Question, Passing

# По скольку нет базы с пользователями, запишу тестовый "токен авторизации администраатора" в переменную
SUCCESS_TOKEN = 'a437b15e363ad6cd401a0a87ce0e371710c6'


# Проверка авторизации
def check_auth(token):
    if token == SUCCESS_TOKEN:
        return True
    else:
        return False


# Класс обрабатывающий все api запросы приложения
class SurveysApiView(ListAPIView):

    # Метод создания опроса
    @api_view(('POST',))
    def create_survey(request):
        if check_auth(request.POST.get('token')):
            survey = SurveySerializer(data=request.data)
            if survey.is_valid():
                survey.save()
                return Response(status=201, data={
                    'message': 'Success'
                })
            else:
                return Response(status=404, data={
                    'message': 'Fail'
                })
        else:
            return Response(status=201, data={
                'message': 'fail auth'
            })

    # Метод создания вопроса
    @api_view(('POST',))
    def create_question(request):
        if check_auth(request.POST.get('token')):
            question = QuestionSerializer(data=request.data)
            if question.is_valid():
                question.save()
                return Response(status=201, data={
                    'message': 'Success'
                })
            else:
                return Response(status=404, data={
                    'message': 'Fail'
                })
        else:
            return Response(status=201, data={
                'message': 'fail auth'
            })

    # Метод удаления опроса
    @api_view(('GET',))
    def delete_survey(request):
        if check_auth(request.GET.get('token')):
            if request.GET.get('survey_id'):
                survey = Survey.objects.get(id=request.GET.get('survey_id'))
                survey.delete()
                return Response(status=201, data={
                    'message': 'Success'
                })
            else:
                return Response(status=404, data={
                    'message': 'Fail'
                })
        else:
            return Response(status=201, data={
                'message': 'fail auth'
            })
    # Метод изменения опроса
    @api_view(('GET',))
    def edit_survey(request):
        if check_auth(request.GET.get('token')):
            if request.GET.get('survey_id'):
                survey = Survey.objects.get(pk=request.GET.get('survey_id'))
                if request.GET.get('title'):
                    survey.title = request.GET.get('title')
                if request.GET.get('end_date'):
                    survey.title = request.GET.get('end_date')
                if request.GET.get('description'):
                    survey.title = request.GET.get('description')
                survey.save()
                return Response(status=201, data={
                    'message': 'success'
                })
            else:
                return Response(status=404, data={
                    'message': 'fail'
                })
        else:
            return Response(status=201, data={
                'message': 'fail auth'
            })

    # Метод изменения вопроса
    @api_view(('GET',))
    def edit_question(request):
        if request.GET.get('survey_id'):
            if check_auth(request.GET.get('token')):
                question = Question.objects.get(pk=request.GET.get('survey_id'))
                if request.GET.get('title'):
                    question.question = request.GET.get('question')
                if request.GET.get('answer_type'):
                    question.question = request.GET.get('answer_type')

                question.save()
                return Response(status=201, data={
                    'message': 'success'
                })
            else:
                return Response(status=201, data={
                    'message': 'fail auth'
                })
        else:
            return Response(status=404, data={
                'message': 'fail'
            })

    # Метод удаления вопроса
    @api_view(('GET',))
    def delete_question(request):
        if check_auth(request.GET.get('token')):
            if request.GET.get('question_id'):
                question = Question.objects.get(id=request.GET.get('question_id'))
                question.delete()
                return Response(status=201, data={
                    'message': 'Success'
                })
            else:
                return Response(status=404, data={
                    'message': 'fail'
                })
        else:
            return Response(status=201, data={
                'message': 'fail auth'
            })

    # Метод получения опроса
    @api_view(('GET',))
    def get_survey(request):
        survey = Survey.objects.all()
        if request.GET.get("survey_id"):
            survey = Survey.objects.get(pk=request.GET.get("survey_id"))
        if request.GET.get("survey_id"):
            survey = Passing.objects.get(pk=request.GET.get("user_id"))
        serializer = SurveySerializer(survey)
        return Response(serializer.data)

    # Метод получения прохождения опроса
    @api_view(('GET',))
    def get_passing(request):
        passing = Passing.objects.all()
        if request.GET.get("passing_id"):
            passing = Passing.objects.get(pk=request.GET.get("passing_id"))
        if request.GET.get("user_id"):
            passing = Passing.objects.get(pk=request.GET.get("user_id"))
        serializer = PassingSerializer(passing, many=True)
        return Response(serializer.data)

    # Метод создания прохождения  опроса
    @api_view(('POST',))
    def create_passing(request):
        passing = PassingSerializer(data=request.data)
        if passing.is_valid():
            passing.save()
            for item in request.data['answers']:
                answer = AnswerSerializer(data=item)
                if answer.is_valid():
                    answer.save()
            return Response(status=201, data={
                'message': 'Success'
            })
