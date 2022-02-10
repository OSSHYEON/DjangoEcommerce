from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.shop, name="shop"),
    path('shop/<int:pk>/', views.detail, name='detail'),
    # path('review/', views.add_review, name='review'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('kakaopay/', views.kakaopay, name="kakaopay"),
    path('success/', views.pay_success, name="pay_success"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)