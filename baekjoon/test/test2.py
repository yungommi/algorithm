from itertools import combinations_with_replacement as cwr
from collections import Counter

for new in cwr(range(11), 5):
  print(new[::-1])
  counter = Counter(new)
  print(counter)
  