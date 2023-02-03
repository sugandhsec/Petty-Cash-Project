from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('back/',views.back,name='back'),
    path('change_password/',views.change_password,name='change_password'),
    path('new_password/',views.new_password,name='new_password'),
    path('photo_capture/',views.photo_capture,name='photo_capture'),
    path('visitor_view/',views.visitor_view,name='visitor_view'),
    path('visitor_exit/',views.visitor_exit,name='visitor_exit'),
    path('mail/',views.mail , name="mail"),
    path('camera/',views.camera , name="camera"),
    path('<id>/update', views.update_view ),
    path('edit_exit/<int:id>',views.edit_exit,name='edit_exit'),
    path('exit_user/<int:pk>',views.exit_user,name='exit_user'),
    path('return_amount/<int:pk>',views.return_amount,name='return_amount'),

    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('send_email/<int:pk>',views.send_email,name='send_email'),
    path('ajax/validate_email/',views.validate_email,name='validate_email'),
    path('visitor_search/',views.visitor_search,name='visitor_search'),
    path('visitor_entry/<int:pk>',views.visitor_entry,name='visitor_entry'),
   #path('visitor_login/',views.visitor_login,name='visitor_login'),
    #path('visitor_signup/',views.visitor_signup,name='visitor_signup'),
    path('visitor_log/',views.visitor_log,name='visitor_log'),
    path('add_amount/',views.add_amount,name='add_amount'),
    path('view_cash/',views.view_cash,name='view_cash'),
   


    
]