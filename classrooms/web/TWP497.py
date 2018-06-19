import bottle

@bottle.route('/')
def home_page():
    mythings = ['Python', 'Ruby', 'Perl', 'C++']
    return bottle.template('TWP497', {'username': 'Masanori', 'things': mythings})

@bottle.post('/favorita')
def favorita():
    lang = bottle.request.forms.get('lang')
    if lang == None or lang == '':
        lang = 'Nenhuma escolhida'
    return bottle.template('TWP497_2', {'lang': lang})


bottle.debug(True)
bottle.run(host='localhost', port=8082)