from django.contrib import admin
from IOTD.models import UserProfile,Vote,Day,Total,Report
# registers the user profile in the admin site
admin.site.register(UserProfile)
# registers the vote in the admin site
admin.site.register(Vote)
# registers the day in the admin site
admin.site.register(Day)
# registers the total likes and dislikes in the admin site
admin.site.register(Total)
# registers the report in the admin site
admin.site.register(Report)

