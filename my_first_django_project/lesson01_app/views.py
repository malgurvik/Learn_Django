import random
import logging

from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("Hello, World!")


def heads_or_tails(request):
    coin_flip = random.choice(['Heads', 'Tails'])
    logger.info(f"The coin flip resulted in {coin_flip}")
    return HttpResponse(f"The coin flip resulted in {coin_flip}")


def dice(request):
    dice_roll = random.randint(1, 6)
    logger.info(f"The dice rolled a {dice_roll}")
    return HttpResponse(f"The dice rolled a {dice_roll}")

def random_number(request):
    random_num = random.randint(1, 100)
    logger.info(f"The random number is {random_num}")
    return HttpResponse(f"The random number is {random_num}")
