import numpy as np
from scipy import ndimage
from kymatio.numpy import HarmonicScattering3D

rot=True

np.random.seed(12)

#basically the first example from 
#https://www.kymat.io/codereference.html

# Set the parameters of the scattering transform.
J = 3
M, N, O = 32, 32, 32

# Generate a sample signal.
x = np.random.randn(M, N, O)

#x=ndimage.rotate(x,33,reshape=False)#not so clear how to define rotation for other angles than multiples of 90°
x=np.rot90(x,axes=(1,2))#so I just take 90 here



# Define a HarmonicScattering3D object.
#S = HarmonicScattering3D(J, x.shape,rotation_covariant=rot)
S = HarmonicScattering3D(J, x.shape,rotation_covariant=rot)

# Calculate the scattering transform.
Sx = S.scattering(x)

np.savez_compressed("out.npz",q=Sx)



