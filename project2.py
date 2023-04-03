import PySimpleGUI as sg
import qrcode

layout = [
    [sg.Input(key="Text")],
    [sg.Button("Create")],
    [sg.Image(key="QR")],
]

# Create a window object
window = sg.Window("QR Code Generator", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Create":
        # Get the link from the input field
        text = values["Text"]
        # Create a QR code image
        img = qrcode.make(text)
        # Save the image as a file
        img.save("qr.png")
        # Update the image element with the file
        window["QR"].update(filename="qr.png")

# Close the window
window.close()
