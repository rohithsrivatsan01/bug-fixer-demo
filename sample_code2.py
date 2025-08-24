def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    # BUG: dividing by fixed 10 instead of length of list
    return total / 10  

scores = [80, 90, 100, 70]
print("Average score:", calculate_average(scores))
