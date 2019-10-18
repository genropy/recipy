# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('ingrediente_tipo', pkey='id', name_long='Tipo ingrediente', 
                    name_plural='Tipi',caption_field='descrizione',lookup=True)
        self.sysFields(tbl)
        tbl.column('descrizione',name_long='Descrizione')