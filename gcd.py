# GCD: Greatest common divisor
# gcd(m,n): largest k such that k divide m & n
# gcd(8,12) = 4
# gcd(18,25) = 1
# 1 divides every number
#----------------------
# Computing gcd(m,n)
# List out factors of m & n
# Report the largest number that appears on both lists
############ Euclid's algorithm ##############
# Consider gcd(m,n) with m>n
# if n divides m, return n
# Otherwise, let r = m%n
# Return gcd(n,r) ; where n>r

def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
        while (m%n) != 0:
            (m,n) = (n, m%n) # m%n < n , always
        return (n)
# End
