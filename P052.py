def getDigits(n):
    return [int(d) for d in str(n)]

def isPermutation(A, B):
    return list(sorted(A)) == list(sorted(B))

def brute_force(N):
    
    sequences = []
    OoM = 1                                 # order of magnitude
    checked = [False]
    while len(sequences) == 0:
        checked += [False] * (10**(OoM) - 10**(OoM-1))

        for n in range(10**(OoM-1), 10**(OoM)):
            if checked[n]:
                continue
            
            seq = [n]
            digits = getDigits(n)
            checked[n] = True
            
            for k in range(2, 10):
                if k*n >= 10**(OoM):
                    break
                
                if isPermutation(digits, getDigits(k*n)):
                    seq.append(k*n)
                    checked[k*n] = True
                else:
                    break

            if len(seq) >= N:
                #sequences.append(seq)
                return seq                  # if we only care about the smallest such sequence, we can just return here
        
        OoM += 1
        
    return sequences[0]

def main(N=6):
    seq = brute_force(N)
    
    print(f"The smallest positive integer, n, such that 2n, 3n, ..., {N}n contain the same digits is:", seq[0])
    return seq[0]

if __name__ == "__main__":
    main()