test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> False not in (load_data('data.txt')[0] == np.arange(100))
          True
          >>> False not in np.isclose(load_data('data.txt')[1],[85.248294391492351, 39.224885823793365, 43.53867297588301, 34.216580899211102, 78.779345556345518, 12.556610277697871, 102.86241528349761, 50.981810250576274, 76.923148384439045, 67.088662852140203, 106.72774223387594, 32.794946603900911, 73.003546672906893, 74.166020503695378, 109.60279689867899, 63.632359499285528, 86.258307896155543, 73.450472331106226, 95.916038303728371, 110.14709013763334, 76.116563854479608, 127.34050450351963, 124.56451863686367, 118.40412715417054, 129.54857409903775, 97.663105455916977, 112.33328210624533, 97.193803276578208, 114.18682867211545, 134.00871362821863, 109.9909616875608, 118.8904484672253, 115.0883524074047, 114.15903757947778, 120.43395896084103, 137.22517820345985, 115.75436543461447, 147.5868206426309, 181.01770724328418, 163.60235828452818, 145.83716851375294, 133.23845147935904, 138.78666502560682, 194.2262648423021, 161.10252827863982, 148.67719446944503, 169.14286601728401, 213.07553646159087, 172.60744926885135, 185.893307480651, 181.51369594304145, 169.85617833109063, 155.20735510291956, 174.91926292364056, 180.46699513576732, 200.2297232486537, 208.20594008107676, 212.7049151642872, 201.19724495801742, 216.7075632646748, 183.62956468037262, 229.68723896856235, 216.13057710307078, 201.03138547827106, 220.60084377986368, 210.86009382744308, 239.55635770769595, 250.48002491636171, 267.42698632176962, 192.19602951990743, 193.6627304221779, 216.55309077406201, 233.47280440701792, 251.51286558822207, 241.84927835514284, 193.61823361661914, 233.35537292596433, 260.46704974457725, 249.99305575740712, 264.03564261277091, 245.1754793053552, 248.14354990421904, 259.04838218444576, 266.39812074441915, 264.30310392675091, 265.08248761402183, 250.44662838752805, 275.69313416316396, 272.64352158051418, 297.00980080168864, 301.01651799386269, 281.5178942594016, 271.85631658304453, 268.63955015824337, 294.18982748319127, 289.17827948316375, 282.53837524010765, 293.44605179330318, 281.5459816863256, 312.64729513936715])
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
