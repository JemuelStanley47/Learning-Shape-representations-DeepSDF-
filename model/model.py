import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset

class Decoder(nn.Module):
  def __init__(self, latent_size=256, dims=512, drop_prob = 0.2, weight_norm=True):
    super(Decoder, self).__init__()
    # TODO: Create laers according to architecture

    

    # Non-linear output
    self.tanh = nn.Tanh()
  
  def forward(self, input):
    # TODO: Call layers
    x = None

    # Make sure to have skip connection to 4th layer

    
    return x