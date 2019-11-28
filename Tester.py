import SignalGenerator as sig
import matplotlib.pyplot as plt
import SteeringGenerator as str
import DOAEstimators as est
import numpy as np
import AlgebraLibrary as alg
import GeometryLibrary as geo

# A = str.generate_ula_vectors([-45, 60], 8, 1/2)
# S = sig.gen_signal(2, 100, 15)
#
# X = np.matmul(A, S)

# angular_power, angles = est.conventional_beamformer(X, 2, 1/2)
#
# plt.plot(angles, angular_power)
# plt.show()

#positions = np.array([[-0.25, 0.25], [-0.25, 0],  [-0.25, -0.25], [-0.125, 0.125], [-0.125, -0.125], [0, 0.25], [0, 0], [0, -0.25], [0.125, 0.125], [0.125, -0.125], [0.25, 0.25], [0.25, 0], [0.25, -0.25]])*4
#A = str.generate_sparse_vectors([-45, 60], positions, 0.125)
A = str.generate_ula_vectors([60, 15], 15, 1/2)
S = sig.gen_signal(2, 100)

u = str.generate_polarization_steering([60, 15], 2)

# angular_power, angles = est.conventional_beamformer_sparse(X, 0.1, positions, 0.125)
# plt.plot(angles, angular_power)
# plt.show()



Z = str.merge_space_polarization_steering(A, u)
X = np.matmul(Z, S)
DOAS = est.ESPRIT_Polarization(X, 2, 1/2)
print(DOAS)
#
#
# plt.plot(angles, angular_power)
# plt.show()

#
# s = sig.generate_OFDM_signal(16000, 32, [0.3, -0.5, 0, 1, 0.2, -0.3], 5, 15, True, True)