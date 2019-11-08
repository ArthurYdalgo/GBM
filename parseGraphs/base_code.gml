graph [
  directed 1
  node [
    id 0
    label "<base_code>"
  ]
  node [
    id 1
    label "end"
  ]
  node [
    id 2
    label "<variable_declaration>"
  ]
  node [
    id 3
    label "<code_instruction>"
  ]
  node [
    id 4
    label "begin"
  ]
  node [
    id 5
    label "var"
  ]
  edge [
    source 0
    target 5
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 3
    target 3
  ]
  edge [
    source 3
    target 1
  ]
  edge [
    source 4
    target 3
  ]
  edge [
    source 5
    target 4
  ]
  edge [
    source 5
    target 2
  ]
]
