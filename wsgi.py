#@+leo-ver=5-thin
#@+node:2014fall.20141212095015.1775: * @file wsgi.py
# coding=utf-8
# 上面的程式內容編碼必須在程式的第一或者第二行才會有作用

################# (1) 模組導入區
# 導入 cherrypy 模組, 為了在 OpenShift 平台上使用 cherrypy 模組, 必須透過 setup.py 安裝


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:2014fall.20141212095015.1776: ** <<declarations>> (wsgi)
import cherrypy
# 導入 Python 內建的 os 模組, 因為 os 模組為 Python 內建, 所以無需透過 setup.py 安裝
import os
# 導入 random 模組
import random
# 導入 gear 模組
import gear
import man3
import menuLink1
import  index_all
import man2
################# (2) 廣域變數設定區
# 確定程式檔案所在目錄, 在 Windows 下有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
#1 設定在雲端與近端的資料儲存目錄
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    download_root_dir = os.environ['OPENSHIFT_DATA_DIR']
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
else:
    # 表示程式在近端執行
    download_root_dir = _curdir + "/local_data/"
    data_dir = _curdir + "/local_data/"

'''以下為近端 input() 與 for 迴圈應用的程式碼, 若要將程式送到 OpenShift 執行, 除了採用 CherryPy 網際框架外, 還要轉為 html 列印
# 利用 input() 取得的資料型別為字串
toprint = input("要印甚麼內容?")
# 若要將 input() 取得的字串轉為整數使用, 必須利用 int() 轉換
repeat_no = int(input("重複列印幾次?"))
for i in range(repeat_no):
    print(toprint)
'''
#@-<<declarations>>
#@+others
#@+node:2014fall.20141212095015.1777: ** class Hello
################# (3) 程式類別定義區
# 以下改用 CherryPy 網際框架程式架構
# 以下為 Hello 類別的設計內容, 其中的 object 使用, 表示 Hello 類別繼承 object 的所有特性, 包括方法與屬性設計
class Hello(object):

    # Hello 類別的啟動設定
    _cp_config = {
    'tools.encode.encoding': 'utf-8',
    'tools.sessions.on' : True,
    'tools.sessions.storage_type' : 'file',
    #'tools.sessions.locking' : 'explicit',
    # session 以檔案儲存, 而且位於 data_dir 下的 tmp 目錄
    'tools.sessions.storage_path' : data_dir+'/tmp',
    # session 有效時間設為 60 分鐘
    'tools.sessions.timeout' : 60
    }

    #@+others
    #@+node:2014fall.20141212095015.1778: *3* index_orig
    # 以 @ 開頭的 cherrypy.expose 為 decorator, 用來表示隨後的成員方法, 可以直接讓使用者以 URL 連結執行
    @cherrypy.expose
    # index 方法為 CherryPy 各類別成員方法中的內建(default)方法, 當使用者執行時未指定方法, 系統將會優先執行 index 方法
    # 有 self 的方法為類別中的成員方法, Python 程式透過此一 self 在各成員方法間傳遞物件內容
    def index_orig(self, toprint="Hello World!"):
        return toprint
    #@+node:2014fall.20141212095015.2004: *3* __init__
    def __init__(self):
        # 配合透過案例啟始建立所需的目錄
        if not os.path.isdir(data_dir+'/tmp'):
            os.mkdir(data_dir+'/tmp')
        if not os.path.isdir(data_dir+"/downloads"):
            os.mkdir(data_dir+"/downloads")
        if not os.path.isdir(data_dir+"/images"):
            os.mkdir(data_dir+"/images")
    #@+node:2014fall.20141212095015.1779: *3* hello
    @cherrypy.expose
    def hello(self, toprint="Hello World!"):
        return toprint
    #@+node:2014fall.20141215194146.1791: *3* index
    @cherrypy.expose
    def a_40223151(self):
        return'''
                <html>
                40223151
                </html>
                '''
    def index(self):
        outstring=''' 
    <html>
    <font size='6' color='darkslateblue' face='標楷體' >
    協同產品設計分組報告
    </font><br />
     <font size='4' color='darkslateblue' face='標楷體' >
    第八組 40223151網站
    <br />
    </html>'''
        outstring +='''
    <html>
    <br />
    <br />
    <table border=3>
　 <tr>
　　 <th><font size="4">小組名單</font></th>
　　 <th><font size="4"></font></th>
    </tr>
　 <tr>
　　 <th><font size="4"><a href="http://2015cdag8-40223124.rhcloud.com/" target="_blank">小組openshift</a></font></th>
　　 <th><font size="4"><a href="https://github.com/mm112287/2015cda_g8" target="_blank">小組github</a></font></th>
    </tr>
　 <tr rowspan="2">
　　 <th><font size='4' color='yellow' ><a href="http://cd0427-40223151.rhcloud.com/" target="_blank">40223151簡正斌</a> </font></th>
　　 <th><font size="4"><a href="http://cd0427-40223110.rhcloud.com/" target="_blank">40223110王常浩</a></font></th>
　 </tr>
　 <tr>
　　 <th><font size="4"><a href="http://cd0427-40223124.rhcloud.com/" target="_blank">40223124袁丞宗 </a></font></th>
　　 <th><font size="4"><a href="http://cd0427-40223129.rhcloud.com/" target="_blank">40223129許家瑋 </a></font></th>
    </tr>
　 <tr>
　　 <th><font size='4' color='yellow' ><a href="http://2015springcda-40223149.rhcloud.com/" target="_blank">40223149賴涵餘</a></font></th>
　　 <th><font size="4"><a href="http://2015cd0505-40223150.rhcloud.com/" target="_blank">40223150謝俊宇</a></font></th>
    </tr>
　 <tr>
　　 <th><font size="4">40223145劉兆銓</font></th>
　　 <th></th>
    </tr>



    </table>
    </font>
    </html>'''
        outstring  += self.index2()
        return outstring
    index.exposed = True
    def test1(self, K=None, N=None, inp2=None):
        # 將標準答案存入 answer session 對應區
        theanswer = random.randint(1, 100)
        thecount = 0
        # 將答案與計算次數變數存進 session 對應變數
        cherrypy.session['answer'] = theanswer
        cherrypy.session['count'] = thecount
        # 印出讓使用者輸入的超文件表單
        outstring ='''<font size='6' color='darkslateblue' face='標楷體' >垂直齒輪七齒</font>'''
        outstring = self.menuLink2()
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()" bgcolor='azure' link='darkorenge' vlink='darkorenge '>        
    <form method=\"post\" action=\"mytest1\">
    <fieldset>
    <legend>考試協同七個齒輪齒輪參數表單值:</legend>
    齒數1:<br />
    <input type=\"text\" name=\"N\"value="24"><br />
    齒數2:<br />
    <input list="ng1" name="ng1" value="15">
    <datalist id="ng1">
    <option value="10">10</option>
    <option value="15">15</option>
    <option value="20">20</option>
    <option value="25">25</option>
    <option value="30">30</option>
    <option value="35">35</option>
    <option value="40">40</option>
    <option value="45">45</option>
    <option value="50">50</option>
    </datalist><br />
    齒數3:<br />
    <input list="ng2" name="ng2" value="15">
    <datalist id="ng2">
    <option value="10">10</option>
    <option value="15">15</option>
    <option value="20">20</option>
    <option value="25">25</option>
    <option value="30">30</option>
    <option value="35">35</option>
    <option value="40">40</option>
    <option value="45">45</option>
    <option value="50">50</option>
    </datalist><br /><br />
    齒數4: <br />
    <input list="ng3" name="ng3" value="24">
    <datalist id="ng3">
    <option value="10">10</option>
    <option value="15">15</option>
    <option value="20">20</option>
    <option value="25">25</option>
    <option value="30">30</option>
    <option value="35">35</option>
    <option value="40">40</option>
    <option value="45">45</option>
    <option value="50">50</option>
    </datalist><br />
    齒數5:<br />
    <input list="ng4" name="ng4" value="15">
    <datalist id="ng4">
    <option value="10">10</option>
    <option value="15">15</option>
    <option value="20">20</option>
    <option value="25">25</option>
    <option value="30">30</option>
    <option value="35">35</option>
    <option value="40">40</option>
    <option value="45">45</option>
    <option value="50">50</option>
    </datalist><br />
    齒數6:<br />
    <input list="ng5" name="ng5" value="15">
    <datalist id="ng5">
    <option value="10">10</option>
    <option value="15">15</option>
    <option value="20">20</option>
    <option value="25">25</option>
    <option value="30">30</option>
    <option value="35">35</option>
    <option value="40">40</option>
    <option value="45">45</option>
    <option value="50">50</option>
    </datalist><br />
    齒數7:<br />
    <input list="ng6" name="ng6" value="24">
    <datalist id="ng6">
    <option value="10">10</option>
    <option value="15">15</option>
    <option value="20">20</option>
    <option value="25">25</option>
    <option value="30">30</option>
    <option value="35">35</option>
    <option value="40">40</option>
    <option value="45">45</option>
    <option value="50">50</option>
    </datalist><br /><br />
    模數:<br />
    <input type=\"text\" name=\"K\" value="15"><br />
    壓力角:<br />
    <input type=\"text\" name=\"inp2\" value="15"><br />
    <input type=\"submit\" value=\"確定\">
    <input type=\"reset\" value=\"重填\">'''+self.menuLink()+'''
    </form>
    </body>
    </html>
    '''
        return outstring
    test1.exposed = True  




    def mytest1(self, K=None, N=None,ng1=None, ng2=None, ng3=None, ng4=None, ng5=None, ng6=None, inp2=None):
        try:
            你的數字 = int(N)
            你的數字1= int(K)
            你的數字2 = int(ng1)
            你的數字3 = int(ng2)
            你的數字4 = int(ng3)
            你的數字5 = int(ng4)
            你的數字6 = int(ng5)
            你的數字7 = int(ng6)
            你的數字8 = int(inp2)

        except:
            return "請輸入 15 到 80 間的整數!<br />"+"<br /><a href='test1'>再試一次!<br /><a href='/'>回首頁</a>"
        # html 表單
        outstring = '''    
        <form method=\"post\" action=\"mytest1\">
        <fieldset>
        <legend>垂直齒輪七齒:</legend>
        齒數1:<br />
        <input type=\"text\" name=\"N\"value="24"><br />
        齒數2:<br />
        <input list="ng1" name="ng1" value="15">
        <datalist id="ng1">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數3:<br />
        <input list="ng2" name="ng2" value="15">
        <datalist id="ng2">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br /><br />
        齒數4: <br />
        <input list="ng3" name="ng3" value="24">
        <datalist id="ng3">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數5:<br />
        <input list="ng4" name="ng4" value="15">
        <datalist id="ng4">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數6:<br />
        <input list="ng5" name="ng5" value="15">
        <datalist id="ng5">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數7:<br />
        <input list="ng6" name="ng6" value="24">
        <datalist id="ng6">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br /><br />
        模數:<br />
        <input type=\"text\" name=\"K\" value="15"><br />
        壓力角:<br />
        <input type=\"text\" name=\"inp2\" value="15"><br />
        <input type=\"submit\" value=\"確定\">
        <input type=\"reset\" value=\"重填\">'''

        if int(80) < 你的數字 or int(80)<你的數字2 or int(80)<你的數字1 or int(80)<你的數字3 or int(80)<你的數字4 or int(80)<你的數字5 or int(80)<你的數字6 or int(80)<你的數字7 or int(80)<你的數字8:
            outString = '太大了<br /><br />'
            outString += "請輸入 15 到 80 間的整數!<br />"+"<br /><a href='test1'>再試一次!<br /><a href='/'>回首頁</a>"

        elif int(15) > 你的數字 or int(15)>你的數字2 or int(15)>你的數字1 or int(15)>你的數字3 or int(15)>你的數字4 or int(15)>你的數字5 or int(15)>你的數字6 or int(15)>你的數字7 or int(15)>你的數字8 :
            outString = '太小了<br /><br />'
            outString += "請輸入 15 到 80 間的整數!<br />"+"<br /><a href='test1'>再試一次!<br /><a href='/'>回首頁</a>"

        else:
            outString = ""
            outString +="藍色，齒數1:"+N
            outString += "<br />"
            outString +="黑色，齒數2:"+ng1
            outString += "<br />"
            outString +="紅色，齒數3:"+ng2
            outString += "<br />"
            outString +="咖啡色，齒數4:"+ng3
            outString += "<br />"
            outString +="綠色，齒數5:"+ng4
            outString += "<br />"
            outString +="黃色，齒數6:"+ng5
            outString += "<br />"
            outString +="粉紅色，齒數7:"+ng6
            outString += "<br />"
            outString +="模數:"+K
            outString += "<br />"
            outString +="壓力角:"+inp2
            outString += "<br />"
            outString += self.menuLink()
            outString += '''
        <!DOCTYPE html> 
        <html>
        <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
        <!-- 載入 brython.js -->
        <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
        <script src="/static/Cango2D.js" type="text/javascript"></script>
        <script src="/static/gearUtils-04.js" type="text/javascript"></script>
        </head>
        <!-- 啟動 brython() -->
        <body onload="brython()">

        <!-- 以下為 canvas 畫圖程式 -->
        <script type="text/python">
        # 從 browser 導入 document
        from browser import document
        from math import *
        # 請注意, 這裡導入位於 Lib/site-packages 目錄下的 spur.py 檔案
        import spur

        # 準備在 id="plotarea" 的 canvas 中繪圖
        canvas = document["plotarea"]
        ctx = canvas.getContext("2d")
        # 以下利用 spur.py 程式進行繪圖, 接下來的協同設計運算必須要配合使用者的需求進行設計運算與繪圖
        # 其中並將工作分配給其他組員建立類似 spur.py 的相關零件繪圖模組
        # midx, midy 為齒輪圓心座標, rp 為節圓半徑, n 為齒數, pa 為壓力角, color 為線的顏色
        # Gear(midx, midy, rp, n=20, pa=20, color="black"):
        # 模數決定齒的尺寸大小, 囓合齒輪組必須有相同的模數與壓力角
        # 壓力角 pa 單位為角度
        pa = '''+str(inp2)+'''
        # m 為模數
        m = '''+str(K)+'''
        # 第1齒輪齒數
        n_g1 = '''+str(N)+'''
        # 第2齒輪齒數
        n_g2 = '''+str(ng1)+'''
        n_g3 = '''+str(ng2)+'''
        n_g4 = '''+str(ng3)+'''
        n_g5 = '''+str(ng4)+'''
        n_g6 = '''+str(ng5)+'''
        n_g7 = '''+str(ng6)+'''
        # 計算兩齒輪的節圓半徑
        rp_g1 = m*n_g1/2
        rp_g2 = m*n_g2/2
        rp_g3 = m*n_g3/2
        rp_g4 = m*n_g4/2
        rp_g5 = m*n_g5/2
        rp_g6 = m*n_g6/2
        rp_g7 = m*n_g7/2
        #齒輪嚙合的旋轉角
        # 將第1齒輪順時鐘轉 90 度
        th1 = 0
        th2 = pi-pi/n_g2
        # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
        th3 =-pi/2-pi/n_g3+(pi/2)*rp_g1/ rp_g3
        # 將第3齒輪逆時鐘轉 90 度之後, 再往回轉第2齒輪定位帶動轉角, 然後再逆時鐘多轉一齒, 以便與第2齒輪進行囓合
        # 第1個 -pi/2 為將原先垂直的第3齒輪定位線逆時鐘旋轉 90 度
        # -pi/n_g3 則是第3齒與第2齒定位線重合後, 必須再逆時鐘多轉一齒的轉角, 以便進行囓合
        # (pi+pi/n_g2)*n_g2/n_g3 則是第2齒原定位線為順時鐘轉動 90 度, 
        # pi+pi/n_g2 為第2齒輪從順時鐘轉 90 度之後, 必須配合目前的標記線所作的齒輪 2 轉動角度, 要轉換到齒輪3 的轉動角度
        # 必須乘上兩齒輪齒數的比例, 若齒輪2 大, 則齒輪3 會轉動較快
        # 但是第2齒輪為了與第1齒輪囓合, 已經距離定位線, 多轉了 180 度, 再加上第2齒輪的一齒角度, 因為要帶動第3齒輪定位, 
        # 這個修正角度必須要再配合第2齒與第3齒的轉速比加以轉換成第3齒輪的轉角, 因此乘上 n_g2/n_g3
        th4 =-pi/n_g4-(pi/2)*rp_g1/ rp_g4+(-pi/2+pi/n_g3)*rp_g3/rp_g4

        th5 = -pi/2-pi/n_g5+(pi/2)*rp_g1/ rp_g5-(-pi/2+pi/n_g3)*rp_g3/rp_g5+(pi/2+pi/n_g4)*rp_g4/ rp_g5
        th6 =-pi/n_g6-(pi/2)*rp_g1/ rp_g6+(-pi/2+pi/n_g3)*rp_g3/rp_g6-(pi/2+pi/n_g4)*rp_g4/ rp_g6+(-pi/2+pi/n_g5)*rp_g5/rp_g6
        th7 =-pi/2-pi/n_g7+(pi/2)*rp_g1/ rp_g7-(-pi/2+pi/n_g3)*rp_g3/rp_g7+(pi/2+pi/n_g4)*rp_g4/ rp_g7-(-pi/2+pi/n_g5)*rp_g5/rp_g7+(pi/2+pi/n_g6)*rp_g6/ rp_g7


        # 將第1齒輪順時鐘轉 90 度
        # 使用 ctx.save() 與 ctx.restore() 以確保各齒輪以相對座標進行旋轉繪圖
        ctx.save()
        # translate to the origin of second gear
        ctx.translate(400,400)
        # rotate to engage
        ctx.rotate( th1)
        # put it back
        ctx.translate(-400,-400)
        spur.Spur(ctx).Gear(400,400,rp_g1,n_g1, pa, "blue")
        ctx.restore()
        ctx.font = "10px Verdana";
        ctx.fillText("",400-60, 400-10);

        # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
        ctx.save()
        # translate to the origin of second gear
        ctx.translate(400,400-rp_g1-rp_g2)
        # rotate to engage
        ctx.rotate( th2)
        # put it back
        ctx.translate(-400,-(400-rp_g1-rp_g2))
        spur.Spur(ctx).Gear(400,400-rp_g1-rp_g2,rp_g2,n_g2, pa, "black")
        ctx.restore()

        # 將第3齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
        ctx.save()
        # translate to the origin of second gear
        ctx.translate(400+rp_g1+rp_g3,400)
        # rotate to engage
        ctx.rotate( th3)
        # put it back
        ctx.translate(-(400+rp_g1+rp_g3),-400)
        spur.Spur(ctx).Gear(400+rp_g1+rp_g3,400,rp_g3,n_g3, pa, "red")
        ctx.restore()

        # 將第4齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
        ctx.save()
        # translate to the origin of second gear
        ctx.translate(400+rp_g1+rp_g3,400+rp_g3+rp_g4)
        # rotate to engage
        ctx.rotate( th4)
        # put it back
        ctx.translate(-(400+rp_g1+rp_g3),-(400+rp_g3+rp_g4))
        spur.Spur(ctx).Gear(400+rp_g1+rp_g3,400+rp_g3+rp_g4,rp_g4,n_g4, pa, "black")
        ctx.restore()

        # 將第5齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
        ctx.save()
        # translate to the origin of second gear
        ctx.translate(400+rp_g1+rp_g3+rp_g4+rp_g5,400+rp_g3+rp_g4)
        # rotate to engage
        ctx.rotate( th5)
        # put it back
        ctx.translate(-(400+rp_g1+rp_g3+rp_g4+rp_g5),-(400+rp_g3+rp_g4))
        spur.Spur(ctx).Gear(400+rp_g1+rp_g3+rp_g4+rp_g5,400+rp_g3+rp_g4,rp_g5,n_g5 ,pa, "green")
        ctx.restore()

        # 將第6齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
        ctx.save()
        # translate to the origin of second gear
        ctx.translate(400+rp_g1+rp_g3+rp_g4+rp_g5,400+rp_g3+rp_g3+rp_g4+rp_g6)
        # rotate to engage
        ctx.rotate( th6)
        # put it back
        ctx.translate(-(400+rp_g1+rp_g3+rp_g4+rp_g5),-(400+rp_g3+rp_g3+rp_g4+rp_g6))
        spur.Spur(ctx).Gear(400+rp_g1+rp_g3+rp_g4+rp_g5,400+rp_g3+rp_g3+rp_g4+rp_g6,rp_g6,n_g6 ,pa, "yellow")
        ctx.restore()

        # 將第7齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
        ctx.save()
        # translate to the origin of second gear
        ctx.translate(400+rp_g1+rp_g3+rp_g4+rp_g5+rp_g6+rp_g7,400+rp_g3+rp_g3+rp_g4+rp_g6)
        # rotate to engage
        ctx.rotate( th7)
        # put it back
        ctx.translate(-(400+rp_g1+rp_g3+rp_g4+rp_g5+rp_g6+rp_g7),-(400+rp_g3+rp_g3+rp_g4+rp_g6))
        spur.Spur(ctx).Gear(400+rp_g1+rp_g3+rp_g4+rp_g5+rp_g6+rp_g7,400+rp_g3+rp_g3+rp_g4+rp_g6,rp_g7,n_g7 ,pa, "pink")
        ctx.restore()
        # 假如第3齒也要進行囓合, 又該如何進行繪圖?
        #spur.Spur(ctx).Gear(400,400,100,12, pa, "red")

        </script>
        <canvas id="plotarea" width="3600" height="3600"></canvas>
        </body>
        </html>
        '''

        return outString
    mytest1.exposed = True

    def video1(self):
        outstring ='''<font size='6' color='darkslateblue' face='標楷體' >第一次考試影片</font>'''
        outstring += "</br>"
        outstring += self.menuLink2()
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring +="""
                            <body bgcolor='azure' link='darkorenge' vlink='darkorenge '>
                            <font size='5' color='darkslateblue' face='標楷體'>手動組立教學影片</font></br>
                            <iframe src="https://player.vimeo.com/video/130829329" width="500" height="375" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> </br>
                            影片網址:</br>
                            <a href="https://vimeo.com/130829329">cdag8-w16</a> </br>
                            <font size='5' color='darkslateblue' face='標楷體'>自動組立教學影片</font></br>
                            <iframe src="https://player.vimeo.com/video/130831129" width="500" height="375" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></br>
                            影片網址:</br>
                            <a href="https://vimeo.com/130831129">cdag8w16-2</a></br>
                            <font size='5' color='darkslateblue' face='標楷體'>程式頁面教學</font></br>
                            <iframe src="https://player.vimeo.com/video/130834938" width="500" height="375" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></br>
                            影片網址:</br>
                            <a href="https://vimeo.com/130834938">cdag8w16-3</a> </br>

                            </body>
                            """
        outstring += self.menuLink()
        return outstring
    video1.exposed = True
    def mas(self):
        outstring ='''<font size='6' color='darkslateblue' face='標楷體' >樂高人偶</font>'''
        outstring += "</br>"
        outstring += self.menuLink2()
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring +="""
                            <body bgcolor='azure' link='darkorenge' vlink='darkorenge '>
                            </body>
                            """
        outstring += self.menuLink()
        return outstring
    mas.exposed = True

    def Reviews(self):
        outstring ='''<font size='6' color='darkslateblue' face='標楷體' >心得</font>'''
        outstring += "</br>"
        outstring += self.menuLink2()
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring +="""
                        <body bgcolor='azure' link='darkorenge' vlink='darkorenge '>
                        <font size='3'>
                        <DT>心得:
                                <DD>我覺得這週一方面在了解期中考所做得程式跟七齒嚙合另一方面是讓我們可以跟小組同</br>
                                <DD>步分工，用最短的時間內更有效率的做事，在這個環境中了解到分工是多麼的重要也對程</br>
                                <DD>式更加了解。



                        </fon>
                        </body>
                            """
        outstring += self.menuLink()
        return outstring
    Reviews.exposed = True
    
    def index3(self):
        outstring ='''<font size='6' color='darkslateblue' face='標楷體' >個人影片</font>'''
        outstring += "</br>"
        outstring += self.menuLink2()
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring +='''<font size='3'>學號:40223151</font>'''
        outstring += "<br />"
        outstring +='''<font size='3'>姓名:簡正斌</font>'''
        outstring += "<br />"
        outstring += '''<font size='3'>班級:四設二甲</font>'''
        outstring += "<br />"
        outstring += """
                    <body bgcolor='azure' link='darkorenge' vlink='darkorenge '>
                    <font size='5' color='darkslateblue' face='標楷體'>七齒教學影片</font></br>
                    <iframe src="https://player.vimeo.com/video/128123220" width="500" height="375" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></br>
                    影片網址:
                    <font size='4'><a href="https://vimeo.com/128123220">2015cda w11</a></font></br>
                    <font size='5' color='darkslateblue' face='標楷體'>手動組立教學影片</font></br>
                    <iframe src="https://player.vimeo.com/video/130121112" width="500" height="375" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></br>
                    影片網址:
                    <a href="https://vimeo.com/130121112">cda8-w13</a></br>  
                    個人vimeo網站:
                    <font size='4'><a href="https://vimeo.com/user27353237">40223151@gm.nfu.edu.tw</font></a>
                    </br></br></body>



"""


        outstring += self.menuLink()
        return outstring
    index3.exposed = True
    def drawspur1(self, K=None, N=None, inp2=None):

        # 將標準答案存入 answer session 對應區
        theanswer = random.randint(1, 100)
        thecount = 0
        # 將答案與計算次數變數存進 session 對應變數
        cherrypy.session['answer'] = theanswer
        cherrypy.session['count'] = thecount
        # 印出讓使用者輸入的超文件表單
        outstring ='''<font size='6' color='darkslateblue' face='標楷體' >2015cda 期中上機考</font>'''
        outstring += self.menuLink2()
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += '''
    <!DOCTYPE html> 
    <html>
    <body bgcolor='azure' link='darkorenge' vlink='darkorenge '>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <font size='3'>
    <form method=\"post\" action=\"spuraction\">
        <fieldset>
        <legend>2015cda 期中上機考:</legend>
        學號:40223151<br />
        齒數:<br />
        <input type=\"text\" name=\"N\"><br />

        </select>
        模數:<br />
        <input type=\"text\" name=\"K\"><br />
        壓力角:<br />
        <input type=\"text\" name=\"inp2\"><br />
        <input type=\"submit\" value=\"確定\">
        <input type=\"reset\" value=\"重填\">
        <a href="index">首頁</a>
        <a href="gear">3D齒輪模式</a>
        <a href="spur">七顆齒輪</a>
        <a href="drawspur"> 2015cda 期中上機考一顆齒輪繪圖</a>
        <a href="drawspur1"> 2015cda 期中上機考表單文字輸出</a>
        <a href="index1"> 個人影片</a>
    </font>
    </form>
    </body>
    </html>
    '''

        return outstring
    drawspur1.exposed = True

 
    def drawspur(self, K=None, N=None, inp2=None):

          # 將標準答案存入 answer session 對應區
        theanswer = random.randint(1, 100)
        thecount = 0
        # 將答案與計算次數變數存進 session 對應變數
        cherrypy.session['answer'] = theanswer
        cherrypy.session['count'] = thecount
        # 印出讓使用者輸入的超文件表單
        outstring ='''<font size='6' color='darkslateblue' face='標楷體' >2015cda 期中上機考</font>'''
        outstring += self.menuLink2()
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += '''
    <!DOCTYPE html> 
    <html>
    <body bgcolor='azure' link='darkorenge' vlink='darkorenge '>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <font size='3'>
    <form method=\"post\" action=\"drawspuraction\">
        <fieldset>
        <legend>2015cda 期中上機考:</legend>
        學號:40223151<br />
        齒數:<br />
        <input type=\"text\" name=\"N\"><br />

        </select>
        模數:<br />
        <input type=\"text\" name=\"K\"><br />
        壓力角:<br />
        <input type=\"text\" name=\"inp2\"><br />
        <input type=\"submit\" value=\"確定\">
        <input type=\"reset\" value=\"重填\">
        <a href="index">首頁</a>
        <a href="gear">3D齒輪模式</a>
        <a href="spur">七顆齒輪</a>
        <a href="drawspur"> 2015cda 期中上機考一顆齒輪繪圖</a>
        <a href="drawspur1"> 2015cda 期中上機考表單文字輸出</a>
        <a href="index1"> 個人影片</a>
    </font>
    </form>
    </body>
    </html>
    '''

        return outstring
    drawspur.exposed = True

    #@+node:2015.20150330144929.1713: *3* twoDgear
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角

    def test2(self, K=None, N=None, inp2=None):
        # 將標準答案存入 answer session 對應區
        theanswer = random.randint(1, 100)
        thecount = 0
        # 將答案與計算次數變數存進 session 對應變數
        cherrypy.session['answer'] = theanswer
        cherrypy.session['count'] = thecount
        # 印出讓使用者輸入的超文件表單
        outstring ='''<font size='6' color='darkslateblue' face='標楷體' >垂直齒輪</font>'''
        outstring = self.menuLink2()
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()" bgcolor='azure' link='darkorenge' vlink='darkorenge '>        
    <form method=\"post\" action=\"doCheck\">
        <fieldset>
        <legend>垂直齒輪:</legend>
        齒數1:<br />
        <input type=\"text\" name=\"N\" value="24"><br />
        齒數2:<br />
        <input list="ng1" name="ng1" value="15">
        <datalist id="ng1">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        模數:<br />
        <input type=\"text\" name=\"K\" value="15"><br />
        壓力角:<br />
        <input type=\"text\" name=\"inp2\" value="15"><br />
        <input type=\"submit\" value=\"確定\">
        <input type=\"reset\" value=\"重填\">'''+self.menuLink()+'''
    </form>
    </body>
    </html>
    '''
        return outstring
    test2.exposed = True  

    def doCheck(self, K=None, N=None,ng1=None, inp2=None):
        # 假如使用者直接執行 doCheck, 則設法轉回根方法
        try:
            你的數字 = int(N)
            你的數字1= int(K)
            你的數字2 = int(ng1)
            你的數字3 = int(inp2)
        except:
            return "請輸入 15 到 80 間的整數!<br />"+"<br /><a href='test2'>再試一次!<br /><a href='/'>回首頁</a>"
        # html 表單
        outstring = '''    <form method=\"post\" action=\"doCheck\">
        <fieldset>
        <legend>考試協同七個齒輪齒輪參數表單值:</legend>
        齒數1:<br />
        <input type=\"text\" name=\"N\" value="24"><br />
        齒數2:<br />
        <input list="ng1" name="ng1" value="15">
        <datalist id="ng1">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        模數:<br />
        <input type=\"text\" name=\"K\" value="15"><br />
        壓力角:<br />
        <input type=\"text\" name=\"inp2\" value="15"><br />
        <input type=\"submit\" value=\"確定\">
        <input type=\"reset\" value=\"重填\">'''

        if int(80) < 你的數字 or int(80)<你的數字2 or int(80)<你的數字1 or int(80)<你的數字3 :
            outstring = '太大了<br /><br />'
            outstring += "請輸入 15 到 80 間的整數!<br />"+"<br /><a href='test2'>再試一次!<br /><a href='/'>回首頁</a>"

        elif int(15) > 你的數字 or int(15)>你的數字2 or int(15)>你的數字1 or int(15)>你的數字3:
            outstring = '太小了<br /><br />'
            outstring += "請輸入 15 到 80 間的整數!<br />"+"<br /><a href='test2'>再試一次!<br /><a href='/'>回首頁</a>"

        else:
            outstring = ""
            outstring +="黑色，齒數1:"+ng1
            outstring += "<br />"
            outstring +="藍色，齒數2:"+N
            outstring +="模數:"+K
            outstring += "<br />"
            outstring +="壓力角:"+inp2
            outstring += "<br />"
            outstring += self.menuLink()
            outstring += '''
    <!DOTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">

    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    from math import *
    # 請注意, 這裡導入位於 Lib/site-packages 目錄下的 spur.py 檔案
    import spur

    # 準備在 id="plotarea" 的 canvas 中繪圖
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")
    # 以下利用 spur.py 程式進行繪圖, 接下來的協同設計運算必須要配合使用者的需求進行設計運算與繪圖
    # 其中並將工作分配給其他組員建立類似 spur.py 的相關零件繪圖模組
    # midx, midy 為齒輪圓心座標, rp 為節圓半徑, n 為齒數, pa 為壓力角, color 為線的顏色
    # Gear(midx, midy, rp, n=20, pa=20, color="black"):
    # 模數決定齒的尺寸大小, 囓合齒輪組必須有相同的模數與壓力角
    # 壓力角 pa 單位為角度
    pa = '''+str(你的數字3)+'''
    # m 為模數
    m = '''+str(你的數字1)+'''
    # 第1齒輪齒數
    n_g1 = '''+str(你的數字)+'''
    # 第2齒輪齒數
    n_g2 = '''+str(你的數字2)+'''
    # 計算兩齒輪的節圓半徑
    rp_g1 = m*n_g1/2
    rp_g2 = m*n_g2/2
 #齒輪嚙合的旋轉角
# 將第1齒輪順時鐘轉 90 度
    th1 = 0

    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    th2 = pi+pi/n_g2
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400,400)
    # rotate to engage
    ctx.rotate( th1)
    # put it back
    ctx.translate(-400,-400)
    spur.Spur(ctx).Gear(400,400,rp_g1,n_g1, pa, "blue")
    ctx.restore()
    ctx.font = "10px Verdana";
    ctx.fillText("",400-60, 400-10);

    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400,400-rp_g1-rp_g2)
    # rotate to engage
    ctx.rotate( th2)
    # put it back
    ctx.translate(-400,-(400-rp_g1-rp_g2))
    spur.Spur(ctx).Gear(400,400-rp_g1-rp_g2,rp_g2,n_g2, pa, "black")
    ctx.restore()

    </script>
    <canvas id="plotarea" width="3600" height="3600"></canvas>
    </body>
    </html>
    '''
            
        return outstring
    doCheck.exposed = True

    @cherrypy.expose

    def spur(self, K=None, N=None, inp2=None):
        # 將標準答案存入 answer session 對應區
        theanswer = random.randint(1, 100)
        thecount = 0
        # 將答案與計算次數變數存進 session 對應變數
        cherrypy.session['answer'] = theanswer
        cherrypy.session['count'] = thecount
        # 印出讓使用者輸入的超文件表單
        outstring ='''<font size='6' color='darkslateblue' face='標楷體' >考試協同七個齒輪齒輪參數表單值</font>'''
        outstring = self.menuLink2()
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()" bgcolor='azure' link='darkorenge' vlink='darkorenge '>        
    <form method=\"post\" action=\"mygeartest2\">
        <fieldset>
        <legend>考試協同七個齒輪齒輪參數表單值:</legend>
        齒數1:<br />
        <input type=\"text\" name=\"N\"><br />
        齒數2:<br />
        <input list="ng1" name="ng1">
        <datalist id="ng1">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數3:<br />
        <input list="ng2" name="ng2">
        <datalist id="ng2">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br /><br />
        齒數4: <br />
        <input list="ng3" name="ng3">
        <datalist id="ng3">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數5:<br />
        <input list="ng4" name="ng4">
        <datalist id="ng4">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數6:<br />
        <input list="ng5" name="ng5">
        <datalist id="ng5">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br />
        齒數7:<br />
        <input list="ng6" name="ng6">
        <datalist id="ng6">
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="25">25</option>
        <option value="30">30</option>
        <option value="35">35</option>
        <option value="40">40</option>
        <option value="45">45</option>
        <option value="50">50</option>
        </datalist><br /><br />
        模數:<br />
        <input type=\"text\" name=\"K\"><br />
        壓力角:<br />
        <input type=\"text\" name=\"inp2\"><br />
        <input type=\"submit\" value=\"確定\">
        <input type=\"reset\" value=\"重填\">'''+self.menuLink()+'''
    </form>
    </body>
    </html>
    '''
        return outstring
    spur.exposed = True

    #@+node:2015.20150330144929.1713: *3* twoDgear
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角


    def twoDgear(self, N=20, M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">
        
    <form method=POST action=do2Dgear>
    齒數:<input type=text name=N><br />
    模數:<input type=text name=M><br />
    壓力角:<input type=text name=P><br />
    <input type=submit value=send>
    </form>
    </body>
    </html>
    '''

        return outstring
    #@+node:2015.20150330144929.1762: *3* do2Dgear
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def do2Dgear(self, N=20, M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">
    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    import math

    # 畫布指定在名稱為 plotarea 的 canvas 上
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")

    # 用紅色畫一條直線
    ctx.beginPath()
    ctx.lineWidth = 3
    '''
        outstring += '''
    ctx.moveTo('''+str(N)+","+str(M)+")"
        outstring += '''
    ctx.lineTo(0, 500)
    ctx.strokeStyle = "red"
    ctx.stroke()

    # 用藍色再畫一條直線
    ctx.beginPath()
    ctx.lineWidth = 3
    ctx.moveTo(0, 0)
    ctx.lineTo(500, 0)
    ctx.strokeStyle = "blue"
    ctx.stroke()

    # 用綠色再畫一條直線
    ctx.beginPath()
    ctx.lineWidth = 3
    ctx.moveTo(0, 0)
    ctx.lineTo(500, 500)
    ctx.strokeStyle = "green"
    ctx.stroke()

    # 用黑色畫一個圓
    ctx.beginPath()
    ctx.lineWidth = 3
    ctx.strokeStyle = "black"
    ctx.arc(250,250,50,0,2*math.pi)
    ctx.stroke()
    </script>
    <canvas id="plotarea" width="800" height="600"></canvas>
    </body>
    </html>
    '''

        return outstring
    #@+node:2014fall.20141215194146.1793: *3* doAct
    @cherrypy.expose
    def spuraction(self, K=None, N=None, inp2=None):
        inp3=int(N)*int(K)/2
        #inp 變數即為表單值, 其格式為字串
        outString = ""
        outString +="2015cda 期中上機考:"
        outString += "<br />"
        outString +="齒數:"+N
        outString += "<br />"
        outString +="模數:"+K
        outString += "<br />"
        outString +="壓力角:"+inp2
        outString += "<br />"
        outString += self.menuLink()

        return outString
    spuraction.exposed = True
    def drawspuraction (self, K=None, N=None, inp2=None):
        inp3=int(N)*int(K)/2
        #inp 變數即為表單值, 其格式為字串
        outString   = self.menuLink()
        outString += '''

    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.0-20150301-090019/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">
    <hr>
    <!-- 以下為 canvas 畫圖程式 -->
<script type="text/python">
# 從 browser 導入 document
from browser import document
from math import *

# 準備在 id="plotarea" 的 canvas 中繪圖
canvas = document["plotarea"]
ctx = canvas.getContext("2d")

def create_line(x1, y1, x2, y2, width=3, fill="red"):
    ctx.beginPath()
    ctx.lineWidth = width
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.strokeStyle = fill
    ctx.stroke()

# 導入數學函式後, 圓周率為 pi
# deg 為角度轉為徑度的轉換因子
deg = pi/180.
#
# 以下分別為正齒輪繪圖與主 tkinter 畫布繪圖
#
# 定義一個繪正齒輪的繪圖函式
# midx 為齒輪圓心 x 座標
# midy 為齒輪圓心 y 座標
# rp 為節圓半徑, n 為齒數
def gear(midx1, midy, j, n, 顏色):
    # 將角度轉換因子設為全域變數
    global deg
    # 齒輪漸開線分成 15 線段繪製
    imax = 15
    # 在輸入的畫布上繪製直線, 由圓心到節圓 y 軸頂點畫一直線
    rp=j*n/2
    if (midx1>0):
        midx=midx1
    else:
        midx=400+(rp+6)*2
    create_line(midx, midy, midx, midy-rp)
    # 畫出 rp 圓, 畫圓函式尚未定義
    #create_oval(midx-rp, midy-rp, midx+rp, midy+rp, width=2)
    # a 為模數 (代表公制中齒的大小), 模數為節圓直徑(稱為節徑)除以齒數
    # 模數也就是齒冠大小
    a=2*rp/n
    # d 為齒根大小, 為模數的 1.157 或 1.25倍, 這裡採 1.25 倍
    d=2.5*rp/n
    # ra 為齒輪的外圍半徑
    ra=rp+a
    print("ra:", ra)
    # 畫出 ra 圓, 畫圓函式尚未定義
    #create_oval(midx-ra, midy-ra, midx+ra, midy+ra, width=1)
    # rb 則為齒輪的基圓半徑
    # 基圓為漸開線長齒之基準圓
    rb=rp*cos(20*deg)
    print("rp:", rp)
    print("rb:", rb)
    # 畫出 rb 圓 (基圓), 畫圓函式尚未定義
    #create_oval(midx-rb, midy-rb, midx+rb, midy+rb, width=1)
    # rd 為齒根圓半徑
    rd=rp-d
    # 當 rd 大於 rb 時
    print("rd:", rd)
    # 畫出 rd 圓 (齒根圓), 畫圓函式尚未定義
    #create_oval(midx-rd, midy-rd, midx+rd, midy+rd, width=1)
    # dr 則為基圓到齒頂圓半徑分成 imax 段後的每段半徑增量大小
    # 將圓弧分成 imax 段來繪製漸開線
    dr=(ra-rb)/imax
    # tan(20*deg)-20*deg 為漸開線函數
    sigma=pi/(2*n)+tan('''+(inp2)+'''*deg)-'''+(inp2)+'''*deg
    for j in range(n):
        ang=-2.*j*pi/n+sigma
        ang2=2.*j*pi/n+sigma
        lxd=midx+rd*sin(ang2-2.*pi/n)
        lyd=midy-rd*cos(ang2-2.*pi/n)
        #for(i=0;i<=imax;i++):
        for i in range(imax+1):
            r=rb+i*dr
            theta=sqrt((r*r)/(rb*rb)-1.)
            alpha=theta-atan(theta)
            xpt=r*sin(alpha-ang)
            ypt=r*cos(alpha-ang)
            xd=rd*sin(-ang)
            yd=rd*cos(-ang)
            # i=0 時, 繪線起點由齒根圓上的點, 作為起點
            if(i==0):
                last_x = midx+xd
                last_y = midy-yd
            # 由左側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
            create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=顏色)
            # 最後一點, 則為齒頂圓
            if(i==imax):
                lfx=midx+xpt
                lfy=midy-ypt
            last_x = midx+xpt
            last_y = midy-ypt
        # the line from last end of dedendum point to the recent
        # end of dedendum point
        # lxd 為齒根圓上的左側 x 座標, lyd 則為 y 座標
        # 下列為齒根圓上用來近似圓弧的直線
        create_line((lxd),(lyd),(midx+xd),(midy-yd),fill=顏色)
        #for(i=0;i<=imax;i++):
        for i in range(imax+1):
            r=rb+i*dr
            theta=sqrt((r*r)/(rb*rb)-1.)
            alpha=theta-atan(theta)
            xpt=r*sin(ang2-alpha)
            ypt=r*cos(ang2-alpha)
            xd=rd*sin(ang2)
            yd=rd*cos(ang2)
            # i=0 時, 繪線起點由齒根圓上的點, 作為起點
            if(i==0):
                last_x = midx+xd
                last_y = midy-yd
            # 由右側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
            create_line((midx+xpt),(midy-ypt),(last_x),(last_y),fill=顏色)
            # 最後一點, 則為齒頂圓
            if(i==imax):
                rfx=midx+xpt
                rfy=midy-ypt
            last_x = midx+xpt
            last_y = midy-ypt
        # lfx 為齒頂圓上的左側 x 座標, lfy 則為 y 座標
        # 下列為齒頂圓上用來近似圓弧的直線
        create_line(lfx,lfy,rfx,rfy,fill=顏色)

gear(400,400,'''+str(K)+''','''+str(N)+''',"blue")
</script>
<canvas id="plotarea" width="1000" height="1000"></canvas>
</body>
</html>
    '''

        return outString
    drawspuraction.exposed = True
    def guessform(self):
        # 印出讓使用者輸入的超文件表單
        outstring = str(cherrypy.session.get('answer')) + "/" + str(cherrypy.session.get('count')) + '''<form method=POST action=doCheck>
    請輸入您所猜的整數:<input type=text name=guess><br />
    <input type=submit value=send>
    </form>'''
        return outstring0

    #@+node:2015.20150420212038.1941: *3* mygeartest2
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def mygeartest2(self, K=None, N=None,ng1=None, ng2=None, ng3=None, ng4=None, ng5=None, ng6=None, inp2=None):
        outString = ""
        outString +="藍色，40223124丞宗繪製，齒數1:"+N
        outString += "<br />"
        outString +="黑色，40223145兆銓繪製，齒數2:"+ng1
        outString += "<br />"
        outString +="紅色，40223110常皓繪製，齒數3:"+ng2
        outString += "<br />"
        outString +="咖啡色，40223129家偉繪製，齒數4:"+ng3
        outString += "<br />"
        outString +="綠色，40223149涵餘繪製，齒數5:"+ng4
        outString += "<br />"
        outString +="黃色，40223150俊宇繪製，齒數6:"+ng5
        outString += "<br />"
        outString +="粉紅色，40223151正斌繪製，齒數7:"+ng6
        outString += "<br />"
        outString +="模數:"+K
        outString += "<br />"
        outString +="壓力角:"+inp2
        outString += "<br />"
        outString += self.menuLink()
        outString += '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">

    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    from math import *
    # 請注意, 這裡導入位於 Lib/site-packages 目錄下的 spur.py 檔案
    import spur

    # 準備在 id="plotarea" 的 canvas 中繪圖
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")
    # 以下利用 spur.py 程式進行繪圖, 接下來的協同設計運算必須要配合使用者的需求進行設計運算與繪圖
    # 其中並將工作分配給其他組員建立類似 spur.py 的相關零件繪圖模組
    # midx, midy 為齒輪圓心座標, rp 為節圓半徑, n 為齒數, pa 為壓力角, color 為線的顏色
    # Gear(midx, midy, rp, n=20, pa=20, color="black"):
    # 模數決定齒的尺寸大小, 囓合齒輪組必須有相同的模數與壓力角
    # 壓力角 pa 單位為角度
    pa = '''+str(inp2)+'''
    # m 為模數
    m = '''+str(K)+'''
    # 第1齒輪齒數
    n_g1 = '''+str(N)+'''
    # 第2齒輪齒數
    n_g2 = '''+str(ng1)+'''
    n_g3 = '''+str(ng2)+'''
    n_g4 = '''+str(ng3)+'''
    n_g5 = '''+str(ng4)+'''
    n_g6 = '''+str(ng5)+'''
    n_g7 = '''+str(ng6)+'''
    # 計算兩齒輪的節圓半徑
    rp_g1 = m*n_g1/2
    rp_g2 = m*n_g2/2
    rp_g3 = m*n_g3/2
    rp_g4 = m*n_g4/2
    rp_g5 = m*n_g5/2
    rp_g6 = m*n_g6/2
    rp_g7 = m*n_g7/2
 #齒輪嚙合的旋轉角
# 將第1齒輪順時鐘轉 90 度
    th1 = pi/2

    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    th2 = -pi/2-pi/n_g2

    # 將第3齒輪逆時鐘轉 90 度之後, 再往回轉第2齒輪定位帶動轉角, 然後再逆時鐘多轉一齒, 以便與第2齒輪進行囓合
    # 第1個 -pi/2 為將原先垂直的第3齒輪定位線逆時鐘旋轉 90 度
    # -pi/n_g3 則是第3齒與第2齒定位線重合後, 必須再逆時鐘多轉一齒的轉角, 以便進行囓合
    # (pi+pi/n_g2)*n_g2/n_g3 則是第2齒原定位線為順時鐘轉動 90 度, 
    # pi+pi/n_g2 為第2齒輪從順時鐘轉 90 度之後, 必須配合目前的標記線所作的齒輪 2 轉動角度, 要轉換到齒輪3 的轉動角度
    # 必須乘上兩齒輪齒數的比例, 若齒輪2 大, 則齒輪3 會轉動較快
    # 但是第2齒輪為了與第1齒輪囓合, 已經距離定位線, 多轉了 180 度, 再加上第2齒輪的一齒角度, 因為要帶動第3齒輪定位, 
    # 這個修正角度必須要再配合第2齒與第3齒的轉速比加以轉換成第3齒輪的轉角, 因此乘上 n_g2/n_g3
    th3 = -pi/2-pi/n_g3+(pi+pi/n_g2)*n_g2/n_g3

    th4 = -pi/2-pi/n_g4+(pi+pi/n_g3)*n_g3/n_g4-(pi+pi/n_g2)*n_g2/n_g4
    th5 = -pi/2-pi/n_g5+(pi+pi/n_g4)*n_g4/n_g5-(pi+pi/n_g3)*n_g3/n_g5+(pi+pi/n_g2)*n_g2/n_g5
    th6 = -pi/2-pi/n_g6+(pi+pi/n_g5)*n_g5/n_g6-(pi+pi/n_g4)*n_g4/n_g6+(pi+pi/n_g3)*n_g3/n_g6-(pi+pi/n_g2)*n_g2/n_g6
    th7 = -pi/2-pi/n_g7+(pi+pi/n_g6)*n_g6/n_g7-(pi+pi/n_g5)*n_g5/n_g7+(pi+pi/n_g4)*n_g4/n_g7-(pi+pi/n_g3)*n_g3/n_g7+(pi+pi/n_g2)*n_g2/n_g7


    # 將第1齒輪順時鐘轉 90 度
    # 使用 ctx.save() 與 ctx.restore() 以確保各齒輪以相對座標進行旋轉繪圖
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400,400)
    # rotate to engage
    ctx.rotate( th1)
    # put it back
    ctx.translate(-400,-400)
    spur.Spur(ctx).Gear(400,400,rp_g1,n_g1, pa, "blue")
    ctx.restore()
    ctx.font = "10px Verdana";
    ctx.fillText("組員:24號袁丞宗所繪製",400-60, 400-10);

    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+rp_g2,400)
    # rotate to engage
    ctx.rotate( th2)
    # put it back
    ctx.translate(-(400+rp_g1+rp_g2),-400)
    spur.Spur(ctx).Gear(400+rp_g1+rp_g2,400,rp_g2,n_g2, pa, "black")
    ctx.restore()

    # 將第3齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+2*rp_g2+rp_g3,400)
    # rotate to engage
    ctx.rotate( th3)
    # put it back
    ctx.translate(-(400+rp_g1+2*rp_g2+rp_g3),-400)
    spur.Spur(ctx).Gear(400+rp_g1+2*rp_g2+rp_g3,400,rp_g3,n_g3, pa, "red")
    ctx.restore()

    # 將第4齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+2*rp_g2+2*rp_g3+rp_g4,400)
    # rotate to engage
    ctx.rotate( th4)
    # put it back
    ctx.translate(-(400+rp_g1+2*rp_g2+2*rp_g3+rp_g4),-400)
    spur.Spur(ctx).Gear(400+rp_g1+2*rp_g2+2*rp_g3+rp_g4,400,rp_g4,n_g4, pa, "black")
    ctx.restore()

    # 將第5齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+rp_g5,400)
    # rotate to engage
    ctx.rotate( th5)
    # put it back
    ctx.translate(-(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+rp_g5),-400)
    spur.Spur(ctx).Gear(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+rp_g5,400,rp_g5,n_g5 ,pa, "green")
    ctx.restore()

    # 將第6齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+rp_g6,400)
    # rotate to engage
    ctx.rotate( th6)
    # put it back
    ctx.translate(-(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+rp_g6),-400)
    spur.Spur(ctx).Gear(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+rp_g6,400,rp_g6,n_g6 ,pa, "yellow")
    ctx.restore()

    # 將第7齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+2*rp_g6+rp_g7,400)
    # rotate to engage
    ctx.rotate( th7)
    # put it back
    ctx.translate(-(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+2*rp_g6+rp_g7),-400)
    spur.Spur(ctx).Gear(400+rp_g1+2*rp_g2+2*rp_g3+2*rp_g4+2*rp_g5+2*rp_g6+rp_g7,400,rp_g7,n_g7 ,pa, "pink")
    ctx.restore()
    # 假如第3齒也要進行囓合, 又該如何進行繪圖?
    #spur.Spur(ctx).Gear(400,400,100,12, pa, "red")

    </script>
    <canvas id="plotarea" width="3600" height="3600"></canvas>
    </body>
    </html>
    '''

        return outString
    mygeartest2.exposed = True

    #@-others
    def default(self):
        sys.exit()
    default.exposed = True
    def menuLink(self):
        return '''
        <br />
        <a href=\"index\">協同組員</a>|
        <a href=\"index1\">首頁</a>|
        <a href="gear">3D齒輪模式</a>|
        <a href=\"spur\">七顆齒輪</a>|
        <a href="drawspur">2015cda 期中上機考 一顆齒輪繪圖</a>|
        <a href="drawspur1"> 2015cda 期中上機考表單文字輸出</a>|
        <a href="index3"> 個人影片</a>|
        <a href="test1"> 垂直齒輪7齒</a>|
        <a href="test2"> 垂直齒輪</a>|</br>

    
        '''
    @cherrypy.expose
    #副程式
    def  menuLink2(self):
        return self.menuLink1.index()
    def index1(self):
        outstring ='''<font size='6' color='darkslateblue' face='標楷體' >首頁</font>'''
        outstring += self.menuLink2()
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += '''
                        <body bgcolor='azure' link='darkorenge' vlink='darkorenge '>
                        <font size='6' color='black' face='標楷體' >協同的背景</font></br>
                        <font size='4' color='black' face='標楷體' >
                        全球化帶來的密集與瞬息萬變的競爭, 即便是全球各領域目前領先的國際大公司都必須</br>
                        要靠快速併購, 才能具備克敵致勝的專業能力, 因此對於規模較小, 專業能力較不全面的</br>
                        公司與團隊, 為求生存, 必得積極尋求各方協同的機會.</br>
                        </br>
                        以機械設計流程的角度言, 協同產品設計過程中主要的項目在資訊與知識層次上的協同.</br>

                        協同的目的在追求速度, 效能, 多元, 互動與彈性</br>

                        速度 - 推出新產品的速度, 修正既有錯誤的速度</br>

                        效能 - 強調效率與功能, 持續降低成本</br>

                        多元 - 多方嘗試, 多方檢視, 多方調控, 多方出擊</br>

                        互動 - 有推有拉, 有來有往, 密切藕合</br>

                        彈性 - 及時調整適應, 配合需求能夠加以變化</br></br>

                        協同(Collaboration)與合作(Cooperation)有何差異?</br></br>

                        協同源自各方公認的共同目標, 而合作則通常指源自個別認知下的不同標的.</br></br>

                        協同互動性高於合作</br>
                        協同的積極與動態性, 高於合作</br>
                        協同成員間的專業重疊性, 高於合作</br>
                        協同的價值通常高於合作</br>
                        就時代發展的潮流而言, 以 Collaboration 模式進行協同合作的公司, 所有成員不僅秉持</br>
                        相同目標, 積極主動, 彼此可互相替代職務, 在永續經營理念下, 不斷創造價值的公司, 將</br>
                        具有相對於採 Cooperation 模式公司較高的國際競爭力.</br></br>

                        Collaboration 公司 (若公司文化無法支撐以下條件, 則必須透過系統機制達成):</br></br>

                        所有成員在所規劃安排的時間, 盡心盡力完成自我期許的任務, 沒有摸魚與怠忽職守的問題.</br>
                        所有成員在解決各種問題的流程中, 能不斷自我學習並惕勵自己, 讓公司價值不斷向上攀升.</br>
                        所有成員都是老闆, 公司的價值得以即時公平落實到所有成員身上.</br>
                        所有成員在任何時間地點都能上班, 也都能到世界各地去上班, 沒有打卡約束與適應的問題.</br>
                        公司成員間, 有許多職務都可隨時替代安排, 因此沒有“非我不可”, 加班與爆肝的問題.</br></br>
                        協同範例</br></br>

                        <a href=\"http://en.flossmanuals.net/_booki/openstreetmap/openstreetmap.pdf\">http://en.flossmanuals.net/_booki/openstreetmap/openstreetmap.pdf</a></br>
                       <a href="http://www.openstreetmap.org/"> http://www.openstreetmap.org/</a></br></br>
                        協同原理</br></br>

                        <a href="http://en.wikipedia.org/wiki/General_theory_of_collaboration"> http://en.wikipedia.org/wiki/General_theory_of_collaboration</a></br>
                        <a href="http://www.designingcollaboration.com/"> http://www.designingcollaboration.com/</a></br></br>
                        控制工廠間的協同</br></br>
                        協同的基本元素:</br>

                        協同的動機 - 為何要協同? 環境使然, 趨勢使然, 或者只是為協同而協同.</br>
                        協同的分享 - 協同過程中, 如何分享?(功勞記在誰頭上?) 分享甚麼?(要全盤托出嗎?) 何時分享? 跟誰分享?</br>
                        協同的溝通 - 該與誰溝通? 如何溝通? 溝通甚麼? 何時進行溝通?(隨選或即時或定時溝通)</br>
                        協同的廣度 - 協同的範圍取捨, 哪些領域與專長的人該進來協同?</br>
                        協同的效度 - 協同解決了甚麼問題? 解決誰的問題? 解決何時的問題? 問題真的解決了嗎?</br>
                        協同的支援 - 因協同而得的特殊支援項目, 當天就要塌下來了, 誰該負責?</br>
                    </font>
                     </body>
    '''
        outstring += self.menuLink()
        return outstring 
    index1.exposed = True
    def  index2(self):
        return '''
        <br />
        <table border=3>
　     <tr>
        <th align='left'><font " size='4' color='black' face='標楷體' > 40223151功課表單  </font></br></th>
        </tr>
　     <tr>
        <th align='left'><a href="gear" target="_blank">3D齒輪模式</a></br></th>
　     </tr>
　     <tr>
        <th align='left'><a href=\"index_all/spur_1\" target="_blank">七顆齒輪</a></br></th>
　     </tr>
　     <tr>
        <th align='left'><a href="index_all/drawspur_1" target="_blank">2015cda 期中上機考 一顆齒輪繪圖</a></br></th>
　     </tr>
　     <tr>
        <th align='left'><a href="index_all/drawspur1_1" target="_blank"> 2015cda 期中上機考表單文字輸出</a></br></th>
　     </tr>
　     <tr>
        <th align='left'><a href="man" target="_blank"> 樂高機器人組立</a></th>
　     </tr>
　     <tr>
        <th align='left'><a href="index1"> 個人首頁</a><font color='red' face='標楷體' >(內有心得跟影片)</font></th>
　     </tr>
　     <tr>
        <th align='left'><font color='black' face='標楷體' >第一次小考程式w16</font></br>
        <a href="a_40223151"> a_40223151</a></br>
        <a href="man" target="_blank"> 樂高機器人組立</a></br>
        <a href="video1"> 第一次小考影片</a></br>
        </th>
　     </tr>
　     <tr>
        <th align='left'><font color='black' face='標楷體' >第二次小考程式w17</font></br>
        <a href="test2">垂直齒輪</a></br>
        <a href="test1">垂直齒輪7齒</a></br>
        </th>
　     </tr>

        '''
    index2.exposed = True
    def me(self):
        outstring ='''<font size='6' color='darkslateblue' face='標楷體' >首頁</font>'''
        outstring += self.menuLink2()
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += "</br>"
        outstring += '''
            <body background="http://www.gameapps.hk/images/201412/01/sao.jpg" bgproperties=fixed link='darkorenge' vlink='darkorenge '>
            </body>
                    '''   
        return outstring  
    me.exposed = True
              
    def man(self, *args, **kwargs):
        outstring = '''
這是 2014CDA 協同專案下的 cdag30 模組下的 MAN 類別.<br /><br />
<!-- 這裡採用相對連結, 而非網址的絕對連結 (這一段為 html 註解) -->
<font size='5' color='#FF8800' face='標楷體' >樂高機器人程式一次組起來</font><br />
<a href="man3/assembly">執行  MAN 類別中的 assembly 方法</a><br /><br />
請確定下列零件於 V:/home/lego/man 目錄中, 且開啟空白 Creo 組立檔案.<br />
<a href="/static/lego_man.7z">lego_man.7z</a>(滑鼠右鍵存成 .7z 檔案)<br />
'''
        outstring +=self.man2.man4()
        outstring +=self.man2.man5()
        return outstring
    man.exposed = True
    def man_index(self, *args, **kwargs):
        outstring = '''
'''
        outstring +=self.man2.man5()
        return outstring
    man_index.exposed = True



#@-others
################# (4) 程式啟動區
# 配合程式檔案所在目錄設定靜態目錄或靜態檔案
application_conf = {'/static':{
        'tools.staticdir.on': True,
        # 程式執行目錄下, 必須自行建立 static 目錄
        'tools.staticdir.dir': _curdir+"/static"},
        '/downloads':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/downloads"},
        '/images':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/images"}
    }
root = Hello()
root.gear = gear.Gear()
root.man2 = man2.MAN()
root.man3 = man3.MAN()
root.menuLink1 = menuLink1.MenuLink1()
root. index_all =  index_all. Index_all()
cherrypy.server.socket_port = 8081
cherrypy.server.socket_host = '127.0.0.1'
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示在 OpenSfhit 執行
    application = cherrypy.Application(root, config=application_conf)
else:
    # 表示在近端執行
    cherrypy.quickstart(root, config=application_conf)
#@-leo
