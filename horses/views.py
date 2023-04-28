import json
from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime
from .serializers import HorseSerializer
from .models import Horse
from .horse_query import horse_query

class HorseDetail(generics.RetrieveAPIView):
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer
    lookup_field = 'nft_id'

    def retrieve(self, request, *args, **kwargs):
        horse_id = kwargs.get('pk')
        summary_horse_data = horse_query(horse_id)
        print(summary_horse_data)
        
        try:
            horse = Horse.objects.get(nft_id=horse_id)
            horse.bloodline = summary_horse_data.get('bloodline')
            horse.breed_type = summary_horse_data.get('breed_type')
            horse.color = summary_horse_data.get('color')
            horse.gen = summary_horse_data.get('gen')
            horse.horse_type = summary_horse_data.get('horse_type')
            horse.img_url = summary_horse_data.get('img_url')
            horse.inserted_at = datetime.strptime(summary_horse_data.get('inserted_at'), '%Y-%m-%dT%H:%M:%S')
            horse.name = summary_horse_data.get('name')
            horse.offsprings = json.dumps(summary_horse_data.get('offsprings'))
            horse.parents = json.dumps(summary_horse_data.get('parents'))
            race_stats = summary_horse_data.get('race_statistic')
            positions_per_distance = race_stats.get('positions_per_distance')
            positions = json.dumps(positions_per_distance) if len(positions_per_distance) > 0 else []
            horse.race_statistic = json.dumps({
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
            horse.save()
            serializer = HorseSerializer(horse)
        except Horse.DoesNotExist:
            horse = Horse.create_from_graphql(summary_horse_data)
            serializer = HorseSerializer(horse)
        return Response(serializer.data)
