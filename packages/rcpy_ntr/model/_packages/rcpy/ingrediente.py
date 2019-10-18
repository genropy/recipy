# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('ingrediente')
        tbl.column('alimento_id',size='22', group='_', name_long='Alimento',plugToForm=dict(width='20em'),
                    batch_assign=True
                    ).relation('blv.alimento.id', relation_name='ingredienti_collegati', 
                    mode='foreignkey', onDelete='raise')        
        tbl.column('conversione', dtype='N', name_long='Conversione',plugToForm=True,default=1)  
        tbl.aliasColumn('alimento_um','@alimento_id.um',
                        name_long='Unità di misura (alimento)',
                        name_short='UM(Al)',plugToForm=True)
        tbl.aliasColumn('qt_riferimento','@alimento_id.qt_riferimento',
                        name_long='Quantità di riferimento',
                        name_short='Qt.Rif.',plugToForm=True)
        tbl.formulaColumn('convertitore',"COALESCE($conversione,1)/$qt_riferimento")
        self.aggiungiColonneNutrizionali(tbl)
    
    def aggiungiColonneNutrizionali(self,tbl):
        formula = '$convertitore * @alimento_id.{valore}'
        for field,name_long,name_short in self.db.application.packages['rcpy_ntr'].campiNutrizionali():
            tbl.formulaColumn(field,formula.format(valore=field),dtype='N',
                            name_long=name_long,name_short=name_short)