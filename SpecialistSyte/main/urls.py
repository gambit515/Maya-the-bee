from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',StartPageView.as_view(), name = 'start'),
    path('main/',views.mainsheet, name = 'main'),
    path('index/',views.index, name = 'index'),
    path('profile/',views.profile, name = 'prof'),
    path('login/',views.login, name = 'log'),
    path('createanketas/',AnketaView.as_view(), name = 'anket'),
    path('registration/',CreatePostView.as_view(), name='reg'),
    path('test/',TestView.as_view(), name='test'),
    path('ankets/<int:anket_id>/', show_anket, name='ankets'),
    path('soft_cat/<int:soft_cat_id>/', show_soft_cat, name='soft_cat'),
    path('lang_cat/<int:lang_cat_id>/', show_lang_cat, name='lang_cat'),
]
