from library import views 
from django.urls import path

# importing views from views..py


urlpatterns = [
	path('', views.Home_page),
    path("Book/",views.Books_page),
    path('Book_detail/<int:id>/',views.Book_detail)
	
]
