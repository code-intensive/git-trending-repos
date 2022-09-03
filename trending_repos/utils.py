from datetime import datetime, timedelta

from requests import Response

from git_trending_repos.constants import DATE_FORMAT, REPO_COUNT, REPO_LIST


def calculate_days_ago(days: int = 30) -> str:
    """ 

    Calculate the difference in days between today and the given `days` arg

    args:
        * days - An integer representing the number of days before today
        
    returns `datetime.datetime.strftime` of the date in `yyyy-mm-dd` format

    """

    # TODO could do some validation here to ensure only a valid integer is passed
    days_ago = (datetime.today() - timedelta(days))
    return days_ago.strftime(DATE_FORMAT)


def parse_trending_repos(response: Response) -> dict:
    """ Parses the trending repositories from github's API response"""
    trending_repos = response.json()['items']
    parsed_trending_repos: dict = {}

    for trending_repo in trending_repos:
        lang_used = trending_repo['language']
        repo_reference = parsed_trending_repos.setdefault(lang_used, {REPO_COUNT:0, REPO_LIST: []})
        repo_reference[REPO_COUNT] += 1
        repo_reference[REPO_LIST].append({'api_url': trending_repo['url'], 'web_url': trending_repo['html_url']})
    return parsed_trending_repos
