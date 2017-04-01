#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import re
from blessings import Terminal
from validate_email import validate_email
import requests
import sys
_site_ = sys.argv[1]
_saida_ = sys.argv[2]
_file_ = open(_saida_, "w")
t = Terminal()
r = requests.get(_site_)
conteudo = r.content
_file_ = open(_saida_, "w")
_filtro_ = re.findall(r'[\w\.-]+@[\w\.-]+', conteudo)
for line in _filtro_:
   if validate_email(line, verify=True)==False:
     print line, t.red("INVALID!")
   else:
     print line, t.green("OK!")
     _file_.write(line)
     _file_.write("\n")
