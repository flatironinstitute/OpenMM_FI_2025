# 🧬 OpenMM Hackathon 2025

Welcome to the OpenMM Hackathon! This guide walks you through installing OpenMM via both **conda** (recommended in general) and **pip with CUDA support** (recommended for today!).

---

## Installation with `conda` (Recommended)

OpenMM is a high-performance toolkit for molecular simulation. The easiest and most reliable way to install it is using **conda**.

### Works on:
- Windows
- macOS
- Linux

### Prerequisites:
- [Anaconda](https://www.anaconda.com) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Installation
```bash
conda create -n openmm-env
conda activate openmm-env
conda install -c conda-forge openmm
```

### Test your installation:
```bash
python -c "import openmm; print(openmm.version.version)"
```

---

## 🚀 Installation with CUDA Support (works on rusty)


###  Notes:
- Use `pip` in a `venv`
- Optional: `matplotlib`, `seaborn` for plotting
- Optional: Patch OpenMM for Martini support

### ⚙️ Installation:
```bash
module load modules/2.3-20240529 python/3.11.7
python -m venv ~/openmm-env
source ~/openmm-env/bin/activate
module load cuda/12.3.2
pip install openmm[cuda12]
```

### Test your installation:
```bash
python -m openmm.testInstallation
```

### Install openmmtools:
```bash
pip install git+https://github.com/jharrymoore/openmmtools.git@development
pip install pyyaml
pip install git+https://github.com/choderalab/mpiplus.git
pip install pymbar
pip install numba
```


### ⚙️ Optional: for plotting-
```bash
pip install matplotlib seaborn
```

### ⚙️ Optional: Martini patch for OpenMM-
```bash
git clone https://github.com/maccallumlab/martini_openmm.git
cd martini_openmm/
python setup.py install
```

---

## 📚 References

-  [OpenMM Documentation](http://docs.openmm.org)
-  [OpenMM GitHub Repository](https://github.com/openmm/openmm)
