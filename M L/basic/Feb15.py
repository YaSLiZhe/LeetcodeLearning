def recur(n):
    res = 0
    if n == 1:
        return 1
    res = recur(n-1)
    return n + res

def tail_recur(n, res):
    if n == 0:
        return res
    return tail_recur(n - 1, res + n)

# O(2^n)
def exp_recur(n):
    if n == 1:
        return 1
    return exp_recur(n-1) + exp_recur(n-1)

if __name__ == "__main__":
    n=5
    res = recur(n)
    res1 = tail_recur(n, 0)
    res2 = exp_recur(7)
    print(res, res1, res2)