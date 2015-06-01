from django.contrib import admin
from .models import Post,Image

admin.site.register(Post)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','imgfile','image_img', )
    
admin.site.register(Image,ImageAdmin)
# Register your models here.
