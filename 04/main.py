from read import iterfiles

import os
import numpy as np
from kymatio.numpy import HarmonicScattering3D as scat

from tqdm import tqdm



J=3

dims=(512,512,290)
dims=(48,48,36)#cut away most stuff to be able to run it locally


os.makedirs("output",exist_ok=True)

#print("creating scattering object")
S=scat(J,dims)

for fn,x in tqdm(iterfiles(),total=20):
    x=x[:dims[0],:dims[1],:dims[2]]
    fn=fn.replace(".nii","")
    #print("loaded",fn,x.shape)
    y=S(x)
    #print("scattered, saving")
    np.savez_compressed(f"output/{fn}",q=y,fn=fn)





