import sys
import logging
import threading
import time



def ExceptionCatcher(typeErr, value = None, traceback = None, thread = None):
    # sys.__excepthook__(typeErr, value, traceback)
    logging.info(f"{str(threading.currentThread()).split(',')[0][8:]}: Erreur {str(typeErr.exc_value)}")

threading.excepthook = ExceptionCatcher

def Thread1():
    logging.info("Thread 1: starting")
    import Test
    logging.info("Thread 1: finishing")

def Thread2():
    logging.info("Thread 2: starting")
    import Test2
    logging.info("Thread 2: finishing")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    Programme_1 = threading.Thread(target=Thread1, args=())
    Programme_2 = threading.Thread(target=Thread2, args=())



    Programme_1.start()

    Programme_2.start()
