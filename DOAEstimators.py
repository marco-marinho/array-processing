import numpy as np
import SteeringGenerator as stg
import AlgebraLibrary as alg


def conventional_beamformer(signal, resolution, separation = 1/2):

    angular_power = []
    angles = np.arange(-90, 90, resolution)
    elements = np.shape(signal)[0]
    R = alg.get_covariance(signal)

    for angle in angles:
        A = stg.generate_ula_vectors(angle, elements, separation)
        p = np.abs(np.matmul(np.matmul(A.conj().T, R),A))
        angular_power.append(np.squeeze(p))

    return angular_power, angles


def ESPRIT(signal, model_order, separation = 1/2):

    Qs, Qn = alg.get_subspaces(signal, model_order)
    phi = np.linalg.lstsq(Qs[0:-1, :], Qs[1:, :], rcond=None)[0]
    ESPRIT_doas = np.arcsin(-np.angle(np.linalg.eigvals(phi)) / (2 * np.pi * separation)) * 180 / np.pi

    return ESPRIT_doas
