使用的資料為 台電所提供的 2017/1/2至2019/2/28的資料，提供的資料包刮
    1.日期 2.淨尖峰供電能力(MW) 3.尖峰負載(MW) 4.備轉容量(MW) 5.備轉容量率(%)
其中，上述的1.2.4.5為輸入的X，3為輸出的Y，以此為作為LinearRegression線性回歸模型輸入輸出
再利用台電自身預測4/2至4/8的1.2.4.5作為輸入，求出作業希望的尖峰負載(MW
