bricks_arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

def trapped_water(barr):
    # print(barr)
    # print("\n\n")

    # get the highest block
    max = 0
    for i in barr:
        if i > max:
            max = i

    sum = 0

    # layers
    for layer in range(1, max+1):
        # take only one layers of bricks
        layer_arr = []
        for i in barr:
            if i < layer:
                layer_arr.append(0)
            else:
                layer_arr.append(1)

        # print(layer_arr)

        # count holes
        left = right = -1
        for i in layer_arr:
            if i == 1 :
                left = right
                right = i
                if left != -1 & right != -1 & right - left != 1:
                    sum = sum + right - left
        # print(sum)

    # print("\n\n")
    return sum

################ MAIN
if __name__ == '__main__':
    print(trapped_water(bricks_arr))
