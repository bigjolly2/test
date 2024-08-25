from nicegui import ui

label = ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: label.set_text(label.text + '!'))

ui.run()
