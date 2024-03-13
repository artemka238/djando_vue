from django.contrib import admin
from cats.models import AboutCats, Balance, CatHistory


class AboutCatsAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "breed", "image", "cost"]

class BalanceAdmin(admin.ModelAdmin):
    list_display = ["user", "balance"]

class CatsForPeopleAdmin(admin.ModelAdmin):
    list_display = ["cat", "owner"]



# Register your models here.
admin.site.register(AboutCats, AboutCatsAdmin)
admin.site.register(Balance, BalanceAdmin)
admin.site.register(CatHistory)