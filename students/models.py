from django.db import models
from django.core.validators import MaxValueValidator


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(validators=[MaxValueValidator(99)])
    student_id = models.IntegerField(primary_key=True, validators=[
                                     MaxValueValidator(999999999)])

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self) -> str:
        return str(self.student_id)
