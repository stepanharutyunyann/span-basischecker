
def input_getter():
    print("For stopping the program input 'f'.")
    vecs = []
    dim1 = 0
    while True:
        user_inp = input("Enter the dimension: ")
        if user_inp == "f":
            print("Goodbye!")
            exit()
        try:
            dim = int(user_inp)
            if dim < 0:
                print("The dimension has to be an integer which is bigger than 0!\n")
                continue
            break
        except ValueError:
            print("The dimension has to be a whole and positive number!\n")
        print(f"Great! Your dimension is: {dim}\n")
        dim1 = dim

    while True:
        user_input = input(
            f"Enter {dim1} vectors, each with {dim1} components, separated by commas\n(e.g., 1 2 3, 4 5 6): ")
        if user_input == "f":
            print("Goodbye!")
            exit()
        elements = user_input.split(",")

        if len(elements) < dim1:
            print(f"Error: expected {dim1} vectors, got {len(elements)}.")
            continue

        valid = True
        vecs = []

        for v in elements:
            vec1 = []
            for i in v.split():
                vec1.append(float(i))

            if len(vec1) != dim:
                print(f"Error: each vector must have {dim} components. Got {len(vec1)}.")
                valid = False
                break

            vecs.append(vec1)

        if valid:
            break

    print("\n--- Success! ---")
    print(f"Your vectors are: {vecs}")
    return dim1, vecs