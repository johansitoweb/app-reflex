#chatapp
import reflex as rx

def index()-> rx.component:
    return rx.container(
        rx.box(
            "what is  reflex",
            #the user s question is on the right,
            text_alig="right",
        ),
        rx.box(

            "Away to build web app in pure python",
            # the answer is on the ceft,
            text_align="left",
        ),
    )
#Add state and page to the app.
app= rx.App()
app.add_page(index)
app.compile() 