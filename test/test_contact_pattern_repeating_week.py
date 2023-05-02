from glowgreen import ContactPatternRepeating
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
