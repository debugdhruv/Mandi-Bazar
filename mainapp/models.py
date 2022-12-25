from django.db import models

class Users(models.Model):
    type = models.CharField(max_length=30)      # here choice field

class Farmers_detail(models.Model):
    full_name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    email = models.EmailField(max_length = 254, unique= True )
    password = models.CharField(max_length=30)
    pan_card = models.IntegerField(null=True)
    adhar_card = models.IntegerField(null=True)
    address = models.CharField(max_length=200,null=True)
    bank_account_no = models.IntegerField(null=True)
    account_holder_name = models.CharField(max_length=30,null=True)
    ifsc_code = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.email

class Businessman_details(models.Model):
    full_name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length = 254, unique= True )
    password = models.CharField(max_length=30)
    pan_card = models.CharField(max_length=15, null=True)
    gst_number = models.CharField(max_length=15, null=True)
    adhar_card = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    bank_account_number = models.IntegerField( null=True)
    ifsc_code = models.CharField(max_length=20, null=True)
    account_holder_name = models.CharField(max_length=30, null=True)

class Admins_details(models.Model):
    full_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)      # here choice field
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)


class Product_details(models.Model):
    product_type = models.CharField(max_length=30) 
    subtype = models.CharField(max_length=30)   # here choice field
    quantity = models.IntegerField()
    district_name = models.CharField(max_length=30)  # here choice field
    base_price = models.DecimalField(max_digits=100, decimal_places=2)
    current_price=models.DecimalField(max_digits=100, decimal_places=2, null=True, default=0.0)
    description = models.CharField(max_length=300 )
    product_image1 = models.FileField(upload_to='images')
    product_image2 = models.FileField(upload_to='images')
    product_video = models.FileField(upload_to='videos')
    farmer = models.ForeignKey(Farmers_detail, on_delete=models.CASCADE)

class Market_rate(models.Model):
    date = models.DateField()
    rate = models.IntegerField()

class Bid_status(models.Model):
    status = models.CharField(max_length=30)

class Bid_price(models.Model):
    max_bid_price = models.IntegerField()

class Sale_Details(models.Model):
    Total_sale_price = models.IntegerField()
    picking_address = models.CharField(max_length=30)
    delivery_address = models.CharField(max_length=30)
    delivery_status = models.CharField(max_length=30)   # here choice field
