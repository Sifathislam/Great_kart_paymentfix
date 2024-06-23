from django.urls import path
from . import views
from . import views2 #    # New Method Urls 

urlpatterns = [
    # Old code not need to work with them if facing probem with impelement in paypal 
    # path('place_order/', views.place_order, name='place_order'),
    # path('payments/', views.payments, name='payments'),
    # path('order_complete/', views.order_complete, name='order_complete'),

    #*====================  New Method Urls ======================== # 
    path('payment_product/', views2.payment_product, name='payment-product'),
    path('payment-success/<int:order_number>/', views2.PaymentSuccessful, name='payment-success'),
    path('payment-failed/', views2.paymentFailed, name='payment-failed'),
    path('paypal-ipn/', views2.paypal_ipn, name='paypal-ipn'),
]
