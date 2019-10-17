# encoding: utf-8

from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ingrediente',pkey='id',name_long='Ingrediente',
                        name_plural='Ingredienti',caption_field='nome')
        self.sysFields(tbl)
        tbl.column('nome',name_long='Nome',unique=True)
        tbl.column('ingrediente_tipo_id',size='22', group='_', name_long='Tipo'
                    ).relation('ingrediente_tipo.id', 
                                relation_name='ingredienti', 
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('misura',size=':30',
                    values='Numero,Millilitri,Grammi,Kg,Cucchiai,Tazze',
                    name_long='Misura')
