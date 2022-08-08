from django.db import models





class Courses(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)
    text = models.TextField()
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return self.title

class Teacher(models.Model):
    img = models.ImageField(upload_to='images/')
    last_anme = models.CharField(max_length=250)
    jobs = models.CharField(max_length=250)


    def __str__(self):
        return self.last_anme

class New(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.TextField()
    text = models.TextField()


    def __str__(self):
        return self.name


class Contact(models.Model):
    last_name = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    text = models.TextField()


