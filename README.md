# Hướng dẫn Vận hành Quy trình viết PRD Tự động

Tài liệu này hướng dẫn cách sử dụng công cụ PRD Writer và quy trình vận hành chi tiết, giúp người mới có thể hiểu cách hệ thống hoạt động và cách tương tác để đạt được kết quả chất lượng nhất.

---

## 1. Tổng quan Quy trình (The Automated HITL Pipeline)

Quy trình viết PRD được điều phối bởi **Master PRD Writer** (`prd-writer.md`), giúp chuyển đổi các yêu cầu thô từ người dùng thành một tài liệu PRD hoàn chỉnh, chuẩn mực và có thể xuất ra file DOCX.

Quy trình bao gồm 6 bước chính với sự tham gia của con người ở những điểm quyết định (Human-in-the-loop - HITL):

### Bước 0: Xác nhận nhu cầu Sơ đồ (Clarification)

- Hệ thống sẽ xác định xem tính năng có cần sử dụng/vẽ Diagram (BPMN, Activity, Sequence) hay không.
- Nếu bạn chưa đề cập, hệ thống có nhiệm vụ phải dừng lại và hỏi bạn loại biểu đồ mong muốn để lên kế hoạch phù hợp.

### Bước 1: Tiền xử lý dữ liệu (Input Router)

- Yêu cầu thô của bạn được đưa qua công cụ `input-router` để chuẩn hóa thành cấu trúc JSON rành mạch (gồm Feature Name, User Flow, Business Logic và các Edge Cases).
- Dữ liệu thô này được lưu trữ theo chuẩn Domain (ví dụ `/domain-knowledge/[Tên_Domain]/inputs/`).
- **Lưu ý quan trọng:** Bạn sẽ được xem và xét duyệt hoặc bổ sung thông tin cho bản JSON này (đặc biệt là các phần thông tin bị thiếu - đánh dấu là `[CẦN_LÀM_RÕ]`) trước khi hệ thống chuyển sang bước viết nháp.

### Bước 2: Chuẩn bị Kiến thức Domain & Framework

- Hệ thống sẽ tự động tổng hợp những business rules và nguyên tắc thiết kế trước đó của Domain tương ứng.
- Áp dụng nghiêm ngặt các tiêu chuẩn tạo User Story và JTBD (đảm bảo theo chuẩn INVEST và phủ kín các test cases).

### Bước 3: Viết bản thảo (Drafting)

- Từ dữ liệu JSON sinh ra ở Bước 1, hệ thống tạo bản nháp PRD dưới dạng Markdown.
- Lưu trữ vào đúng thư mục `/PRDs/` của Domain.

### Bước 4: Kiểm định Chất lượng (PRD Reviewer)

- Bản nháp được đưa cho `prd-reviewer` - đóng vai QA Product Manager - để săm soi các lỗ hổng logic, missing edge cases...
- Các bình luận kiểm định (*Reviewer's Note*) sẽ được chèn trực tiếp (inline) vào dưới các đoạn có vấn đề trong file nháp chứa đề xuất giải pháp, giúp quá trình đối chiếu cực kỳ trực quan.

### Bước 5: Phê duyệt của Người dùng (CRITICAL PAUSE)

- **Hệ thống sẽ BẮT BUỘC chững lại ở điểm này để bạn xét duyệt.**
- Bạn sẽ đưa ra những yêu cầu thay đổi, điểu chỉnh đối với bản PRD (đã bao gồm các Reviewer's Notes). Lặp lại quá trình này cho đến khi bạn đưa ra lệnh "Đồng ý" hoặc "Approve".

### (Tùy chọn) Bước 5.5: Tạo Wireframe/UI (Stitch MCP)

- Dựa vào PRD đã chốt, nếu có định nghĩa hiển thị trên UI, hệ thống sẽ gọi MCP để tự động tạo ứng dụng và tạo ra các bản vẽ Wireframe/Preview trực quan.

### Bước 6: Xuất file (Docx Converter)

- Khi quá trình "Approve" được xác nhận, hệ thống kết xuất nội dung Markdown cuối cùng để xuất thành file Word (.docx) và trả đường dẫn file về cho bạn.

---

## 2. Hướng dẫn Người dùng: Cấu trúc Input "Chuẩn mực"

Thực tế, dữ liệu bạn đưa vào ở **Bước 1** quyết định 80% chất lượng của PRD được sinh ra. Để tiết kiệm thời gian hỏi/đáp và tránh việc logic sinh ra bị rỗng (`[CẦN_LÀM_RÕ]`), người dùng nên cung cấp luồng thông tin thô đáp ứng được những yếu tố cơ bản sau:

1. **Tên tính năng & Mục tiêu cốt lõi (Business Value):** Tính năng này là gì? Giải quyết vấn đề gì của người dùng hoặc có giá trị như thế nào đối với doanh nghiệp (Business)?
2. **Luồng người dùng cơ bản (User Flow):** Đường đi suôn sẻ (*Happy path*) diễn ra như thế nào? Ví dụ: Bước 1 user nhấn nút X > Bước 2 hệ thống hiển thị màn hình Y.
3. **Logic và Ràng buộc (Business Rules & Edge Cases):** Điều kiện đầu vào là gì? Điều kiện trừ tiền/cộng điểm/chặn truy cập là gì? Nếu người dùng rớt mạng, bị timeout hệ thống, hoặc hết số dư thì hiển thị lỗi gì?
4. **Nhu cầu về Sơ đồ (Diagrams):** Nêu rõ nếu bạn muốn có thêm Sequence diagram, BPMN hay Activity Diagram.

**Ví dụ một Input lý tưởng:**  
> *"Làm cho anh tính năng Lì xì nhóm trong dịp Tết. Mục tiêu: tăng tương tác user. User flow: Từ màn hình chính -> Chọn Lì xì nhóm -> Nhập Lời chúc, Nhập tổng tiền 200k -> Chọn chế độ Chia ngẫu nhiên cho 10 người -> Bấm Gửi -> Chia sẻ liên kết vào group chat -> Các user bấm link để nhận tiền đưọc random. Edge case: Nếu user thứ 11 bấm vào thì báo hết lượt. Nếu người gửi Lì xì khi gửi mà số dư không đủ => Báo pop-up lỗi yêu cầu nạp tiền. Cần vẽ Sequence Diagram."*

Cung cấp Input càng chất lượng thì PRD xuất ra càng hoàn hảo, chuẩn xác và hạn chế lỗi.

---

## 3. Lưu ý: Khi nào KHÔNG cần dùng toàn bộ luồng PRD?

Luồng hoạt động 6 bước cực kì lý tưởng đối với các Tính năng lớn (Epics/Features).

Tuy nhiên, nếu người dùng có **quy mô dự án nhỏ**, hoặc **chỉ có nhu cầu tạo ra các cấu trúc tài liệu đơn lẻ** (Ví dụ: Bạn chỉ cần viết vài User Story lẻng tẻng để tạo ticket Jira, hoặc lên khung JTBD), bạn có thể **bỏ qua quy trình PRD này để tiết kiệm thời gian**.

Lúc đó, hãy tham khảo hoặc yêu cầu LLM gọi ngay các Skills (Kỹ năng) riêng biệt đã sẵn sàng tại các thư mục:

- **Để tạo Jobs-to-be-Done (JTBD):** Tham khảo tại `/knowledge-base/knowledge/jobs-to-be-done/SKILL.md`
- **Để tạo User Story đạt chuẩn INVEST:** Tham khảo tại `/knowledge-base/knowledge/user-story-skill/SKILL.md`

Điều này đảm bảo luồng công việc của bạn được tinh gọn và tiết kiệm nguồn lực một cách tối đa.
