from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    class Meta:
        ordering = ['-pub_date']
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    class Meta:
        ordering = ['votes']
    def __str__(self):
        return self.choice_text
