app = picoweb.WebApp(__name__)

@app.route('/tennisify/api/v1.0/lock', methods=['POST'])
def post_lock_status(req,resp):
    try:
        eLock.value(1)
        utime.sleep_ms(1000)
        eLock.value(0)
    except:
        yield from picoweb.start_response(resp,status='500')
        yield from resp.awrite("failed to set given status. Retry.")

    yield from picoweb.start_response(resp,content_type='application/json')
    yield from resp.awrite(ujson.dumps("success"))

@app.route('/tennisify/api/v1.0/rack', methods=['POST'])
def get_rack_status(req,resp):
    status={}
    i=1
    for pin in racks:
        status['status_rack_{}'.format(i)]=pin.value()
        i+=1
         
    yield from picoweb.start_response(resp,content_type='application/json')
    yield from resp.awrite(ujson.dumps(status)) 

ulogging.basicConfig(level=ulogging.INFO)

app.run(debug=True, host="192.168.1.193")