graph [
  directed 1
  node [
    id 0
    label "elif"
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
    label "<code_instructions>"
  ]
  node [
    id 4
    label "<else>"
  ]
  node [
    id 5
    label "<elif>"
  ]
  node [
    id 6
    label "<conditional>"
  ]
  node [
    id 7
    label "{"
  ]
  node [
    id 8
    label "}"
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 1
    target 7
  ]
  edge [
    source 2
    target 6
  ]
  edge [
    source 3
    target 8
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
  edge [
    source 8
    target 4
  ]
  edge [
    source 8
    target 5
  ]
]
