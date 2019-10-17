# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ricetta',pkey='id',name_long='Ricetta',name_plural='Ricette',caption_field='titolo')
        self.sysFields(tbl)
        tbl.column('titolo',name_long='Titolo')
        tbl.column('descrizione',name_long='Descrizione')
        tbl.column('n_porzioni',dtype='I',name_long='N.Porzioni', default=2)
        tbl.column('ricetta_tipo_id',size='22',
                    name_long='Tipo ricetta'
                    ).relation('rcpy.ricetta_tipo.id',
                                relation_name='ricette', 
                                mode='foreignkey', 
                                onDelete='raise')
        tbl.column('n_difficolta',dtype='I',name_long='Difficoltà')