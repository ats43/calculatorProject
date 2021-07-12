import random


def get_random_int():
    return random.randint(0, 100)


def get_random_dec():
    return 100*random.random()


def get_random_int_seeded():
    return random.seed(1000)


def get_random_dec_seeded():
    return random.seed(1000.0)
