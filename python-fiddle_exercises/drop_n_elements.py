def drop(n, seq):
    """
    Returns a list containing the elements of seq with the first n elements dropped.

    Args:
    n: The number of elements to drop.
    seq: The input sequence.

    Returns:
    list: The list with the first n elements dropped.
    """
    new_seq = []
    for i,char in enumerate(seq):
        if (i + 1) > n:
            new_seq.append(char)
    return new_seq