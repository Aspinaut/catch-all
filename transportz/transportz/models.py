from django.db import models

class User(models.Model):
    firstname  = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    pseudo = models.CharField(max_length=30)
    phrasepass= models.CharField(max_length=50)
    admin=models.BooleanField()
    GENDER_CHOISES= (('M', 'Male'), ('F', 'Female'), ('X', 'X'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES)

    def __str__(self):
        return self.firstname+' '+ self.lastname

class Line(models.Model):
    name= models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Arret(models.Model):
    arret = models.CharField(max_length=30)
    def __str__(self):
        return self.arret

class Junction(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    arret = models.ForeignKey(Arret, on_delete=models.CASCADE)
    position = models.IntegerField(default=0)

class Signal(models.Model):
    arret = models.ForeignKey(Arret, on_delete=models.CASCADE)
    who=models.ForeignKey(User, on_delete=models.CASCADE )
    def __str__(self):
        return self.line + '' + self.arret
