from django.utils.translation import gettext_lazy as _

PERIOD_CHOICES = (
    (0, _("Only Once")),
    (1, _("Every Month")),
    (3, _("Every 3 Months")),
    (6, _("Every 6 Months")),
    (9, _("Every 9 Months")),
    (12, _("Every 12 Months")),
    (24, _("Every 24 Months")),
)

CURRENCY_CHOICES = (
    ("COP", "COP"),
    ("USD", "USD"),
)

ID_TYPE_CHOICES = (
    ("", ""),
    ("ti", _("TI")),
    ("cc", _("CC")),
    ("te", _("TE")),
    ("nit", _("NIT")),
    ("passport", _("PASSPORT")),
    ("final_consumer", _("FINAL CONSUMER")),
    ("civil_register", _("CIVIL _REGISTRATION")),
    ("another", _("ANOTHER")),
    ("undefined", _("UNDEFINED")),
)

STATUS_CHOICES = (
    ("active", _("Active")),
    ("inactive", _("Inactive")),
    ("to_deactivate", _("To be deactivated")),
)

CONTRACT_TYPE_CHOICES = (
    ("unique", _("Unique Charge")),
    ("recurring", _("Recurring Charge")),
    ("quotas", _("Multiple Quotas")),
)
USER_ROLES = (
    ("user", _("User")),
    ("administrator", _("Administrator")),
    ("owner", _("Owner")),
)

DEBT_STATUS_CHOICES = (
    ("pending", _("Pending")),
    ("sent", _("Sent")),
    ("paid", _("Paid")),
    ("expired", _("Expired")),
    ("voided", _("Voided")),
)

PAYMENT_METHOD_CHOICES = (
    ("cash", _("Cash")),
    ("bank", _("Bank Transfer")),
    ("payu", _("Payu")),
    ("epayco", _("ePayco")),
    ("stripe", _("Stripe")),
)

TRANSACTION_STATUS = (
    ("pending", _("Pending")),
    ("approved", _("Approved")),
    ("failed", _("Failed")),
)

NOTIFICATION_CHANNELS_CHOICES = (
    ("email", _("Email")),
    ("sms", _("SMS")),
)

ORGANIZATION_SESSION_NAME = "_logged_organization"

NOTIFICATION_TARGET_TYPES = (
    ("start_date", _("Start Date")),
    ("expiration_date", _("Expiration Date")),
)

OTHER_VALUES = (
    _("savings"),
    _("checking"),
)
