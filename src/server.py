import sys
import os
sys.dont_write_bytecode = True
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import src.infrastructure.router as flask



if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    flask.app.run(host=host, port=port, debug=True)