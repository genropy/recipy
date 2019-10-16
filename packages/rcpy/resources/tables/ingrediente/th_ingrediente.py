#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome', width='25em')
        r.fieldcell('categoria_id', width='15em')
        r.fieldcell('qt_riferimento')
        r.fieldcell('energia_kilojoules')
        r.fieldcell('energia_calorie')
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
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')


class ViewEdit(BaseComponent):
    
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome', width='20em', edit=dict(validate_notnull=True))
        r.fieldcell('categoria_id', edit=dict(validate_notnull=True))
        r.fieldcell('qt_riferimento',  edit=dict(validate_notnull=True))
        r.fieldcell('um', edit=dict(validate_notnull=True, tag='filteringSelect', values='g,ml'))

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px', width='600px', fld_width='5em')
        fb.field('nome', colspan=2, width='100%')
        fb.field('um', tag='filteringSelect', values='g,ml')
        fb.field('qt_riferimento')
        fb.field('energia_kilojoules' )
        fb.field('energia_calorie' )
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
