from django.urls import path

from trending_repos.api.views import top_trending_repos

app_name = 'trending_repos'

urlpatterns = [
    path('trending_langs/', top_trending_repos, name='top-trending-repos'),
]
