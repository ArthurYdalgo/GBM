graph [
  directed 1
  node [
    id 0
    label "canvas"
  ]
  node [
    id 1
    label "<id_token>"
  ]
  node [
    id 2
    label "string"
  ]
  node [
    id 3
    label "<variable_declaration>"
  ]
  node [
    id 4
    label "int"
  ]
  node [
    id 5
    label "float"
  ]
  node [
    id 6
    label ","
  ]
  node [
    id 7
    label "bool"
  ]
  node [
    id 8
    label ";"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 1
    target 8
  ]
  edge [
    source 1
    target 6
  ]
  edge [
    source 2
    target 1
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 3
    target 0
  ]
  edge [
    source 3
    target 5
  ]
  edge [
    source 3
    target 7
  ]
  edge [
    source 3
    target 2
  ]
  edge [
    source 4
    target 1
  ]
  edge [
    source 5
    target 1
  ]
  edge [
    source 6
    target 1
  ]
  edge [
    source 7
    target 1
  ]
]
