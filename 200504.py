d = -5
c = bool(d)
print(c)


def accumulator():
    total = 0
    while True:
        print("total", total)

        value = yield total
        print('Got: {}'.format(value))

        if value:
            total += value


generator = accumulator()

print(next(generator))
print(next(generator))

print('Accumulated: {}'.format(generator.send(1)))

print('Accumulated: {}'.format(generator.send(10)))

print(next(generator))
print(next(generator))

print('Accumulated: {}'.format(generator.send(100)))

print(next(generator))
print(next(generator))
