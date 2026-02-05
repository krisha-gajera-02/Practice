# math library

import math

def math_demo():

    print("1. Math Constants")
    print("PI:", math.pi)
    print("E:", math.e)
    print("TAU:", math.tau)
    print("Infinity:", math.inf)
    print("NaN:", math.nan)

    print("\n2. Power & Roots")
    print("2^3:", math.pow(2, 3))
    print("Square root of 25:", math.sqrt(25))
    print("Cube root of 27:", math.cbrt(27))

    print("\n3. Rounding")
    print("Ceil:", math.ceil(4.2))
    print("Floor:", math.floor(4.8))
    print("Trunc:", math.trunc(4.9))

    print("\n4. Trigonometry")
    angle = math.radians(30)
    print("sin(30°):", math.sin(angle))
    print("cos(30°):", math.cos(angle))
    print("tan(30°):", math.tan(angle))

    print("\n5. Factorial & Combinations")
    print("5!:", math.factorial(5))
    print("Combinations (5C2):", math.comb(5, 2))
    print("Permutations (5P2):", math.perm(5, 2))

    print("\n6. GCD & LCM")
    print("GCD of 12 & 18:", math.gcd(12, 18))
    print("LCM of 12 & 18:", math.lcm(12, 18))


if __name__ == "__main__":
    math_demo()
