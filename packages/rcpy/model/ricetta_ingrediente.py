# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ricetta_ingrediente',pkey='id',name_long='Ingrediente ricetta',name_plural='Ingredienti ricetta',caption_field='id')
        self.sysFields(tbl)
        tbl.column('ricetta_id',size='22',name_long='Ricetta').relation('rcpy.ricetta.id',relation_name='ingredienti', mode='foreignkey', onDelete='cascade')
        tbl.column('ingrediente_id',size='22',name_long='Ingrediente').relation('rcpy.ingrediente.id',relation_name='ricette', mode='foreignkey', onDelete='raise')
        tbl.column('qt',dtype='N',name_long='Quantità')

        tbl.aliasColumn('ingrediente_nome','@ingrediente_id.nome',name_long='Nome ingrediente')
        
        calcolo_tpl = '@ingrediente_id.{} * qt / @ingrediente_id.qt_riferimento / @ricetta_id.n_porzioni'
        
        tbl.formulaColumn('energia_calorie', calcolo_tpl.format('energia_calorie'), name_long='Calorie')
        tbl.formulaColumn('energia_kilojoules', calcolo_tpl.format('energia_kilojoules'), name_long='Kilojoules')
        tbl.formulaColumn('lipidi_totali_g', calcolo_tpl.format('lipidi_totali_g'), name_long='Lipidi')
        tbl.formulaColumn('acidi_grassi_saturi_g', calcolo_tpl.format('acidi_grassi_saturi_g'), name_long='Gr.Saturi')
        tbl.formulaColumn('acidi_grassi_monoinsaturi_g', calcolo_tpl.format('acidi_grassi_monoinsaturi_g'), name_long='Gr.Monoinsaturi')
        tbl.formulaColumn('acidi_grassi_polinsaturi_g', calcolo_tpl.format('acidi_grassi_polinsaturi_g'), name_long='Gr.Polinsaturi')
        tbl.formulaColumn('colesterolo_mg', calcolo_tpl.format('colesterolo_mg'), name_long='Colesterolo mg')
        tbl.formulaColumn('glucidi_disponibili_g', calcolo_tpl.format('glucidi_disponibili_g'), name_long='Glucidi disp.')
        tbl.formulaColumn('zuccheri_g', calcolo_tpl.format('zuccheri_g'), name_long='Zuccheri')
        tbl.formulaColumn('fibra_alimentare_g', calcolo_tpl.format('fibra_alimentare_g'), name_long='Fibra')
        tbl.formulaColumn('proteine_g', calcolo_tpl.format('proteine_g'), name_long='Proteine')
        tbl.formulaColumn('amido_g', calcolo_tpl.format('amido_g'), name_long='Amido')
        tbl.formulaColumn('sale_nacl_g', calcolo_tpl.format('sale_nacl_g'), name_long='Sale')
