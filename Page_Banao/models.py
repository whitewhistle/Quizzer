from django.db import models


# Create your models here.
class Questions(models.Model):
    question_id = models.IntegerField()
    category = models.CharField(max_length=50)
    question_text = models.CharField(max_length=500)
    marks = models.IntegerField()
    answer = models.CharField(max_length=50)
    is_correct = models.BooleanField(default = False)


class Quizing(models.Model):
    quiz_id = models.IntegerField()
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE )







