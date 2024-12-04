def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Recursive solution to the Tower of Hanoi problem.
    
    Args:
    n (int): Number of discs.
    source (str): The starting pole.
    destination (str): The target pole.
    auxiliary (str): The auxiliary pole.

    Returns:
    None
    """
    if n == 1:
        # Base case: Only one disc to move
        print(f"Move disc 1 from {source} to {destination}")
        return
    
    # Step 1: Move top (n-1) discs from source to auxiliary pole
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Step 2: Move the nth (largest) disc from source to destination
    print(f"Move disc {n} from {source} to {destination}")
    
    # Step 3: Move the (n-1) discs from auxiliary pole to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# Example usage
n_discs = 4  # You can change this to any number of discs
tower_of_hanoi(n_discs, 'A', 'C', 'B')