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

    def th_top_toolbarsuperiore(self,top):
        top.slotToolbar('5,sections@ingrediente_tipo_id,*',childname='superiore',_position='<bar')

    def th_options(self):
        return dict(virtualStore=False, widget='dialog')

class Form(BaseComponent):
    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top', datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px', fld_width='100%',
                              colswidth='auto', margin_right='20px')
        fb.field('nome', colspan=2)
        fb.field('ingrediente_tipo_id')
        fb.field('unita_misura')

        center = bc.contentPane(region='center')
        center.plainTableHandler(title='Usato nelle ricette',
                                relation='@ricette', pbl_classes=True, 
                                viewResource='ViewFromIngrediente', margin='2px')


    def th_options(self):
        return dict(dialog_height='500px', dialog_width='600px')
