# encoding: utf-8

class Table(object):

    def touch_popolaIngrediente(self,record,old_record=None):

        self.db.table('rcpy.ingrediente').insert(
            dict(alimento_id=record['id'],nome=record['nome'])
        )        