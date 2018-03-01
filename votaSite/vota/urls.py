from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # ex: /
    path('', views.index, name='index'),
    # ex: /5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    

]