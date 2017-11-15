from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .models import OrderItem, Order
from .forms import OrderCreateForm
from ..cart.cart import Cart
from django.template.loader import render_to_string
import weasyprint
from django.conf import settings
from django.http import HttpResponse
#from .tasks import order_created


@staff_member_required
def admin_order_detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	return render(request, 'admin/orders/order/detail.html', {'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	html = render_to_string('orders/order/pdf.html', {'order': order})
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename'
	
def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			for item in cart:
				OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
			cart.clear()
			request.session['order_id'] = order.id
			return redirect(reverse('payment:process'))
	else:
		form = OrderCreateForm()
	return render(request, 'orders/order/create.html', {'cart': cart, 'form':form})
			# if offer < item.minOffer:
			# 	error.append('Please make better offer')
			# elif offer >= minOffer:
			# 	cost = offer
			# if cost > item.price:
			# 	itemPrice = cost
			# else:
			# 	itemPrice = price

		'''
		if cart.coupon:
			order.coupon = cart.coupon
			order.discount = cart.counpon.discount
			order.save()
		'''
			# for item in cart:
			# 	OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
			# 	OrderItem.save()
			# cart.clear()
			# launch asynchronous task
			#order_created.delay(order.id)
	# 		return render(request, 'orders/order/created.html', {'order': order})
	# else:
	# 	form = OrderCreateForm()
	# return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
		# order_created.delay(order.id)
		# request.session['order_id'] = order.id
		# return redirect(reverse('payments:process'))

