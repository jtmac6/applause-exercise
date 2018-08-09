from tester_matcher import match_testers


def test_no_input():
    country = []
    device = []
    expected = [(4, 'Taybin', 'Rutkin', 'US', 125),
                (7, 'Lucas', 'Lowry', 'JP', 117),
                (8, 'Sean', 'Wellington', 'JP', 116),
                (1, 'Miguel', 'Bautista', 'US', 114),
                (6, 'Stanley', 'Chen', 'GB', 110),
                (5, 'Mingquan', 'Zheng', 'JP', 109),
                (3, 'Leonard', 'Sutton', 'GB', 106),
                (9, 'Darshini', 'Thiagarajan', 'GB', 104),
                (2, 'Michael', 'Lubavin', 'US', 99)]
    results = match_testers(country, device)
    assert results == expected


def test_all_all():
    country = ["all"]
    device = ["all"]
    expected = [(4, 'Taybin', 'Rutkin', 'US', 125),
                (7, 'Lucas', 'Lowry', 'JP', 117),
                (8, 'Sean', 'Wellington', 'JP', 116),
                (1, 'Miguel', 'Bautista', 'US', 114),
                (6, 'Stanley', 'Chen', 'GB', 110),
                (5, 'Mingquan', 'Zheng', 'JP', 109),
                (3, 'Leonard', 'Sutton', 'GB', 106),
                (9, 'Darshini', 'Thiagarajan', 'GB', 104),
                (2, 'Michael', 'Lubavin', 'US', 99)]
    results = match_testers(country, device)
    assert results == expected


def test_all_countries_only():
    country = ["all"]
    device = []
    expected = [(4, 'Taybin', 'Rutkin', 'US', 125),
                (7, 'Lucas', 'Lowry', 'JP', 117),
                (8, 'Sean', 'Wellington', 'JP', 116),
                (1, 'Miguel', 'Bautista', 'US', 114),
                (6, 'Stanley', 'Chen', 'GB', 110),
                (5, 'Mingquan', 'Zheng', 'JP', 109),
                (3, 'Leonard', 'Sutton', 'GB', 106),
                (9, 'Darshini', 'Thiagarajan', 'GB', 104),
                (2, 'Michael', 'Lubavin', 'US', 99)]
    results = match_testers(country, device)
    assert results == expected


def test_all_devices_only():
    country = []
    device = ["all"]
    expected = [(4, 'Taybin', 'Rutkin', 'US', 125),
                (7, 'Lucas', 'Lowry', 'JP', 117),
                (8, 'Sean', 'Wellington', 'JP', 116),
                (1, 'Miguel', 'Bautista', 'US', 114),
                (6, 'Stanley', 'Chen', 'GB', 110),
                (5, 'Mingquan', 'Zheng', 'JP', 109),
                (3, 'Leonard', 'Sutton', 'GB', 106),
                (9, 'Darshini', 'Thiagarajan', 'GB', 104),
                (2, 'Michael', 'Lubavin', 'US', 99)]
    results = match_testers(country, device)
    assert results == expected


def test_one_valid_country_only():
    country = ["US"]
    device = []
    expected = [(4, 'Taybin', 'Rutkin', 'US', 125),
                (1, 'Miguel', 'Bautista', 'US', 114),
                (2, 'Michael', 'Lubavin', 'US', 99)]
    results = match_testers(country, device)
    assert results == expected


def test_one_valid_device_only():
    country = []
    device = ["iPhone 4"]
    expected = [(4, 'Taybin', 'Rutkin', 'US', 66), (8, 'Sean', 'Wellington', 'JP', 28),
                (1, 'Miguel', 'Bautista', 'US', 23), (5, 'Mingquan', 'Zheng', 'JP', 21)]
    results = match_testers(country, device)
    assert results == expected


def test_one_invalid_country_only():
    country = ["ZZ"]
    device = []
    expected = []
    results = match_testers(country, device)
    assert results == expected


def test_one_invalid_device_only():
    country = []
    device = ["Banana Phone"]
    expected = []
    results = match_testers(country, device)
    assert results == expected


def test_one_country_one_device():
    country = ["US"]
    device = ["iPhone 4"]
    expected = [(4, 'Taybin', 'Rutkin', 'US', 66), (1, 'Miguel', 'Bautista', 'US', 23)]
    results = match_testers(country, device)
    assert results == expected


def test_mult_country_mult_device():
    country = ["US", "JP"]
    device = ["Galaxy S3", "Galaxy S4"]
    expected = [(7, 'Lucas', 'Lowry', 'JP', 50),
                (2, 'Michael', 'Lubavin', 'US', 43),
                (5, 'Mingquan', 'Zheng', 'JP', 20)]
    results = match_testers(country, device)
    assert results == expected


def test_mult_country_only():
    country = ["US", "GB"]
    device = []
    expected = [(4, 'Taybin', 'Rutkin', 'US', 125),
                (1, 'Miguel', 'Bautista', 'US', 114),
                (6, 'Stanley', 'Chen', 'GB', 110),
                (3, 'Leonard', 'Sutton', 'GB', 106),
                (9, 'Darshini', 'Thiagarajan', 'GB', 104),
                (2, 'Michael', 'Lubavin', 'US', 99)]
    results = match_testers(country, device)
    assert results == expected


def test_mult_device_only():
    country = []
    device = ["Galaxy S3", "iPhone 5"]
    expected = [(6, 'Stanley', 'Chen', 'GB', 110),
                (3, 'Leonard', 'Sutton', 'GB', 60),
                (1, 'Miguel', 'Bautista', 'US', 30),
                (8, 'Sean', 'Wellington', 'JP', 30),
                (7, 'Lucas', 'Lowry', 'JP', 28),
                (2, 'Michael', 'Lubavin', 'US', 24)]
    results = match_testers(country, device)
    assert results == expected


def test_mult_all_country():
    country = ["all", "all"]
    device = []
    expected = [(4, 'Taybin', 'Rutkin', 'US', 125),
                (7, 'Lucas', 'Lowry', 'JP', 117),
                (8, 'Sean', 'Wellington', 'JP', 116),
                (1, 'Miguel', 'Bautista', 'US', 114),
                (6, 'Stanley', 'Chen', 'GB', 110),
                (5, 'Mingquan', 'Zheng', 'JP', 109),
                (3, 'Leonard', 'Sutton', 'GB', 106),
                (9, 'Darshini', 'Thiagarajan', 'GB', 104),
                (2, 'Michael', 'Lubavin', 'US', 99)]
    results = match_testers(country, device)
    assert results == expected


def test_mult_all_device():
    country = []
    device = ["all", "all"]
    expected = [(4, 'Taybin', 'Rutkin', 'US', 125),
                (7, 'Lucas', 'Lowry', 'JP', 117),
                (8, 'Sean', 'Wellington', 'JP', 116),
                (1, 'Miguel', 'Bautista', 'US', 114),
                (6, 'Stanley', 'Chen', 'GB', 110),
                (5, 'Mingquan', 'Zheng', 'JP', 109),
                (3, 'Leonard', 'Sutton', 'GB', 106),
                (9, 'Darshini', 'Thiagarajan', 'GB', 104),
                (2, 'Michael', 'Lubavin', 'US', 99)]
    results = match_testers(country, device)
    assert results == expected
