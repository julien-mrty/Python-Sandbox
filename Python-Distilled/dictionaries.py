from collections import Counter

portfolio = [
    ('ACME', 50, 92.34),
    ('IBM', 75, 102.25),
    ('PHP', 40, 74.50),
    ('IBM', 50, 124.75)
]

total_shares = { s[0]: 0 for s in portfolio }
print(total_shares)

for s in portfolio:
    total_shares[s[0]] += s[1]

print(total_shares)

dict = {
    "key1": 1,
    "key2": 2
}

print(dict.get("key1"))

total_shares2 = Counter()

print(total_shares2)

with open("exemple.txt") as file:
    print(type(file))