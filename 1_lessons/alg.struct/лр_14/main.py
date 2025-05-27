import random
from sympy import isprime
from math import gcd
import mysql.connector
import time

def generate_prime_candidate(start=100, end=300):
    while True:
        p = random.randint(start, end)
        if isprime(p):
            return p

def generate_keypair():
    p = generate_prime_candidate()
    q = generate_prime_candidate()
    while p == q:
        q = generate_prime_candidate()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    def modinv(a, m):
        for d in range(2, m):
            if (a * d) % m == 1:
                return d
        return None

    d = modinv(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678L",
    database="studentcoursemanagement"
)
cursor = conn.cursor()

public, private = generate_keypair()

cursor.execute("SELECT student_id, first_name, last_name FROM Students")
students = cursor.fetchall()

for student_id, first_name, last_name in students:
    encrypted_fn = encrypt(public, first_name)
    encrypted_ln = encrypt(public, last_name)

    enc_fn_str = ','.join(map(str, encrypted_fn))
    enc_ln_str = ','.join(map(str, encrypted_ln))

    cursor.execute("UPDATE Students SET first_name=%s, last_name=%s WHERE student_id=%s", (enc_fn_str, enc_ln_str, student_id))

conn.commit()

cursor.execute("SELECT student_id, first_name, last_name FROM Students")
students = cursor.fetchall()

for student_id, enc_fn_str, enc_ln_str in students:
    decrypted_fn = decrypt(private, list(map(int, enc_fn_str.split(','))))
    decrypted_ln = decrypt(private, list(map(int, enc_ln_str.split(','))))
    print(f"ID: {student_id}, Name: {decrypted_fn} {decrypted_ln}")

message = "RSA test"
encrypted = encrypt(public, message)
decrypted = decrypt(private, encrypted)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

for size in [8, 16, 32, 64, 128]:
    start = time.time()
    p = generate_prime_candidate(2**(size-1), 2**size)
    q = generate_prime_candidate(2**(size-1), 2**size)
    n = p * q
    end = time.time()
    print(f"{size}-bit primes: {p}, {q} -> n = {n}, generated in {end-start:.4f} sec")
