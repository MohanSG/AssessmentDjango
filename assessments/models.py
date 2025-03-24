from django.db import models

# Create your models here.
class SchoolClass(models.Model):
    class_name = models.CharField(max_length=50)
    yearOfStudy = models.IntegerField()
    number_of_students = models.IntegerField()

    def __str__(self):
        return self.class_name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    assigned_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Parent(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Topic(models.Model):
    name = models.CharField(max_length=50)
    content_description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
