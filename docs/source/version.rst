Version History
===============

.. note::
   **Versioning Policy:**
   
   - Versions ending in odd numbers (e.g., v0.01, v1.03) indicate **Development/Unstable** releases, focusing on new features and pipeline testing.
   - Versions ending in even numbers (e.g., v0.02, v1.02) indicate **Stable** releases, representing validated milestones.



**v2.01** (Current Version)
---------------------------
:Date: November 2025
:Status: **Unstable / Development**
:Focus: Smart Data Center & Visualization

Refinement of the "FOOD" ecosystem infrastructure and initial release of the visualization tools.

- **Smart Data Center**: Completed the core development of the Smart Data Center (initiated in May 2025)
- **Visualization**: Deployed the MC Visualizer (Nov 14, 2025) for high-fidelity data replay and analysis.
- **Milestone**: System demonstrated at the CSIF Workshop at SJTU (Nov 16, 2025)

**v1.03**
---------
:Date: October 2025
:Status: **Unstable / Design**
:Focus: Use Case Definition



- Preliminary design and definition of high-level autonomous driving use cases.
- Finalized requirements for the transition from raw data collection to "Smart" data processing.


**v1.02**
---------
:Date: July 2024
:Status: **Stable Release**
:Focus: On-road Validation

Successful execution of real-world operational tests on the SJTU campus.

- **Data Collection**: Verified intersection selection and collection significance.
- **Stability**: Confirmed system stability over long-duration and high-temperature operation tests (July 28, 2024).
- **Safety**: Standardized safety protocols for human operators during data collection.

**v1.01**
---------
:Date: July 2024
:Status: **Unstable / Integration**
:Focus: Vehicle Assembly

Hardware integration and physical platform construction.

- **Assembly**: Completed the mechanical and electrical integration of Lidar, Camera, and radar (July 22, 2024).

**v0.03**
---------
:Date: Spring 2024
:Status: **Unstable / Debugging**
:Focus: Off-board Sensor Calibration

Pre-installation phase focusing on sensor subsystems.

- **Indoor Debugging**: Completed offline debugging of sensor streams before vehicle integration.
- **Calibration**: Verified intrinsic parameters and data interfaces in a controlled lab environment.



**v0.02**
---------
:Date: December 2023
:Status: **Stable Release**
:Focus: Cloud Center V1 & System Optimization

First stable release of the cloud data processing backend.

- **Integration**: Finalized complex configuration modules for vehicle and sensor setups.
- **UI/UX**: Optimized the 3D visualization platform interface.

**v0.01**
---------
:Date: October - November 2023
:Status: **Unstable / MVP**
:Focus: Pipeline & Hardware Connectivity

Initial proof-of-concept and architecture deployment.

- **Pipeline**: Established the end-to-end data loop: *Board Collection -> Server Storage -> Frontend Visualization*.
- **Architecture**: Designed the RawData structure and deployed NAS/GitLab infrastructure.
- **Connectivity**: Validated hardware interfaces for Camera and LiDAR point clouds using web-based rendering.