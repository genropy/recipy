#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class ViewValoriNutrizionali(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        energia = r.columnset('energia', name='Energia', 
                                background='rgba(38, 88, 32, 1.00)',
                                cell_width='5em',cell_background='rgba(38, 88, 32, 0.20)')
        grassi = r.columnset('grassi', name='Grassi', 
                            background='rgba(128, 23, 14, 1.00)',
                            cell_background='rgba(128, 23, 14, 0.20))',
                            cell_width='5em')
        zuccheri = r.columnset('zuccheri', name='Zuccheri', 
                            background='rgba(64, 128, 180, 1.00)',
                            cell_background='rgba(64, 128, 180, 0.20)',
                                cell_width='5em')

        r.fieldcell('ingrediente_id', width='100%',min_width='20em')
        r.fieldcell('qt',  width='6em')
        r.fieldcell('@ingrediente_id.@alimento_id.um', name='U.M.', width='4em')

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
