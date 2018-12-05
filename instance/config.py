class Config:
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}