# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ricetta_fase',pkey='id',name_long='Fase ricetta',
                        name_plural='Fasi ricetta',
                        caption_field='descrizione')
        self.sysFields(tbl,counter='ricetta_id')
        tbl.column('ricetta_id',size='22',name_long='Ricetta'
                    ).relation('rcpy.ricetta.id',
                                relation_name='fasi', 
                                mode='foreignkey', 
                                onDelete='cascade')
        tbl.column('descrizione',name_long='Descrizione')
        tbl.column('minuti_attesa',dtype='I',name_long='Min. attesa', 
                    name_short='Min Att')
        tbl.column('minuti_lavorazione',dtype='I',name_long='Min. lavorazione', 
                    name_short='Min Lav')
