# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ricetta_ingrediente',
                        pkey='id',name_long='Ingrediente ricetta',
                        name_plural='Ingredienti ricetta',caption_field='id')
        self.sysFields(tbl,counter='ricetta_id')
        tbl.column('ricetta_id',size='22',name_long='Ricetta'
                    ).relation('rcpy.ricetta.id',
                                relation_name='ingredienti', 
                                mode='foreignkey', 
                                onDelete='cascade')
        tbl.column('ingrediente_id',size='22',name_long='Ingrediente'
                    ).relation('rcpy.ingrediente.id',
                                relation_name='ricette', 
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('qt',dtype='N',name_long='Quantità')

        tbl.aliasColumn('ingrediente_nome','@ingrediente_id.nome',name_long='Nome ingrediente')
        
        