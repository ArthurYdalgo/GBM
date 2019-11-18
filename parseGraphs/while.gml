graph [
  directed 1
  node [
    id 0
    label "<while>"
  ]
  node [
    id 1
    label "<literal_token>"
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
    label ")"
  ]
  node [
    id 5
    label "while"
  ]
  node [
    id 6
    label "<identifier>"
  ]
  node [
    id 7
    label "<conditional>"
  ]
  node [
    id 8
    label "<operation>"
  ]
  node [
    id 9
    label "{"
  ]
  node [
    id 10
    label "}"
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
    target 1
  ]
  edge [
    source 2
    target 8
  ]
  edge [
    source 2
    target 6
  ]
  edge [
    source 2
    target 7
  ]
  edge [
    source 3
    target 10
  ]
  edge [
    source 4
    target 9
  ]
  edge [
    source 5
    target 2
  ]
  edge [
    source 6
    target 4
  ]
  edge [
    source 7
    target 4
  ]
  edge [
    source 8
    target 4
  ]
  edge [
    source 9
    target 3
  ]
]
