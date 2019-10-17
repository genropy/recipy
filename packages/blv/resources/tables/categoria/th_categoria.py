#!/usr/bin/python
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome')
        r.fieldcell('hierarchical_nome')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('nome')
       # th = bc.contentPane(title='Ingredienti', region='center').inlineTableHandler(relation='@ingredienti',
       #                                                                              pbl_classes=True,
       #                                                                              margin='2px',
       #                                                                              viewResource='ViewEdit')
       # form.htree.relatedTableHandler(th,dropOnRoot=False,inherited=True)

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', hierarchical=True)
