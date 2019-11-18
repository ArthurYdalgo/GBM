graph [
  directed 1
  node [
    id 0
    label "LEAF"
  ]
  node [
    id 1
    label "<literal_token>"
  ]
  node [
    id 2
    label "<tree>"
  ]
  node [
    id 3
    label "TRUNK"
  ]
  node [
    id 4
    label "tree"
  ]
  node [
    id 5
    label ")"
  ]
  node [
    id 6
    label "("
  ]
  node [
    id 7
    label "<int>Y"
  ]
  node [
    id 8
    label "<int>X"
  ]
  node [
    id 9
    label "Y"
  ]
  node [
    id 10
    label "X"
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
    source 1
    target 0
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 3
    target 1
  ]
  edge [
    source 4
    target 6
  ]
  edge [
    source 6
    target 10
  ]
  edge [
    source 7
    target 3
  ]
  edge [
    source 8
    target 9
  ]
  edge [
    source 9
    target 7
  ]
  edge [
    source 10
    target 8
  ]
]
