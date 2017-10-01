import os
from os.path import join, exists
import re
import numbers
try:
    # Python 2
    from urllib2 import HTTPError
    from urllib2 import quote
    from urllib2 import urlopen
except ImportError:
    # Python 3+
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.request import urlopen

import numpy as np
import scipy as sp
from scipy import io
from shutil import copyfileobj

from .base import get_data_home
from ..utils import Bunch

