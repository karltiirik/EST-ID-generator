from random import randint


def gen_est_id():
    id = ""

    # gender and century
    id += rand_int(1, 8)
    # birth date (future dates included)
    id += rand_birth_date()
    # nth baby that day
    id += rand_int(0, 999)
    # calculate checksum
    id += calc_checksum(id)

    return id


def rand_birth_date():
    # creates a random birth date, returns as a string
    bd = ""

    # months that don't have 31 days
    MON_30_DAYS = ['04', '06', '09', '11']
    MON_28_DAYS = ['28']
    
    # year and month
    bd += rand_int(0, 99)
    bd += rand_int(1, 12)
    # day
    if bd[3:5] in MON_30_DAYS:
        bd += rand_int(1, 30)
    elif bd[3:5] in MON_28_DAYS:
        bd += rand_int(1, 28)
    else:
        bd += rand_int(1, 31)
    return bd


def rand_int(mn, mx):
    # generates a random int between mn and mx
    # and pads it with "0"-s, returns as a string
    r_int = ""
    rand_nr = str(randint(mn, mx))

    # padding
    if len(rand_nr) < len(str(mx)):
        for i in range(len(str(mx)) - len(rand_nr)):
            r_int += "0"
    r_int += rand_nr

    return r_int


def calc_checksum(numbers):
    # calculate checksum with Modulo 11 and weights,
    # returns checksum as a string
    LVL_1_WEIGHTS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    LVL_2_WEIGHTS = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    cs = 0

    remainder = modulo_11(numbers, LVL_1_WEIGHTS)
    if remainder != 10:
        cs = remainder
    else:
        remainder = modulo_11(numbers, LVL_2_WEIGHTS)
        if remainder != 10:
            cs = remainder

    return str(cs)


def modulo_11(numbers, weights):
    # Modulo 11 method with weights 
    sum = 0

    for i in range(len(numbers)):
        sum += int(numbers[i]) * weights[i]

    return sum % 11


print(gen_est_id())
