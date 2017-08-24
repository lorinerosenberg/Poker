from django.conf.urls import url, include

from . import views


app_name = 'poker'
urlpatterns = [

    # /homepage/
    url(r'^$', views.index, name="index"),
    # /profile/
    url(r'^profile/$', views.profile, name="profile"),
    # /game/
    url(r'^game/$', views.game, name='game'),
    # /register/
    url(r'^register/$', views.UserFormView.as_view(), name="register"),
    # /login/
    url(r'^login/$', views.login_view, name='login'),
    # /logout/
    url(r'^logout/$', views.logout_view, name='logout'),


]
