import sys

def ListInt(list):
    new_list =[]
    for i in list:
        new_list.append(int(i))
    return new_list

def ListStr(list):
    new_list = []
    for i in list:
        new_list.append(str(i))
    return new_list

def ListAddNewLine(list):
    new_list =[]
    for i in list:
        new_list.append(i + "\n")
    return new_list

def FindPrimeNum(n, list=[]):
    prime_num_list = list
    prime_min = max(prime_num_list)
    for i in range(prime_min+1,n):
        prime = True
        for p in prime_num_list:
            if i < p**2:
                break
            if i % int(p) == 0:
                prime = False
                break
        if prime:
            prime_num_list.append(i)
    return ListStr(prime_num_list)

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print("We need at least one arg.")
    elif len(args) <= 3:
        n = int(args[1])
        if len(args) == 2:
            prime_num_list =[]
        if len(args) == 3:
            f = open(args[2])
            prime_num_list = f.read().split()
        prime_num_list = ListInt(prime_num_list)
        prime_num_list = FindPrimeNum(n, prime_num_list)
        prime_num_list = ListAddNewLine(ListStr(prime_num_list))
        f = open('PrimeNumber.txt', 'w')
        f.writelines(prime_num_list)
    else:
        print("There is too many args.")