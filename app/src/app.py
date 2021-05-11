# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
from util.LogUtil import LogUtil

logger = getLogger(__name__)
config.dictConfig(LogUtil.get_log_conf('/opt/app/env/log_config.json'))
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


if __name__ == '__main__':
  logger.debug('hello')
