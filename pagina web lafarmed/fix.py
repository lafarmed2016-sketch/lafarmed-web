import os, re

base_dir = r"c:\Users\Intel\Desktop\pagina web lafarmed"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html') and file != 'scraped_table.html':
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            if root == base_dir:
                prefix = ""
            else:
                prefix = "../"

            # 1. Update the <nav> block for subpages
            nav_pattern = re.compile(r'<nav[^>]*>.*?</nav>\s*<a href="[^"]*contactenos/index\.html" class="btn btn-primary"[^>]*>.*?</a>', re.DOTALL)
            
            replacement = f"""<nav id="navMenu">
                <a href="{prefix}index.html" class="nav-link">Inicio</a>
                <a href="{prefix}quienes-somos/index.html" class="nav-link">Quiénes Somos</a>
                <a href="{prefix}cobertura/index.html" class="nav-link">Cobertura</a>
                <a href="{prefix}productos/catalogo.html" class="nav-link">Productos</a>
                <a href="{prefix}contactenos/index.html" class="nav-link">Contacto</a>
                <a href="{prefix}farmacovigilancia/index.html" class="nav-link">Farmacovigilancia</a>
            </nav>

            <div class="header-actions">
                <a href="{prefix}contactenos/index.html" class="btn btn-primary header-btn" style="text-decoration: none; display: flex; align-items: center; gap: 0.5rem;">
                    <i data-lucide="phone" class="icon"></i> Cotizar
                </a>
                <button class="menu-toggle" id="menuToggle" aria-label="Abrir menú">
                    <div class="hamburger">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </button>
            </div>"""
            
            if 'class="header-actions"' not in content:
                content = nav_pattern.sub(replacement, content)
            elif root == base_dir:
                content = content.replace('href="#"', 'href="index.html"')
                content = content.replace('href="#quienes-somos"', 'href="quienes-somos/index.html"')
                content = content.replace('href="#cobertura"', 'href="cobertura/index.html"')
                content = content.replace('href="#productos"', 'href="productos/catalogo.html"')
                content = content.replace('href="#contacto"', 'href="contactenos/index.html"')
                content = content.replace('href="#farmacovigilancia"', 'href="farmacovigilancia/index.html"')

            # 2. Add the JS if it doesn't exist
            if 'const menuToggle = document.getElementById(\'menuToggle\');' not in content:
                js_injection = """            // Mobile Menu Toggle
            const menuToggle = document.getElementById('menuToggle');
            const navMenu = document.getElementById('navMenu');
            const navLinks = document.querySelectorAll('.nav-link');

            const toggleMenu = () => {
                navMenu.classList.toggle('active');
                menuToggle.classList.toggle('active');
            };

            if (menuToggle && navMenu) {
                menuToggle.addEventListener('click', toggleMenu);
                navLinks.forEach(link => {
                    link.addEventListener('click', () => {
                        if (navMenu.classList.contains('active')) {
                            toggleMenu();
                        }
                    });
                });
            }

            // Intersection Observer for scroll animations"""
                content = content.replace('            // Intersection Observer for scroll animations', js_injection)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Done updating headers and JS!")
