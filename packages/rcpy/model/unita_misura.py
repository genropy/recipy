# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('unita_misura', pkey='codice', name_long='Unità di misura', 
                    name_plural='Unità di misura',caption_field='descrizione',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('codice',size=':5',name_long='Codice')
        tbl.column('descrizione',name_long='Descrizione')