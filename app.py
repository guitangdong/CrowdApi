import logging
from logging.handlers import TimedRotatingFileHandler

from app.config.cfg import cfg
from app.route import app

def setLogger():
    handler = TimedRotatingFileHandler(filename=cfg.get('log.file'), when="D", interval=1, backupCount=7)
    app.logger.level = logging.INFO
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)


setLogger()

if __name__ == '__main__':
    # app.debug=True
    app.run(host='0.0.0.0', port=cfg.getint("flask.port"))
