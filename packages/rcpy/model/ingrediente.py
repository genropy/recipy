# encoding: utf-8

from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ingrediente',pkey='id',name_long='Ingrediente',name_plural='Ingredienti',caption_field='nome')
        self.sysFields(tbl)
        tbl.column('nome',name_long='Nome',unique=True)
        tbl.column('sinonimi', name_long='Sinonimi')
        tbl.column('um',size=':2')
        tbl.column('qt_riferimento',dtype='N',name_long='Qt rif.')
        tbl.column('categoria_id',size='22',name_long='Categoria').relation('rcpy.categoria.id',relation_name='ingredienti', mode='foreignkey', onDelete='raise')
        
        tbl.column('energia_kilojoules', dtype='N', name_long='Kilojoules')
        tbl.column('energia_calorie', dtype='N', name_long='Calorie')
        tbl.column('lipidi_totali_g', dtype='N', name_long='Lipidi g')
        tbl.column('acidi_grassi_saturi_g', dtype='N', name_long='Grassi saturi g')
        tbl.column('acidi_grassi_monoinsaturi_g', dtype='N',name_long='Grassi monoinsaturi g')
        tbl.column('acidi_grassi_polinsaturi_g', dtype='N',name_long='Grassi polinsaturei g')
        tbl.column('colesterolo_mg',dtype='N', name_long='Colesterolo mg')
        tbl.column('glucidi_disponibili_g', dtype='N',name_long='Glucidi disp. g')
        tbl.column('zuccheri_g',dtype='N', name_long='Zuccheri g')
        tbl.column('amido_g',dtype='N', name_long='Amido g')
        tbl.column('fibra_alimentare_g', dtype='N',name_long='Fibra g')
        tbl.column('proteine_g',dtype='N', name_long='Proteine g')
        tbl.column('sale_nacl_g',dtype='N', name_long='Sale g')

    @metadata(doUpdate=True)
    def touch_fixNome(self, record, old_record):
        record['nome'] = record['nome'].replace('(in media)', '')