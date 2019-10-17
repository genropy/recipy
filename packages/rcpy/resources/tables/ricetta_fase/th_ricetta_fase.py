#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent

class ViewFromRicetta(BaseComponent):
    
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count', counter=True, name='N.',width='3em')
        r.fieldcell('descrizione', width='100%', edit=dict(tag='simpleTextArea', height='10ex'))
        r.fieldcell('minuti_attesa', width='6em', edit=True, totalize=True)
        r.fieldcell('minuti_lavorazione', width='6em', edit=True, totalize=True)
