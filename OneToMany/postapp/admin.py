from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import PostModel
@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display=['user','post_title','post_description','current_datetime','update_datetime']