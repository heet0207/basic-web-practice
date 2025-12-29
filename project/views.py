from django.shortcuts import render,redirect
from django.views import View
from . models import Product,Customer,Cart
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q,Count
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
#we can render pages by two ways using function and class  

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def about(request):
    return render(request,'about.html')

@login_required
def contact(request):
    return render(request,'contact.html')

@method_decorator(login_required,name='dispatch')
class CategoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)  #filter is a condition
        title=Product.objects.filter(category=val).values('title')
        return render(request,"category.html",locals()) #locals function pass variable from this fun to this file

@method_decorator(login_required,name='dispatch')    
class CategoryTitle(View):
    def get(self,request,val):
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values('title')
        return render(request,"category.html",locals())

@method_decorator(login_required,name='dispatch')    
class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)  #primary key=variable
        return render(request,"productdetail.html",locals())
    
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,"registration.html",locals())
    
    def post(self,request):         #this fun is used to perform some functionality after submitting the form
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Registered Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,"registration.html",locals())

@method_decorator(login_required,name='dispatch')    
class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,"profile.html",locals())
    def post(self,request):  
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user= request.user                      #storing in varibales
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
        
        # (object)(model) (dbcolumn=var)
            reg= Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            reg.save()  #save in db
            messages.success(request,"Congratulations! Profile Saved Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,"profile.html",locals())
    
 #use function if you only want to fetch data from db and display

@login_required 
def address(request):
    add=Customer.objects.filter(user=request.user)  #only logged in user data is stored in add
    return render(request,'address.html',locals())

@login_required
def add_to_cart(request):
    user=request.user #storing the logged in user
    prodruct_id=request.GET.get('prod_id') #fetching product id from productdetailpage
    product=Product.objects.get(id=prodruct_id)
    Cart(user=user,product=product).save()  #inserting the values in cart table
    return redirect("/cart")

@login_required
def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity * p.product.discounted_price
        amount=amount+value
    totalamount=amount+40
    return render(request,'addtocart.html',locals())

@method_decorator(login_required,name='dispatch')
class checkout(View):
    def get(self,request):
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount=0
        for p in cart_items:
            value=p.quantity * p.product.discounted_price
            famount=famount+value
        totalamount=famount+40
        return render(request,'checkout.html',locals())
    
    def post(self, request):
        user = request.user
        Cart.objects.filter(user=user).delete()
        return redirect('order_confirmation')

@login_required
def order_confirmation(request):
    return render(request, 'order_confirmation.html')

def plus_cart(request):           
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) #Q is used for multiple filter conditions
        c.quantity+=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity * p.product.discounted_price
            amount=amount+value
        totalamount=amount+40
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def minus_cart(request):           
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) #Q is used for multiple filter conditions
        c.quantity-=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity * p.product.discounted_price
            amount=amount+value
        totalamount=amount+40
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def remove_cart(request):           
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) #Q is used for multiple filter conditions
        c.delete()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity * p.product.discounted_price
            amount=amount+value
        totalamount=amount+40
        data={
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

@login_required    
def search(request):
    query=request.GET['search']
    product=Product.objects.filter(Q(title__icontains=query))
    return render(request,"search.html",locals())


