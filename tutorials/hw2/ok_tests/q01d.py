test = {
  'name': 'Question 1d',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(continuum_subtracted_spectrum) == np.ndarray
          True
          >>> int(np.mean(continuum_subtracted_spectrum)) == -299
          True
          >>> np.min(continuum_subtracted_spectrum)== -4906.1684096271383
          True
          >>> max(continuum_subtracted_spectrum) == 1224.5225556461428
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
