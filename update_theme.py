import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace tailwind config colors
config_old = '''          colors: {
            "surface-container": "#eaedff",
            "surface-container-highest": "#dae2fd",
            "secondary-container": "#d0e1fb",
            "on-tertiary-container": "#009668",
            "inverse-surface": "#283044",
            "surface-container-lowest": "#ffffff",
            "surface-dim": "#d2d9f4",
            "on-primary": "#ffffff",
            "on-error": "#ffffff",
            "tertiary-fixed-dim": "#4edea3",
            "error": "#ba1a1a",
            "on-secondary-fixed": "#0b1c30",
            "background": "#faf8ff",
            "outline-variant": "#c6c6cd",
            "primary": "#000000",
            "inverse-on-surface": "#eef0ff",
            "on-surface-variant": "#45464d",
            "surface": "#faf8ff",
            "on-tertiary": "#ffffff",
            "on-primary-container": "#5979ff",
            "secondary": "#505f76",
            "tertiary-container": "#002113",
            "on-error-container": "#93000a",
            "error-container": "#ffdad6",
            "primary-fixed": "#dde1ff",
            "primary-container": "#001356",
            "surface-container-high": "#e2e7ff",
            "on-primary-fixed-variant": "#0035be",
            "secondary-fixed-dim": "#b7c8e1",
            "on-secondary-fixed-variant": "#38485d",
            "surface-tint": "#124af0",
            "tertiary": "#000000",
            "on-secondary": "#ffffff",
            "outline": "#76777d",
            "surface-bright": "#faf8ff",
            "primary-fixed-dim": "#b8c3ff",
            "on-secondary-container": "#54647a",
            "secondary-fixed": "#d3e4fe",
            "inverse-primary": "#b8c3ff",
            "surface-variant": "#dae2fd",
            "tertiary-fixed": "#6ffbbe",
            "on-primary-fixed": "#001356",
            "surface-container-low": "#f2f3ff",
            "on-background": "#131b2e",
            "on-tertiary-fixed-variant": "#005236",
            "on-surface": "#131b2e",
            "on-tertiary-fixed": "#002113"
          }'''

config_new = '''          colors: {
            "surface-container": "#fdf2f8",
            "surface-container-highest": "#fce7f3",
            "secondary-container": "#fbcfe8",
            "on-tertiary-container": "#831843",
            "inverse-surface": "#831843",
            "surface-container-lowest": "#ffffff",
            "surface-dim": "#fce7f3",
            "on-primary": "#ffffff",
            "on-error": "#ffffff",
            "tertiary-fixed-dim": "#f472b6",
            "error": "#ba1a1a",
            "on-secondary-fixed": "#4c0519",
            "background": "#fffbfc",
            "outline-variant": "#fbcfe8",
            "primary": "#000000",
            "inverse-on-surface": "#fdf2f8",
            "on-surface-variant": "#9d174d",
            "surface": "#fffbfc",
            "on-tertiary": "#ffffff",
            "on-primary-container": "#db2777",
            "secondary": "#9d174d",
            "tertiary-container": "#4c0519",
            "on-error-container": "#93000a",
            "error-container": "#ffdad6",
            "primary-fixed": "#fbcfe8",
            "primary-container": "#831843",
            "surface-container-high": "#fce7f3",
            "on-primary-fixed-variant": "#be185d",
            "secondary-fixed-dim": "#f9a8d4",
            "on-secondary-fixed-variant": "#9d174d",
            "surface-tint": "#db2777",
            "tertiary": "#000000",
            "on-secondary": "#ffffff",
            "outline": "#be185d",
            "surface-bright": "#fffbfc",
            "primary-fixed-dim": "#f9a8d4",
            "on-secondary-container": "#831843",
            "secondary-fixed": "#fce7f3",
            "inverse-primary": "#f9a8d4",
            "surface-variant": "#fce7f3",
            "tertiary-fixed": "#f9a8d4",
            "on-primary-fixed": "#4c0519",
            "surface-container-low": "#fdf2f8",
            "on-background": "#4c0519",
            "on-tertiary-fixed-variant": "#be185d",
            "on-surface": "#4c0519",
            "on-tertiary-fixed": "#4c0519"
          }'''

html = html.replace(config_old, config_new)

# 2. Replace style overrides
html = html.replace('color: #124af0;', 'color: #db2777;')
html = html.replace('border-bottom-color: #124af0;', 'border-bottom-color: #db2777;')
html = html.replace('color: #4edea3;', 'color: #f472b6;')
html = html.replace('border-bottom-color: #4edea3;', 'border-bottom-color: #f472b6;')

# 3. Replace utility classes for gradients and badges
html = html.replace('from-[#124af0]', 'from-[#db2777]')
html = html.replace('to-[#4edea3]', 'to-[#f472b6]')
html = html.replace('bg-[#4edea3]', 'bg-[#f472b6]')
html = html.replace('text-[#005236]', 'text-[#9d174d]')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
