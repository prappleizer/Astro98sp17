test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> False not in np.isclose(restrictions,res,rtol=1E-4)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import numpy as np
      >>> res = np.loadtxt('ok_tests/res.txt')
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
