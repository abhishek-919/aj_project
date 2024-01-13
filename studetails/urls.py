from django.urls import path
from .views import student_view_set

urlpatterns = [
    path('create/', student_view_set.as_view({
        'post': 'create'
    })),
    path('view/<str:pk>', student_view_set.as_view({
        'get': 'retrieve_mobilenumber'
    })),
    path('view/reg/<str:pk>', student_view_set.as_view({
        'get': 'retrieve_regnumber'
    })),
]
