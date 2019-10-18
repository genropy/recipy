#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='rcpy_ntr package',sqlschema='rcpy_ntr',sqlprefix=True,
                    name_short='Rcpy_ntr', name_long='Nutrition', name_full='Rcpy_ntr')
                    
    def config_db(self, pkg):
        pass
        
    def required_packages(self):
        return ['blv:blv']
    
    def campiNutrizionali(self):
        return [
            ('energia_calorie','Calorie','Cal'),
            ('energia_kilojoules','Kilojoules','KJ'),
            ('lipidi_totali_g','Grassi totali','Grassi'),
            ('acidi_grassi_saturi_g','Saturi','Saturi'),
            ('acidi_grassi_monoinsaturi_g','Monoinsaturi','Monoins.'),
            ('acidi_grassi_polinsaturi_g','Polinsaturi','Polins.'),
            ('colesterolo_mg','Colesterolo(mg)','Colest(mg)'),
            ('glucidi_disponibili_g','Glucidi','Glucidi'),
            ('zuccheri_g','Zuccheri','Zucc.'),
            ('amido_g','Amido','Amido'),
            ('fibra_alimentare_g','Fibre','Fibre'),
            ('proteine_g','Proteine','Proteine'),
            ('sale_nacl_g','Sale','Sale')
        ]

        
class Table(GnrDboTable):
    pass