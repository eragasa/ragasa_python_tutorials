import ase.build
# author: Eugene J. Ragasa

""" 
some simple code for building simulation cells using ASE.

"""

def print_cell_information(obj_ase_cell):
    """ print the cell information of an ase cell 

    Args:
    obj_ase_cell: an ase crystal structure
    """
    # print the lattice vectors
    print('a1=',obj_ase_cell.cell[0,:])
    print('a2=',obj_ase_cell.cell[1,:])
    print('a3=',obj_ase_cell.cell[2,:])
    for i,a in enumerate(obj_ase_cell):
        print(i,a.symbol,a.position)


fcc_primitive = ase.build.bulk('Cu','fcc',a=3.6)
print('--- primitive cell ---')
print_cell_information(fcc_primitive)

fcc_ortho = ase.build.bulk('Cu','fcc',a=3.6,orthorhombic=True)
print('--- orthorhombic cell ---')
print_cell_information(fcc_ortho)

fcc_cubic = ase.build.bulk('Cu','fcc',a=3.6,cubic=True)
print('--- cubic cell ---')
print_cell_information(fcc_cubic)


