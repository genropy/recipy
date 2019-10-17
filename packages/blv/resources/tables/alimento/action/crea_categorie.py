# -*- coding: UTF-8 -*-

from gnr.web.batch.btcaction import BaseResourceAction
from gnr.core.gnrbag import Bag

caption = 'Crea categorie' #nome nel menu dei batch
tags = 'admin'  #autorizzazione al batch
description =  'Crea categorie' #nome piu completo

class Main(BaseResourceAction):
    batch_prefix = 'ccat' #identificatore di batch (univoco)
    batch_title = 'Crea categorie' #titolo all'interno del visore del batch
    batch_delay = 0.5  #periodo campionamento termometro
    batch_cancellable = True

    def do(self):
        categorie_raw = self.tblobj.query(columns='$categoria', distinct=True).fetch()
        categorie = []
        for c in categorie_raw:
            c_name = c["categoria"]
            if ";" in c_name:
                categorie.extend(c_name.split(";"))
            else:
                categorie.append(c_name)
        categorie = list(set(categorie))
        categorie.sort()
        
        self.tbl_cat = self.db.table('rcpy.categoria')
        self.cat_dict = dict()
        for c in categorie:
            self.insertCategoria(c)
        self.db.commit()

    def insertCategoria(self, categoria):
        cs = categoria.rsplit('/',1)
        if len(cs)>1:
            child_name = cs[1]
            parent_id = self.cat_dict.get(cs[0], None)
            if not parent_id:
                parent_id = self.insertCategoria(cs[0])
        else:
            child_name = cs[0]
            parent_id=None
        cat_record = dict(nome=child_name, parent_id= parent_id)
        self.tbl_cat.insert(cat_record)
        self.cat_dict[categoria] = cat_record['id']
        return cat_record['id']


   #def result_handler(self):
   #    return 'Batch concluso', dict(url='url del file da scaricare', document_name='nome del file')