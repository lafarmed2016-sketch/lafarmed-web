import re

css_path = 'c:/Users/Intel/Desktop/pagina web lafarmed/assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Fonts
content = re.sub(r"@import url\('https://fonts\.googleapis\.com/css2\?family=Outfit.*?display=swap'\);", "@import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,300;0,400;0,700;0,900;1,400&display=swap');", content)
content = content.replace("'Inter', sans-serif", "'Lato', sans-serif")
content = content.replace("'Outfit', sans-serif", "'Times New Roman', Times, serif")

# Replace Colors
content = content.replace('--primary: #048C9A; /* Teal */', '--primary: #0071BA; /* Institutional Blue */')
content = content.replace('--primary-dark: #036C77;', '--primary-dark: #004D80;')
content = content.replace('--primary-light: #E0F2F4;', '--primary-light: #E6F3FB;')

content = content.replace('--secondary: #FF7B54; /* Orange */', '--secondary: #37AAE1; /* Light Blue */')
content = content.replace('--secondary-dark: #E56A45;', '--secondary-dark: #2087BD;')

# Also the mobile menu overlay color had a teal color: rgba(4, 140, 154, 0.95)
content = content.replace('rgba(4, 140, 154, 0.95)', 'rgba(0, 113, 186, 0.95)')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done updating styles.css!')
