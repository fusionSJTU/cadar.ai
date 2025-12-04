Metrics Framework
===================

In the pursuit of next-generation autonomous systems, standardizing data is only the first step. To fully unlock the potential of FOOD's fusion-oriented architecture, we must also revolutionize how we evaluate performance.

Traditional metrics often treat perception output as deterministic points, discarding the rich uncertainty information (e.g., covariance, existence probability) inherent in multi-sensor fusion algorithms. This leads to an incomplete assessment of an agent's true capability.

Therefore, the FOOD metrics framework is designed to be Uncertainty-Aware. We prioritize metrics that can evaluate the full probabilistic output of fusion algorithms, ensuring that the confidence of the system is measured as rigorously as its accuracy.


P-GOSPA :ref:`[1] <pgospa_paper_ref>`
~~~~~~~~~~~~~~~~~~~

For multi-object tracking and fusion tasks within FOOD, we adopt Probabilistic GOSPA (P-GOSPA) as the primary performance metric. Unlike traditional metrics (such as OSPA or Hausdorff) or the standard GOSPA, which operate on deterministic sets, P-GOSPA extends evaluation into the space of Multi-Bernoulli (MB) densities.

This metric is particularly suitable for the FOOD platform because it accounts for the inherent uncertainty in fusion algorithms—capturing not just where an object is, but how confident the system is about its existence and state.

   .. _metrics_p_gospa_mb_density:
   .. figure:: figures/metrics_p_gospa_mb_density.png
        :align: center
        :width: 80%
        :alt: An exemplary scenario with two objects and two MB set densities. Each Bernoulli density has Gaussian single-object density, and its existence probability is shown next to its Gaussian mean. A desirable metric should be able to answer: 1) what is the distance between each MB density and ground truth object states? and 2) what is the distance between the two MB densities?

        Fig. 1: An exemplary scenario with two objects and two MB set densities. Each Bernoulli density has Gaussian single-object density, and its existence probability is shown next to its Gaussian mean. A desirable metric should be able to answer: 1) what is the distance between each MB density and ground truth object states? and 2) what is the distance between the two MB densities?

The Definition 
-----------------
  
We utilize the standard configuration of P-GOSPA (parameter :math:`\alpha = 2`). According to **Equation (8)** in the original paper, this configuration offers a mathematically rigorous definition that can be **exactly decomposed** into four interpretable components.

Let the ground truth set be :math:`f_X` and the estimated Multi-Bernoulli density be :math:`f_Y`. The metric is defined as:

.. math::

   d_p^{(c, 2)}\left(f_X, f_Y\right) = \left[\min_{\gamma \in \Gamma} \left( \underbrace{\sum_{(i, j) \in \gamma}\text{LocErr}(i,j)}_{\text{Localization}} + \underbrace{\sum_{(i, j) \in \gamma}\text{UncErr}(i,j)}_{\text{Uncertainty}} + \underbrace{\frac{c^p}{2}\sum_{i \notin \gamma} r_x^i}_{\text{Missed}} + \underbrace{\frac{c^p}{2}\sum_{j \notin \gamma} r_y^j}_{\text{False}}\right)\right]^{\frac{1}{p}}

This decomposition provides a **granular performance analysis** for algorithms, highlighting the **Soft Penalty** mechanism:

.. admonition:: Localization Error
   :class: no-icon

   .. math::

      \sum_{(i, j) \in \gamma} \min \left(r_x^i, r_y^j\right) d\left(p_x^i, p_y^j\right)^p

   Measures spatial accuracy. **Soft Penalty Feature:** The error is scaled by :math:`\min(r_x, r_y)`. A track with low existence probability contributes significantly less to the error than a high-confidence track, preventing weak detections from dominating the localization score.

.. admonition:: Existence Probability Mismatch
   :class: no-icon

   .. math::

      \sum_{(i, j) \in \gamma} \left|r_x^i - r_y^j\right| \frac{c^p}{2}

   **[Unique to P-GOSPA]** Penalizes the "probability discrepancy." If an object exists (:math:`r_x=1`) but the tracker is unsure (e.g., :math:`r_y=0.6`), a penalty proportional to the difference (:math:`0.4`) is applied.

.. admonition:: Missed Detection Error
   :class: no-icon

   .. math::

      \frac{c^p}{2} \sum_{i: \forall j,(i, j) \notin \gamma} r_x^i

   Cost for unassigned ground truth objects. The penalty is proportional to the target's existence probability.

.. admonition:: False Detection Error
   :class: no-icon

   .. math::

      \frac{c^p}{2} \sum_{j: \forall i,(i, j) \notin \gamma} r_y^j

   **[Key Soft Penalty]** Represents the cost for **false positives** (estimated tracks that do not correspond to any ground truth).
   
   * **Standard GOSPA (Hard Penalty):** A false positive is binary—either ignored (cost=0) or fully penalized (cost= :math:`c^p/2`) based on a cut-off threshold.
   * **P-GOSPA (Soft Penalty):** The penalty scales **linearly** with :math:`r_y`. A false positive with low existence probability (:math:`r=0.1`) incurs only 10% of the max penalty, while a high-confidence false positive (:math:`r=0.9`) incurs 90%. This encourages the filter to report potential objects without excessive punishment.

.. only:: html

   .. tip::
      
      For the full mathematical proofs and the derivation of Equation, please refer to `the original paper <https://fusion.sjtu.edu.cn/pub/paper/Probabilistic%20GOSPA.pdf>`_.
      
Why P-GOSPA?
------------

1. **Mathematically Well-Defined**: 
   P-GOSPA satisfies all properties of a metric (identity, symmetry, and triangle inequality). This ensures rigorous and consistent comparisons across different datasets and algorithms.

2. **Soft Penalties vs. Hard Thresholding**: 
   Standard metrics require "hard thresholding" (e.g., discarding tracks with existence probability :math:`r < 0.5`) before evaluation. This leads to information loss. 
   P-GOSPA evaluates the raw probabilistic output using **Soft Penalties**, where the cost is proportional to the confidence. This rewards algorithms that accurately model their uncertainty rather than making binary guesses.

3. **Smoothness**: 
   As a result of soft penalties, the metric is continuous. As shown in the heatmap below, the error transitions **smoothly** with changes in existence probability (:math:`r`) and variance (:math:`\sigma^2`), avoiding the abrupt jumps that are typical for deterministic metrics.

   .. figure:: figures/metrics_p_gospa_heatmap.png
        :align: center
        :width: 60%
        :alt: P-GOSPA Heatmap showing smoothness

        Fig. 2: P-GOSPA versus :math:`r` and :math:`\sigma^2`


Probabilistic Trajectory GOSPA :ref:`[2] <pgospa_paper_ref>`
~~~~~~~~~~~~~~~~~~~

The probabilistic trajectory GOSPA (PT-GOSPA) metric extends the P-GOSPA framework to evaluate entire object trajectories over time, rather than just individual time steps. This is crucial for assessing multi-object tracking algorithms that must maintain consistent object identities.

The PT-GOSPA metric incorporates temporal consistency by evaluating the alignment of estimated trajectories with ground truth trajectories, considering both spatial accuracy and uncertainty over time. This allows for a more comprehensive assessment of tracking performance, capturing not only instantaneous errors but also the ability to maintain accurate tracks across multiple frames.

   .. figure:: figures/TPGOSPA_example.png
      :align: center
      :width: 80%
      :alt: An exemplary scenario with a single ground truth trajectory and two sets of trajectory estimates, where each trajectory estimate is a sequence of Bernoulli densities. Each Bernoulli density has Gaussian single object density, and its existence probability is shown next to its Gaussian mean. The true trajectory and the trajectory estimate in blue exist at time step 1, 2 and 3. The set of trajectory estimates in orange consists of two single trajectory estimates, one exists only at time step 1, and the other exists at time step 2 and 3. A desirable metric should be able to answer: 1) what is the distance between each set of sequences of Bernoulli densities and the set of true trajectories? and 2) what is the distance between the two sets of sequences of Bernoulli densities?

      Fig. 3: An exemplary scenario with a single ground truth trajectory and two sets of trajectory estimates, where each trajectory estimate is a sequence of Bernoulli densities. Each Bernoulli density has Gaussian single object density, and its existence probability is shown next to its Gaussian mean. The true trajectory and the trajectory estimate in blue exist at time step 1, 2 and 3. The set of trajectory estimates in orange consists of two single trajectory estimates, one exists only at time step 1, and the other exists at time step 2 and 3. A desirable metric should be able to answer: 1) what is the distance between each set of sequences of Bernoulli densities and the set of true trajectories? and 2) what is the distance between the two sets of sequences of Bernoulli densities?

Similar to P-GOSPA, PT-GOSPA decomposes the overall error into five interpretable components, including localization error, uncertainty error, missed detection error, false detection error, and track switch error, all evaluated over entire trajectories. This decomposition allows for detailed performance analysis of tracking algorithms, highlighting their strengths and weaknesses in maintaining accurate and confident tracks over time.

.. only:: html

   .. tip::
      
      For more details on the mathematical formulation and properties of the PT-GOSPA metric, please refer to `the original paper <https://arxiv.org/pdf/2506.15148>`_.

