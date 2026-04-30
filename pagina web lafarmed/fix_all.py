import os
import glob
import re

root_dir = r"c:\Users\Intel\Desktop\pagina web lafarmed"
files = glob.glob(os.path.join(root_dir, "**", "index.html"), recursive=True)

for filepath in files:
    is_subfolder = os.path.dirname(filepath) != root_dir
    prefix = "../" if is_subfolder else ""
    
    # 1. Revert the CERTIFICACIONES column to the 24px version
    cert_col_new = f"""<h4 class="footer-title">CERTIFICACIONES</h4>
                <ul class="footer-links" style="display: flex; flex-direction: column; gap: 1rem;">
                    <li style="display: flex; align-items: center; gap: 0.75rem;">
                        <img src="{prefix}assets/img/BPA_GPS.png" style="width: 24px; height: 24px; object-fit: contain;">
                        <span>BPA — DIGEMID</span>
                    </li>
                    <li style="display: flex; align-items: center; gap: 0.75rem;">
                        <img src="{prefix}assets/img/BPDT_GPDT.png" style="width: 24px; height: 24px; object-fit: contain;">
                        <span>BPDT — DIGEMID</span>
                    </li>
                    <li style="display: flex; align-items: center; gap: 0.75rem;">
                        <img src="{prefix}assets/img/BPM_GMP.png" style="width: 24px; height: 24px; object-fit: contain;">
                        <span>BPM — DIGEMID</span>
                    </li>
                </ul>"""

    # 2. Replace the social links with the 3 big cert images + facebook
    social_links_new = f"""<div class="footer-certs-inline" style="display: flex; gap: 1rem; margin-top: 1.5rem; margin-bottom: 1.5rem;">
                    <div style="width: 65px; height: 65px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.05); border-radius: 50%; padding: 5px;">
                        <img src="{prefix}assets/img/BPA_GPS.png" style="width: 100%; height: 100%; object-fit: contain; transform: scale(1.2);">
                    </div>
                    <div style="width: 65px; height: 65px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.05); border-radius: 50%; padding: 5px;">
                        <img src="{prefix}assets/img/BPDT_GPDT.png" style="width: 100%; height: 100%; object-fit: contain; transform: scale(1.2);">
                    </div>
                    <div style="width: 65px; height: 65px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.05); border-radius: 50%; padding: 5px;">
                        <img src="{prefix}assets/img/BPM_GMP.png" style="width: 100%; height: 100%; object-fit: contain; transform: scale(1.2);">
                    </div>
                </div>
                <div class="social-links">
                    <a href="https://www.facebook.com/laboratoriolafarmed?ref=embed_page" target="_blank" class="social-btn" style="background: var(--primary);"><i data-lucide="facebook" class="icon"></i></a>
                </div>"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert Column 3 (Certificaciones)
    pattern_col = r'<h4 class="footer-title">CERTIFICACIONES</h4>\s*<ul class="footer-links".*?</ul>'
    content = re.sub(pattern_col, cert_col_new, content, flags=re.DOTALL)

    # Replace Column 1 Social Links
    # We will look for <div class="social-links">...</div> or <div class="footer-certs-inline"...
    pattern_social = r'<div class="social-links">.*?</div>'
    if '<div class="footer-certs-inline"' in content:
        # Already updated once, need a combined regex
        pattern_social_combined = r'<div class="footer-certs-inline".*?<div class="social-links">.*?</div>'
        content = re.sub(pattern_social_combined, social_links_new, content, flags=re.DOTALL)
    else:
        content = re.sub(pattern_social, social_links_new, content, count=1, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated footer layout")
