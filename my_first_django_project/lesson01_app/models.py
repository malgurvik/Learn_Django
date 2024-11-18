from django.db import models


# Create your models here.
class HeadsOrTails(models.Model):
    flip_result = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def flip_statistics():
        total_flips = HeadsOrTails.objects.count()
        heads_count = HeadsOrTails.objects.filter(flip_result='Heads').count()
        tails_count = HeadsOrTails.objects.filter(flip_result='Tails').count()
        return (f'Total flips: {total_flips}, Heads: {heads_count}, Tails: {tails_count}, '
                f'Heads percentage: {heads_count / total_flips * 100:.2f}%,'
                f'Tails percentage: {tails_count / total_flips * 100:.2f}%')




