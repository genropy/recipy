#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='rcpy package',sqlschema='rcpy',sqlprefix=True,
                    name_short='Rcpy', name_long='Ricette', name_full='Rcpy')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
