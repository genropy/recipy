#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

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
