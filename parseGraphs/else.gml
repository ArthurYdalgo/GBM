graph [
  directed 1
  node [
    id 0
    label "{"
  ]
  node [
    id 1
    label "}"
  ]
  node [
    id 2
    label "<else>"
  ]
  node [
    id 3
    label "<code_instructions>"
  ]
  node [
    id 4
    label "else"
  ]
  edge [
    source 0
    target 3
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
    target 0
  ]
]
