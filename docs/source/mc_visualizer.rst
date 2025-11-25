SMART FOOD Visualizer
=======================

As one platform providing multi-sensor data, SMART FOOD has collected and integrated diverse sensor information. We developed the Minecraft Based Visualizer where each data fragment has a corresponding 3D sphere in the interactive 3D scene. Users can click on the sphere to view the data, which includes sensor information, timestamp, and other details. This visualizer allows users to explore and analyze the data in a more intuitive way.

   .. raw:: html

      <div style="text-align: center;">
         <video width="600" controls>
            <source src="_static/videos/mc_visualizer_1min.mp4" type="video/mp4">
            Your browser does not support the video tag.
         </video>
         <div style="text-align: center;">
         Fig. 01: The visualizer of FOOD
      </div>

After checking the fitness of data fragments and selecting the required data slices, we can get access to them by entering the download page directly.


Overview
----------

The software contains one overview part and four data introduction parts:

- FOOD Overview
- Perception Data
- Pre-Processing
- Metrics
- Tags

FOOD Overview
---------------

This panel contains an outline for the whole dataset, where it is easy to know the structure of the data. It offered six perspectives: Scene, Use Case, Environment, Sensor, Functionality, Fusion.

Perception Data
-----------------

This window is on the top left of the dashboard, which provides intuitive display for the point cloud data collected. It is easy to make a rough judgment about the suitability of the sample you select.

Pre-Processing
----------------

In this part, we provide several methods and algorithms (in development) to preprocess the data. It is a place where the effects of newest algorithms can be seen.

Metrics
---------
In addition to the results that you can directly observe, this part provides quantitative metrics for the difference between the algorithm results and the ground truth. Each algorithm provided above has corresponding metrics to evaluate its performance.

Tags
---------
We provide the structure view for the sample data you select. It shows the properties and metadata associated with each data fragment.
