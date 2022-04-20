import os
import math
import numpy as np
import scipy.stats as stats
from scipy.stats import norm
import matplotlib.pyplot as plt


def fitProbabilisticModelParams(filename):
	title= filename.split("/")
	title = title[1]

	mu = []
	with open(filename, 'r') as f:
		for line in f:
			mu.append(float(line.strip()))

	# Stuff for histogram
	mu = np.asarray(mu)
	w = 0.005

	full_range = True
	if full_range:
		n = math.ceil(1/w)
		x = np.linspace(0, 1, n)
	else:
		n = math.ceil((mu.max() - mu.min())/w)
		x = np.linspace(mu.min(), mu.max(), n)

	bins = np.linspace(0, 1, n)
	digitized = np.digitize(mu, bins)
	count = np.zeros((n,))
	for val in digitized:
		count[val] += 1
	density = count / (sum(count) * w)

	print("Model Parameters for ", title, " Class")

	# Fitting a Gaussian distribution
	mean,std = norm.fit(mu)
	y = norm.pdf(x, mean, std)
	print("Gaussian: ", mean, std)

	# Fitting a log-normal distribution
	lognormal = stats.lognorm.fit(mu, loc=0)
	lognormal_pdf = stats.lognorm.pdf(x, lognormal[0], loc=lognormal[1], scale=lognormal[2]) # fitted distribution
	print("Lognormal: ", lognormal)

	# Fit a generalized gamma distribution
	gamma = stats.gengamma.fit(mu)
	gamma_pdf = stats.gengamma.pdf(x, gamma[0], gamma[1], gamma[2], gamma[3])

	# Fit a t-Student distribution
	tstud = stats.t.fit(mu)
	tstud_pdf = stats.t.pdf(x, tstud[0], tstud[1], tstud[2])

	# Fit a t-Student distribution
	weibull = stats.weibull_min.fit(mu, loc=0)
	weibull_pdf = stats.weibull_min.pdf(x, weibull[0], weibull[1], weibull[2])
	print("Weibull: ", weibull, "\n")

	print("Kolmogorov-Smirnov Test for ", title, " Class")
	print("Normal Distribution: ", stats.kstest(x, 'norm', args=[mean, std]))
	print("Lognormal Distribution: ", stats.kstest(x, 'lognorm', args=[lognormal[0], lognormal[1], lognormal[2]]))
	# print("Gamma Distribution: ", stats.kstest(x, gamma_pdf))
	# print("T-Student Distribution: ", stats.kstest(x, tstud_pdf))
	print("Weibull Distribution: ", stats.kstest(x, 'weibull_min', args=[weibull[0], weibull[1], weibull[2]]))
	input()


	fig = plt.figure()
	plt.rcParams.update({'font.size': 30})
	ax = fig.add_subplot(111)
	plt.xlabel("Coefficient of Friction")
	plt.ylabel("Frequency")
	plt.title(title)
	ax.plot(x, y, color="#d95f02", linewidth=3, label="Gaussian Distribution")
	ax.plot(x, lognormal_pdf, color="#7570b3", linewidth=3, label="Lognormal Distribution")
	ax.plot(x, weibull_pdf, color='#e7298a', linewidth=3, label="Weibull Distribution")
	ax.hist(mu, bins=n, density=True,  color="#66a61e")
	ax.legend()
	# plt.yticks(np.arange(1,20,1), [i+1 if i in range(1,20,2) else '' for i in range(19) ])
	# plt.xlim([0.3,0.8])
	plt.show()

files = ['data/Concrete/concrete.txt',
		 'data/SoftRubber/soft_rubber.txt',
		 'data/Plywood/plywood.txt',
		 'data/Wood/wood.txt',
		 'data/Grass/grass.txt',
		 'data/Pebbles/pebbles.txt',
		 'data/Rocks/rocks.txt',
		 'data/HardRubber/hard_rubber.txt',
		 'data/Carpet/carpet.txt',
		 'data/Flooring/flooring.txt',
		 'data/Ice/ice.txt',
		 'data/Snow/snow.txt']


for file in files:
	fitProbabilisticModelParams(file)