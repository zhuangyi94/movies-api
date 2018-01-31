# movies-api/movies/movies/urls.py

...
from django.conf.urls import url, include # add include as an import here
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('api.urls')) # add this line
]