# GoogleTrends_Covid19

This project is from the manuscript "Building Longitudinal Google Trends to Measure Dynamic Local-Level Issue Attention" by Taeyong Park, Haewoon Kwak, and Jisun An. The manuscript is available at http://www.taeyongpark.com/uploads/1/1/6/6/116640555/longitudinalgoogletrends1.pdf 

CrossSection_comparison.py: This code is to collect DMA-level cross-sectional Google Trends indices for the CDC-CNN-Fox News comparison-search term for the period between February 1, 2020 and May 10, 2020.

TimeSeries_comparison.py: This code is to collect DMA-level time-series Google Trends indices for each of the CDC, CNN, and Fox News single-search term for the period between February 1, 2020 and May 10, 2020. Though this code generates 210 DMAs' CDC, CNN, and Fox News time-series, the manuscript only uses the CNN time-series for Atlanta as the reference for the rescaling method.

Rescale_comparison.ipynb: This Jupyter Notebook code is to rescale the cross-sectional CDC-CNN-Fox News comparison-search indices using the reference Atlanta time-series. This code corresponds to the second and third steps in the manuscript. 

dma_googleid.tsv: This text data file includes individual DMAs' Google ID. This file is called in the Python code where needed.
