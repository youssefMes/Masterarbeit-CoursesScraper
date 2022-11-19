from django.db import models

class Information(models.Model):
    university = models.CharField(max_length=100)
    description = models.TextField(null=True)
    city = models.CharField(max_length=100)
    study_start = models.CharField(max_length=100, null=True)
    study_form = models.CharField(max_length=100, null=True)
    study_periode = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True)
    languages = models.CharField(max_length=100, null=True)
    other_informations = models.JSONField(null=True)

class Rating(models.Model):
    class Type(models.TextChoices):
        COMMENT = 'comment'
        PERCENTAGE = 'percentage'
        STAR = 'star'
    name = models.CharField(max_length=30)
    value = models.FloatField()
    type = models.CharField(
        max_length=10,
        choices=Type.choices,
        default=Type.STAR,
    )
    comment = models.TextField(null=True)


class Portal(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=100)

class History(models.Model):
    portal = models.ForeignKey(
        'Portal',
        on_delete=models.CASCADE,)
    link = models.CharField(max_length=100)


class Course(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    portal = models.ForeignKey(
        'Portal',
        on_delete=models.CASCADE,
    )
    information = models.ForeignKey(
        'Information',
        on_delete=models.SET_NULL,
        null=True

    )
    rating = models.ForeignKey(
        'Rating',
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)