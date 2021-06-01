# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG

import sys
sys.path.append('util')
from LogUtil import LogUtil
import tmp

logger = getLogger("same_hierarchy")
log_conf = LogUtil.get_log_conf('../env/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':
  logger.info('hello')
  tmp.call_log()