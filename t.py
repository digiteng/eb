import os
import requests
SRC = os.environ.get('SOURCE')
# exec(str(SRC), globals())
open("./tmp/srct.py", "w").write(f"{SRC}")
