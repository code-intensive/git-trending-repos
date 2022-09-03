from django.urls import path, include


urlpatterns = [
    path('api/', include('trending_repos.urls'))
]
