from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=5)

    objects = models.Manager()

    def __str__(self):
        return str(self.name)
    
class Student(models.Model):
    name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)

    #Связь один ко многим, с таблицей ГРУППЫ
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.name} {self.group}"
    
class Mark(models.Model):
    
    MARK_CHOICES = [
        ('2', '2'),
        ('3', '3'), 
        ('4', '4'),
        ('5', '5'),
        ('зачет', 'Зачет'),
        ('незачет', 'Незачет')
    ]
    name = models.CharField(max_length= 50, choices=MARK_CHOICES, unique=True)

    def __str__(self):
        return self.name
    
class Discipline(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

# нужна промежуточная таблица(модель) студент - предмет
# сделать так, чтобы у студента по 1 предмету не могло быть по 20 орценок

class StudentDisciplineMark(models.Model):
    objects = models.Manager()

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'discipline'],
                name='unique_student_discipline'
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.mark} по {self.discipline}"



    