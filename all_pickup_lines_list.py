from retrieve_data import retrieve_pickup_lines


all_pickup_lines = retrieve_pickup_lines()


all_funny_pickup_lines = [
    category for category in all_pickup_lines if category["category"] == "Funny"
]

all_cheesy_pickup_lines = [
    category for category in all_pickup_lines if category["category"] == "Cheesy"
]
all_flirty_pickup_lines = [
    category for category in all_pickup_lines if category["category"] == "Flirty"
]
all_clever_pickup_lines = [
    category for category in all_pickup_lines if category["category"] == "Clever"
]
all_complimentary_pickup_lines = [
    category for category in all_pickup_lines if category["category"] == "Complimentary"
]
all_romantic_pickup_lines = [
    category for category in all_pickup_lines if category["category"] == "Romantic"
]
