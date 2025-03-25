from openmm.app import *
from openmm import *
from openmm.unit import *
import numpy as np
import time
import matplotlib.pyplot as plt

# Load the PDB file
pdb = PDBFile("../chignolin/1uao.pdb")

# Load force fields
forcefield = ForceField("amber14-all.xml", "amber14/tip3p.xml")

# Create modeller and apply modifications
modeller = Modeller(pdb.topology, pdb.positions)
modeller.addHydrogens(forcefield)
modeller.addSolvent(forcefield, model='tip3p', padding=1.0 * nanometer)

# Create the system from the solvated topology
system = forcefield.createSystem(modeller.topology,
                                 nonbondedMethod=PME,
                                 nonbondedCutoff=1.0 * nanometer,
                                 constraints=HBonds)

def benchmark(platform_name, properties=None, steps=5000):
    try:
        platform = Platform.getPlatformByName(platform_name)
        integrator = LangevinIntegrator(300 * kelvin, 1 / picosecond, 2 * femtosecond)
        simulation = Simulation(Topology(), system, integrator, platform, properties or {})
        simulation.context.setPositions(modeller.positions)
        LocalEnergyMinimizer.minimize(simulation.context, tolerance=1.0 * kilojoule_per_mole / nanometer, maxIterations=1000)
        simulation.context.setVelocitiesToTemperature(300 * kelvin)
        start = time.time()
        simulation.step(steps)
        end = time.time()
        rate = steps / (end - start)
        print(f"{platform_name} {properties if properties else ''}: {rate:.2f} steps/sec")
        return f"{platform_name} {properties if properties else ''}", rate
    except Exception as e:
        print(f"Error on {platform_name} {properties}: {e}")
        return f"{platform_name} {properties if properties else ''}", 0


configs = [
    ("CPU", {"Threads": "1"}),
    ("CPU", {"Threads": "4"}),
    ("CPU", {"Threads": "8"}),
    ("CUDA", {"DeviceIndex": "0", "Precision": "single"}),
    ("CUDA", {"DeviceIndex": "0,1", "Precision": "single"}),  # Multi-GPU (if available)
    ("OpenCL", {"DeviceIndex": "0", "Precision": "single"}),
]

results = [benchmark(name, props) for name, props in configs]

labels, speeds = zip(*results)

# Save labels and speeds to a text file
with open("results.txt", "w") as file:
    for label, speed in zip(labels, speeds):
        file.write(f"{label}: {speed:.2f} steps/sec\n")
