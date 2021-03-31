from django.contrib import admin
from IOTD.models import UserProfile,Vote,Day,Total,Report
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Vote)
admin.site.register(Day)
admin.site.register(Total)
admin.site.register(Report)

