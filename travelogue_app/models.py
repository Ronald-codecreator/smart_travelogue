from django.db import models

# Create your models here.


class Login (models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200) 
    utype=models.CharField(max_length=200)
    
class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    Post=models.CharField(max_length=100)
    Pin=models.CharField(max_length=100)
    Phonenumber=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Photo=models.CharField(max_length=100)


class category(models.Model):
    category=models.CharField(max_length=200)


    
class Place(models.Model):
    place_name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    landmark=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    lati=models.CharField(max_length=200)
    longi=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    CATEGORY = models.ForeignKey(category, on_delete=models.CASCADE)
    pos = models.IntegerField(default=0)
    neg = models.IntegerField(default=0)
    neu = models.IntegerField(default=0)


class Notification(models.Model):
    notification=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    
class Feedback(models.Model):
    feedback=models.CharField(max_length=200)
    date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Review(models.Model):
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    review=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    date=models.DateField()
    photo1=models.CharField(max_length=200)



class Facility(models.Model):
    type=models.CharField(max_length=200)
    f_name=models.CharField(max_length=200)
    f_place=models.CharField(max_length=200)
    lati=models.CharField(max_length=200)
    longi=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    photo=models.CharField(max_length=250)
    
    
class Travelogue(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    travel_title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    date=models.DateField()





class Media(models.Model):
    place=models.CharField(max_length=100)
    media_type=models.CharField(max_length=200)
    file=models.CharField(max_length=250)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    travelogue=models.ForeignKey(Travelogue,on_delete=models.CASCADE)

    
    
    
class Checkin(models.Model):
    travelogue=models.ForeignKey(Travelogue,on_delete=models.CASCADE)
    facility=models.ForeignKey(Facility,on_delete=models.CASCADE)
    overall_exp=models.CharField(max_length=200)
    
    
class Package(models.Model):
    facility=models.ForeignKey(Facility,on_delete=models.CASCADE)
    package_name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    valid_from=models.CharField(max_length=200)
    valid_till=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    
    
    
    
    
class tree(models.Model):
    venueid= models.CharField(max_length=50)
    distance= models.FloatField()
    parentnodeid= models.IntegerField()
    level= models.IntegerField()
    nodeid= models.IntegerField()



    
    