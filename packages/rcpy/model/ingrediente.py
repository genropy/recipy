# encoding: utf-8
  
class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ingrediente',pkey='id',name_long='Ingrediente',
                        name_plural='Ingredienti',caption_field='nome')
        self.sysFields(tbl)
        tbl.column('nome', name_long='Nome', unique=True)
        tbl.column('tipo_ingrediente',  name_long='Tipo ingrediente')