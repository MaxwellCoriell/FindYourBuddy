from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'lost_pet_post', views.lost_pet_post, name='lost_pet_post'),
    url(r'found_pet_post', views.found_pet_post, name='found_pet_post'), ]