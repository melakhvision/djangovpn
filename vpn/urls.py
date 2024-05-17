from django.urls import include, path

from core import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    # path('api/', include(category_router.urls)),
    # path('api/health', views.health_check),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    # path('create_user/', views.create_user, name='create_user'),
    path('delete/<int:id>/', views.delete, name='delete')
]
