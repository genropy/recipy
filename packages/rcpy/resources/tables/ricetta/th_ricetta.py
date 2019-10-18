#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('titolo',width='20em')
        r.fieldcell('descrizione',width='30em')
        r.fieldcell('n_porzioni')
        r.fieldcell('ricetta_tipo_id')
        r.fieldcell('n_difficolta')

    def th_order(self):
        return 'titolo'

    def th_query(self):
        return dict(column='titolo', op='contains', val='')


class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        pane = bc.contentPane(region='top',datapath='.record')
        fb = pane.formbuilder(cols=3, border_spacing='4px', colswidth='auto', width='600px')
        fb.field('titolo', colspan=2, validate_notnull=True)
        fb.field('ricetta_tipo_id')
        fb.field('descrizione', colspan=3, tag='simpleTextArea', height='10ex')
        fb.field('n_porzioni', width='5em', validate_notnull=True)
        fb.field('n_difficolta', tag='filteringSelect', values='3:Difficile,2:Media,1:Facile')