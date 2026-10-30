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
        bottle='minori-ultra-grow.svg',
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

# Lựa chọn thứ hai của giai đoạn giữa vụ (02). Trang riêng được dựng ở cuối file.
leaf = dict(
    slug='duong-cay-khoe-la',
    title='MINORI Dưỡng Cây Khỏe Lá',
    short='Dưỡng Cây Khỏe Lá',
    bottle='minori-duong-cay-khoe-la.svg',
    tagline='Bổ sung lân kali, dưỡng lá khỏe, cây vững giữa vụ.',
)

# Hai thẻ lựa chọn trong article giai đoạn 02 của trang chủ.
mid_choices = [
    dict(slug=leaf['slug'], title=leaf['title'], bottle=leaf['bottle'], tag='Lân – Kali giữa vụ',
         desc=leaf['tagline'], alt='Chai MINORI Dưỡng Cây Khỏe Lá 500 ml – phân bón lá hỗn hợp PK', premium=False),
    dict(slug='ultra-grow', title='MINORI Ultra Grow', bottle='minori-ultra-grow.svg', tag='Dòng chuyên sâu',
         desc='Công thức potassium phosphite, chăm cây chuyên sâu giữa vụ.',
         alt='Chai MINORI Ultra Grow 500 ml – potassium phosphite', premium=True),
]

def header(active, base='./'):
    items = [
        (f'{base}', 'Trang chủ', 'home'),
        (f'{base}root-turbo/', 'Root Turbo - Kích Rễ', 'root-turbo'),
        (f'{base}ultra-grow/', 'Ultra Grow - Khỏe Cây', 'ultra-grow'),
        (f'{base}duong-cay-khoe-la/', 'Dưỡng Cây Khỏe Lá', 'duong-cay-khoe-la'),
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
          <b>Ba giai đoạn • Bốn lựa chọn</b>
          <nav aria-label="Sản phẩm">
            <a href="{base}root-turbo/">MINORI Root Turbo</a>
            <a href="{base}ultra-grow/">MINORI Ultra Grow</a>
            <a href="{base}duong-cay-khoe-la/">MINORI Dưỡng Cây Khỏe Lá</a>
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

SITE = 'https://minorivn.com/'

def doc(title, description, active, body, base='./', path=None, head_extra=''):
    canonical = f'\n  <link rel="canonical" href="{SITE}{path}">' if path is not None else ''
    return f'''<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#b88127">
  <meta name="description" content="{escape(description)}">
  <title>{escape(title)} | Minori Agritech</title>{canonical}
  <link rel="icon" type="image/svg+xml" href="{base}assets/minori-logo.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="{base}assets/site.css">
  <link rel="stylesheet" href="{base}assets/refinements.css">
  <script>
    if (/iPad|iPhone|iPod|Android/i.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)) {{
      document.documentElement.classList.add('mobile-os');
    }}
  </script>{head_extra}
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

def stage_body(p):
    """Nội dung cột phải của mỗi article trong hành trình."""
    if p['number'] == '02':
        cards = '\n'.join(f'''                <a class="choice-card{' choice-card--premium' if c['premium'] else ''}" href="./{c['slug']}/">
                  <span class="choice-thumb"><img src="./assets/{c['bottle']}" alt="{escape(c['alt'])}" loading="lazy"></span>
                  <span class="choice-text">
                    <span class="choice-tag">{escape(c['tag'])}</span>
                    <strong class="choice-name">{escape(c['title'])}</strong>
                    <span class="choice-desc">{escape(c['desc'])}</span>
                    <span class="choice-cta">Khám phá sản phẩm<span class="choice-cta-arrow" aria-hidden="true"> →</span></span>
                  </span>
                </a>''' for c in mid_choices)
        return f'''              <div class="stage-day">{p['day']}</div>
              <h3>Hai lựa chọn dưỡng cây giữa vụ</h3>
              <p>Giữ cây khỏe, bộ lá hoạt động tốt để sẵn sàng bước vào làm đòng.</p>
              <div class="stage-choices">
{cards}
              </div>'''
    blurb = 'Kích rễ nhanh. Rễ trắng – đẻ nhánh – hấp thu mạnh.' if p['slug'] == 'root-turbo' else 'Tối đa hóa tạo hạt. Cứng cây – nuôi đòng – vô gạo – chắc hạt.'
    return f'''              <div class="stage-day">{p['day']}</div>
              <h3>{p['title']}</h3>
              <p>{blurb}</p>
              <a class="arrow-link" href="./{p['slug']}/" aria-label="Tìm hiểu {escape(p['title'])}">Khám phá sản phẩm</a>
              <div class="stage-product">
                <a class="stage-product-link" href="./{p['slug']}/" aria-label="Xem sản phẩm {escape(p['title'])}">
                  <img src="./assets/{p['bottle']}" alt="{escape(p['title'])}" loading="lazy">
                </a>
              </div>'''

rows = '\n\n'.join(f'''          <!-- Giai đoạn {p['number']}: {'Hai lựa chọn giữa vụ' if p['number'] == '02' else p['short']} -->
          <article class="stage-row glass reveal{' stage-row--choices' if p['number'] == '02' else ''}">
            <div class="stage-count">
              <span>{p['number']}</span>
              <small>{p['overline']}</small>
            </div>
            <div class="stage-photo">
              <img src="./assets/{p['photo']}" alt="{p['alt']}" loading="lazy">
            </div>
            <div class="stage-body">
{stage_body(p)}
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
          <h2>Ba giai đoạn.<br>Bốn lựa chọn.<br>Một hành trình.</h2>
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
          <blockquote>“Không chỉ là những chai phân bón. Đây là câu chuyện xuyên suốt một mùa vụ.”</blockquote>
        </div>
        <div>
          <p>Minori mong trở thành thương hiệu đồng hành với người nông dân ở từng giai đoạn của cây trồng. Với cây lúa, hành trình đầu tiên bắt đầu từ rễ và đi đến hạt vàng.</p>
          <div class="manifesto-signature">FROM THE EARTH • FOR GENERATIONS</div>
          <p>Từ đất lành • Cho muôn đời xanh</p>
          <a class="btn gold" href="./lien-he/">Kết nối với Minori</a>
        </div>
      </div>
    </section>'''

(root / 'index.html').write_text(doc('Cho mùa vụ tốt hơn', 'Minori Agritech đồng hành cùng cây lúa từ bộ rễ đến hạt vàng qua ba giai đoạn của mùa vụ.', 'home', home, base='./', path=''), encoding='utf-8')

for p in products:
    if p['slug'] == 'root-turbo':
        # Root Turbo page has been upgraded to a dedicated rich showcase page with composition, Japan tech, field guide, and FAQ
        continue
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
          <div class="full-view-artwork" data-full-img="../assets/{p['bottle']}" role="button" tabindex="0" title="Nhấn để phóng to hình ảnh">
            <img src="../assets/{p['bottle']}" alt="Hình ảnh đầy đủ {escape(p['title'])}" loading="lazy">
            <span class="zoom-badge zoom-badge--full">🔍 Nhấn để phóng to</span>
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
          <p>{'Khám phá giai đoạn dưỡng cây với MINORI Ultra Grow.' if p['slug']=='root-turbo' else 'Khám phá giai đoạn nuôi bông, vô gạo với MINORI Vô Gạo Pro Max.' if p['slug']=='ultra-grow' else 'Quay lại bước khởi đầu với MINORI Root Turbo hoặc liên hệ Minori.'}</p>{f"""
          <p class="next-sibling">Cùng giai đoạn giữa vụ: <a href="../{leaf['slug']}/">{leaf['title']}</a> – {escape(leaf['tagline'][0].lower() + leaf['tagline'][1:])}</p>""" if p['slug']=='ultra-grow' else ''}
        </div>
        <a class="btn" href="../{nxt['slug']}/">Xem {nxt['short']}</a>
      </div>
    </section>'''
    (root / p['slug'] / 'index.html').write_text(doc(p['title'], p['role'], p['slug'], body, base='../', path=f"{p['slug']}/"), encoding='utf-8')

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

(root / 'lien-he' / 'index.html').write_text(doc('Liên hệ', 'Biểu mẫu liên hệ tạm cho khách quan tâm đến sản phẩm và hành trình mùa vụ của Minori Agritech.', 'contact', contact, base='../', path='lien-he/'), encoding='utf-8')

# ================================================================
# Trang MINORI Dưỡng Cây Khỏe Lá (/duong-cay-khoe-la/)
# Nội dung chọn lọc từ minori-duong-cay-khoe-la-bai-gioi-thieu.md.
# Nhãn Minori đang chờ phê duyệt: chỉ dùng số liệu trong phần bài viết công khai,
# không hiển thị phần "Lưu ý biên tập" và không tạo Product/FAQ schema.
# ================================================================
leaf_faq = [
    ('MINORI Dưỡng Cây Khỏe Lá có thành phần chính nào?',
     'Nhãn Minori dự kiến ghi lân hữu hiệu (P₂O₅) <strong>31%</strong> và kali hữu hiệu (K₂O) <strong>23%</strong>. Đây là phân bón lá hỗn hợp PK.'),
    ('Lân và kali giúp gì cho cây lúa?',
     'Lân hỗ trợ chuyển hóa năng lượng, phát triển rễ và nhánh; kali góp phần điều tiết nước và duy trì hoạt động quang hợp của lá. Kết hợp hai dưỡng chất giúp cây có nền dinh dưỡng cân đối khi bước vào giai đoạn làm đòng.'),
    ('Khi nào dùng cho lúa?',
     'Theo nhãn Minori dự kiến, thời điểm phun bắt đầu lúc lúa làm đòng, trước và sau khi trổ đều. Cần nhận diện đúng giai đoạn sinh trưởng của giống lúa tại ruộng, thay vì chỉ tính theo số ngày sau sạ.'),
    ('Pha và phun như thế nào?',
     'Hướng dẫn trên nhãn dự kiến ghi <strong>25–30 ml cho bình 25 lít nước</strong>, phun <strong>2 bình/1.000 m²</strong>. Phun đều ướt tán lá và làm theo hướng dẫn trên nhãn chính thức của sản phẩm.'),
]
leaf_faq_html = '\n\n'.join(f'''            <details class="faq-item">
              <summary class="faq-question">
                <span>{i}. {escape(q)}</span>
                <span class="faq-toggle-icon" aria-hidden="true">+</span>
              </summary>
              <div class="faq-answer">
                <p>{a}</p>
              </div>
            </details>''' for i, (q, a) in enumerate(leaf_faq, 1))

leaf_url = f"{SITE}{leaf['slug']}/"
leaf_title = 'MINORI Dưỡng Cây Khỏe Lá – Vững cây, khỏe lá giữa vụ'
leaf_desc = 'MINORI Dưỡng Cây Khỏe Lá – phân bón lá hỗn hợp PK với lân hữu hiệu (P₂O₅) 31% và kali hữu hiệu (K₂O) 23%, dưỡng lá khỏe, cây vững giai đoạn giữa vụ lúa.'
leaf_head = f'''

  <!-- Schema.org: chỉ WebPage + Breadcrumb. Product/FAQ schema bổ sung sau khi nhãn được phê duyệt. -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "@id": "{leaf_url}#webpage",
    "url": "{leaf_url}",
    "name": "{leaf_title} | Minori Agritech",
    "description": "{leaf_desc}",
    "breadcrumb": {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "{SITE}" }},
        {{ "@type": "ListItem", "position": 2, "name": "Dưỡng Cây Khỏe Lá", "item": "{leaf_url}" }}
      ]
    }}
  }}
  </script>'''

leaf_body = f'''
    <!-- 1. PRODUCT HERO -->
    <section class="product-hero">
      <div class="wrap product-hero-grid">
        <div class="product-hero-copy glass">
          <div class="eyebrow">02 / Giai đoạn giữa vụ (20–45 ngày sau sạ)</div>
          <h1>MINORI Dưỡng Cây Khỏe Lá<br><em>Vững cây, khỏe lá giữa vụ</em></h1>
          <div class="stage-chip">Dưỡng đúng nhịp phát triển</div>
          <p class="lead">Sau khi bén rễ, lúa bước vào đẻ nhánh, mở rộng tán lá và tích lũy sức để chuyển sang làm đòng. MINORI Dưỡng Cây Khỏe Lá là phân bón lá hỗn hợp PK được Minori Agritech định vị cho nhịp phát triển ấy.</p>
        </div>

        <div class="product-hero-art">
          <div class="art-photo">
            <img class="photo" src="../assets/growth.webp" alt="Ruộng lúa xanh đồng đều trong giai đoạn giữa vụ">
            <span class="art-label">MINORI Dưỡng Cây Khỏe Lá</span>
          </div>

          <div class="product-bottle-card">
            <!-- Nhấn vào để phóng to hình ảnh scale-fit màn hình -->
            <div class="bottle-window" data-full-img="../assets/{leaf['bottle']}" role="button" tabindex="0" title="Nhấn để phóng to hình ảnh">
              <img src="../assets/{leaf['bottle']}" alt="Mặt trước chai MINORI Dưỡng Cây Khỏe Lá 500 ml" loading="lazy">
              <span class="zoom-badge">🔍 Phóng to</span>
            </div>
            <div class="bottle-caption">
              <span>Phân bón lá hỗn hợp PK</span>
              <strong>MINORI Dưỡng Cây Khỏe Lá</strong>
              <small>Giai đoạn giữa vụ</small>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. FULL VIEW: hình ảnh đầy đủ bao bì -->
    <section class="product-full-view">
      <div class="wrap">
        <div class="product-full-card glass reveal">
          <div class="full-view-header">
            <div class="eyebrow section-label">Bao bì &amp; Nhãn chi tiết</div>
            <h2>Hình ảnh đầy đủ MINORI Dưỡng Cây Khỏe Lá</h2>
            <p class="lead">Ba mặt chai 500 ml: thành phần &amp; hướng dẫn sử dụng, mặt chính và ưu điểm nổi bật.</p>
          </div>
          <div class="full-view-artwork" data-full-img="../assets/{leaf['bottle']}" role="button" tabindex="0" title="Nhấn để phóng to hình ảnh">
            <img src="../assets/{leaf['bottle']}" alt="Ba mặt chai MINORI Dưỡng Cây Khỏe Lá 500 ml – phân bón lá hỗn hợp PK" loading="lazy">
            <span class="zoom-badge zoom-badge--full">🔍 Nhấn để phóng to</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. ĐIỂM RƠI MÙA VỤ -->
    <section class="detail-section" id="giua-vu">
      <div class="wrap detail-grid glass reveal">
        <div>
          <div class="eyebrow section-label">Điểm rơi mùa vụ</div>
          <h2>Giữa vụ, cây lúa cần điều gì?</h2>
        </div>
        <div>
          <p class="lead">Khoảng 20–45 ngày sau sạ là khung theo dõi giữa vụ thường gặp; thời điểm thực tế thay đổi theo giống, mùa vụ và điều kiện ruộng.</p>
          <p>Đây là lúc cây cần bộ lá hoạt động tốt để tạo chất khô, đồng thời duy trì dinh dưỡng cân đối cho thân, rễ và những nhánh đang hình thành. Thời điểm phun sản phẩm cho lúa cần theo mốc sinh trưởng ghi trên nhãn Minori.</p>
          <div class="problem-grid">
            <div class="problem">Đẻ nhánh hữu hiệu</div>
            <div class="problem">Mở rộng tán lá</div>
            <div class="problem">Duy trì quang hợp</div>
            <div class="problem">Chuẩn bị làm đòng</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. THÀNH PHẦN & CƠ CHẾ KHOA HỌC -->
    <section class="composition-section" id="thanh-phan">
      <div class="wrap">
        <div class="composition-card-wrap glass reveal">
          <div class="composition-header">
            <div class="eyebrow section-label" style="justify-content:center">Phân bón lá hỗn hợp PK</div>
            <h2>Lân và kali cho giai đoạn giữa vụ</h2>
            <p class="lead">Hàm lượng theo nhãn Minori dự kiến của sản phẩm, tập trung vào phát triển rễ, nhánh và hoạt động của tán lá.</p>
          </div>

          <div class="composition-grid composition-grid--two">
            <div class="nutrient-card">
              <div class="nutrient-val">31%</div>
              <div class="nutrient-name">Lân hữu hiệu</div>
              <div class="nutrient-en">P₂O₅</div>
              <p class="nutrient-desc">Gắn với quá trình dự trữ, chuyển giao năng lượng trong cây; hỗ trợ rễ phát triển, cây đẻ nhánh và duy trì tốc độ sinh trưởng.</p>
            </div>

            <div class="nutrient-card">
              <div class="nutrient-val">23%</div>
              <div class="nutrient-name">Kali hữu hiệu</div>
              <div class="nutrient-en">K₂O</div>
              <p class="nutrient-desc">Tham gia điều tiết nước trong tế bào, hoạt động của khí khổng và enzyme; giúp lá duy trì trạng thái thuận lợi cho quang hợp.</p>
            </div>
          </div>

          <details class="research-expandable">
            <summary class="research-summary">
              <span>Lân và kali hỗ trợ cây lúa như thế nào? (Cơ chế khoa học)</span>
              <span class="summary-indicator">
                <span>Xem chi tiết / Thu gọn</span>
                <span class="summary-chevron" aria-hidden="true">▼</span>
              </span>
            </summary>
            <div class="research-body">
              <p class="research-intro">Các tài liệu nông học ghi nhận vai trò của từng dưỡng chất đối với cây lúa giai đoạn giữa vụ:</p>

              <div class="research-list">
                <div class="research-item">
                  <strong>Lân hữu hiệu 31%:</strong> Tài liệu kỹ thuật của PhilRice nêu rõ vai trò của lân đối với rễ và nhánh lúa; nghiên cứu trên cây lúa cũng ghi nhận thiếu lân có thể làm giảm diện tích lá, số nhánh và sinh khối. Vì thế, chăm dinh dưỡng lân là một phần quan trọng khi cây đang xây dựng tán lá và số nhánh hữu hiệu. [2][3]
                </div>
                <div class="research-item">
                  <strong>Kali hữu hiệu 23%:</strong> Khi được cung cấp cân đối, kali giúp lá duy trì trạng thái sinh lý thuận lợi cho quang hợp và vận chuyển sản phẩm quang hợp đến các bộ phận đang lớn. Nghiên cứu trên lúa cho thấy thiếu kali làm giảm tốc độ quang hợp của lá; PhilRice cũng ghi nhận kali góp phần tăng diện tích lá và sức sinh trưởng của cây. [2][4]
                </div>
                <div class="research-item">
                  <strong>Kết hợp lân và kali qua lá:</strong> Một nghiên cứu thực địa trên lúa tại Iran ghi nhận việc bổ sung dinh dưỡng qua lá ở giai đoạn đẻ nhánh và bắt đầu làm đòng có ảnh hưởng tích cực đến số nhánh, diệp lục, diện tích lá và sinh trưởng. Nghiên cứu dùng công thức khác, không phải thử nghiệm sản phẩm Minori. [5]
                </div>
              </div>

              <div class="reference-links">
                <h3 class="reference-title">Tài liệu khoa học tham khảo</h3>
                <ol>
                  <li><a href="https://webapps.irri.org/in/od/rcm/questionnaires/BlankRecommendationPage.pdf" target="_blank" rel="noopener noreferrer">IRRI – Rice growth stages and critical stages by variety</a>: thời điểm đẻ nhánh và làm đòng cần xét theo giống, ngày sạ và điều kiện ruộng.</li>
                  <li><a href="https://www.pinoyrice.com/palaycheck/nutrient-management/" target="_blank" rel="noopener noreferrer">PhilRice – Nutrient Management, PalayCheck</a>: vai trò của lân, kali và yêu cầu dinh dưỡng từ đẻ nhánh đến bắt đầu làm đòng.</li>
                  <li><a href="https://link.springer.com/article/10.1186/s12870-021-03015-4" target="_blank" rel="noopener noreferrer">BMC Plant Biology – phosphate deficiency in rice</a>: ảnh hưởng của thiếu lân đến sinh trưởng, nhánh và lá lúa.</li>
                  <li><a href="https://pubmed.ncbi.nlm.nih.gov/18251852/" target="_blank" rel="noopener noreferrer">Weng và cộng sự, Physiologia Plantarum (2007)</a>: quang hợp lá lúa khi thiếu kali.</li>
                  <li><a href="https://doi.org/10.5586/aa.7332" target="_blank" rel="noopener noreferrer">Mahmoodi và cộng sự, Acta Agrobotanica (2020)</a>: thử nghiệm phân bón lá NPK và vi lượng trên lúa tại nhiều giai đoạn.</li>
                </ol>
                <p class="research-disclaimer">
                  <em>* Các tài liệu trên giải thích vai trò của lân, kali và dinh dưỡng qua lá nói chung; không phải khảo nghiệm hiệu quả riêng của MINORI Dưỡng Cây Khỏe Lá.</em>
                </p>
              </div>
            </div>
          </details>
        </div>
      </div>
    </section>

    <!-- 5. VAI TRÒ SẢN PHẨM -->
    <section class="effect-section">
      <div class="wrap effect-card glass-dark reveal">
        <div class="eyebrow light" style="justify-content:center">Vai trò của Dưỡng Cây Khỏe Lá</div>
        <h2>Nền dinh dưỡng vững trước chặng làm đòng</h2>
        <div class="flow">
          <div class="flow-step">Rễ &amp; nhánh</div>
          <div class="flow-step">Tán lá khỏe</div>
          <div class="flow-step">Quang hợp ổn định</div>
          <div class="flow-step">Sẵn sàng làm đòng</div>
        </div>
        <blockquote>“Dưỡng cây khỏe hôm nay để ruộng lúa có nền phát triển vững vàng cho chặng tiếp theo.”</blockquote>
      </div>
    </section>

    <!-- 6. CHĂM LÚA ĐÚNG NHỊP -->
    <section class="field-guide-section" id="cach-dung">
      <div class="wrap">
        <div class="field-guide-card glass reveal">
          <div class="field-guide-header">
            <div class="eyebrow section-label">Chăm lúa giữa vụ</div>
            <h2>Dưỡng cây đúng nhịp, chăm ruộng bền sức</h2>
            <p class="lead">MINORI Dưỡng Cây Khỏe Lá là lựa chọn bổ sung lân và kali trong chương trình chăm lúa, đi cùng quản lý nước và bón phân gốc cân đối.</p>
          </div>

          <div class="field-guide-grid">
            <div class="guide-step">
              <div class="step-num">01</div>
              <div class="step-body">
                <h3>Theo dõi ruộng giữa vụ</h3>
                <p>Quan sát độ đồng đều của ruộng, số nhánh hữu hiệu, diện tích và tình trạng bộ lá. Lá phát triển tốt giúp cây duy trì khả năng đón ánh sáng; nhánh khỏe tạo tiền đề cho giai đoạn hình thành bông.</p>
              </div>
            </div>

            <div class="guide-step">
              <div class="step-num">02</div>
              <div class="step-body">
                <h3>Phun theo mốc sinh trưởng trên nhãn</h3>
                <p>Nhãn Minori dự kiến hướng dẫn phun cho lúa từ lúc bắt đầu làm đòng, trước và sau khi trổ đều. Khung 20–45 ngày sau sạ là nhịp quan sát giữa vụ, không phải lịch phun cố định cho mọi giống. [1]</p>
              </div>
            </div>

            <div class="guide-step">
              <div class="step-num">03</div>
              <div class="step-body">
                <h3>Pha đúng liều, phun đều tán lá</h3>
                <p>Liều dự kiến trên nhãn: 25–30 ml cho bình 25 lít nước, phun 2 bình/1.000 m², phun đều ướt tán lá. Luôn làm theo liều lượng, thời điểm và cách phun trên nhãn chính thức của sản phẩm.</p>
              </div>
            </div>

            <div class="guide-step">
              <div class="step-num">04</div>
              <div class="step-body">
                <h3>Kết hợp quản lý nước &amp; phân gốc</h3>
                <p>Phân bón lá không thay thế kế hoạch bón phân gốc. Cần kết hợp quản lý nước và bón phân cân đối để cây đi qua giai đoạn giữa vụ đều và khỏe.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. FAQ -->
    <section class="faq-section" id="faq">
      <div class="wrap">
        <div class="faq-card glass reveal">
          <div class="faq-header">
            <div class="eyebrow section-label" style="justify-content:center">Hỏi đáp kỹ thuật</div>
            <h2>Câu hỏi thường gặp về MINORI Dưỡng Cây Khỏe Lá</h2>
            <p class="lead">Những thắc mắc phổ biến khi chăm lúa giai đoạn giữa vụ.</p>
          </div>

          <div class="faq-list">
{leaf_faq_html}
          </div>
        </div>
      </div>
    </section>

    <!-- 8. CÙNG GIAI ĐOẠN & TIẾP NỐI MÙA VỤ -->
    <section class="next">
      <div class="wrap next-card glass reveal">
        <div>
          <div class="eyebrow">Tiếp nối mùa vụ</div>
          <h2>Khi cây đã vững, hành trình chuyển sang nuôi bông và hạt.</h2>
          <p>Khám phá giai đoạn nuôi bông, vô gạo với MINORI Vô Gạo Pro Max.</p>
          <p class="next-sibling">Cùng giai đoạn giữa vụ: <a href="../ultra-grow/">MINORI Ultra Grow</a> – công thức potassium phosphite, chăm cây chuyên sâu giữa vụ.</p>
        </div>
        <a class="btn" href="../vo-gao-promax/">Xem Vô Gạo Pro Max</a>
      </div>
    </section>
'''

(root / leaf['slug']).mkdir(exist_ok=True)
(root / leaf['slug'] / 'index.html').write_text(
    doc(leaf_title, leaf_desc, leaf['slug'], leaf_body, base='../', path=f"{leaf['slug']}/", head_extra=leaf_head),
    encoding='utf-8')

# ================================================================
# Trang Root Turbo được biên tập thủ công: chỉ đồng bộ header/footer
# và lời dẫn sang giai đoạn giữa vụ, giữ nguyên phần nội dung còn lại.
# ================================================================
import re
rt_path = root / 'root-turbo' / 'index.html'
rt = rt_path.read_text(encoding='utf-8')
rt = re.sub(r'  <!-- ================= SITE HEADER ================= -->.*?</header>',
            lambda m: header('root-turbo', '../'), rt, count=1, flags=re.S)
rt = re.sub(r'  <!-- ================= FOOTER ================= -->.*?</footer>',
            lambda m: footer('../'), rt, count=1, flags=re.S)
if 'class="next-sibling"' not in rt:
    rt = rt.replace(
        '<p>Khám phá giai đoạn dưỡng cây với MINORI Ultra Grow (20–45 ngày sau sạ).</p>',
        '<p>Khám phá giai đoạn dưỡng cây với MINORI Ultra Grow (20–45 ngày sau sạ).</p>\n'
        f'          <p class="next-sibling">Hoặc lựa chọn cùng giai đoạn: <a href="../{leaf["slug"]}/">{leaf["title"]}</a> – {leaf["tagline"][0].lower() + leaf["tagline"][1:]}</p>')
rt_path.write_text(rt, encoding='utf-8')

print('Built', len(products) + 3, 'pages with clean layout & new requirements')
