import argparse

import torch
from torch import nn, optim


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--string', type=str, default='c9s\nHAPPY\nBIRTHDAY\n')
    args = parser.parse_args()
    x = torch.Tensor([9, 3])
    y = torch.Tensor([ord(s) for s in args.string])
    net = nn.Linear(len(x), len(y))
    optimizer = optim.Adam(net.parameters())
    num_steps = 15000
    for _ in range(num_steps):
        out = net(x)
        loss = (y - out).pow(2).mean()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        try:
            print(''.join(map(lambda s: chr(round(s)), out.tolist())))
        except Exception:
            pass

if __name__ == '__main__':
    main()
