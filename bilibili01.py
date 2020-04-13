#!/usr/bin/python
#- * -coding: utf - 8 - * -
import sys
import os
import requests as req
import requests
import json
import time, datetime
sys.path.append('/home/pi/.local/lib/python2.7/site-packages')
import  sxtwl
from time import strftime, localtime

# 获取B站粉丝数
UserUid = 397875469 #设置B站账号uid
url = 'http://api.bilibili.com/x/relation/stat?vmid=%d' 
data = requests.get(url % (UserUid), verify=False)
information = json.loads(data.text)
fsss = information['data']['follower']
fss = str(fsss)
print(fss)



# 获取日期、 时间、 星期、农历
rq = strftime("%Y", localtime()) + "    " + strftime("%m", localtime()) +"    " + strftime("%d", localtime()) + "          "
#时间
sj = strftime("%H", localtime()) + ":" + strftime("%M", localtime()) 
#星期
dayOfWeek = datetime.datetime.now().isoweekday()
def get_week_day(date):
	week_day_dict = {
	0 : '星期一',
	1 : '星期二',
	2 : '星期三',
	3 : '星期四',
	4 : '星期五',
	5 : '星期六',
	6 : '星期天',
	}
  	day = date.weekday()
  	return week_day_dict[day]
xquu = get_week_day(datetime.datetime.now())
xq = xquu.decode('utf-8')   #把星期输出的文本转换为Unicode，方便变量输出显示，余同


#农历-农历需要在命令行安装库 命令为：pip install sxtwl 
sys.path.append('/home/pi/.local/lib/python2.7/site-packages')
import  sxtwl
lunar = sxtwl.Lunar()
ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
 "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九",
  "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]
yy = datetime.datetime.now().year
mm = datetime.datetime.now().month
dd = datetime.datetime.now().day
yll = lunar.getDayBySolar(yy, mm, dd)
if yll.Lleap:
    yl = "农历润"+ymc[yll.Lmc] + "月" + rmc[yll.Ldi]
else:
    yl = "农历"+ymc[yll.Lmc]+ "月" + rmc[yll.Ldi]
print yl
yll = yl.decode('utf-8')

#墨水屏显示部分
from time import strftime, localtime
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath( __file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath( __file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
import logging
from waveshare_epd import epd7in5bc_V2
from PIL  import Image, ImageDraw, ImageFont
import traceback
logging.basicConfig(level = logging.DEBUG)
try:
	logging.info("epd7in5bc_V2 Demo")
	epd = epd7in5bc_V2.EPD()
	logging.info("清屏..........") 
	epd.init()
	epd.Clear()
	font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24) #字体文件放置在pic目录，用到
	font68 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 68)
	#font72 = ImageFont.truetype(os.path.join(picdir, 'msyh.ttc'), 72)
	font42 = ImageFont.truetype(os.path.join(picdir, 'msyh.ttc'), 42)
	font60 = ImageFont.truetype(os.path.join(picdir, 'digtal.ttf'), 60)
	font38 = ImageFont.truetype(os.path.join(picdir, 'digtal.ttf'), 38)
	font36 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 36)
	font31 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 30)
	font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

#Drawing on the Horizontal image
	logging.info("1.Drawing on the Horizontal image...")
	Himage = Image.new('1', (epd.width, epd.height), 255)# 255: clear the frame
	Other = Image.new('1', (epd.width, epd.height), 255)# 255: clear the frame
	draw_Himage = ImageDraw.Draw(Himage)
	draw_other = ImageDraw.Draw(Other)
	draw_Himage.text((175, 80), u'风行造价工作室', font = font68, fill = 0)
	draw_Himage.text((170, 185), u'祝贺您获得                粉丝', font = font42, fill = 0)
	draw_other.text((420, 185), fss, font = font60, fill = 0)
	draw_Himage.text((20, 440), u'          年     月    日 ', font = font31, fill = 0)
	draw_Himage.text((20, 440), rq, font = font38, fill = 0)
	draw_Himage.text((280, 440), xq , font = font31, fill = 0)
	draw_Himage.text((390, 440), yll , font = font31, fill = 0)
	draw_Himage.text((660, 440), sj, font = font38, fill = 0)
	bmp = Image.open(os.path.join(picdir, 'bili.bmp'))
	Himage.paste(bmp, (180, 300))
	epd.display(epd.getbuffer(Himage), epd.getbuffer(Other))
	time.sleep(2)
	logging.info("Goto Sleep...")
	epd.sleep()
except IOError as e:
	logging.info(e)
except KeyboardInterrupt:
	logging.info("ctrl + c:")
	epd7in5.epdconfig.module_exit()
	exit()
