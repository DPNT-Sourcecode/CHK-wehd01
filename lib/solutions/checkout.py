

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # The below string determines the order of iteration over the different SKUs
    recognised_skus = 'AEBCDFGHIJKLNMOPQRSTUVWXYZ'

    prices = {
        'A': 50,
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
            if sku == 'A':
                if counts['A'] / 5 > 0:
                    counts['A'] -= 5
                    cost += 200
                elif counts['A'] / 3 > 0:
                    counts['A'] -= 3
                    cost += 130
                else:
                    counts[sku] -= 1
                    cost += 50
            elif sku == 'B':
                if counts['B'] / 2 > 0:
                    counts['B'] -= 2
                    cost += 45
                else:
                    counts['B'] -= 1
                    cost += 30
            elif sku == 'C':
                counts['C'] -= 1
                cost += 20
            elif sku == 'D':
                counts['D'] -= 1
                cost += 15
            elif sku == 'E':
                if counts['B'] > 0 and counts['E'] / 2 > 0:
                    counts['B'] -= 1
                    counts['E'] -= 2
                    cost += 80
                else:
                    counts['E'] -= 1
                    cost += 40
            elif sku == 'F':
                if counts['F'] / 3 > 0:
                    counts['F'] -= 3
                    cost += 20
                else:
                    counts['F'] -= 1
                    cost += 10
    return cost
