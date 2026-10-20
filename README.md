# OsdagBridge-Desktop

Desktop Graphical User Interface (GUI), 3D CAD visualizer, and standalone installer package for [OsdagBridge](https://github.com/osdagbridge).

## Overview

`osdagbridge-desktop` provides the interactive graphical application for steel bridge analysis and design according to Indian Standard codes (IRC:5, IRC:6, IRC:22, IRC:24, IRC:112, IS 800).

It interfaces seamlessly with `osdagbridge-core`, which provides the underlying grillage analysis engine, finite element solvers (OpenSees), code validation checks, and LaTeX design report generators.

## Key Features

- **Interactive Bridge Modeler**: Intuitive docks and dialogs for bridge geometry, materials, support conditions, cross bracings, and vehicular load placement.
- **3D CAD Visualization**: Real-time 3D rendering of plate girder bridges, diaphragms, shear studs, and stiffeners powered by Open CASCADE (`pythonocc-core`).
- **Results & Plots**: Comprehensive 2D bending moment, shear force, deflection, and stress envelope diagrams (`matplotlib`).
- **Location Mapping**: Indian seismic and wind zone mapping using OpenStreetMap tile rendering.
- **Standalone Installer**: Fully packaged installer generation powered by Conda Constructor.

## Installation

### Via Conda

```bash
conda install -c gsrathore -c osdag -c geompy -c conda-forge osdagbridge-desktop
```

### Launching the Application

Once installed, simply run:

```bash
osdagbridge
```

## Development Setup

```bash
# Clone the repository
git clone https://github.com/osdagbridge/OsdagBridge-Desktop.git
cd OsdagBridge-Desktop

# Create and activate development environment
conda env create -f environment.yaml
conda activate osb-desktop

# Install in editable mode
pip install -e . --no-deps

# Run the app
osdagbridge
```

## Architecture

osdagbridge-desktop provides the osdagbridge_desktop graphical user interface and 3D visualization layer, consuming osdagbridge-core for computational analysis, design engines, and databases.

## License

GNU Lesser General Public License v3 or later (LGPLv3+).
