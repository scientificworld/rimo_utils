import time
import contextlib

import torch


@contextlib.contextmanager
def 计时(名字=''):
    torch.cuda.synchronize()
    开始时间 = time.time()
    yield
    if 名字: 
        名字 = f'「{名字}」'
    torch.cuda.synchronize()
    print(f'{名字}用时:', time.time()-开始时间)
