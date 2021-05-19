from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index),
    # path('basket-page', views.basket_page)
    path('<slug:category_slug>/', views.index,
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', views.index,
         name='product_detail')
]
