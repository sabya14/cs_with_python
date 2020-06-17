
def minimum_swaps(arr):
    pos = {}
    result = 0

    # Keep track of positions
    for index, value in enumerate(arr):
        pos[value] = index

    for i in range(0, len(arr)):
        if arr[i] != i+1:
            # If incorrect value in a position, then swap it
            temp = arr[i]
            arr[i] = i+1
            arr[pos[i+1]] = temp
            result += 1

            # Make sure to update the position dictionary also with it
            past_position = pos[i+1]
            pos[i+1] = i
            pos[temp] = past_position
    return result

