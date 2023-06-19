from django.contrib import admin
from reviews.models import User, Review, Comments
# Register your models here.
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Comments)