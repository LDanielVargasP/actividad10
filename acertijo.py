def acertijo():
    for a in range(1,3,1):
        for b in range(1,10,1):
            for c in range(1,10,1):
                for d in range(1,10,1):
                    if (a + c == d) and (a * b == c) and (c - b == b) and (a * 4 == d):
                        print('a -> ' + str(a))
                        print('b -> ' + str(b))
                        print('c -> ' + str(c))
                        print('d -> ' + str(d))

if __name__=='__main__':
    acertijo()