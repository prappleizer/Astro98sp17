test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> fibonacci(5) == 5
          True
          >>> fibonacci(8) == 21
          True
          >>> fibonacci(21) == 10946
          True
          >>> fibonacci('cat') == None
          True
          >>> fibonacci(-5) == None
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
