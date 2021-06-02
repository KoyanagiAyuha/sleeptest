
import logging
import time

if __name__ == "__main__":
    try:
        logging.critical('set_environ_name')
        for i in range(1800):
            logging.critical(i)
            time.sleep(1)
        exit(0)

    except Exception as e:
        logging.error('---except exception---')
        logging.error(e)
        exit(1)