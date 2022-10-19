from django import views
from django.urls import path
from Ignis_Task_App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('addEvent',views.addEvent,name='addEvent'),
    path('like/<int:eid>',views.like,name="like"),
    path('dislike/<int:eid>',views.dislike,name='dislike'),
    path('allLikeEvents',views.allLikeEvents,name='allLikedEvents'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
