from django.contrib import admin

from .models import Profile,Events

class profileAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')
    list_filter =('firstname', 'lastname', 'email')


class EventsAdmin(admin.ModelAdmin):
    ist_display = ('date', 'time','location','description' ,'email')
    list_filter =('date', 'time','location','description' ,'email')
    


admin.site.register(Profile,profileAdmin)
admin.site.register(Events,EventsAdmin)

