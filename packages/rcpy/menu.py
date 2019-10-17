#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    rcpy = root.branch('Recipy')
    rcpy.lookups('Tipi ingrediente', lookup_manager="rcpy.ingrediente_tipo")
    rcpy.thpage('Ingredienti',table='rcpy.ingrediente')
    rcpy.thpage('Tipi ricetta',table='rcpy.ricetta_tipo')
    rcpy.thpage('Ricette',table='rcpy.ricetta')
    
    