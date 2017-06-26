def check_const(a, b, c):
    return (c >= a+b) and (c <= 2* b)

def stingy(total_lambs):
    check = [1,1]
    i = 2
    cur_tot = 2
    while True:
        next = check[i-1] + check[i-2]
        cur_tot += next
        if cur_tot > total_lambs:
            rem = total_lambs + next - cur_tot
            if i >= 2 and check_const(check[-2], check[-1], rem):
                check.append(rem)
            break
        check.append(next)
        i += 1
    return len(check)

def generous(total_lambs):
    i = 0
    cur_tot = 0
    check = []
    while True:
        val = 2 ** i
        cur_tot += val
        if cur_tot > total_lambs:
            rem = total_lambs + val - cur_tot
            if i >= 2 and check_const(check[-2], check[-1], rem):
                check.append(rem)
            break
        check.append(val)
        i += 1
    return len(check)

def answer(total_lambs):
    if total_lambs < 10 or total_lambs > 10**9:
        return 0
    num_gen = generous(total_lambs)
    num_sti = stingy(total_lambs)
    return num_sti - num_gen