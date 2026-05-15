from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

from .views import (
    JournalListView, MyJournalListView, JournalDetailView, JournalCreateView,
    JournalUpdateView, JournalDeleteView,
)
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.ConnexionView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register_view, name='register'),

    path('journals/', JournalListView.as_view(), name='journal_list'),
    path('journals/mine/', MyJournalListView.as_view(), name='my_journal_list'),
    path('journals/create/', JournalCreateView.as_view(), name='journal_create'),
    path('journals/<int:pk>/', JournalDetailView.as_view(), name='journal_detail'),
    path('journals/<int:pk>/update/', JournalUpdateView.as_view(), name='journal_update'),
    path('journals/<int:pk>/delete/', JournalDeleteView.as_view(), name='journal_delete'),

   
]