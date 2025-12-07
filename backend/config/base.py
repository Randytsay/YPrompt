# -*- coding: utf-8 -*-

class BaseConfig(object):
    """配置基類"""

    DEBUG = True

    # JWT 密鑰
    SECRET_KEY = 'intramirror'
    
    # Linux.do OAuth配置
    LINUX_DO_CLIENT_ID = ''
    LINUX_DO_CLIENT_SECRET = ''
    LINUX_DO_REDIRECT_URI = ''
    
    # ==========================================
    # 数据库配置
    # ==========================================
    # 数据库类型: 'sqlite' 或 'mysql'
    DB_TYPE = 'sqlite'
    
    # SQLite 配置
    SQLITE_DB_PATH = '../data/yprompt.db'
    
    # MySQL 配置（當 DB_TYPE='mysql' 時使用）
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASS = ''
    DB_NAME = 'yprompt'
    DB_PORT = 3306
    
    # ==========================================
    # 預設管理員帳號配置（僅首次初始化時使用）
    # ==========================================
    DEFAULT_ADMIN_USERNAME = 'admin'
    DEFAULT_ADMIN_PASSWORD = 'admin123'
    DEFAULT_ADMIN_NAME = '管理員'

    ACCESS_LOG = False

    # 服務 worker 數量
    WORKERS = 1

    # 跨域相關
    # 是否啟動跨域功能
    ENABLE_CORS = False
    CORS_SUPPORTS_CREDENTIALS = True

    # redis 配置
    REDIS_CON = "redis://127.0.0.1:6379/2"

    # 日誌配置，相容 sanic 內建 log 庫
    LOGGING_INFO_FILE = '../data/logs/backend/info.log'
    LOGGING_ERROR_FILE = '../data/logs/backend/error.log'
    BASE_LOGGING = {
        'version': 1,
        'loggers': {
            "sanic.root": {"level": "INFO", "handlers": ["console", 'info_file', 'error_file']},
        },
        'formatters': {
            'default': {
                'format': '%(asctime)s | %(levelname)s | %(message)s',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'default',
            },
            'info_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': LOGGING_INFO_FILE,
                'maxBytes': (1 * 1024 * 1024),
                'backupCount': 10,
                'encoding': 'utf8',
                'level': 'INFO',
                'formatter': 'default',
            },
            'error_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': LOGGING_ERROR_FILE,
                'maxBytes': (1 * 1024 * 1024),
                'backupCount': 10,
                'encoding': 'utf8',
                'level': 'ERROR',
                'formatter': 'default',
            },
        },
    }

    # 告警源和派生表映射关系
    S2T = {
        "apm": "apm",
        "rum": "rum",
        "ckafka": "mid",
        "mongodb": "mid",
        "redis": "mid",
        "cdb": "mid",
        "es": "mid",
        "cvm": "iaas",
        "ecs": "iaas",
        "cos": "iaas",
        "cls": "iaas",
        "sls": "iaas",
        "custom": "custom"
    }

    # 沒有對應的分派策略的預設 owner
    OWNER_DEFAULT = [{
        'workforceType': 4,
        'watchkeeperId': 833,
        'watchkeeperName': '朱威',
        'dingDingId': 4311207311543872874
    }]
    ARGS_DEFAULT = {
    'status': 0,
    'dingtalk_person': 0,
    'sms': 0,
    'dingtalk_group': 0
    }


    def __init__(self):
        if self.LOGGING_INFO_FILE:
            self.BASE_LOGGING['handlers']['info_file']['filename'] = self.LOGGING_INFO_FILE

        if self.LOGGING_ERROR_FILE:
            self.BASE_LOGGING['handlers']['error_file']['filename'] = self.LOGGING_ERROR_FILE
