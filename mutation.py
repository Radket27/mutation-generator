def mutation_generator(gen):
    """
    Substitution mutation generator
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

def generator_nucleotides(length):
    return 'A' * length

def main():
    mutation1 = int(input("Probability of random substitution mutations (0-99)\n: "))
    length = int(input("Length of nucleotide sequence (int)\n: "))
    time = int(input("Generations (int)\n: "))
    genome = generator_nucleotides(length)
    for x in range(time):
        if(math(mutation1)):
            genome = mutation_generator(genome)
            print(f"Generation {x}")
            print(genome)

if(__name__ == "__main__"):
    main()