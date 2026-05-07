import os
import requests
SRC = os.environ.get('SOURCE')
exec(str(SRC), globals())
