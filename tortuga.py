import sys
import turtle

HLINE = 32 * "+"


class tortuga:

    def __init__(self, config, alfabet):
        self.pensize = config["pensize"]
        self.width = config["width"]
        self.pencolor = config["pencolor"]
        self.heading = config["heading"]
        self.mdistance = config["mdistance"]
        self.mrotation = config["mrotation"]
        self.speed = config["speed"]
        self.hideturtle = bool(config["hideturtle"])

        self.memory = []
        self.translator = config["dictionary"]
        self.accions = {}

        print(f"{HLINE}\n"
              f"[DEBUG]: La configuracio de la tortuga es:\n"
              f"[DEBUG]: pensize: {self.pensize}\n"
              f"[DEBUG]: width: {self.width}\n"
              f"[DEBUG]: pencolor: {self.pencolor}\n"
              f"[DEBUG]: heading: {self.heading}\n"
              f"[DEBUG]: movement distance: {self.mdistance}\n"
              f"[DEBUG]: movement rotation: {self.mrotation}\n"
              f"[DEBUG]: speed: {self.speed}"
              f"[DEBUG]: hideturtle: {self.hideturtle}"
              f"[DEBUG]: translator table: {self.translator}"
              )

        turtle.pencolor(self.pencolor)
        turtle.width(self.width)
        turtle.setheading(self.heading)
        turtle.speed(self.speed)
        if self.hideturtle:
            turtle.hideturtle()

        for accio in alfabet:
            if accio in self.accions:
                print(f"[ERROR]: La accio `{accio}` ja té un moviment de la tortuga associat.\n"
                      f"[ERROR]: Moviment de `{accio}` associat es `{self.accions[accio]}`")
                sys.exit(-1)

            if self.translator[accio] == "linia":
                self.accions[accio] = self.tforward_draw
            elif self.translator[accio] == "nlinia":
                self.accions[accio] = self.tforward_ndraw
            elif self.translator[accio] == "rot+":
                self.accions[accio] = self.trotate_positive
            elif self.translator[accio] == "rot-":
                self.accions[accio] = self.trotate_negative
            elif self.translator[accio] == "recorda pos":
                self.accions[accio] = self.tremember_state
            elif self.translator[accio] == "restaura pos":
                self.accions[accio] = self.trestore_state
            else:
                print(f"[ERROR]: La accio `{accio}` no te un moviment de la tortuga associat.")
                sys.exit(-1)

        print(f"[DEBUG]: El diccionari d'accions de tortuga del L-System es:\n"
              f"[DEBUG]: {self.accions}\n"
              f"{HLINE}")

    """
    Accio personalitzada de la tortuga: avanca $distancia i dibuixa la linia.
    $distancia: integer o float
    """
    def tforward_draw(self):
        print(f"[DEBUG]: Movement with drawing of length {self.mdistance}")
        turtle.pendown()
        turtle.forward(self.mdistance)


    """
    Accio personalitzada de la tortuga: avanca $distancia sense dibuixar la linia
    $distancia: integer o float
    """
    def tforward_ndraw(self):
        print(f"[DEBUG]: Movement without drawing of length {self.mdistance}")
        turtle.penup()
        turtle.forward(self.mdistance)


    """
    Accio personalitzada de la tortuga: actualitza la direccio de 
    la tortuga $rotation graus positius
    $rotation: integer o float
    """
    def trotate_positive(self):
        print(f"[DEBUG]: Positive rotation of {self.mrotation} degrees")
        heading = turtle.heading()
        turtle.setheading(heading + self.mrotation)


    """
    Accio personalitzada de la tortuga: actualitza la direccio de 
    la tortuga $rotation graus negatius
    $rotation: integer o float
    """
    def trotate_negative(self):
        print(f"[DEBUG]: Negative rotation of {self.mrotation} degrees")
        heading = turtle.heading()
        turtle.setheading(heading - self.mrotation)

    """
    Accio personalitzada de la tortuga: guarda l'estat de la
    tortuga (direcció i posicio) al final de la llista $self.memory
    """
    def tremember_state(self):
        state = {"heading": turtle.heading(),
                 "position": turtle.position()
                 }
        print(f"[DEBUG]: Remembering turtle state (heading, pox, posy)"
              f"[DEBUG]: ({state['heading']}, {state['position'][0]}, {state['position'][1]})"
        )

        self.memory.append(state)

    """
    Accio personalitzada de la tortuga: restaura l'ultim estat de la
    tortuga (direcció i posicio) guardat en la llista $self.memory
    """
    def trestore_state(self):
        state = self.memory.pop()
        print(f"[DEBUG]: Restoring turtle's last state (heading, pox, posy)"
              f"[DEBUG]: ({state['heading']}, {state['position'][0]}, {state['position'][1]})"
        )

        turtle.penup()
        turtle.setposition(state["position"][0], state["position"][1])
        turtle.setheading(state["heading"])

    """
    Genera el dibuix del L-System a partir de $axioma
    $axioma: string
    """
    def draw_lindenmayer(self, axioma):
        for accio in axioma:
            self.accions[accio]()