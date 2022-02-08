from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

from mv.models import Question, Movie


@receiver(post_save, sender=Question)
def on_post_question_save(sender, instance: Question, created: bool, raw: bool, using, update_fields, **kwargs):
    movie: Movie = instance.movie

    review_point = movie.question_set.aggregate(Avg('score'))['score__avg']
    movie.review_point = review_point
    movie.save()
