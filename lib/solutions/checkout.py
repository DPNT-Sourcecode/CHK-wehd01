

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    recognised_skus = 'AEBCD'
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

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
                if counts[sku] / 5 > 0:
                    counts[sku] -= 5
                    cost += 200
                elif counts[sku] / 3 > 0:
                    counts[sku] -= 3
                    cost += 130
                else:
                    counts[sku] -= 1
                    cost += 50
            elif sku == 'B':
                if counts[sku] / 2 > 0:
                    counts[sku] -= 2
                    cost += 45
                else:
                    counts[sku] -= 1
                    cost += 30
            elif sku == 'C':
                counts[sku] -= 1
                cost += 20
            elif sku == 'D':
                counts[sku] -= 1
                cost += 15
            elif sku == 'E':
                if counts['B'] >
    return cost
