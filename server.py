import bottle

from checkout import Checkout


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


bottle.run(app, host='localhost', port=8000, debug=True, reloader=True)
