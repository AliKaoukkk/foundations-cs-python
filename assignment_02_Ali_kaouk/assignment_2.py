tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)

combined = zip(tuple1, tuple2, tuple3)
result = tuple(map(sum, combined))
print(result) 