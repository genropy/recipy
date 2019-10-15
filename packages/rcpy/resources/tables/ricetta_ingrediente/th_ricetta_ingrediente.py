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
        r.fieldcell('tot_energia_calorie')
        r.fieldcell('tot_energia_kilojoules')
        r.fieldcell('tot_lipidi_totali_g')
        r.fieldcell('tot_acidi_grassi_saturi_g')
        r.fieldcell('tot_acidi_grassi_monoinsaturi_g')
        r.fieldcell('tot_acidi_grassi_polinsaturi_g')
        r.fieldcell('tot_colesterolo_mg')
        r.fieldcell('tot_glucidi_disponibili_g')
        r.fieldcell('tot_zuccheri_g')
        r.fieldcell('tot_amido_g')
        r.fieldcell('tot_fibra_alimentare_g')
        r.fieldcell('tot_proteine_g')
        r.fieldcell('tot_sale_nacl_g')

    def th_order(self):
        return 'ricetta_id'

    def th_query(self):
        return dict(column='id', op='contains', val='')


class ViewFromRicetta(BaseComponent):
    
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('ingrediente_id', edit=dict(remoteRowController=True,validate_notnull=True), width='15em')
        r.fieldcell('qt', edit=dict(remoteRowController=True,validate_notnull=True), width='6em')
        r.fieldcell('@ingrediente_id.um', name='U.M.', width='4em')
        r.fieldcell('tot_energia_calorie', totalize=True)
        r.fieldcell('tot_energia_kilojoules',  totalize=True)
        r.fieldcell('tot_lipidi_totali_g', totalize=True)
        r.fieldcell('tot_acidi_grassi_saturi_g', totalize=True)
        r.fieldcell('tot_acidi_grassi_monoinsaturi_g',  totalize=True)
        r.fieldcell('tot_acidi_grassi_polinsaturi_g', totalize=True)
        r.fieldcell('tot_colesterolo_mg', totalize=True)
        r.fieldcell('tot_glucidi_disponibili_g', totalize=True)
        r.fieldcell('tot_zuccheri_g', totalize=True)
        r.fieldcell('tot_amido_g', totalize=True)
        r.fieldcell('tot_fibra_alimentare_g', totalize=True)
        r.fieldcell('tot_proteine_g', totalize=True)
        r.fieldcell('tot_sale_nacl_g', totalize=True)

    @public_method
    def th_remoteRowController(self,row=None,field=None,**kwargs):
        field = field or 'ingrediente_id'
        
        if not row['ingrediente_id']:
            return row
        ingrediente_record = self.db.table('rcpy.ingrediente').record(row['ingrediente_id'], mode='dict')
        if not row['qt']:
            row['qt'] = ingrediente_record['qt_riferimento']
        for k in row.keys():
            if k.startswith('tot_'):
                grandezza = k[4:]
                valore = ingrediente_record.get(grandezza)
                if valore is None:
                    row[k] = valore
                else:
                    row[k] = valore * row['qt'] / ingrediente_record['qt_riferimento']   
        return row

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('ricetta_id' )
        fb.field('ingrediente_id' )
        fb.field('qt')
        fb.field('tot_calorie' )
        fb.field('tot_kilojoule' )
        fb.field('tot_lipidi_totali_g' )
        fb.field('tot_acidi_grassi_saturi_g' )
        fb.field('tot_acidi_grassi_monoinsaturi_g' )
        fb.field('tot_acidi_grassi_polinsaturi_g' )
        fb.field('tot_colesterolo_mg' )
        fb.field('tot_glucidi_disponibili_g' )
        fb.field('tot_zuccheri_g' )
        fb.field('tot_amido_g' )
        fb.field('tot_fibra_alimentare_g' )
        fb.field('tot_proteine_g' )
        fb.field('tot_sale_nacl_g' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
