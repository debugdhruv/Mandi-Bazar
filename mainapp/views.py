from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .models import *
import random


def index(request):
    return render(request, 'index.html')

def farmer_signup(request):
    if request.method != 'POST':
        pass
    else:
        global farmer_first_name, farmer_last_name, farmer_contact_no,farmer_email, farmer_password
        farmer_first_name = request.POST.get('first_name')
        farmer_last_name = request.POST.get('last_name')
        farmer_contact_no = request.POST.get('contact_no')
        farmer_email = request.POST.get('email')
        farmer_password = request.POST.get('password')
        farmer_re_password = request.POST.get('re-password')
        
        correct_info = 'YES'

        queryset = Farmers_detail.objects.filter(email= farmer_email)
        list(queryset)

        if(len(queryset) !=0):    
            messages.error(request, 'Email Already Registered. ')
            correct_info = 'NO'


        if not (farmer_first_name.isalpha()):
            messages.error(request, 'First name must be alphabetic ')
            correct_info = 'NO'

        if not (farmer_last_name.isalpha()):
            messages.error(request, 'Last name must be alphabetic ')
            correct_info = 'NO'

        if len(farmer_contact_no) != 10 :
            messages.error(request, 'Contact no should be equal to 10')
            correct_info = 'NO'

        if len(farmer_password) < 8:
            messages.error(request, 'your password length should be more than 8')   
            correct_info = 'NO'


        elif farmer_password != farmer_re_password:
            messages.error(request, "Password does not match")
            correct_info = 'NO'

        if(correct_info == 'YES'):
            random1 = random.randint(1000, 9999)
            request.session['random1'] = random1

            send_mail(
            'mandi bazar',
            f'Your OTP to register with mandi-bazar is :{random1}',
            settings.EMAIL_HOST_USER, 
            [farmer_email],
            fail_silently=False,
            )
            return HttpResponseRedirect('/mandi/farmer_otp')

        else:
            print('Incorrect info')
    return render(request, 'farmer_signup.html')

def farmer_confirm_otp(request):
    if request.method != 'POST':
        pass
    else:
        user_otp = request.POST.get('otp')
        print(user_otp)
        
        random1 = request.session.get('random1')

        print(random1)
        if(random1 == int(user_otp)):
            print('Register Successfully')
            
            farmer = Farmers_detail()
            farmer.full_name = farmer_first_name + " " + farmer_last_name
            farmer.contact_no = farmer_contact_no
            farmer.email = farmer_email
            farmer.password = farmer_password
            farmer.save()

            return HttpResponseRedirect('/mandi/farmer-login')

        else:
            messages.error(request, 'otp does not match')    
            print('not match')

    
    return render(request, 'farmer_otp.html')

def farmer_login(request):
    if request.method != 'POST':
        pass
    else:
        user_email = request.POST.get('email')
        user_password =  request.POST.get('password')
        print(user_email)
        print(user_password)

        queryset = Farmers_detail.objects.filter(email= user_email, password=user_password)
        list(queryset)
        if(len(queryset) !=0):    
            print('loged in successfully')
            request.session['email'] = user_email
            return HttpResponseRedirect('/mandi/farmer_home')
        else:
            messages.error(request, 'Email and password does not match')    
    return render(request, 'farmer_login.html')

def farmer_home(request):
    email = request.session.get('email')
    
    return render(request, 'farmer_home.html',{"email":email})

def farmer_complete_profile(request):
    if request.method != 'POST':
        pass
    else:
        email = request.session.get('email')

        farmer_Adhar_card = request.POST.get('Adhar_card')
        farmer_pan_card = request.POST.get('Pan_card')
        farmer_address = request.POST.get('Address')
        farmer_bank_account_no = request.POST.get('Bank_account_no')
        farmer_account_holder_name = request.POST.get('Account_holder_name')
        farmer_ifsc_code = request.POST.get('Ifsc_code')

        farmer_account_holder_name2 = farmer_account_holder_name.replace(" ", "")        
        correct_info = 'YES'

        if len(farmer_Adhar_card) != 12:       
            messages.error(request, 'please enter correct adhar card number')
            correct_info = 'NO'

        if len(farmer_pan_card) != 10:       
            messages.error(request, 'please enter correct pan card number')
            correct_info = 'NO'

        if not (farmer_account_holder_name2.isalpha()):
            messages.error(request, 'User name must be alphabetic ')
            correct_info = 'NO'

        if(correct_info == 'YES'):

            farmer = Farmers_detail.objects.get(email=email)
            farmer.adhar_card = farmer_Adhar_card
            farmer.pan_card = farmer_pan_card
            farmer.address = farmer_address
            farmer.bank_account_no = farmer_bank_account_no
            farmer.account_holder_name = farmer_account_holder_name
            farmer.ifsc_code = farmer_ifsc_code
            farmer.save() 
            return HttpResponseRedirect('/mandi/farmer_home')


    return render(request, "farmer_complete_profile.html")

def product_form(request):
    if request.method != 'POST' and ('image1' not in request.FILES and 'image2' not in request.FILES and 'video' not in request.FILES):
        pass
    else:
        print('hy')
        print('hy')
        product_name = request.POST.get("product_name")
        product_subtype = request.POST.get("subtype")
        quantity = request.POST.get("quantity")
        district = request.POST.get("district")
        base_price = request.POST.get("base_price")
        description = request.POST.get("description")
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        video = request.FILES.get('video')
        
        email = request.session.get('email')
        queryset = Farmers_detail.objects.filter(email=email)
        list(queryset)
        id = queryset[0].id


        product = Product_details()
        product.product_type = product_name
        product.subtype = product_subtype
        product.quantity = quantity
        product.district_name = district
        product.base_price = base_price
        product.description = description
        product.product_image1 = image1
        product.product_image2 = image2
        product.product_video = video
        product.farmer_id = id
        product.save()
        return HttpResponseRedirect('/mandi/farmer_home')

    return render(request, 'product_form.html')

def businessman_signup(request):
    if request.method != 'POST':
        pass
    else:
        businessman_first_name = request.POST.get('first_name')
        businessman_last_name = request.POST.get('last_name')
        businessman_contact_no = request.POST.get('contact_no')
        businessman_email = request.POST.get('email')
        businessman_password = request.POST.get('password')
        businessman_re_password = request.POST.get('re-password')
        

        correct_info = 'YES'

        queryset = Businessman_details.objects.filter(email= businessman_email)
        list(queryset)

        if(len(queryset) !=0):    
            messages.error(request, 'Email Already Registered. ')
            correct_info = 'NO'

        if not (businessman_first_name.isalpha()):
            messages.error(request, 'First name must be alphabetic ')
            correct_info = 'NO'

        if not (businessman_last_name.isalpha()):
            messages.error(request, 'Last name must be alphabetic ')
            correct_info = 'NO'

        if len(businessman_contact_no) != 10 :
            messages.error(request, 'Contact no should be equal to 10')
            correct_info = 'NO'

        if len(businessman_password) < 8:
            messages.error(request, 'your password length should be more than 8')   
            correct_info = 'NO'


        elif businessman_password != businessman_re_password:
            messages.error(request, "Password does not match")
            correct_info = 'NO'

        if(correct_info == 'YES'):
            request.session['businessman_first_name'] = businessman_first_name
            request.session['businessman_last_name'] = businessman_last_name
            request.session['businessman_contact_no'] = businessman_contact_no
            request.session['businessman_email'] = businessman_email
            request.session['businessman_password'] = businessman_password

            random2 = random.randint(1000, 9999)
            request.session['random2'] = random2
            print(random2)
            send_mail(
            'mandi bazar',
            f'Your OTP to register with mandi-bazar is :{random2}',
            settings.EMAIL_HOST_USER, 
            [businessman_email],
            fail_silently=False,
            )
            return HttpResponseRedirect('/mandi/businessman_otp')

        else:
            print('Incorrect info')

    return render(request, 'businessman_signup.html')

def businessman_confirm_otp(request):

    if request.method != 'POST':
        pass
    else:
        user_otp = request.POST.get('otp')
        print(user_otp)
        
        random2 = request.session.get("random2")
        print(random2)

        businessman_first_name = request.session.get("businessman_first_name")
        businessman_last_name = request.session.get("businessman_last_name")
        businessman_contact_no = request.session.get("businessman_contact_no")
        businessman_email = request.session.get("businessman_email")
        businessman_password = request.session.get("businessman_password")

        print(businessman_contact_no)

        if(random2 == int(user_otp)):
            print('Register Successfully')
            
            businessman = Businessman_details()
            businessman.full_name = str(businessman_first_name) + " " + str(businessman_last_name)
            businessman.email = businessman_email
            businessman.contact_number = businessman_contact_no
            businessman.password = businessman_password
            businessman.save()

            return HttpResponseRedirect('/mandi/businessman_home')

        else:
            messages.error(request, 'otp does not match')    
            print('not match')
    
    return render(request, 'businessman_otp.html')


def businessman_login(request):
    if request.method != 'POST':
        pass
    else:
        user_email = request.POST.get('email')
        user_password =  request.POST.get('password')
        print(user_email)
        print(user_password)

        queryset = Businessman_details.objects.filter(email= user_email, password=user_password)
        list(queryset)
        if(len(queryset) !=0):    
            print('logged in successfully')
            request.session['email2'] = user_email
            return HttpResponseRedirect('/mandi/businessman_home')
        else:
            messages.error(request, 'Email and password does not match')    
    return render(request, 'businessman_login.html')

def businessman_home(request):
    email2 = request.session.get('email2')

    return render(request, 'businessman_home.html',{"email":email2})


def businessman_complete_profile(request):
    if request.method != 'POST':
        pass
    else:
        email2 = request.session.get('email2')

        businessman_Adhar_card = request.POST.get('Adhar_card')
        businessman_pan_card = request.POST.get('Pan_card')
        businessman_gst_number = request.POST.get('gst_number')
        businessman_address = request.POST.get('Address')
        businessman_bank_account_no = request.POST.get('Bank_account_no')
        businessman_account_holder_name = request.POST.get('Account_holder_name')
        businessman_ifsc_code = request.POST.get('Ifsc_code')

        businessman_account_holder_name2 = businessman_account_holder_name.replace(" ", "")        
        correct_info = 'YES'

        if len(businessman_Adhar_card) != 12:       
            messages.error(request, 'please enter correct adhar card number')
            correct_info = 'NO'

        if len(businessman_pan_card) != 10:       
            messages.error(request, 'please enter correct pan card number')
            correct_info = 'NO'

        if not (businessman_account_holder_name2.isalpha()):
            messages.error(request, 'User name must be alphabetic ')
            correct_info = 'NO'

        if(correct_info == 'YES'):
            businessman = Businessman_details.objects.get(email=email2)
# Edited ----------------------------------------------------------------------------------
            # try:
            #     businessman = Businessman_details.objects.get(email=email2)
            # except Businessman_details.DoesNotExist:
            #     businessman = None
# -----------------------------------------------------------------------------------------
            businessman.adhar_card = businessman_Adhar_card
            businessman.pan_card = businessman_pan_card
            businessman.gst_number = businessman_gst_number
            businessman.address = businessman_address
            businessman.bank_account_number = businessman_bank_account_no
            businessman.account_holder_name = businessman_account_holder_name
            businessman.ifsc_code = businessman_ifsc_code
            print('hy')
            businessman.save() 
            return HttpResponseRedirect('/mandi/businessman_home')


    return render(request, "businessman_complete_profile.html")

def farmer_analytics(request):
    return render(request, 'farmer_analytics.html')

def market_rates(request):
    return render(request, 'market_rates.html')

def thirty_days_market_rates(request):
    return render(request, '30days_market_rates.html')
    
def our_company(request):
    return render(request, 'our_company.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def pricing(request):
    return render(request, 'pricing.html')

def disclaimer(request):
    return render(request, 'disclaimer.html')
    
def privacy_policy(request):
    return render(request, 'privacy_policy.html')
    
def transaction_history(request):
    return render(request, 'transaction_history.html')

def added_product(request):
    return render(request, 'added_product.html')

def products_list(request, product):
    queryset = Product_details.objects.filter(product_type=product)
    list(queryset)

    return render(request, 'products_list.html', {'queryset':queryset, 'product': product})

def bidding_page(request,id):
    queryset = Product_details.objects.filter(id=id)
    current_price = queryset[0].current_price
    base_price = queryset[0].base_price
    print('method = ',request.method)
    if request.method == 'POST':
        print('hy')
        tmp_price = request.POST.get('price')
        print(tmp_price)
        tmp_price = float(tmp_price)
        print('type', type(tmp_price))

        if (current_price == 0.00) : 
            print('1')
            Product_details.objects.filter(id=id).update(current_price=tmp_price)
            return HttpResponseRedirect('/mandi/businessman_home')


        elif (tmp_price > current_price):
            print('2')
            Product_details.objects.filter(id=id).update(current_price=tmp_price)
            return HttpResponseRedirect('/mandi/businessman_home')


        else:
            messages.error(request, 'please enter price greater than current price')

    print('c r ',current_price)
    list(queryset)
    return render(request, "bidding_page.html", {'queryset':queryset})

