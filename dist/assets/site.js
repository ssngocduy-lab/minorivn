// Phát hiện hệ điều hành iOS hoặc Android để tối ưu hóa hiển thị di động
(function detectMobileOS() {
  const ua = navigator.userAgent || navigator.vendor || window.opera || '';
  const isIOS = /iPad|iPhone|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  const isAndroid = /Android/i.test(ua);
  if (isIOS || isAndroid) {
    document.documentElement.classList.add('mobile-os');
    if (isIOS) document.documentElement.classList.add('os-ios');
    if (isAndroid) document.documentElement.classList.add('os-android');
  }
})();

const toggle=document.querySelector('.menu-toggle');const nav=document.querySelector('.main-nav');if(toggle&&nav){toggle.addEventListener('click',()=>{const open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));toggle.textContent=open?'Đóng':'Menu'});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.textContent='Menu'}))}
const items=document.querySelectorAll('.reveal');if('IntersectionObserver'in window){const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}),{threshold:.07});items.forEach(item=>observer.observe(item))}else items.forEach(item=>item.classList.add('visible'));
const form=document.querySelector('#contact-form');if(form){form.addEventListener('submit',event=>{event.preventDefault();if(!form.reportValidity())return;const status=document.querySelector('#form-status');status.textContent='Biểu mẫu này là bản tạm: thông tin của bạn chưa được lưu hoặc gửi đến Minori. Vui lòng giữ lại lời nhắn để sử dụng khi kênh liên hệ chính thức được mở.';status.classList.add('show');status.setAttribute('role','status')})}

// Image Modal Popup: Scale to fit user screen on click
(function setupImageModal() {
  function init() {
    const triggers = document.querySelectorAll('.bottle-window[data-full-img]');
    if (!triggers.length) return;
    
    let modal = document.querySelector('#image-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'image-modal';
      modal.className = 'image-modal';
      modal.setAttribute('role', 'dialog');
      modal.setAttribute('aria-modal', 'true');
      modal.setAttribute('aria-label', 'Phóng to hình ảnh sản phẩm');
      modal.innerHTML = `
        <div class="modal-backdrop"></div>
        <div class="modal-content">
          <button class="modal-close" type="button" aria-label="Đóng phóng to">✕</button>
          <img id="modal-img" src="" alt="Hình ảnh sản phẩm chi tiết">
        </div>
      `;
      document.body.appendChild(modal);

      const closeModal = () => {
        modal.classList.remove('open');
      };

      modal.querySelector('.modal-close').addEventListener('click', closeModal);
      modal.querySelector('.modal-backdrop').addEventListener('click', closeModal);
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('open')) {
          closeModal();
        }
      });
    }

    triggers.forEach(trig => {
      trig.style.cursor = 'pointer';
      trig.setAttribute('title', 'Nhấn để phóng to hình ảnh');
      trig.addEventListener('click', (e) => {
        e.preventDefault();
        const fullImg = trig.getAttribute('data-full-img');
        const modalImg = modal.querySelector('#modal-img');
        if (fullImg && modalImg) {
          modalImg.src = fullImg;
          modal.classList.add('open');
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
