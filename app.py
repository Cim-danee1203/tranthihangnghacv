<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CV - Trần Thị Hằng Nga</title>

<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>
:root {
  --navy: #17324d;
  --blue: #315b78;
  --light: #eef3f6;
  --text: #263746;
  --muted: #647789;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Be Vietnam Pro', sans-serif;
  background: #e8edf1;
  color: var(--text);
  line-height: 1.7;
  padding: 35px 15px;
}

.cv {
  max-width: 1000px;
  margin: auto;
  background: white;
  display: grid;
  grid-template-columns: 310px 1fr;
  box-shadow: 0 12px 45px rgba(20,40,60,.12);
  border-radius: 12px;
  overflow: hidden;
}

/* LEFT COLUMN */
.sidebar {
  background: var(--navy);
  color: white;
  padding: 42px 30px;
}

.avatar {
  width: 125px;
  height: 125px;
  border-radius: 50%;
  background: #dce7ee;
  color: var(--navy);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 38px;
  font-weight: 700;
  margin: 0 auto 25px;
  border: 5px solid rgba(255,255,255,.25);
}

.sidebar h2 {
  font-size: 16px;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  border-bottom: 1px solid rgba(255,255,255,.35);
  padding-bottom: 9px;
  margin: 28px 0 16px;
}

.sidebar p, .sidebar li {
  font-size: 12.5px;
  color: #e0e9ef;
  margin-bottom: 10px;
  overflow-wrap: anywhere;
}

.sidebar ul {
  padding-left: 18px;
}

.contact-item {
  margin-bottom: 13px;
}

.contact-item strong {
  display: block;
  color: #9fc3dc;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* RIGHT COLUMN */
.main {
  padding: 48px 42px;
}

.name {
  color: var(--navy);
  font-size: 31px;
  line-height: 1.3;
  font-weight: 800;
  letter-spacing: -.5px;
}

.position {
  color: var(--blue);
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  margin-top: 10px;
}

.intro {
  font-size: 12.5px;
  color: var(--muted);
  margin-top: 18px;
  padding-bottom: 23px;
  border-bottom: 2px solid var(--light);
}

.section {
  margin-top: 27px;
}

.section-title {
  color: var(--navy);
  font-size: 17px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 15px;
}

.section-title:after {
  content: "";
  height: 1px;
  background: #dce5eb;
  flex: 1;
}

.entry {
  margin-bottom: 19px;
}

.entry h3 {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--navy);
}

.entry .sub {
  color: var(--blue);
  font-size: 11.5px;
  font-weight: 600;
  margin: 3px 0 7px;
}

.entry p, .entry li {
font-size: 12px;
  color: var(--muted);
}

.entry ul {
  padding-left: 18px;
}

.tag {
  display: inline-block;
  background: var(--light);
  color: var(--navy);
  padding: 6px 11px;
  margin: 4px 3px 4px 0;
  border-radius: 5px;
  font-size: 11px;
  font-weight: 600;
}

.download {
  display: block;
  margin: 22px auto;
  padding: 12px 25px;
  background: var(--navy);
  color: white;
  border: none;
  border-radius: 7px;
  font-family: inherit;
  font-weight: 600;
  cursor: pointer;
  font-size: 13px;
}

.download:hover {
  background: var(--blue);
}

@media(max-width: 700px) {
  body { padding: 10px; }
  .cv { grid-template-columns: 1fr; }
  .sidebar { padding: 30px; }
  .main { padding: 30px 25px; }
  .name { font-size: 26px; }
}

@media print {
  @page {
    size: A4;
    margin: 0;
  }

  body {
    padding: 0;
    background: white;
    print-color-adjust: exact;
    -webkit-print-color-adjust: exact;
  }

  .cv {
    width: 210mm;
    max-width: none;
    min-height: 297mm;
    border-radius: 0;
    box-shadow: none;
  }

  .download {
    display: none;
  }
}
</style>
</head>

<body>

<div class="cv">

  <!-- SIDEBAR -->
  <aside class="sidebar">

    <div class="avatar">
    <img src="avatar.jpg" alt="Trần Thị Hằng Nga">
</div>

    <h2>Thông tin liên hệ</h2>

    <div class="contact-item">
      <strong>Điện thoại</strong>
      <p>0945345307</p>
    </div>

    <div class="contact-item">
      <strong>Email</strong>
      <p>hngacute289@gmail.com</p>
    </div>

    <div class="contact-item">
      <strong>Địa chỉ</strong>
      <p>Thành phố Hồ Chí Minh, Việt Nam</p>
    </div>

    <div class="contact-item">
      <strong>Ngày sinh</strong>
      <p>28/09/2007</p>
    </div>

    <h2>Chứng chỉ</h2>
    <ul>
      <li>IELTS 6.5</li>
      <li>Microsoft Office Specialist (MOS) Word</li>
    </ul>

    <h2>Kỹ năng chuyên môn</h2>
    <ul>
      <li>Tiếng Anh trong giao tiếp và môi trường học tập, làm việc.</li>
      <li>Soạn thảo và trình bày văn bản bằng Microsoft Word.</li>
      <li>Tìm kiếm, tổng hợp và xử lý thông tin.</li>
      <li>Quản lý, sắp xếp và lưu trữ tài liệu.</li>
      <li>Kiến thức nền tảng về kinh doanh quốc tế.</li>
    </ul>

    <h2>Kỹ năng mềm</h2>
    <ul>
      <li>Giao tiếp và làm việc nhóm.</li>
      <li>Quản lý thời gian.</li>
      <li>Tư duy logic và giải quyết vấn đề.</li>
      <li>Chủ động học hỏi, thích nghi.</li>
      <li>Cẩn thận và có trách nhiệm.</li>
    </ul>

  </aside>

  <!-- MAIN CONTENT -->
  <main class="main">

    <h1 class="name">TRẦN THỊ HẰNG NGA</h1>

    <p class="position">Import - Export Intern</p>

    <p class="intro">
      Sinh viên năm 2 ngành Kinh doanh quốc tế tại Trường Đại học
Tài chính – Marketing. Có nền tảng tiếng Anh tốt, khả năng
      giao tiếp, tìm kiếm và xử lý thông tin. Mong muốn được vận dụng
      kiến thức chuyên ngành vào môi trường doanh nghiệp, đồng thời
      tích lũy kinh nghiệm thực tế trong lĩnh vực xuất nhập khẩu và
      logistics.
    </p>

    <section class="section">
      <h2 class="section-title">Mục tiêu nghề nghiệp</h2>

      <div class="entry">
        <p>
          Trong ngắn hạn, mong muốn trở thành thực tập sinh xuất nhập khẩu,
          được tiếp cận quy trình xử lý đơn hàng, chứng từ xuất nhập khẩu,
          khai báo hải quan và phối hợp với các bên liên quan. Đồng thời,
          phát triển khả năng sử dụng tiếng Anh trong công việc chuyên môn.
        </p>
        <br>
        <p>
          Trong dài hạn, định hướng phát triển trở thành nhân viên xuất nhập
          khẩu chuyên nghiệp, có khả năng xử lý nghiệp vụ độc lập, am hiểu
          quy trình thương mại quốc tế và đóng góp vào hoạt động của doanh nghiệp.
        </p>
      </div>
    </section>

    <section class="section">
      <h2 class="section-title">Học vấn</h2>

      <div class="entry">
        <h3>ĐẠI HỌC TÀI CHÍNH – MARKETING (UFM)</h3>
        <p class="sub">2025 – Hiện tại | Sinh viên năm 2</p>
        <p>Chuyên ngành: Kinh doanh quốc tế</p>
        <p>
          Được trang bị kiến thức nền tảng về thương mại quốc tế,
          hoạt động kinh doanh, kinh tế và môi trường kinh doanh toàn cầu.
        </p>
      </div>
    </section>

    <section class="section">
      <h2 class="section-title">Kinh nghiệm làm việc</h2>

      <div class="entry">
        <h3>GIA SƯ / TRỢ GIẢNG ĐỘC LẬP</h3>
        <p class="sub">Kinh nghiệm giảng dạy và hỗ trợ học tập</p>
        <ul>
          <li>Hỗ trợ học viên trong quá trình học tập, ôn tập và củng cố kiến thức.</li>
          <li>Chủ động chuẩn bị, sắp xếp tài liệu và xây dựng kế hoạch học tập.</li>
          <li>Trao đổi, phối hợp với phụ huynh và học viên để theo dõi tiến độ.</li>
          <li>Rèn luyện kỹ năng giao tiếp, quản lý thời gian và xử lý tình huống.</li>
        </ul>
      </div>

      <div class="entry">
        <h3>ĐỊNH HƯỚNG PHÁT TRIỂN CHUYÊN MÔN</h3>
        <p class="sub">Lĩnh vực Xuất nhập khẩu và Logistics</p>
        <ul>
          <li>Chủ động tìm hiểu kiến thức về thương mại quốc tế và quy trình xuất nhập khẩu.</li>
          <li>Quan tâm đến nghiệp vụ chứng từ, vận tải quốc tế và thủ tục hải quan.</li>
        </ul>
      </div>
    </section>

    <section class="section">
<h2 class="section-title">Năng lực nổi bật</h2>

      <span class="tag">IELTS 6.5</span>
      <span class="tag">MOS Word</span>
      <span class="tag">International Business</span>
      <span class="tag">Communication</span>
      <span class="tag">Document Management</span>
      <span class="tag">Teamwork</span>
      <span class="tag">Problem Solving</span>
    </section>

    <section class="section">
      <h2 class="section-title">Định hướng phát triển</h2>
      <div class="entry">
        <p>
          Không ngừng trau dồi ngoại ngữ, kiến thức nghiệp vụ và kỹ năng
          chuyên môn; sẵn sàng tiếp nhận thử thách mới, học hỏi từ đồng nghiệp
          và thích nghi với môi trường làm việc chuyên nghiệp.
        </p>
      </div>
    </section>

  </main>
</div>

<button class="download" onclick="window.print()">
  TẢI CV / LƯU DƯỚI DẠNG PDF
</button>

</body>
</html>
