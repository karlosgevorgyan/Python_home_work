# -*- coding: utf-8 -*-

from model.generator import generate_data
from model.importer import import_data
from model.exporter import export_data
from model.comparator import compare_data


def process():
    generate_data()
    import_data()
    export_data()
    compare_data()


process()
