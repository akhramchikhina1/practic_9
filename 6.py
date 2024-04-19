for A in range(0,10):
    for B in range(0,10):
        AB = A * 10 + B
        result = AB * 11
        if result // 100 == A and result % 10 == B:
            print(f"{AB} * {AB} = {result}")
