# Terrain Class Friction Dataset

Data used for the paper "*These Maps Are Made For Walking: Real-Time Terrain Property Estimation for Mobile Robots*". Post-processed friction coefficients are included within the data/ folder on a per-class basis. Images for several classes have also been provided.


## Data

Data for eleven terrain classes has been provided within the data/ folder. Each folder contains one self-titled txt document which includes the post-processed coefficient of friction measurments. We built a device to measure the coefficient of friction using the pulling force measured using  a load cell and the known weight of the device. Measurements were post-processed using a high-pass filter to remove sensor noise from the load cell.

Included within several data class folders is an image showing the terrain over which the measurements were taken

## Probabilistic Model Fitting

The file model.py includes scripts to read the contents of each terrain class friction data file and fits a Gaussian, lognormal, gamma, T-student, and Weibull distribution to the data using the scipy stats library. These distibutions are then plotted over the histogram of data for comparison. Distribution parameters are output to the terminal along with the Kolmogorov-Smirnov test results for each distribution.

Note: The gamma and T-student distributions cannot be fit to the data for several class and thus are not plotted.