from django.contrib import admin
from .models import *

admin.site.register(Task)
admin.site.register(App)
admin.site.register(AppDeveloper)
admin.site.register(AppSubcategory)
admin.site.register(AppCategory)
admin.site.register(AppAgeRating)
admin.site.register(AppEstimation)
admin.site.register(AppPreviewImage)