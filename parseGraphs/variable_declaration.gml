graph [
  directed 1
  node [
    id 0
    label "<id_token>"
  ]
  node [
    id 1
    label "string"
  ]
  node [
    id 2
    label "<variable_declaration>"
  ]
  node [
    id 3
    label "int"
  ]
  node [
    id 4
    label "float"
  ]
  node [
    id 5
    label ","
  ]
  node [
    id 6
    label "bool"
  ]
  node [
    id 7
    label ";"
  ]
  edge [
    source 0
    target 7
  ]
  edge [
    source 0
    target 5
  ]
  edge [
    source 1
    target 0
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 2
    target 6
  ]
  edge [
    source 2
    target 1
  ]
  edge [
    source 3
    target 0
  ]
  edge [
    source 4
    target 0
  ]
  edge [
    source 5
    target 0
  ]
  edge [
    source 6
    target 0
  ]
]
