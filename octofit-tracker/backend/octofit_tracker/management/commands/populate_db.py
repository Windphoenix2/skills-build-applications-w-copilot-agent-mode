from django.core.management.base import BaseCommand
from djongo import models
from octofit_tracker import models as octofit_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        octofit_models.User.objects.all().delete()
        octofit_models.Team.objects.all().delete()
        octofit_models.Activity.objects.all().delete()
        octofit_models.Leaderboard.objects.all().delete()
        octofit_models.Workout.objects.all().delete()

        # Create teams
        marvel = octofit_models.Team.objects.create(name='Marvel')
        dc = octofit_models.Team.objects.create(name='DC')

        # Create users
        ironman = octofit_models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = octofit_models.User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = octofit_models.User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = octofit_models.User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create activities
        octofit_models.Activity.objects.create(user=ironman, type='Run', duration=30)
        octofit_models.Activity.objects.create(user=batman, type='Swim', duration=45)

        # Create workouts
        octofit_models.Workout.objects.create(user=superman, description='Strength training')
        octofit_models.Workout.objects.create(user=captain, description='Cardio')

        # Create leaderboard
        octofit_models.Leaderboard.objects.create(team=marvel, points=100)
        octofit_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
