#!C:\Users\andrew.mushokambere\Documents\Data Science Capacity Building Inniative\myenv\Scripts\python.exe

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.ogr_layer_algebra as a convenience to use as a script
from osgeo_utils.ogr_layer_algebra import *  # noqa
from osgeo_utils.ogr_layer_algebra import main

deprecation_warn("ogr_layer_algebra")
sys.exit(main(sys.argv))
