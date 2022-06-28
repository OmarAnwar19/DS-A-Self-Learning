def ex1(arr):
    arr.append(1980)
    arr[3] -= 200

    answers = [
        {f"february vs january: ${arr[1] - arr[0]}"},
        {f"first quarter expense: ${arr[0] + arr[1] + arr[2]}"},
        {f"$2000 in array?: {2000 in arr}"},
        {f"$1980 added: {arr}"},
        {f"April correction: {arr[3]}"},
    ]

    return answers


def ex2(heros):
    heros.insert(2, "black panther")
    heros.pop(1)
    heros.pop(2)
    heros.append("doctor strange")
    heros.sort()

    answers = [
        {f"length: {len(heros)}"},
        {f"black panther added: {heros}"},
        {f"thor and hulk removed: {heros}"},
        {f"array sorted: {heros}"},
    ]

    return answers


def ex3(max_num):
    arr = []

    for i in range(max_num):
        # if i divided by two is a whole number, add it to the array
        if i % 2 == 1:
            arr.append(i)

    return arr


if __name__ == "__main__":
    arr_ex1 = [2200, 2350, 2600, 2130, 2190]
    heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
    max_num = int(input("Max number: "))

    ex1_answers = ex1(arr_ex1)
    ex2_answers = ex2(heros)
    ex3_answers = ex3(max_num)

    print(ex1_answers)
    print(ex2_answers)
    print(ex3_answers)
