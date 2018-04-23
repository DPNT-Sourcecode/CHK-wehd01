

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
    offers_bulk = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)]
    }

    offers_bogof = {
        'F': (2, 1),
        'U': (3, 1),
    }

    offers_mix = {
        'E': (2, 1, 'B'),
        'N': (3, 1, 'M'),
        'R': (3, 1, 'Q'),
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
            offer_applied = False

            if sku in offers_mix:
                offer = offers_mix[sku]
                second_sku = offer[2]
                if counts[second_sku] / offer[1] > 0 and counts[sku] / offer[0] > 0:
                    counts[sku] -= offer[0]
                    counts[second_sku] -= offer[1]
                    cost += prices[sku] * offer[0]
                    offer_applied = True
            #         NOTE: this elif logic relies on no SKU having offers of both types
            elif sku in offers_bogof:
                offer = offers_bogof[sku]
                if counts[sku] / (offer[0] + offer[1]) > 0:
                    counts[sku] -= offer[0] + offer[1]
                    cost += offer[0] * prices[sku]
                    offer_applied = True
            elif sku in offers_bulk:
                for offer in offers_bulk[sku]:
                    if counts[sku] / offer[0] > 0:
                        counts[sku] -= offer[0]
                        cost += offer[1]
                        offer_applied = True
                        break

            if not offer_applied:
                counts[sku] -= 1
                cost += prices[sku]

    return cost
