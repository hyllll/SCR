import matplotlib.pyplot as plt
import IPython.display as ipd

import os
import json
import math
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
import vits_lib.commons as commons
import vits_lib.utils as vits_utils
from vits_lib.models import SynthesizerTrn
from vits_lib.text.symbols import symbols
from scipy.io.wavfile import write
from utils import *


if __name__ == '__main__':
    vctk_to_speaker_id, total_speaker = preprocess_speaker_info()
    agent, user = load_vits_model()
    text = "VITS is Awesome!"
    audio = generate_agent_speech(agent, text)
