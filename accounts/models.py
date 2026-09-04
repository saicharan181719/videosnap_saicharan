from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about=models.CharField(max_length=500)
    city=models.TextField(blank=True,null=True)
    state=models.TextField(blank=True,null=True)
    district=models.TextField(blank=True,null=True)
    profile_picture=models.ImageField(upload_to='profiles/',blank=True,null=True)

    def __str__(self):
        return self.user.username

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.college_name

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.company_name

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    def __str__(self):
        return self.skill_name

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    project_link = models.URLField(blank=True)
    def __str__(self):
        return self.project_name

class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    certificate_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)

    def __str__(self):
        return self.certificate_name

class Position(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    service_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.service_name}"

class CareerBreak(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    reason = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.reason}"

class Language(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    language_name = models.CharField(max_length=50)

    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('native', 'Native'),
    ]

    proficiency = models.CharField(
        max_length=20,
        choices=PROFICIENCY_CHOICES
    )

    def __str__(self):
        return f"{self.user.username} - {self.language_name}"

