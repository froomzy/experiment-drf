from django.db import models


class Application(models.Model):
    user = models.ForeignKey(to='auth.User')
    year = models.IntegerField()
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    declaration = models.NullBooleanField(default=None)
    declaration_date = models.DateField()

    class Meta:
        unique_together = [('user', 'year',)]


class Qualification(models.Model):
    name = models.CharField(max_length=200)
    date_started = models.IntegerField()
    date_finished = models.IntegerField()

    class Meta:
        abstract = True


class EntranceQualification(Qualification):
    application = models.OneToOneField(to='application.Application')


class OtherQualification(Qualification):
    application = models.ForeignKey(to='application.Application')


# class Institution(models.Model):
#     name = models.CharField(max_length=200)
#     country = models.CharField(max_length=200)
