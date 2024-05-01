from taipy.gui import Gui

img_path= "logo.png"
upld_img = " "

index = """
<|text-center|
<|{img_path}|image|>

Select an image from your file
<|{upld_img}|file_selector|>
>
"""
#img_path is the var specified

app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True)