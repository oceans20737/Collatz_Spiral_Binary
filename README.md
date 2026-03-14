[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19021509.svg)](https://doi.org/10.5281/zenodo.19021509)

Title:
Revealing the Modular Structure of Collatz Trajectories through Binary Logarithmic Spiral Plots
A Topological Analysis of 4m+1 Magazines and a·2ᵇ Launchers
Author: Hiroshi Harada
Date: March 15, 2026
License: MIT License

Overview
This repository contains the visualization code and research materials for the study:
“Revealing the Modular Structure of Collatz Trajectories through Binary Logarithmic Spiral Plots:
A Topological Analysis of 4m+1 Magazines and a·2ᵇ Launchers.”
The project introduces a geometric visualization method for Collatz trajectories using a base‑2 logarithmic spiral coordinate system.
Odd-number sequences of the form 4m+1 are treated as magazines, and even-number sequences of the form a·2ᵇ are treated as glide launchers.
These structures appear as angular lanes on the spiral plane, allowing Collatz transitions to be tracked visually.
The visualization highlights how trajectories move through:
    - Heating Odd Numbers (4k+3)
    - Cooling Odd Numbers (4k+1)
    - Glide Launchers (a·2ᵇ)
This reveals a modular and deterministic structure underlying the Collatz dynamics.

Files Included
- Collatz_Spiral_Binary_Title.pdf
- Collatz_Spiral_Binary_Report_EN.pdf
- Collatz_Spiral_Binary_Report_JP.pdf
    Research report describing the theoretical framework and analysis (English/Japanese).
- collatz_spiral_binary.py
    Python script for generating the Log₂ Collatz Spiral visualization.
    Includes:
    - Collatz trajectory generator
    - 4m+1 magazine detection
    - a·2ᵇ launcher plotting
    - Auto‑tracking radar visualization
- README.txt
- LICENSE.txt
    MIT License

How to Run
- Install Python 3.x
- Install required libraries:
    numpy, matplotlib
- Run the script:
    python collatz_spiral_binary.py
- The visualization image will be saved as:
    collatz_log2_radar_<n>.png

Keywords
Collatz conjecture, Logarithmic spiral, Dynamical systems, Topology, Binary representation, Visualization

License
This report is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0).
The accompanying source code is released under the MIT License.
© 2026 Hiroshi Harada

