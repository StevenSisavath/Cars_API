# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g-ak-l&c+02=a_@8kb$-9m^@@2z&*_*_0n9(hs^twjlr8^2^t!'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}