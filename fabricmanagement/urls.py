from django.urls import path
from fabricmanagement import views,MasterDataView


urlpatterns = [

    #Master Data

    path('buyer/', MasterDataView.BuyerListView.as_view(), name='buyer_list'),
    path('buyer/create/', MasterDataView.BuyerCreateView.as_view(), name='buyer_create'),
    path('buyer/<int:pk>/', MasterDataView.BuyerDetailView.as_view(), name='buyer_detail'),
    path('buyer/<int:pk>/update/', MasterDataView.BuyerUpdateView.as_view(), name='buyer_update'),
    path('buyer/<int:pk>/delete/', MasterDataView.BuyerDeleteView.as_view(), name='buyer_delete'),

    path('unit/', MasterDataView.UnitListView.as_view(), name='unit_list'),
    path('unit/create/', MasterDataView.UnitCreateView.as_view(), name='unit_create'),
    path('unit/<int:pk>/', MasterDataView.UnitDetailView.as_view(), name='unit_detail'),
    path('unit/<int:pk>/update/', MasterDataView.UnitUpdateView.as_view(), name='unit_update'),
    path('unit/<int:pk>/delete/', MasterDataView.UnitDeleteView.as_view(), name='unit_delete'),



    path('',views.OrderCreate,name='order_create'),
    path('save-order/', views.save_order, name='save_order'),  
    path('order-list/',views.order_list.as_view(),name='order_list'),
    path('order/<int:pk>/delete/', views.order_delete.as_view(), name='order_delete'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),

    path('add-yarn/<int:id>/', views.add_yarn, name='add_yarn'),


]
