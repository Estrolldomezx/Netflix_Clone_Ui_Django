# Netflix_Clone_Ui_Django
3SB04 Django-python framework
- คำอธิบาย
- manage.py เป็นไฟล์ script ไว้รันคำสั่งต่างๆ ที่เกี่ยวข้องกับตัว framework เช่น runserver
- init.py ไว้สำหรับเก็บ package ของ python เพื่อเพิ่ม script ในการทำงานได้
- settings.py ใช้สำหรับ ตั้งค่าโปรเจ็ค เช่น เวลา, path, database และอื่นๆที่เกี่ยวข้อง
- urls.py ใช้สำหรับ routing HTTP request หรือกำหนดแพทเทิร์นของ url ของโปรเจ็ค
- wsgi.py ใช้เก็บข้อมูลสำหรับการ deployment (ไม่ได้ใช้)
- ในส่วนของ Django จะทำการ routing ไปหา url ของโปรเจ็ค แล้วเข้าไปใน view เพื่อเก็บพวก model และ template ซึ่ง model จะเป็นส่วนที่เก็บข้อมูล และ template จะเก็บข้อมูลการประมวลผลที่ได้จาก view มาแสดงร่วมกับ html
