# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):

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
        center.div('^.risultati',margin='10px')

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
        result.append('<h1 class="titolo">Ingredienti</h1>')
        result.append('<table style="width:500px;border-collapse:collapse;border:1px solid silver;">')
        result.append('<thead style="background:#555;color:white"><th>Ingrediente</th><th>Quantità</th></thead>')
        for ing in ingredienti:
            riga = dict(ing)
            riga['qt'] = riga['qt']*porzioni/porzioni_ricetta
            result.append('<tr><td>{ingrediente_nome}:</td><td>{qt}</td></tr>'.format(**riga))
        result.append('</table>')

        result.append('<h1 class="titolo">Fasi</h1>')
        result.append('<table style="width:500px;border-collapse:collapse;border:1px solid silver;">')
        result.append('<thead style="background:#555;color:white"><th>Descrizione</th><th>T(lav)</th><th>T(att)</th></thead>')
        for f in fasi:
            riga = dict(f)
            riga['minuti_attesa'] = riga['minuti_attesa'] or ''
            riga['minuti_lavorazione'] = riga['minuti_lavorazione'] or '' 
 
            result.append('<tr><td>{descrizione}:</td><td>{minuti_lavorazione}</td><td>{minuti_attesa}</td></tr>'.format(**riga))
        result.append('</table>')

        return ''.join(result)
