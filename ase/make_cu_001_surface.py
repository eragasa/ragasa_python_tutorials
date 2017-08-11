import ase.build

""" We want to build an FCC structure with the 100 surface exposes in the z direction. """

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

# this is one way to do it
slab_symbol = 'Cu'
slab_lattice_parameter = 3.6
slab_supercell = (1,1,1)
slab_surface = [1,0,0]
slab_vacuum = 10
slab_is_orthogonal = True

fcc_100 = ase.build.fcc100(\
        symbol=slab_symbol,
        size=slab_supercell,
        vacuum = slab_vacuum,
        orthogonal = True)
print_cell_information(fcc_100)

#fcc_110 = ase.build.fcc110(\
#        symbol=slab_symbol,
#        size=slab_supercell,
#        vacuum=slab_vacuum,
#        orthogonal=slab_is_orthogonaal)
