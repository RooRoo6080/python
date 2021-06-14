def sieve_of_eratosthenes(n):
    list = []
    for i in range(0, n):
        for j in range(0,i):
            if i % j == 0:
                break
        list.append(i)
    return list


a = int(raw_input("Enter a number | ex: 5"))
sieve_of_eratosthenes(a)