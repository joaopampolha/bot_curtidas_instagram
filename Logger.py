import logging
import datetime as dt

class Logger():

    __logger = None
    __handler = None
    __formatter = None

    def __init__(self):
        self.__logger = logging.getLogger('BotCurtidasInstagram')
        self.__handler = logging.FileHandler('Log_' + dt.datetime.strftime(dt.datetime.now(), '%Y%m%d_%H%M%S') + '.log')
        self.__formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.__handler.setFormatter(self.__formatter)
        self.__logger.addHandler(self.__handler) 
        self.__logger.setLevel(logging.INFO)
        self.log("Iniciando ...")

    def log(self, msg):
        self.__logger.info(msg)
        print(msg)