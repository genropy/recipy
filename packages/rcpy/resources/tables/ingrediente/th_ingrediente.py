#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome', width='25em')
        r.fieldcell('ingrediente_tipo_id',width='15em')
        r.fieldcell('ingrediente_um',width='15em')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')

    def th_top_toolbarsuperiore(self,top):
        top.slotToolbar('5,sections@ingrediente_tipo_id,*',childname='superiore',_position='<bar')


class Form(BaseComponent):
    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px', width='600px', fld_width='5em')
        fb.field('nome', width='20em')
        fb.field('ingrediente_tipo_id',width='15em')
        fb.field('ingrediente_um',width='15em')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
