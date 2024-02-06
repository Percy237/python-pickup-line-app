import all_pickup_lines_list
import random


def main():
    print(f"Random : {get_random_pickup_line()}")
    print(f"Funny : {get_random_funny_pickup_line()}")
    print(f"Cheesy : {get_random_cheesy_pickup_line()}")
    print(f"Complimentary : {get_random_complimentary_pickup_line()}")
    print(f"Romantic : {get_random_romantic_pickup_line()}")
    print(f"Clever : {get_random_clever_pickup_line()}")
    print(f"Flirty : {get_random_flirty_pickup_line()}")


def get_random_pickup_line():
    random_pickup_line = random.choice(all_pickup_lines_list.all_pickup_lines)
    return random_pickup_line["text"]


def get_random_funny_pickup_line():
    random_funny_pickup_line = random.choice(
        all_pickup_lines_list.all_funny_pickup_lines
    )
    return random_funny_pickup_line["text"]


def get_random_cheesy_pickup_line():
    random_cheesy_pickup_line = random.choice(
        all_pickup_lines_list.all_cheesy_pickup_lines
    )
    return random_cheesy_pickup_line["text"]


def get_random_flirty_pickup_line():
    random_flirty_pickup_line = random.choice(
        all_pickup_lines_list.all_flirty_pickup_lines
    )
    return random_flirty_pickup_line["text"]


def get_random_clever_pickup_line():
    random_clever_pickup_line = random.choice(
        all_pickup_lines_list.all_clever_pickup_lines
    )
    return random_clever_pickup_line["text"]


def get_random_complimentary_pickup_line():
    random_complimentary_pickup_line = random.choice(
        all_pickup_lines_list.all_complimentary_pickup_lines
    )
    return random_complimentary_pickup_line["text"]


def get_random_romantic_pickup_line():
    random_romantic_pickup_line = random.choice(
        all_pickup_lines_list.all_romantic_pickup_lines
    )
    return random_romantic_pickup_line["text"]


if __name__ == "__main__":
    main()
