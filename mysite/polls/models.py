from django.db import models

# Create your models here.

"""
Each model is represented by a class that subclasses django.db.models.Model
Models have class variables which represent a database field in the model
fields are instances of Field class. Name is used in python code and database column names
some fields have required arguments eg CharField requires max_length
Some fields have optional arguments eg. our votes field which is IntegerField has the optional field for default (which we set to 0)

This small chunk of model code tells django to
    create database schema- CREATE TABLE statements
    create a Python database-access api for accessing our Question and Choice objects
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #string method to make object representation a little more intuative
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #string method to make object representation a little more intuative
    def __str__(self):
        return self.choice_text