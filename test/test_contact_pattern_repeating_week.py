from glowgreen import ContactPatternRepeating, Clearance_1m
from datetime import datetime
import numpy as np


def test_shift_weekly_pattern():
    """Test with single contact.

    + single contact Tues 12 PM
    + admin at Wed 2 PM
    + -> after shift, contact starts at 156 h
    """
    theta = [36]
    c = [1]
    d = [0.1]
    cpat = ContactPatternRepeating(theta, c, d, repeat="week")
    admin_datetime = datetime(year=2023, month=5, day=3, hour=14)
    theta_shift = cpat._shift_weekly_pattern(admin_datetime)
    assert np.array_equal(theta_shift, np.array([156]))


def test_shift_weekly_pattern2():
    """Test with 2 contact elements, second gets split into 2.

    + contact Tues 12 PM and Thurs 12 PM
    + admin at Wed 2 PM
    + -> after shift, contacts start at 156 h and 36 h
    """
    theta = [36, 84]
    c = [1, 2]
    d = [0.1, 0.2]
    cpat = ContactPatternRepeating(theta, c, d, repeat="week")
    admin_datetime = datetime(year=2023, month=5, day=3, hour=14)
    theta_shift = cpat._shift_weekly_pattern(admin_datetime)
    assert np.array_equal(
        theta_shift,
        np.array([156, 36, 37]),
    )


def test_get_dose_weekly_daily():
    """Since we already test that get_dose() works for diurnal patterns,
    make a weekly pattern the same as a daily pattern.
    """
    theta_day = np.array([5, 13])
    c_day = np.array([2, 3.5])
    d_day = [0.3, 1.5]
    cpat_day = ContactPatternRepeating(theta_day, c_day, d_day, repeat="day")

    theta_week = np.array(
        [5 + 24 * n for n in np.linspace(0, 6, num=7)]
        + [13 + 24 * n for n in np.linspace(0, 6, num=7)]
    )
    theta_week.sort()
    c_week = [2, 3.5] * 7
    d_week = [0.3, 1.5] * 7
    cpat_week = ContactPatternRepeating(theta_week, c_week, d_week, repeat="week")

    datetime_admin = datetime(year=2021, month=10, day=25, hour=10, minute=15)

    # exp clearance
    dose_rate_init_1m = 50  # uSv/h
    effective_half_life = 40  # h
    tau = 51  # h
    cfit_exp = Clearance_1m(
        "exponential", [dose_rate_init_1m, effective_half_life], 1.0
    )

    dose_day = cpat_day.get_dose(cfit_exp, tau, datetime_admin)
    dose_week = cpat_week.get_dose(cfit_exp, tau, datetime_admin)
    assert np.allclose(dose_day, dose_week)

    # biexp clearance
    dose_rate_init_1m = 90  # uSv/h
    fraction1 = 0.3
    half_life1 = 5  # h
    half_life2 = 50  # h
    tau = 51  # h
    cfit_biexp = Clearance_1m(
        "biexponential", [dose_rate_init_1m, fraction1, half_life1, half_life2], 1.0
    )

    dose_day = cpat_day.get_dose(cfit_biexp, tau, datetime_admin)
    dose_week = cpat_week.get_dose(cfit_biexp, tau, datetime_admin)
    assert np.allclose(dose_day, dose_week)
