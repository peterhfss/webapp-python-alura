from flask import Flask, render_template

app = Flask(__name__)

#criando classe Game
class Game:
    def __init__(self, name, category, console):
        self.name =name
        self.category =category
        self.console = console

@app.route('/')
def listar():
    #criando objeto de Game para adicionar na lista para serem exibidos
    game1 = Game('Diablo 4', 'RPG', 'PlayStation 4')
    game2 = Game('Resident Evil 2', 'Horror', 'PlayStation 4')
    game3 = Game('Halo Infinity', 'Action', 'XBOX S')
    game4 = Game('Fall Guys', 'Adventure', 'PC')
    lista= [ game1, game2, game3, game4 ]
    
    ''' utlizando o render_template para buscar e carregar o arquivo HTML, passando
    os parâmetros da página a ser exibida '''
    return render_template('list-games.html', titulo='Games', games=lista)

app.run()    