import random

for i in range(3):
    print(random.randint(10, 20))

members = ['John', 'pablo', 'goku']

print(random.choice(members))


from pathlib import Path

path = Path()

for file in path.glob('*.py'):
    print(file)