from github_actions import mean


def test_mean():
    assert mean([1, 2, 3]) == 2
