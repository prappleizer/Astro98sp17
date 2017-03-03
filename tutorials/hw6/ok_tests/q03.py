test = {
  'name': 'Question 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sirius1 = Star(0.000117211,2.64)
          >>> sirius1.mass_loss(0.05)
          >>> sirius2 = Star(0.000117211,2.64)
          >>> False not in np.isclose(sirius1.mass,np.array([2.1328451345014185]),rtol=1E-3)
          True
          >>> False not in np.isclose(sirius2.force(sirius1,3E18),np.array([1.39126142833511e+23]),rtol=1E-3)
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
