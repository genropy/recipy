#!/usr/bin/python
# -*- coding: utf-8 -*-

def config(root,application=None):
    blv = root.branch('blv')
    blv.thpage('alimento',table='blv.alimento')
