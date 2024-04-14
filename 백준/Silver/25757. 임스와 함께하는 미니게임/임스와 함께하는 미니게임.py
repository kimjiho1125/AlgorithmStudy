import sys
games = {'Y':2, 'F':3, 'O':4 }
n, game = sys.stdin.readline().split()
n = int(n)
members = set()

for _ in range(n):
    members.add(sys.stdin.readline())

print(len(members)//(games[game]-1))