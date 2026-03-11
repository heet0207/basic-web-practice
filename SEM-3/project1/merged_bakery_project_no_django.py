# Merged Python Code (Django Removed)
# NOTE: Django-specific imports and references have been stripped.

# Merged Python Code for Bakery_eComm Project



================================================================================
================================================================================

#!/usr/bin/env python
import os
import sys


def main():
    """Run administrative tasks."""
    try:
    except ImportError as exc:
        raise ImportError(
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/__init__.py
================================================================================



================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/admin.py
================================================================================

from . models import Product,Customer,Cart

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']  #list  of columns from model

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/apps.py
================================================================================



class MannappConfig(AppConfig):
    name = 'mannapp'


================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/forms.py
================================================================================

from .models import Customer

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','mobile','state','zipcode']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
        }


================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/migrations/0001_initial.py
================================================================================




class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('BR', 'Bread'), ('CK', 'Cake'), ('CI', 'Cookie'), ('PS', 'Pastrie'), ('CC', 'Cupcake')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]


================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/migrations/0002_remove_product_composition_remove_product_prodapp_and_more.py
================================================================================




class Migration(migrations.Migration):

    dependencies = [
        ('mannapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='composition',
        ),
        migrations.RemoveField(
            model_name='product',
            name='prodapp',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BR', 'Bread'), ('CA', 'Cake'), ('CO', 'Cookie'), ('PS', 'Pastrie'), ('MU', 'Muffin')], max_length=2),
        ),
    ]


================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/migrations/0003_alter_product_category.py
================================================================================




class Migration(migrations.Migration):

    dependencies = [
        ('mannapp', '0002_remove_product_composition_remove_product_prodapp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BR', 'Bread'), ('CA', 'Cake'), ('CO', 'Cookie'), ('PS', 'Pastrie')], max_length=2),
        ),
    ]


================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/migrations/0004_customer.py
================================================================================




class Migration(migrations.Migration):

    dependencies = [
        ('mannapp', '0003_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
            ],
        ),
    ]


================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/migrations/0005_cart.py
================================================================================




class Migration(migrations.Migration):

    dependencies = [
        ('mannapp', '0004_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]


================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/migrations/__init__.py
================================================================================



================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/models.py
================================================================================


# Create your models here.
CATEGORY_CHOICES=(
    ('BR','Bread'),
    ('CA','Cake'),
    ('CO','Cookie'),
    ('PS','Pastrie'),
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/tests.py
================================================================================


# Create your tests here.


================================================================================
================================================================================

from . import views
from .forms import LoginForm

urlpatterns = [
    path("", views.home,name="home"),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("category/<slug:val>/",views.CategoryView.as_view(),name="category"),
    path("category-title/<val>/",views.CategoryTitle.as_view(),name="category-title"), #.as_view is used when we use class for function not needed
    path("productdetail/<int:pk>/",views.ProductDetail.as_view(),name="productdetail"),
    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("address/",views.address,name="address"),

    path("add-to-cart/",views.add_to_cart,name="add-to-cart"),
    path("cart/",views.show_cart,name="showcart"),
    path("checkout/",views.checkout.as_view(),name="checkout"),
    path("order-confirmation/", views.order_confirmation, name="order_confirmation"),
    path("search/",views.search,name="search"),

    path("pluscart/",views.plus_cart),
    path("minuscart/",views.minus_cart),
    path("removecart/",views.remove_cart),

    #login authentication
    path("registraion/",views.CustomerRegistrationView.as_view(),name="registration"),
    path("accounts/login/",auth_view.LoginView.as_view(template_name="login.html",authentication_form=LoginForm),name="login"), #accounts/login/->inbuilt path  LoginView->readymade view auth_view is renamed view
    path("logout/",auth_view.LogoutView.as_view(next_page="login"),name="logout"), #LogoutView is builtin view

admin.site.site_header="Sweet Slice"
admin.site.site_title="Sweet Slice"
admin.site.site_index_title="Welcome to Sweet Slice"

================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannapp/views.py
================================================================================

from . models import Product,Customer,Cart
from . forms import CustomerRegistrationForm,CustomerProfileForm

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




================================================================================
# FILE: /mnt/data/bakery_extracted/Bakery_eComm(Project)/Bakery_eComm(Project)/mannecomm/mannecomm/__init__.py
================================================================================



================================================================================
================================================================================

"""


For more information on this file, see
"""

import os





================================================================================
================================================================================

"""


For more information on this file, see

"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'mannapp',#me
]

MIDDLEWARE = [
]

ROOT_URLCONF = 'mannecomm.urls'

TEMPLATES = [
    {
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
            ],
        },
    },
]



# Database

DATABASES = {
    'default': {
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
    },
    {
    },
    {
    },
    {
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
#me
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL='/media/'
MEDIA_ROOT = BASE_DIR /'media'
LOGIN_REDIRECT_URL = '/profile/'


# Default primary key field type



================================================================================
================================================================================

"""
URL configuration for mannecomm project.

The `urlpatterns` list routes URLs to views. For more information please see:
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mannapp.urls")),
]


================================================================================
================================================================================

"""


For more information on this file, see
"""

import os



