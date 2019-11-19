graph [
  directed 1
  node [
    id 0
    label ")"
  ]
  node [
    id 1
    label "<if>"
  ]
  node [
    id 2
    label "<code_instructions>"
  ]
  node [
    id 3
    label "("
  ]
  node [
    id 4
    label "<conditional>"
  ]
  node [
    id 5
    label "{"
  ]
  node [
    id 6
    label "}"
  ]
  node [
    id 7
    label "<else>"
  ]
  node [
    id 8
    label "if"
  ]
  edge [
    source 0
    target 5
  ]
  edge [
    source 1
    target 8
  ]
  edge [
    source 2
    target 6
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 4
    target 0
  ]
  edge [
    source 5
    target 2
  ]
  edge [
    source 6
    target 7
  ]
  edge [
    source 8
    target 3
  ]
]
