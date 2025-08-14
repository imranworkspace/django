from django.contrib import admin
from .models import ProfileModel,PageModel,LikeModel
# Register your models here.
@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['profile_name','city']

admin.site.register(PageModel)
admin.site.register(LikeModel)