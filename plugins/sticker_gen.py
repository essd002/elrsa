
import pickle
print(1024**2)

class sticker:
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern

kawai = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢔⣦⣶⣿⣿⣿⣿⡷⠖⠒⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠉⠁⠂⠀⠀⢀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠶⣦⡤⣄⠀⠀⠀⠀⠀⠀⣠⠖⢩⣶⣿⣿⣿⣿⣿⠟⢉⣠⠔⠊⠁⠀⠀⠀⣀⣄⠀⠀⠉⠑⢦⣠⣤⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣌⡧⡾⠀⠀⠀⠀⡠⠊⢁⣴⣿⣿⣿⣿⣿⢟⣠⡾⠟⠁⠀⣀⣤⣶⠞⣫⠟⠁⠀⢀⠄⠀⢀⠙⢿⣿⣿⣷⣄
⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣠⣾⣶⣶⣿⣿⣿⣿⣿⣿⣷⡿⠋⣀⣤⣶⣿⣿⣋⣴⡞⠁⠀⠀⣠⠊⠀⠀⢸⡄⢨⣿⣿⣿⣿
⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠿⠿⢻⣿⣿⣿⣿⣿⣿⠿⠛⢉⣴⣿⢿⣿⠏⠀⠀⠀⡴⠃⣰⢀⠀⢸⣿⣤⣏⢻⣿⣿
⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⢀⣾⡿⣿⡿⠁⠀⢀⣾⣿⣿⣿⡿⠋⠁⠀⣠⣿⠟⢡⣿⡟⠀⢀⣤⣾⠁⣼⣿⢸⡇⢸⣿⣿⣿⡈⣿⣿
⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⢀⣾⠋⣼⣿⠁⢀⠀⣼⣿⣿⠟⠁⠀⠀⠀⣰⡿⠋⢠⣿⡿⠁⢠⣾⣿⡏⢀⣿⣿⣾⣿⢸⣿⣿⣿⡇⢹⣿
⠀⠀⠀⢰⡶⣤⣤⣄⠀⠀⠀⡼⠁⣼⣿⣿⣾⣿⣰⣿⠟⠁⠀⠀⠀⠀⢠⡿⠁⠀⣾⣿⠃⢠⣿⢿⡿⠁⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿
⠀⠀⠀⠘⣧⣈⣷⡟⠀⠀⣰⠁⡼⢻⣿⣿⣿⣿⡿⠋⠀⠀⠂⠒⠒⠒⣾⠋⠀⢠⣿⡏⢠⣿⢃⡿⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿
⠀⠀⠀⠀⠈⠉⠁⠀⠀⢠⠇⣰⠁⠸⣹⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠐⡇⠀⠀⢸⣿⢃⣿⠋⣿⡀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣰⠃⡀⢀⣿⣿⡏⢘⣶⣶⣶⣷⣒⣄⠀⠀⠀⠀⠀⠸⣿⣾⠃⠰⠁⠙⢦⡀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⢠⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⢁⠞⢁⣾⣿⣿⣷⠟⠁⣠⣾⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⠀⠀⠙⢦⡀⠀⢿⣿⣿⣿⣿⣿⣿⣸⠃
⠀⠀⠀⠀⠀⠀⠀⣠⣾⡖⠁⣠⣾⣿⣿⣿⡏⠀⢰⠿⢿⣿⣯⣼⠁⠀⠀⠀⠀⠀⠹⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⢬⣿⣿⡘⣿⣿⣏⣿⠀
⠀⠀⠀⠀⠀⣠⣾⢟⠋⣠⣾⣿⡿⠋⢿⣿⠀⠀⢼⠀⠀⢀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣷⣴⣆⡀⠀⠀⠈⢿⣧⠸⣿⣿⣿⣿
⠀⠀⢀⡤⠞⢋⣴⣯⣾⡿⠟⠋⠀⠀⢸⣿⡆⠀⠸⡀⠉⢉⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣶⣆⠀⠈⢿⣧⠹⣿⣿⣿
⠀⠀⠀⣸⣶⣿⣿⠟⠋⠀⠀⠀⠀⣴⡎⠈⠻⡀⠈⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠿⠛⠛⠻⣿⣬⡏⠻⣷⡀⠈⢻⣿⣿⣿⣿
⢂⣠⣴⣿⡿⢋⣼⣿⣿⣿⣿⣿⠋⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⡄⠀⠀⢀⡾⣿⠁⠀⢹⡇⠀⢠⣿⣿⣿⣿
⣿⣿⣽⣯⣴⣿⣿⠿⡿⠟⠛⢻⡤⠚⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠈⠉⢉⡴⠃⠀⠀⢸⠇⢠⣿⣿⣿⣿⣿
⣿⡇⣿⠿⣯⡀⠀⠀⠈⣦⡴⠋⠀⠀⢀⠨⠓⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠷⠒⠋⠀⠀⠀⠀⠃⣴⣿⠿⣡⣿⠏⠀
⠁⠀⠃⠀⠈⠳⣤⠴⡻⠋⠀⢀⡠⠊⠁⠀⠀⢀⡽⢄⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⠏⣺⠟⠁⠀⠀
⠀⠀⠀⠀⠀⡰⠋⢰⠁⠀⠀⠀⠀⠀⣀⠤⠊⠁⠀⠀⢱⡀⠘⢆⡀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠖⠛⠛⢉⣤⠞⠁⠀⠀⠀⠀
⠀⠀⠀⠀⡜⠁⠀⠈⢢⡀⠀⠀⠀⠀⠁⠀⠀⠀⣀⠔⠋⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠉⠀⠀⠀⣀⠀⠀⠈
⠀⠀⠀⡜⠀⠀⠀⠀⢰⠑⢄⠀⠀⠀⠀⠀⠀⠊⠀⢀⣀⢀⠇⠀⡠⠒⠒⢶⠈⠉⠑⡖⠈⠓⢢⠤⢄⣀⣴⣾⣏⠉⠛⠋⠉⠉⠀⠀⠀⢠
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠑⣄⡀⠀⠀⠀⠀⠀⠀⣹⡿⢤⣼⠃⠀⠀⢸⠀⠀⠀⡇⠀⠀⢸⠀⠀⠈⣿⣿⣿⣦⣀⣀⣀⣀⣀⣶⢶⣿
⠀⠀⠀⠀⠀⣠⠔⠒⢻⠀⠀⠀⠃⠉⠒⠤⣀⡀⠤⠚⠁⣇⡰⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠀⠀⣰⠟⠋⠁⠀⠀⠀⠀⠈⠉⠛⠦⡻
⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠀⠀⠈⠓⠤⣀⡀⠀⠀⠀⠀⠀⢀⣠⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⠉⠉⠉⠉⠉⡁⠀⠀⠀⠀⠀
"""


happy = """

⠀⠀⠀⢰⠇⠀⠀⠀⠀⠀⠀⡼⠁⡴⣼⢄⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠆⢠⡄⣀⡄⡆⢣⢏⣆⠃⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠹
⠀⠀⠀⡎⠀⠀⠀⠀⠀⠀⢠⠃⡰⢱⣏⡿⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣸⣏⢻⢻⡈⡞⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀
⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⡜⢰⠃⠀⠈⠁⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠉⠁⠁⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀
⣄⣀⡾⠀⠀⠀⠀⠀⠀⢰⣧⠇⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀
⠋⢹⡇⠀⠀⠀⠀⠀⠀⣼⡞⠀⠀⠀⠀⠀⠀⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀
⠀⣸⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀
⠀⡇⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⢀⡎⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⣸⣇⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀
⠀⠃⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⣰⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⣠⠴⢲⡏⠙⢧⠀⠀⢧⠀⠀⠈⠁⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠅⠀
⢸⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢀⣴⠟⠚⣽⣿⠉⠉⠙⠒⠦⣄⡴⠃⠀⠀⠀⠀⡞⠀⠀⢀⡞⠀⠀⠠⠎⠁⠀⡜⠀⠀⠈⢳⡀⠀⠳⡀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣸⠀⠀⠀⠀⠀⠀⠀⣿⣀⣴⡿⠃⣠⡞⣹⠃⠀⠀⠀⠀⣰⠏⠉⠀⠀⠀⡔⡸⠁⠀⣠⡞⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠹⣄⠀⠙⢦⠳⡀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⠀⠀⠀⠀⠀⠀⠀⡿⢋⡾⢁⡴⠋⣼⠃⠀⠀⠀⣠⢞⡏⠀⠀⠀⠀⡸⡱⠁⢀⡼⢡⠇⠀⠀⠀⠀⠀⣠⠃⠀⠀⣀⣀⡀⠀⠈⢷⡀⠀⠑⣝⣦⡀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢈⠀⠀⠀⠀⠀⠀⠀⣷⢟⣴⠏⠀⣼⠃⠀⢀⣤⣞⣁⡞⠀⠀⠀⠀⣰⡿⣁⡴⠋⢀⡞⠀⠀⠀⠀⠀⣰⠋⣠⠔⣊⣁⣤⣴⣶⣾⣿⣿⣿⣶⣿⣿⣿⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⠀⠀⠀⠀⠀⠀⠀⣿⠟⠁⣷⣾⣥⣴⣶⣿⣷⣶⣿⣿⣵⣦⣀⣼⣿⠟⠉⠀⠀⡜⠀⠀⠀⠀⢀⡾⠁⢘⣽⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠙⠛⢿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⠀⠀⠀⠀⠀⠀⠀⢹⢀⣤⣿⣿⡿⠟⠋⢉⣿⣿⣿⣿⣿⣿⣿⣞⠁⠀⠀⠀⡼⠁⠀⠀⢀⣴⠏⠀⠀⠈⠿⠋⢹⣿⣻⣿⠛⠻⡿⢦⣶⠀⠀⣸⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣟⢿⣿⣏⠀⠀⠀⢸⣿⣿⣿⠋⠙⣿⣴⡏⠀⠀⠀⡼⠁⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠘⣿⠟⠙⣄⣠⡟⠂⣼⠀⢠⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡤⠀⡄⠀⠀⠀⠀⠀⠀⢻⡆⢻⣿⡄⠀⠀⠸⣟⠁⠘⠦⠴⠃⢸⡇⠀⠀⡼⠁⣠⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⣇⣀⣇⣠⠇⠀⡞⢟⣟⡜⠀⠀⠀⠀⠀⢠⠆⠀⡀⠀
⢻⡆⢧⠀⠀⠀⠀⠀⠀⠈⣿⡄⠙⣿⣄⠀⠀⠙⣆⣸⣁⣀⡿⠼⠀⢀⡾⠷⣿⠟⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠙⠛⢀⣾⠟⠀⠀⠀⠀⠀⣠⠟⠀⠀⡇⠀
⠃⡇⠸⡄⠀⠀⠀⠀⠀⠀⠘⢷⡀⠀⠈⠶⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⢠⠄⣢⡿⠋⠀⠀⠀⠀⣠⠞⠁⠀⠀⢸⠓⠶
⠀⢻⠀⢣⠀⠀⣄⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢁⡴⠋⠀⠀⠀⣠⡴⠛⠁⠀⠀⠀⡇⣼⠀⠀
⠀⠈⡆⠈⢧⡀⠈⠙⠢⢤⣀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⣀⡤⠖⠋⣹⡇⠀⠀⠀⠀⢀⣇⡇⠀⠀
⠶⢶⣧⠀⠀⠑⢄⡀⠀⠀⠈⢻⡗⣶⡤⣤⣽⣳⣦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠰⠿⠓⠛⠉⠁⠀⠀⢠⡿⠀⠀⠀⠀⠀⢸⢾⠀⠀⠀
⠀⠀⠘⡆⠀⠀⠀⠙⠲⣶⣤⣄⣙⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡶⠂⠀⠁⠀⠀⠀⠀⠀⠀⠈⢻⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀
⠀⠀⠀⢳⠀⠀⠀⠀⠀⢠⠈⣿⡇⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⠀
⠀⠀⠀⢸⡆⠀⠀⠀⠀⠸⡄⢻⡇⠀⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⣸⠁⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀
⠀⠀⠀⢸⢻⡄⠀⠀⠀⠀⢧⢸⣇⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⣠⡶⠋⠁⢠⠇⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀
⠀⠀⠀⢠⠀⣷⡄⠀⠀⠀⠈⣎⣿⠀⠀⠀⠀⠀⠙⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠤⠚⠁⠀⠀⠀⠀⠀⠀⣀⣴⣾⣻⣄⠀⢠⠏⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢰⠇⠹⣄⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⢿⢏⡽⢿⠉⠻⣴⠏⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠀⣀
⠀⠀⠀⣀⡼⠀⠀⠘⢧⡀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⠟⠉⠁⡞⢀⡼⠃⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⢠⣾⡿
⠀⠀⢠⣿⠃⠀⠀⠀⠀⠙⢦⡀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣹⣷⣦⣀⣀⣤⣶⢟⣻⣿⠟⠋⠉⠁⠀⠀⢀⣷⠟⠀⠀⢀⡴⠞⠁⠀⠀⠀⠀⠀⠀⢀⣼⣿⣯⡴
⢀⣣⣿⠏⠀⠀⠀⠀⠀⠀⠀⠙⠢⣄⡀⠙⣆⠀⠀⠀⢀⡖⠲⢤⠀⠀⠀⠀⢸⡥⢿⣿⣿⣿⣾⣫⡟⠁⠀⠀⠀⠀⠀⠀⠶⠯⣤⣤⡶⠚⠉⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡟⠁⠀
⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠾⠷⠄⢠⣟⡀⢠⠏⠀⠀⠀⠀⠀⠹⡌⠛⠻⣄⣾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣶⣄⣤⣄⡀⠀⠀⣀⣴⣿⣿⣿⡿⠁⠀⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⢿⣀⣀⣾⣻⣀⣀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣷⣟⣻⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣸⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⡉⢹⣿⡏⣇⣩⡷⠀⠀⠀⣀⣤⣾⠟⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀
"""


nice = """

⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⡀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣶⡇⠀⣾⡇⠀⠛⠃⠀⠀⣾⠛⠛⠀⠀⡇⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⢷⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⠻⣼⣿⠇⠀⢸⡇⠀⢸⡇⠀⢀⡀⠀⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠟⠀⠹⠿⠁⠀⠘⠃⠀⠀⠙⠛⠋⠀⠀⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠀⠀⠀⠀⠀⣠⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣄⣠⡤⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢾⣤⣤⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣯⣿⣿⣿⣭⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⢿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀
⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣿⣿⣿⣿⣿⣿⣿⠹⣿⣿⣿⣿⣿⣿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⠆⠀⠀
⠀⠰⠿⠿⠿⣿⣿⣿⣿⣿⣿⡿⠀⢠⣿⣿⣿⣿⣿⣿⣿⡄⣿⣿⣿⣿⣿⣿⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠑⠊⠙⣿⣿⣿⠿⠿⠿⠛⠃⠙⠛⣛⣿⣿⣿⣄⡸⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡧⣴⡾⠿⠿⠿⣭⡄⠀⠀⠀⠀⠀⠠⠽⠛⠻⠟⠿⣿⣻⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡇⠀
⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⠋⠉⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀
⠀⠀⢀⡤⣤⡔⢻⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⢾⣍⠙⠆⢸⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⢠⠃⢠⡟⠁⢸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡧⠴⠋⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⣦⡇⠀⣿⠁⣸⣻⣿⣿⣿⠿⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⡇⢻⠀⠻⠀⠉⠀⠉⠻⣿⣿⣿⣿⣿⣶⣦⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⡇⠀⠁⠀⢰⣾⣿⣧⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⢸⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢣⠀⠀⣄⡈⠛⠿⠁⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⢁⠀⠈⡷⠀⠀⢀⣔⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⢻⣿⠿⠛⠉⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣿⣿⣿⣿⣿⠃
⠀⠀⢃⠀⠀⠀⢠⠎⠁⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⠟⠁⠀⣀⣤⠴⠛⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⠀
⠀⠀⢸⠀⠀⠀⠸⣀⠀⠘⣿⣿⣿⣿⠟⠋⣀⣾⣋⣤⡤⠖⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⡇⠀
⠀⠀⠈⡅⠀⠀⠀⢹⠀⠀⢠⡼⠛⠁⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⡏⢸⣿⡿⠀⠀
⠀⠀⠀⢱⠀⠀⠀⠈⣿⣠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡉⠉⠉⠉⠀⠈⠉⠀⠀⠀
⠀⠀⠀⠀⠁⠀⠀⠀⠈⣹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣄⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀
"""


ztwo = """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡷⡀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠺⣟⡽⠀⠀⠀⠀⠀⠀⠀⠈⠑⠂⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠊⠁⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠈⠳⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠆⠀⢰⡃⠀⠐⡄⠀⢲⠀⠃⢻⠀⠀⠀⡄⠀⠀⠈⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣶⣄⣺⢇⡄⠀⡇⠀⢰⢺⠱⣄⠀⠘⢆⠈⡆⠀⠸⠀⠀⠀⡇⠀⠀⠀⠰⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⡏⢸⠀⠀⡇⠀⢸⣾⢀⣨⣷⡄⠈⢣⣇⠀⠀⡆⠀⠀⡇⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠃⢸⡄⢸⡇⡀⢸⢿⡏⠀⣀⣹⣦⡀⢿⠀⠀⡇⠀⠀⡇⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⡄⠈⡇⠈⣿⣿⣼⣞⣷⠾⣿⣿⡿⠉⢻⠀⠀⡇⠀⠀⡿⠟⢷⡄⠀⠀⠀⡘⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⣇⢸⢿⡀⠇⠻⠉⠸⠏⣠⠟⠉⠀⠀⠀⡄⠀⠿⠀⠀⣿⡀⠀⡇⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣾⣷⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢀⡿⢃⣼⠁⠀⠀⠃⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⡻⢯⣻⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⢸⡧⡎⢸⠃⠀⠀⢠⢀⣸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⢸⠉⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢸⡇⡇⢸⠀⠀⠀⢸⡈⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠃⢸⡀⠀⠀⠀⢀⡠⠴⠚⠀⠀⠀⠀⠀⢸⠀⠀⠀⢸⡇⢸⢸⡀⠀⠀⠈⡇⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⡆⠀⢇⠀⠀⠰⠋⠀⠀⠀⠀⠀⠀⠀⠀⢨⠀⠀⠀⢸⠃⠈⡇⡇⠀⠀⠀⢱⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠍⠀⠀⠀⣿⠀⠀⢡⠱⠀⠀⠀⠸⡜⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣽⢆⠀⠀⠀⠀⠀⣠⠒⠁⠉⢀⡆⠀⠀⣿⡄⠀⠸⡄⠀⠀⠀⠀⢇⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⣿⠀⠓⠤⠔⠒⠻⡇⢀⡴⠚⠉⡇⠀⠀⡧⢇⠀⠀⢱⡀⠀⠀⠀⠘⣾⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡆⠀⢰⣿⡄⡆⠀⠀⠀⠀⢷⠋⠀⠀⠀⡇⠀⢀⠁⢈⠷⢶⣤⡷⣤⣤⢤⡤⠞⠓⠒⠦⢄⡀⠀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⢸⡇⡇⢁⠀⠀⠀⢀⢻⠀⠀⠀⠀⡇⠀⢸⠀⠣⢤⣀⣞⡏⠉⡱⠋⠀⠀⠀⠀⠀⠀⠙⡆
⠀⠀⠀⠀⠀⠀⢸⠀⠀⡞⠀⢡⢸⡀⠀⣀⡼⠀⢳⠀⠀⠀⡇⠀⡏⠀⢀⣾⣿⣾⣟⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻
⠀⠀⠀⠀⠀⠀⢸⠀⢠⠇⠀⠈⢇⡷⣺⢿⠏⡞⠑⠚⠉⢀⠀⢠⠁⣠⣿⣿⣻⣟⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿
⠀⠀⠀⠀⠀⠀⣿⠀⡘⢀⣠⠞⣉⠵⣡⠏⠀⢧⠀⠀⠀⣸⠀⣾⣼⣉⣉⣍⡿⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⢀⣴⡿⢠⠏⣉⣵⠞⠁⡰⡃⠀⠀⢘⡤⠴⢒⠇⢠⣿⡀⣉⣴⣿⣿⡁⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹
⠀⠀⠀⢀⠎⢸⡇⣸⣾⣿⣿⣀⣴⢱⣇⡤⠚⠁⢀⠀⣼⠄⡿⠋⠉⠁⢸⡛⢿⠑⢤⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⡞⢀⣎⢧⣟⣿⡿⠋⠀⠀⠉⠁⠀⣠⣾⠟⣸⡟⢸⠁⠀⠀⠀⠸⡇⢸⡄⢸⠃⠀⢀⣠⠤⠤⠤⠔⠢⡀⣸
⠀⠀⣸⠀⡸⢸⡟⣶⡿⠁⠀⠀⠀⠀⠀⠀⠉⠀⢠⣿⠀⡞⠀⠀⠀⠀⡇⣿⠸⣿⣾⠀⠀⠀⠙⠒⠒⠲⣌⣠⢌⣻
⠀⠀⡏⠀⣇⠞⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢿⢻⠀⡇⠀⠀⠀⠀⣷⡇⠀⢻⢹⡄⠀⠀⠀⠀⠀⠀⠈⠁⠀⣼
⠀⢰⢀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⣞⡄⡇⠀⠀⠀⠀⡿⡇⠀⠸⡆⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟
⠀⡞⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⠀⢸⢸⠛⠙⠻⠀⠀⠀⠀⢣⡇⠀⠀⡇⢡⠀⠀⠀⠀⠀⡀⠀⠀⠀⡇
⠀⢳⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡿⠀⠀⡞⡀⠀⠀⠀⠀⠀⠀⠘⡾⡄⠀⡇⢸⠀⠀⠀⠀⡼⠁⠀⠀⢠⠃
⢸⢸⠀⣾⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠘⣿⣆⡇⡆⠀⠀⣀⡜⠁⠀⠀⠀⢸⡆
"""


kwatch = """

⠀⠀⠀⠀⢀⡠⠤⠔⢲⢶⡖⠒⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⡚⠁⢀⠀⠀⢄⢻⣿⠀⠀⠀⡙⣷⢤⡀⠀⠀⠀⠀⠀⠀
⠀⡜⢱⣇⠀⣧⢣⡀⠀⡀⢻⡇⠀⡄⢰⣿⣷⡌⣢⡀⠀⠀⠀⠀
⠸⡇⡎⡿⣆⠹⣷⡹⣄⠙⣽⣿⢸⣧⣼⣿⣿⣿⣶⣼⣆⠀⠀⠀
⣷⡇⣷⡇⢹⢳⡽⣿⡽⣷⡜⣿⣾⢸⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀
⣿⡇⡿⣿⠀⠣⠹⣾⣿⣮⠿⣞⣿⢸⣿⣛⢿⣿⡟⠯⠉⠙⠛⠓
⣿⣇⣷⠙⡇⠀⠁⠀⠉⣽⣷⣾⢿⢸⣿⠀⢸⣿⢿⠀⠀⠀⠀⠀
⡟⢿⣿⣷⣾⣆⠀⠀⠘⠘⠿⠛⢸⣼⣿⢖⣼⣿⠘⡆⠀⠀⠀⠀
⠃⢸⣿⣿⡘⠋⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⡆⠇⠀⠀⠀⠀
⠀⢸⡿⣿⣇⠀⠈⠀⠤⠀⠀⢀⣿⣿⣿⣿⣿⣿⣧⢸⠀⠀⠀⠀
⠀⠈⡇⣿⣿⣷⣤⣀⠀⣀⠔⠋⣿⣿⣿⣿⣿⡟⣿⡞⡄⠀⠀⠀
⠀⠀⢿⢸⣿⣿⣿⣿⣿⡇⠀⢠⣿⡏⢿⣿⣿⡇⢸⣇⠇⠀⠀⠀
⠀⠀⢸⡏⣿⣿⣿⠟⠋⣀⠠⣾⣿⠡⠀⢉⢟⠷⢼⣿⣿⠀⠀⠀
⠀⠀⠈⣷⡏⡱⠁⠀⠊⠀⠀⣿⣏⣀⡠⢣⠃⠀⠀⢹⣿⡄⠀⠀
⠀⠀⠘⢼⣿⠀⢠⣤⣀⠉⣹⡿⠀⠁⠀⡸⠀⠀⠀⠈⣿⡇⠀
"""


shut_up = """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⣿⢏⡼⠀⢀⣾⢃⣼⠏⢠⡾⠃⣠⠏⠀⠁⣀⠀⡁⠀⠀⣠⡈⠉⡉⠉⢻⡄⠀⠀⠈⠈⢄⠐⣦
⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣯⣾⠃⣼⢁⢠⡿⣡⣾⠃⣴⣿⠁⣠⡟⠀⠄⠡⢀⠈⠀⣠⣱⣿⠇⠡⠄⠀⠀⢿⡆⠈⠄⡁⠈⣳⣽
⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣯⣿⠇⣼⡇⠀⣿⢓⣿⠧⣼⣻⠇⢠⣿⠁⠀⠌⠰⠀⢀⣴⣿⡟⣹⠀⠐⡌⠄⠸⡌⣿⠀⠀⠄⠄⢹⣿
⠄⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣟⣟⢨⣿⠀⣼⣏⣾⡟⣰⣟⣿⢣⣿⡟⠀⠈⢀⢀⣄⣾⣿⡟⣇⣿⣀⡐⣈⡀⠐⣿⢹⡇⠀⠁⠂⢸⣿
⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣹⡇⣯⣿⠀⣿⣿⣿⣿⣿⣼⣧⡟⣽⡃⠀⢈⠈⣭⣿⡿⠃⠉⣿⣿⡍⢉⡏⠙⠻⣿⣼⡷⣬⣶⢷⣿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣸⡗⣯⣿⢘⣿⢼⣿⣿⣿⣿⣿⢠⣿⠀⠀⣠⡾⣻⣟⣡⣄⡀⣽⡏⣧⢸⡇⠂⠱⢺⣿⣗⡻⣽⣾⣿⠘
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡿⣷⣹⣿⡞⡿⣸⣿⣿⣿⣿⡏⢸⡿⠀⣰⡿⢣⡿⢻⣿⣿⣷⣿⣥⣿⣾⢡⠀⠐⣾⣿⡝⣧⣿⣿⢹⡀
⠀⠀⠀⠀⢀⣠⣄⣀⣀⣀⣠⣸⣷⣿⣿⣿⢿⣇⠹⣟⡹⠿⡟⠀⠀⣿⣼⠏⢠⠋⠀⣿⣿⣿⣿⣿⣿⠿⣿⡇⠀⢨⣿⣿⡽⣟⡿⠁⢸⠅
⠀⠀⠀⢰⣿⡟⠿⠿⢯⡿⣽⣿⣻⣿⣯⣿⣌⣷⠀⠉⠛⠁⠀⠀⢨⡿⠁⠀⠀⠀⠀⣿⠟⣿⢿⣿⠟⣰⡟⠀⠠⣼⣿⢯⣽⠟⣠⠀⢸⡇
⠀⠀⢠⣿⣻⠃⢠⣄⣤⣔⣃⡀⠉⠉⠙⠛⠻⠾⢧⣤⣤⣤⣤⣀⣈⠀⠀⠀⠀⠀⠀⠙⠿⠶⠞⠁⣰⡿⠁⢀⣽⢻⣿⠟⠁⠀⢹⡄⠐⣿
⡄⠀⣾⣧⡟⠀⣿⡏⠉⠉⠛⠁⢈⣿⠃⠀⠀⠀⢠⣦⡀⢠⣌⡉⠙⠛⠛⠷⠶⠶⠴⣶⣤⣦⣰⣾⡟⠁⢠⡾⢫⣿⡟⠀⠰⠈⢌⣧⠀⢿
⡁⠀⣿⣽⠃⠀⠻⣿⣦⡀⠐⡁⢸⣟⠀⠀⠀⠀⢸⣿⡉⢸⡿⠁⠀⠁⠈⣷⡦⣷⣤⣤⣄⣠⡉⠉⠙⠛⣿⡿⣟⣿⣇⠀⠰⢈⠀⢿⡀⢈
⢶⣴⣿⡟⠀⠀⠀⠀⠛⢿⣦⢀⣿⡟⠶⠶⢶⣦⣿⡇⡘⣿⡇⠀⠀⠀⢀⣿⠁⠀⠉⢹⣿⠛⠛⠋⠀⢠⣿⣗⡣⢿⣿⠀⠐⠠⠀⢸⣷⡀
⣿⢿⣷⡇⠰⢷⣤⣤⣤⣿⢿⣸⣿⠁⠀⠀⠀⢠⣿⢱⢱⣿⠁⠀⠀⠀⣸⣿⠀⠈⡄⣿⡟⠀⠀⠀⠀⣸⣿⣶⢹⣻⣿⡄⠀⡁⠂⠈⣿⣷
⣿⠉⢥⡂⠀⠀⠈⠉⠉⠀⠀⠛⠛⠀⠀⠀⠀⢼⣿⠘⠘⣿⣄⠀⠀⢢⣿⡇⠀⠐⢆⣿⠃⠀⠀⠀⢀⣿⣗⣻⣧⢚⣿⣧⠀⠐⠠⠄⢻⣿
⣿⡀⡸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠿⠛⠋⠀⠀⠀⣸⣿⠀⠀⠐⡏⠹⣿⣧⢏⣷⢫⡜⣿⡆⠀⠃⠌⠘⣟
⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⠆⠀⠀⠀⣀⣀⠀⣁⠀⠀⠂⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠸⣿⠉⠁⢻⣎⢿⡧⡽⣹⣿⡄⠉⠄⠈⢷
⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⠀⠀⠀⢀⣿⡏⠂⣿⡿⠿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡶⠛⠙⣿⡞⣿⡱⣧⣛⣿⡄⠀⠈⠈
⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⢸⣿⠃⢰⣿⠃⢀⡝⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠄⣿⣳⢻⣧⡿⡹⡽⣷⡄⠀⠠
⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⣸⡟⠀⣼⣯⣤⣼⣽⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣯⠘⠀⣿⣧⢻⡷⣿⡱⢏⡿⣿⣄⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⣀⣀⣠⣿⠃⢡⣿⡇⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⢿⣄⣁⣿⣏⣯⣿⣿⠱⣏⣿⢿⣿⣦
⣶⣶⢦⡤⣤⣄⣀⣀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠸⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣬⠿⡻⣍⠯⣹⣿⢇⡿⡜⣿⡇⣿⣿
⠋⠙⠛⠛⢲⠾⢯⣽⣟⣟⣶⡶⢦⣤⣤⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣍⡲⣍⠳⢎⡳⣽⡟⢮⡳⡝⣿⡇⢸⣿
⠀⠀⠀⢀⣀⢀⡉⣴⣮⣉⣉⣹⣟⣿⡯⣭⣿⣻⣯⡿⣟⢳⡶⢤⡤⣤⣀⣀⣀⠀⠀⠀⠀⢰⣟⣛⣛⢳⡹⣎⣶⣿⣹⢣⣛⠵⣻⠆⠸⣿
"""

emo = """

⣶⣿⡟⠋⠉⠁⠉⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠻
⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⢀⣀⠀⠀⣀⡄⣴⣀
⠀⢡⣴⣤⣦⢄⣀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢰⣿⣿⣿⣾⣿⣿⣿⣷
⠀⠸⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠈⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿
⣦⣠⢄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣷⡋⠉⠉⠉⠋
⣿⢏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠙⣿⣿⣿⣿⣿⣿⣿⣿⣧⡙⢿⣿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣷⣶⣤⡀⠀⠀⠀⠈⠛⢿⣿⣿⣷⡀⠀⠀⠀
⠏⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣾⠓⠦⣄⡀⠀⠀⠀⠉⠛⠻⢿⣿⡏⣰⣿⢷⣄⠀⠀⠀⠀⠙⠛⠛⠛⠒⠛⠓
⣅⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⢻⣿⣿⣝⠿⣿⣿⣿⣿⣯⣉⠉⠓⢶⣄⣀⠀⠀⠀⠀⠉⠉⠛⠾⣌⣻⣦⣀⠀⢀⣀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠶⠿⠋⠀⠈⠻⣿⣷⣿⣿⠿⠿⣿⣷⣶⣼⣿⣿⣿⣶⣄⣀⡀⠀⠀⠀⠀⠉⠳⢬⠉⠉⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⣿⣿⣿⡷⣦⠾⢿⣿⣯⠙⢿⣿⣿⣿⣿⠏⢹⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠠⢤⣀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⣰⠻⣿⢸⣿⡟⢰⣿⣿⠄⣻⣿⠀⠈⣿⣿⣿⣿⡀⢸⠀⣠⡯⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣀⣉⣩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⢷⡀⠻⢿⣤⣟⣻⣶⡿⠃⠀⠀⠸⣿⣿⣿⣧⠼⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠳⣤⣶⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡝⠿⣿⣿⣿⣦⣤⣤⢤⡆⠉⠛⣛⣫⣥⠞⠀⠀⣀⣹⠟⠋⠁⠀⠀⠀⠀⣀⣠⠤⣤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢸⠏⢽⣿⠏⣹⣿⡏⠀⢈⣿⡿⠿⣿⣦⡀⠉⠙⠒⠒⠒⢛⠁⠀⠚⠛⠉⣠⡤⠒⠛⠉⠀⠀⠀⣀⡤⠖⠚⠉⠉⠀⠀⠀⠉⠃⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣿⣦⣼⣿⣆⢹⣿⣿⣿⣤⣿⣿⠀⠀⠉⠙⠲⢤⣤⣤⠶⠋⠀⠀⠀⣠⠞⠁⠀⠀⢀⣠⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡄⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣏⠉⠙⠛⠿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠁⠀⣠⠴⠋⠉⠀⠀⠀⠀⢀⣀⡤⢶⣶⣿⣿⣧⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠹⣦⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⢰⣿⣿⣿⣧⣏⠳⣌⠛⠛⣒⡤⠶⠶⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠧⠴⢻⠏⠀⣀⣠⠤⢴⣶⡟⠉⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠓⠀⢠
⡀⠀⠹⣿⣿⣿⡏⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⢸⡄⢈⡷⠋⠁⠀⢀⣠⡶⠋⠈⠃⠀⠀⠀⠠⣤⣄⣀⠀⠀⠈⠉⠉⠀⠀⣠⣿⣿⠃⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈
⣷⡄⠀⠈⠻⣿⢻⣿⣿⠇⠀⢀⣿⣿⣿⣿⣿⡼⠟⠉⠀⣀⡴⠚⠉⢈⡿⠃⠀⠀⠀⢸⣷⣾⡿⠿⠿⢷⠀⠀⠀⠀⢀⣴⣿⣿⡟⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀
⠉⣿⡄⠀⠀⠙⣿⣿⡏⠀⠀⢸⢹⣿⣿⡿⠋⠀⠀⣠⠔⠉⠀⠀⣴⡏⠀⠀⠀⠀⠀⠀⠙⠧⣄⣀⡤⠏⠀⠀⢀⣴⣿⣿⣿⣿⠃⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣁⠀⠀⠀⠀⠀
⢠⢏⣿⣄⠀⠀⠘⢿⡇⠀⠀⣟⣸⡟⠉⠀⠀⢀⡴⠋⠀⢀⣠⠞⠉⠙⠲⠦⠤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠏⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡿⣿⣷⠀⠀⠀⠀
⣿⣾⣿⢻⡆⠀⡀⠚⠀⠀⠠⠿⠋⠀⠀⠀⣠⠏⠀⠀⢠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠦⣤⣤⣴⣾⠛⠉⠭⠿⠿⣧⣤⣀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣧⠘⣿⣧⠀⠀⠀
⣿⢟⣵⢛⡟⠋⠁⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠺⡇⢹⣿⣿⣿⣿⣿⣿⣿⡉⠙⢦⡀⠀⣿⣿⣿⣿⣿⣿⣿⡟⣧⠹⣿⣧⠀⠈
⡿⢟⣁⡾⠁⠀⠀⠀⠀⠀⠀⠀⠉⠹⠏⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣇⢻⡌⢿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠙⣆⢸⣿⣿⣿⣿⣿⣿⣷⠸⡆⢿⣿⡇⠀
⣄⢿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠃⠸⣿⡎⠻⣌⢿⣿⣿⡿⠿⢿⣿⡆⠀⢠⡼⠛⣿⣿⣿⣿⣿⣿⣿⣧⡇⢸⣿⡇⠀
⣿⠀⢳⡀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠘⣿⣧⠻⣆⠻⣿⣿⣿⣿⣿⣿⠖⠁⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⡇⠀
⣿⠀⠀⠙⢦⣀⠀⡠⠔⠋⠁⠀⠀⠀⠀⣰⠋⠀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠈⢿⣷⡝⢷⣜⢿⣿⣿⣿⠿⣷⡀⠀⠀⠀⠘⢯⡻⢿⣿⣿⣿⣿⣿⣿⡄⠀
⣿⣆⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⢸⠴⢧⠴⠚⠁⠀⠀⠈⠉⠙⢲⠀⠀⠀⠀⢀⢰⠇⠀⠀⠀⠀⠀⠀⠀⢻⣿⣮⡻⣦⣙⢿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠙⠛⠿⢿⡿⠿⠿⠿⠿⢦
"""

headphone = """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⡾⠿⠛⠛⠉⠉⠉⠉⠉⠉⡉⠉⠉⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢿⣷⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠄⢒⣶⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠈⠄⠂⠀⠀⠀⠀⠨⠙⠻⢿⣿⣿⣿⣿⣿⣿⣟⣗⣻⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣤⣾⣿⣻⣿⠟⠁⠀⢀⠔⠀⠀⠀⠀⢀⣖⠀⠀⠈⠀⠈⢰⡇⠀⠀⠀⠀⠀⡀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⡿⣭⣛⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢤⣾⣿⣟⣿⠟⠁⠀⠀⢠⠃⠀⠀⠀⢀⠔⠁⢰⠈⠀⠀⠀⠀⡸⣇⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠈⠻⣟⣿⣿⣿⣿⣯⡿⢮⣝⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠯⣠⣾⣿⣿⡿⠁⠀⠀⠀⢠⠁⠀⠀⢀⡴⠁⠀⠀⠸⡄⠀⠀⠀⠀⡇⢸⡀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠠⡀⠀⠹⢿⣿⢿⣿⣿⣿⣯⣟⠻⣿⡖⠒⠒⠒⠢⠤
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠃⣾⡟⢀⠀⠀⠀⢠⠃⠀⠀⢠⠊⠀⠀⠀⠀⠀⢯⠀⠀⠐⠀⡇⠀⣇⠀⠀⠀⠀⠐⢃⠀⠀⠀⠀⢱⡀⠀⠸⣿⣿⣿⣿⣿⣏⣛⠻⡷⢾⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠜⡿⢧⡼⡟⠀⡜⠀⠀⢠⡟⠤⠤⣠⠃⠀⠀⠀⠀⠀⠀⢸⡃⠀⢀⠼⠃⠛⢻⡛⠤⢀⠀⠀⢸⠄⠀⠀⠀⠀⣧⠀⠀⢸⣿⣿⣿⣿⣿⠼⠻⢤⣛⣿⡄⠀⠀⠠
⠀⠀⠀⠀⠀⠀⢘⣴⣶⣾⣶⠁⡸⠀⡠⢲⠃⠇⠀⣰⠃⠈⠂⠀⠀⠀⠀⠀⠀⢳⠐⢡⢹⠀⠀⠀⢇⠀⠀⠉⠲⢼⡄⠀⠀⠀⠀⠸⡀⠀⠸⣿⣶⣿⣿⣿⣷⣶⣤⣝⡳⡇⠀⠀⠀
⠀⠀⠀⠀⠀⡠⢾⣩⣾⣿⠇⢰⠁⠊⠰⠃⢰⢀⣠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢖⠀⢸⠀⠀⠀⠈⢆⠀⠀⠀⠘⣷⠄⠀⠀⠀⠀⡇⢀⠀⢿⣿⡿⣿⣿⣿⣿⣿⣿⣾⣯⠀⠀⠀
⡀⠀⠀⢀⡼⣽⣿⣿⡿⣿⠀⡆⠀⡰⠁⠀⢸⣰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢺⢸⠀⠀⠀⠀⠘⡆⠀⠀⠀⡙⡄⠀⠀⠀⠀⢱⠀⠀⢺⣽⣦⣿⣿⢿⣿⣿⣿⡾⣷⠀⠀⠀
⠀⠀⢠⣯⣴⣿⣿⣫⣾⣿⣸⠁⢰⠁⡠⠒⠉⣃⡈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠙⠋⠙⠒⠤⣀⠘⢆⠀⠀⡆⢱⡀⠀⠀⠀⢸⣀⣤⣿⣿⣿⣿⣿⢿⡟⠛⠻⣹⡇⠀⠀⠀
⠀⢠⣯⣿⠟⣿⣾⣿⣿⣷⡏⢠⢣⠞⠀⣴⣿⠁⢈⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠛⠓⣄⠀⠈⢣⡈⢆⢠⡇⠀⢧⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣏⡟⣿⣷⣒⢿⡳⠤⣀⠀
⢠⡟⣿⡟⣲⣿⣿⣿⣿⣿⣧⣞⠏⠀⣼⣷⣿⣶⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣻⣿⣄⣤⣿⣧⠀⠀⢳⠀⠳⠅⠀⠈⣶⣿⣿⣿⣿⣷⣿⣿⣿⣿⢯⢵⡿⣿⣿⣼⣼⠀⠀⠈
⠇⠣⢿⠱⣿⣿⣿⣿⣿⣿⡟⣹⠀⠀⡟⢺⣿⣿⣷⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⣿⣿⣿⣿⡿⠀⠀⠈⡇⠀⠀⠀⣼⣿⣿⣿⣿⣿⣟⣿⡿⣷⣟⣿⣿⣿⣿⣟⣿⢟⡆⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠇⠣⠀⠀⠹⣯⣭⣵⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⣽⠿⠿⣯⣾⠇⠀⠀⠀⡇⠀⠀⣸⣿⣿⣿⣿⣿⢿⣿⣿⢠⣿⢋⣾⡿⣿⣿⣿⡹⣾⣧⠀⠀
⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠛⠁⠀⠀⠀⢀⡇⠀⠀⣿⣿⣿⣿⣿⣿⣺⣿⣹⠁⠈⣿⡟⠀⢸⠟⠛⡷⣿⣿⠀⠀
⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⢸⣿⣿⣿⣿⣿⣟⡈⠩⣝⠀⠀⢹⡇⠀⢸⠀⢀⣷⣿⣿⠀⠀
⠀⠀⠀⠀⡿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠛⠛⢿⣷⠛⠙⢹⠀⠀⢸⠁⠀⢸⠀⡸⡸⢉⡏⠀⠀
⠀⠀⠀⠀⡇⠀⠙⠻⢿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣆⠀⠀⠙⢶⣂⣽⠀⠀⠈⡀⠀⢸⠀⣿⣭⡿⠁⠀⠀
⠀⠀⠀⠀⠁⠀⠀⢀⠜⠉⡹⢢⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⠒⠒⠒⠒⠒⠒⠠⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣷⡄⠀⠈⠻⠋⠀⠀⠀⡇⠀⠆⢠⣷⡶⠁⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡠⠋⠀⡰⠁⠀⠑⠄⡀⠀⠀⠀⠀⠀⠈⢄⠀⠀⠀⠀⠀⠀⠀⠀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣹⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡸⠀⠀⢀⠇⢀⣀⡤⠐⠉⢦⡀⠀⠀⠀⠀⠈⠢⢄⡀⠀⠀⢀⣀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⠀⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠃⠀⠀⠘⠋⠁⢰⡇⠀⠀⠀⠉⠓⣤⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⠚⡏⠀⠀⠀⣤⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⢳⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⡜⡇⢀⡠⠔⢣⠀⠀⠉⢐⠶⠤⣄⣀⣀⡀⠀⠀⠀⠀⢀⣀⣀⣠⠤⠖⡞⠉⠀⠀⢣⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠈⡆⠀⠀⠀⠀⠀
⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⢰⠃⠈⠁⠀⠀⠈⣆⠀⡠⠋⣀⣠⣿⣾⣟⣯⠻⠿⠛⠛⠉⠁⠀⠀⠀⣈⣿⣷⣆⣀⠀⠱⡀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠼⠤⣀⣀⣀⣹⠀⠀⠀⠀⠀
⠀⠀⠀⡜⠀⠀⠀⠀⠀⢠⠃⢀⣀⣀⣠⣤⣤⣾⠎⠉⢩⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣶⣄⡑⡄⠀⢣⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⣷⣠⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣦⠀⡆⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⡛⠿⠿⠿⠿⠿⠿⠟⠛⠛⠉⠁⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠘⠀⠀⠀⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⢧⡀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀
"""

wtch = """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠤⠤⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠚⢿⡟⠃⠀⡆⠀⠀⠲⣄⠀⠈⠱⡦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⢾⡿⠚⠁⡎⠀⠀⠀⢳⡀⠀⠀⠀⠙⠦⡀⠀⠈⠓⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡞⢥⠏⠀⠀⣼⠁⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠈⢦⡀⠀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡎⢡⠏⠀⠀⣀⣿⠀⠀⣠⠤⣄⠘⡆⠀⠀⠀⠀⠀⠀⠳⡀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣜⠀⡞⠀⠀⣀⣀⣿⣶⡶⢿⠀⡿⠷⠾⠒⠒⠦⠤⠤⢤⣀⣻⡄⠀⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠃⢸⡗⠉⠉⠁⠀⠀⠀⠀⠈⠓⠃⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⢷⠀⠀⢹⠀⠀⠀⠀⠀⠀
⠀⠀⡟⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠈⡇⠀⠘⡇⠀⠀⠀⠀⠀
⠀⢸⠃⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢄⣱⡄⠀⣧⠀⠀⠀⠀⠀
⠀⢸⠀⠀⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠁⠀⠀⢻⠀⠀⠀⠀⠀
⠀⣾⡀⠀⣷⡇⠀⠀⠀⠀⣤⣀⠀⠀⣀⣀⡀⠀⠀⣤⡀⠀⠀⠀⠀⢿⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
⢰⣿⡇⡆⣿⡇⠀⠀⠀⠀⠛⠋⠀⠀⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀⢸⠀⠰⡀⠀⢸⠀⠀⠀⠀⠀
⠈⣿⣿⡐⠨⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⡇⠀⣼⠀⠀⠀⠀⠀
⠀⣿⢿⠅⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢰⠀⡇⠀⢿⠀⠀⠀⠀⠀
⠀⣿⣾⡇⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡜⠀⠁⠀⣼⡄⠀⠀⠀⠀
⠀⢻⣷⡇⠙⡎⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⡇⠀⢸⡇⠀⠀⠀⠀
⠀⠀⢿⣇⠐⡏⢷⠲⢶⠒⢶⢶⡖⢲⣶⣶⣉⣽⣿⣿⣿⡏⢻⢻⠉⢻⠃⠀⡇⠀⡏⣇⠀⠀⠀⠀
⠀⠀⠈⢿⠆⠇⢘⡀⢸⡀⢸⠘⣇⣸⣿⣿⣿⣿⣿⡿⠁⣇⢹⢸⠀⡞⠀⠀⡃⠄⡇⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣷⢦⠀⢣⠀⡇⢘⣷⣿⣿⠿⣿⣿⠿⠋⠀⠀⢿⣿⣿⣠⠃⠀⠀⠃⠀⢱⠹⡆⠀⠀⠀
⠀⠀⠀⠀⡇⢸⠀⠘⣦⣷⣾⣿⣿⡉⠀⠀⠀⠀⠀⠀⠀⠈⢹⡏⣿⣿⣶⣦⣤⣀⡈⠇⡇⠀⠀⠀
⠀⠀⠀⢀⣧⣼⣶⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣀⠀
⢀⣴⣾⣿⣮⣭⣍⣙⣛⡿⢿⣿⣿⣿⣷⠚⣛⣋⣉⣛⢶⣾⣿⣿⡿⢛⣭⣾⣿⣿⣿⣿⣿⣿⣿⡷
"""

hkitty = """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠛⢿⣶⡄⠀⢀⣀⣤⣤⣦⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⠋⠀⠀⠈⠙⠻⢿⣶⣶⣶⣶⣶⣶⣶⣿⠟⠀⠀⠀⠀⠹⣿⡿⠟⠋⠉⠁⠈⢻⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⡧⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⣾⡏⠀⠀⢠⣾⢶⣶⣽⣷⣄⡀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢸⣧⣾⠟⠉⠉⠙⢿⣿⠿⠿⠿⣿⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣄⣀⣠⣼⣿⠀⠀⠀⠀⣸⣿⣦⡀⠀⠈⣿⡄⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠻⣷⣤⣤⣶⣿⣧⣿⠃⠀⣰⣿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⣀⠀⠀⣀⣴⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠛⠉⢸⣿⠀⠀⠀⠀
⢀⣠⣤⣤⣼⣿⣤⣄⠀⠀⠀⡶⠟⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⡄⠀⠀⠀⠀⢀⣀⣿⣄⣀⠀⠀
⠀⠉⠉⠉⢹⣿⣩⣿⠿⠿⣶⡄⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⣤⡀⠀⠀⠀⠀⠀⠿⡿⠃⠀⠀⠀⠘⠛⠛⣿⠋⠉⠙⠃
⠀⠀⠀⣤⣼⣿⣿⡇⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀⠘⠿⣤⡼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣼⣿⣀⠀⠀⠀
⠀⠀⣾⡏⠀⠈⠙⢧⠀⠀⠀⢿⣧⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠟⠙⠛⠓⠀
⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠻⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣶⣿⣯⡀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⢀⣴⠿⠿⠗⠈⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⠟⠋⠉⠛⠷⠄⠀⠀
⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⢿⣇⠀⢀⣠⡄⢘⣿⣶⣶⣤⣤⣤⣤⣀⣤⣤⣤⣤⣶⣶⡿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠈⠛⠛⠛⠋⠁⣼⡟⠈⠻⣿⣿⣿⣿⡿⠛⠛⢿⣿⣿⣿⣡⣾⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣦⣄⣀⣀⣀⣀⣴⣾⣿⡁⠀⠀⠀⡉⣉⠁⠀⠀⣠⣾⠟⠉⠉⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠛⠉⠀⠹⣿⣶⣤⣤⣷⣿⣧⣴⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢦⣭⡽⣯⣡⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

disg = """

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠓⠒⠤⢤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣶⣦⣭⣓⢟⢻⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡟⠽⣿⡍⡇⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠉⠙⠛⠡⠀⠘⢟⠀⠀⠀⠀⠈⠉⠙⠘⠻⣿⠇⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣲⣖⣒⢄⠻⣿
⣿⣿⣿⣿⣿⣿⣿⡏⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣷⣼
⣿⣿⣿⣿⣿⣿⡏⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠙⠻⡟⠙⢿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠈⠲⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⡇⠀⠀⠀⠀⠀⠒⢤⣀⡀⠀⠀⠀⠀⠈⠀⠀⠀⠀⣸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⡇⠀⠀⠀⠀⠀⠀⠀⠈⠂⠌⡑⠄⠀⠀⠀⠀⢀⢊⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⡿⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣇⡇⠈⢻⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣏⣿⣿⣿⣿⣿
"""


with open("anime_stickers.pk", 'wb') as f:
    pickle.dump([sticker("kawai1", kawai), sticker("happy", happy), sticker("nice", nice), sticker("ztwo1", ztwo),
                 sticker("kwatch", kwatch), sticker("shutup", shut_up), sticker("emo", emo),
                 sticker("headphone", headphone), sticker("wtch", wtch), sticker("hkitty", hkitty),
                 sticker("gisg", disg)], f)

with open("anime_stickers.pk", 'rb') as f:
    stik = pickle.load(f)

print(stik[0].pattern)