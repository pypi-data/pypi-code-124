"""
M3L6
====

"""

import numpy as np

from ...topology_graph import Edge
from ..cage import Cage
from ..vertices import LinearVertex, NonLinearVertex


class M3L6(Cage):
    """
    Represents a cage topology graph.

    Unoptimized construction

    .. moldoc::

        import moldoc.molecule as molecule
        import stk

        bb1 = stk.BuildingBlock(
            smiles='[Pd+2]',
            functional_groups=(
                stk.SingleAtom(stk.Pd(0, charge=2))
                for i in range(4)
            ),
            position_matrix=[[0, 0, 0]],
        )

        bb2 = stk.BuildingBlock(
            smiles=(
                'C1=NC=CC(C2=CC=CC(C3=C'
                'C=NC=C3)=C2)=C1'
            ),
            functional_groups=[
                stk.SmartsFunctionalGroupFactory(
                    smarts='[#6]~[#7X2]~[#6]',
                    bonders=(1, ),
                    deleters=(),
                ),
            ],
        )

        cage = stk.ConstructedMolecule(
            topology_graph=stk.cage.M3L6(
                building_blocks=(bb1, bb2),
            ),
        )

        moldoc_display_molecule = molecule.Molecule(
            atoms=(
                molecule.Atom(
                    atomic_number=atom.get_atomic_number(),
                    position=position,
                ) for atom, position in zip(
                    cage.get_atoms(),
                    cage.get_position_matrix(),
                )
            ),
            bonds=(
                molecule.Bond(
                    atom1_id=bond.get_atom1().get_id(),
                    atom2_id=bond.get_atom2().get_id(),
                    order=(
                        1
                        if bond.get_order() == 9
                        else bond.get_order()
                    ),
                ) for bond in cage.get_bonds()
            ),
        )

    :class:`.MCHammer` optimized construction

    .. moldoc::

        import moldoc.molecule as molecule
        import stk

        bb1 = stk.BuildingBlock(
            smiles='[Pd+2]',
            functional_groups=(
                stk.SingleAtom(stk.Pd(0, charge=2))
                for i in range(4)
            ),
            position_matrix=[[0, 0, 0]],
        )

        bb2 = stk.BuildingBlock(
            smiles=(
                'C1=NC=CC(C2=CC=CC(C3=C'
                'C=NC=C3)=C2)=C1'
            ),
            functional_groups=[
                stk.SmartsFunctionalGroupFactory(
                    smarts='[#6]~[#7X2]~[#6]',
                    bonders=(1, ),
                    deleters=(),
                ),
            ],
        )

        cage = stk.ConstructedMolecule(
            topology_graph=stk.cage.M3L6(
                building_blocks=(bb1, bb2),
                optimizer=stk.MCHammer(),
            ),
        )

        moldoc_display_molecule = molecule.Molecule(
            atoms=(
                molecule.Atom(
                    atomic_number=atom.get_atomic_number(),
                    position=position,
                ) for atom, position in zip(
                    cage.get_atoms(),
                    cage.get_position_matrix(),
                )
            ),
            bonds=(
                molecule.Bond(
                    atom1_id=bond.get_atom1().get_id(),
                    atom2_id=bond.get_atom2().get_id(),
                    order=(
                        1
                        if bond.get_order() == 9
                        else bond.get_order()
                    ),
                ) for bond in cage.get_bonds()
            ),
        )

    Metal building blocks with four functional groups are
    required for this topology.

    Ligand building blocks with two functional groups are required for
    this topology.

    When using a :class:`dict` for the `building_blocks` parameter,
    as in :ref:`cage-topology-graph-examples`:
    *Multi-Building Block Cage Construction*, a
    :class:`.BuildingBlock`, with the following number of functional
    groups, needs to be assigned to each of the following vertex ids:

        | 4-functional groups: 0 to 2
        | 2-functional groups: 3 to 8

    See :class:`.Cage` for more details and examples.

    """

    _R, _theta = 1, 0

    _vertex_prototypes = (
        NonLinearVertex(
            id=0,
            position=[_R*np.cos(_theta), _R*np.sin(_theta), 0]
        ),
        NonLinearVertex(
            id=1,
            position=[
                _R*np.cos(_theta+(4*np.pi/3)),
                _R*np.sin(_theta+(4*np.pi/3)),
                0
            ]
        ),
        NonLinearVertex(
            id=2,
            position=[
                _R*np.cos(_theta+(2*np.pi/3)),
                _R*np.sin(_theta+(2*np.pi/3)),
                0
            ]
        ),

        LinearVertex(
            id=3,
            position=[
                _R*np.cos((_theta+np.pi/4)),
                _R*np.sin((_theta+np.pi/4)),
                0.5
            ],
            use_neighbor_placement=False
        ),
        LinearVertex(
            id=4,
            position=[
                _R*np.cos((_theta+1*np.pi/3)),
                _R*np.sin((_theta+1*np.pi/3)),
                -0.5
            ],
            use_neighbor_placement=False
        ),

        LinearVertex(
            id=5,
            position=[
                _R*np.cos((_theta+1*np.pi/3)+(4*np.pi/3)),
                _R*np.sin((_theta+1*np.pi/3)+(4*np.pi/3)),
                0.5
            ],
            use_neighbor_placement=False
        ),
        LinearVertex(
            id=6,
            position=[
                _R*np.cos((_theta+1*np.pi/3)+(4*np.pi/3)),
                _R*np.sin((_theta+1*np.pi/3)+(4*np.pi/3)),
                -0.5
            ],
            use_neighbor_placement=False
        ),

        LinearVertex(
            id=7,
            position=[
                _R*np.cos((_theta+1*np.pi/3)+(2*np.pi/3)),
                _R*np.sin((_theta+1*np.pi/3)+(2*np.pi/3)),
                0.5
            ],
            use_neighbor_placement=False
        ),
        LinearVertex(
            id=8,
            position=[
                _R*np.cos((_theta+1*np.pi/3)+(2*np.pi/3)),
                _R*np.sin((_theta+1*np.pi/3)+(2*np.pi/3)),
                -0.5
            ],
            use_neighbor_placement=False
        ),
    )

    _edge_prototypes = (
        Edge(0, _vertex_prototypes[0], _vertex_prototypes[3]),
        Edge(1, _vertex_prototypes[0], _vertex_prototypes[4]),
        Edge(2, _vertex_prototypes[0], _vertex_prototypes[5]),
        Edge(3, _vertex_prototypes[0], _vertex_prototypes[6]),

        Edge(4, _vertex_prototypes[1], _vertex_prototypes[5]),
        Edge(5, _vertex_prototypes[1], _vertex_prototypes[6]),
        Edge(6, _vertex_prototypes[1], _vertex_prototypes[7]),
        Edge(7, _vertex_prototypes[1], _vertex_prototypes[8]),

        Edge(8, _vertex_prototypes[2], _vertex_prototypes[3]),
        Edge(9, _vertex_prototypes[2], _vertex_prototypes[4]),
        Edge(10, _vertex_prototypes[2], _vertex_prototypes[7]),
        Edge(11, _vertex_prototypes[2], _vertex_prototypes[8]),
    )

    _num_windows = 2
    _num_window_types = 1
