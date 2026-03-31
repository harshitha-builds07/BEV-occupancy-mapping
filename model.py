import torch
import torch.nn as nn
import torchvision.models as models
import matplotlib.pyplot as plt
#cnn feature extractor
class Encoder(nn.Module):
    def __init__(self):
        super().__init__()
        resnet=models.resnet18(pretrained=True)
        self.backbone=nn.Sequential(*list(resnet.children())[:-2])
    def forward(self,x):
        return self.backbone(x)
#mapping to bev grid using interpolation
class BEVProjector(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self,features):
        bev=torch.mean(features,dim=2,keepdim=True)
        return bev
#occupancy head
class OccupancyHead(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv=nn.Conv2d(512,1,kernel_size=1)
    def forward(self,x):
        return torch.sigmoid(self.conv(x))
#attaining the full model
class BEVModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder=Encoder()
        self.projector=BEVProjector()
        self.head=OccupancyHead()
    def forward(self,x):
        features=self.encoder(x)
        bev=self.projector(features)
        out=self.head(bev)
        return out
#converting input image to tensor
