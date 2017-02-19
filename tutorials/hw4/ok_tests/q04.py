test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 'mean' in list(find_residuals(x,y)[1].keys())
          True
          >>> 'min' in list(find_residuals(x,y)[1].keys())
          True
          >>> 'max' in list(find_residuals(x,y)[1].keys())
          True
          >>> 'std' in list(find_residuals(x,y)[1].keys())
          True
          >>> False not in np.isclose(np.array(np.median(find_residuals(x,y)[0])),np.array([-0.92225898557427399]),rtol=1E-2)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hw4 import *
      >>> import numpy as np
      >>> x, y = load_data('data.txt')
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
