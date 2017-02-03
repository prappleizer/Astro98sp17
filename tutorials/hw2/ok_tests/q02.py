test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> string_splosion('Code') == 'CCoCodCode'
          True
          >>> string_splosion('fade') == 'ffafadfade'
          True
          >>> string_splosion('Kitten') == 'KKiKitKittKitteKitten'
          True
          >>> string_splosion('data!') == 'ddadatdatadata!'
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
