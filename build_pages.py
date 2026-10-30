from pathlib import Path
from html import escape
import json
import re

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
    if p['slug'] in ('root-turbo', 'ultra-grow', 'vo-gao-promax'):
        # Root Turbo, Ultra Grow, and Vô Gạo Pro Max pages have been upgraded to dedicated rich showcase pages
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
# Trang MINORI Ultra Grow (/ultra-grow/)
# Nâng cấp thành trang giới thiệu chuyên sâu, cao cấp bám sát nhãn Minori và
# bài viết minori-ultra-grow-bai-gioi-thieu.md
# ================================================================
ug_slug = 'ultra-grow'
ug_url = f"{SITE}{ug_slug}/"
ug_title = 'MINORI Ultra Grow – Dưỡng Cây Chuyên Sâu Giữa Vụ'
ug_desc = 'MINORI Ultra Grow – Dòng dưỡng cây chuyên sâu giữa vụ lúa với công thức potassium phosphite 30–20 (Lân hữu hiệu 30%, Kali hữu hiệu 20%), chăm bộ rễ, lá xanh dày và hỗ trợ đề kháng.'

ug_faq = [
    ('MINORI Ultra Grow khác gì ở nền tảng công thức?',
     'Theo thông tin Minori Agritech, sản phẩm dựa trên potassium phosphite từ Van Iperen, Hà Lan. Nhãn Minori ghi lân hữu hiệu 30%, kali hữu hiệu 20% và nhà sản xuất tại Hà Lan.'),
    ('Potassium phosphite được nghiên cứu về tác dụng gì?',
     'Nghiên cứu trên lúa mì và lúa ghi nhận thay đổi ở bộ rễ, hoạt động quang hợp hoặc các phản ứng sinh lý của cây trong những điều kiện thí nghiệm cụ thể. Đây là cơ sở cho hướng dưỡng cây chuyên sâu.'),
    ('Số 30–20 có nghĩa là gì?',
     'Nhãn Minori ghi <strong>lân hữu hiệu 30%</strong> và <strong>kali hữu hiệu 20%</strong>. Tài liệu Van Iperen ghi tỷ lệ P₂O₅/K₂O quy đổi tương ứng của nguyên liệu potassium phosphite. Phosphite không thay thế nguồn lân phosphate thông thường.'),
    ('Pha và dùng cho lúa như thế nào?',
     'Nhãn ghi pha <strong>1 lít với 400–800 lít nước</strong>; với cây lương thực, dùng tổng cộng <strong>1,5–2 lít/ha/vụ</strong>, chia <strong>2–3 lần/ha/vụ</strong> vào các giai đoạn bón lót, bón thúc. Phun sáng sớm hoặc chiều mát. Mốc 20–45 ngày sau sạ không phải lịch phun cố định cho mọi giống lúa.'),
]

ug_faq_html = '\n\n'.join(f'''            <details class="faq-item">
              <summary class="faq-question">
                <span>{i}. {escape(q)}</span>
                <span class="faq-toggle-icon" aria-hidden="true">+</span>
              </summary>
              <div class="faq-answer">
                <p>{a}</p>
              </div>
            </details>''' for i, (q, a) in enumerate(ug_faq, 1))

ug_faq_json = ',\n'.join(f'''          {{
            "@type": "Question",
            "name": {json.dumps(q, ensure_ascii=False)},
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": {json.dumps(re.sub(r'<[^>]+>', '', a), ensure_ascii=False)}
            }}
          }}''' for q, a in ug_faq)

ug_head = f'''

  <!-- Schema.org Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebPage",
        "@id": "{ug_url}#webpage",
        "url": "{ug_url}",
        "name": "{ug_title} | Minori Agritech",
        "description": "{ug_desc}",
        "breadcrumb": {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "{SITE}" }},
            {{ "@type": "ListItem", "position": 2, "name": "Ultra Grow", "item": "{ug_url}" }}
          ]
        }}
      }},
      {{
        "@type": "Product",
        "@id": "{ug_url}#product",
        "name": "MINORI Ultra Grow",
        "category": "Dinh dưỡng cây trồng & Chăm cây chuyên sâu",
        "description": "Phân bón lá hỗn hợp PK Newriver - Fosfo với công thức potassium phosphite (Lân hữu hiệu 30%, Kali hữu hiệu 20%) dành cho giai đoạn dưỡng cây chuyên sâu giữa vụ.",
        "brand": {{
          "@type": "Brand",
          "name": "Minori Agritech"
        }},
        "image": "https://minorivn.com/assets/minori-ultra-grow.svg"
      }},
      {{
        "@type": "FAQPage",
        "@id": "{ug_url}#faq",
        "mainEntity": [
{ug_faq_json}
        ]
      }}
    ]
  }}
  </script>'''

ug_body = f'''
    <!-- 1. PRODUCT HERO -->
    <section class="product-hero">
      <div class="wrap product-hero-grid">
        <div class="product-hero-copy glass">
          <div class="eyebrow">02 / Giai đoạn giữa vụ (20–45 ngày sau sạ)</div>
          <h1>MINORI Ultra Grow<br><em>Dưỡng cây chuyên sâu giữa vụ</em></h1>
          <div class="stage-chip">Khung theo dõi giữa vụ thường gặp</div>
          <p class="lead">Sau khi bén rễ và bước vào đẻ nhánh, cây lúa cần nuôi bộ lá, phát triển thân và chuẩn bị làm đòng. Khoảng 20–45 ngày sau sạ là khung theo dõi giữa vụ thường gặp, thay đổi theo từng giống và mùa vụ. MINORI Ultra Grow được định vị là dòng chăm cây chuyên sâu, cao cấp với công thức potassium phosphite 30–20, giúp cây duy trì sức sinh trưởng bền bỉ trước khi bước vào giai đoạn làm đòng.</p>
          <div class="hero-actions">
            <a class="btn" href="#thanh-phan">Xem thành phần</a>
            <a class="btn ghost" href="#huong-dan-su-dung">Xem hướng dẫn sử dụng</a>
          </div>
        </div>

        <div class="product-hero-art">
          <div class="art-photo">
            <img class="photo" src="../assets/growth.webp" alt="Ruộng lúa xanh khỏe trong giai đoạn giữa vụ">
            <span class="art-label">MINORI Ultra Grow</span>
          </div>

          <div class="product-bottle-card">
            <!-- Nhấn vào để phóng to hình ảnh scale-fit màn hình -->
            <div class="bottle-window" data-full-img="../assets/minori-ultra-grow.svg" role="button" tabindex="0" title="Nhấn để phóng to hình ảnh">
              <img src="../assets/minori-ultra-grow.svg" alt="Mặt trước chai MINORI Ultra Grow 500 ml" loading="lazy">
              <span class="zoom-badge">🔍 Phóng to</span>
            </div>
            <div class="bottle-caption">
              <span>Dòng chăm cây chuyên sâu</span>
              <strong>MINORI Ultra Grow</strong>
              <small>Potassium Phosphite 30–20</small>
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
            <div class="eyebrow section-label">Bao bì &amp; Nhãn chi tiết</div>
            <h2>Hình ảnh đầy đủ MINORI Ultra Grow</h2>
            <p class="lead">Bao bì chuẩn nhận diện chai 500 ml: thành phần công bố, công dụng, đặc tính cây lúa và hướng dẫn sử dụng.</p>
          </div>
          <div class="full-view-artwork" data-full-img="../assets/minori-ultra-grow.svg" role="button" tabindex="0" title="Nhấn để phóng to hình ảnh">
            <img src="../assets/minori-ultra-grow.svg" alt="Ba mặt chai MINORI Ultra Grow 500 ml – công thức potassium phosphite 30-20" loading="lazy">
            <span class="zoom-badge zoom-badge--full">🔍 Nhấn để phóng to</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. DETAIL / ĐIỂM RƠI MÙA VỤ -->
    <section class="detail-section" id="giua-vu">
      <div class="wrap detail-grid glass reveal">
        <div>
          <div class="eyebrow section-label">Điểm rơi mùa vụ</div>
          <h2>Giai đoạn giữa vụ cần điều gì?</h2>
        </div>
        <div>
          <p class="lead">Sau giai đoạn đẻ nhánh, cây lúa bước vào thời kỳ sinh trưởng mạnh. Bộ rễ tốt đầu vụ là điểm khởi đầu; cây còn cần giữ nhịp phát triển ổn định để đi đường dài.</p>
          <p>Người nông dân cần cây đủ sức đi qua áp lực giữa vụ, duy trì bộ lá xanh dày quang hợp tốt, rễ thân cứng cáp và sẵn sàng tích lũy dinh dưỡng cho giai đoạn làm đòng.</p>
          <div class="problem-grid">
            <div class="problem">Khỏe rễ, khỏe thân</div>
            <div class="problem">Lá xanh dày, quang hợp tốt</div>
            <div class="problem">Tăng sức chống chịu stress</div>
            <div class="problem">Sẵn sàng làm đòng &amp; nuôi bông</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. THÀNH PHẦN THEO NHÃN MINORI ULTRA GROW & CƠ CHẾ KHOA HỌC -->
    <section class="composition-section" id="thanh-phan">
      <div class="wrap">
        <div class="composition-card-wrap glass reveal">
          <div class="composition-header">
            <div class="eyebrow section-label" style="justify-content:center">Công thức Potassium Phosphite 30–20</div>
            <h2>Chỉ tiêu công bố theo nhãn sản phẩm</h2>
            <p class="lead">Hàm lượng và chỉ tiêu vật lý trích xuất chính xác theo nhãn sản xuất MINORI Ultra Grow:</p>
          </div>

          <!-- Bảng 4 thẻ thành phần hiển thị trực quan dạng HTML text rõ ràng -->
          <div class="composition-grid">
            <div class="nutrient-card">
              <div class="nutrient-val">30%</div>
              <div class="nutrient-name">Lân hữu hiệu</div>
              <div class="nutrient-en">Phosphite (P₂O₅ quy đổi)</div>
              <p class="nutrient-desc">Nền tảng potassium phosphite tham gia kích hoạt các phản ứng sinh lý của cây, hỗ trợ phát triển rễ và kích hoạt hệ thống đề kháng tự nhiên.</p>
            </div>

            <div class="nutrient-card">
              <div class="nutrient-val">20%</div>
              <div class="nutrient-name">Kali hữu hiệu</div>
              <div class="nutrient-en">K₂O</div>
              <p class="nutrient-desc">Điều tiết nước trong tế bào, hoạt động khí khổng, tăng cường vận chuyển quang hợp và giúp thân lá cứng cáp, bền bỉ.</p>
            </div>

            <div class="nutrient-card">
              <div class="nutrient-val">1,5</div>
              <div class="nutrient-name">Tỷ trọng</div>
              <div class="nutrient-en">Density (g/ml)</div>
              <p class="nutrient-desc">Dung dịch đậm đặc, đồng nhất, bám dính tốt trên bề mặt lá và hỗ trợ cây hấp thu dinh dưỡng nhanh qua rễ, thân, lá.</p>
            </div>

            <div class="nutrient-card">
              <div class="nutrient-val">6,5</div>
              <div class="nutrient-name">pH H₂O</div>
              <div class="nutrient-en">Chỉ số trung tính</div>
              <p class="nutrient-desc">Độ pH lý tưởng, an toàn cho mô lá lúa non, dễ dàng phối hợp trong các lần phun chăm sóc định kỳ.</p>
            </div>
          </div>

          <div class="composition-disclaimer">
            <strong>Lưu ý khoa học:</strong> Phosphite khác phosphate. Potassium phosphite là một hợp chất riêng biệt, không thay thế nguồn lân phosphate trong chương trình dinh dưỡng phân bón thông thường. Chỉ số 30% và 20% là thông tin công bố của chính nhãn MINORI Ultra Grow (phương thức sử dụng: bón lá).
          </div>

          <!-- Khối mở rộng: Cơ chế khoa học & Tài liệu tham khảo -->
          <details class="research-expandable">
            <summary class="research-summary">
              <span>Nền tảng hoạt chất được nghiên cứu quốc tế (Cơ chế khoa học)</span>
              <span class="summary-indicator">
                <span>Xem chi tiết / Thu gọn</span>
                <span class="summary-chevron" aria-hidden="true">▼</span>
              </span>
            </summary>
            <div class="research-body">
              <p class="research-intro">Các nghiên cứu nông học quốc tế ghi nhận tiềm năng và phản ứng sinh học của hoạt chất potassium phosphite đối với cây trồng:</p>

              <div class="research-list">
                <div class="research-item">
                  <strong>Nghiên cứu trên lúa mì (Frontiers in Plant Science, 2022):</strong> Nghiên cứu ghi nhận chế phẩm gốc potassium phosphite phun qua lá cải thiện một số đặc điểm rễ, sinh khối rễ, hoạt động enzyme nitrate reductase và quang hợp trong điều kiện thí nghiệm. Một số phản ứng thể hiện rõ nét hơn khi cây chịu thiếu dinh dưỡng, nóng hoặc hạn. [4]
                </div>
                <div class="research-item">
                  <strong>Nghiên cứu trên cây lúa (Plants, 2020):</strong> Nghiên cứu với giống lúa Nipponbare ghi nhận phosphite làm thay đổi biểu hiện của nhiều nhóm gene liên quan đến phản ứng tự vệ của cây; mô lá cây con trong thí nghiệm dày hơn đối chứng. [5]
                </div>
                <div class="research-item">
                  <strong>Đánh giá thực địa ruộng lúa (Crop Protection / FAO AGRIS, 2016):</strong> Một thử nghiệm đồng ruộng tại Uruguay đánh giá potassium phosphite trên lúa ở giai đoạn cuối làm đòng đến đầu trổ trong bối cảnh bệnh thân và bẹ lúa. [6]
                </div>
              </div>

              <div class="reference-links">
                <h3 class="reference-title">Tài liệu khoa học tham khảo</h3>
                <ol>
                  <li>
                    <a href="https://webapps.irri.org/in/od/rcm/questionnaires/BlankRecommendationPage.pdf" target="_blank" rel="noopener noreferrer">IRRI – Critical growth stages of rice</a>: Phân biệt ngày sau sạ với các mốc đẻ nhánh, làm đòng, trổ theo từng giống.
                  </li>
                  <li>
                    <a href="https://www.vaniperen.com/wp-content/uploads/dlm_uploads/2017/12/VII-TDS-EN-EL-Potassium-Phosphite-50-Liquid-27-11-2017-681-1.pdf" target="_blank" rel="noopener noreferrer">Van Iperen – Potassium Phosphite 50% Liquid, Product Datasheet</a>: Xuất xứ Hà Lan và chỉ tiêu 30% P₂O₅, 20% K₂O theo w/w của nguyên liệu.
                  </li>
                  <li>
                    <a href="https://ask.ifas.ufl.edu/publication/HS254" target="_blank" rel="noopener noreferrer">University of Florida IFAS – Phosphite và phosphate trong dinh dưỡng cây</a>: Giải thích vai trò sinh học khác nhau giữa phosphite và phosphate.
                  </li>
                  <li>
                    <a href="https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.1017048/full" target="_blank" rel="noopener noreferrer">Mohammed và cộng sự, Frontiers in Plant Science (2022)</a>: Nghiên cứu phosphite trên lúa mì, khảo sát rễ, quang hợp và đáp ứng stress.
                  </li>
                  <li>
                    <a href="https://www.mdpi.com/2223-7747/9/10/1334" target="_blank" rel="noopener noreferrer">Huang và cộng sự, Plants (2020)</a>: Nghiên cứu phosphite trên cây lúa con Nipponbare, khảo sát đặc điểm mô lá và biểu hiện gene.
                  </li>
                  <li>
                    <a href="https://agris.fao.org/search/en/providers/122535/records/65e00c6f63b8185d9cb0ea2b" target="_blank" rel="noopener noreferrer">Martínez và cộng sự, Crop Protection (2016), hồ sơ FAO AGRIS</a>: Thử nghiệm potassium phosphite trên ruộng lúa Uruguay ở cuối làm đòng đến đầu trổ.
                  </li>
                </ol>
                <p class="research-disclaimer">
                  <em>* Lưu ý: Các tài liệu khoa học trên giải thích cơ chế và tiềm năng của hoạt chất potassium phosphite; không chứng minh hay bảo đảm hiệu quả độc quyền của sản phẩm MINORI Ultra Grow trên mọi điều kiện ruộng lúa thương mại.</em>
                </p>
              </div>
            </div>
          </details>

        </div>
      </div>
    </section>

    <!-- 5. EFFECT / VAI TRÒ SẢN PHẨM -->
    <section class="effect-section">
      <div class="wrap effect-card glass-dark reveal">
        <div class="eyebrow light" style="justify-content:center">Vai trò của Ultra Grow</div>
        <h2>Chăm cây chuyên sâu – Nuôi dưỡng sức bền</h2>
        <div class="flow">
          <div class="flow-step">Khỏe rễ &amp; thân</div>
          <div class="flow-step">Lá xanh dày</div>
          <div class="flow-step">Hỗ trợ đề kháng</div>
          <div class="flow-step">Chuẩn bị làm đòng</div>
        </div>
        <blockquote>“Bộ rễ tốt chưa đủ, cây phải đủ sức đi đường dài để nuôi đòng và chắc hạt.”</blockquote>
      </div>
    </section>

    <!-- 6. HƯỚNG DẪN THỰC ĐỊA / HƯỚNG DẪN SỬ DỤNG GHI TRÊN NHÃN -->
    <section class="field-guide-section" id="huong-dan-su-dung">
      <div class="wrap">
        <div class="field-guide-card glass reveal">
          <div class="field-guide-header">
            <div class="eyebrow section-label">Quy trình khuyến cáo trên nhãn</div>
            <h2>Hướng dẫn sử dụng MINORI Ultra Grow</h2>
            <p class="lead">Trích xuất chính xác hướng dẫn sử dụng từ nhãn sản phẩm MINORI Ultra Grow:</p>
          </div>

          <div class="field-guide-grid">
            <div class="guide-step">
              <div class="step-num">01</div>
              <div class="step-body">
                <h3>Tỷ lệ pha nước</h3>
                <p>Pha 1 lít sản phẩm với 400–800 lít nước. Khuấy tan đều trước khi đưa vào bình phun hoặc hệ thống tưới.</p>
              </div>
            </div>

            <div class="guide-step">
              <div class="step-num">02</div>
              <div class="step-body">
                <h3>Liều lượng cây lương thực</h3>
                <p>Sử dụng 1,5–2 lít/ha/vụ (đây là tổng lượng khuyến cáo cho cả vụ). Chia đều phun 2–3 lần/ha/vụ vào các giai đoạn bón lót, bón thúc.</p>
              </div>
            </div>

            <div class="guide-step">
              <div class="step-num">03</div>
              <div class="step-body">
                <h3>Thời điểm phun</h3>
                <p>Phun vào lúc sáng sớm hoặc chiều mát khi khí khổng lá mở tối ưu, tránh ánh nắng gay gắt để dưỡng chất thẩm thấu trọn vẹn.</p>
              </div>
            </div>

            <div class="guide-step">
              <div class="step-num">04</div>
              <div class="step-body">
                <h3>Quản lý dinh dưỡng tổng thể</h3>
                <p>Sản phẩm bón lá hỗ trợ hấp thu nhanh và kích hoạt sức đề kháng; cần kết hợp chặt chẽ với quản lý nước và bón phân gốc cân đối theo nhu cầu thực tế của ruộng.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. FAQ / CÂU HỎI THƯỜNG GẶP -->
    <section class="faq-section" id="faq">
      <div class="wrap">
        <div class="faq-card glass reveal">
          <div class="faq-header">
            <div class="eyebrow section-label" style="justify-content:center">Hỏi đáp kỹ thuật</div>
            <h2>Câu hỏi thường gặp về MINORI Ultra Grow</h2>
            <p class="lead">Những thắc mắc phổ biến của bà con nông dân về dòng chăm cây chuyên sâu giữa vụ.</p>
          </div>

          <div class="faq-list">
{ug_faq_html}
          </div>
        </div>
      </div>
    </section>

    <!-- 8. NEXT STAGE -->
    <section class="next">
      <div class="wrap next-card glass reveal">
        <div>
          <div class="eyebrow">Tiếp nối mùa vụ</div>
          <h2>Khi cây đã lớn khỏe, hành trình chuyển sang nuôi bông và hạt.</h2>
          <p>Khám phá giai đoạn nuôi bông, vô gạo với MINORI Vô Gạo Pro Max.</p>
          <p class="next-sibling">Cùng giai đoạn giữa vụ: <a href="../duong-cay-khoe-la/">MINORI Dưỡng Cây Khỏe Lá</a> – bổ sung lân kali, dưỡng lá khỏe, cây vững giữa vụ.</p>
        </div>
        <a class="btn" href="../vo-gao-promax/">Xem Vô Gạo Pro Max</a>
      </div>
    </section>
'''

(root / ug_slug).mkdir(exist_ok=True)
(root / ug_slug / 'index.html').write_text(
    doc(ug_title, ug_desc, ug_slug, ug_body, base='../', path=f"{ug_slug}/", head_extra=ug_head),
    encoding='utf-8')

# ================================================================
# Trang MINORI Vô Gạo Pro Max (/vo-gao-promax/)
# Nâng cấp thành trang giới thiệu chuyên sâu, cao cấp bám sát nhãn Minori và
# bài viết minori-vo-gao-promax-bai-gioi-thieu.md
# ================================================================
vg_slug = 'vo-gao-promax'
vg_url = f"{SITE}{vg_slug}/"
vg_title = 'MINORI Vô Gạo Pro Max – Cứng Cây, Vững Bông, Chắc Hạt'
vg_desc = 'MINORI Vô Gạo Pro Max – Công thức Silic 22% kết hợp Kali 10% theo mẫu nhãn, bổ sung qua lá giai đoạn làm đòng, trước và sau trổ, giúp cứng cây, vững thân lá, nuôi bông và chắc hạt.'

vg_faq = [
    ('Vô Gạo Pro Max có những thành phần chính nào?',
     'Mẫu nhãn Minori ghi <strong>Silic hữu hiệu (SiO₂) 22%</strong> và <strong>Kali tinh khiết (K₂O) 10%</strong> (tính theo w/w); độ <strong>pH (H₂O) 6,5</strong> và <strong>tỷ trọng 1,2 g/cm³</strong>.'),
    ('Sản phẩm phù hợp lúc nào trên ruộng lúa?',
     'Mẫu nhãn hướng dẫn dùng ở giai đoạn <strong>làm đòng – trước và sau trổ</strong>. Thời điểm cụ thể cần căn theo giống lúa và nhịp sinh trưởng thực tế của ruộng thay vì một mốc ngày cố định.'),
    ('Silic và kali hỗ trợ gì cho cây lúa?',
     'Silic liên quan đến cấu trúc thân lá và khả năng đứng vững; kali tham gia vận chuyển chất đồng hóa và quá trình nuôi hạt. Nghiên cứu trên lúa đã khảo sát hai hướng tác động này nhằm làm rõ cơ sở nông học, không phải thử nghiệm riêng trên sản phẩm Minori.'),
    ('Dùng bao nhiêu cho một hecta?',
     'Mẫu nhãn ghi liều lượng <strong>0,5–1,0 lít/ha</strong> cho lúa, pha loãng với nước để phun qua lá vào sáng sớm hoặc chiều mát. Bà con cần đối chiếu nhãn thành phẩm cuối cùng trước khi sử dụng.'),
]

vg_faq_html = '\n\n'.join(f'''            <details class="faq-item">
              <summary class="faq-question">
                <span>{i}. {escape(q)}</span>
                <span class="faq-toggle-icon" aria-hidden="true">+</span>
              </summary>
              <div class="faq-answer">
                <p>{a}</p>
              </div>
            </details>''' for i, (q, a) in enumerate(vg_faq, 1))

vg_faq_json = ',\n'.join(f'''          {{
            "@type": "Question",
            "name": {json.dumps(q, ensure_ascii=False)},
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": {json.dumps(re.sub(r'<[^>]+>', '', a), ensure_ascii=False)}
            }}
          }}''' for q, a in vg_faq)

vg_head = f'''

  <!-- Schema.org Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebPage",
        "@id": "{vg_url}#webpage",
        "url": "{vg_url}",
        "name": "{vg_title} | Minori Agritech",
        "description": "{vg_desc}",
        "breadcrumb": {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "{SITE}" }},
            {{ "@type": "ListItem", "position": 2, "name": "Vô Gạo Pro Max", "item": "{vg_url}" }}
          ]
        }}
      }},
      {{
        "@type": "Product",
        "@id": "{vg_url}#product",
        "name": "MINORI Vô Gạo Pro Max",
        "category": "Phân bón lá Kali - Trung lượng",
        "description": "Phân bón lá Kali - Trung lượng KALI SILIC AB với công thức Silic hữu hiệu (SiO₂) 22% và Kali tinh khiết (K₂O) 10%, bổ sung qua lá giai đoạn làm đòng, trước và sau trổ cho cây lúa.",
        "brand": {{
          "@type": "Brand",
          "name": "Minori Agritech"
        }},
        "image": "https://minorivn.com/assets/vo-gao-promax.svg"
      }},
      {{
        "@type": "FAQPage",
        "@id": "{vg_url}#faq",
        "mainEntity": [
{vg_faq_json}
        ]
      }}
    ]
  }}
  </script>'''

vg_body = f'''
    <!-- 1. PRODUCT HERO -->
    <section class="product-hero">
      <div class="wrap product-hero-grid">
        <div class="product-hero-copy glass">
          <div class="eyebrow">03 / Giai đoạn cuối vụ (Từ 40 ngày đến cuối vụ)</div>
          <h1>MINORI Vô Gạo Pro Max<br><em>Cứng cây, vững bông, chắc hạt</em></h1>
          <div class="stage-chip">Làm đòng • Trước và sau trổ • Nuôi hạt</div>
          <p class="lead">Silic 22% kết hợp kali 10%: chăm thân lá từ lúc làm đòng, tạo nền cho bông lúa chắc khỏe đến cuối vụ. Bổ sung silic và kali qua lá giúp thân cây đứng vững để đón nhận ánh sáng, đồng thời hỗ trợ vận chuyển dinh dưỡng nuôi hạt lúa no đầy.</p>
          <div class="hero-actions">
            <a class="btn" href="#thanh-phan">Xem thành phần</a>
            <a class="btn ghost" href="#huong-dan-su-dung">Xem hướng dẫn sử dụng</a>
          </div>
        </div>

        <div class="product-hero-art">
          <div class="art-photo">
            <img class="photo" src="../assets/harvest.webp" alt="Bông lúa vàng trĩu hạt trong giai đoạn thu hoạch">
            <span class="art-label">MINORI Vô Gạo Pro Max</span>
          </div>

          <div class="product-bottle-card">
            <!-- Nhấn vào để phóng to hình ảnh scale-fit màn hình -->
            <div class="bottle-window" data-full-img="../assets/vo-gao-promax.svg" role="button" tabindex="0" title="Nhấn để phóng to hình ảnh">
              <img src="../assets/vo-gao-promax.svg" alt="Ba góc nhìn chai MINORI Vô Gạo Pro Max 500 ml" loading="lazy">
              <span class="zoom-badge">🔍 Phóng to</span>
            </div>
            <div class="bottle-caption">
              <span>Phân bón lá Kali - Trung lượng</span>
              <strong>MINORI Vô Gạo Pro Max</strong>
              <small>Silic 22% • Kali 10%</small>
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
            <div class="eyebrow section-label">Bao bì &amp; Nhãn chi tiết</div>
            <h2>Hình ảnh đầy đủ MINORI Vô Gạo Pro Max</h2>
            <p class="lead">Ba góc nhìn chai 500 ml: thành phần &amp; công dụng, mặt chính và hướng dẫn sử dụng chi tiết.</p>
          </div>
          <div class="full-view-artwork" data-full-img="../assets/vo-gao-promax.svg" role="button" tabindex="0" title="Nhấn để phóng to hình ảnh">
            <img src="../assets/vo-gao-promax.svg" alt="Ba góc nhìn chai MINORI Vô Gạo Pro Max 500 ml – công thức Silic 22% và Kali 10%" loading="lazy">
            <span class="zoom-badge zoom-badge--full">🔍 Nhấn để phóng to</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. DETAIL / ĐIỂM RƠI MÙA VỤ -->
    <section class="detail-section" id="cuoi-vu">
      <div class="wrap detail-grid glass reveal">
        <div>
          <div class="eyebrow section-label">Điểm rơi mùa vụ</div>
          <h2>Cuối vụ, cây lúa cần điều gì?</h2>
        </div>
        <div>
          <p class="lead">Khi cây lúa chuyển sang làm đòng, trổ và nuôi hạt, sức bền của thân, khả năng hoạt động của lá đòng và quá trình vận chuyển chất đồng hóa đều đáng được quan tâm.</p>
          <p>Một ruộng lúa có thân đứng vững sẽ thuận lợi hơn trong việc duy trì tán lá nhận ánh sáng quang hợp, hạn chế đổ ngã trước mưa gió và dồn sức hoàn thiện hạt lúa no chắc, sáng hạt.</p>
          <div class="problem-grid">
            <div class="problem">Thân cứng, lá đứng</div>
            <div class="problem">Hạn chế đổ ngã</div>
            <div class="problem">Nuôi đòng, tích lũy tinh bột</div>
            <div class="problem">Vô gạo nhanh, hạt chắc</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. THÀNH PHẦN THEO NHÃN MINORI VÔ GẠO PRO MAX & CƠ CHẾ KHOA HỌC -->
    <section class="composition-section" id="thanh-phan">
      <div class="wrap">
        <div class="composition-card-wrap glass reveal">
          <div class="composition-header">
            <div class="eyebrow section-label" style="justify-content:center">Công thức Silic – Kali theo mẫu nhãn</div>
            <h2>Chỉ tiêu thành phần định hướng</h2>
            <p class="lead">Số liệu trích xuất từ mẫu thiết kế nhãn MINORI Vô Gạo Pro Max do Minori Agritech cung cấp (tính theo tỷ lệ w/w):</p>
          </div>

          <!-- Bảng 4 thẻ thành phần hiển thị trực quan dạng HTML text rõ ràng -->
          <div class="composition-grid">
            <div class="nutrient-card">
              <div class="nutrient-val">22%</div>
              <div class="nutrient-name">Silic hữu hiệu</div>
              <div class="nutrient-en">SiO₂</div>
              <p class="nutrient-desc">Cây lúa tích lũy silic trong các mô thân và lá, tạo khung tế bào dày dặn, hỗ trợ thân đứng thẳng và tăng sức chống chịu với điều kiện bất lợi.</p>
            </div>

            <div class="nutrient-card">
              <div class="nutrient-val">10%</div>
              <div class="nutrient-name">Kali tinh khiết</div>
              <div class="nutrient-en">K₂O</div>
              <p class="nutrient-desc">Tham gia điều tiết nước, hoạt hóa enzyme và thúc đẩy quá trình vận chuyển sản phẩm quang hợp từ lá về nuôi hạt, hỗ trợ hạt vào gạo đều và chắc.</p>
            </div>

            <div class="nutrient-card">
              <div class="nutrient-val">6,5</div>
              <div class="nutrient-name">pH H₂O</div>
              <div class="nutrient-en">Chỉ số trung tính</div>
              <p class="nutrient-desc">Ngưỡng pH trung tính theo thiết kế nhãn, thuận tiện cho việc pha loãng phun qua lá trong các cữ chăm sóc đòng và nuôi hạt.</p>
            </div>

            <div class="nutrient-card">
              <div class="nutrient-val">1,2</div>
              <div class="nutrient-name">Tỷ trọng</div>
              <div class="nutrient-en">Density (g/cm³)</div>
              <p class="nutrient-desc">Dung dịch đồng nhất, ổn định theo tiêu chuẩn chất lượng ghi trên mẫu thiết kế bao bì chai 500 ml.</p>
            </div>
          </div>

          <div class="composition-disclaimer">
            <strong>Lưu ý biên tập:</strong> Số liệu được ghi theo mẫu thiết kế nhãn MINORI Vô Gạo Pro Max do Minori Agritech cung cấp. Đối chiếu nhãn lưu hành, phiếu kiểm nghiệm và hồ sơ đăng ký chính thức trước khi xuất bản.
          </div>

          <!-- Khối mở rộng: Cơ sở nông học & Tài liệu tham khảo -->
          <details class="research-expandable">
            <summary class="research-summary">
              <span>Cơ sở nông học về Silic và Kali trên cây lúa (Nghiên cứu khoa học)</span>
              <span class="summary-indicator">
                <span>Xem chi tiết / Thu gọn</span>
                <span class="summary-chevron" aria-hidden="true">▼</span>
              </span>
            </summary>
            <div class="research-body">
              <p class="research-intro">Các tài liệu và nghiên cứu nông học quốc tế ghi nhận vai trò thiết yếu của Silic và Kali đối với cây lúa giai đoạn cuối vụ:</p>

              <div class="research-list">
                <div class="research-item">
                  <strong>Silic và sức bền thân lá (SiO₂ 22%):</strong> Nghiên cứu trên lúa cho thấy việc cung cấp silic ở điều kiện phù hợp có thể cải thiện một số đặc điểm cấu trúc thân liên quan đến khả năng chống đổ ngã. Silic còn được quan tâm trong việc duy trì sức hoạt động của lá và khả năng thích nghi với điều kiện bất lợi. [2]
                </div>
                <div class="research-item">
                  <strong>Kali và quá trình nuôi hạt (K₂O 10%):</strong> Kali tham gia điều tiết nước, hoạt động enzyme và vận chuyển sản phẩm quang hợp trong cây. Khi lúa bước vào giai đoạn tạo bông và nuôi hạt, kali là một phần quan trọng của chương trình dinh dưỡng cân đối. Nghiên cứu thực địa trên lúa japonica ghi nhận việc quản lý kali cùng đạm có liên quan đến tốc độ vào hạt và khối lượng hạt. [3]
                </div>
                <div class="research-item">
                  <strong>Nghiên cứu về Potassium Silicate phun qua lá:</strong> Một nghiên cứu đồng ruộng tại Ai Cập đánh giá potassium silicate phun qua lá trên giống lúa Giza 179 ghi nhận cải thiện một số chỉ tiêu sinh trưởng, năng suất và chất lượng hạt ở các nghiệm thức phù hợp. Một nghiên cứu khác trên đất thiếu silic cũng ghi nhận các nghiệm thức bổ sung potassium silicate (gồm phun lá) ảnh hưởng tích cực đến hấp thu dinh dưỡng và chất lượng hạt. [4][5]
                </div>
              </div>

              <div class="reference-links">
                <h3 class="reference-title">Tài liệu khoa học tham khảo</h3>
                <ol>
                  <li>
                    Mẫu thiết kế nhãn MINORI Vô Gạo Pro Max do Minori Agritech cung cấp: Căn cứ chỉ tiêu và hướng dẫn của sản phẩm; chưa thay thế việc đối chiếu nhãn lưu hành, phiếu kiểm nghiệm và hồ sơ đăng ký.
                  </li>
                  <li>
                    <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11820559/" target="_blank" rel="noopener noreferrer">Jiang và cộng sự, Plants (2025) – Silicon Nutrition Improves Lodging Resistance of Rice Under Dry Cultivation</a>: Nghiên cứu bổ sung silic qua đất trên lúa canh tác khô, khảo sát cấu trúc thân và chỉ số đổ ngã; không phải thử nghiệm phân bón lá Minori.
                  </li>
                  <li>
                    <a href="https://peerj.com/articles/14710/" target="_blank" rel="noopener noreferrer">Xu và cộng sự, PeerJ (2023) – Nitrogen and potassium interactions optimized asynchronous spikelet filling and increased grain yield of japonica rice</a>: Thí nghiệm đồng ruộng về đạm, kali và sự vào hạt ở lúa japonica; không phải thử nghiệm Minori.
                  </li>
                  <li>
                    <a href="https://jpp.journals.ekb.eg/article_41115_f3f24a326c9692c16bf214575aa84499.pdf" target="_blank" rel="noopener noreferrer">Wissa, Journal of Plant Production (2017) – Impact of Potassium Silicate Compound as Foliar Application on the Growth, Yield and Grains Quality of Giza 179 Rice Cultivar</a>: Thử nghiệm potassium silicate phun lá trên lúa cấy ở Ai Cập; thời điểm trong nghiên cứu tính theo ngày sau cấy, không phải lịch phun khuyến nghị cho Minori.
                  </li>
                  <li>
                    <a href="https://journalijpss.com/index.php/IJPSS/article/view/2837" target="_blank" rel="noopener noreferrer">Arthi và cộng sự, International Journal of Plant &amp; Soil Science (2023)</a>: Nghiên cứu potassium silicate cùng NPK trên đất thiếu silic, gồm nghiệm thức phun lá và bón đất.
                  </li>
                </ol>
                <p class="research-disclaimer">
                  <em>* Lưu ý: Các tài liệu khoa học trên tạo cơ sở nông học cho hướng kết hợp silic – kali trên lúa; chúng khảo nghiệm công thức, liều dùng và điều kiện khác, không phải khảo nghiệm hay chứng nhận trực tiếp sản phẩm MINORI Vô Gạo Pro Max.</em>
                </p>
              </div>
            </div>
          </details>

        </div>
      </div>
    </section>

    <!-- 5. EFFECT / VAI TRÒ SẢN PHẨM -->
    <section class="effect-section">
      <div class="wrap effect-card glass-dark reveal">
        <div class="eyebrow light" style="justify-content:center">Vai trò của Vô Gạo Pro Max</div>
        <h2>Cứng cây vững thân – Nuôi hạt chắc mẩy</h2>
        <div class="flow">
          <div class="flow-step">Cứng cây</div>
          <div class="flow-step">Đứng lá</div>
          <div class="flow-step">Nuôi bông</div>
          <div class="flow-step">Vô gạo → Chắc hạt</div>
        </div>
        <blockquote>“Bắt đầu mùa vụ bằng một bộ rễ khỏe. Kết thúc bằng bông lúa vàng và những hạt lúa no tròn, chắc mẩy.”</blockquote>
      </div>
    </section>

    <!-- 6. HƯỚNG DẪN THỰC ĐỊA / HƯỚNG DẪN SỬ DỤNG GHI TRÊN NHÃN -->
    <section class="field-guide-section" id="huong-dan-su-dung">
      <div class="wrap">
        <div class="field-guide-card glass reveal">
          <div class="field-guide-header">
            <div class="eyebrow section-label">Quy trình khuyến cáo trên nhãn</div>
            <h2>Hướng dẫn sử dụng MINORI Vô Gạo Pro Max</h2>
            <p class="lead">Trích xuất chính xác hướng dẫn sử dụng từ mẫu thiết kế nhãn sản phẩm cho cây lúa:</p>
          </div>

          <div class="field-guide-grid">
            <div class="guide-step">
              <div class="step-num">01</div>
              <div class="step-body">
                <h3>Liều lượng cho lúa</h3>
                <p>Sử dụng 0,5–1,0 lít/ha. Liều lượng được tính theo diện tích; bà con pha với lượng nước phù hợp theo thực tế thiết bị và tập quán canh tác địa phương.</p>
              </div>
            </div>

            <div class="guide-step">
              <div class="step-num">02</div>
              <div class="step-body">
                <h3>Thời điểm sử dụng</h3>
                <p>Sử dụng ở giai đoạn làm đòng – trước và sau trổ. Hãy căn theo giai đoạn phát triển thực tế của giống lúa trên ruộng thay vì áp một mốc ngày sau sạ cố định.</p>
              </div>
            </div>

            <div class="guide-step">
              <div class="step-num">03</div>
              <div class="step-body">
                <h3>Phương pháp &amp; thời điểm phun</h3>
                <p>Pha loãng với nước, phun đều qua lá vào lúc sáng sớm hoặc chiều mát khi khí khổng mở tối ưu, tránh ánh nắng gay gắt để dưỡng chất hấp thu trọn vẹn.</p>
              </div>
            </div>

            <div class="guide-step">
              <div class="step-num">04</div>
              <div class="step-body">
                <h3>Thử tương hợp khi phối trộn</h3>
                <p>Ngưỡng pH 6,5 trung tính thuận tiện khi pha loãng, nhưng không bảo đảm mọi hỗn hợp đều ổn định. Cần kiểm tra nhãn từng sản phẩm và thử tương hợp lượng nhỏ trước khi phối trộn đại trà.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. FAQ / CÂU HỎI THƯỜNG GẶP -->
    <section class="faq-section" id="faq">
      <div class="wrap">
        <div class="faq-card glass reveal">
          <div class="faq-header">
            <div class="eyebrow section-label" style="justify-content:center">Hỏi đáp kỹ thuật</div>
            <h2>Câu hỏi thường gặp về MINORI Vô Gạo Pro Max</h2>
            <p class="lead">Những thắc mắc phổ biến của bà con nông dân về công thức Silic – Kali và cách chăm lúa cuối vụ.</p>
          </div>

          <div class="faq-list">
{vg_faq_html}
          </div>
        </div>
      </div>
    </section>

    <!-- 8. NEXT STAGE -->
    <section class="next">
      <div class="wrap next-card glass reveal">
        <div>
          <div class="eyebrow">Khép lại &amp; Khởi đầu mùa vụ</div>
          <h2>Một vụ lúa thắng lợi mở ra tiền đề cho mùa vụ tiếp theo.</h2>
          <p>Thu hoạch hạt vàng trọn vẹn, và hành trình mùa vụ mới lại bắt đầu từ một bộ rễ khỏe mạnh với MINORI Root Turbo.</p>
          <p class="next-sibling">Xem lại giai đoạn giữa vụ: <a href="../ultra-grow/">MINORI Ultra Grow</a> hoặc <a href="../duong-cay-khoe-la/">MINORI Dưỡng Cây Khỏe Lá</a> – chăm cây vững vàng trước khi bước vào làm đòng.</p>
        </div>
        <a class="btn" href="../root-turbo/">Khám phá Root Turbo</a>
      </div>
    </section>
'''

(root / vg_slug).mkdir(exist_ok=True)
(root / vg_slug / 'index.html').write_text(
    doc(vg_title, vg_desc, vg_slug, vg_body, base='../', path=f"{vg_slug}/", head_extra=vg_head),
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
