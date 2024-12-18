import random
import logging

from django.db.models.expressions import result
from django.shortcuts import render
from .forms import GameForm
from .models import HeadsOrTails
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, World!")


# def heads_or_tails(request):
#     coin_flip = random.choice(['Heads', 'Tails'])
# flip = HeadsOrTails(flip_result=coin_flip)
# flip.save()
# logger.info(f"The coin flip resulted in {coin_flip}")
# context = {
#     "title": "Heads or Tails",
#     "game_name": "Heads or Tails",
#     "result": f"The coin flip resulted in '{coin_flip}'",
# }
# return render(request, "lesson01_app/game.html", context)
# return HttpResponse(f"The coin flip resulted in {coin_flip}")


def heads_or_tails(request, count):
    res = []
    for _ in range(count):
        coin_flip = random.choice(["Heads", "Tails"])
        res.append(coin_flip)
        flip = HeadsOrTails(flip_result=coin_flip)
        flip.save()
        logger.info(f"The coin flip resulted in {coin_flip}")

    context = {
        "title": "Heads or Tails",
        "game_name": "Heads or Tails",
        "result": res,
    }
    return render(request, "lesson01_app/game.html", context)


def heads_or_tails_stats(request):
    return HttpResponse(f"{HeadsOrTails.flip_statistics()}")


def dice(request, count):
    res = []
    for _ in range(count):
        dice_roll = random.randint(1, 6)
        res.append(dice_roll)
        logger.info(f"The dice rolled a {dice_roll}")
    context = {
        "title": "Dice",
        "game_name": "Dice",
        "result": res,
    }
    return render(request, "lesson01_app/game.html", context)

    # return HttpResponse(f"The dice rolled a {dice_roll}")


def random_number(request, count):
    res = []
    for _ in range(count):
        random_num = random.randint(1, 100)
        res.append(random_num)
        logger.info(f"The random number is {random_num}")
    context = {
        "title": "Random Number",
        "game_name": "Random Number",
        "result": res,
    }
    return render(request, "lesson01_app/game.html", context)
    # return HttpResponse(f"The random number is {random_num}")


def main(request):
    logger.info("Main page accessed")
    context = {"title": "Main page", "name": "Evgeny"}
    return render(request, "lesson01_app/index.html", context)


def about(request):
    logger.info("About page accessed")
    return render(request, "lesson01_app/about.html", {"title": "About"})


def choose_game(request):
    logger.info("Game page accessed")
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data["game"]
            count = form.cleaned_data["count"]
            if game == "Heads_or_Tails":
                return heads_or_tails(request, count)
            elif game == "Dice":
                return dice(request, count)
            elif game == "Random_Number":
                return random_number(request, count)

    else:
        form = GameForm()
        return render(request, "lesson01_app/choose_game.html", {"form": form})
