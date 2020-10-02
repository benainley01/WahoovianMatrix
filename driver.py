import numpy as np
import logging  # See https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

import greeter_lib  # Our local library with greeter()
from wahoovian import wahoovian

def main():
    logging.basicConfig(filename='demo-log.txt', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')
                        
    logging.info('Program begins!')

    greeter_lib.greeter("Our program begins!")

    m1 = np.array([[2, 4], [5, -6]])
    m2 = np.array([[2, 4, 9], [5, -6, 7]])

    result1 = wahoovian(m1)
    result2 = wahoovian(m2)

    print(result1)
    print(result2)

    logging.info('Program ends')
    greeter_lib.greeter("Program ending")

if __name__ == '__main__':
    main()