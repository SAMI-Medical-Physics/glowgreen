import numpy as np
from glowgreen import Clearance_1m


def test_at_timedelta_exp():
	dose_rate_xm_init = 80.
	effective_half_life = 11.
	measurement_distance = 2.
	n_half_lives = 1.3

	dose_rate_1m_init = dose_rate_xm_init * measurement_distance**1.5
	val_hand = dose_rate_1m_init * (1/2) ** (n_half_lives)

	model = 'exponential'
	model_params = [dose_rate_xm_init, effective_half_life]
	cfit = Clearance_1m(model, model_params, measurement_distance)
	hrs = n_half_lives * effective_half_life
	val_code = cfit.at_timedelta(hrs)

	assert val_code == val_hand


def test_at_timedelta_biexp():
	dose_rate_xm_init = 50.
	fraction_1 = 0.4
	half_life_1 = 11.
	half_life_2 = 20.
	measurement_distance = 2.
	hrs = 42.1

	dose_rate_1m_init = dose_rate_xm_init * measurement_distance**1.5
	val_hand = dose_rate_1m_init * ((fraction_1 * (1/2) ** (hrs / half_life_1)) + ((1-fraction_1) * (1/2) ** (hrs / half_life_2)))

	model = 'biexponential'
	model_params = [dose_rate_xm_init, fraction_1, half_life_1, half_life_2]
	cfit = Clearance_1m(model, model_params, measurement_distance)
	val_code = cfit.at_timedelta(hrs)

	assert np.isclose(val_code, val_hand)


def test_at_timedelta_activity_exp():
	a0 = 3e3
	n_half_lives = 1.3

	val_hand = a0 * (1/2) ** (n_half_lives)

	dose_rate_xm_init = np.nan
	effective_half_life = 11.
	measurement_distance = 3.
	model = 'exponential'
	model_params = [dose_rate_xm_init, effective_half_life]
	measurement_distance = 3.
	cfit = Clearance_1m(model, model_params, measurement_distance)
	hrs = n_half_lives * effective_half_life 
	val_code = cfit.at_timedelta(hrs, init=a0)

	assert val_code == val_hand


def test_at_timedelta_activity_biexp():
	a0 = 3e3
	fraction_1 = 0.4
	half_life_1 = 11.
	half_life_2 = 20.
	hrs = 42.1

	val_hand = a0 * ((fraction_1 * (1/2) ** (hrs / half_life_1)) + ((1-fraction_1) * (1/2) ** (hrs / half_life_2)))

	dose_rate_xm_init = np.nan
	model = 'biexponential'
	model_params = [dose_rate_xm_init, fraction_1, half_life_1, half_life_2]
	measurement_distance = 3.
	cfit = Clearance_1m(model, model_params, measurement_distance)
	val_code = cfit.at_timedelta(hrs, init=a0)

	assert np.isclose(val_code, val_hand)


def test_get_timedelta_exp():
	dose_rate_xm_init = 80.
	effective_half_life = 11.
	measurement_distance = 2.

	dose_rate_1m_init = dose_rate_xm_init * measurement_distance**1.5
	hrs_hand = effective_half_life * np.log(dose_rate_1m_init/25.) / np.log(2)

	model = 'exponential'
	model_params = [dose_rate_xm_init, effective_half_life]
	cfit = Clearance_1m(model, model_params, measurement_distance)
	hrs_code = cfit.get_timedelta(25.)
	
	assert hrs_code == hrs_hand


def test_get_timedelta_biexp():
	# fake biexp
	dose_rate_xm_init = 50.
	fraction_1 = 1.
	half_life_1 = 11.
	half_life_2 = 20.
	measurement_distance = 2.

	dose_rate_1m_init = dose_rate_xm_init * measurement_distance**1.5
	hrs_hand = half_life_1 * np.log(dose_rate_1m_init/25.) / np.log(2)

	model = 'biexponential'
	model_params = [dose_rate_xm_init, fraction_1, half_life_1, half_life_2]
	cfit = Clearance_1m(model, model_params, measurement_distance)
	hrs_code = cfit.get_timedelta(25.)
	
	assert np.isclose(hrs_code, hrs_hand)

	model_params = [dose_rate_xm_init, 0., half_life_2, half_life_1]
	cfit = Clearance_1m(model, model_params, measurement_distance)
	hrs_code = cfit.get_timedelta(25.)
	
	assert np.isclose(hrs_code, hrs_hand)


def test_get_timedelta_activity_exp():
	a0 = 3e3
	activity_limit_for_discharge = 5e2
	effective_half_life = 11.

	hrs_hand = effective_half_life * np.log(a0/activity_limit_for_discharge) / np.log(2)

	dose_rate_xm_init = np.nan
	measurement_distance = 3.
	model = 'exponential'
	model_params = [dose_rate_xm_init, effective_half_life]
	cfit = Clearance_1m(model, model_params, measurement_distance)
	hrs_code = cfit.get_timedelta(activity_limit_for_discharge, init=a0)

	assert hrs_code == hrs_hand


def test_get_timedelta_activity_biexp():
	# fake biexp
	a0 = 3e3
	activity_limit_for_discharge = 5e2
	fraction_1 = 1.
	half_life_1 = 11.
	half_life_2 = 20.

	hrs_hand = half_life_1 * np.log(a0/activity_limit_for_discharge) / np.log(2)

	dose_rate_xm_init = np.nan
	measurement_distance = 3.
	model = 'biexponential'
	model_params = [dose_rate_xm_init, fraction_1, half_life_1, half_life_2]
	cfit = Clearance_1m(model, model_params, measurement_distance)
	hrs_code = cfit.get_timedelta(activity_limit_for_discharge, init=a0)

	model_params = [dose_rate_xm_init, 0., half_life_2, half_life_1]
	cfit = Clearance_1m(model, model_params, measurement_distance)
	hrs_code = cfit.get_timedelta(activity_limit_for_discharge, init=a0)

	assert np.isclose(hrs_code, hrs_hand)


def test_residence_time_exp():
	model = 'exponential'
	dose_rate_xm_init = 80.
	effective_half_life = 11.
	model_params = [dose_rate_xm_init, effective_half_life]
	measurement_distance = 2.
	cfit = Clearance_1m(model, model_params, measurement_distance)
	
	assert cfit.residence_time() == effective_half_life / np.log(2)


def test_residence_time_biexp1():
	# fake biexp
	model = 'biexponential'
	dose_rate_xm_init = 80.
	fraction_1 = 1.
	half_life_1 = 11.
	half_life_2 = 20.
	model_params = [dose_rate_xm_init, fraction_1, half_life_1, half_life_2]
	measurement_distance = 2.
	cfit = Clearance_1m(model, model_params, measurement_distance)
	
	assert cfit.residence_time() == half_life_1 / np.log(2)


def test_residence_time_biexp2():
	model = 'biexponential'
	dose_rate_xm_init = 80.
	fraction_1 = 0.3
	half_life_1 = 11.
	half_life_2 = 30.
	model_params = [dose_rate_xm_init, fraction_1, half_life_1, half_life_2]
	measurement_distance = 2.
	cfit = Clearance_1m(model, model_params, measurement_distance)
	
	assert cfit.residence_time() == (fraction_1*half_life_1 + (1.-fraction_1)*half_life_2) / np.log(2)