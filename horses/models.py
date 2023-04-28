import json
from django.db import models
from datetime import datetime

# Create your models here.
class Horse(models.Model):
    bloodline = models.CharField(max_length=255)
    breed_type = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    gen = models.CharField(max_length=4)
    horse_type = models.CharField(max_length=255)
    img_url = models.URLField()
    inserted_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    nft_id = models.IntegerField(unique=True)
    offsprings = models.JSONField()
    parents = models.JSONField()
    race_statistic = models.JSONField()

    def __str__(self):
        return "{}, {}, {} {}".format(self.name, self.gen, self.bloodline, self.breed_type)

    @classmethod
    def create_from_graphql(cls, data):
        race_stats = data.get('race_statistic')
        positions_per_distance = race_stats.get('positions_per_distance')
        positions = json.dumps(positions_per_distance) if len(positions_per_distance) > 0 else []
        horse = cls(
            bloodline=data.get('bloodline'),
            breed_type=data.get('breed_type'),
            color=data.get('color'),
            gen=data.get('gen'),
            horse_type=data.get('horse_type'),
            img_url=data.get('img_url'),
            inserted_at=datetime.strptime(data.get('inserted_at'), '%Y-%m-%dT%H:%M:%S'),
            name=data.get('name'),
            nft_id=data.get('nft_id'),
            offsprings=json.dumps(data.get('offsprings')),
            parents=json.dumps(data.get('parents')),
            race_statistic=json.dumps({
                'first_place_finishes': race_stats.get('first_place_finishes'),
                'second_place_finishes': race_stats.get('second_place_finishes'),
                'third_place_finishes': race_stats.get('third_place_finishes'),
                'number_of_races': race_stats.get('number_of_races'),
                'win_rate': race_stats.get('win_rate'),
                'number_of_free_races': race_stats.get('number_of_free_races'),
                'number_of_paid_races': race_stats.get('number_of_paid_races'),
                'free_win_rate': race_stats.get('free_win_rate'),
                'paid_win_rate': race_stats.get('paid_win_rate'),
                'positions_per_distance': positions
            })
        )
        horse.save()
        return horse
