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

    path('yarn-count/', MasterDataView.YarnCountListView.as_view(), name='yarn_count_list'),
    path('yarn-count/create/', MasterDataView.YarnCountCreateView.as_view(), name='yarn_count_create'),
    path('yarn-count/<int:pk>/', MasterDataView.YarnCountDetailView.as_view(), name='yarn_count_detail'),
    path('yarn-count/<int:pk>/update/', MasterDataView.YarnCountUpdateView.as_view(), name='yarn_count_update'),
    path('yarn-count/<int:pk>/delete/', MasterDataView.YarnCountDeleteView.as_view(), name='yarn_count_delete'),

    path('yarn-type/', MasterDataView.YarnTypeListView.as_view(), name='yarn_type_list'),
    path('yarn-type/create/', MasterDataView.YarnTypeCreateView.as_view(), name='yarn_type_create'),
    path('yarn-type/<int:pk>/', MasterDataView.YarnTypeDetailView.as_view(), name='yarn_type_detail'),
    path('yarn-type/<int:pk>/update/', MasterDataView.YarnTypeUpdateView.as_view(), name='yarn_type_update'),
    path('yarn-type/<int:pk>/delete/', MasterDataView.YarnTypeDeleteView.as_view(), name='yarn_type_delete'),


    path('',views.OrderCreate,name='order_create'),
    path('save-order/', views.save_order, name='save_order'),  
    path('save-yarn/', views.save_yarn, name='save_yarn'),  
    path('order-list/',views.order_list.as_view(),name='order_list'),
    path('order/<int:pk>/delete/', views.order_delete.as_view(), name='order_delete'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),

    path('add-yarn/<int:order_id>/<int:item_id>/', views.add_yarn_view, name='add_yarn'),

    path('add-knitcard/<int:id>/', views.add_knitcard_view, name='add_knitcard_view'),
    path('knitcards/', views.KnitCardListView.as_view(), name='knitcard_list'),



    # select2
    path('buyer/search/', views.buyer_search, name='buyer_search'),
    path('yarn-count-list', views.yarn_count_list, name='yc_list'),
    path('yarn-type-list', views.yarn_type_list, name='yt_list'),

    path('unit-select2-list', views.unit_select2, name='unit_select2'),
    path('machine-select2-list', views.machine_select2, name='machine_select2'),


]
