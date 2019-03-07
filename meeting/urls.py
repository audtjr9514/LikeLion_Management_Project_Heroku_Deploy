from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name="new" ),
    path('create/', views.create, name="create" ),
    path('detail/', views.detail, name="detail"),
    path('<int:meet_id>', views.detail, name="detail")
]
