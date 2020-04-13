#!/usr/bin/python
#- * -coding: utf - 8 - * -
import sys
import os
import requests as req
import requests
import calendar
import json
import time, datetime
#from threading
#import Timer
#def bilibili():
UserUid = 397875469# 获取B站粉丝数
data = requests.get('https://api.bilibili.com/x/web-interface/card?mid=%d' % (UserUid))
information = json.loads(data.text)
fsss = information['data']['follower']
fss = str(fsss)
print(fss)
from time import strftime, localtime
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath( __file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath( __file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
# 获取日期、 时间、 星期
    rq = strftime("%Y", localtime()) + "    " + strftime("%m", localtime()) +"    " + strftime("%d", localtime()) + "          "
    sj = strftime("%H", localtime()) + ":" + strftime("%M", localtime()) +":" + strftime("%S", localtime())
    print(sj)
    dayOfWeek = datetime.datetime.now().isoweekday()
    xq = str(dayOfWeek)
    print(xq)
import logging
from waveshare_epd import epd7in5bc_V3
import time
from PIL  import Image, ImageDraw, ImageFont
import traceback
logging.basicConfig(level = logging.DEBUG)
try:
    logging.info("epd7in5bc_V3 Demo")
    epd = epd7in5bc_V3.EPD()
    logging.info("清屏..........")
    epd.init()
    epd.Clear()

    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font68 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 68)
    font72 = ImageFont.truetype(os.path.join(picdir, 'msyh.ttc'), 72)
    font42 = ImageFont.truetype(os.path.join(picdir, 'msyh.ttc'), 42)
    font60 = ImageFont.truetype(os.path.join(picdir, 'yj.ttf'), 60)
    font34 = ImageFont.truetype(os.path.join(picdir, 'yj.ttf'), 34)
    font73 = ImageFont.truetype(os.path.join(picdir, 'jt.ttf'), 72)
    font74 = ImageFont.truetype(os.path.join(picdir, 'ph.ttf'), 96)
    font36 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 36)
    font31 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 30)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.width, epd.height), 255)# 255: clear the frame
    Other = Image.new('1', (epd.width, epd.height), 255)# 255: clear the frame
    draw_Himage = ImageDraw.Draw(Himage)
    draw_other = ImageDraw.Draw(Other)
    draw_Himage.text((175, 80), u'风行造价工作室', font = font68, fill = 0)
    draw_Himage.text((170, 185), u'祝贺您获得                粉丝', font = font42, fill = 0)
    draw_other.text((420, 185), fss, font = font60, fill = 0)
    draw_Himage.text((20, 440), u'          年     月    日 星期', font = font31, fill = 0)
    draw_Himage.text((24, 440), rq, font = font34, fill = 0)
    draw_Himage.text((660, 440), sj, font = font34, fill = 0)
    if xq == '7':

        draw_Himage.text((332, 440), u'日', font = font31, fill = 0)

    elfi xq == '6':

        draw_Himage.text((332, 440), u'六', font = font31, fill = 0)
    elfi xq == '5':

        draw_Himage.text((332, 440), u'五', font = font31, fill = 0)

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