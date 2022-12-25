from django.urls import path
from . import views 
urlpatterns = [
    path('',views.index, name='index'),

    path('farmer-signup/',views.farmer_signup, name='farmer-signup'),
    path("farmer-login/", views.farmer_login, name="farmer-login"),
    path("farmer_otp/", views.farmer_confirm_otp, name="farmer_otp"),
    path("farmer_home/", views.farmer_home, name="farmer_home"),
    path("farmer_home/farmer_complete_profile/",views.farmer_complete_profile,
    name="farmer_complete_profile"),
    path("farmer_home/product_form/", views.product_form, name="product_form"),
    path("farmer_home/added_product/", views.added_product, name="added_product"),
    path("farmer_home/transaction_history/", views.transaction_history, name="transaction_history"),
    path("farmer_analytics/", views.farmer_analytics, name="farmer_analytics"),
    path("market_rates/", views.market_rates, name="market_rates"),
    path("market_rates/thirty_days_market_rates", views.thirty_days_market_rates, name="thirty_days_market_rates"),
    path("about/our_company/", views.our_company, name="our_company"),
    path("about/contact_us/", views.contact_us, name="contact_us"),
    path("pricing/", views.pricing, name="pricing"),
    path("disclaimer/", views.disclaimer, name="disclaimer"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),

    path('businessman-signup/',views.businessman_signup, name='businessman-signup'),
    path("businessman-login/", views.businessman_login, name="businessman-login"),
    path("businessman_otp/", views.businessman_confirm_otp, name="farmer_otp"),
    path("businessman_home/", views.businessman_home, name="businessman_home"),
    path("businessman_home/products_list/<str:product>", views.products_list, name="products_list"),
    path("businessman_home/businessman_complete_profile/",views.businessman_complete_profile,
    name='businessman_complete_profile'),
    path("businessman_home/bidding/<id>", views.bidding_page, name='bidding_page')

    # path("businessman_home/bidding_products/<str:product>",views.bidding_products, name='bidding_products' )
    # path('businessman_home/soyabeen_page/',views.soyabeen_page, name='soyabeen' )

]