def negrito(text):
    def envelope():
        return '<b>' + text() + '</b>'
    return envelope

def italico(text):
    def envelope():
        return '<i>' + text() + '</i>'
    return envelope

@negrito
@italico
def hello():
    return 'Hello Word'

print(hello())