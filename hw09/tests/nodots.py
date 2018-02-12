test = {
  'name': 'nodots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (nodots '(1 . 2))
          (1 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '(1 2 . 3))
          (1 2 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '((1 . 2) 3))
          ((1 2) 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '(1 (2 3 . 4) . 3))
          (1 (2 3 4) 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '(1 . ((2 3 . 4) . 3)))
          539ce7c99587b5a410f10ca8bd7e3fab
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw09)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
