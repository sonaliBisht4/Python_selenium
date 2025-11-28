import logging
logging.basicConfig( filename='demo.log', filemode='a', level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S' )



class demoLogging1:
    def add_number(self,a,b):
        return a+b

    def multiply_number(self,a,b):
        return a*b
dl = demoLogging1()
sum_result = dl.add_number(3,5)
logging.info("info: addition of no is {}".format(sum_result))
logging.debug("debug : addition of no is {}".format(sum_result))
logging.warning("warning : addition of no is {}".format(sum_result))
logging.error("error : addition of no is {}".format(sum_result))
logging.critical("critical : addition of no is {}".format(sum_result))


mul_result = dl.multiply_number(3,5)
logging.info("info: addition of no is {}".format(mul_result))
logging.debug("debug : addition of no is {}".format(mul_result))
logging.warning("warning : addition of no is {}".format(mul_result))
logging.error("error : addition of no is {}".format(mul_result))
logging.critical("critical : addition of no is {}".format(mul_result))