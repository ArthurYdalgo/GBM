graph [
  directed 1
  node [
    id 0
    label "<id_token>"
  ]
  node [
    id 1
    label ")"
  ]
  node [
    id 2
    label "("
  ]
  node [
    id 3
    label "erase"
  ]
  node [
    id 4
    label "<erase>"
  ]
  node [
    id 5
    label ";"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 1
    target 5
  ]
  edge [
    source 2
    target 0
  ]
  edge [
    source 3
    target 2
  ]
  edge [
    source 4
    target 3
  ]
]
