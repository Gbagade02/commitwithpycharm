import logging

'''logging.DEBUG = 10
logging.INFO = 20
logging.WARNING = 30 
logging.ERROR = 40
logging.CRITICAL = 50
'''


logging.basicConfig(filename="test5.log", level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s ')

try:
    logging.info("I am trying to read a file")
    with open("gaurav.txt", 'r'):
        logging.info("we have read the file")
except Exception as e:
    logging.critical("This is the situation for us")
    logging.error(e)
    logging.exception(e)

