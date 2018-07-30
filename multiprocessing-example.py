import logging
import threading

from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions

FORMAT = '%(asctime)-15s %(name)s %(threadName)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
log = logging.getLogger()

app = FlaskAPI(__name__)

if __name__ == "__main__":
    log.info('start')
    rest_service_thread = threading.Thread(name='reset_service', target=app.run, kwargs=dict(debug=False))
    rest_service_thread.start()
    log.info('main thread is mine!')
    import time
    while True:
        print('this is main thread' + time.ctime())
        time.sleep(1)
    rest_service_thread.join()
