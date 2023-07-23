from . import views
from django.urls import path


urlpatterns = [
    path('', views.home,name='home'),
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('page', views.page, name='page'),
    path('form',views.form,name='form'),
    path('ajax/load-branches/',views.load_branches,name='ajax_load_branches'),
    path('submit',views.submit,name='submit'),

]