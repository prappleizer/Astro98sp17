test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> quad_solve(5,1,-5)==None
          True
          >>> quad_solve(1,5,7)==(1.140054944640259, -6.1400549446402586)
          True
          >>> quad_solve(3,9,12)==(1.0, -4.0)
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
