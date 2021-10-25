from django.db import models

# Create your models here.

class Product(models.Model):
        Name= models.CharField( max_length=50)
        productImg= models.ImageField( upload_to='Shop/media')
        Description= models.TextField()
        publishDate = models.DateField( auto_now_add=False)
        categary= models.CharField( max_length=50)
        subcategary= models.CharField( max_length=50)

        def __str__(self):
            return self.Name
        

class Contact(models.Model):
    Name=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    feedback= models.TextField()
    timeAndDate=  models.TimeField( auto_now_add=True)

    def __str__(self):
        return self.Name

        
    
