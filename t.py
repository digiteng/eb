import os
import requests
SRC = os.environ.get('SOURCE')
exec(SRC, globals())
