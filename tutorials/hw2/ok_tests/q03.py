test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> quad_solve(2,3,4)==None
          True
          >>> quad_solve(4,5,1)==(-0.25, -1.0)
          True
          >>> quad_solve(2,5,2)==(-0.5, -2.0)
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
