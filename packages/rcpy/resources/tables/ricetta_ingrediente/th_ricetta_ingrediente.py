#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrnumber import decimalRound


class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('ricetta_id')
        r.fieldcell('ingrediente_id')
        r.fieldcell('qt')
        r.fieldcell('energia_calorie')
        r.fieldcell('energia_kilojoules')
        r.fieldcell('lipidi_totali_g')
        r.fieldcell('acidi_grassi_saturi_g')
        r.fieldcell('acidi_grassi_monoinsaturi_g')
        r.fieldcell('acidi_grassi_polinsaturi_g')
        r.fieldcell('colesterolo_mg')
        r.fieldcell('glucidi_disponibili_g')
        r.fieldcell('zuccheri_g')
        r.fieldcell('amido_g')
        r.fieldcell('fibra_alimentare_g')
        r.fieldcell('proteine_g')
        r.fieldcell('sale_nacl_g')

    def th_order(self):
        return 'ricetta_id'


class ViewEdit(BaseComponent):
    
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('ingrediente_id', width='100%', edit=True)
        r.fieldcell('qt',  width='6em', edit=True)
        r.fieldcell('@ingrediente_id.um', name='U.M.', width='4em')


class ViewValoriNutrizionali(BaseComponent):
    
    def th_struct(self,struct):
        r = struct.view().rows()
        energia = r.columnset('energia', name='Energia', background_color='red')
        grassi = r.columnset('grassi', name='Grassi', background_color='orange')
        zuccheri = r.columnset('zuccheri', name='Zuccheri', background_color='green')

        r.fieldcell('ingrediente_id', width='100%')
        r.fieldcell('qt',  width='6em')
        r.fieldcell('@ingrediente_id.um', name='U.M.', width='4em')

        energia.fieldcell('energia_calorie', totalize=True)
        energia.fieldcell('energia_kilojoules',  totalize=True)

        grassi.fieldcell('lipidi_totali_g', totalize=True)
        grassi.fieldcell('acidi_grassi_saturi_g', totalize=True)
        grassi.fieldcell('acidi_grassi_monoinsaturi_g',  totalize=True)
        grassi.fieldcell('acidi_grassi_polinsaturi_g', totalize=True)
        grassi.fieldcell('colesterolo_mg', totalize=True)

        zuccheri.fieldcell('glucidi_disponibili_g', totalize=True)
        zuccheri.fieldcell('zuccheri_g', totalize=True)
        r.fieldcell('amido_g', totalize=True)
        r.fieldcell('fibra_alimentare_g', totalize=True)
        r.fieldcell('proteine_g', totalize=True)
        r.fieldcell('sale_nacl_g', totalize=True)

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('ricetta_id' )
        fb.field('ingrediente_id' )
        fb.field('qt')
        fb.field('calorie' )
        fb.field('kilojoule' )
        fb.field('lipidi_totali_g' )
        fb.field('acidi_grassi_saturi_g' )
        fb.field('acidi_grassi_monoinsaturi_g' )
        fb.field('acidi_grassi_polinsaturi_g' )
        fb.field('colesterolo_mg' )
        fb.field('glucidi_disponibili_g' )
        fb.field('zuccheri_g' )
        fb.field('amido_g' )
        fb.field('fibra_alimentare_g' )
        fb.field('proteine_g' )
        fb.field('sale_nacl_g' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
