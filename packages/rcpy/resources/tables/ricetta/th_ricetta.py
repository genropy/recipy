#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('titolo')
        r.fieldcell('descrizione')
        r.fieldcell('n_porzioni')
        r.fieldcell('tipo_ricetta_id')
        r.fieldcell('n_difficolta')

    def th_order(self):
        return 'titolo'

    def th_query(self):
        return dict(column='titolo', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record', height='160px')
        fb = top.formbuilder(cols=3, border_spacing='4px', colswidth='auto', width='600px')
        fb.field('titolo', colspan=2, validate_notnull=True)
        fb.field('tipo_ricetta_id', tag='hdbselect')
        fb.field('descrizione', colspan=3, tag='simpleTextArea', height='10ex')
        fb.field('n_porzioni', width='5em', validate_notnull=True)
        fb.field('minuti_preparazione', width='5em')
        fb.field('n_difficolta', tag='filteringSelect', values='3:Difficile,2:Media,1:Facile')

        center = bc.contentPane(region='center')
        center.inlineTableHandler(relation='@ingredienti',
                                   viewResource='ViewFromRicetta',
                                   picker='ingrediente_id',
                                   picker_structure_field='categoria_id')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
