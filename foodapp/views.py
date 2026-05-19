from django.shortcuts import render, redirect


# LOGIN PAGE
def login(request):

    if request.method == "POST":
        return redirect('/')

    return render(request, 'foodapp/login.html')


# HOME PAGE
def home(request):

    return render(request, 'foodapp/index.html')





# ADD TO CART
def add_to_cart(request):

    name = request.GET.get('name')
    price = int(request.GET.get('price'))
    image = request.GET.get('image')

    cart_items = request.session.get('cart_items', [])

    item_found = False

    # CHECK IF ITEM ALREADY EXISTS
    for item in cart_items:

        if item['name'] == name:

            item['quantity'] += 1
            item_found = True
            break

    # NEW ITEM
    if not item_found:

        cart_items.append({

            'name': name,
            'price': price,
            'image': image,
            'quantity': 1
        })

    request.session['cart_items'] = cart_items

    return redirect('/cart/')


# CART PAGE
def cart(request):

    cart_items = request.session.get('cart_items', [])

    total = 0

    for item in cart_items:

        total += item['price'] * item['quantity']

    return render(request, 'foodapp/cart.html', {

        'cart_items': cart_items,
        'total': total
    })


# INCREASE QUANTITY
def increase_quantity(request, index):

    cart_items = request.session.get('cart_items', [])

    if index < len(cart_items):

        cart_items[index]['quantity'] += 1

    request.session['cart_items'] = cart_items

    return redirect('/cart/')


# DECREASE QUANTITY
def decrease_quantity(request, index):

    cart_items = request.session.get('cart_items', [])

    if index < len(cart_items):

        if cart_items[index]['quantity'] > 1:

            cart_items[index]['quantity'] -= 1

        else:

            cart_items.pop(index)

    request.session['cart_items'] = cart_items

    return redirect('/cart/')


# REMOVE ITEM
def remove_item(request, index):

    cart_items = request.session.get('cart_items', [])

    if index < len(cart_items):

        cart_items.pop(index)

    request.session['cart_items'] = cart_items

    return redirect('/cart/')
# views.py

from django.shortcuts import render

def view_menu(request, restaurant_name):

    menus = {

        'Pizza Palace': [

            {
                'name': 'Margherita Pizza',
                'price': 299,
                'image': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?q=80&w=1200&auto=format&fit=crop'
            },

            {
                'name': 'Cheese Burst Pizza',
                'price': 399,
                'image': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?q=80&w=1200&auto=format&fit=crop'
            },

        ],

        'Burger Barn': [

            {
                'name': 'Chicken Burger',
                'price': 199,
                'image': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=1200&auto=format&fit=crop'
            },

            {
                'name': 'French Fries',
                'price': 99,
                'image': 'https://images.unsplash.com/photo-1571091718767-18b5b1457add?q=80&w=1200&auto=format&fit=crop'
            },

        ],

        'KFC': [

            {
                'name': 'Chicken Bucket',
                'price': 499,
                'image': 'https://images.unsplash.com/photo-1562967914-608f82629710?q=80&w=1200&auto=format&fit=crop'
            },

            {
                'name': 'Zinger Burger',
                'price': 249,
                'image': 'https://images.unsplash.com/photo-1550547660-d9450f859349?q=80&w=1200&auto=format&fit=crop'
            },

        ],

        'Momos Point': [

            {
                'name': 'Chicken Momos',
                'price': 149,
                'image': 'https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?q=80&w=1200&auto=format&fit=crop'
            },

            {
                'name': 'Fried Momos',
                'price': 179,
                'image': 'https://images.unsplash.com/photo-1601050690597-df0568f70950?q=80&w=1200&auto=format&fit=crop'
            },

        ],

        'Paradise Biryani': [

            {
                'name': 'Chicken Biryani',
                'price': 299,
                'image': 'https://images.unsplash.com/photo-1701579231349-d7459c40919d?q=80&w=1200&auto=format&fit=crop'
            },

            {
                'name': 'Mutton Biryani',
                'price': 399,
                'image': 'https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?q=80&w=1200&auto=format&fit=crop'
            },

        ],

        'Green Bowl': [

            {
                'name': 'Healthy Salad',
                'price': 199,
                'image': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=1200&auto=format&fit=crop'
            },

            {
                'name': 'Fruit Bowl',
                'price': 149,
                'image': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=1200&auto=format&fit=crop'
            },

        ],

        'Chocolate Room': [

            {
                'name': 'Chocolate Cake',
                'price': 179,
                'image': 'https://images.unsplash.com/photo-1515003197210-e0cd71810b5f?q=80&w=1200&auto=format&fit=crop'
            },

            {
                'name': 'Ice Cream Sundae',
                'price': 129,
                'image': 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?q=80&w=1200&auto=format&fit=crop'
            },

        ]

    }

    items = menus.get(restaurant_name, [])

    return render(request, 'foodapp/view_menu.html', {
        'restaurant_name': restaurant_name,
        'items': items
    })
def restaurants(request):

    return render(request, 'foodapp/restaurants.html')
def green_bowl(request):
    return render(request, 'foodapp/green_bowl.html')

def chocolate_room(request):
    return render(request, 'foodapp/chocolate_room.html')

def kfc(request):
    return render(request, 'foodapp/kfc.html')

def pizza(request):
    return render(request, 'foodapp/pizza.html')
def burger(request):

    return render(request, 'foodapp/burger.html')
def meals(request):

    return render(request, 'foodapp/meals.html')
def paradise(request):

    return render(request, 'foodapp/paradise.html')
from django.shortcuts import render, redirect

def feedback(request):

    if request.method == "POST":

        return redirect('/feedback-success/')

    return render(request, 'foodapp/feedback.html')


def feedback_success(request):

    return render(request,'foodapp/feedback_success.html')
# PAYMENT PAGE
def payment(request):

    return render(request, 'foodapp/payment.html')


# SUCCESS PAGE
def success(request):

    return render(request, 'foodapp/success.html')


# TRACKING PAGE
def tracking(request):

    return render(request, 'foodapp/tracking.html')