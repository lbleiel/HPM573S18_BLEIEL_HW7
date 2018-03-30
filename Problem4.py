import CalibrationClasses as Cls

calibrated = Cls.Calibration()
calibrated.sample_posterior()

print('PROBLEM 4:')
print('The estimated annual mortality probability and the 95% credible interval is:', calibrated.get_mortality_estimate_credible_interval(alpha=.05, deci=4))



