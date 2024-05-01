from taipy.gui import Gui

img_path= "logo.png"
upld_img = " "
stat_img = "placeholder_image.png"

index = """
<|text-center|
<|{img_path}|image|>

Select an image from your file
<|{upld_img}|file_selector|>

<|{stat_img}|image|>
>
"""
#img_path is the var specified
#also it can be <|{"logo.png"}|image|> no need of var declaration at the top

app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True)