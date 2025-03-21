import PySimpleGUI as sg

layout=[[sg.Text("Input file name:"), sg.InputText(key="-NAME-")],
        [sg.Text("Input message:") ,
        sg.InputText(key="-IN-")],
        [sg.Text(key="-OUTPUT-")],
        [sg.Ok() , sg.Exit()]]

title = "Bang! - Just write a message"
window = sg.Window(title, layout)









while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    if event == "Ok":

        if values["-NAME-"] and values["-IN-"]:
                
                file = open(values["-NAME-"]+".txt","w+")
                file.write(values["-IN-"])
                file.close()
                
                sg.popup_ok("Message saved :)")

                print(values, event)

                break
        else:
             sg.popup_ok("You must enter the file name and message!")