from django.db import models


class Word(models.Model):
    word_text = models.CharField(max_length=200)
    tf_amount = models.FloatField(default=0)
    idf_amount = models.FloatField(default=0)


class Dict(models.Model):
    doc_dict = models.JSONField()


class TempD(models.Model):
    temp_dict = models.JSONField()


class Idf(models.Model):
    idf_dict = models.JSONField()