from django.conf.urls import url, include
# from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.registration.urls', namespace='loginreg')),
    url(r'^travels/', include('apps.belt_main.urls', namespace='travels')),
    # url(r'^admin/', admin.site.urls),
]
