from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'myshop.payment'
    verbose_name = 'myshop.Payment'

    def ready(self):
    	# import signal handlers
    	import myshop.payment.signals