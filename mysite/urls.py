from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
#from home import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'',include('blog.urls')),
    #url(r'^$', views.index),
    url(r'^$', TemplateView.as_view(template_name='static_page/index.html'), name='home'),

]
