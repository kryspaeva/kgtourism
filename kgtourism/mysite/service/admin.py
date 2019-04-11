from django.contrib import admin

from .models import Hotel,Hostel,Cafe,Attraction,Regions,Staff_of_hotel,Staff_of_hostel,Staff_of_cafe,Staff_of_attraction

admin.site.register(Hotel)
admin.site.register(Hostel)
admin.site.register(Cafe)
admin.site.register(Attraction)
admin.site.register(Regions)
admin.site.register(Staff_of_hotel)
admin.site.register(Staff_of_hostel)
admin.site.register(Staff_of_cafe)
admin.site.register(Staff_of_attraction)