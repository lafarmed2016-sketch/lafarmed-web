import re
import glob

files = [
    'index.html',
    'quienes-somos/index.html',
    'productos/index.html',
    'productos/catalogo.html',
    'contactenos/index.html',
    'farmacovigilancia/index.html',
    'cobertura/index.html'
]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We will replace the entire script section to be safe.
    # From <script> to </script> at the end of the file.
    start = content.find('    <script>')
    if start != -1:
        end = content.find('</script>\n</body>') + 9
        
        # Determine prefix for images
        pfx = '../' if '/' in f else ''
        
        new_script = f'''    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            // Initialize Lucide icons
            lucide.createIcons();

            // Header Scroll Effect
            const header = document.querySelector('header');
            window.addEventListener('scroll', () => {{
                if (window.scrollY > 35) {{
                    header.classList.add('scrolled');
                }} else {{
                    header.classList.remove('scrolled');
                }}
            }});

            // Intersection Observer for scroll animations
            const observerOptions = {{
                root: null,
                rootMargin: '0px',
                threshold: 0.1
            }};

            const observer = new IntersectionObserver((entries, observer) => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        entry.target.classList.add('visible');
                        observer.unobserve(entry.target);
                    }}
                }});
            }}, observerOptions);

            const animatedElements = document.querySelectorAll('.animate-fade-up');
            animatedElements.forEach(el => observer.observe(el));

            // Chat Widget Logic
            const chatToggle = document.getElementById('chatToggle');
            const chatBox = document.getElementById('chatBox');
            const chatClose = document.getElementById('chatClose');
            const chatInput = document.getElementById('chatInput');
            const chatSend = document.getElementById('chatSend');
            const chatMessages = document.getElementById('chatMessages');
            
            const btnAvatar = document.getElementById('chatBotAvatarBtn');
            const headerAvatar = document.getElementById('chatBotAvatarHeader');
            const botStatus = document.getElementById('chatBotStatus');
            const chatBubble = document.getElementById('chatBotBubble');

            const imgSaludo = '{pfx}assets/img/iaSaludo.png';
            const imgNormal = '{pfx}assets/img/ia.png';
            const imgDurmiendo = '{pfx}assets/img/iaDurmiendo.png';

            let isChatOpen = false;
            let hasGreeted = false;
            let idleTimer = null;
            let waveTimeouts = [];

            const stopWaving = () => {{
                waveTimeouts.forEach(clearTimeout);
                waveTimeouts = [];
                chatBubble.style.opacity = '0';
            }};

            const startWaving = () => {{
                stopWaving();
                if (isChatOpen) return;
                
                chatBubble.style.opacity = '1';
                btnAvatar.src = imgSaludo; // Mano arriba
                
                waveTimeouts.push(setTimeout(() => {{
                    if (!isChatOpen && !btnAvatar.src.includes('Durmiendo')) btnAvatar.src = imgNormal;
                }}, 400)); // Mano abajo
                
                waveTimeouts.push(setTimeout(() => {{
                    if (!isChatOpen && !btnAvatar.src.includes('Durmiendo')) btnAvatar.src = imgSaludo;
                }}, 800)); // Mano arriba
                
                waveTimeouts.push(setTimeout(() => {{
                    if (!isChatOpen && !btnAvatar.src.includes('Durmiendo')) btnAvatar.src = imgNormal;
                    chatBubble.style.opacity = '0';
                }}, 1200)); // Finaliza el saludo en un poco más de 1 segundo
            }};

            const wakeUpBot = () => {{
                if (btnAvatar.src.includes('Durmiendo')) {{
                    btnAvatar.classList.remove('bot-sleep');
                    headerAvatar.src = imgNormal;
                    botStatus.textContent = 'En línea';
                    if (!isChatOpen) {{
                        startWaving();
                    }}
                }}
                resetIdleTimer();
            }};

            const sleepBot = () => {{
                stopWaving();
                btnAvatar.src = imgDurmiendo;
                btnAvatar.classList.add('bot-sleep');
                headerAvatar.src = imgDurmiendo;
                botStatus.textContent = 'Ausente (Zzz...)';
            }};

            const resetIdleTimer = () => {{
                clearTimeout(idleTimer);
                idleTimer = setTimeout(sleepBot, 60000); // 1 minute
            }};

            // Saludo inicial al cargar la página
            startWaving();
            resetIdleTimer();

            // Wake up on any interaction
            document.addEventListener('mousemove', () => {{
                if (btnAvatar.src.includes('Durmiendo')) wakeUpBot();
                resetIdleTimer();
            }});
            document.addEventListener('keydown', () => {{
                if (btnAvatar.src.includes('Durmiendo')) wakeUpBot();
                resetIdleTimer();
            }});

            const toggleChat = () => {{
                isChatOpen = !isChatOpen;
                if (isChatOpen) {{
                    wakeUpBot();
                    stopWaving();
                    btnAvatar.src = imgNormal; // Se queda normal
                    chatBox.classList.add('open');
                    chatToggle.style.transform = 'scale(0)';
                    
                    if (!hasGreeted) {{
                        setTimeout(() => {{
                            addMessage("¡Hola! 👋 Soy la inteligencia artificial de La Farmed. ¿En qué te puedo ayudar hoy?", "bot");
                            hasGreeted = true;
                        }}, 500);
                    }}
                }} else {{
                    chatBox.classList.remove('open');
                    chatToggle.style.transform = 'scale(1)';
                    startWaving(); // Saluda al cerrar el chat
                    resetIdleTimer();
                }}
            }};

            chatToggle.addEventListener('click', toggleChat);
            chatClose.addEventListener('click', toggleChat);

            const addMessage = (text, sender) => {{
                const msgDiv = document.createElement('div');
                msgDiv.className = `chat-message ${{sender}}`;
                msgDiv.textContent = text;
                chatMessages.appendChild(msgDiv);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }};

            const getBotResponse = (msg) => {{
                const lowerMsg = msg.toLowerCase();
                if (lowerMsg.includes('producto') || lowerMsg.includes('linea') || lowerMsg.includes('catálogo')) {{
                    return "Contamos con más de 89 productos divididos en líneas como Antibiótica, Dermatológica, Digestiva, Dolor, Respiratoria y Natural.";
                }} else if (lowerMsg.includes('contacto') || lowerMsg.includes('telefono') || lowerMsg.includes('llamar') || lowerMsg.includes('cotizar')) {{
                    return "Puedes contactarnos al (01) 7192378 o al 984 375 070. También nos encuentras en Av. Encalada 1171, Surco — Lima.";
                }} else if (lowerMsg.includes('cobertura') || lowerMsg.includes('donde') || lowerMsg.includes('lima') || lowerMsg.includes('provincia')) {{
                    return "Tenemos cobertura a nivel nacional. Distribuimos a miles de boticas y farmacias en Lima y provincias garantizando calidad y confianza.";
                }} else if (lowerMsg.includes('hola') || lowerMsg.includes('buenos') || lowerMsg.includes('buenas')) {{
                    return "¡Hola! ¿Cómo te podemos ayudar en La Farmed el día de hoy?";
                }} else {{
                    return "Gracias por escribirnos. Para información más detallada, por favor dale clic al botón 'Cotizar' en el menú principal o llámanos a nuestros números de contacto.";
                }}
            }};

            const handleSend = () => {{
                const text = chatInput.value.trim();
                if (text) {{
                    addMessage(text, 'user');
                    chatInput.value = '';
                    
                    setTimeout(() => {{
                        const response = getBotResponse(text);
                        addMessage(response, 'bot');
                    }}, 1000);
                }}
                resetIdleTimer();
            }};

            chatSend.addEventListener('click', handleSend);
            chatInput.addEventListener('keypress', (e) => {{
                if (e.key === 'Enter') handleSend();
            }});
            
            // Hero Background Slider (for index.html)
            const slides = document.querySelectorAll('.hero-slide');
            if (slides.length > 0) {{
                let currentSlide = 0;
                setInterval(() => {{
                    slides[currentSlide].classList.remove('active');
                    currentSlide = (currentSlide + 1) % slides.length;
                    slides[currentSlide].classList.add('active');
                }}, 3000);
            }}
        }});
    </script>'''
        
        content = content[:start] + new_script
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
            
        print(f'Updated {f}')
