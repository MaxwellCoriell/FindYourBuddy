from django.conf.urls import url
import fyb_web.views


urlpatterns = [
    url(r'^$', fyb_web.views.index, name='index'),
    url(r'^login$', fyb_web.views.login_user, name='login'),
    url(r'^logout$', fyb_web.views.user_logout, name='logout'),
    url(r'^register$', fyb_web.views.register, name='register'),
    url(r'^view_account$', fyb_web.views.view_account, name='view_account'),
    url(r'lost_pet_post', fyb_web.views.lost_pet_post, name='lost_pet_post'),
    url(r'found_pet_post', fyb_web.views.found_pet_post, name='found_pet_post')
]