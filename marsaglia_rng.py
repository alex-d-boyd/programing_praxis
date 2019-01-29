#! /usr/bin/env python3

# Marsaglia’s Mental RNG
# https://programmingpraxis.com/2019/01/29/marsaglias-mental-rng

def marsaglia_generator(seed):
    """Generate a pseudorandom sequence based on Marsaglia’s Mental RNG"""
    
    if seed < 10 or seed > 99:
        raise ValueError('Seed value must be two digits.')
    if seed == 59:
        raise ValueError('Seed value 59 will cause an infinite loop.')
    
    def next_seed(seed):
        return seed // 10 + seed % 10 * 6
    while seed > 58:
        seed = next_seed(seed)
    new_seed = seed
    while True:
        yield new_seed % 10
        new_seed = next_seed(new_seed)
        # chain is exhausted when original number comes round again
        if new_seed == seed:
            break

def marsaglia_chain(seed):
    """Get the full Marsaglia’s Mental RNG sequence for a given seed value.

    seed -- the seed value (should be two digits)

    Returns a list.
    Will always contain 58 values.
    """
    generator = marsaglia_generator(seed)
    return [v for v in generator]

def marsaglia_rand(seed, n):
    """Return a Marsaglia Mental RNG number based on seed and of n digits"""
    generator = marsaglia_generator(seed)
    digits = [next(generator) for _ in range(n)]
    return int(''.join(str(d) for d in digits))
