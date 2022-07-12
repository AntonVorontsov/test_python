import math


# BEGIN (write your solution here)

def make(numer, denom):
    gcd = math.gcd(numer, denom)
    return {"numer": numer // gcd, "denom": denom // gcd}


def get_numer(rat):
    return rat["numer"]


def get_denom(rat):
    return rat["denom"]


def add(rat1, rat2):
    numer1 = get_numer(rat1) * get_denom(rat2)
    numer2 = get_numer(rat2) * get_denom(rat1)
    numer = numer1 + numer2
    denom = get_denom(rat1) * get_denom(rat2)
    return make(numer, denom)


def sub(rat1, rat2):
    numer1 = get_numer(rat1) * get_denom(rat2)
    numer2 = get_numer(rat2) * get_denom(rat1)
    numer = numer1 - numer2
    denom = get_denom(rat1) * get_denom(rat2)
    return make(numer, denom)


def rat_to_string(rat):
    return "{}/{}".format(get_numer(rat), get_denom(rat))

# END


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"
