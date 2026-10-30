# Prompt cho Antigravity: cập nhật trang MINORI Ultra Grow

Bạn là người thiết kế và phát triển website Minori Agritech. Hãy **kiểm tra mã nguồn của trang `/ultra-grow/`**, cập nhật nội dung và bố cục trong dự án cục bộ, chạy bản xem trước rồi bàn giao thay đổi để tôi duyệt. **Không tự deploy lên website đang chạy.** Mục tiêu là một trang sản phẩm rõ ràng, đẹp trên điện thoại và desktop, thể hiện MINORI Ultra Grow là **dòng chăm cây chuyên sâu, cao cấp** dựa trên công thức potassium phosphite, nhưng mọi thông số và công bố sản phẩm phải bám nguồn.

## Nguồn đầu vào và thứ tự ưu tiên

1. **Nhãn MINORI Ultra Grow**: `Minori_Ultra_Grow_v2_EDITABLE_235mm_width.pdf`, tại `C:\Users\Admin\Dropbox\Confidential\Minori Agritech\MINORI_DESIGN_LIBRARY\APPROVED_LABELS\`. Dùng để đối chiếu **thành phần, chỉ tiêu vật lý, phương thức và hướng dẫn sử dụng** của sản phẩm Minori. PDF hiện vẫn có các ô cần đối chiếu; xem mục “Điểm cần rà trước khi xuất bản” bên dưới.
2. **Bài giới thiệu đã biên tập**: `minori-ultra-grow-bai-gioi-thieu.md`. Dùng làm nguồn nội dung, lý giải khoa học, 4 Q&A và đường dẫn tài liệu tham khảo. Phần **“Lưu ý biên tập trước khi xuất bản”** là ghi chú nội bộ, không hiển thị nguyên văn trên trang công khai. Nếu không tìm thấy file trong repo, dùng các nội dung bắt buộc được chép trong prompt này và báo rõ file còn thiếu khi bàn giao; không tự viết thêm dữ kiện.
3. **Mã nguồn và trang đang chạy**: [https://minorivn.com/ultra-grow/](https://minorivn.com/ultra-grow/). Kiểm tra component, CSS, JS và asset thực tế trước khi sửa. Giữ URL `/ultra-grow/` và liên kết nội bộ hiện có.
4. **Tài liệu quốc tế** cuối prompt: chỉ dùng để giải thích potassium phosphite và các kết quả nghiên cứu trên cây trồng, **không** biến thành chứng nhận hiệu quả của riêng MINORI Ultra Grow.

Khi các nguồn khác nhau, **nhãn Minori là nguồn cho chỉ tiêu của thành phẩm**, tài liệu Van Iperen chỉ là nguồn cho nguyên liệu, còn bài báo khoa học là nguồn cho kết quả nghiên cứu của hoạt chất hoặc công thức đã được thử nghiệm. Không lấy chữ trên ảnh chai, ảnh sản phẩm Swissgrow/Newriver hoặc Agrifos Pro làm nguồn thay thế nhãn Minori.

## Hiện trạng đã quan sát trên trang live

- Menu đã có **Dưỡng Cây Khỏe Lá** và footer đã ghi **“Ba giai đoạn • Bốn lựa chọn”**. Giữ cấu trúc điều hướng này.
- Trang có `section.product-hero` với H1 **“Khỏe cây để đi đường dài.”**, nhãn **“20–45 ngày sau sạ”**, ảnh ruộng lúa và thumbnail chai. Ảnh hiện tham chiếu `../assets/minori-ultra-grow.svg`.
- `section.product-full-view` chiếm diện tích lớn để hiển thị lại cùng ảnh chai/nhãn. `section#vai-tro` và `.effect-section` lặp các thông điệp “khỏe rễ, khỏe cây, tăng sức chống chịu, chuẩn bị làm đòng”. Cuối trang có `.next` dẫn đến Vô Gạo Pro Max và liên kết Dưỡng Cây Khỏe Lá.
- Trang hiện **chưa có** bảng thành phần dạng text, hướng dẫn dùng rõ ràng, Q&A và nguồn nghiên cứu. Meta description vẫn là câu giới thiệu chung.
- Ở viewport khoảng **1280 px**, trang có tràn ngang (`scrollWidth` khoảng **1476 px**), menu bị cắt một phần. Tìm nguyên nhân trong layout/header và sửa để không còn cuộn ngang ngoài ý muốn.

## Kết quả nội dung cần có

### 1. Hero rõ tên sản phẩm và định vị cao cấp

- Dùng **một H1 duy nhất** có tên sản phẩm, ví dụ: **“MINORI Ultra Grow – Dưỡng cây chuyên sâu giữa vụ”**. Có thể giữ câu “Khỏe cây để đi đường dài” làm tagline phụ nếu không lặp ý.
- Tóm tắt ngắn: **“Công thức potassium phosphite 30–20, dành cho nhịp dưỡng cây chuyên sâu giữa vụ.”** Đặt cạnh ảnh ruộng và chai hiện có, tạo cảm giác cao cấp bằng khoảng trắng, phân cấp chữ, sắc xanh đậm và điểm nhấn tinh tế; không dùng huy hiệu chứng nhận giả, ngôi sao đánh giá hoặc hứa hẹn năng suất.
- Nhãn **20–45 ngày sau sạ** chỉ là **khung theo dõi giữa vụ thường gặp**, thay đổi theo giống và mùa. Không trình bày số ngày này như lịch phun bắt buộc. Nếu giữ badge, thêm giải thích ngắn gần đó hoặc trong phần hướng dẫn.
- Nếu dùng CTA, ưu tiên **“Xem thành phần”** và **“Xem hướng dẫn sử dụng”**, trỏ tới anchor thật trong trang.

### 2. Bảng thành phần đọc được bằng text

Tạo section `#thanh-phan` với bảng HTML hoặc thẻ thông số có nhãn rõ ràng. **Dữ liệu chính xác trên PDF Minori**:

| Chỉ tiêu trên nhãn | Giá trị |
| --- | ---: |
| Lân hữu hiệu | 30% |
| Kali hữu hiệu | 20% |
| Tỷ trọng | 1,5 |
| pH H₂O | 6,5 |
| Phương thức sử dụng | Bón lá |

Không ghi `w/w` cạnh 30% và 20% trong bảng nhãn Minori vì PDF không ghi đơn vị đó. Nếu giải thích tài liệu Van Iperen, nói rõ **P₂O₅/K₂O quy đổi 30/20 theo w/w là số liệu của nguyên liệu**, không tự đồng nhất toàn bộ thông số vật lý của hai tài liệu. Chữ thành phần và cách dùng phải là HTML text, không chỉ nằm trong ảnh SVG.

### 3. Câu chuyện công thức và nghiên cứu quốc tế

- Diễn đạt **potassium phosphite là một hợp chất riêng**, khác việc trộn hai nguồn lân và kali thông thường. Nêu nền tảng công thức được nghiên cứu về phản ứng sinh lý của cây, hướng đến chăm bộ rễ, hoạt động của lá và khả năng thích nghi trong giai đoạn sinh trưởng mạnh.
- Tạo khối “**Nền tảng hoạt chất được nghiên cứu quốc tế**” với 2–3 thẻ ngắn, nguồn liên kết ngay tại thẻ:
  - **Lúa mì:** nghiên cứu đăng trên *Frontiers in Plant Science* ghi nhận thay đổi tích cực ở đặc điểm rễ, sinh khối rễ, enzyme nitrate reductase và quang hợp dưới các điều kiện thí nghiệm.
  - **Lúa:** nghiên cứu trên giống Nipponbare ghi nhận thay đổi biểu hiện gene liên quan đến đáp ứng của cây và mô lá cây con dày hơn đối chứng.
  - **Đồng ruộng lúa:** một nghiên cứu tại Uruguay có đánh giá potassium phosphite cuối làm đòng đến đầu trổ; nghiên cứu tập trung vào bệnh thân/bẹ và điều kiện thí nghiệm riêng, nên chỉ nêu phạm vi nghiên cứu, không chuyển kết quả năng suất sang sản phẩm Minori.
- Văn phong tự tin, gọn, dễ đọc. Không viết rằng **MINORI Ultra Grow được tổ chức quốc tế chứng nhận hoặc kiểm chứng hiệu quả** khi nguồn chỉ nghiên cứu hoạt chất/công thức khác. Không tự thêm phần trăm tăng năng suất, cam kết “mọi ruộng đều hiệu quả” hoặc tuyên bố phòng/trị bệnh ngoài hồ sơ được phép.
- Giữ một câu giải thích khoa học chính xác: **“Phosphite khác phosphate; sản phẩm không thay thế nguồn lân phosphate trong chương trình dinh dưỡng thông thường.”** Không diễn giải 30% lân hữu hiệu trên nhãn thành “30% lân phosphate dễ hấp thu”.

### 4. Chăm cây giữa vụ và hướng dẫn dùng trên nhãn

- Tái cấu trúc `#vai-tro` và `.effect-section`: chọn một vị trí chính để nói về **hấp thụ dinh dưỡng, nền rễ, hoạt động bộ lá, hỗ trợ hệ thống đề kháng** theo nhãn và nghiên cứu; bỏ các ý hoặc khẩu hiệu lặp nhau. Có thể giữ sơ đồ hành trình nếu nó giúp hiểu mối nối **rễ → thân lá → làm đòng**, nhưng không dùng mũi tên như cam kết nhân quả hoặc hiệu quả chắc chắn.
- Giữ thông điệp: Ultra Grow là lựa chọn **chăm cây chuyên sâu giữa vụ** trong quy trình quản lý nước và dinh dưỡng cân đối. Cụm “hỗ trợ hệ thống đề kháng” có trên nhãn; không biến thành “trị bệnh” hay công bố bệnh cụ thể trên trang lúa khi chưa đối chiếu hồ sơ cuối.
- Tạo section `#huong-dan-su-dung` có bảng hoặc các bước dễ quét. **Trích đúng dữ liệu nhãn:**
  - Pha **1 lít sản phẩm với 400–800 lít nước**.
  - Với **cây lương thực**: **1,5–2 lít/ha/vụ**, sử dụng **2–3 lần/ha/vụ** vào giai đoạn **bón lót, bón thúc**.
  - Phun vào **sáng sớm hoặc chiều mát**.
  - Nhấn mạnh **1,5–2 lít/ha/vụ là tổng lượng cho cả vụ**, không phải liều cho mỗi lần phun. Không tự tính liều cho bình 16/25 lít nếu nhãn chưa đưa ra.
- PDF ghi **“Phương thức sử dụng: Bón lá”** nhưng phần hướng dẫn dùng chữ **“phun (tưới)”**. Ghi bất nhất này trong báo cáo bàn giao để tôi đối chiếu bản nhãn cuối; đừng tự sửa thành một hướng dẫn mới. Mốc 20–45 ngày sau sạ không được thay thế cụm thời điểm trên nhãn.

### 5. Q&A, ảnh và liên kết cuối trang

- Thêm **4 Q&A ngắn** ở gần cuối: (1) công thức Ultra Grow khác gì; (2) potassium phosphite được nghiên cứu về tác dụng gì; (3) 30–20 nghĩa là gì; (4) pha và dùng cho lúa thế nào. Lấy câu trả lời từ bài Markdown đã biên tập, đồng bộ bảng thành phần và hướng dẫn ở trên. Có thể dùng `<details><summary>` hoặc accordion có `button`, `aria-expanded`, hỗ trợ bàn phím; nội dung vẫn đọc được khi JS lỗi.
- Giữ hình chai `minori-ultra-grow.svg` và chức năng phóng to nếu asset đúng với bản được duyệt. Hiện một hình chai xuất hiện ở hero và được lặp rất lớn ở `product-full-view`; cân lại thứ bậc để **nội dung sản phẩm và cách dùng không bị đẩy xuống quá sâu**. Không tạo thêm render chai mới. Nếu ảnh nhãn hiện còn chỗ trống hoặc lỗi chữ, không gọi đó là “nhãn chuẩn”; chờ asset đã sửa và liệt kê trong bàn giao.
- Giữ liên kết đến **MINORI Dưỡng Cây Khỏe Lá** (cùng giai đoạn) và **MINORI Vô Gạo Pro Max** (giai đoạn tiếp theo). Tránh so sánh Dưỡng Cây Khỏe Lá như lựa chọn kém chất lượng; điểm cao cấp của Ultra Grow đến từ nền tảng công thức và cách trình bày.

## Điểm cần rà trước khi xuất bản

PDF nằm trong thư mục `APPROVED_LABELS`, nhưng nội dung trích xuất còn hai chỗ **“[chờ đối chiếu hồ sơ]”** ở phần chủ thể/xuất xứ và lô/NSX/HSD. Tên nhà sản xuất trong PDF được viết **“VAN INPEREN INTERNATIONNAL B.V.”**, địa chỉ **“Midsweg”**; tài liệu hãng viết **Van Iperen International B.V., Smidsweg**. PDF Minori ghi **tỷ trọng 1,5**, trong khi TDS nguyên liệu Van Iperen ghi **1,39 ± 0,01 kg/L**. Hãy **ghi riêng các điểm lệch này trong báo cáo bàn giao** và đề xuất nơi cần sửa ở asset/nhãn. Không tự chỉnh nội dung pháp lý trên ảnh, không suy diễn nguồn gốc lô hàng, không công bố “nhập khẩu 100% nguyên chai” nếu chưa có chứng từ tương ứng. Việc triển khai nội dung và layout cục bộ vẫn tiếp tục; các câu cần xác nhận được đánh dấu để duyệt trước khi đăng.

## SEO, responsive và kiểm tra hoàn thành

- Title và meta description phải nêu **MINORI Ultra Grow**, **potassium phosphite 30–20** và mục đích chăm cây giữa vụ bằng câu tự nhiên. Canonical giữ `https://minorivn.com/ultra-grow/`. Dùng H1 duy nhất, H2/H3 theo thứ bậc, alt text đúng ảnh, anchor rõ nghĩa và liên kết nguồn hoạt động.
- Nếu dùng Product/FAQ structured data, chỉ đưa thông tin nhìn thấy trên trang và đã được xác thực; không thêm giá, đánh giá, sao, chứng nhận hoặc tác dụng điều trị chưa có nguồn.
- Kiểm tra desktop, tablet, mobile: menu, bảng thành phần, Q&A, modal ảnh, CTA, focus và tương phản chữ trên nền ảnh/glass. Khắc phục **tràn ngang ở 1280 px** và kiểm tra các breakpoint lân cận; không che bớt menu để giấu lỗi layout. Hỗ trợ `prefers-reduced-motion` cho hiệu ứng.
- Chạy kiểm tra/build có sẵn, kiểm tra mọi liên kết và lỗi console. Bàn giao **danh sách file sửa, ảnh chụp desktop/mobile, URL preview, các nội dung đã thay/xóa vì trùng ý và danh sách điểm còn cần đối chiếu nhãn**. Không tự deploy.

## Nguồn khoa học để đối chiếu

- [Van Iperen – Potassium Phosphite 50% Liquid, TDS](https://www.vaniperen.com/wp-content/uploads/dlm_uploads/2017/12/VII-TDS-EN-EL-Potassium-Phosphite-50-Liquid-27-11-2017-681-1.pdf): thông tin **nguyên liệu**, xuất xứ Hà Lan, P₂O₅/K₂O quy đổi 30/20 w/w, tỷ trọng 1,39 ± 0,01 kg/L.
- [University of Florida IFAS – Phosphite và phosphate](https://ask.ifas.ufl.edu/publication/HS254): hai dạng có vai trò dinh dưỡng khác nhau.
- [Mohammed và cộng sự, *Frontiers in Plant Science* (2022)](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.1017048/full): nghiên cứu phosphite trên lúa mì.
- [Huang và cộng sự, *Plants* (2020)](https://www.mdpi.com/2223-7747/9/10/1334): nghiên cứu phosphite trên lúa con.
- [Martínez và cộng sự, *Crop Protection* (2016), FAO AGRIS](https://agris.fao.org/search/en/providers/122535/records/65e00c6f63b8185d9cb0ea2b): thử nghiệm trên ruộng lúa Uruguay, có bối cảnh bệnh thân/bẹ.
