from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.home),
	url(r'home/$', views.home),
	url(r'student_info/$' , views.student_info),
	url(r'centre_info/$' , views.centre_info),
	url(r'centre_alloc/$' , views.centre_alloc),
	url(r'roll_no_info/$' , views.roll_no_info),
	url(r'show_result/$' , views.show_result),
    # Examples:
    # url(r'^$', 'summer_proj.views.home', name='home'),
    # url(r'^summer_proj/', include('summer_proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
