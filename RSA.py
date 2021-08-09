#Helper Functions
def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod

def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]

def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b

#RSA Implementations
#1st Question
def Encrypt(message, modulo, exponent):
  # Fix this implementation
  messageInt = ConvertToInt(message)
  ciphertext = PowMod(messageInt, exponent, modulo)
  return ciphertext

p = 1000000007
q = 1000000009
exponent = 23917
modulo = p * q

Encrypt("attack", modulo, exponent)

#2nd Question
def Decrypt(ciphertext, p, q, exponent):
  n = (p-1) * (q-1)
  #ed congruent 1 mod n
  d = InvertModulo(exponent ,n)
  modulo = p * q
  dmsg = PowMod(ciphertext, d, modulo)
  return ConvertToStr(dmsg)

a = 3
b = 7
c = InvertModulo(a, b)
print(c)

p = 1000000007
q = 1000000009
exponent = 23917
modulo = p * q
ciphertext = Encrypt("attack", modulo, exponent)
message = Decrypt(ciphertext, p, q, exponent)
print(message)

#RSA Attacks
#3rd Question
def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
  # Fix this implementation
  if ciphertext == Encrypt(potential_messages[0], modulo, exponent):
    return potential_messages[0]
  if ciphertext == Encrypt(potential_messages[1], modulo, exponent):
    return potential_messages[1]
  if ciphertext == Encrypt(potential_messages[2], modulo, exponent):
    return potential_messages[2]
  
  return "don't know"

modulo = 101
exponent = 12
ciphertext = Encrypt("wait", modulo, exponent)
print(ciphertext)
print(DecipherSimple(ciphertext, modulo, exponent, ["attack", "don't attack", "wait"]))

#4th Question
def DecipherSmallPrime(ciphertext, modulo, exponent):
  for num in range(2,1000000):
    for i in range(2, num):
      if(num % i) == 0:
        break
      else:
        if modulo % num == 0:
          small_prime = num
          big_prime = modulo // num
          return Decrypt(ciphertext, small_prime, big_prime, exponent)

  return "don't know"
  
modulo = 101 * 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
exponent = 239
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
print(DecipherSmallPrime(ciphertext, modulo, exponent))

#5th Question
#Try all integers between √𝑛 − 𝑟 and √𝑛 as divisors of 𝑛

def DecipherSmallDiff(ciphertext, modulo, exponent):
  for num in range(IntSqrt(modulo)-5000, IntSqrt(modulo)+1):
    if modulo % num == 0:
      small_prime = num
      big_prime = modulo // num
      return Decrypt(ciphertext, small_prime, big_prime, exponent)

  return "don't know"
  
p = 1000000007
q = 1000000009
n = p * q
e = 239
ciphertext = Encrypt("attack", n, e)
message = DecipherSmallDiff(ciphertext, n, e)
print(ciphertext)
print(message)

#6th Question
def GCD(a, b):
  if b == 0:
    return a
  return GCD(b, a % b)
  
def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent):
  # Fix this implementation to correctly decipher both messages in case
  # first_modulo and second_modulo share a prime factor, and return
  # a pair (first_message, second_message). The implementation below won't work
  # if the common_prime is bigger than 1000000.
  #GCD(𝑛1, 𝑛2) = common_prime
  common_prime = GCD(first_modulo, second_modulo)
  if common_prime != 1:
    q1 = first_modulo // common_prime
    q2 = second_modulo // common_prime
    return (Decrypt(first_ciphertext, common_prime, q1, first_exponent), Decrypt(second_ciphertext, common_prime, q2, second_exponent))
  else:
    return ("unknown message 1", "unknown message 2")
  
# Example usage with common prime p and different second primes q1 and q2  
p = 101
q1 = 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
q2 = 1000000007
first_modulo = p * q1
second_modulo = p * q2
first_exponent = 239
second_exponent = 17
first_ciphertext = Encrypt("attack", first_modulo, first_exponent)
second_ciphertext = Encrypt("wait", second_modulo, second_exponent)
print(DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent))

#7th Question
def ChineseRemainderTheorem(n1, r1, n2, r2):
  (x, y) = ExtendedEuclid(n1, n2)
  return ((r2 * x * n1 + r1 * y * n2) % (n1 * n2) + (n1 * n2)) % (n1 * n2)

def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
  # Fix this implementation
  r = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
  return ConvertToStr(IntSqrt(r))
  
p1 = 790383132652258876190399065097
q1 = 662503581792812531719955475509
p2 = 656917682542437675078478868539
q2 = 1263581691331332127259083713503
n1 = p1 * q1
n2 = p2 * q2
ciphertext1 = Encrypt("attack", n1, 2)
ciphertext2 = Encrypt("attack", n2, 2)
message = DecipherHastad(ciphertext1, n1, ciphertext2, n2)
print(message)
