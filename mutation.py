def mutation_generator(gen):
    """
    mutation generator
    """
    from random import randint
    a1 = randint(0,3)
    if(a1 == 0):
        a2 = 'A'
    elif(a1 == 1):
        a2 = 'T'
    elif(a1 == 2):
        a2 = 'G'
    elif(a1 == 3):
        a2 = 'C'
    l = randint(0,(len(gen)-1))
    w1 = list(gen)
    w1[l] = a2
    gen = ''.join(w1)
    return gen

def math(new):
    """
    random probability of mutation
    """
    from random import randint
    s = randint(0,99)
    back = False
    if(s <= new):
        back = True
    return back

def generator_genome(length):
    return 'A' * length

def main():
    mutation1 = int(input("Probability of random mutations (0-99)\n:"))
    length = int(input("Length of genome (int)\n:"))
    time = int(input("Generations (int)\n:"))
    genome = generator_genome(length)
    for x in range(time):
        if(math(mutation1)):
            genome = mutation_generator(genome)
            print(f"generation {x}")
            print(genome)

if(__name__ == "__main__"):
    main()