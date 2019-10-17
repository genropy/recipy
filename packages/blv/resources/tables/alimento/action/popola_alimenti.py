# -*- coding: UTF-8 -*-

from gnr.web.batch.btcaction import BaseResourceAction
from gnr.core.gnrbag import Bag
from decimal import Decimal

caption = 'Popola alimenti' #nome nel menu dei batch
tags = 'admin'  #autorizzazione al batch
description =  'Popola alimenti' #nome piu completo

class Main(BaseResourceAction):
    batch_prefix = 'palim' #identificatore di batch (univoco)
    batch_title = 'Popola alimenti' #titolo all'interno del visore del batch
    batch_delay = 0.5  #periodo campionamento termometro
    batch_cancellable = True

    def do(self):
        alimenti_old = self.tblobj.query().fetch()
        self.cat_dict = self.db.table('rcpy.categoria').query().fetchAsDict(key='hierarchical_nome')
        tbl_alim = self.db.table('rcpy.alimento')
        for a in alimenti_old:
            record_alimento = self.convertiRecord(dict(a))
            tbl_alim.insert(record_alimento)
        self.db.commit()

    def convertiRecord(self, source_record):
        result = dict()
        result['old_categoria'] =  source_record.pop('categoria')
        result['categoria_id'] = self.cat_dict.get(result['old_categoria'].split(';')[0],dict()).get('id')
        result['old_id'] = source_record.pop('id')
        result['old_id_v_40'] = source_record.pop('id_v_40')
        result['old_id_swissfir'] = source_record.pop('id_swissfir')
        u_rif = source_record.pop('unita_di_riferimento')
        u_rif_list = u_rif.replace('per ','').replace(' di parte edibile','').split(' ')
        result['qt_riferimento'], result['um'] = int(u_rif_list[0]), u_rif_list[1]
        result['nome'] = source_record.pop('nome')
        result['sinonimi'] = source_record.pop('sinonimi')
        source_record.pop('voce_modificata')

        for k,v in source_record.items():
            if v is None:
                pass
            elif 'nd' in v or 'tr' in v:
                v = None
            elif v.startswith('<'):
                v=Decimal(v[1:])
            else:
                v=Decimal(v.replace(',','.'))
            result[k]=v
        return result

   #def result_handler(self):
   #    return 'Batch concluso', dict(url='url del file da scaricare', document_name='nome del file')