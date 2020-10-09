from django.db import models

class Userdata(models.Model):
    hospitalid= models.SlugField(primary_key=True, unique=True)   #hospital_id for patient  #must be unique
    name      = models.CharField(max_length=40)      #name
    age       = models.IntegerField()   #agefield
    hpd       = models.BooleanField()   #history of pulmonary disease
    ckd       = models.BooleanField()   #history of ckd
    dm        = models.BooleanField()   #history of DM
    htn       = models.BooleanField()   #history of HTN
    hiv       = models.BooleanField()   #history of HIV
    trans     = models.BooleanField()   #immunosuppression/transplant
    resrate   = models.IntegerField()   #respiratory rate to be taken from electronics
    heartrate = models.IntegerField()   #heart rate to be taken from electronics
    spo       = models.IntegerField()   #spo2 to be taken from electronics
    ddimer    = models.IntegerField(null=True)   #ddimer ug/ml
    cpk       = models.IntegerField(null=True)   #cpk     U/L
    crp       = models.IntegerField(null=True)   #crp     mg/L
    ldh       = models.IntegerField(null=True)   #LDH     U/L
    tropo     = models.FloatField(null=True)     #tropopin ng/mL
    ferr      = models.IntegerField(null=True)   #ferritin ug/L
    absolute  = models.FloatField(null=True)     #Absolute Lymphocyte count
    ctscan    = models.IntegerField(null=True)   #CT SCAN
    abg       = models.IntegerField(null=True)   #ABG (P/F ratio)

    def __str__(self):
        return self.name
