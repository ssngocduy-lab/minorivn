# Prompt cho Antigravity: thêm MINORI Dưỡng Cây Khỏe Lá vào website

Bạn là người thiết kế và phát triển website Minori Agritech. Hãy kiểm tra mã nguồn thực tế và bản xem trước của `https://minorivn.com/`, sau đó **thực hiện thay đổi trong dự án cục bộ**. Cần giữ phong cách hiện có: ảnh đồng lúa, nền glass, màu xanh lá và vàng, nhịp kể chuyện theo giai đoạn mùa vụ. Không tự đưa bản sửa lên website đang chạy.

## Tài liệu đầu vào

- Trang chủ: `https://minorivn.com/`.
- Trang sản phẩm hiện có: `https://minorivn.com/ultra-grow/` và các trang sản phẩm khác để tham chiếu cấu trúc, menu, footer, hiệu ứng và cách phóng to ảnh.
- Bài viết đã biên tập: `minori-duong-cay-khoe-la-bai-gioi-thieu.md`. Tìm file trong workspace được cung cấp; nếu chưa có, yêu cầu tôi đưa file vào dự án trước khi hoàn thiện trang mới. Dùng phần bài giới thiệu, bảng thành phần, Q&A và nguồn tham khảo có chọn lọc. Phần **“Lưu ý biên tập trước khi xuất bản”** là chỉ dẫn nội bộ, không hiển thị nguyên văn cho khách truy cập.
- Ảnh chai dự kiến: `minori-duong-cay-khoe-la.svg` và `minori-ultra-grow.svg`. Kiểm tra đường dẫn và tên file thực tế trong dự án trước khi dùng. Website đang chạy có thể vẫn tham chiếu `ultra-grow.svg`; hãy cập nhật sang asset mới khi file có mặt. Không tạo liên kết ảnh bị lỗi hoặc dùng ảnh chai của sản phẩm khác để lấp chỗ trống.

## Hiện trạng cần xác nhận trong mã nguồn

Trang chủ đang có menu **Trang chủ / Root Turbo - Kích Rễ / Ultra Grow - Khỏe Cây / Vô Gạo Pro Max / Liên hệ**. Khối hành trình `#hanh-trinh` có ba `article.stage-row.glass.reveal`; article thứ hai là giai đoạn **02 / 20–45 ngày sau sạ**, hiện chỉ giới thiệu MINORI Ultra Grow. Lớp `visible` xuất hiện khi hiệu ứng reveal chạy; hãy sửa markup/component gốc, không phụ thuộc vào việc ghi cứng lớp `visible`. Footer mới liệt kê ba sản phẩm. Hero có số **03** cho ba giai đoạn, nhưng câu **“Ba sản phẩm. Một hành trình.”** sẽ không còn đúng sau khi thêm lựa chọn thứ tư.

## 1. Thêm điều hướng cho sản phẩm mới

- Thêm mục **“Dưỡng Cây Khỏe Lá”** vào menu desktop và menu mobile, dẫn đến trang sản phẩm mới. Đặt cạnh Ultra Grow để người đọc thấy hai lựa chọn giữa vụ.
- Thêm liên kết sản phẩm mới vào footer và những vị trí điều hướng sản phẩm liên quan. Kiểm tra trạng thái menu đang mở, focus bàn phím, vùng bấm trên mobile và hiện tượng tràn ngang khi có thêm một mục.
- Đề xuất URL nhất quán với site, ví dụ `/duong-cay-khoe-la/`; dùng URL cuối cùng tương ứng với cấu trúc route thật của dự án. Mọi liên kết phải trỏ về cùng một URL.

## 2. Thiết kế lại article giai đoạn giữa vụ để có đúng hai lựa chọn

Giữ article giai đoạn **02** trong hành trình ba giai đoạn và giữ ảnh ruộng lúa nếu vẫn phù hợp. Bên trong article, thay phần giới thiệu một sản phẩm bằng tiêu đề ngắn như **“Hai lựa chọn dưỡng cây giữa vụ”** và hai thẻ sản phẩm rõ ràng. Mỗi thẻ có tên, một câu giới thiệu ngắn, thumbnail chai và mũi tên **“Khám phá sản phẩm →”**. Tạo **một liên kết có vùng bấm rõ cho mỗi sản phẩm** bao quanh nội dung thẻ hoặc một cấu trúc tương đương; tránh liên kết lồng nhau và tránh hai liên kết trùng đích gây rối cho người dùng bàn phím.

### Thẻ 1 — MINORI Dưỡng Cây Khỏe Lá

- Tên: **MINORI Dưỡng Cây Khỏe Lá**.
- Câu giới thiệu đề xuất, **11 từ**: **“Bổ sung lân kali, dưỡng lá khỏe, cây vững giữa vụ.”**
- CTA: **“Khám phá sản phẩm →”**, mở trang Dưỡng Cây Khỏe Lá.
- Thumbnail: `minori-duong-cay-khoe-la.svg`, alt text mô tả đúng chai sản phẩm.
- Định vị trực quan: lựa chọn dưỡng cây giữa vụ rõ ràng, dễ tiếp cận, không dùng từ “bản rẻ”, “thấp cấp” hay các so sánh giảm giá trị sản phẩm.

### Thẻ 2 — MINORI Ultra Grow

- Tên: **MINORI Ultra Grow**.
- Câu giới thiệu đề xuất: **“Công thức potassium phosphite, chăm cây chuyên sâu giữa vụ.”** Nếu hồ sơ Minori xác nhận nguồn gốc, có thể thay bằng **“Potassium phosphite từ Hà Lan, chăm cây chuyên sâu giữa vụ.”**
- CTA: **“Khám phá sản phẩm →”**, mở trang Ultra Grow hiện có.
- Thumbnail: `minori-ultra-grow.svg`, alt text mô tả đúng chai sản phẩm.
- Định vị trực quan cao cấp hơn bằng nhãn nhỏ như **“Dòng chuyên sâu”**, kiểu chữ, khoảng trắng hoặc điểm nhấn tinh tế. Chỉ thêm **“từ Hà Lan”** sau khi đối chiếu được hồ sơ Minori. Hai thẻ vẫn phải có độ rõ và khả năng truy cập tương đương; không dùng hiệu ứng làm thẻ Dưỡng Cây Khỏe Lá trở nên mờ, nhỏ khó đọc hoặc kém tin cậy.

**Ràng buộc nội dung cho Ultra Grow:** Tài liệu kỹ thuật của Van Iperen ghi *Potassium Phosphite 50% Liquid*, xuất xứ Hà Lan, hàm lượng theo quy đổi **30% P₂O₅ và 20% K₂O (w/w)**. Tên nhà cung cấp đúng là **Van Iperen**, không phải “Van Inperen”. Trước khi đưa “nhập khẩu 100% từ Hà Lan”, tên Van Iperen hoặc số liệu 30–20 vào nội dung công khai của **MINORI Ultra Grow**, đối chiếu nhãn Minori mới, hồ sơ nhập khẩu và tài liệu lô hàng để xác nhận đúng mối liên hệ. **Phosphite khác phosphate:** không viết rằng phosphite là nguồn lân dinh dưỡng tương đương phosphate, không gọi đây là “hỗn hợp lân + kali giúp cây phát triển toàn diện nhất”, và không hứa hiệu quả vượt trội trên mọi ruộng. Có thể nêu tính chuyên biệt của **công thức potassium phosphite** và nguồn gốc Hà Lan khi đã xác thực. Không tự thêm tuyên bố phòng/trị bệnh hoặc công dụng ngoài nhãn được phê duyệt.

Sau khi có bốn sản phẩm trong **ba giai đoạn**, cập nhật những câu đếm sai như **“Ba sản phẩm. Một hành trình.”** và **“Không chỉ là ba chai phân bón.”** thành cách nói đúng, ví dụ **“Ba giai đoạn. Bốn lựa chọn. Một hành trình.”** Số **03** vẫn có thể giữ nếu nhãn gần đó nói rõ đó là **ba giai đoạn/ba điểm rơi**, không phải số sản phẩm. Giữ thẻ giai đoạn 01 và 03 cùng mạch kể chuyện hiện tại.

## 3. Tạo trang MINORI Dưỡng Cây Khỏe Lá

- Tạo một trang sản phẩm mới theo ngôn ngữ thiết kế và cấu trúc của các trang Root Turbo/Ultra Grow: hero có H1 duy nhất, ảnh sản phẩm, mốc giai đoạn, các khối nội dung dễ quét, thông tin thành phần, cách chăm lúa và liên kết tiếp nối mùa vụ.
- Tích hợp có chọn lọc nội dung từ file Markdown được cung cấp. Giữ thông điệp **lân hữu hiệu (P₂O₅) 31%**, **kali hữu hiệu (K₂O) 23%**, vai trò đối với bộ lá và cây lúa, cùng **4 Q&A** cuối bài. Không biến bài viết thành một khối chữ dài và không lặp cùng một ý ở hero, thẻ lợi ích, phần giải thích khoa học và Q&A.
- Dùng ảnh `minori-duong-cay-khoe-la.svg` theo đúng tỉ lệ; cho phép phóng to ảnh nếu mẫu trang sản phẩm hiện có hỗ trợ. Chữ thành phần và hướng dẫn dùng cần là HTML text, không chỉ nằm trong ảnh.
- Phân biệt **khung quan sát giữa vụ 20–45 ngày sau sạ** với **mốc dùng trên nhãn Minori dự kiến: bắt đầu làm đòng, trước và sau trổ đều**. Không biến số ngày 20–45 thành lịch phun cố định cho mọi giống. Liều lượng và lời công bố chính thức phải theo bản nhãn được cơ quan chức năng phê duyệt.
- Nhãn Minori của sản phẩm này hiện **đang chờ phê duyệt**. Hãy hoàn thiện trang trong môi trường cục bộ/staging, giữ phần cần xác nhận trong ghi chú bàn giao, và chỉ dùng bản nhãn cuối cùng khi đưa lên website công khai. Không hiển thị “Lưu ý biên tập” hoặc dữ liệu chưa được duyệt như thể đã là thông tin pháp lý chính thức.
- Bổ sung title, meta description, canonical, alt text, heading H2/H3 theo thứ bậc, liên kết nội bộ về trang chủ và các sản phẩm cùng giai đoạn. Chỉ tạo Product/FAQ schema với dữ liệu đã được xác nhận; không tự thêm xếp hạng, nhận xét, giá hay claim năng suất.

## 4. Kiểm tra và bàn giao

- Kiểm tra menu desktop/mobile, hai thẻ trong article giai đoạn 02, footer, CTA, thumbnail, URL mới, ảnh phóng to, khả năng điều khiển bằng bàn phím và không có cuộn ngang.
- Xem giao diện ở desktop, tablet và điện thoại; bố cục hai lựa chọn phải rõ ngay cả khi xếp dọc trên mobile. Giữ hiệu ứng reveal hoạt động và tôn trọng chế độ giảm chuyển động của người dùng.
- Chạy các kiểm tra sẵn có trong dự án. Bàn giao danh sách file đã sửa, ảnh chụp desktop/mobile, các URL đã kiểm tra, và danh sách tài liệu/claim cần xác nhận trước khi xuất bản. Không tự deploy.

### Nguồn kỹ thuật cho phần Ultra Grow

- [Van Iperen – Potassium Phosphite 50% Liquid, Product Datasheet](https://www.vaniperen.com/wp-content/uploads/dlm_uploads/2017/12/VII-TDS-EN-EL-Potassium-Phosphite-50-Liquid-27-11-2017-681-1.pdf): xuất xứ Hà Lan; potassium phosphite; 30% P₂O₅ và 20% K₂O theo quy đổi w/w.
- [University of Florida IFAS – Phosphite và phosphate trong dinh dưỡng cây](https://ask.ifas.ufl.edu/publication/HS254): phân biệt vai trò của phosphite và phosphate; không diễn giải phosphite như nguồn lân dinh dưỡng tương đương phosphate.

