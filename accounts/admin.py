from django.contrib import admin
from accounts.models.Account import Account
from accounts.models.Transaction import Transaction

# Register your models here.
admin.site.register(Account)
admin.site.register(Transaction)
