import os
import requests

from django.db import transaction

from django.conf import settings
from feed_parser.models import Comment, Repo, ProgLanguage


class Parser(object):

    def __init__(self, base_url=settings.FEED_URL, gh_org=settings.GITHUB_ORG, gh_owner=settings.GITHUB_OWNER):
        self.repo_host = settings.GITHUB_URL
        self.base_url = base_url
        self.gh_org = gh_org
        self.gh_owner = gh_owner
        self.API_repo_list = os.path.join(self.base_url, 'orgs', self.gh_org, 'repos')
        self.API_repo = os.path.join(self.base_url, 'repos', self.gh_owner)
        self.auth_header = {'Authorization': f'token {settings.AUTH_TOKEN}'}


    def get_all_repos(self, save=False):
        #payload = {'list': ','.join(map(str, self.product_ids))}
        r = requests.get(self.API_repo_list, headers=self.auth_header)
        all_repos = r.json()
        if save:
            for repo in all_repos:
                name = repo['name']
                url = os.path.join(self.repo_host, repo['full_name'])
                rl = requests.get(os.path.join(self.API_repo, name, 'languages'), headers=self.auth_header)
                language_ids = []
                for language in rl.json().keys():
                    language_ids.append(ProgLanguage.objects.get_or_create(name=language)[0].id)
                repo = Repo(name=name, url=url)
                repo.save()
                repo.languages.add(*language_ids)

        return all_repos
                
                
    def get_repo_names(self):
        all_repos = self.get_all_repos()
        return [repo['name'] for repo in all_repos]
        

    @transaction.atomic
    def get_all_commit_comments(self, repo_name_list, save=False):
        comments = []
        for repo in repo_name_list:
            repo_url = urljoin(self.repo, repo)
            r = requests.get(repo_url)
            comment_full = r.json()
            comment = {'body': comment_full['body'], 'username': comment_full['user']['login'], 'date': comment_full['created_at']}
            comments.append(comment)
            if save:
                comment.save()
        transaction.commit()

        return comments
