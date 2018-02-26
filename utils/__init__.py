#################################
# Support tools
#
# Version: 1.0.0
# Creator: Jeff Wang
# Date: 2017/11/08
#
import configparser
import os
import datetime
import logging
import base64

__version__="1.0.0"

##################################
# Load properties from config file, default filename is config.properties locates in script launch folder
#
class Properties:
    """ Property value is able to get from properties file, environment or dynamic value """

    __default_env__ = "default"
    def __init__(self, filename=None, environment="default"):
        self.env = environment

        file_name: str = filename
        if file_name is None:
            file_name = os.getcwd() + "/conf/config.properties"

        self.config = configparser.ConfigParser()
        self.config.readfp(open(file_name))

    def getString(self, key, default_value=None):
        """ Get string value from properties file """
        try:
            return self.config.get(self.env, key)
        except configparser.NoOptionError:
            try:
                return self.config.get(self.__default_env__, key)
            except configparser.NoOptionError as error:
                if default_value is None:
                    raise error
                return default_value

    def getBoolean(self, key, default_value=None):
        """ Get boolean value from properties file """
        try:
            return self.config.getboolean(self.env, key)
        except configparser.NoOptionError:
            try:
                return self.config.getboolean(self.__default_env__, key)
            except configparser.NoOptionError as error:
                if default_value is None:
                    raise error
                return default_value
    
    def getInt(self, key, default_value=None):
        """ Get integer value from properties file """
        try:
            return self.config.getint(self.env, key)
        except configparser.NoOptionError:
            try:
                return self.config.getint(self.__default_env__, key)
            except configparser.NoOptionError as error:
                if default_value is None:
                    raise error
                return default_value

    def getCurrentYearMonth(self):
        """ year and month information are not get from properties file """
        return YearMonth()

    def getEnv(self, name, default_value=None):
        """ Get environment variable """
        try:
            return os.environ[name]
        except KeyError as error:
            if default_value is None:
                raise error
            else:
                return default_value
    
    def getPassword(self, key):
        """ Decode base64 password"""
        enc = self.getString(key)
        return base64.b64decode(enc).decode("utf-8", "ignore").replace('\n', '')


class YearMonth:
    """YearMonth class"""
    def __init__(self):
        self.dt = datetime.datetime.now()

    def __str__(self):
        return format()

    def __eq__(self, other):
        return self.dt.__eq__(other.dt)

    def format(self, separator="-"):
        """ Format output """
        return self.dt.strftime('%Y'+separator+'%m')

class Log:
    """ Provide logging function """
    logger: logging.Logger = None

    def __init__(self, config: Properties, applicationName=""):
        self.logger = logging.getLogger(applicationName)

        formatter = logging.Formatter(config.getString("log.format", '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        log_level = config.getInt("log.level", logging.DEBUG)
        self.logger.setLevel(log_level)

        try:
            log_file_path = config.getString("log.file")
            file_handler = logging.FileHandler(log_file_path)
            log_file_level = config.getString("log.file.level", log_level)
            file_handler.setLevel(log_file_level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        except configparser.NoOptionError as error:
            print(error.message)

        if config.getBoolean("log.console", True):
            channel = logging.StreamHandler()
            log_console_level = config.getString("log.console.level", log_level)
            channel.setLevel(log_console_level)
            channel.setFormatter(formatter)
            self.logger.addHandler(channel)

    def debug(self, message:str):
        self.logger.debug(message)

    def info(self, message:str):
        self.logger.info(message)

    def warning(self, message:str):
        self.logger.warning(message)

    def error(self, message:str):
        self.logger.error(message)
