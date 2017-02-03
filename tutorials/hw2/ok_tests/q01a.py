test = {
  'name': 'Question 1a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(vertical_profile) == np.ndarray
          True
          >>> len(vertical_profile) == 1024
          True
          >>> max(vertical_profile)==57502
          True
          >>> len(np.where(vertical_profile>10000)[0]) == 61
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
