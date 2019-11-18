graph [
  directed 1
  node [
    id 0
    label ")"
  ]
  node [
    id 1
    label "("
  ]
  node [
    id 2
    label "<conditional>"
  ]
  node [
    id 3
    label "else"
  ]
  node [
    id 4
    label "<code_instructions>"
  ]
  node [
    id 5
    label "<else>"
  ]
  node [
    id 6
    label "<if>"
  ]
  node [
    id 7
    label "{"
  ]
  node [
    id 8
    label "}"
  ]
  node [
    id 9
    label "if"
  ]
  edge [
    source 0
    target 7
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 2
    target 0
  ]
  edge [
    source 3
    target 1
  ]
  edge [
    source 4
    target 8
  ]
  edge [
    source 5
    target 3
  ]
  edge [
    source 6
    target 3
  ]
  edge [
    source 7
    target 4
  ]
  edge [
    source 9
    target 6
  ]
]
