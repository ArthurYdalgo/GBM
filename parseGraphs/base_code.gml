graph [
  directed 1
  node [
    id 0
    label "var"
  ]
  node [
    id 1
    label "begin"
  ]
  node [
    id 2
    label "end"
  ]
  node [
    id 3
    label "<code_instruction>"
  ]
  node [
    id 4
    label "<variable_declaration>"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 3
    target 3
  ]
  edge [
    source 3
    target 2
  ]
  edge [
    source 4
    target 1
  ]
]
