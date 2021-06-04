from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "Appsarathii"

urlpatterns = [
    path('', Index, name='Index'),
    path('register/', Registration_p, name='Registration'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)