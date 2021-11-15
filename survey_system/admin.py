from django.contrib import admin
from .models import Survey, Question, Answer, Passing


class QuestionInline(admin.StackedInline):
    model = Question


class SurveyAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [QuestionInline]


admin.site.register(Survey, SurveyAdmin)


class AnswerInline(admin.StackedInline):
    model = Answer


class PassingAdmin(admin.ModelAdmin):
    list_display = ("survey",)
    inlines = [AnswerInline]


admin.site.register(Passing, PassingAdmin)