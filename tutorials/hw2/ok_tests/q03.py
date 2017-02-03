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
          >>> quad_solve(2,5,1)==(3.0, -5.5)
          True
          >>> quad_solve(1,5,2)==(6.0, -11.0)
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
