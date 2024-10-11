from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

cards = [input().rstrip() for _ in range(n)]
candidates = list(permutations(cards, k))
results = set()

for candidate in candidates:
  results.add(''.join(candidate))

print(len(results))