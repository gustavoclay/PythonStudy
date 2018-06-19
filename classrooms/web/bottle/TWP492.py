import bottle

@bottle.route('/')
def home_page():
    return 'Hello World'

@bottle.route('/outra')
def teste_page():
    return 'Teste Page'

bottle.debug(True)
bottle.run(host='localhost', port=8082)