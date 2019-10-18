# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ingrediente',pkey='id',name_long='Ingrediente',
                        name_plural='Ingredienti',caption_field='nome')
        self.sysFields(tbl)
        tbl.column('nome',name_long='Nome',unique=True)
        tbl.column('ingrediente_tipo_id',size='22', group='_', name_long='Tipo',
                    batch_assign=True
                    ).relation('ingrediente_tipo.id', 
                                relation_name='ingredienti', 
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('unita_misura',size=':3',
                    batch_assign=True,
                    values='N:Numero,ml:ml,g:Grammi,Kg:Chili',
                    name_long='Misura',default='g')

