test = {
  'name': 'Question 2',
  'points': 7,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sirius = Star(0.000117211,2.64)
          >>> sirius.distance == 2.64
          True
          >>> False not in np.isclose(sirius.luminosity,np.array([25.406384654191676]),rtol=1E-3)
          True
          >>> False not in np.isclose(sirius.mass, np.array([2.2451001415804406]),rtol=1E-3)
          True
          >>> False not in np.isclose(sirius.radius, np.array([1.6605107378314656]),rtol=1E-3)
          True
          >>> False not in np.isclose(sirius.temperature,np.array([10069.473128481242]),rtol=1E-3)
          True
          >>> False not in np.isclose(sirius.peak_wl,np.array([2879.991795993204]),rtol=1E-3)
          True
          >>> sirius.color == 'UV'
          True
          >>> False not in np.isclose(sirius.t_ms,np.array([1.324069271829432]),rtol=1E-3)
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
