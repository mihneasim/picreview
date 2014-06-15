from django.db import models


class Request(models.Model):

    name = models.CharField(max_length=200, blank=False)

    email = models.EmailField()

    passkey = models.CharField(max_length=100)

    public = models.BooleanField(default=False)

    signed = models.BooleanField(default=False)

    notes = models.TextField()

    submitted = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=150)

    slug = models.CharField(max_length=150, db_index=True)

    answer = models.TextField()

    answered = models.DateTimeField(blank=True, default=None)


class Image(models.Model):

    SOURCES = (('REQ', 'request'), ('ANS', 'answer'))

    request = models.ForeignKey(Request)

    source = models.CharField(choices=SOURCES, default=SOURCES[0][0],
            max_length=3)

