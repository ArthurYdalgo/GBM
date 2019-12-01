graph [
  directed 1
  node [
    id 0
    label "<id_token>"
  ]
  node [
    id 1
    label "<literal_token>"
  ]
  node [
    id 2
    label "<attribution>"
  ]
  node [
    id 3
    label "<operation>"
  ]
  node [
    id 4
    label ";"
  ]
  node [
    id 5
    label "="
  ]
  node [
    id 6
    label "<sketchType_token>"
  ]
  edge [
    source 0
    target 5
  ]
  edge [
    source 1
    target 4
  ]
  edge [
    source 2
    target 0
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 5
    target 3
  ]
  edge [
    source 5
    target 1
  ]
  edge [
    source 5
    target 6
  ]
  edge [
    source 6
    target 4
  ]
]
