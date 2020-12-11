# DEBUG =  False
# DATABASES = 
# ALLOWED_HOSTS =


# AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = S3_URL

# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# DATABASES = {
#     'default': {
#         'ENGINE'   : 'django.db.backends.postgresql',
#         'NAME'     : "project", #postgresqlで作成したデータベース名(この場合だとCREATE DATABASE project ;)
#         'USER'     : "*****",
#         "PASSWORD" : "*****",
#         "HOST"     : "localhost",
#         "PORT"     : "5432",
#     }
# }

# ALLOWED_HOSTS = ['*.*.*.*'] #サーバーのIPを入力
# STATIC_URL = '/static/'
# STATIC_ROOT = '/usr/share/nginx/html/static' 
# #↑ css,オブジェクトに紐付けられない画像,javascriptなどを配信するルートディレクトリ
# MEDIA_URL = '/media/'
# MEDIA_ROOT = '/usr/share/nginx/html/media'　
# #↑ オブジェクトに紐付けられる画像を配信するルートディレクトリ
# STATICFILES_DIR = [os.path.join(BASE_DIR, 'static')]