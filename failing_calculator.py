def average_ratios(numbers):
    total = 0.0
    count = 0
    for n in numbers:
        if n == 0:
            # Sıfırları atla; sıfıra bölme hatasını önle
            continue
        total += 100.0 / n
        count += 1
    if count == 0:
        raise ValueError("average_ratios: all input values are zero; cannot compute average.")
    return total / count

print(average_ratios([10, 5, 0]))
