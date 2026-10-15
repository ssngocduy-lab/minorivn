# Prompt cho Antigravity + Gemini: cập nhật trang MINORI Root Turbo

Bạn là người phụ trách giao diện và nội dung website Minori Agritech. Hãy kiểm tra **mã nguồn thực tế** của trang `https://minorivn.com/root-turbo/` trong dự án được mở, rồi tích hợp chọn lọc nội dung từ file `minori-root-turbo-bai-gioi-thieu.md`. Chỉ sửa mã nguồn cục bộ và bàn giao bản để duyệt; không tự triển khai lên website đang chạy.

## Nguồn nội dung ưu tiên cho lần cập nhật này

**Dữ liệu text Minori Agritech cung cấp là nguồn nội dung biên tập cần bám sát.** Ảnh `root-turbo.svg` hiện là ảnh chai cũ và đang được thay mới. **Không đọc chữ trên ảnh đó để suy ra hoặc sửa thành phần, xuất xứ hay nội dung bài viết; không nêu sự khác biệt giữa ảnh cũ và text trong giao diện.** Sau này Minori Agritech sẽ thay file ảnh. Trong mã nguồn, giữ chỗ hiển thị ảnh linh hoạt để thay asset mà không phải sửa lại nội dung và bố cục. Tránh gắn nội dung pháp lý quan trọng vào ảnh; hiển thị bằng HTML text để dễ đọc và cập nhật.

Thông tin thành phần cần dùng trong nội dung mới:

| Thành phần | Hàm lượng |
| --- | ---: |
| Chất hữu cơ (Organic Matter) | 40% |
| Fulvic Acid | 19% |
| Amino Acid | 16% |
| Đạm tổng số (N) | 2% |

Đây là thông tin/công thức tham chiếu Minori Agritech cung cấp. Trước khi xuất bản chính thức, đối chiếu với nhãn mới và hồ sơ công bố/kiểm nghiệm của đúng sản phẩm. Nếu tài liệu còn thiếu, vẫn thiết kế và chuẩn bị bản cục bộ theo bảng này, nhưng đánh dấu điểm cần xác thực trong phần bàn giao; không tự thay bằng số liệu lấy từ ảnh cũ.

## Trang hiện tại và hướng sắp xếp

Trang hiện có hero **“Muốn cây khỏe, phải bắt đầu từ rễ.”**, mốc **7–20 ngày sau sạ**, ảnh rễ lúa và chai sản phẩm; khối **“Hình ảnh đầy đủ MINORI Root Turbo”**; khối **“Giai đoạn đầu vụ cần điều gì?”** nêu vấn đề rễ yếu, đất phèn, rơm rạ, ngộ độc hữu cơ, hấp thu phân kém, đẻ nhánh chậm; khối **“Vai trò của Root Turbo”** với chuỗi rễ khỏe → bung rễ trắng → hấp thu tốt → đẻ nhánh mạnh; cuối trang liên kết sang Ultra Grow. Hãy xác nhận lại bằng mã nguồn vì trang có thể thay đổi.

1. Kiểm tra framework, component, CSS, nguồn ảnh, metadata, heading và responsive hiện có. Lập bảng “nội dung cũ / nội dung bài mới / quyết định giữ, gộp, sửa hoặc bỏ”. Mục tiêu là mỗi ý chính chỉ xuất hiện ở một vị trí phù hợp. Nếu hero đã nói về vai trò của rễ, phần sau cần bổ sung thông tin cụ thể thay vì diễn đạt lại cùng ý.
2. Đề xuất bố cục dễ đọc: hero gọn; vấn đề đầu vụ; MINORI Root Turbo giúp gì; bảng/thẻ bốn thành phần; section nguồn gốc và kiểm chứng; cách theo dõi ruộng và sử dụng theo nhãn; nội dung mở rộng/FAQ; liên kết sang Ultra Grow. Có thể thay thứ tự khi mã nguồn và trải nghiệm thực tế cho thấy phương án khác hợp lý hơn. Giữ khả năng thay ảnh chai thuận tiện và chức năng phóng to ảnh nếu vẫn hữu ích sau khi ảnh mới được cập nhật.
3. Tích hợp bài giới thiệu **có chọn lọc**. Rút gọn các đoạn giải thích khoa học để dễ quét trên điện thoại. Không chép toàn bộ bài ~700 từ vào một khối dài; dùng heading, đoạn ngắn, thẻ thông tin và liên kết “Tìm hiểu thêm”. Không lặp lại bảng thành phần ở nhiều nơi trên trang.
4. Thiết kế một `section`/`div` nổi bật với tiêu đề **“Công nghệ Nhật Bản – Kiểm chứng trên đồng ruộng Việt Nam”**, có nền, hình/đồ họa, khoảng trắng và tương phản nhất quán với nhận diện Minori. Nội dung cần thể hiện đúng thông tin Minori Agritech cung cấp: nguồn gốc từ nhà máy sản xuất tại Nhật Bản; doanh nghiệp kiểm tra nguồn gốc và đối chiếu sản phẩm; sản phẩm được theo dõi, thử nghiệm nhiều năm trên khu ruộng hơn 20 mẫu trước khi giới thiệu. Viết chuyên nghiệp, dùng tên **Minori Agritech** như một công ty, không gọi là hoạt động “của gia đình”. Trước khi xuất bản, kiểm tra hồ sơ nhà máy, vai trò cụ thể của công nghệ Nhật Bản và tài liệu khảo nghiệm. Nếu chưa có hồ sơ, vẫn hoàn thiện thiết kế section nhưng ghi rõ claim chờ xác thực trong bản bàn giao và dùng câu chữ có quy thuộc như “Theo thông tin Minori Agritech cung cấp”; không tự thêm lịch sử/quy mô của đối tác Nhật, chứng nhận, kết quả so sánh hoặc mức tăng năng suất.
5. Với phần dài, hiển thị tóm tắt và nút **“Xem thêm” / “Thu gọn”**; có thể dùng dấu `…` làm tín hiệu phụ nhưng không dùng riêng `…` làm nhãn. Ưu tiên `<details>/<summary>` hoặc `<button>` thật với `aria-expanded`, `aria-controls`, trạng thái focus rõ và điều khiển bằng bàn phím. Đảm bảo trình đọc màn hình đọc được nội dung, không giấu bảng thành phần hoặc hướng dẫn an toàn trong vùng thu gọn.
6. Thiết kế responsive ưu tiên điện thoại: chữ và bảng dễ đọc, thẻ không dày, khoảng cách thoáng, ảnh có thể co giãn khi asset được thay, không cuộn ngang, CTA rõ. Kiểm tra trên điện thoại, máy tính bảng và desktop.
7. SEO: một H1, H2/H3 đúng thứ bậc, title và meta description tự nhiên, canonical đúng URL hiện hành, alt text cho ảnh, liên kết nội bộ hợp lý. Nếu dùng Product/FAQ schema, chỉ đưa dữ liệu đã xác thực. Không thêm review, xếp hạng, chứng nhận, giá hoặc claim năng suất khi không có nguồn.
8. Chạy các kiểm tra sẵn có, xem giao diện ở nhiều kích thước, thử nút mở rộng bằng bàn phím/chuột và kiểm tra ảnh phóng to. Bàn giao danh sách file đã sửa, ảnh chụp desktop/mobile, bảng nội dung đã gộp/bỏ, danh sách điểm chờ xác minh. Không deploy khi chưa được Minori Agritech duyệt.

## Nguyên tắc kiểm chứng

- Bảng thành phần và nội dung nguồn gốc ở trên là thông tin **Minori Agritech cung cấp cho lần chỉnh sửa này**. Bám sát text đó; đối chiếu hồ sơ của đúng sản phẩm trước khi đăng live.
- Nghiên cứu khoa học về chất hữu cơ, Fulvic Acid, Amino Acid và đạm chỉ giải thích cơ chế/tiềm năng chung; không biến thành tuyên bố hiệu quả đã được chứng minh cho công thức MINORI Root Turbo.
- Không tự suy diễn liều dùng, thời gian tác dụng, năng suất, chất lượng hạt, chứng nhận, quan hệ với nhà máy hoặc địa điểm thử nghiệm ngoài thông tin được cung cấp. Khi thiếu bằng chứng, ghi câu hỏi cần Minori Agritech trả lời trong phần bàn giao.

Tài liệu nền cho phần giải thích chung: [FAO về chất hữu cơ trong đất](https://www.fao.org/4/a0100e/a0100e04.htm), [nghiên cứu Fulvic Acid trên lúa](https://pmc.ncbi.nlm.nih.gov/articles/PMC11271057/), [nghiên cứu chế phẩm thủy phân protein trên lúa](https://www.aeeisp.com/jnau/en/article/id/64e4a499-ae1a-4085-be52-74329f983d3b), [IRRI về đạm cho lúa](https://www.knowledgebank.irri.org/ericeproduction/PDF_%26_Docs/fs_nitrogen.pdf).
