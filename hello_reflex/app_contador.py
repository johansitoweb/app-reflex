import reflex as rx

class State(rx.state):
    count: int = 0
    def increment(self):
       self .count+=1 
        
    def decrement(self):
       self .count-=1

def index():
    return rx.hstack(
        rx.hstack(
        rx.button(
            "Descrement",
            color_scheme="red",
            border_radius="1em",
            on_click= State.decrement
        ),
        rx.heading( State.count,font_size="2em"),
        rx.button(
            "Increment",
            color_scheme="green",
            border_radius="1em",
            on_click= State.increment
        ),
    )
    )

aap = rx.App()
app.add_page(index) 
app.compile()