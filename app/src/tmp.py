# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG

import sys
sys.path.append('util')
from LogUtil import LogUtil

logger = getLogger("same_hierarchy")
log_conf = LogUtil.get_log_conf('../env/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

def call_log():
  logger.info("tmp")