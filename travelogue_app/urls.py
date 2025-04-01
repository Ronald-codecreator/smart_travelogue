from django.urls import path,include
from django.contrib import admin
from django.urls import path
from travelogue_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login',views.log,name="log"),
    
    path('admin_view_users',views.admin_view_users,name="admin_view_users"),
    path('adminhome', views.adminhome, name='adminhome'),
    path('admin_manage_notification', views.admin_manage_notification, name='admin_manage_notification'),
    path('admin_update_notification/<id>', views.admin_update_notification, name='admin_update_notification'),
    path('admin_delete_notification/<id>', views.admin_delete_notification, name='admin_delete_notification'),
    path('admin_view_feedback',views.admin_view_feedback,name="admin_view_feedback"),
    
    path('admin_manage_places', views.admin_manage_places, name='admin_manage_places'),
    path('admin_update_places/<id>', views.admin_update_places, name='admin_update_places'),
    path('admin_delete_delete/<id>', views.admin_delete_delete, name='admin_delete_delete'),
    
    path('admin_manage_package', views.admin_manage_package, name='admin_manage_package'),
    path('admin_update_package/<id>', views.admin_update_package, name='admin_update_package'),
    path('admin_delete_package/<id>', views.admin_delete_package, name='admin_delete_package'),
    
    path('admin_view_review',views.admin_view_review,name="admin_view_review"),

    path('admin_manage_facility', views.admin_manage_facility, name='admin_manage_facility'),
    path('admin_update_facility/<id>', views.admin_update_facility, name='admin_update_facility'),
    path('admin_delete_facility/<id>', views.admin_delete_facility, name='admin_delete_facility'),
    
    
    
    
    
    #################################################################################################################
    #################################################################################################################
    ########################################APPPPPPPPPPPPPPPPPI##########################################################
    #################################################################################################################
    path('andlogin/', views.andlogin, name='andlogin'),
    # path('user_reg', views.user_reg, name='user_reg'),
    path('view_placess', views.view_placess, name='view_placess'),
    path('view_noti', views.view_noti, name='view_noti'),
    path('view_packages', views.view_packages, name='view_packages'),
    path('user_near_by_facility', views.user_near_by_facility, name='user_near_by_facility'),
    # path('update_pass_location', views.update_pass_location, name='update_pass_location'),
    path('user_view_near_by_places', views.user_view_near_by_places, name='user_view_near_by_places'),
    path('add_travelogue', views.add_travelogue, name='add_travelogue'),
    path('View_travelogue', views.View_travelogue, name='View_travelogue'),
    path('send_rating', views.send_rating, name='send_rating'),
    path('user_view_facility',views.user_view_facility),
    path('Multi_file_upload',views.Multi_file_upload),
    path('dropdwonviewplace',views.dropdwonviewplace),


    path('searchvenue/',views.searchvenue),
    path('user_registeration/',views.user_registration),
    path('user_viewprofile/',views.user_viewprofile),
    path('user_editprofile/',views.user_editprofile),
    path('sendfeedback/',views.sendfeedback),
    path('user_add_travel/',views.user_add_travel),
    path('user_view_tra/',views.user_view_traveogue),
    path('travel_delete/',views.travel_delete),
    path('user_view_notification/',views.user_view_notification),
    path('user_view_package/',views.user_view_package),
    path('user_view_facility/',views.user_view_facility),
    path('viewcategory/',views.viewcategory),
    path('user_send_review/',views.user_send_review),
    path('user_add_media/',views.user_add_media),
    path('viewmedia/',views.viewmedia),
    path('admin_add_category/',views.admin_add_category),
    path('admin_delete_category/<id>',views.admin_delete_category),
    path('and_generateplanning/',views.and_generateplanning),
    path('user_view_places/',views.user_view_places),
    path('sindex/',views.sindex),


     
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    ]
