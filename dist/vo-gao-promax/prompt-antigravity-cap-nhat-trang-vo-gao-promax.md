# Prompt gửi Antigravity + Gemini: cập nhật trang MINORI Vô Gạo Pro Max

Bạn là lập trình viên và biên tập viên nội dung cho website Minori Agritech. Hãy kiểm tra code hiện tại và **chỉnh sửa bản làm việc trong repository** cho trang `https://minorivn.com/vo-gao-promax/`. Sau khi hoàn tất, trình bày diff, ảnh chụp màn hình kiểm tra và các điểm cần Minori đối chiếu trước khi xuất bản. **Không tự deploy hoặc thay đổi website production.**

## Tài liệu đầu vào và thứ tự ưu tiên

1. Bài viết: `minori-vo-gao-promax-bai-gioi-thieu.md` (file đi kèm prompt này). Đây là nguồn chính cho nội dung trang; đọc cả mục **Lưu ý biên tập trước khi xuất bản**.
2. Ảnh chai mới do Minori cung cấp: `C:\Users\Admin\Downloads\vo-gao-promax.png` (PNG 1536 × 1024, ba góc nhìn chai). Nếu đường dẫn khác trong môi trường của bạn, yêu cầu người giao việc cung cấp đúng file ảnh hoặc tìm trong tài liệu dự án; không dùng ảnh tự tạo thay thế.
3. Hai ảnh thiết kế nhãn `vo-gao-promax.png` và `Vo_Gao_Promax_v5_EDITABLE_4K_3840x2124.png` chỉ để đối chiếu chữ trên nhãn; bản phẳng không thay thế ảnh chai đã được chỉ định ở mục 2.
4. Trang hiện tại và code repository là nguồn để kiểm tra cấu trúc, đường dẫn, phong cách và tính năng đang hoạt động. Trang nhà cung cấp do Minori gửi chỉ là tài liệu tham khảo nội bộ, **không phải** nguồn xác nhận độc lập cho claim của Minori. `report.md` về Sika39 là tài liệu nội bộ, không phải nội dung marketing đã kiểm chứng.
5. Khi có khác biệt giữa bản nháp và nhãn thành phẩm/hồ sơ lưu hành đã xác nhận, ưu tiên **nhãn và hồ sơ đã xác nhận**; ghi rõ khác biệt để Minori duyệt. Không tự suy diễn thông số.

## 1. Kiểm tra code và trang hiện tại

- Xác định file trang `/vo-gao-promax/`, layout chung, CSS, JS, metadata, sitemap và nơi quản lý asset. Dùng tìm kiếm toàn repository (`rg`) cho `vo-gao-promax.svg`, `Vô Gạo Pro Max`, URL trang và các ảnh chai liên quan.
- Kiểm tra cả desktop và mobile. Trang hiện có hero “Bông lúa vàng. Hạt chắc.”, ảnh chai SVG cũ ở hero và section toàn cảnh, phần vai trò/effect nói lặp các ý “cứng cây, nuôi bông, vô gạo, chắc hạt”. Giữ những chi tiết thiết kế hữu ích nhưng biên tập thành một mạch nội dung, không lặp ý giữa các section.
- Kiểm tra nav, footer, liên kết từ trang chủ/thẻ sản phẩm và mọi vị trí dùng cùng asset để tránh nơi còn hiện chai tên cũ.

## 2. Thay ảnh chai đúng định dạng

- Chép **nguyên file PNG** được cung cấp vào thư mục asset của website, ví dụ `assets/vo-gao-promax.png`, theo cách quản lý ảnh hiện có trong repository.
- Cập nhật mọi tham chiếu đến ảnh chai cũ `assets/vo-gao-promax.svg` (trên trang sản phẩm, thumbnail trang chủ, modal/zoom nếu có, preload hoặc metadata nếu có) sang đường dẫn PNG mới. **Không đổi đuôi file PNG thành `.svg` và không giữ đường dẫn SVG trỏ tới dữ liệu PNG.** Chỉ loại bỏ asset SVG cũ khi xác nhận nó không còn được dùng ở nơi nào khác.
- Ảnh mới gồm ba chai trong một khung ngang. Dùng `object-fit: contain`, khoảng trống và kích thước phù hợp để đọc được nhãn ở desktop, tablet, mobile; không crop mất chai hai bên. Tối ưu tải ảnh hợp lý, đặt `width`/`height` hoặc tỉ lệ khung để tránh nhảy layout. Ảnh dưới màn hình đầu có thể lazy-load. Alt text: “Ba góc nhìn chai MINORI Vô Gạo Pro Max 500 ml”. Nếu có nút phóng to, đảm bảo hoạt động bằng bàn phím, có tên truy cập được và đóng bằng Escape.
- Giữ nguyên toàn bộ chữ, ký hiệu và thiết kế trên ảnh nhãn được Minori cung cấp. Không chỉnh sửa ảnh chai hoặc tạo ghi chú trên giao diện về các tên, mã hay thông tin đăng ký thể hiện trên nhãn.

## 3. Tổ chức lại trang và nội dung

Thiết kế theo nhận diện Minori hiện tại, bố cục đẹp, dễ đọc, responsive. Có thể điều chỉnh thứ tự nếu code hiện tại gợi ra cách tốt hơn, nhưng phải có các phần sau:

1. **Hero:** tên “MINORI Vô Gạo Pro Max”, thông điệp ngắn về chăm thân lá, làm đòng và nuôi hạt; ảnh chai PNG mới; CTA đến thành phần hoặc hướng dẫn sử dụng. Không dùng lời hứa chắc chắn về năng suất.
2. **Thành phần nổi bật:** bảng HTML semantic đúng dữ liệu mẫu nhãn: Silic hữu hiệu (SiO₂) **22%**, Kali tinh khiết (K₂O) **10%**, pH (H₂O) **6,5**, tỷ trọng **1,2 g/cm³**. Không biến pH, tỷ trọng thành phần trăm. Có ghi chú “Theo mẫu nhãn Minori cung cấp; đối chiếu nhãn lưu hành trước khi xuất bản” cho bản làm việc.
3. **Vai trò silic và kali:** một section giải thích ngắn, dễ hiểu: silic liên quan đến cấu trúc thân lá/khả năng đứng vững; kali tham gia vận chuyển chất đồng hóa và quá trình nuôi hạt. Dùng các câu “hỗ trợ”, “góp phần”, “trong quy trình dinh dưỡng cân đối”. Nếu đã nêu ý ở đây, không lặp lại thành các đoạn dài ở section kế tiếp.
4. **Bằng chứng nông học:** tóm tắt 2–3 ý từ bài viết Markdown kèm liên kết tới các nghiên cứu gốc về silic, kali và potassium silicate trên lúa. Nói rõ đó là nghiên cứu **về dưỡng chất/công thức khác**, không phải chứng nhận hay khảo nghiệm trực tiếp sản phẩm Minori. Có thể làm phần “Xem cơ sở nghiên cứu” dạng `<details><summary>` hoặc cơ chế mở rộng accessible để giữ trang gọn.
5. **Thời điểm và cách dùng:** hiển thị rõ lúa **0,5–1,0 lít/ha**, giai đoạn **làm đòng – trước và sau trổ**, pha loãng phun qua lá sáng sớm hoặc chiều mát, theo mẫu nhãn. Không tạo lịch phun 20–25/35–45 ngày sau sạ từ `report.md`, vì lịch đó không khớp bảng hướng dẫn trên mẫu nhãn.
6. **FAQ 4 câu:** lấy câu hỏi và câu trả lời ngắn ở cuối bài viết. Nếu dùng accordion, mỗi nút có trạng thái `aria-expanded`, liên kết `aria-controls`, điều khiển được bằng bàn phím; ưu tiên `<details>/<summary>` nếu phù hợp.
7. **Nguồn tham khảo và liên kết hành trình:** nguồn khoa học ở cuối trang theo cách gọn; điều hướng về trang chủ và sản phẩm liên quan. Không đẩy toàn bộ chú thích biên tập nội bộ lên giao diện khách hàng.

Trên trang hiện tại có hai khu vực ảnh chai và các section mô tả cùng công dụng. Hãy giảm lặp, giữ nhịp thị giác giữa ảnh đồng ruộng, ảnh chai, bảng thông số và nội dung. Nếu phần toàn cảnh chai vẫn hữu ích, cho phép dùng ảnh PNG mới như gallery/zoom thay vì thêm một khối lớn gây kéo dài trang.

## 4. Giới hạn claim và kiểm tra nguồn

- **Chỉ dùng con số 22%, 10%, pH 6,5, 1,2 g/cm³ và liều 0,5–1,0 lít/ha theo mẫu nhãn đã cung cấp.** Trước lúc publish, Minori phải đối chiếu nhãn cuối, hồ sơ đăng ký và phiếu kiểm nghiệm. Không tự chuyển các số từ sản phẩm cạnh tranh sang nhãn Minori.
- Không đưa so sánh với **Sika39**, các mức pH/độ cứng/hiệu quả giả định của đối thủ, giá bán, chính sách thương mại hoặc lời dẫn trong `report.md` lên trang.
- Không viết “chống đổ ngã tuyệt đối”, “tăng năng suất chắc chắn”, “hạt to hơn X%”, “không kết tủa với mọi thuốc”, “phun drone an toàn với mọi hỗn hợp”, “không gây cháy ở mọi liều”, “phòng/trị sâu bệnh” hay “được tổ chức quốc tế chứng nhận hiệu quả” khi chưa có hồ sơ cụ thể cho chính sản phẩm.
- pH 6,5 của sản phẩm không tự chứng minh độ tương hợp của hỗn hợp phun. Nếu có hướng dẫn phối chung, nêu cần đọc nhãn của từng sản phẩm và thử tương hợp ở quy mô nhỏ.
- Tách rõ ba tầng thông tin: **chỉ tiêu trên mẫu nhãn Minori**, **cơ sở khoa học chung**, **suy luận biên tập về vị trí sản phẩm trong quy trình chăm lúa**. Đặt nguồn ngay gần các đoạn khoa học; không gắn kết quả nghiên cứu của sản phẩm khác vào MINORI Vô Gạo Pro Max.
- Nguồn gốc nguyên liệu từ Ấn Độ, mã số phân bón 32811 và QĐLH 714/QĐ-TTTV-PB chỉ xuất hiện trên ảnh thiết kế. Chỉ đưa vào HTML công khai nếu Minori có nhãn/hồ sơ cuối xác nhận cách ghi và quan hệ pháp lý với tên sản phẩm hiện tại.

## 5. SEO, khả năng truy cập và chất lượng giao diện

- Một H1 duy nhất; H2/H3 theo thứ bậc. Cập nhật title, meta description tiếng Việt, canonical `/vo-gao-promax/`, Open Graph/Twitter image phù hợp với ảnh mới, sitemap nếu quy trình dự án yêu cầu. Không nhồi từ khóa.
- Cân nhắc `Product` và `FAQPage` structured data **chỉ khi dữ liệu hiển thị và điều kiện sử dụng schema đều phù hợp**; không thêm giá, đánh giá, xếp hạng hoặc claim không có thật.
- Kiểm tra tương phản màu, kích cỡ chữ, focus visible, thao tác bàn phím, alt text và `prefers-reduced-motion`. Nội dung quan trọng phải đọc được khi JS tắt hoặc hiệu ứng reveal chưa chạy.
- Đảm bảo không có cuộn ngang ở 320, 375, 768, 1280 px; ảnh ba chai không làm tràn layout. Kiểm tra nav, CTA, ảnh, FAQ, link nghiên cứu, liên kết sản phẩm trên desktop và mobile.
- Tối ưu tốc độ tải ảnh, không thêm thư viện nặng khi HTML/CSS/JS hiện có đã đủ.

## 6. Bàn giao

Hãy gửi lại: (1) danh sách file đã sửa và tóm tắt diff; (2) ảnh chụp trang desktop/mobile; (3) kết quả kiểm tra liên kết và responsive; (4) các điểm cần Minori duyệt trước khi xuất bản về chỉ tiêu, liều dùng và hồ sơ; (5) xác nhận **chưa deploy**. Nếu thiếu nhãn đã phê duyệt, vẫn hoàn thiện bản làm việc nhưng đánh dấu các chỗ cần đối chiếu, không tự tạo thông tin để lấp chỗ trống.
