from time import time

def tic():
    """
    Return the start time
    :return: Start time.
    """
    start_time = time()

    return start_time

def toc(start_time):
    """
    Return the elapsed time
    :return: elapsed time.
    """
    elapsed_time = time() - start_time
    
    return elapsed_time


