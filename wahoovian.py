import numpy as np
import logging  # See https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

import greeter_lib  # Our local library with greeter()

def wahoovian(arr):
    logging.info("entering the wahoovian function")
    num_rows, num_columns = arr.shape
    if (num_rows != num_columns):
        logging.warning("Warning: matrix is not square")
        return arr
    if (num_rows == 0):
        return arr
    new_arr = np.transpose(arr)
    new_arr = np.negative(new_arr)
    return new_arr