# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ricetta_ingrediente',pkey='id',name_long='Ingrediente ricetta',name_plural='Ingredienti ricetta',caption_field='id')
        self.sysFields(tbl)
        tbl.column('ricetta_id',size='22',name_long='Ricetta Id').relation('rcpy.ricetta.id',relation_name='ingredienti', mode='foreignkey', onDelete='cascade')
        tbl.column('ingrediente_id',size='21',name_long='Ingrediente Id').relation('rcpy.ingrediente.id',relation_name='ricette', mode='foreignkey', onDelete='raise')
        tbl.column('qt',dtype='N',name_long='Quantità')
        tbl.column('tot_energia_calorie',dtype='N',name_long='Tot Calorie')
        tbl.column('tot_energia_kilojoule',dtype='N',name_long='Tot Kilojoul')
        tbl.column('tot_lipidi_totali_g', dtype='N', name_long='Lipidi g')
        tbl.column('tot_acidi_grassi_saturi_g', dtype='N', name_long='Grassi saturi g')
        tbl.column('tot_acidi_grassi_monoinsaturi_g', dtype='N', name_long='Grassi monoinsaturi g')
        tbl.column('tot_acidi_grassi_polinsaturi_g', dtype='N', name_long='Grassi polinsaturei g')
        tbl.column('tot_colesterolo_mg', dtype='N', name_long='Colesterolo mg')
        tbl.column('tot_glucidi_disponibili_g', dtype='N', name_long='Glucidi disp. g')
        tbl.column('tot_zuccheri_g', dtype='N', name_long='Zuccheri g')
        tbl.column('tot_amido_g', dtype='N', name_long='Amido g')
        tbl.column('tot_fibra_alimentare_g', dtype='N', name_long='Fibra g')
        tbl.column('tot_proteine_g',  dtype='N', name_long='Proteine g')
        tbl.column('tot_sale_nacl_g', dtype='N', name_long='Sale g')