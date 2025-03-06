
from django.urls import path
from . views import BooksListView, BooksDetailView, BookCheckoutView, paymentComplete, SearchResultsListView
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    
    path('', BooksListView.as_view(), name = 'list'),
    path('<int:pk>/', BooksDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
    path('logout/', LogoutView.as_view(next_page='list'), name='logout'),
    path('', views.base, name='list'),
    
    

]