#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    blv = root.branch('Blv')
    blv.thpage('Categorie',table='blv.categoria')
    blv.thpage('Alimento',table='blv.alimento')
    
    