from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name=models.CharField(max_length=30)
    dept_seats=models.IntegerField()

    def __str__(self):
        return f'{self.dept_name},{self.dept_seats}'

class Student(models.Model):
    Dept_stud=models.ForeignKey(Department,on_delete=models.CASCADE)
    stu_rn=models.IntegerField()
    stu_name = models.CharField(max_length=30)
    stu_marks = models.FloatField()

    def __str__(self):
        return f'{self.stu_rn},{self.stu_name},{self.stu_marks}'


class Lecturer(models.Model):
    Dept_lec= models.ManyToManyField(Department)
    name=models.CharField(max_length=30)
    salary=models.FloatField()






































