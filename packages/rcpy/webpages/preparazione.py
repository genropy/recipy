# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    py_requires = 'gnrcomponents/framegrid:FrameGrid'

    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')
        top = bc.contentPane(region='top')
        fb = top.formbuilder(cols=3)
        fb.dbselect(value='^.ricetta_id',dbtable='rcpy.ricetta',lbl='Ricetta')
        fb.numberTextBox(value='^.porzioni',lbl='Porzioni',width='4em')
        fb.timeTextBox(value='^.ora_pasto',lbl='Servire alle')
        center = bc.borderContainer(region='center')
        bc.dataRpc('.risultati',self.getPreparazione,ricetta_id='^.ricetta_id',
                    porzioni='^.porzioni',ora_pasto='^.ora_pasto',
                    _if='ricetta_id&&porzioni&&ora_pasto')
        center.div('^.risultati')

    @public_method
    def getPreparazione(self,ricetta_id=None,porzioni=None,ora_pasto=None):
        porzioni_ricetta = self.db.table('rcpy.ricetta').readColumns(columns='$n_porzioni',
                                                pkey=ricetta_id)
        ingredienti = self.db.table('rcpy.ricetta_ingrediente'
                            ).query(where='$ricetta_id=:rid',
                                    columns='$ingrediente_nome,$qt',
                                    rid=ricetta_id).fetch()

        fasi = self.db.table('rcpy.ricetta_fase').query(where='$ricetta_id=:rid',
                rid=ricetta_id).fetch()
        result = []
        result.append('<h1 class="ingredienti">Ingredienti</h1>')
        result.append('<ul>')
        for ing in ingredienti:
            riga = dict(ing)
            riga['qt'] = riga['qt']*porzioni/porzioni_ricetta
            result.append('<li>{ingrediente_nome}: {qt}</li>'.format(**riga))
        result.append('</ul>')
        return ''.join(result)


    #def xx(self)
    #    center.dataRecord('.ricetta','rcpy.ricetta',pkey='^.ricetta_id')
#
    #    bc.contentPane(region='left',width='50%',margin='2px',border='1px solid gray').quickGrid(value='^.ingredienti')
    #    bc.contentPane(region='center',margin='2px',border='1px solid gray').quickGrid(value='^.fasi')
#
    #    center.dataSelection('.ingredienti','rcpy.ricetta_ingrediente',
    #                        where='$ricetta_id=:rid',rid='^.ricetta_id')
    #    center.dataSelection('.fasi','rcpy.ricetta_fase',
    #                        where='$ricetta_id=:rid',rid='^.ricetta_id')
    #        