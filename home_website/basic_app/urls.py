from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('timesheet/', views.HomeTimesheetView.as_view(), name='timesheet'),
    path('timesheet/<int:pk>', views.HomeTimesheetDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',views.HomeTimesheetUpdate.as_view(), name='update'),
    path('delete/<int:pk>/',views.HomeTimesheetDeleteView.as_view(), name='delete'),
    path('register/',views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('reset-timesheets/', views.reset_timesheets, name='reset_timesheets'),
]
