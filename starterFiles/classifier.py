from taipy.gui import Gui

img_path= "logo.png"

index ="""
<|text-center|
<|{img_path}|image|>
>
"""
#img_path is the var specified

app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True)