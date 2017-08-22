from django.conf.urls import url

from . import views


app_name = 'poker'
urlpatterns = [

    # /homepage/
    url(r'^$', views.index, name="index"),
    # /profile/
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name="profile"),
    # /game/
    url(r'^game/$', views.game, name='game'),
    # /register/
    url(r'^register/$', views.UserFormView.as_view(), name="register"),
    ]
