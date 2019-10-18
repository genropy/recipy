#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('hierarchical_nome',width='30em')


    def th_query(self):
        return dict(column='id', op='contains', val='')


class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('nome',width='30em')
        th = bc.contentPane(title='Ricette', region='center').plainTableHandler(relation='@ricette',pbl_classes=True, margin='2px')
        form.htree.relatedTableHandler(th,dropOnRoot=False,inherited=True)

    def th_options(self):
        return dict(hierarchical=True)
