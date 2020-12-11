# GoogleTrends_Covid19

This project is from the manuscript "Building Longitudinal Google Trends to Measure Dynamic Local-Level Issue Attention" by Taeyong Park, Haewoon Kwak, and Jisun An. The manuscript is available at http://www.taeyongpark.com/uploads/1/1/6/6/116640555/longitudinalgoogletrends1.pdf 

The code crawl_search_snapshots_combined.py is to collect DMA-level cross-sectional Google Trends indices for the CDC-CNN-Fox News comparison-search term for the period between February 1, 2020 and May 9, 2020. DMA refers to the Designated Market Area, a geographic area where people receive the same television station offerings in the United States.

The code crawl_search_over_time_dma.py is to collect DMA-level time-series Google Trends indices for the CDC-CNN-Fox News comparison-search term for the period between February 1, 2020 and May 9, 2020.

The code Recale-combined.ipynb is to rescale the cross-sectional CDC-CNN-Fox News comparison-search indices using the Atlanta time-series. This code is for the second and third steps in the manuscript.
