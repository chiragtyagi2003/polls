from django.urls import path
from . import views

# url patterns

urlpatterns = [
    # param1 => path route
    # param2 => the view we want to call
    # param3 => the name for this view to refer later
    path("", views.index, name = 'index')
]