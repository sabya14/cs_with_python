"""
Classic problem of towers of hanoi.
"""


def solve(n, current, buffer, final):
    # No elements, returns state as it is
    if n == 1:
        print(f"Moving {n} from {current} to {final}")
    else:
        # First move n - 1 to the buffer using final as the buffer stack
        solve(n - 1, current, final, buffer)
        # Move n th element from the current stack to the final stack
        print(f"Moving {n} from {current} to {final}")
        # Move the n-1 elements in the buffer stack to the final stack using the empty current stack as the buffer stack
        solve(n - 1, buffer, current, final)


if __name__ == "__main__":
    solve(4, "A", "B", "C")
