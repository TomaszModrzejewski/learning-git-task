import sys

debug = False
if len(sys.argv) > 1:
    debug = True

def main():
    tab = ['0' for x in range(10)]
    for linia in sys.stdin:
        znak, l1, l2 = linia.split()
        l1, l2 = int(l1), int(l2)
        if debug is True:
            print(znak, l1, l2)
        if znak == "z":
            tab[l1] = str(l2)
        else:
            print(int(eval(tab[l1] + znak + tab[l2])))
    return

main()