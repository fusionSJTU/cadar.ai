Cloud Data Center
===================


System Architecture
~~~~~~~~~~~~~~~~~~~

The system is organized into three primary logical layers: the Control & Access Layer, the Core Data Services Layer, and the Infrastructure Layer. It facilitates a closed-loop workflow from vehicle-side data acquisition to cloud-side storage, management, and visualization.

1. Access Layer

    This layer serves as the system's center, orchestrating workflows between the cloud and the vehicle edge. It is embodied by the Smart Data Center (SDC) suite:

    * SDC Server: Acting as the central scheduler, it manages user requests via the API and Web interfaces. It coordinates data indexing instructions and dispatches tasks to edge devices.

    * SDC Remote: A specialized lightweight agent deployed on the vehicle. It bridges the gap between local hardware and the cloud. Unlike passive loggers, SDC Remote actively communicates with the server to execute command-and-control tasks, managing the local HDF5 Storage and uploading data.

2. Core Data Services Layer

    This layer implements the specialized logic for data management and retrieval. It consists of two distinct subsystems tailored for different data paradigms:

    A. Highly Scalable Data Service (HSDS) 
    
        HSDS is implemented as a microservice-based architecture designed to handle HDF5-formatted multidimensional data. It allows for high-concurrency access and efficient slicing of large datasets without full-file downloads.
    
    B. TSDB (Time-Series Data Management) 
        
        TSDB acts as the dedicated management and retrieval engine for high-frequency time-series data. It leverages TDengine as its core backend to provide efficient query interfaces and data ingestion capabilities.

        As the core Time Series Database, TDengine offers distinct advantages over traditional relational systems (e.g., MySQL), specifically tailored for autonomous system scenarios. It delivers superior write performance for massive concurrent data streams and achieves up to 90% storage reduction through columnar storage and specialized delta encoding. Furthermore, TDengine provides native support for complex time-window aggregation and downsampling—operations that are computationally expensive and inefficient to implement in standard SQL.
3. Infrastructure Layer

    This layer provides the fundamental persistence capability, decoupled from specific hardware implementations.

    Object Storage Service (OS): OS serves as the unified storage interface for the system. While currently implemented using MinIO (a high-performance, S3-compatible local storage cluster), the architecture is designed as a generic Data Object Storage Service. It communicates via the standard S3 protocol, allowing the underlying physical storage to be seamlessly switched between local clusters and public cloud providers (e.g., AWS S3) without affecting the upper-layer application logic.
    
----------------------------------------------------------------------------------------------------

.. autosummary::
   :toctree: generated

   Cloud Data Center