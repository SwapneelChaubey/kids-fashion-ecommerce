from django.db import models

# Create your models here.
class Contact(models.Model):
    SUBJECT_CHOICES = [
    ("order", "Order Status & Delivery"),
    ("returns", "Returns & Exchange"),
    ("product", "Product Inquiries"),
    ("general", "General Support"),
    ]

    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField(max_length=100)
    customer_no = models.CharField(max_length=15)
    customer_message = models.CharField(max_length=300,default="")
    subject = models.CharField(max_length=20,choices=SUBJECT_CHOICES,default="general")
    date = models.DateTimeField(auto_now_add=True ,null=True)
    
    # Add this method to display the name in the admin panel!
    def __str__(self):
        return self.customer_name
    
class Product(models.Model):
    Products_id  = models.AutoField(primary_key=True)
    Products_name = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    price = models.IntegerField()
    des = models.CharField(max_length=300)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='kids/images' ,default="")
    
    def __str__(self):
        return self.Products_name
    
class Product_view(models.Model):
    Products_id  = models.AutoField(primary_key=True)
    Products_name = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    price = models.IntegerField()
    des = models.CharField(max_length=300)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='kids/images' ,default="")
    
    def __str__(self):
        return self.Products_name
    
class Boy(models.Model):
    Products_id  = models.AutoField(primary_key=True)
    Products_name = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    price = models.IntegerField()
    des = models.CharField(max_length=300)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='kids/images' ,default="")
    
    def __str__(self):
        return self.Products_name
    
class Girl(models.Model):
    Products_id  = models.AutoField(primary_key=True)
    Products_name = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    price = models.IntegerField()
    des = models.CharField(max_length=300)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='kids/images' ,default="")
    
    def __str__(self):
        return self.Products_name