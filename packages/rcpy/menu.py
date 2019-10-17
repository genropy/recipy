#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    rcpy = root.branch('Recipy')
    rcpy.thpage('Categorie ingredienti',table='rcpy.categoria')
    rcpy.thpage('Tipi ricetta',table='rcpy.tipo_ricetta')
    rcpy.thpage('Ingredienti',table='rcpy.ingrediente')
    rcpy.thpage('Ricette',table='rcpy.ricetta')
    rcpy.webpage('Preparazione',filepath='/rcpy/preparazione')
    