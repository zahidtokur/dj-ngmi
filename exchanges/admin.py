from django.contrib import admin
from exchanges.models import ExchangeAccount


class ExchangeAccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExchangeAccount, ExchangeAccountAdmin)