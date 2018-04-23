

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    recognised_skus = 'ABCD'
    counts = {}

    for sku in skus:
        if sku in recognised_skus:
            counts[sku] += 1
        else:
            return -1

    # Compute cost
    cost = 0
    for sku in counts:
        while counts[sku] > 0:
            if sku == 'A':
                if counts[sku] / 3 > 0:
                counts[sku] -= 3
                cost + =


