## Team Workflow

## สมาชิกในกลุ่ม
- Member 1 นายศุภกฤต แก้วแกมทอง รหัสนักศึกษา 663380404-9 
- Member 2 นายอรรนพ แสงศิลา     รหัสนักศึกษา 663380413-8 
- Member 3 นายภูชิต จำปาชน       รหัสนักศึกษา 663380611-4 


## Work Flow Procress
1. Set up : Member 2  สร้างโฟลเดอร์และไฟล์ต่างๆเบื้องต้น และเขียน main เพื่อรับ input
2. Quick Sort : Member 2 เขียน Algoritym ของ Quick Sort
3. Buble Sort : Member 3 เขียน Algoritym ของ Buble Sort
4. Main Program : Member 1 เขียน main เพื่อรับค่า input (Integer) และตัวเลือก Algoritym ที่ใช้
5. Merge and Commit : เมื่อแต่ละคนทำหน้าที่ในส่วนของตัวเองเสร็จเรียบร้อยแล้วให้ commit และ push ขึ้นบน sever github
6. Final Project : ทุกคนทำการ merge งานของตัวเองเข้ากับ branch main



### ขั้นตอนทำงานบน git และ github 

## ขั้นตอนที่ 1. configuration(ตั้งค่าเบื้องต้น) 
1. กำหนดชื่อและอีเมลของตัวเอง
- git config --global user.name "ชื่อตัวเอง"
- git config --global user.email "Email ของตัวเอง"


## ขั้นตอนที่ 2. lnitialize (เริ่มต้นทำโปรเจค) 
1. คัดลอกโปรเจกต์ Github
- git clone https://github.com/kku-computer-science/configuration-management-using-git-the-skubik-team.git

## ขั้นตอนที่ 3. Basic workflow(แผนการทำงาน)
1. ตรวจเช็คสถานะ
- git status

2. เลือกไฟล์ที่เราเพิ่มหรือโค้ดที่เราเขียนไปยัง Staging Area
- git add . (เลือกทุกไฟล์)
- git add <ตามด้วยชื่อไฟล์> (สำหรับเลือกไฟล์นั้นๆเท่านั้น)

3. บันทึกประวัติจาก Staging Area ไปที่ repository พร้อมข้อมความกำกับ
- git commit -m "ข้อความ"

## ขั้นตอนที่ 4. Branching (สาขาของเราและคนในทีม)
1. สร้าง Branch และไปที่ Branch ใหม่
- git checkout -b <ชื่อ branch ของเรา>

2. สลับกลับมา Branch เดิม
- git checkout <ชื่อ branch เดิม>

## ขั้นตอนที่ 5. Remote (ทำงาานบน sever)
1. ส่งงานขึ้นบน sever
- git push origin <ชื่อ Branch ของเรา>

2. ดึงงานจาก Server
git pull origin <ชื่อ Branch ของเรา>