def designer_door_mat(N, M):
    """
    This function creates a doormat design of size NxM using characters ., |, and -.

    Args:
      N: The height of the doormat, which must be an odd natural number.
      M: The width of the doormat, which must be three times N.

    Returns:
      A string containing the doormat design.
    """

    # Check if N and M meet the constraints
    if N % 2 == 0 or N < 5 or N > 101 or M < 15 or M > 303:
        return "Invalid input. N must be an odd natural number between 5 and 101, and M must be three times N and between 15 and 303."

    result = []  # Initialize an empty list to store the lines of the design

    # Create the top half of the design
    for i in range(1, N // 2 + 1):
        # Create the pattern for the current line
        pattern = ".|." * (2 * i - 1)
        # Center the pattern within the width M and pad with '-' characters
        line = pattern.center(M, '-')
        # Append the line to the result list
        result.append(line)

    # Add the welcome message centered within the width M to the result list
    welcome_line = "WELCOME".center(M, '-')
    result.append(welcome_line)

    # Create the bottom half of the design (reversed)
    for i in range(N // 2, 0, -1):
        # Create the pattern for the current line
        pattern = ".|." * (2 * i - 1)
        # Center the pattern within the width M and pad with '-' characters
        line = pattern.center(M, '-')
        # Append the line to the result list
        result.append(line)

    # Join the lines in the result list into a single string separated by newline characters
    return '\n'.join(result)

# Get the input from the user
N, M = map(int, input().split())

# Create and print the doormat design
print(designer_door_mat(N, M))
