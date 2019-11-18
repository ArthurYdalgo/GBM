graph [
  directed 1
  node [
    id 0
    label ")"
  ]
  node [
    id 1
    label "<int>"
  ]
  node [
    id 2
    label "color"
  ]
  node [
    id 3
    label "("
  ]
  node [
    id 4
    label "<circle>"
  ]
  node [
    id 5
    label "<literal_token>"
  ]
  node [
    id 6
    label "radius"
  ]
  node [
    id 7
    label "circle"
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 2
    target 5
  ]
  edge [
    source 3
    target 6
  ]
  edge [
    source 4
    target 7
  ]
  edge [
    source 5
    target 0
  ]
  edge [
    source 6
    target 1
  ]
  edge [
    source 7
    target 3
  ]
]
