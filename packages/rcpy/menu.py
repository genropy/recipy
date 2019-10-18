#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    rcpy = root.branch('Recipy')
    rcpy.thpage('Ingredienti',table='rcpy.ingrediente')
    rcpy.lookups('Altre tabelle', lookup_manager='rcpy')