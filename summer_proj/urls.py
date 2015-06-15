from django.conf.urls import patterns, include, url
from summer_proj import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.home),
	url(r'home/$', views.home),     				#Home Page
	url(r'student_info/$' , views.student_info),    #For entering student Info.
	url(r'centre_info/$' , views.centre_info),      #For entering centre info.
	url(r'centre_alloc/$' , views.centre_alloc),    #Link to generate random roll numbers and allocate centres.
	url(r'roll_no_info/$' , views.roll_no_info),    #Views content of Roll No. Info.xls
	url(r'generate_result/$' , views.result_evaluator),#To generate new results
	url(r'show_result/$' , views.show_result),      #To show the results.
	url(r're_evaluate/$' , views.re_evaluate),		# To re-evaluate result based on questions r4emoved from evaluation
	url(r'analysis/$' , views.analysis),			# To show question wise analysis.
    # Examples:
    # url(r'^$', 'summer_proj.views.home', name='home'),
    # url(r'^summer_proj/', include('summer_proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
