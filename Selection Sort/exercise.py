def selection_sort(arr, key):
    size = len(arr)

    # loop over each element in the sort_key
    # then, you run selection sort on the array with key[k]
    for k in range(len(key)):
        for i in range(size-1):
            min_i = i

            for j in range(i+1, size):
                if arr[j][key[k]] < arr[min_i][key[k]]:
                    min_i = j

            if i != min_i:
                arr[i], arr[min_i] = arr[min_i], arr[i]


if __name__ == "__main__":
    arr = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    # call the selection_sort function, passing in the order
    selection_sort(arr, ["First Name", "Last Name"])

    # print each entry from the array on a seperate line
    for i in range(len(arr)):
        print(arr[i])
