# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('ricetta_ingrediente')
        self.aggiungiColonneNutrizionali(tbl)



    def aggiungiColonneNutrizionali(self,tbl):
        formula = '$qt * @ingrediente_id.{valore}'
        for field,name_long,name_short in self.db.application.packages['rcpy_ntr'].campiNutrizionali():
            tbl.formulaColumn(field,formula.format(valore=field),dtype='N',
                             name_long=name_long,name_short=name_short)