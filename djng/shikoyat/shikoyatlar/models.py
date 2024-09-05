from django.db import models

stat = (
    ('Bajarildi', "Bajarildi"),
    ("Bajarilmoqda", "Bajarilmoqda"),
    ("Bajarilmadi", "Bajarilmadi")
)


company = (

    ('MARS' , "MARS"),
    ("Uzinfacom" , "Uzinfacom"),
    ("Realsoft" , "Realsoft"),
    ("Smartsoft" , "Smartsoft"),
    ("Cloudit" , "Cloudit"),
    ("Pentagon" , "Pentagon"),
    ("UIC group" , "UIC group"),
    ("Cometa" , "Cometa"),
    ("MXX" , "MXX"),
    ("YPX" , "YPX"),

    
)

class Shikoyat(models.Model):
    name = models.CharField(max_length=50)
    telnomer = models.CharField(max_length=50)
    location = models.TextField()
    company = models.CharField(max_length = 1000000000000, choices=company)
    complaint = models.TextField()
    status = models.CharField(max_length = 50, choices=stat)
    
def __str__(self) -> str:
    return self.name