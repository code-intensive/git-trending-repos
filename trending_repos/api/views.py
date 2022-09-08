import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view

from git_trending_repos.constants import BASE_REPOSITORY_SEARCH_URL
from trending_repos.utils import calculate_days_ago, parse_trending_repos


@api_view(['GET'])
def top_trending_repos(request) -> Response:
    """ 
    RESTFul API endpoint for retrieving a dictionary of the top 100
    github repositories based on the number of stars the repositories possess
    """

    GITHUB_QUERY_URL = BASE_REPOSITORY_SEARCH_URL + (
        F'?q=created:>{ calculate_days_ago() }'
        '&sort=stars&order=desc&page=1&per_page=100'
    )
    response = requests.get(GITHUB_QUERY_URL)

    if response.status_code == 200:
        return Response(data=parse_trending_repos(response))
    return Response(data=response.json(), status=response.status_code)
