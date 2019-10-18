# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ricetta_tipo',pkey='id',
                        name_long='Tipo Ricetta',
                        name_plural='Tipi ricetta',
                        caption_field='nome')
        self.sysFields(tbl, hierarchical='nome', counter=True)
        tbl.column('nome',name_long='Nome')
