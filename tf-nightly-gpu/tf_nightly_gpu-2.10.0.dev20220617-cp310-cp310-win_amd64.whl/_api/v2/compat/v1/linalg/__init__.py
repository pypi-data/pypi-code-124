# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Operations for linear algebra.
"""

import sys as _sys

from . import experimental
from tensorflow.python.ops.array_ops import matrix_diag as diag
from tensorflow.python.ops.array_ops import matrix_diag_part as diag_part
from tensorflow.python.ops.array_ops import matrix_set_diag as set_diag
from tensorflow.python.ops.array_ops import matrix_transpose
from tensorflow.python.ops.array_ops import matrix_transpose as transpose
from tensorflow.python.ops.array_ops import tensor_diag_part
from tensorflow.python.ops.clip_ops import global_norm
from tensorflow.python.ops.gen_array_ops import diag as tensor_diag
from tensorflow.python.ops.gen_array_ops import matrix_band_part as band_part
from tensorflow.python.ops.gen_linalg_ops import cholesky
from tensorflow.python.ops.gen_linalg_ops import log_matrix_determinant as slogdet
from tensorflow.python.ops.gen_linalg_ops import lu
from tensorflow.python.ops.gen_linalg_ops import matrix_determinant as det
from tensorflow.python.ops.gen_linalg_ops import matrix_inverse as inv
from tensorflow.python.ops.gen_linalg_ops import matrix_logarithm as logm
from tensorflow.python.ops.gen_linalg_ops import matrix_solve as solve
from tensorflow.python.ops.gen_linalg_ops import matrix_square_root as sqrtm
from tensorflow.python.ops.gen_linalg_ops import qr
from tensorflow.python.ops.gen_math_ops import cross
from tensorflow.python.ops.linalg.linalg_impl import adjoint
from tensorflow.python.ops.linalg.linalg_impl import eigh_tridiagonal
from tensorflow.python.ops.linalg.linalg_impl import logdet
from tensorflow.python.ops.linalg.linalg_impl import lu_matrix_inverse
from tensorflow.python.ops.linalg.linalg_impl import lu_reconstruct
from tensorflow.python.ops.linalg.linalg_impl import lu_solve
from tensorflow.python.ops.linalg.linalg_impl import matrix_exponential as expm
from tensorflow.python.ops.linalg.linalg_impl import matrix_rank
from tensorflow.python.ops.linalg.linalg_impl import pinv
from tensorflow.python.ops.linalg.linalg_impl import tridiagonal_matmul
from tensorflow.python.ops.linalg.linalg_impl import tridiagonal_solve
from tensorflow.python.ops.linalg.linear_operator import LinearOperator
from tensorflow.python.ops.linalg.linear_operator_adjoint import LinearOperatorAdjoint
from tensorflow.python.ops.linalg.linear_operator_block_diag import LinearOperatorBlockDiag
from tensorflow.python.ops.linalg.linear_operator_block_lower_triangular import LinearOperatorBlockLowerTriangular
from tensorflow.python.ops.linalg.linear_operator_circulant import LinearOperatorCirculant
from tensorflow.python.ops.linalg.linear_operator_circulant import LinearOperatorCirculant2D
from tensorflow.python.ops.linalg.linear_operator_circulant import LinearOperatorCirculant3D
from tensorflow.python.ops.linalg.linear_operator_composition import LinearOperatorComposition
from tensorflow.python.ops.linalg.linear_operator_diag import LinearOperatorDiag
from tensorflow.python.ops.linalg.linear_operator_full_matrix import LinearOperatorFullMatrix
from tensorflow.python.ops.linalg.linear_operator_householder import LinearOperatorHouseholder
from tensorflow.python.ops.linalg.linear_operator_identity import LinearOperatorIdentity
from tensorflow.python.ops.linalg.linear_operator_identity import LinearOperatorScaledIdentity
from tensorflow.python.ops.linalg.linear_operator_inversion import LinearOperatorInversion
from tensorflow.python.ops.linalg.linear_operator_kronecker import LinearOperatorKronecker
from tensorflow.python.ops.linalg.linear_operator_low_rank_update import LinearOperatorLowRankUpdate
from tensorflow.python.ops.linalg.linear_operator_lower_triangular import LinearOperatorLowerTriangular
from tensorflow.python.ops.linalg.linear_operator_permutation import LinearOperatorPermutation
from tensorflow.python.ops.linalg.linear_operator_toeplitz import LinearOperatorToeplitz
from tensorflow.python.ops.linalg.linear_operator_tridiag import LinearOperatorTridiag
from tensorflow.python.ops.linalg.linear_operator_zeros import LinearOperatorZeros
from tensorflow.python.ops.linalg_ops import cholesky_solve
from tensorflow.python.ops.linalg_ops import eye
from tensorflow.python.ops.linalg_ops import matrix_solve_ls as lstsq
from tensorflow.python.ops.linalg_ops import matrix_triangular_solve as triangular_solve
from tensorflow.python.ops.linalg_ops import norm
from tensorflow.python.ops.linalg_ops import self_adjoint_eig as eigh
from tensorflow.python.ops.linalg_ops import self_adjoint_eigvals as eigvalsh
from tensorflow.python.ops.linalg_ops import svd
from tensorflow.python.ops.math_ops import matmul
from tensorflow.python.ops.math_ops import matvec
from tensorflow.python.ops.math_ops import tensordot
from tensorflow.python.ops.math_ops import trace
from tensorflow.python.ops.nn_impl import l2_normalize
from tensorflow.python.ops.nn_impl import normalize
from tensorflow.python.ops.special_math_ops import einsum