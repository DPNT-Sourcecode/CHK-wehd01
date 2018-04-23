

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
                if counts[sku] / 2 > 0:
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
    return cost
