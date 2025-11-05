from django.db import models


class Question(models.Model):
    text = models.TextField("Savol matni")
    image = models.ImageField(upload_to='questions/', blank=True, null=True)
    category = models.CharField("Kategoriya", max_length=100)

    def __str__(self):
        return self.text[:50]


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField("Javob matni", max_length=255)
    is_correct = models.BooleanField("To'g'ri javob", default=False)

    def __str__(self):
        return self.text


class TestResult(models.Model):
    user_name = models.CharField("Foydalanuvchi ismi", max_length=100)
    score = models.IntegerField("Ball")
    total_questions = models.IntegerField("Jami savollar")
    created_at = models.DateTimeField("Sana", auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.score}"