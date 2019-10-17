# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('categoria',pkey='id',name_long='Categoria ingredienti',name_plural='Categorie ingredienti',caption_field='nome')
        self.sysFields(tbl,hierarchical='nome',counter=True)
        tbl.column('nome',name_long='Nome',unique=True,indexed=True)
