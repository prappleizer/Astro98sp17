test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> False not in np.isclose(sfrtxt,sfrs,rtol=1E-4)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import numpy as np
      >>> sfrtxt = np.loadtxt('ok_tests/sfrs.txt')
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
