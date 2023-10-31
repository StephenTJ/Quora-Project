from django.db import models

class Question_Table(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    asked_by_user_id = models.IntegerField()  
    asked_by_user_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class Answer_Table(models.Model):
    answer_id = models.AutoField(primary_key=True)
    answer_text = models.TextField()
    answered_by_user_id = models.IntegerField()  
    answered_by_user_name = models.CharField(max_length=255)
    question_id = models.ForeignKey(Question_Table, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text

class Like_Table(models.Model):
    answer_id = models.ForeignKey(Answer_Table, on_delete=models.CASCADE)
    liked_by_user_id = models.IntegerField()  
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like for Answer {self.answer_id}"
