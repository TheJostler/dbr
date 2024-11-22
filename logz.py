from colored import fg

# include these variables in a print() function to output different clours to your terminal
txt_blue = fg('blue')
txt_green = fg('green')
txt_white = fg('white')
txt_red = fg('red')

def info(txt):
  print(f"{txt_blue}[INFO]{txt_white} {txt}")
def warn(txt):
  print(f"{txt_red}[WARN]{txt_white} {txt}")
def blue(txt):
  print(f"{txt_blue}{txt_white} {txt}")
def red(txt):
  print(f"{txt_red}{txt_white} {txt}")
def green(txt):
  print(f"{txt_green}{txt_white} {txt}")