import keyword
import torch
import tensorboardX as tbx
import numpy as np
import torchvision
import PIL




writer = tbx.SummaryWriter('runs/exp-1')
#writer.add_embedding(torch.randn(100, 5), metadata=meta, label_img=label_img)
writer.add_scalar('loss', torch.tensor([0.3]).item(), 1)
writer.add_scalar('loss', torch.tensor([0.9]).item(), 2)
#writer.add_embedding(torch.randn(100, 5), metadata=meta)
writer.close()
