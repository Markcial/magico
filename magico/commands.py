# -*- coding: utf-8 -*-
from magico.actions import say, react, get_realname
from urllib.parse import quote_plus
from py_expression_eval import Parser


_parser = Parser()


def default(message, event):
    say(event['channel'], """Hola {}
Si no sabes como funciono prueba a pedirme ayuda: magico ayuda
""".format(get_realname(event['user'])))


def ayuda(message, event):
    say(event['channel'], """Veo que me has pedido ayuda.
Prueba a pedirme que
  * te salude: magico saluda...
  * te diga donde esta algo: magico donde esta...
  * que te calcule algo: magico calcula....
  * o que te busque algo en ulabox: magico tenemos...
""")
    

def saluda(message, event):
    say(event['channel'], "Hola %s!!" % get_realname(event['user']))


def where_is(message, event):
    say(event['channel'], "https://www.google.es/maps/search/{}".format(quote_plus(message)))


def do_we_have(message, event):
    say(event['channel'], 'https://www.ulabox.com/busca?q={}'.format(quote_plus(message)))


def calcula(message, event):
    try:
        result = _parser.parse(message).evaluate({})
        out = "{} son : {}".format(
            message,
            result 
        )
    except Exception:
        out = "No he sabido calcularte {}".format(message)
    say(event['channel'], out)


mapping = {
  'ayuda': ayuda,
  'saluda': saluda,
  'hola': saluda,
  'donde esta': where_is,
  'tenemos': do_we_have, 
  'calcula': calcula
}
