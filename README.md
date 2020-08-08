# Mã nguồn : Python + Scrapy

name :tên của spider và không được đặt các name giống nhau.<br/>
allowed_domains:vùng cho phép crawl dữ liệu.<br/>
start_urls:<br/>
Hàm parse(self,response):hàm gọi để xử lý phản hồi được tải xuống và thực hiện các chức năng:<br/>
Kiểm tra xem link đó có phải là link cần crawl không (tránh crawl các link rác)<br/>
Sau khi kiểm tra thì ghi lại :link, category, time, title, subtitle, content, source, tags ra file .tex.<br/>
yield from : cho phép chỉ tiến hành crawl trên các bài báo có dạng: "https://vnexpress.net/" hoặc "/". và callback lại parse.<br/>

# Các công việc đã thực hiện được: lấy được link, category, thời gian, tiêu đề, tiêu đề con, nội dung, tác giả và tag của một bài viết.
# Kết quả : đã thu nhập được 9441 bài viết trừ trang https://vnexpress.net/ và các bài viết được đặt trong file TuoiTre.txt nằm trong mục Tuoitre
