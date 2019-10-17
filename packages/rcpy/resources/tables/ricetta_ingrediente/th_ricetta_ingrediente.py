#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrnumber import decimalRound

class ViewFromRicetta(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count', counter=True, name='N.',width='3em')
        r.fieldcell('ingrediente_id', width='20em', edit=True)
        r.fieldcell('@ingrediente_id.misura',width='10em')
        r.fieldcell('qt',  width='6em', edit=True)


