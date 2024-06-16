from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(null=True)

    def __str__(self):
        return self.name

class Intern(models.Model):
    name = models.CharField(max_length=50)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, related_name='interns')

    def __str__(self):
        return self.name
