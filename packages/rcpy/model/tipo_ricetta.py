# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tipo_ricetta',pkey='id',name_long='Tipo Ricetta',name_plural='Tipi ricetta',caption_field='nome')
        self.sysFields(tbl,hierarchical=True,counter=True)
        tbl.column('nome',name_long='Nome')
        tbl.column('descrizione',name_long='Descrizione')
