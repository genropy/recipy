#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class Form(BaseComponent):
    def th_form(self, form):
        bc = form.center.borderContainer()
        self.ricettaInfo(bc.contentPane(region='top',datapath='.record'))
        tc = bc.tabContainer(region='center')
        tab1 = tc.borderContainer(title='Ingredienti & Fasi')
        self.ricettaIngredienti(tab1.contentPane(region='left', width='40%'))
        self.ricettaFasi(tab1.contentPane(region='center'))
        self.valoriNutrizionali(tc.contentPane(title='Valori nutrizionali'))

    def valoriNutrizionali(self,pane):
        pane.plainTableHandler(relation='@ingredienti',viewResource='ViewValoriNutrizionali')