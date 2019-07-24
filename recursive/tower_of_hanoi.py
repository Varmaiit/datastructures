# Code related to Tower of hanoi in python using recursive code


def printMove(fr , to):
    print('Move from {fr} to {to}'.format(fr=fr, to=to))

def Towers(n , fr , to, spare):
    count = 0
    if n== 1:
        printMove(fr, to)
        count += 1
    else:
        count += Towers(n-1, fr, spare, to)
        count += Towers(1, fr, to, spare)
        count += Towers(n-1, spare, to, fr)
    return count


if __name__ == "__main__":
    print(Towers(5, 'f', 't', 's'))