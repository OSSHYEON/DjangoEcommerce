from datetime import datetime

from django.db.models import Q
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.conf import settings
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from .forms import ReviewForm
from .models import Product, Order, OrderItem, Customer, ShippingAddress, Review
import json
import requests
import http.client
from django.urls import reverse


def shop(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            cartItems = order['order.get_cart_items']
        except:
            cartItems = 0

    products = Product.objects.all()
    kw = request.GET.get('kw')

    if kw:
        products = Product.objects.all().filter(Q(name__icontains=kw)).distinct()

    context={'products':products, 'cartItems':cartItems, 'kw':kw}
    return render(request, 'product/shop.html', context)



def detail(request, pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        form = ReviewForm()
    else:
        try:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            cartItems = order['order.get_cart_items']
            form = ReviewForm()
        except:
            cartItems = 0
    products = get_object_or_404(Product, id=pk)
    context ={'products':products, 'cartItems':cartItems, 'form':'form'}

    return render(request, 'product/product_detail.html', context)


# def add_review(request):
#     url = request.META.get('HTTP_REFERER')
#     try:
#         if request.method == 'POST':
#             form = ReviewForm(request.POST)
#             review = Review()
#             product = form.cleaned_data['review-product']
#             review.product_id = product.id
#             review.customer_id = request.user.customer.id
#             review.content = form.cleaned_data['content']
#             review.create_date = timezone.now()
#             review.save()
#             return redirect('detail')
#     except Exception as e:
#         print(e)




#=======================================================================================================================
# 장바구니, 주문

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            cartItems = order['order.get_cart_items']
        except:
            cartItems = 0

    context={'items':items, 'order':order, 'cartItems':cartItems, 'shipping': False}
    return render(request, 'product/cart.html', context)



def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['order.get_cart_items']

    context = {'items': items, 'order': order, 'cartItems':cartItems, 'shipping': False}
    return render(request, 'product/checkout.html', context)


def updateItem(request):

    data = json.loads(request.body)

    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)


    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'empty':
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('상품이 추가되었습니다', safe=False)


#=======================================================================================================================

@csrf_exempt
def kakaopay(request):
    if request.method == "POST":
        order_data = json.loads(request.body)
        print(order_data)
        product = order_data['item_name']
        quantity = order_data['quantity']
        total_amount = order_data['total_amount']
        admin_key = ""

        transaction_id = datetime.today().strftime("%Y_%m_%d")
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order.transaction_id = transaction_id
        order.complete = True
        order.save()


        ShippingAddress.objects.create(
            post_address=order_data['post_address'],
            road_name=order_data['road_addr'],
            detail_addr=order_data['detail_addr'],
            isShipped=False,
            isPaid=True,
            date_added=timezone.now(),
            customer=customer,
            order=order,
            phone= order_data['phone'],
            total_amount=order_data['total_amount']
        )

        url = 'https://kapi.kakao.com/v1/payment/ready'

        headers = {
            'Authorization': f'KakaoAK {admin_key}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }

        data = {
            'cid': "TC0ONETIME",
            'partner_order_id': "1",
            'partner_user_id': request.user.customer,
            'item_name' : product,
            'quantity': quantity,
            'total_amount' : total_amount,
            'tax_free_amount' : 0,
            'approval_url' : 'http://127.0.0.1:8010/success',
            'fail_url' : 'http://127.0.0.1:8010/',
            'cancel_url': 'http://127.0.0.1:8010/'
        }

        print(headers, data)
        try:
            response = requests.post(url, data=data, headers=headers)
            print(response)
            result = response.json()
            request.session['tid'] = result['tid']
            print(result['tid'])
            next_url = result['next_redirect_pc_url']
            print(next_url)
            return redirect(result['next_redirect_pc_url'])

        except Exception as e:
            print("에러 : ", e)
            return render(request, 'product/checkout.html')




def pay_success(request):
    transaction_id = datetime.today().strftime("%Y_%m_%d")

    url = 'https://kapi.kakao.com/v1/payment/approve'
    adminkey = ""

    headers = {
        'Authorization': 'KakaoAK' + adminkey,
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    data = {
        'cid': 'TC0ONETIME',
        'tid': request.session['tid'],
        'partner_order_id': "1",
        'partner_user_id': request.user.customer,
        'pg_token': request.GET['pg_token']
    }

    try:
        response = requests.post(url, data=data, headers=headers)
        result = response.json()
        return render(request, 'product/success.html')
    except Exception as e:
        print("에러 : ", e)
        return render(request, 'product/checkout.html')
