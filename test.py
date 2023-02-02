def yield_infinite_abc():
  while True:
    yield "A"
    yield "B"
    yield "C"


gen = yield_infinite_abc()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(gen)