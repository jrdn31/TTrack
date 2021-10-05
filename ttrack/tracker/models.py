from django.db import models
from django.core.validators import DecimalValidator, MaxValueValidator, MinValueValidator
from decimal import *


# Create your models here.
class TRC(models.Model):
    """Stores a list of TRCs not """
    name = models.CharField(max_length=5)
    def __str__(self):
        return self.name
class Borrower(models.Model):
    """Stores Borrower information"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(null=False, blank=False, max_length =20)
    email= models.EmailField(max_length=254, blank=False)
    trc = models.ForeignKey(TRC, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Location(models.Model):
    """Stores item locations"""
    name = models.CharField(max_length= 30)
    description = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.name} {self.description}'

class Item_Status(models.Model):
    """Stores item locations"""
    class Meta:
        verbose_name_plural="item status"
    name = models.CharField(max_length= 30)
    description = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.name}:   {self.description}'



class Item(models.Model):
    DE = "EXAM_CAM"
    DC = "CAMERA"
    DM = "MOBILE"
    DS = "STETH"
    DD = "DENTAL"
    DX = "MULTIPURPOSE"
    DZ = "OTHER/MISC"
    TL = "TOOL"
    SP = "SUPPLIES"
    PA = "PRODUCTION_AUDIO"
    PV = "PRODUCTION_VIDEO"
    ZZ = "OTHER"

    DEVICE_CAT_CHOICES= [
        (DE, 'Exam Cameras'),
        (DC, 'Camera'),
        (DM, 'Mobile'),
        (DS, 'Stethoscope'),
        (DD, 'Dental'),
        (DX, 'Other Device'),
        (TL, 'Tool'),
        (SP, 'Supplies'),
        (PA, 'Production: Audio'),
        (PV, 'Production: Video'),
        (ZZ, 'Other/Misc.'),
    ]

    name = models.CharField(max_length= 30)
    date_added = models.DateField(auto_now_add=True)
    manufacturer = models.CharField(max_length=150, blank=True)
    
    purchase_price = models.DecimalField(max_digits=7, decimal_places=2,validators=[MinValueValidator(Decimal('0.00'))])
    serial_number = models.CharField(max_length = 30, blank = True)
    device_category = models.CharField(
        max_length= 30,
        choices = DEVICE_CAT_CHOICES)
    location= models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.ForeignKey(Item_Status, on_delete=models.CASCADE)
    status_date = models.DateField(blank = True, null = True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Kit(models.Model):
    """Class for storing Kits which are a collection of items"""
    LOAN = "LOAN"
    DEMO = "DEMO"

    KIT_TYPE_CHOICES= [
        (LOAN, 'Loan Kit'),
        (DEMO, 'Demo Kit'),
    ]
    name = models.CharField(max_length = 30)
    description= models.CharField(max_length=255)
    items = models.ManyToManyField(Item)
    available = models.BooleanField(default = True)
    category = models.CharField(
        max_length= 4,
        choices = KIT_TYPE_CHOICES)
    def __str__(self):
        return self.name
class Request(models.Model):
    """A class that stores Loan request data"""
    # These are the states a loan status can take
    REQUESTED = 'REQ'
    APPROVED = 'APP'
    CANCELLED = 'CNC'
    COMPLETED = 'CMP'
    RETURNED = 'RTN'
    REQ_STATE_CHOICES = [
        (REQUESTED, 'Requested'),
        (APPROVED, 'Approved'),
        (CANCELLED, 'Cancelled'),
        (COMPLETED, 'Completed'),
        (RETURNED, 'Returned'),        
    ]
    borrower = models.ForeignKey(Borrower,on_delete=models.CASCADE)
    #TODO add staff once setup for tracking who approves loans
    #staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    request_date = models.DateTimeField(auto_now_add=True)
    #Adding desired date for when they want the equipment
    desired_date = models.DateField(blank=True, null = True)
    loan_length = models.SmallIntegerField(
        validators = [MinValueValidator(1, message="Loans cannot be shorter than one day."), MaxValueValidator(10, message="Loans cannot be longer than 10 days.")])
    req_status = models.CharField(
        max_length=3,
        choices = REQ_STATE_CHOICES,
        default= REQUESTED,
        )
    loan_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateField(blank=True, null = True)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)


