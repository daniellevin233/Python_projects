dividend = 23053
divisor = 4123

def divide(dividend, divisor):
    original_divisor = divisor
    counter = 0
    ans = 0
    if dividend - divisor >= 0:
        counter = 1
    else:
        return ans
    while (dividend - divisor >= 0):
        counter *= 2
        divisor *= 2
    divisor /= 2
    counter /= 2
    ans += counter
    remainder = dividend - divisor
    if remainder - original_divisor >= 0:
        ans += divide(remainder, original_divisor)
    return ans

print(divide(dividend, divisor))