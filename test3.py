import logging

logging.basicConfig(filename="test3.log", level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s ')

def devide(a,b):
    logging.info("The Number entered by user is %s and %s", a,b)
    try:
        logging.info("we are in try block")
        div = a/b
        logging.info("we have succesfully  completed our division task.")
        logging.info("The result of code is %s", div)
        return div
    except Exception as e:
        logging.exception(e)


print(devide(44,9))