import inspect
import logging
class CustLogger():
    def custlogger(self, loglevel = logging.DEBUG):
        logger_name = inspect.stack()[0][1]
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)


        fh = logging.FileHandler('automation.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
