from graph import *

# Лицо
penColor("Black")
brushColor("Yellow")
circle(250, 300, 150)

# Губы
brushColor("Black")
rectangle(180, 370, 320, 390)

# Глаза
brushColor("Red")
circle(180, 270, 25)
brushColor("Black")
circle(180, 270, 10)
brushColor("Red")
circle(320, 270, 20)
brushColor("Black")
circle(320, 270, 10)

# Брови
brushColor("Black")
polygon([(100, 217), (230, 260), (235, 250), (100, 217)])
brushColor("Black")
polygon([(380, 225), (280, 265), (275, 250), (380, 225)])

run()