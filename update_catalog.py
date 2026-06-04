import sys

file_path = 'productos/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '    <!-- PRODUCTS SECTION -->'
end_marker = '    </section>'

start_idx = content.find(start_marker)
# Find the next closing section tag after start_marker
end_idx = content.find(end_marker, start_idx) + len(end_marker)

if start_idx == -1 or end_idx < len(end_marker):
    print('Could not find section markers')
    sys.exit(1)

new_section = '''    <!-- CATALOG SECTION -->
    <section class="catalog section-padding" id="catalogo">
        <div class="container">
            <div class="section-header animate-fade-up">
                <div>
                    <div class="pill" style="background: rgba(4, 140, 154, 0.1); border: none; box-shadow: none;">CATÁLOGO COMPLETO</div>
                    <h2 class="section-title">Encuentra el <span class="text-gradient">producto ideal</span></h2>
                </div>
            </div>

            <!-- TABS -->
            <div class="catalog-filters animate-fade-up" style="transition-delay: 100ms;">
                <button class="filter-btn active" data-filter="all">Todas las líneas</button>
                <button class="filter-btn" data-filter="antibiotica">Antibiótica</button>
                <button class="filter-btn" data-filter="dermatologica">Dermatológica</button>
                <button class="filter-btn" data-filter="digestiva">Digestiva</button>
                <button class="filter-btn" data-filter="dolor">Dolor</button>
                <button class="filter-btn" data-filter="respiratoria">Respiratoria</button>
                <button class="filter-btn" data-filter="natural">Natural</button>
            </div>

            <!-- PRODUCT GRID -->
            <div class="catalog-grid" id="catalogGrid">
                
                <!-- Product 1 -->
                <div class="product-card animate-fade-up" data-category="antibiotica" style="transition-delay: 200ms;">
                    <div class="product-img-box">
                        <span class="product-badge antibiotica">Línea Antibiótica</span>
                        <img src="https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&q=80&w=400" alt="Amoxicilina">
                    </div>
                    <div class="product-info">
                        <h3>Amoxicilina 500mg</h3>
                        <p class="product-desc">Caja x 100 cápsulas. Antibiótico de amplio espectro para tratamiento de infecciones.</p>
                        <a href="https://wa.me/51984375070?text=Hola,%20deseo%20cotizar%20Amoxicilina%20500mg" target="_blank" class="btn-outline-primary product-btn">Cotizar <i data-lucide="message-circle" class="icon" style="width: 16px; height: 16px;"></i></a>
                    </div>
                </div>

                <!-- Product 2 -->
                <div class="product-card animate-fade-up" data-category="antibiotica" style="transition-delay: 300ms;">
                    <div class="product-img-box">
                        <span class="product-badge antibiotica">Línea Antibiótica</span>
                        <img src="https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&q=80&w=400" alt="Azitromicina">
                    </div>
                    <div class="product-info">
                        <h3>Azitromicina 500mg</h3>
                        <p class="product-desc">Caja x 3 tabletas recubiertas. Macrólido indicado para infecciones del tracto respiratorio.</p>
                        <a href="https://wa.me/51984375070?text=Hola,%20deseo%20cotizar%20Azitromicina%20500mg" target="_blank" class="btn-outline-primary product-btn">Cotizar <i data-lucide="message-circle" class="icon" style="width: 16px; height: 16px;"></i></a>
                    </div>
                </div>

                <!-- Product 3 -->
                <div class="product-card animate-fade-up" data-category="dermatologica" style="transition-delay: 400ms;">
                    <div class="product-img-box">
                        <span class="product-badge dermatologica">Línea Dermatológica</span>
                        <img src="https://images.unsplash.com/photo-1556228578-0d85b1a4d571?auto=format&fit=crop&q=80&w=400" alt="Terbinafina">
                    </div>
                    <div class="product-info">
                        <h3>Terbinafina 1%</h3>
                        <p class="product-desc">Tubo x 20g. Crema antimicótica de amplio espectro para tratamiento tópico.</p>
                        <a href="https://wa.me/51984375070?text=Hola,%20deseo%20cotizar%20Terbinafina%201%25" target="_blank" class="btn-outline-primary product-btn">Cotizar <i data-lucide="message-circle" class="icon" style="width: 16px; height: 16px;"></i></a>
                    </div>
                </div>

                <!-- Product 4 -->
                <div class="product-card animate-fade-up" data-category="digestiva" style="transition-delay: 500ms;">
                    <div class="product-img-box">
                        <span class="product-badge digestiva">Línea Digestiva</span>
                        <img src="https://images.unsplash.com/photo-1631549916768-4119b2e5f926?auto=format&fit=crop&q=80&w=400" alt="Omeprazol">
                    </div>
                    <div class="product-info">
                        <h3>Omeprazol 20mg</h3>
                        <p class="product-desc">Caja x 30 cápsulas. Protector gástrico e inhibidor de bomba de protones.</p>
                        <a href="https://wa.me/51984375070?text=Hola,%20deseo%20cotizar%20Omeprazol%2020mg" target="_blank" class="btn-outline-primary product-btn">Cotizar <i data-lucide="message-circle" class="icon" style="width: 16px; height: 16px;"></i></a>
                    </div>
                </div>

                <!-- Product 5 -->
                <div class="product-card animate-fade-up" data-category="dolor" style="transition-delay: 600ms;">
                    <div class="product-img-box">
                        <span class="product-badge dolor">Línea Dolor</span>
                        <img src="https://images.unsplash.com/photo-1587854692152-cbe660dbde88?auto=format&fit=crop&q=80&w=400" alt="Ibuprofeno">
                    </div>
                    <div class="product-info">
                        <h3>Ibuprofeno 400mg</h3>
                        <p class="product-desc">Caja x 100 tabletas. Analgésico y antiinflamatorio no esteroideo (AINE).</p>
                        <a href="https://wa.me/51984375070?text=Hola,%20deseo%20cotizar%20Ibuprofeno%20400mg" target="_blank" class="btn-outline-primary product-btn">Cotizar <i data-lucide="message-circle" class="icon" style="width: 16px; height: 16px;"></i></a>
                    </div>
                </div>

                <!-- Product 6 -->
                <div class="product-card animate-fade-up" data-category=\"dolor\" style=\"transition-delay: 700ms;\">
                    <div class=\"product-img-box\">
                        <span class=\"product-badge dolor\">Línea Dolor</span>
                        <img src=\"https://images.unsplash.com/photo-1587854692152-cbe660dbde88?auto=format&fit=crop&q=80&w=400\" alt=\"Paracetamol\">
                    </div>
                    <div class=\"product-info\">
                        <h3>Paracetamol 500mg</h3>
                        <p class=\"product-desc\">Caja x 100 tabletas. Analgésico y antipirético seguro y de acción rápida.</p>
                        <a href=\"https://wa.me/51984375070?text=Hola,%20deseo%20cotizar%20Paracetamol%20500mg\" target=\"_blank\" class=\"btn-outline-primary product-btn\">Cotizar <i data-lucide=\"message-circle\" class=\"icon\" style=\"width: 16px; height: 16px;\"></i></a>
                    </div>
                </div>

                <!-- Product 7 -->
                <div class="product-card animate-fade-up" data-category="respiratoria" style="transition-delay: 800ms;">
                    <div class="product-img-box">
                        <span class="product-badge respiratoria">Línea Respiratoria</span>
                        <img src="https://images.unsplash.com/photo-1628771065518-0d82f1938462?auto=format&fit=crop&q=80&w=400" alt="Loratadina">
                    </div>
                    <div class="product-info">
                        <h3>Loratadina 10mg</h3>
                        <p class="product-desc">Caja x 100 tabletas. Antihistamínico de segunda generación para alergias.</p>
                        <a href="https://wa.me/51984375070?text=Hola,%20deseo%20cotizar%20Loratadina%2010mg" target="_blank" class="btn-outline-primary product-btn">Cotizar <i data-lucide="message-circle" class="icon" style="width: 16px; height: 16px;"></i></a>
                    </div>
                </div>

                <!-- Product 8 -->
                <div class="product-card animate-fade-up" data-category="natural" style="transition-delay: 900ms;">
                    <div class="product-img-box">
                        <span class="product-badge natural">Naturvid Natural</span>
                        <img src="https://images.unsplash.com/photo-1471193945509-9ad0617afabf?auto=format&fit=crop&q=80&w=400" alt="Colágeno">
                    </div>
                    <div class="product-info">
                        <h3>Colágeno Hidrolizado</h3>
                        <p class="product-desc">Frasco x 300g. Suplemento dietético para el cuidado de articulaciones y piel.</p>
                        <a href="https://wa.me/51984375070?text=Hola,%20deseo%20cotizar%20Colageno%20Hidrolizado" target="_blank" class="btn-outline-primary product-btn">Cotizar <i data-lucide="message-circle" class="icon" style="width: 16px; height: 16px;"></i></a>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Script for Filtering -->
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const filterBtns = document.querySelectorAll(".filter-btn");
            const products = document.querySelectorAll(".product-card");

            // Also check if there's a filter in the URL e.g. ?linea=antibiotica
            const urlParams = new URLSearchParams(window.location.search);
            const initialFilter = urlParams.get("linea") || "all";

            const applyFilter = (filterValue) => {
                // Update active button
                filterBtns.forEach(btn => {
                    if (btn.getAttribute("data-filter") === filterValue) {
                        btn.classList.add("active");
                    } else {
                        btn.classList.remove("active");
                    }
                });

                // Filter products
                products.forEach(product => {
                    if (filterValue === "all" || product.getAttribute("data-category") === filterValue) {
                        product.style.display = "flex";
                        setTimeout(() => {
                            product.style.opacity = "1";
                            product.style.transform = "scale(1)";
                        }, 50);
                    } else {
                        product.style.opacity = "0";
                        product.style.transform = "scale(0.95)";
                        setTimeout(() => {
                            product.style.display = "none";
                        }, 300);
                    }
                });
            };

            // Apply initial filter
            applyFilter(initialFilter);

            filterBtns.forEach(btn => {
                btn.addEventListener("click", () => {
                    const filterValue = btn.getAttribute("data-filter");
                    applyFilter(filterValue);
                });
            });
        });
    </script>'''

new_content = content[:start_idx] + new_section + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated successfully')
