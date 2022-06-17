# Copyright 2021 qclib project.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
qclib auxiliary functions
"""

from qiskit import execute, transpile
from qiskit.providers.aer.backends import AerSimulator
import numpy as np
from scipy import sparse


def get_counts(circ):
    """
    Parameters
    ----------
    circ: QuantumCircuit (with measurement operations)

    Returns
    -------
    counts: output generated by the quantum circuit
    """
    backend = AerSimulator()
    counts = execute(circ, backend).result().get_counts()
    return counts


def get_state(circ):
    """
    Parameters
    ----------
    circ: QuantumCircuit

    Returns
    -------
    state_vector: state generated by the quantum circuit
    """

    backend = AerSimulator()
    tcirc = transpile(circ, backend)
    tcirc.save_statevector()
    state_vector = backend.run(tcirc).result().get_statevector()

    return np.array(state_vector)


def replace_all_values_with(new_value, dataset):
    """
        Given a list of tuples (v, b),where v is the value
        and b is the binary pattern associated to it.
        this procedure performs the task of replacing
        v with the new_value
    :param new_value: Value to replate the v in all the tuples
                      (v, b)
    :param dataset: List of tuples where the values are to be
                    replaced
    :return: new list of tuples
    """

    new_dataset = []
    for _, binary_pattern in dataset:
        new_dataset.append((new_value, binary_pattern))

    return new_dataset


def build_list_of_quibit_objects(quantum_register):
    """
        Buid a list of Qubit objects to be used as
        input to some procedure of the qiskit framework
    :param quantum_register: Quantum register with the qubits
    :return: Qubits list
    """
    qubits_list = []

    for i in range(quantum_register.size):
        qubits_list.append(quantum_register[quantum_register.size - i - 1])

    return qubits_list


def verify_interval_in_state_vector(statevector, start, finish):
    """
        Verifies if there is at least one non zero entry in
        a given interval in the state vectors cells, and
        returns true if positive
    :param statevector: state vector to be processed
    :param start: start of the interval
    :param finish: end of the interval
    :return: Boolean True if a non zero entry has been found
    """
    found = False
    for cell_idx in range(start, finish):

        cell_value = statevector[cell_idx]
        if cell_value != 0:
            found = True
            break
    return found


def verify_trigonometric_interval(value):
    """
        Verify if a certain value is inside the interval
        of the domain of the tirgonometric functions
        cosine and sine, [-1, 1]
    :param value: Real value to be evaluated
    :return: Value, if the value is inside the domain
             Updated value, if the value is outside the
             domain
    """

    value = min(value, 1)
    if value < -1:
        value = -1
    return value


def _count_ones(pattern):
    return pattern[0].count(1)


def random_sparse(nbits, density):
    '''
    Creates a random input for sparse quantum state preparation
    nbits: int number of qubits
    density: float in [0,1]

    returns
    bin_data: [(binary_string_k, float_k)] k = 0 ... n
    '''

    data = sparse.random(2 ** nbits, 1, density, format="dok")

    rows, _ = data.nonzero()
    bin_data = []

    length = sparse.linalg.norm(data)

    for k in rows:
        bin_data.append((format(k, "0" + str(nbits) + "b"), data[k, 0] / length))

    bin_data.sort(key=_count_ones)
    return bin_data

def _double_sparse_binary(nbits, log_size, p_1, p_0):

    bin_data = []
    while len(bin_data)< 2**log_size:
        lst = np.random.choice(2, nbits, p=[p_1, p_0]).tolist()

        if lst not in bin_data:
            bin_data.append(lst)

    return  bin_data


def double_sparse(nbits, log_size, p_1):
    """
    Parameters
    ----------
    nbits (int): number of qubits
    log_size (int): log_2(number of amplitudes)
    p_1 (float): probability of qubit equal to one

    Returns
    -------
    \\sum_{k} x_k |p_k>, each bit of p_k is equal to 1 with probability p1
    """
    data = np.random.rand(2 ** log_size) + np.random.rand(2 ** log_size)*1j
    length = np.linalg.norm(data)
    data = (1/length) * data

    binary = _double_sparse_binary(nbits, log_size, 1 - p_1, p_1)
    bin_data = [(binary[i], data[i]) for i in range(2 ** log_size)]

    bin_data.sort(key=_count_ones)
    return bin_data


def _compute_matrix_angles(feature, norm):
    """
        Compute the angles of the matrix U3 necessary for encoding
        the phase of the state
    :param feature: Complex or float, feature to be stored
    :param norm: remaining norm to be used to compute the angles
    :return: the angles alpha, beta and phi of the operator U3
    """
    alpha = 0
    beta = 0
    phi = 0

    if isinstance(feature, complex):
        phase = np.abs(np.power(feature, 2))

        if (norm - phase) < 0:
            norm = phase

        cos_value = np.sqrt((norm - phase) / norm)
        cos_value = verify_trigonometric_interval(cos_value)
        alpha = 2 * (np.arccos(cos_value))
        beta = np.arccos(- feature.real / np.sqrt(np.abs(np.power(feature, 2))))

        if feature.imag < 0:
            beta = 2 * np.pi - beta

        phi = - beta

    else:
        sin_value = - feature / np.sqrt(norm)
        sin_value = verify_trigonometric_interval(sin_value)
        alpha = 2 * (np.arcsin(sin_value))

    return alpha, beta, phi

def build_state_dict(state):
    """
    Builds a dict of the non zero amplitudes with their
    associated binary strings as follows:
      { '000': <value>, ... , '111': <value> }
    Args:
      state: The classical description of the state vector
    """
    n_qubits = np.ceil(np.log(len(state))).astype(int)
    state_dict = {}
    for (value_idx, value) in enumerate(state):
        if value != 0:
            binary_string = '{:0{}b}'.format(value_idx, n_qubits)[::-1]
            state_dict[binary_string] = value
    return state_dict
