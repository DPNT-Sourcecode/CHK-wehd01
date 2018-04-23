

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # The below string determines the order of iteration over the different SKUs
    recognised_skus = 'AEBCDFGHIJKLNMOPQRSTUVWXYZ'

    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50,
    }

    # Structures specifying offers
    offers_multi = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)]
    }

    offers_bogof = {
        'E': (2, 1, 'B'),
        'F': (2, 1, 'F'),
        'N': (3, 1, 'M'),
        'R': (3, 1, 'Q'),
        'U': (3, 1, 'U'),
    }

    counts = {}
    for sku in recognised_skus:
        counts[sku] = 0

    # Count the occurrences of each SKU
    for sku in skus:
        if sku in recognised_skus:
            counts[sku] += 1
        else:
            return -1

    # Compute cost
    cost = 0
    for sku in recognised_skus:
        while counts[sku] > 0:
            # TODO: refactor these branches into functions
            if sku in offers_bogof:
                offer = offers_bogof[sku]
                second_sku = offer[2]
                if counts[second_sku] > offer[1] and counts[sku] > offer[0]:
                    counts[sku] -= offer[0]
                    counts[second_sku] -= offer[1]
                    cost += prices['sku'] * offer[0]
                else:
                    counts[sku] -= 1
                    cost += prices[sku]


    return cost
