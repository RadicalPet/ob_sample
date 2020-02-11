from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from feed_parser.parse_feed import Parser


class Command(BaseCommand):
    help = "Populate Database with shopify repo info"

    def add_arguments(self, parser):
        parser.add_argument(
            "repos",
            nargs="?",
            default=None,
            type=str,
            help="space separated repo names, None for sample list",
        )

    def handle(self, *args, **options):
        repos = options["repos"]
        if repos is None:
            repos = settings.SAMPLE_REPOS
        parser = Parser()
        parser.get_all_repos(save=True)
        parser.get_all_commit_comments(settings.SAMPLE_REPOS, save=True)
        self.stdout.write(self.style.SUCCESS("feed successfully parsed"))
