from django.contrib import admin
from cats.models import AboutCats, CatsForPeople, Balance


class AboutCatsAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "breed", "image", "cost"]

class BalanceAdmin(admin.ModelAdmin):
    list_display = ["user", "balance"]

class CatsForPeopleAdmin(admin.ModelAdmin):
    list_display = ["cat", "owner"]



# Register your models here.
admin.site.register(AboutCats, AboutCatsAdmin)
admin.site.register(CatsForPeople, CatsForPeopleAdmin)
admin.site.register(Balance, BalanceAdmin)