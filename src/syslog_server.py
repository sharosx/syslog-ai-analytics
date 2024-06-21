import logging
import logging.handlers

def setup_syslog_server():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.handlers.SysLogHandler(address=('localhost', 514))
    logger.addHandler(handler)

    while True:
        message = input("Enter log message: ")
        logger.info(message)

if __name__ == "__main__":
    setup_syslog_server()
