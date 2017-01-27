from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User

# Create your models here.

class LeaderboardManageer(models.Manager):
    def update_score(self, data):

        str_id = int(data['id'])
        str_score = int(data['score'])

        ##find if user
        current_user = User.objects.get(id=str_id)
        #if so:
        print 'success'
        print current_user
        #find if Leaderboard for user:
        try:
            # below is equivalent to    board = Leaderboard.objects.get(user=current_user)
            board = self.get(user=current_user)
            if board.top_score > str_score:
                board.top_score = str_score
            board.games_played += 1
            board.total_gold_earned += str_score
            board.save()
            print board.total_gold_earned, "updated the board"
            # board.total_gold_earned == 0
        except:
            # below is equivalent to    board = Leaderboard.objects.create(......)
            board = self.create(
                user=current_user,
                top_score=data['score'],
                games_played=1,
                total_gold_earned=data['score']
            )
            print board, "-----we made a new board-----"
        # print 'none exists'


class Leaderboard(models.Model):
    user = models.OneToOneField(User)
    top_score = models.IntegerField()
    games_played = models.IntegerField()
    total_gold_earned = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LeaderboardManageer()
