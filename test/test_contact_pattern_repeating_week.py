from glowgreen import ContactPatternRepeating
from datetime import datetime
import numpy as np


def test_shift_weekly_pattern():
    """single contact Tues 12 PM
    admin at Wed 2 PM
    -> after shift, contact starts at 156 h
    """
    theta = [36]
    c = [1]
    d = [0.1]
    cpat = ContactPatternRepeating(theta, c, d, repeat="week")
    admin_datetime = datetime(year=2023, month=5, day=3, hour=14)
    cpat._shift_weekly_pattern(admin_datetime)
    assert np.array_equal(cpat.theta, np.array([156]))
    assert np.array_equal(cpat.c, np.array([1]))
    assert np.array_equal(cpat.d, np.array([0.1]))


def test_shift_weekly_pattern2():
    """contact Tues 12 PM and Thurs 12 PM
    admin at Wed 2 PM
    -> after shift, contacts start at 156 h and 36 h
    """
    theta = [36, 84]
    c = [1, 2]
    d = [0.1, 0.2]
    cpat = ContactPatternRepeating(theta, c, d, repeat="week")
    admin_datetime = datetime(year=2023, month=5, day=3, hour=14)
    cpat._shift_weekly_pattern(admin_datetime)
    assert np.array_equal(
        cpat.theta,
        np.array([156, 36, 37]),
    )
    assert np.array_equal(cpat.c, np.array([1, 1, 1]))
    assert np.array_equal(cpat.d, np.array([0.1, 0.2, 0.2]))
