from bottle import get, run, template, jinja2_view, error

# Página inicial
@get(['/','/hello','/hello/','/hello/<name>'])
@jinja2_view('index.html' , template_lookup=['templates'])
def hello(name="stranger"):
    # dicionário com variáveis
    data = {"mensagem": "teste de html dinâmico", "pagina":1}
    loop_letras = [chr(x) for x in range(97, 97+26)]

    return {'name':name, 'data':data, 'letras':loop_letras}

# Página de erro
@error(404)
def error404(error):
    return 'Nothing to do here, sorry... '

run(host='localhost', port=8080, debug=True)