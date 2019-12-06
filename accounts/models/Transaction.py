from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE


class Transaction(Model):
    WITHDRAWAL = "WITH"
    DEPOSIT = "DEPS"

    type_choices = (
        (WITHDRAWAL, 'Withdrawal'),
        (DEPOSIT, 'Deposit')
    )

    account = ForeignKey('accounts.Account',
                         on_delete=CASCADE, related_name='transactions')

    type = CharField(choices=type_choices, max_length=10)
    amount = IntegerField()

    def __str__(self):
        return f"{self.account} - ${self.amount} {self.type}"
