test = {
  'name': 'Question 1c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(flattened_spectrum_truncated) == np.ndarray
          True
          >>> flattened_spectrum_truncated[-1]== 9150.6153846153848
          True
          >>> np.std(flattened_spectrum_truncated) == 1636.1145431800715
          True
          >>> max(flattened_spectrum_truncated) == 15747.923076923076
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
