def zeef(n):
    cijfers = [i for i in range(2, n + 1)]
    priemgetallen = []

    while cijfers:
        m = min(cijfers)

        if m**2 > n:
            priemgetallen.extend(cijfers)
            break

        priemgetallen.append(m)
        cijfers.remove(m)

        for i in range(m**2, n + 1, m):
            if i in cijfers:
                cijfers.remove(i)

    return priemgetallen

print(zeef(100))