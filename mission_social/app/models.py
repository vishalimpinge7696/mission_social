from django.db import models
from django.contrib.auth.models import User

choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),

]


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, choices=choices, null=True)
    contact = models.IntegerField()

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'profile'
        verbose_name_plural = 'PROFILE'
        managed = True


choices2 = [
        ('Male', 'Male'),
        ('Female', 'Female'),

]


class UserProfile2(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, choices=choices2, null=True)
    contact = models.IntegerField()

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'profile2'
        verbose_name_plural = 'PROFILE2'
        managed = True