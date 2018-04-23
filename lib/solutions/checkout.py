# Ordering of SKUs in below string determines order of iteration
RECOGNISED_SKUS = 'STXYZAEBCDFGHIJKLNMOPRQUVW'

PRICES = {
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
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21,
}


# Structures specifying offers

GROUP_DISCOUNT = ('STXYZ', 3, 45)

OFFERS_BULK = {
    'A': [(5, 200), (3, 130)],
    'B': [(2, 45)],
    'H': [(10, 80), (5, 45)],
    'K': [(2, 120)],
    'P': [(5, 200)],
    'Q': [(3, 80)],
    'V': [(3, 130), (2, 90)]
}

OFFERS_BOGOF = {
    'F': (2, 1),
    'U': (3, 1),
}

OFFERS_MIX = {
    'E': (2, 1, 'B'),
    'N': (3, 1, 'M'),
    'R': (3, 1, 'Q'),
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = {}
    for sku in RECOGNISED_SKUS:
        counts[sku] = 0

    # Count the occurrences of each SKU
    for sku in skus:
        if sku in RECOGNISED_SKUS:
            counts[sku] += 1
        else:
            return -1

    # Compute cost
    cost = 0
    for sku in RECOGNISED_SKUS:
        while counts[sku] > 0:
            offer_applied = False

            if sku in OFFERS_MIX:
                offer = OFFERS_MIX[sku]
                second_sku = offer[2]

                if counts[second_sku] / offer[1] > 0 and counts[sku] / offer[0] > 0:
                    counts[sku] -= offer[0]
                    counts[second_sku] -= offer[1]
                    cost += PRICES[sku] * offer[0]
                    offer_applied = True

            elif sku in OFFERS_BOGOF:
                offer = OFFERS_BOGOF[sku]

                if counts[sku] / (offer[0] + offer[1]) > 0:
                    counts[sku] -= offer[0] + offer[1]
                    cost += offer[0] * PRICES[sku]
                    offer_applied = True

            elif sku in OFFERS_BULK:
                for offer in OFFERS_BULK[sku]:
                    if counts[sku] / offer[0] > 0:
                        counts[sku] -= offer[0]
                        cost += offer[1]
                        offer_applied = True
                        break

            elif sku in GROUP_DISCOUNT[0]:
                selection = [sku * counts[sku]][0]
                for offer_sku in GROUP_DISCOUNT[0]:
                    available_item_count = counts[offer_sku]
                    while offer_sku != sku and available_item_count > 0:
                        selection.append(offer_sku)
                        available_item_count -= 1

                if len(selection) >= GROUP_DISCOUNT[1]:
                    for i in range(GROUP_DISCOUNT[1]):
                        counts[selection[i]] -= 1
                    cost += GROUP_DISCOUNT[2]
                    offer_applied = True

            if not offer_applied:
                counts[sku] -= 1
                cost += PRICES[sku]

    return cost
