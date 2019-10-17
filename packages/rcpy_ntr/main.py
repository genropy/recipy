#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='rcpy_ntr package',sqlschema='rcpy_ntr',sqlprefix=True,
                    name_short='Rcpy_ntr', name_long='Nutrition', name_full='Rcpy_ntr')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
