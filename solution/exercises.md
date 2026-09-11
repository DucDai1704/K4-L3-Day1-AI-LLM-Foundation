# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 4 tiếng
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng *Câu trả lời của bạn* bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi call_openai với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
Khi gọi với Temperature = 0.0, câu trả lời rất an toàn, rập khuôn và lặp lại giống hệt nhau nếu chạy nhiều lần. Khi tăng dần lên 0.5 và 1.0, AI bắt đầu sáng tạo hơn, dùng từ ngữ phong phú và đa dạng hơn. Tuy nhiên ở mức rất cao (1.5), câu trả lời bắt đầu trở nên lủng củng, dùng từ khó hiểu và lạ

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
Đối với chatbot CSKH, tôi sẽ chọn temperature rất thấp (từ 0.0 đến 0.2). Lý do là vì chatbot CSKH cần cung cấp thông tin chuẩn xác, đáng tin cậy theo đúng tài liệu và chính sách công ty, tuyệt đối không được phép tự ý "sáng tạo" hay bịa ra thông tin làm sai lệch chính sách.

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
Giá output của GPT-4o là 0.010 USD/1K token, trong khi GPT-4o-mini chỉ là 0.0006 USD. Suy ra GPT-4o đắt hơn GPT-4o-mini khoảng 16.6 lần. 
- Nên dùng GPT-4o cho: Các bài toán cần suy luận logic phức tạp, lập trình, phân tích số liệu tài chính.
- Nên dùng mini cho: Các tác vụ khối lượng lớn, lặp đi lặp lại như tóm tắt bài viết, CSKH thông thường, phân loại văn bản.

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi chat_with_system_prompt hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
Persona "giáo viên tiểu học" cho câu trả lời ngắn gọn, dùng từ vựng đơn giản (sổ liên lạc, cuốn vở) và nhiều ví dụ so sánh gần gũi. Persona "chuyên gia tài chính" sử dụng nhiều thuật ngữ chuyên ngành (sổ cái phân tán, mã hóa học, phi tập trung) và dài hơn. Điều này cho thấy System prompt đóng vai trò như "kim chỉ nam", định hình hoàn toàn giọng điệu, mức độ phức tạp và cấu trúc văn bản của model.

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo count_tokens
(tiktoken) với ước lượng số từ / 0.75 mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
Số token đếm bằng tiktoken thường cao hơn phương pháp chia 0.75 khoảng từ 1.5 đến 2 lần. Lý do là vì các bộ tokenizer của OpenAI được đào tạo tối ưu chủ yếu cho tiếng Anh (1 từ tiếng Anh thường là 1 token). Với tiếng Việt, do dấu câu và từ ghép, một từ tiếng Việt thường bị băm nhỏ (tokenize) thành 2-3 mảnh token khác nhau, dẫn đến tốn nhiều token và chi phí hơn.

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
Streaming rất quan trọng trong các giao diện tương tác trực tiếp với người dùng (chatbot như ChatGPT), đặc biệt khi câu trả lời dài, giúp người dùng có thể đọc ngay lập tức mà không có cảm giác chờ đợi. Ngược lại, non-streaming phù hợp hơn ở các hệ thống chạy ngầm (backend API), nơi cần tổng hợp toàn bộ kết quả để bóc tách dữ liệu (parse JSON) rồi mới lưu vào database hoặc xử lý tiếp.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
Exponential backoff giúp giảm áp lực liên tục lên server đang bị quá tải bằng cách dãn cách thời gian thử lại ngày càng thưa hơn. Nếu hàng nghìn client cùng dùng delay cố định 1 giây, chúng sẽ đồng loạt gọi lại cùng một lúc sau 1 giây, tạo ra hiện tượng "Thundering Herd" (hiệu ứng bầy đàn), làm sập server thêm lần nữa.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
Persona: "Bạn là một lập trình viên Python senior nhiệt tình. Hãy trả lời ngắn gọn, luôn cung cấp code ví dụ và giải thích bằng tiếng Việt."
Lựa chọn "ngắn gọn" giúp tiết kiệm token/chi phí; "luôn cung cấp code" đảm bảo luôn có kết quả thực hành trực quan; "bằng tiếng Việt" để tránh việc AI ngẫu hứng trả lời bằng tiếng Anh đối với các từ khóa chuyên ngành.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
Hạn chế lớn nhất hiện tại là lịch sử chỉ lưu 3 lượt gần nhất, khiến AI sẽ quên mất bối cảnh ở đầu cuộc trò chuyện nếu cuộc chat kéo dài.
Cách cải thiện: Sử dụng một model phụ giá rẻ chạy ngầm để liên tục tóm tắt (summarize) lịch sử cũ, sau đó đẩy đoạn tóm tắt này vào System Prompt. Như vậy AI sẽ luôn nhớ được cốt lõi câu chuyện mà không làm tràn bộ nhớ token.

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] \python grade.py\ — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder \solution/\, push lên fork và dán link trên trang bài Lab ở VLearn trước 23:59 ngày 11/09/2026
