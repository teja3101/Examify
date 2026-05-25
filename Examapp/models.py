from django.db import models

class Question(models.Model):
    qno = models.AutoField(primary_key=True)
    qtext = models.TextField()
    op1 = models.CharField(max_length=255)
    op2 = models.CharField(max_length=255)
    op3 = models.CharField(max_length=255)
    op4 = models.CharField(max_length=255)
    corr_answer = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.qtext
    
    
class CustomUser(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Result(models.Model):
    username = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + " - " + self.subject