from contextlib import ExitStack
from copy import copy
import functools
import io
import os
from pathlib import Path
import platform
import sys
import urllib.request

import matplotlib
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt

from PIL import Image

from matplotlib import image
from matplotlib.image import _ImageBase
from matplotlib import transforms
from matplotlib.transforms import Bbox

import pytest

def test_make_image_empty():
    #Attempting to use _make_image with the image set as None should produce a RuntimeError.
    with pytest.raises(RuntimeError) as e_info:
        image_base = _ImageBase(None,None)
        image_base._make_image(None,None,None,None,None)

def test_make_image_zero_magnification():
    #Setting magnification to zero should return None,0,0,None.
    image_base = _ImageBase(None,None)
    png_path = Path(__file__).parent / "baseline_images/pngsuite/basn3p04.png"
    bbox = Bbox([[1, 2], [3, 4]])
    temp_image = Image.open(png_path)
    result = image_base._make_image(temp_image,bbox,bbox,bbox,magnification=0)
    assert(result == (None,0,0,None))
    temp_image.close()