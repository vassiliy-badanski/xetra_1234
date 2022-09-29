"""Running the Xetra ETL application"""
from distutils.command.config import config
import logging
import logging.config

import yaml

def main():
    """
    entry point to run xetral ETL job
    """
    # Parsing YAML file
    config_path = r'C:\Users\vassiliy.badanski\Desktop\python\xetra_project\xetra_1234\configs\xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")



if __name__ == '__main__':
    main()