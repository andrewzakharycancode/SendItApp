from django.urls import path
from . import views

urlpatterns = [
    # URLs for Email model
    path('emails/', views.EmailListCreateView.as_view(), name='email-list-create'),
    path('emails/<int:pk>/', views.EmailDetailView.as_view(), name='email-detail'),

    # URLs for PhoneNumber model
    path('phone-numbers/', views.PhoneNumberListCreateView.as_view(), name='phone-number-list-create'),
    path('phone-numbers/<int:pk>/', views.PhoneNumberDetailView.as_view(), name='phone-number-detail'),

    # URLs for Address model
    path('addresses/', views.AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', views.AddressDetailView.as_view(), name='address-detail'),

    # URLs for User model
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),

    # URLs for Relationship model
    path('relationships/', views.RelationshipListCreateView.as_view(), name='relationship-list-create'),
    path('relationships/<int:pk>/', views.RelationshipDetailView.as_view(), name='relationship-detail'),

    # URLs for Contact model
    path('contacts/', views.ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='contact-detail'),

    # URLs for Message model
    path('messages/', views.MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', views.MessageDetailView.as_view(), name='message-detail'),
]
