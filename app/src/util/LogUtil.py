# -*- coding: utf-8 -*-
import json

class LogUtil:
  
  def __init__(self):
    pass

  @classmethod
  def get_log_conf(cls, log_conf_path):
    """ ログ設定ファイルを読み込む
    """
    log_conf = json.load(log_conf_path)
    return log_conf

