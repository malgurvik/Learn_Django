from django.urls import path

from .views import (
    index,
    heads_or_tails,
    dice,
    random_number,
    main,
    about,
    heads_or_tails_stats,
    choose_game
)

urlpatterns = [
    path("", index, name="index"),
    path("heads_or_tails/", heads_or_tails, name="heads_or_tails"),
    path("heads_or_tails_stats/", heads_or_tails_stats, name="heads_or_tails_stats"),
    path("dice/", dice, name="dice"),
    path("random_number/", random_number, name="random_number"),
    path("main/", main, name="main"),
    path("about/", about, name="about"),
    path("choose_game/", choose_game, name="choose_game"),
]
