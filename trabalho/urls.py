from django.urls import path
from .views import IndexView, BaseView

urlpatterns = [
	path('', IndexView.as_view(), name="trabalho"),
    path('', BaseView.as_view(), name="index")
]
