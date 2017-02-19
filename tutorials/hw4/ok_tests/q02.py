test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> False not in np.isclose(linear_fit(x,y)[0],np.array([47.7249833]))
          True
          >>> False not in np.isclose(linear_fit(x,y)[1],np.array([2.57251848]))
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hw4 import *
      >>> x, y = load_data('data.txt')
      >>> import numpy as np
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
