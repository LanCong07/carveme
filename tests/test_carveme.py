#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `carveme` package."""


import unittest

from carveme import project_dir
from carveme.cli.carve import maincall
from reframed import load_cbmodel, FBA


MIN_GROWTH = 0.5

class TestCarveme(unittest.TestCase):

    def test_carve(self):
        maincall(
            inputfile=project_dir + 'data/benchmark/fasta/Ecoli_K12_MG1655.faa',
            verbose=True,
            default_score=-1.0,
            uptake_score=0.0,
            gapfill='LB,M9',
            init='M9',
        )

    def test_simulation(self):
        model = load_cbmodel(project_dir + 'data/benchmark/fasta/Ecoli_K12_MG1655.xml')
        sol = FBA(model)
        print(sol)
        self.assertGreater(sol.fobj, MIN_GROWTH)
