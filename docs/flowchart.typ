#import "@preview/fletcher:0.5.8" as fletcher: diagram, node, edge

#let blob(pos, label, tint: white, ..args) = node(
	pos, align(center, label),
	width: 28mm,
	fill: tint.lighten(60%),
	stroke: 1pt + tint.darken(20%),
	corner-radius: 5pt,
	..args,
)

#diagram(spacing: 8pt,
  blob((0, 0), "Program Start"),
  edge("->"),
  blob((0, 1), "User Input"),
  edge("->"),
  blob((0, 2), "Input Sanitization"),
  edge("->"),
  blob((0, 3), "Main Logic"),
  edge("->"),
  blob((0, 4), "Output")
)
