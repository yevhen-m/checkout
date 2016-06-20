import sys

import bottle

from checkout import Checkout


DEFAULT_PORT = 8000

try:
    script_name, port_str = sys.argv
    port = int(port_str)
except (ValueError, TypeError):
    port = DEFAULT_PORT

app = bottle.Bottle()
app.checkout = Checkout()


@app.route('/')
@bottle.view('index.html')
def index_get():
    return {'total': app.checkout.total}


@app.route('/', method='POST')
def index_post():
    if bottle.request.POST.get('action') == 'Clear':
        app.checkout.clear()
        bottle.redirect('/')
        return
    item = bottle.request.POST.get('item')
    app.checkout.calculate(item)
    bottle.redirect('/')


bottle.run(app, host='localhost', port=port, debug=True, reloader=True)
