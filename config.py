import os

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    pass
class ProdConfig(Config):
    '''
    Production configuration 

    Args:
    Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args: 
    Config The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}    
