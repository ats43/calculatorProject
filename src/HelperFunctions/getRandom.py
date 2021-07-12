import random
random.seed(1000)


def get_random_int():
    return random.randint(0, 100)


def get_random_dec():
    return 100*random.random()


def get_random_int_list():
    random_lst = []
    for i in range(0,1000):
        n = random.randint(0,100)
        random_lst.append(n)
    return random_lst

# def get_random_int_seeded():
#     return random.seed(1000)
#
#
# def get_random_dec_seeded():
#     return random.seed(1000.0)
#
# def get_random_int_list_seeded():
#     return