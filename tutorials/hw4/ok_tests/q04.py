test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
                    >>> False not in np.isclose(np.array([find_residuals(x,y)[1][i] for i in find_residuals(x,y)[1].keys()]),[-5.2935433814127465e-14,-48.030965403761797,44.770746614675517,19.093481326060257],rtol=1E-4) 
                    True
          	  >>> 'mean' in list(find_residuals(x,y)[1].keys())
          	  True 
          	  >>> 'min' in list(find_residuals(x,y)[1].keys())
          	  True
                    >>> 'max' in list(find_residuals(x,y)[1].keys())
          	  True
          	  >>> 'std' in list(find_residuals(x,y)[1].keys())
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
