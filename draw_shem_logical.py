import schemdraw.elements as elm
import schemdraw
d = schemdraw.Drawing()
d+=elm.Ground()
d+=elm.Dot()
d+=elm.Line().right()
d+=elm.Battery().label("E_b 5.7 V").up
d+=elm.Resistor().label("R_B 100 K OHM").left
d+=elm.MeterA()
d+=elm.Dot()
d.push()
d+=elm.Line().right
d+=elm.Bjt()
d.pop()
d+=elm.Line().theta(-21).length(2)
d+=elm.MeterV().right().length(1.9)
d+=elm.Dot()
d.push()
d+=elm.Line().down().length(6)
d+=elm.Line().left()
d+=elm.Line().theta(132).length(1)
d.pop()
d+=elm.Line().down().length(2)
d+=elm.Dot()
d+=elm.Line().right()
d+=elm.MeterV().length(3.5)
d+=elm.Line().left()
d+=elm.Dot()
d+=elm.MeterA()
d+=elm.Battery().left().label("E_K").length(7)
d+=elm.Line().down().length(9.8)
d+=elm.Line().right().length(6)


d.draw()