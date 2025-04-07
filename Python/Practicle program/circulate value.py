def circulate_values():
    n = int(input("Enter the number of variables: "))
    variables = []
    for i in range(n):
        variables.append(input(f"Enter value for variable {i+1}: "))

    print("Before circulation:")
    print("Variables:", variables)

    temp = variables[0]
    for i in range(n-1):
        variables[i] = variables[i+1]
    variables[n-1] = temp

    print("After circulation:")
    print("Variables:", variables)

circulate_values()