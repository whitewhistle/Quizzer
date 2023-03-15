from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category_name

class Questions1(BaseModel):
    category_name = models.ForeignKey(Category,related_name='category' ,on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.question

class Answer(BaseModel):
    questions = models.ForeignKey(Questions1 ,related_name='questions_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)
    is_correct = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.answer






    