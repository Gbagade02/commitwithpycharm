import logging
logging.basicConfig(filename="test.log",level= logging.INFO)
logging.info("This is my very first log")
logging.warning("This will load all warning msg")
l = [i for i in range(8)]
for i in l:
    if i == 2:
        logging.info(l)
        logging.error("This is the error msg if user won't found anything in list")

logging.shutdown()