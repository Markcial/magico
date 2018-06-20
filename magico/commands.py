# -*- coding: utf-8 -*-
import re
import paramiko
from os.path import expanduser
from magico.actions import say, react, get_realname
from urllib.parse import quote_plus
from py_expression_eval import Parser


_ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
_ssh = paramiko.SSHClient()
_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
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


def arsa(message, event):
    react(event['channel'], 'dancer', event['ts'])

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


def ninot_report(message, event):
    try:
        _ssh.connect(
            '10.224.0.80',
            username='pi',
            key_filename='{}/.ssh/id_rsa'.format(expanduser("~"))
        )
        stdin, stdout, stderr = _ssh.exec_command('report')
        text = _ansi_escape.sub('', stdout.read().decode('utf8'))
        out = "El reporte es este:\n{}".format(text)
    except Exception as e:
        print(e)
        out = "No he sido capaz de ver como esta la raspy de ninot!"
    say(event['channel'], out)


mapping = {
  'ayuda': ayuda,
  'saluda': saluda,
  'hola': saluda,
  'ese': arsa,
  'ese pedazo': arsa,
  'donde esta': where_is,
  'como esta la raspberry del ninot': ninot_report,
  'tenemos': do_we_have, 
  'calcula': calcula
}
