def solution(N):
    nb_factor = 0
    i = 1
    while (i * i) < N:
        if (N % i) == 0:
            nb_factor += 2
        i += 1
    if (i * i) == N:
        nb_factor += 1
    return nb_factor
