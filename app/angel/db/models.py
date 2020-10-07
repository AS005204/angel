from django.db import models

class SearchSquad(models.Model):
    event = models.TextField(max_length=159)

    def __str__(self):
        return '{}'.format(self.event)



class Event(models.Model):
    timeDate = models.DateTimeField( null=True, blank=True)
    description = models.TextField(max_length=159, null=True)


    def __str__(self):
        return '{}'.format(self.timeDate)




class Crew(models.Model):
    crewName = models.TextField(max_length=159)    
    timeDate = models.DateTimeField(blank=True)
    denorture = models.TextField(max_length=159, null=True,)
    arrival = models.BooleanField(null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.crewName)



class Education(models.Model):
    surname = models.TextField(max_length=159)
    headman = models.TextField(max_length=159, null=True)
    operator = models.TextField(max_length=159, null=True)

    def __str__(self):
        return '{}'.format(self.surname)


class Volunteers(models.Model):
    squad = models.TextField( max_length=159, null=True, blank=True)
    firstName = models.TextField(max_length=159)
    secondName = models.TextField(max_length=159)
    age = models.TextField(max_length=159, null=True, blank=True)
    position = models.TextField(max_length=159)
    callsign = models.TextField(max_length=159, blank=True)
    car = models.TextField(max_length=159, null=True, blank=True)
    walk = models.TextField(max_length=159, null=True, blank=True)
    lamp = models.TextField(max_length=159, null=True, blank=True)
    telNumber = models.TextField(max_length=159, blank=True)
    description = models.TextField(max_length=159, null=True, blank=True)
    photo = models.ImageField(upload_to='', height_field=100, width_field=100, null=True, blank=True)
    searchSquad = models.ManyToManyField( SearchSquad , blank=True, null=True )
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE , blank=True, null=True)
    education = models.ManyToManyField(Education , blank=True, null=True) 


    def __str__(self):
        return '{}'.format(self.squad)




class Equipment_hisrory(models.Model):
    equipmentId = models.TextField(max_length=159)
    timeDate = models.DateTimeField( null=True, blank=True)
    location = models.TextField(max_length=159)
    event = models.TextField(max_length=159)
    equipment = models.ForeignKey(Volunteers, on_delete=models.CASCADE)
    crew = models.ManyToManyField(Crew) 

    def __str__(self):
        return '{}'.format(self.event)




class Equipment(models.Model):
    typ = models.TextField(max_length=159)
    serName = models.TextField(max_length=159)
    description = models.TextField(max_length=159, null=True)
    photo = models.ImageField(upload_to='', height_field=100, width_field=100, null=True)
    volunteer = models.ForeignKey(Volunteers, on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.typ)

