from django.db import models

# Create your models here.

class Post(models.Model):
        title= models.CharField( max_length=150)
        postImg= models.ImageField(upload_to='ShopBlog/media', default="")
        content= models.TextField()
        subContent=models.TextField(max_length= 200)
        slug= models.SlugField()
        categary= models.CharField( max_length=50)
        subCategary= models.CharField(max_length=50)
        pubDate= models.DateField( auto_now_add=True)

        def __str__(self):
            return self.title 


        
