graph [
  directed 1
  node [
    id 0
    label "<while>"
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
    label "while"
  ]
  node [
    id 5
    label "<operation>"
  ]
  node [
    id 6
    label "{"
  ]
  node [
    id 7
    label "}"
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 1
    target 6
  ]
  edge [
    source 2
    target 5
  ]
  edge [
    source 3
    target 7
  ]
  edge [
    source 4
    target 2
  ]
  edge [
    source 5
    target 1
  ]
  edge [
    source 6
    target 3
  ]
]
