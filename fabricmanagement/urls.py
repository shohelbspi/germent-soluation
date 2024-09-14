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

    path('machine-type/', MasterDataView.MachineTypeListView.as_view(), name='machine_type_list'),
    path('machine-type/create/', MasterDataView.MachineTypeCreateView.as_view(), name='machine_type_create'),
    path('machine-type/<int:pk>/', MasterDataView.MachineTypeDetailView.as_view(), name='machine_type_detail'),
    path('machine-type/<int:pk>/update/', MasterDataView.MachineTypeUpdateView.as_view(), name='machine_type_update'),
    path('machine-type/<int:pk>/delete/', MasterDataView.MachineTypeDeleteView.as_view(), name='machine_type_delete'),


    path('machine/', MasterDataView.MachineListView.as_view(), name='machine_list'),
    path('machine/create/', MasterDataView.MachineCreateView.as_view(), name='machine_create'),
    path('machine/<int:pk>/', MasterDataView.MachineDetailView.as_view(), name='machine_detail'),
    path('machine/<int:pk>/update/', MasterDataView.MachineUpdateView.as_view(), name='machine_update'),
    path('machine/<int:pk>/delete/', MasterDataView.MachineDeleteView.as_view(), name='machine_delete'),


    path('',views.OrderCreate,name='order_create'),
    path('save-order/', views.save_order, name='save_order'),  
    path('order-list/',views.order_list.as_view(),name='order_list'),
    path('order/<int:pk>/delete/', views.order_delete.as_view(), name='order_delete'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),

    path('add-yarn/<int:id>/', views.add_yarn, name='add_yarn'),


    # select2

    path('buyer/search/', views.buyer_search, name='buyer_search'),


]
