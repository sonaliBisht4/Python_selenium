import logging

class Loggerdemo:
    def sample_logger(self):
        logger = logging.getLogger('demologger')
        logger.setLevel(logging.DEBUG)

        # Avoid duplicate logs
        if not logger.handlers:
            ch = logging.StreamHandler()
            fh = logging.FileHandler('demologging.log')
            formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            formatter2 = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')

            ch.setFormatter(formatter1)
            fh.setFormatter(formatter2)
            logger.addHandler(ch)
            logger.addHandler(fh)

        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')


# ---- Call the logger properly ----
if __name__ == "__main__":
    ld = Loggerdemo()
    ld.sample_logger()
