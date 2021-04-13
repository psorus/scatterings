import numpy as np
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

# Define a HarmonicScattering3D object.
S = HarmonicScattering3D(J, (M, N, O),rotation_covariant=rot)

# Calculate the scattering transform.
Sx = S.scattering(x)

np.savez_compressed("out.npz",q=Sx)



