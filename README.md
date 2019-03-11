# AlphaPilot_test2

Upload date: 10/3/2019

Code Explanation:
1. แปลงรูปจากรูปสีให้เป็นรูปขาวดำ
2. cropรูปให้เล็กลง 10% เพื่อลดส่วนที่ไม่สำคัทิ้ง 
3. ทำการหาขอบของรูปภาพที่มีสีขวา
4. ชดเชยตำแหน่งของขอบรูป และปรับตำแหน่งให้ถูกต้อง
5. loop เพื่อหาขอบรูปพื้นที่สีขาวทั้งหมดในรูป
6. หาขอบรูปที่มีขนาดใหญ่ที่สุด
7. วาดกรอบสีเขียวเพื่อแสดงขอบรูปที่หาได้
8. generate มุมของขอบรูปทั้งหมด 4 จุด
9. generate json file


Step-by-Step Compile

1. Transform image to B/W

![alt text](https://github.com/chunmusic/AlphaPilot_test2/blob/master/Screenshot%20from%202019-03-11%2021-32-17.png)

![alt text](https://github.com/chunmusic/AlphaPilot_test2/blob/master/Screenshot%20from%202019-03-11%2021-52-00.png)


2. Lower image size

![alt text](https://github.com/chunmusic/AlphaPilot_test2/blob/master/Screenshot%20from%202019-03-11%2021-54-06.png)

![alt text](https://github.com/chunmusic/AlphaPilot_test2/blob/master/Screenshot%20from%202019-03-11%2021-55-37.png)


3.Find white bg // 4. Compensate and correct contours of photos 

![alt text](https://github.com/chunmusic/AlphaPilot_test2/blob/master/Screenshot%20from%202019-03-11%2022-00-33.png)


5. Find all white bg photos of which have area more than 10000.

![alt text](https://github.com/chunmusic/AlphaPilot_test2/blob/master/Screenshot%20from%202019-03-11%2022-02-58.png)


6. Draw contour on photo

![alt text](https://github.com/chunmusic/AlphaPilot_test2/blob/master/Screenshot%20from%202019-03-11%2022-13-30.png)

![alt text](https://github.com/chunmusic/AlphaPilot_test2/blob/master/Screenshot%20from%202019-03-11%2022-16-02.png)


