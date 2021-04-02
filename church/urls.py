from django.urls import path
from .views import Home, SermonView, EventView, VisitorView
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('sermon', SermonView.as_view(), name='sermon'),
    path("event/", EventView.as_view(), name="event"),
    path("visitor", VisitorView.as_view(), name="visit")
]
