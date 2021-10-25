from django.contrib import admin
from .models import Post

# Register your models here.
 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        css ={
             "all":("css/main.css",)
        
        }

        js= ('JS/main.js',)
         
     


# admin.site.register(Post)