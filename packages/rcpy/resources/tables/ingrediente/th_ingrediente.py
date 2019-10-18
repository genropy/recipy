#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome', width='25em')
        r.fieldcell('ingrediente_tipo_id',width='15em')
        r.fieldcell('unita_misura',width='15em')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')

class Form(BaseComponent):
    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px', width='600px', colswidth='auto')
        fb.field('nome', width='30em', colspan=2)
        fb.field('ingrediente_tipo_id')
        fb.field('unita_misura')