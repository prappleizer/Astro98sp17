test = {
  'name': 'Question 1b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(row_slice) == np.ndarray
          True
          >>> np.std(row_slice) == 13394.459656850979
          True
          >>> row_slice[600]==48459
          True
          >>> max(row_slice) == 56971
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
