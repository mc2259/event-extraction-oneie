import os
import json
import glob
import tqdm
import traceback
from argparse import ArgumentParser

import torch
from torch.utils.data import DataLoader
from transformers import BertTokenizer, BertConfig
from nltk.tokenize import sent_tokenize, word_tokenize

import sys

from pathlib import Path
cur_dir = Path.cwd()
sys.path.append(str(cur_dir.parents[0] / 'oneie'))

print('Done with imports')
