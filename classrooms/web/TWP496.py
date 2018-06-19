import bottle

@bottle.route('/')
def home_page():
    mythings = ['Python', 'Ruby', 'Perl', 'C++']
    return bottle.template('TWP496', {'username': 'Masanori', 'things': mythings})


bottle.debug(True)
bottle.run(host='localhost', port=8082)
