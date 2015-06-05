import cherrypy
# 導入 Python 內建的 os 模組, 因為 os 模組為 Python 內建, 所以無需透過 setup.py 安裝
import man2
class MenuLink1(object):
    # 各組利用 index 引導隨後的程式執行
    @cherrypy.expose
    def  index(self):
        return '''
        <html>
            <head>
                <meta charset="UTF-8" />
                <title>40223151_2015cda報告</title>
                <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
                <script type="text/javascript">
                    $(function(){
                        $("ul.navigation > li:has(ul) > a").append('<div class="arrow-bottom"></div>');
                        $("ul.navigation > li ul li:has(ul) > a").append('<div class="arrow-right"></div>');
                    });
                </script>
                <style type="text/css">

                    /*
                        作者：Yuxin
                        教學文：http://fundesigner.net/only-css-menu
                        授權：MIT License
                    */

                    /* 初始化 */
                    body, ul, li, a{
                        margin: 0;
                        padding: 0;
                        font-size: 13px;
                        text-decoration: none;
                    }
                    ul, li {
                        list-style: none;
                    }
                    /* 選單 li 之樣式 */
                    ul.navigation li {
                        position: relative;
                        float: left;
                    }
                    /* 選單 li 裡面連結之樣式 */
                    ul.navigation li a{
                        display: block;
                        padding: 12px 20px;
                        background: #220088;
                        color: #FFF;
                    }
                    /* 特定在第一層，以左邊灰線分隔 */
                    ul.navigation > li > a{
                        border-bottom: 1px solid #CCC;				
                        border-left: 1px solid #CCC;
                    }
                    ul.navigation > li > a:hover{
                        color: #666;
                        background: #DDD
                    }
                    /* 特定在第一層 > 第二層或以後下拉部分之樣式 */
                    ul.navigation ul{
                        display: none;
                        float: left;
                        position: absolute;			
                        left: 0;	
                        margin: 0;
                    }
                    /* 當第一層選單被觸發時，指定第二層顯示 */
                    ul.navigation li:hover > ul{
                        display: block;
                    }			
                    /* 特定在第二層或以後下拉部分 li 之樣式 */
                    ul.navigation ul li {
                        border-bottom: 1px solid #DDD;
                    }
                    /* 特定在第二層或以後下拉部分 li （最後一項不要底線）之樣式 */
                    ul.navigation ul li:last-child {
                        border-bottom: none;
                    }
                    /* 第二層或以後選單 li 之樣式 */
                    ul.navigation ul a {
                        width: 120px;
                        padding: 10px 12px;	
                        color: #FFF;		
                        background: #0066FF;			
                    }
                    ul.navigation ul a:hover {		
                        background: #CCC;				
                    }
                    /* 第三層之後，上一層的選單觸發則顯示出來（皆為橫向拓展） */
                    ul.navigation ul li:hover > ul{
                        display: block;
                        position: absolute;
                        top: 0;				
                        left: 100%;
                    }
                    /* 箭頭向下 */
                    .arrow-bottom {
                        display: inline-block;
                        margin-left: 5px;
                        border-top: 4px solid #FFF;
                        border-right: 4px solid transparent;				
                        border-left: 4px solid transparent;		
                        width: 1px;
                        height: 1px;
                    }

                    /* 箭頭向右 */
                    .arrow-right {
                        display: inline-block;
                        margin-left: 12px;	
                        border-top: 3px solid transparent;
                        border-bottom: 3px solid transparent;
                        border-left: 3px solid #666;		
                        width: 1px;
                        height: 1px;
                    }
                </style>		
            </head>
            <body>
                <ul class="navigation">
                    <li><a href=\"index1\">首頁</a><br /></li>
                    <li>
                        <a href="#">2015cda-w11</a>
                        <ul>
                            <li><a href="spur">七顆齒輪</a></li>
                            <li>
                                <a href="Reviews">心得</a>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <a href="#">2015cda-w12</a>
                        <ul>
                            <li><a href="man2">樂高人偶</a></li>
                            <li><a href="#">心得</a></li>
                        </ul>
                    </li>
                    <li><a href="#">2015cda-w13</a><br /></li>
                    <li><a href="#">2015cda-w14</a><br /></li>
                    <li><a href="index3"> 個人影片</a><br /></li>
                    <li>
                        <a href="#">2015cda 期中上機考</a>
                        <ul>
                            <li><a href="drawspur">2015cda 期中上機考 一顆齒輪繪圖</a></li>
                            <li><a href="drawspur1"> 2015cda 期中上機考表單文字輸出</a></li>
                        </ul>
                    </li>
                    <li><a href="gear">3D齒輪模式</a></li>
                </ul>
            </body>
        </html>
        '''