from pathlib import Path
from html import escape

root = Path(__file__).parent / 'dist'

products = [
    dict(
        slug='root-turbo',
        title='MINORI Root Turbo',
        short='Root Turbo',
        day='7–20 ngày sau sạ',
        photo='roots.webp',
        bottle='root-turbo.svg',
        alt='Rễ trắng của lúa non trong đất ruộng',
        number='01',
        overline='Giai đoạn đầu vụ',
        hero='Muốn cây khỏe,<br><em>phải bắt đầu từ rễ.</em>',
        intro='Khoảng 7–20 ngày sau sạ, cây lúa còn non nhưng bộ rễ đã quyết định khả năng hấp thu và sức bật đầu mùa vụ.',
        problem_intro='Ở vùng đất phèn, ruộng làm lúa liên vụ hoặc nhiều rơm rạ, cây dễ gặp những khó khăn ngay từ gốc.',
        problems=['Rễ yếu hoặc nghẹt rễ', 'Ngộ độc hữu cơ', 'Hấp thu phân kém', 'Đẻ nhánh chậm'],
        role='MINORI Root Turbo được định vị là bước kích rễ nhanh, giúp cây có nền rễ khỏe để hấp thu tốt và đẻ nhánh mạnh.',
        flow=['Rễ khỏe', 'Bung rễ trắng', 'Hấp thu tốt', 'Đẻ nhánh mạnh'],
        quote='Muốn lúa khỏe cả vụ, phải cho cây một bộ rễ khỏe ngay từ đầu.',
        next='ultra-grow',
        next_line='Khi rễ đã sẵn sàng, cây cần đủ sức đi đường dài.'
    ),
    dict(
        slug='ultra-grow',
        title='MINORI Ultra Grow',
        short='Ultra Grow',
        day='20–45 ngày sau sạ',
        photo='growth.webp',
        bottle='ultra-grow.svg',
        alt='Ruộng lúa xanh khỏe trong giai đoạn sinh trưởng',
        number='02',
        overline='Giai đoạn giữa vụ',
        hero='Khỏe cây để<br><em>đi đường dài.</em>',
        intro='Sau giai đoạn đẻ nhánh, cây lúa bước vào thời kỳ sinh trưởng mạnh. Bộ rễ tốt là điểm khởi đầu; cây còn cần giữ nhịp phát triển ổn định.',
        problem_intro='Người nông dân cần cây đủ sức đi qua áp lực giữa vụ và sẵn sàng cho giai đoạn làm đòng.',
        problems=['Khỏe rễ, khỏe thân', 'Chịu stress tốt', 'Sinh trưởng ổn định', 'Sẵn sàng làm đòng'],
        role='MINORI Ultra Grow đóng vai trò dưỡng cây, phát triển mạnh và duy trì sức khỏe cây sau bước khởi động bộ rễ.',
        flow=['Khỏe rễ', 'Khỏe cây', 'Tăng sức chống chịu', 'Chuẩn bị làm đòng'],
        quote='Bộ rễ tốt chưa đủ, cây phải đủ sức đi đường dài.',
        next='vo-gao-promax',
        next_line='Khi cây đã lớn khỏe, hành trình chuyển sang nuôi bông và hạt.'
    ),
    dict(
        slug='vo-gao-promax',
        title='MINORI Vô Gạo Pro Max',
        short='Vô Gạo Pro Max',
        day='Từ 40 ngày đến cuối vụ',
        photo='harvest.webp',
        bottle='vo-gao-promax.svg',
        alt='Bông lúa vàng với những hạt lúa đầy',
        number='03',
        overline='Giai đoạn cuối vụ',
        hero='Bông lúa vàng.<br><em>Hạt chắc.</em>',
        intro='Từ đứng cái, làm đòng, trổ đến nuôi hạt, mục tiêu của người nông dân chuyển sang nuôi bông và hoàn thiện hạt.',
        problem_intro='Cuối vụ là lúc cây cần giữ dáng đứng và dồn sức cho bông lúa. Nền công thức định hướng của sản phẩm là Kali + Silic.',
        problems=['Thân cứng, lá đứng', 'Hạn chế đổ ngã', 'Nuôi đòng, tích lũy tinh bột', 'Vô gạo nhanh, hạt chắc'],
        role='MINORI Vô Gạo Pro Max là bước cuối của hành trình, hướng đến cứng cây, nuôi bông, vô gạo và chắc hạt.',
        flow=['Cứng cây', 'Đứng lá', 'Nuôi bông', 'Vô gạo → chắc hạt'],
        quote='Bắt đầu mùa vụ bằng một bộ rễ khỏe. Kết thúc bằng bông lúa vàng và hạt chắc.',
        next='root-turbo',
        next_line='Mùa vụ tiếp theo lại bắt đầu từ một bộ rễ khỏe.'
    ),
]
by_slug = {p['slug']: p for p in products}

def header(active, base='./'):
    items = [
        (f'{base}', 'Trang chủ', 'home'),
        (f'{base}root-turbo/', 'Root Turbo', 'root-turbo'),
        (f'{base}ultra-grow/', 'Ultra Grow', 'ultra-grow'),
        (f'{base}vo-gao-promax/', 'Vô Gạo Pro Max', 'vo-gao-promax')
    ]
    links = '\n          '.join(f'<a href="{href}"{(" aria-current=\"page\"" if active==key else "")}>{text}</a>' for href, text, key in items)
    return f'''  <!-- ================= SITE HEADER ================= -->
  <header class="site-header">
    <div class="wrap header-layout">
      <a class="brand" href="{base}" aria-label="Minori Agritech — Trang chủ">
        <img src="{base}assets/minori-logo.svg" alt="Logo Minori Agritech">
        <span>
          <b>MINORI</b>
          <small>Agriculture Technology</small>
        </span>
      </a>

      <div class="nav-shell">
        <button class="menu-toggle" type="button" aria-controls="main-nav" aria-expanded="false">Menu</button>
        <nav class="main-nav" id="main-nav" aria-label="Điều hướng chính">
          {links}
          <a class="nav-contact" href="{base}lien-he/"{(' aria-current="page"' if active=='contact' else '')}>Liên hệ</a>
        </nav>
      </div>
    </div>
  </header>'''

def footer(base='./'):
    return f'''  <!-- ================= FOOTER ================= -->
  <footer class="footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">
            <strong>MINORI AGRITECH</strong>
            <small>AGRICULTURE TECHNOLOGY</small>
          </div>
          <p>Đồng hành cùng cây lúa từ bộ rễ đến hạt vàng.</p>
          <p>
            FROM THE EARTH • FOR GENERATIONS<br>
            Từ đất lành • Cho muôn đời xanh
          </p>
        </div>

        <div>
          <b>Ba giai đoạn</b>
          <nav aria-label="Sản phẩm">
            <a href="{base}root-turbo/">MINORI Root Turbo</a>
            <a href="{base}ultra-grow/">MINORI Ultra Grow</a>
            <a href="{base}vo-gao-promax/">MINORI Vô Gạo Pro Max</a>
          </nav>
        </div>

        <div>
          <b>Khám phá</b>
          <nav aria-label="Trang thông tin">
            <a href="{base}">Trang chủ</a>
            <a href="{base}lien-he/">Liên hệ</a>
          </nav>
        </div>
      </div>

      <div class="footer-bottom">
        <span>© 2026 Minori Agritech</span>
        <span>TỪ RỄ → ĐẾN CÂY → ĐẾN HẠT</span>
      </div>
    </div>
  </footer>'''

def doc(title, description, active, body, base='./'):
    return f'''<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#b88127">
  <meta name="description" content="{escape(description)}">
  <title>{escape(title)} | Minori Agritech</title>
  <link rel="icon" type="image/svg+xml" href="{base}assets/minori-logo.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="{base}assets/site.css">
  <link rel="stylesheet" href="{base}assets/refinements.css">
  <script>
    if (/iPad|iPhone|iPod|Android/i.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)) {{
      document.documentElement.classList.add('mobile-os');
    }}
  </script>
</head>
<body>

{header(active, base)}

  <!-- ================= MAIN CONTENT ================= -->
  <main id="main-content">
{body}
  </main>

{footer(base)}

  <script src="{base}assets/site.js" defer></script>
</body>
</html>'''

rows = '\n\n'.join(f'''          <!-- Giai đoạn {p['number']}: {p['short']} -->
          <article class="stage-row glass reveal">
            <div class="stage-count">
              <span>{p['number']}</span>
              <small>{p['overline']}</small>
            </div>
            <div class="stage-photo">
              <img src="./assets/{p['photo']}" alt="{p['alt']}" loading="lazy">
            </div>
            <div class="stage-body">
              <div class="stage-day">{p['day']}</div>
              <h3>{p['title']}</h3>
              <p>{'Kích rễ nhanh. Rễ trắng – đẻ nhánh – hấp thu mạnh.' if p['slug']=='root-turbo' else 'Dưỡng cây, phát triển mạnh. Khỏe rễ – khỏe cây – tăng sức chống chịu.' if p['slug']=='ultra-grow' else 'Tối đa hóa tạo hạt. Cứng cây – nuôi đòng – vô gạo – chắc hạt.'}</p>
              <a class="arrow-link" href="./{p['slug']}/" aria-label="Tìm hiểu {escape(p['title'])}">Khám phá sản phẩm</a>
              <div class="stage-product">
                <a class="stage-product-link" href="./{p['slug']}/" aria-label="Xem sản phẩm {escape(p['title'])}">
                  <img src="./assets/{p['bottle']}" alt="{escape(p['title'])}" loading="lazy">
                </a>
              </div>
            </div>
          </article>''' for p in products)

home = f'''    <!-- 1. HERO SECTION -->
    <section class="hero">
      <div class="wrap hero-grid">
        <div class="hero-copy glass">
          <div class="eyebrow">Từ đất lành • Cho muôn đời xanh</div>
          <h1>MINORI – CHO <em>MÙA VỤ TỐT HƠN</em></h1>
          <p class="lead">Đồng hành cùng cây lúa từ bộ rễ đến hạt vàng.</p>
          <p>Một vụ lúa tốt không được quyết định ở ngày thu hoạch. Nó được quyết định từ lúc bộ rễ đầu tiên hình thành.</p>
          <div class="hero-actions">
            <a class="btn" href="#hanh-trinh">Khám phá hành trình</a>
            <a class="btn ghost" href="./root-turbo/">Bắt đầu từ rễ</a>
          </div>
        </div>

        <aside class="hero-aside glass-dark">
          <div class="eyebrow light">Một mùa vụ • Ba điểm rơi</div>
          <div class="aside-number">03</div>
          <h2>Ba sản phẩm.<br>Một hành trình.</h2>
          <div class="mini-rule"></div>
          <p>Rễ khỏe đầu vụ. Cây vững giữa vụ. Hạt chắc cuối vụ.</p>
        </aside>
      </div>

      <div class="scroll-mark">Cuộn để khám phá ↓</div>
    </section>

    <!-- 2. STORY SECTION -->
    <section class="section">
      <div class="wrap story-card glass reveal">
        <div class="story-grid">
          <div>
            <div class="eyebrow section-label">Câu chuyện mùa vụ</div>
            <h2>Ba nỗi lo của người trồng lúa.</h2>
          </div>
          <div>
            <p class="lead">Mỗi vụ lúa bắt đầu bằng những câu hỏi rất đời thường.</p>
            <p>Minori chọn đồng hành đúng những thời điểm cây cần được chăm sóc nhất: khi bén rễ, khi lớn khỏe và khi tạo hạt.</p>
          </div>
        </div>

        <div class="questions">
          <div class="question">
            <b>01</b>
            <p>Làm sao để lúa ra rễ nhanh, đẻ nhánh khỏe?</p>
          </div>
          <div class="question">
            <b>02</b>
            <p>Làm sao để cây khỏe, ít suy, chịu stress tốt?</p>
          </div>
          <div class="question">
            <b>03</b>
            <p>Làm sao để cuối vụ cứng cây, chắc hạt, vô gạo tốt?</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. JOURNEY SECTION -->
    <section class="journey" id="hanh-trinh">
      <div class="wrap">
        <div class="journey-top reveal">
          <div>
            <div class="eyebrow section-label">Bộ sản phẩm Minori đầu tiên</div>
            <h2>Từ khởi đầu xanh<br>đến mùa vàng.</h2>
          </div>
          <p>Chọn đúng sản phẩm ở từng giai đoạn của hành trình cây lúa.</p>
        </div>

        <div class="journey-stack">
{rows}
        </div>

        <div class="journey-end">TỪ RỄ → ĐẾN CÂY → ĐẾN HẠT</div>
      </div>
    </section>

    <!-- 4. MANIFESTO SECTION -->
    <section class="manifesto">
      <div class="wrap manifesto-card glass-dark reveal">
        <div>
          <div class="eyebrow light">Tinh thần Minori</div>
          <blockquote>“Không chỉ là ba chai phân bón. Đây là câu chuyện xuyên suốt một mùa vụ.”</blockquote>
        </div>
        <div>
          <p>Minori mong trở thành thương hiệu đồng hành với người nông dân ở từng giai đoạn của cây trồng. Với cây lúa, hành trình đầu tiên bắt đầu từ rễ và đi đến hạt vàng.</p>
          <div class="manifesto-signature">FROM THE EARTH • FOR GENERATIONS</div>
          <p>Từ đất lành • Cho muôn đời xanh</p>
          <a class="btn gold" href="./lien-he/">Kết nối với Minori</a>
        </div>
      </div>
    </section>'''

(root / 'index.html').write_text(doc('Cho mùa vụ tốt hơn', 'Minori Agritech đồng hành cùng cây lúa từ bộ rễ đến hạt vàng qua ba giai đoạn của mùa vụ.', 'home', home, base='./'), encoding='utf-8')

for p in products:
    nxt = by_slug[p['next']]
    problems = '\n            '.join(f'<div class="problem">{escape(item)}</div>' for item in p['problems'])
    flow = '\n          '.join(f'<div class="flow-step">{escape(item)}</div>' for item in p['flow'])
    body = f'''    <!-- 1. PRODUCT HERO -->
    <section class="product-hero">
      <div class="wrap product-hero-grid">
        <div class="product-hero-copy glass">
          <div class="eyebrow">{p['number']} / {p['overline']}</div>
          <h1>{p['hero']}</h1>
          <div class="stage-chip">{p['day']}</div>
          <p class="lead">{p['intro']}</p>
        </div>

        <div class="product-hero-art">
          <div class="art-photo">
            <img class="photo" src="../assets/{p['photo']}" alt="{p['alt']}">
            <span class="art-label">{p['title']}</span>
          </div>

          <div class="product-bottle-card">
            <!-- Nhấn vào để phóng to hình ảnh scale-fit màn hình -->
            <div class="bottle-window" data-full-img="../assets/{p['bottle']}" role="button" tabindex="0" title="Nhấn để phóng to hình ảnh">
              <img src="../assets/{p['bottle']}" alt="Mặt trước chai {escape(p['title'])}" loading="lazy">
              <span class="zoom-badge">🔍 Phóng to</span>
            </div>
            <div class="bottle-caption">
              <span>Sản phẩm Minori</span>
              <strong>{p['title']}</strong>
              <small>{p['day']}</small>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. FULL VIEW SECTION: Hiển thị đầy đủ hình ảnh sản phẩm scale fit chiều rộng trang web -->
    <section class="product-full-view">
      <div class="wrap">
        <div class="product-full-card glass reveal">
          <div class="full-view-header">
            <div class="eyebrow section-label">Bao bì & Nhãn chi tiết</div>
            <h2>Hình ảnh đầy đủ {escape(p['title'])}</h2>
            <p class="lead">Bao bì chuẩn nhận diện và thông số nhãn của {escape(p['short'])}.</p>
          </div>
          <div class="full-view-artwork">
            <img src="../assets/{p['bottle']}" alt="Hình ảnh đầy đủ {escape(p['title'])}" loading="lazy">
          </div>
        </div>
      </div>
    </section>

    <!-- 3. DETAIL / ĐIỂM RƠI MÙA VỤ -->
    <section class="detail-section" id="vai-tro">
      <div class="wrap detail-grid glass reveal">
        <div>
          <div class="eyebrow section-label">Điểm rơi mùa vụ</div>
          <h2>{p['overline']} cần điều gì?</h2>
        </div>
        <div>
          <p class="lead">{p['problem_intro']}</p>
          <p>{p['role']}</p>
          <div class="problem-grid">
            {problems}
          </div>
        </div>
      </div>
    </section>

    <!-- 4. EFFECT / VAI TRÒ SẢN PHẨM -->
    <section class="effect-section">
      <div class="wrap effect-card glass-dark reveal">
        <div class="eyebrow light" style="justify-content:center">Vai trò của {p['short']}</div>
        <h2>{p['title']}</h2>
        <div class="flow">
          {flow}
        </div>
        <blockquote>“{p['quote']}”</blockquote>
      </div>
    </section>

    <!-- 5. NEXT STAGE -->
    <section class="next">
      <div class="wrap next-card glass reveal">
        <div>
          <div class="eyebrow">Tiếp nối mùa vụ</div>
          <h2>{p['next_line']}</h2>
          <p>{'Khám phá giai đoạn dưỡng cây với MINORI Ultra Grow.' if p['slug']=='root-turbo' else 'Khám phá giai đoạn nuôi bông, vô gạo với MINORI Vô Gạo Pro Max.' if p['slug']=='ultra-grow' else 'Quay lại bước khởi đầu với MINORI Root Turbo hoặc liên hệ Minori.'}</p>
        </div>
        <a class="btn" href="../{nxt['slug']}/">Xem {nxt['short']}</a>
      </div>
    </section>'''
    (root / p['slug'] / 'index.html').write_text(doc(p['title'], p['role'], p['slug'], body, base='../'), encoding='utf-8')

contact = '''    <!-- CONTACT SECTION -->
    <section class="contact">
      <div class="wrap contact-grid">
        <div class="contact-copy glass">
          <div class="eyebrow">Kết nối với Minori</div>
          <h1>Cùng bắt đầu một <em>mùa vụ tốt hơn.</em></h1>
          <p class="lead">Bạn đang quan tâm đến giai đoạn nào của cây lúa? Hãy chuẩn bị lời nhắn cho Minori Agritech.</p>
          <div class="contact-warning">
            <strong>Biểu mẫu tạm</strong><br>
            Chức năng tiếp nhận liên hệ đang được chuẩn bị. Thông tin nhập vào đây hiện chưa được lưu hoặc gửi đến Minori.
          </div>
        </div>

        <form class="contact-form glass" id="contact-form">
          <div class="field-row">
            <div class="field">
              <label for="name">Họ và tên *</label>
              <input id="name" name="name" autocomplete="name" required placeholder="Tên của bạn">
            </div>
            <div class="field">
              <label for="phone">Số điện thoại *</label>
              <input id="phone" name="phone" type="tel" autocomplete="tel" required placeholder="Số điện thoại liên hệ">
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="email">Email</label>
              <input id="email" name="email" type="email" autocomplete="email" placeholder="Địa chỉ email (nếu có)">
            </div>
            <div class="field">
              <label for="region">Khu vực canh tác</label>
              <input id="region" name="region" placeholder="Tỉnh / thành phố">
            </div>
          </div>
          <div class="field">
            <label for="message">Lời nhắn *</label>
            <textarea id="message" name="message" required placeholder="Bạn muốn tìm hiểu điều gì về sản phẩm hoặc mùa vụ?"></textarea>
          </div>
          <button class="btn" type="submit">Kiểm tra lời nhắn</button>
          <p class="fine">Đây là bản xem trước giao diện. Biểu mẫu chưa gửi dữ liệu.</p>
          <div class="form-status" id="form-status" aria-live="polite"></div>
        </form>
      </div>
    </section>'''

(root / 'lien-he' / 'index.html').write_text(doc('Liên hệ', 'Biểu mẫu liên hệ tạm cho khách quan tâm đến sản phẩm và hành trình mùa vụ của Minori Agritech.', 'contact', contact, base='../'), encoding='utf-8')
print('Built', len(products) + 2, 'pages with clean layout & new requirements')
