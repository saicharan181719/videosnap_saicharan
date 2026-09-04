from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup/',views.signup_view,name="signup"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('contactus/',views.contactus,name="contactus"),
    path('forgotpass/',views.forgotpass,name="forgotpass"),
    path('resetpass/',views.resetpass,name="resetpass"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('profile/',views.profile_view,name="profile"),
    path('edit_profile/',views.edit_profile_view,name="edit_profile"),
    path('faq/',views.faq,name="faq"),
    path('privacypolicy/',views.privacypolicy,name="privacypolicy"),
    path('tandc/',views.tandc,name="tandc"),
    path('features/',views.features,name="features"),
    path('services/',views.services,name="services"),
    path('testimonials/',views.testimonials,name="testimonials"),
    path('helpcentre/',views.helpcentre,name="helpcentre"),
    path('blog/',views.blog,name="blog"),
    path('news/',views.news,name="news"),
    path('cookie/',views.cookie,name="cookie"),
    path('accessibility/',views.accessibility,name="accessibility"),
    path('careers/',views.careers,name="careers"),
    path('partners/',views.partners,name="partners"),
    path('community/',views.community,name="community"),
    path('events/',views.events,name="events"),
    path('releasenotes/',views.releasenotes,name="releasenotes"),
    path('roadmap/',views.roadmap,name="roadmap"),
    path('about/',views.about,name="about"),
    path('ad/',views.ad,name="ad"),
    path('sub/',views.sub,name="sub"),
    path('mul/',views.mul,name="mul"),
    path('div/',views.div,name="div"),
    path('sqrt/',views.sqrt,name="sqrt"),
    path('add_details/',views.add_details_view,name="add_details"),
    path('my_profile/',views.my_profile_view,name="my_profile")
]

