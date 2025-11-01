from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('', LoginView.as_view(template_name="core/login.html"), name="login_view"),
    path('register/', views.RegisterView.as_view(), name="register_view"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('logout/', LogoutView.as_view(next_page='login_view'), name="logout"),
    
    # profile views
    path('user/<int:pk>/', views.UserProfileView.as_view(), name="profile"),
    
    # crud operations
    path('service/detail/<int:pk>/<slug:slug>/', views.ServiceDetailView.as_view(), name="service_detail_view"),
    path('service/add/', views.AddServiceView.as_view(), name="add_service"),
    path('service/<int:pk>/delete/', views.DeleteServie.as_view(), name="delete_service"),
    path('service/<int:pk>/update/', views.UpdateServiceView.as_view(), name="update_service"),
    
    # Booking Crud operations
    path('service/book/<int:pk>/', views.BookServiceView.as_view(), name="booking_view"),
    
    # manage service
    path('user/<int:pk>/manage/', views.ManageServiceView.as_view(), name="manage_service"),
    
    # error page
    path('404/', views.View404.as_view(), name="404_page")
]
