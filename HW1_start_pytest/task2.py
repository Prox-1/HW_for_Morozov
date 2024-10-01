def gorgons_machinations(n: int, bills: list, gorgona_moneys: int):
    if n > 40:
        return "Too many husbands"
    elif n != len(bills):
        return "The number of husbands and the number of bills do not match"
    elif gorgona_moneys > 109:
        return "The Gorgon's bill is too high"

    bills.sort()
    for bill in bills:
        if bill < 0:
            return "Negative value is not possible"
        if gorgona_moneys > bill:
            continue
        gorgona_moneys = (gorgona_moneys + bill) / 2
    return gorgona_moneys
