import random

# 1. Havuz (İstenilen eklemeler yapıldı, istenmeyenler çıkarıldı)
logo_pool = [
    # Çekirdek & Veri Bilimi
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/anaconda/anaconda-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matlab/matlab-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/r/r-original.svg",
    "https://seaborn.pydata.org/_images/logo-mark-lightbg.svg", # Seaborn Resmi Logo
    
    # Derin Öğrenme, Yapay Zeka ve Görüntü İşleme
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tensorflow/tensorflow-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytorch/pytorch-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/keras/keras-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opencv/opencv-original.svg",
    "https://huggingface.co/front/assets/huggingface_logo-noborder.svg",
    
    # Araçlar, Diller ve Veritabanları
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/c/c-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/googlecloud/googlecloud-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azuresqldatabase/azuresqldatabase-original.svg", # SQL Temsilcisi
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg"
]

def draw_robot(x_offset, y_position, logo_url, direction):
    # Sola giden robotların gövdesini aynalayarak (flip) ters çeviriyoruz
    flip_transform = 'transform="translate(50, 0) scale(-1, 1)"' if direction == -1 else ''
    
    return f"""
    <g transform="translate({x_offset}, {y_position})">
        <!-- Robot Gövdesi (Sola gidiyorsa flip_transform ile yön değiştirir) -->
        <g {flip_transform}>
            <ellipse cx="25" cy="75" rx="35" ry="6" fill="#1A202C" opacity="0.6" />
            
            <rect x="-10" y="55" width="70" height="16" rx="8" fill="#2D3748" stroke="#1A202C" stroke-width="2"/>
            <line x1="-5" y1="63" x2="55" y2="63" stroke="#4A5568" stroke-width="4" stroke-dasharray="4 4">
                <animate attributeName="stroke-dashoffset" from="8" to="0" dur="0.5s" repeatCount="indefinite"/>
            </line>

            <path d="M 0 55 L 5 25 L 45 25 L 50 55 Z" fill="#E2E8F0" stroke="#A0AEC0" stroke-width="2"/>
            <rect x="15" y="30" width="20" height="10" rx="2" fill="#CBD5E0" />
            
            <rect x="2" y="0" width="46" height="28" rx="4" fill="#1A202C" />
            <circle cx="15" cy="14" r="5" fill="#68D391" />
            <circle cx="35" cy="14" r="5" fill="#68D391" />
            <rect x="10" y="9" width="30" height="10" fill="#1A202C" opacity="0">
                <animate attributeName="opacity" values="0;0;1;0;0" dur="4s" repeatCount="indefinite"/>
            </rect>
            
            <path d="M -5 40 L -25 10 L -5 -15" stroke="#718096" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M 55 40 L 75 10 L 55 -15" stroke="#718096" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            
            <ellipse cx="25" cy="-15" rx="38" ry="10" fill="#4FD1C5" opacity="0.8" />
            <ellipse cx="25" cy="-15" rx="30" ry="6" fill="#E6FFFA" />
            <path d="M -10 -15 L 60 -15" stroke="#319795" stroke-width="2" opacity="0.5"/>
        </g>
        
        <!-- Havada Süzülen Logo (Logolar yön değiştirmez, her zaman düz durur) -->
        <g>
            <animateTransform 
                attributeName="transform" 
                type="translate" 
                values="0 0; 0 -8; 0 0" 
                dur="2s" 
                repeatCount="indefinite" 
            />
            <image href="{logo_url}" x="5" y="-55" width="40" height="40" preserveAspectRatio="xMidYMid meet" />
        </g>
    </g>
    """

def build_lane(logos, y_position, direction):
    # Kesintisiz (Carousel) Animasyon Mantığı
    D = 220  # Robotlar arası mesafe
    N = len(logos)
    L = N * D  # Tüm katarın (trenin) toplam uzunluğu
    speed = 50  # Saniyede gidilen piksel
    dur = L / speed
    
    # Yön hesaplamaları
    if direction == 1: # Soldan Sağa
        anim_from = 0
        anim_to = L
        copy2_offset = -L # İkinci katar ekranın solundan girer
    else:              # Sağdan Sola
        anim_from = 0
        anim_to = -L
        copy2_offset = L  # İkinci katar ekranın sağından girer
        
    lane_html = f"""
    <g>
        <animateTransform 
            attributeName="transform" 
            type="translate" 
            from="{anim_from} 0" 
            to="{anim_to} 0" 
            dur="{dur:.1f}s" 
            repeatCount="indefinite" 
        />
    """
    
    # Ekranın boş kalmaması için aynı katarı 2 kez arka arkaya yerleştiriyoruz
    for copy_idx in range(2):
        offset_base = 0 if copy_idx == 0 else copy2_offset
        for i, logo_url in enumerate(logos):
            x_pos = offset_base + (i * D)
            lane_html += draw_robot(x_pos, y_position, logo_url, direction)
            
    lane_html += "</g>"
    return lane_html

def generate_svg():
    # Her gün sıralamanın farklı olması için havuzu bir kez karıştır
    random.shuffle(logo_pool)
    
    # Havuzu iki şeride paylaştır
    half = len(logo_pool) // 2
    top_logos = logo_pool[:half]
    bottom_logos = logo_pool[half:]

    svg_header = """<svg width="800" height="300" viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg">
        <style>
            .asphalt { fill: #2D3748; }
            .stripe { stroke: #ECC94B; stroke-width: 4; stroke-dasharray: 20 20; }
            .bg { fill: #171923; }
        </style>
        
        <rect class="bg" width="800" height="300" rx="15" />
        
        <!-- Üst Şerit (Soldan Sağa) -->
        <rect class="asphalt" x="0" y="60" width="800" height="80" />
        <line class="stripe" x1="0" y1="100" x2="800" y2="100" />
        
        <!-- Alt Şerit (Sağdan Sola) -->
        <rect class="asphalt" x="0" y="170" width="800" height="80" />
        <line class="stripe" x1="0" y1="210" x2="800" y2="210" />
    """
    
    # Şeritleri Oluştur ve Ekle
    robots_html = build_lane(top_logos, y_position=55, direction=1)
    robots_html += build_lane(bottom_logos, y_position=165, direction=-1)

    svg_footer = "</svg>"
    
    with open("robot-animasyon.svg", "w", encoding="utf-8") as file:
        file.write(svg_header + robots_html + svg_footer)

if __name__ == "__main__":
    generate_svg()
    print("Karusel sistemli robot-animasyon.svg başarıyla oluşturuldu!")