from django.db import models

# Create your models here.
class Contact(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField(max_length=100)
    customer_no = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True ,null=True)
    
    # Add this method to display the name in the admin panel!
    def __str__(self):
        return self.customer_name
    
class Product(models.Model):
    Products_id  = models.AutoField(primary_key=True)
    p_tagcolor = models.CharField(max_length=20)
    products_tag = models.CharField(max_length=20)
    Products_name = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    price = models.IntegerField()
    des = models.CharField(max_length=300)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='kids/images' ,default="")
    
    def __str__(self):
        return self.Products_name