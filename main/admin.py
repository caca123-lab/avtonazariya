from django.contrib import admin
from .models import Question, Answer, TestResult

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['text', 'category']

@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'score', 'total_questions', 'created_at']