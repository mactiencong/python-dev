memorize = {}
def fac(nagative):
    if nagative<2: return 1
    if nagative not in memorize:
        return nagative*fac(nagative-1)
    return memorize[nagative]

print fac(10)