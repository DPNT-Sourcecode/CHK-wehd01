

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

    for sku in counts:
        

