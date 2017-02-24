test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a,b,c = z_bins(metallicities)
          >>> False not in (a[0] == a1)
          True
          >>> False not in (b[0] == b1)
          True
          >>> False not in (c[0] == c1)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import numpy as np
      >>> a1 = np.loadtxt('ok_tests/a.txt')
      >>> b1 = np.loadtxt('ok_tests/b.txt')
      >>> c1 = np.loadtxt('ok_tests/c.txt')
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
