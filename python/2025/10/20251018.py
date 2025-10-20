# Missing Socks

# Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:

#     Every 2 wash cycles, you lose a single sock.
#     Every 3 wash cycles, you find a single missing sock.
#     Every 5 wash cycles, a single sock is worn out and must be thrown away.
#     Every 10 wash cycles, you buy a pair of socks.
#     You can never have less than zero total socks.
#     Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
#     Return the number of complete pairs of socks.

# Tests

# 1. sock_pairs(2, 5) should return 1.
# 2. sock_pairs(1, 2) should return 0.
# 3. sock_pairs(5, 11) should return 4.
# 4. sock_pairs(6, 25) should return 3.
# 5. sock_pairs(1, 8) should return 0.

def sock_pairs(pairs, cycles):
    socks = pairs * 2

    if cycles >= 2:
        socks -= cycles // 2

    if cycles >= 3:
        socks += cycles // 3

    if cycles >= 5:
        socks -= cycles // 5

    if cycles >= 10:
        socks += (cycles // 10) * 2

    if socks < 0:
        socks = 0

    pairs = socks // 2
    return pairs

sock_pairs(2, 5)
sock_pairs(1, 2)
sock_pairs(5, 11)
sock_pairs(6, 25)    
sock_pairs(1, 8)

# Comments - while there is probably a more elegant approach, I'm happy just going through the steps one by one