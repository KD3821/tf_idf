from django.db import models
from django.forms import ModelForm


# def user_directory_path(instance, filename):
#     return 'user_{0}/{1}'.format(instance.user.id, filename)




# class UserFile(models.Model):
#     title = models.CharField(max_length=200)
#     upload = models.FileField(upload_to=user_directory_path)







class Word(models.Model):
    word_text = models.CharField(max_length=200)
    tf_amount = models.IntegerField(default=0)
    idf_amount = models.IntegerField(default=0)