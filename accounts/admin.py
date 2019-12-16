from django.contrib.admin import ModelAdmin, TabularInline, register
from accounts.models.Account import Account
from accounts.models.Transaction import Transaction


class TransactionInline(TabularInline):
    model = Transaction


@register(Account)
class AccountAdmin(ModelAdmin):
    inlines = [
        TransactionInline
    ]
