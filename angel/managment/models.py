from django.db import models


class Crew(models.Model):
    crewName = models.TextField(max_length=159)    
    timeDate = models.DateTimeField(blank=True)
    denorture = models.TextField(max_length=159, null=True,) #main
    arrival = models.BooleanField(null=True)

    def __str__(self):
        return '{}'.format(self.crewName)



class Volunteers(models.Model):
    squad = models.TextField(max_length=159)
    firstName = models.TextField(max_length=159)
    secondName = models.TextField(max_length=159)
    age = models.TextField(max_length=159, null=True, blank=True)
    position = models.TextField(max_length=159)
    callsign = models.TextField(max_length=159, blank=True)
    car = models.BooleanField( null=True, blank=True)
    walk = models.TextField(max_length=159, null=True, blank=True)
    lamp = models.TextField(max_length=159, null=True, blank=True)
    telNumber = models.TextField(max_length=159, blank=True)
    description = models.TextField(max_length=159, null=True, blank=True)
    photo = models.ImageField(upload_to='', height_field=100, width_field=100, null=True, blank=True)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE , blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.squad)



class Event(models.Model):
    timeDate = models.DateTimeField( null=True, blank=True)
    description = models.TextField(max_length=159, null=True)
    voluentres = models.ManyToManyField(Volunteers , blank=True) 


    def __str__(self):
        return '{}'.format(self.timeDate)

class SearchSquad(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    voluentres = models.ManyToManyField(Volunteers , blank=True) 
    Found = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.event)


class Education(models.Model):
    surname = models.TextField(max_length=159)
    headman = models.TextField(max_length=159, null=True)
    timeDate = models.DateTimeField( null=True, blank=True)
    description = models.TextField(max_length=159, null=True)
    voluentres = models.ManyToManyField(Volunteers , blank=True) 

    def __str__(self):
        return '{}'.format(self.surname)

class Equipment(models.Model):
    typ = models.TextField(max_length=159)
    serName = models.TextField(max_length=159)
    description = models.TextField(max_length=159, null=True)
    photo = models.ImageField(upload_to='', height_field=100, width_field=100, blank=True)
    volunteer = models.ForeignKey(Volunteers, on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.typ)




class Equipment_hisrory(models.Model):
    equipmentId = models.TextField(max_length=159)
    timeDate = models.DateTimeField( null=True, blank=True)
    location = models.TextField(max_length=159)
    event = models.TextField(max_length=159)
    voluenteers = models.ForeignKey(Volunteers, on_delete=models.CASCADE)
    equipment = models.ManyToManyField(Equipment, )
    crew = models.ManyToManyField(Crew) 


    def __str__(self):
        return '{}'.format(self.event)

class Missing_people(models.Model):
    event =  models.TextField(max_length=159)
    fullname = models.TextField(max_length=159)
    timeDate = models.DateTimeField( null=True, blank=True)
    description = models.TextField(max_length=159)
    photo = models.ImageField(upload_to='', height_field=100, width_field=100, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.event)

class Found_people(models.Model):
    fullname = models.TextField(max_length=159)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    description = models.TextField(max_length=159)
    photo = models.ImageField(upload_to='', height_field=100, width_field=100, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.event)

