#!/usr/bin/env python3

# there is tuning of the size------

# import the necessary packages

#  ls zen_192.168.0.91_20211105_* | while read line; do echo file \'$line\'; done | ffmpeg -protocol_whitelist file,pipe -f concat -i - -c copy zen_192.168.0.91_20211105_.avi

from imutils.video import VideoStream
import socket
import time
import signal
from contextlib import contextmanager
import argparse

import cv2
import datetime
import time

# import datetime as dt

import os


from fire import Fire
import imutils

import urllib.request
import numpy as np

# user pass
import  base64

import getpass

import sys

from flashcam.stream_enhancer import Stream_Enhancer
import webbrowser

import math

import requests # crosson=CROSSON


global centerX1, centerY1
global FILE_USERPASS
global FILE_REDCROSS
# ---------- files:
FILE_USERPASS = "~/.config/flashcam/.flashcam_upw" # will extend
FILE_REDCROSS = "~/.config/flashcam/crossred" # will extend


global local_gamma, integrate
local_gamma = 1 #  adjust_gamma
integrate = 1 # call accum


# i needed a warning before 't'
global allow_tracker, allow_tracker_demand
allow_tracker = False
allow_tracker_demand = False

global show_help
show_help = False


# x ... expand 2x ... buggy
HELPTEXT=""" a/A ... SAVE AVI/ stop (to ~/DATA/)
 s ... save JPG (to ~/DATA/)

 z ... cycle zoom 2x (mouse click fixes the center)
 Z ... zoom 1x
 r ... rotate by 180 degrees

 c/C ... red cross on/off (save when off)
 hjkl ... move the red/green* cross (HJKL)
 t/u ... tracker 1 (cross sync, speed)
 T/u ... tracker 2 (more steady, but fragile)

 m/M ... measure/not distance,  (-v 110,1.2)
 n/N ... inc/decrease distance
 f/F ... inc/dec Field Of View (-v FOV,dist)

 v/V* ... green cross ON/OFF
 b/f* ... substract BG, mix FG
 B/F* ... SAVE BG/ SAVE FG

 eg* ...  expo/gain (+ shift or ctrl)
 y  ...  gamma (local) (+shift or ctrl)
 i/I* ... adjust

 w ... open web browser
 q ... quit
       * with remote flashcam server """



def remap_keys(key):
    table = {1048673:'a',
             1048674:'b',
             1048675:'c',
             1048676:'d',
             1048677:'e',
             1048678:'f',
             1048679:'g',
             1048680:'h',
             1048681:'i',
             1048682:'j',
             1048683:'k',
             1048684:'l',
             1048685:'m',
             1048686:'n',
             1048687:'o',
             1048688:'p',
             1048689:'q',
             1048690:'r',
             1048691:'s',
             1048692:'t',
             1048693:'u',
             1048694:'v',
             1048695:'w',
             1048696:'x',
             1048697:'y',
             1048698:'z',
             1114177:'A',
             1114178:'B',
             1114179:'C',
             1114180:'D',
             1114181:'E',
             1114182:'F',
             1114183:'G',
             1114184:'H',
             1114185:'I',
             1114186:'J',
             1114187:'K',
             1114188:'L',
             1114189:'M',
             1114190:'N',
             1114191:'O',
             1114192:'P',
             1114193:'Q',
             1114194:'R',
             1114195:'S',
             1114196:'T',
             1114197:'U',
             1114198:'V',
             1114199:'W',
             1114200:'X',
             1114201:'Y',
             1114202:'Z'   }
# ctrl e     1310821:''

    if key in table:
        key = ord( table[key] )
    return key


#-------------------- DISPLAY MULTITEXT ---------------------
def disp_mutext(lena, wrapped_text_o):

    lena = np.array(lena) # I turn to np.array
    lena = lena/255

    size = lena.shape
    wrapped_text = wrapped_text_o.split("\n")

    img = np.zeros( size, dtype='uint8')
    img = img+.0 # +0.9 # whitish
    #print("npzero",img.shape, img)

    height, width, channel = img.shape

    text_img = np.ones((height, width))
    #print(text_img.shape)
    font = cv2.FONT_HERSHEY_SIMPLEX

    x, y = 10, 40
    font_size = 0.4
    font_thickness = 1

    i = 0

    textsize1 = 1
    textsize0 = 1


    for line in wrapped_text:
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]
        if textsize[0]> textsize0:
            textsize0=textsize[0]
        if textsize[1]> textsize1:
            textsize1=textsize[1]

    #    wrapped_text.append( " "*textsize1+"[OK]" )
    #print(    wrapped_text )

    for line in wrapped_text:
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]
        if textsize[0]> textsize0:
            textsize0=textsize[0]
        if textsize[1]> textsize1:
            textsize1=textsize[1]
    # ----- after finding the text sizes; define gap

    gap = textsize1 + 6

    nlines = len(wrapped_text)
    offx = 0 +  int((img.shape[1] - textsize0) / 2)
    offy = 0 + int((img.shape[0] - gap*(nlines-1)) / 2)


    pad = 10
    start_point =  ( offx -pad, offy -pad - textsize1)
    start_point2 = ( offx -pad, offy -pad - textsize1 + int(pad/2) )
    end_point = ( pad+ offx + textsize0 , offy   + gap*len(wrapped_text) )
    end_point2 = ( pad+ offx + textsize0 , offy   + gap*len(wrapped_text) - int(pad/2) )

    img = cv2.rectangle(img, start_point, end_point, (0.2,0.2,0.2), -1)

    img = cv2.rectangle(img, start_point, end_point, (-1,-1,-1), 1) # trick
    img = cv2.rectangle(img, start_point2, end_point2, (-1,-1,-1), 1) # trick

    for line in wrapped_text:
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]
        #print(textsize)
        #gap = textsize[1] + 5
        #gap = textsize1 # gap define earlier

        y = int((img.shape[0] + textsize[1]) / 2) + i * gap
        x = 10#for center alignment => int((img.shape[1] - textsize[0]) / 2)
        x = offx
        y = offy + i * gap


        cv2.putText(img, line, (x, y), font,
                    font_size,
    #                (255,255,255),
                    (-1,-1,-1), # BIG TRICK
                    font_thickness,
                    lineType = cv2.LINE_AA)
        i +=1


    img = lena - img
    #print(img)
    return img










@contextmanager
def timeout(atime):
    # register a function to raise a TimeoutError on the signal
    signal.signal(signal.SIGALRM, raise_timeout)
    # schedule the signal to be sent after 'time'
    signal.alarm(atime)
    #print("D... timeout registerred")

    try:
        tok = False
        #print("D... yielding timeout")
        yield
    finally:
        tok = True
        # unregister the signal so it wont be triggered if the timtout is not reached
        #print("D... timeout NOT!  unregisterred")
        signal.signal(signal.SIGALRM, signal.SIG_IGN)


def raise_timeout(signum, frame):
    raise TimeoutError




def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

def img_estim(img, thrshld=127):
    res = np.mean(img)
    return res
    is_light =  res > thrshld
    return 'light' if is_light else 'dark'
    # 40 -> 2.2

#------------------------------------------------------------------------ 3
# ================================================================================================

# ================================================================================================

def display2(videodev, save = False,
             passfile="~/.pycamfw_userpass",
             rotate = 0, vof = "99,2"):
    """
    """
    #sname,sfilenamea,sme,sfilenamea,sfilenamea,sfourcc,saviout

    sme = socket.gethostname()
    #frame = None
    global centerX1, centerY1, clicked
    global FILE_USERPASS, FILE_REDCROSS
    global show_help
    global allow_tracker, allow_tracker_demand
    global local_gamma, integrate
    centerX1, centerY1, clicked = 0,0, True # center zoom ion start


    filesource = False

    def MOUSE(event, x, y, flags, param):
        global centerX1,centerY1, clicked
        if event == cv2.EVENT_LBUTTONDOWN:
            clicked = not clicked
        if event == cv2.EVENT_MOUSEMOVE:
            if not(clicked):
                centerX1,centerY1 = x,y
            #print('({}, {})'.format(x, y))
            #imgCopy = frame.copy()
            #cv2.circle(imgCopy, (x, y), 5, (255, 0, 0), -1)
            #cv2.imshow('image', imgCopy)


    def setupsave():
        sname = "rec"
        sname = videodev
        sname = sname.replace("http","")
        sname = sname.replace("//","")
        sname = sname.replace(":","")
        sname = sname.replace("5000/video","")
        sname = sname.replace("8000/video","")

        sfilenamea = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        sme = socket.gethostname()
        sfilenamea = f"{sme}_{sname}_{sfilenamea}.avi"

        dir2create = os.path.expanduser("~/DATA/")
        if not os.path.isdir( os.path.expanduser(dir2create )):
            print(f"D... trying to create directory {dir2create} for saving")
            #result = False
            os.mkdir( os.path.expanduser(dir2create ))

        sfilenamea = os.path.expanduser("~/DATA/" + sfilenamea)
        sfourcc = cv2.VideoWriter_fourcc(*'XVID')
        saviout = cv2.VideoWriter( sfilenamea,sfourcc,25.0, (640,480))
        print( sfilenamea )
        print( sfilenamea )
        print( sfilenamea )
        print( sfilenamea )
        return sfilenamea,saviout

    def get_stream():
        # localuser
        global FILE_USERPASS, FILE_REDCROSS
        stream = None # i return
        u,p=getpass.getuser(),"a"

        # this is bug.... never find passfile
        if "passfile" in locals():
            if passfile is None:
                print(f"i... nO passfile...trying {videodev} , {passfile}")
                passfile = videodev.strip("http://")
                print("i... TRYING", passfile)
        else:
            passfile = videodev.strip("http://")
            passfile = passfile.strip("/video")
            passfile = passfile.split(":")[0]

            # WITH A HACK  -  I REDEFINE REDCROSS too
            FILE_REDCROSS=f"{FILE_REDCROSS}_{passfile}.txt"

            passfile = f"{FILE_USERPASS}_{passfile}"
            print(f"i... TRYING {videodev} PASS: {passfile}")

        try:
            with open( os.path.expanduser(passfile) ) as f:
                print("YES---> PASSWORD FILE  ", passfile )
                w1 = f.readlines()
                u= w1[0].strip()
                p= w1[1].strip()
        except:
            print("NO PASSWORD FILE (gs) ")


        print("D... capturing from: /{}/".format(videodev) )
        #cam = cv2.VideoCapture( videodev )
        #stream = urllib.request.urlopen( videodev )

        request = urllib.request.Request( videodev )
        print("D... USER/PASS", u,p)
        base64string =base64.b64encode( bytes(  '%s:%s' % (u, p ), 'ascii') )
        print("D... stream ok1", base64string)
        request.add_header("Authorization", "Basic %s" % base64string.decode('utf-8'))

        #request.add_header("Authorization", "Basic %s" % base64string)
        print("D... stream ok2 - request.urlopen (disp)")
        ok = False
        try:
            stream = urllib.request.urlopen(request, timeout=3) # timeout to 7 from 5 sec.
            ok = True
            filesource = True
            print("D... stream ok3")
        except urllib.error.HTTPError as e:
            print("Server Offline1? ",e)
            print(videodev)
            #do stuff here
        except urllib.error.URLError as e:
            print("Server Offline2? ",e)
            print(videodev)
            #do stuff here
        except:
            ok = False
            stream = None
            print("X.... Timeouted on URLOPEN")


        return stream, u, p


    # ********************************************************** main loop
    io_none = 0 # to reset stream
    sfilename = ""  # move up to limi # of AVI files.... tst?
    sfilenamea = ""

    stream_length = 1024*50  # i had 50k all the time from 1st working version
    stream_length = 1024*15  #



    if save:
        sfilenamea,saviout = setupsave()
    while True: #==================== MAIN LOOP =================


        mjpg =False


        # #===================== OPENCV START CAPTURE==========================

        bytex = b'' # stream
        rpi_name = videodev
        frame_num = 0

        if (str(videodev).find("http://")==0) or (str(videodev).find("https://")==0):
            # infinite loop for stream authentication
            stream = None
            while stream is None:
                print("D... waiting for stream")
                ### HERE PUT BWIMAGE
                #cv2.imshow(rpi_name, frame) # 1 window for each RPi
                if "frame" in locals():
                    print("D... frame in locals() ")
                    if (not frame is None):
                        print("D.... graying")
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                        (w, h, c) = frame.shape

                        for i in range(0,w,10):
                            x1, y1 = 0, i
                            x2, y2 = h, i
                            line_thickness = 1
                            cv2.line(gray, (x1, y1), (x2, y2), (111, 111, 111),
                                 thickness=line_thickness)
                        cv2.imshow(rpi_name, gray) # 1 window for each RPi
                        key = cv2.waitKey(1)

                time.sleep(1)
                stream, u, p  = get_stream()
        else:
            print("X... use http:// address")
            #sys.exit(0)



        if (str(videodev).find("http://")==0) or (str(videodev).find("https://")==0):
            ret_val=0
            oi = 0
            while ret_val == 0:
                oi+=1

                #with timeout(2):
                print("D... IN 1st TIO..", end="")
                try:
                    # THIS CAN TIMEOUT #########################################
                    print("D... try ...", end="")
                    bytex += stream.read(stream_length) #  must be long enough?
                except:
                    print("X... exception - timout in 1.st stream.read, ")
                    #bytex+=b"\x00\x00\x00"
                    bytex = b""


                a = bytex.find(b'\xff\xd8') #frame starting
                b = bytex.find(b'\xff\xd9') #frame ending
                if a != -1 and b != -1:
                    io_none = 0
                    jpg = bytex[a:b+2]
                    bytex = bytex[b+2:]
                    # frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
                    if len(jpg)>1000:  # was crash here
                        frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                        ret_val= 1
                        io_none = 0
                        stream_length = int( (b+2-a)/2 ) # expected length
                    else:
                        ret_val = 0
                        # print("D...                ok frame http",oi,len(bytex) )
                else:
                    ret_val = 0
                    print("D...                        frame set None http",oi,len(bytex), end="\r")
                    # it can count to milions here.... why? need to check stream ## OTHER CRASHES
                    #  i try two things now:
                    #bytex+=b""
                    time.sleep(0.2)
                    io_none+=1
                    if io_none>20:
                        stream = None
                        print("X... ---------------  too many unseen frames", io_none, "breaking")
                        io_none = 0
                        break

                    #frame = None
        if 'stream' in locals():
            if stream is None:
                continue
        else:                     # from file ---- 1st moment open
            ret_val = 0
            stream = cv2.VideoCapture( videodev )
            filesource = True
            print ("X... open  = ",stream.isOpened())
            ok,frame = stream.read()
            frame_num+=1
            # pause = True too early.... defined later
            print(f"X... {ok}, frame from {videodev}")

#----------------------------------------------------------------

        first = True

        timestamp_of_last_socket_refresh = time.time()


        i = 0
        fps = 0
        resetfps = True
        lastminu = 88
        motion_last = "999999"

        i7 = 0
        artdelay=0.05

        connection_ok = True

        # ---- bytes per second.  strange looks like 7MB/s
        BPS = 0
        BPSlast=0
        BPStag = datetime.datetime.now()
        FPS = 0
        FPSlast = 0
        frames_total = 0
        frame_num = 0

        senh = Stream_Enhancer()
        saved_jpg = False

        zoomme=1
        centerX1, centerY1 = 320,240
        expande=1
        rorate180 = False


        # measurements (distance)
        measure = 0 #1.7

        if str(vof).find(",")>0:
            vof = str(vof).strip("(")
            vof = str(vof).strip(")")
            measure_fov,measure = float(vof.split(",")[0]),float(vof.split(",")[1])
        else:
            measure_fov = float(vof)     # config.CONFIG['vof'] #


        cross = None
        greencross = False # just tell if on/off

        print(" ... ... reset of all trackers/zoom/measure etc..")

        tracker1 = None
        tracker2 = None
        tracker1_fname = None # change filename for tracking
        tracker2_fname = None # change filename for tracking
        tracker_list = []
        cropped = None # created during tracking1
        orb = None  # i dont use

        # file - pause
        pause = True # FOR FILE but not for CAM
        if filesource==False:
            pause=False
        frame_from_file = None # backup the frame:  for effects; also for CAMERA now!

        # -see the values sent from the webpy - i can use in track, but not in savejpg,saveavi!
        webframen = "" # frame number from web.py()
        webframetime = ""

        while connection_ok: #========================================================
            # read the frame from the camera and send it to the server
            #time.sleep(0.05)

            #while True:
            if (str(videodev).find("http://")==0) or (str(videodev).find("https://")==0):

                print("-", end="")
                artdelay = 0
                ret_val = 0
                try:
                    with timeout(4):
                        while ret_val == 0:
                            for i8 in range(1): # I decimate and remove delay
                                #print("1-", flush=True,end="")
                                bytex += stream.read(stream_length)
                                a = bytex.find(b'\xff\xd8') #frame starting
                                b = bytex.find(b'\xff\xd9') #frame ending
                                ttag = bytex.find(f"#FRAME_ACQUISITION_TIME".encode("utf8")) #frame ending
                                webframen = " "*7
                                webframetime = " "*23
                                if ttag!=-1:
                                    #print(f"i... FRACQT: /{ttag}/ /{bytex[ttag:ttag+32]}/----------------")
                                    webframen = bytex[ttag:ttag+32+23].decode("utf8")
                                    webframen = webframen.split("#")
                                    #print(len(webframen), webframen)
                                    webframen,webframetime = webframen[2],webframen[3]

                                    #print( webframen )
                                    #print( webframetime)

                                if a != -1 and b != -1:
                                    jpg = bytex[a:b+2]
                                    BPS+=len(jpg)/1024
                                    if len(jpg)>0:
                                        FPS+=1
                                    bytex = bytex[b+2:]
                                    # just a test.... if I can append
                                    #jpg = jpg+b'#FRAME_ACQUISITION_TIME#'+f"a".encode("utf8")
                                    frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

                                    # ----taken for pause
                                    if (not pause) or  (frame_from_file is None):
                                        frame_from_file = frame
                                        frame_num+=1
                                    else:
                                        frame = frame_from_file
                                        #ret_val = 1
                                        #frame_num+=1 # ??? I keep this stopped or better not?

                                    #stream_length = b+2-a
                                    stream_length = int( (b+2-a)*0.9 ) # expected length

                                    ret_val=1
                                    print("{:.1f}k #{:06d}/{} {:4.1f}Mb/s {:2d}fps {} w{} {}".format(
                                        # len(bytex)/1024,
                                        stream_length/1024,
                                        frame_num,
                                        webframen,
                                        BPSlast*8/1024,
                                        FPSlast,
                                        str(datetime.datetime.now())[11:-4],
                                        webframetime[11:],
                                        sfilenamea.replace('/home/','')
                                    ) , end="\r")

                                else:
                                    ret_val = 0
                                    # frame = None
                                    # print("Non  sizE={:6.0f}kB ".format(len(bytex)/1024), end = "\r" )
                                    # print("Non", end = "\r" )
                except:
                    print("X... exception - connection lost, ")
                    ret_val = 0
                    #frame = None
                    print("RDE  siZe={:6.0f}kB ".format(len(bytex)/1024), end = "\n" )
                    connection_ok = False


                #print("-2", flush=True,end="")
                if (datetime.datetime.now()-BPStag).total_seconds()>1:
                    BPStag = datetime.datetime.now()
                    BPSlast=BPS
                    BPS=0
                    FPSlast = FPS
                    FPS=0


                #while

            else: #                     from file 2nd point
                if (not pause) or  (frame_from_file is None):
                    ret_val,frame = stream.read()
                    frame_from_file = frame
                    frame_num+=1
                else:
                    frame = frame_from_file
                    ret_val = 1
                if ret_val==0:
                    sys.exit(0)
            if connection_ok:
                if (ret_val == 0) or (type(frame)=="NoneType"):
                    print("Not a good frame", type(frame), end="\r")
                    continue
                frame = frame
                (w, h, c) = frame.shape
                frame_area = w*h
                motion_det = False

                # print(".", end="")
                #print("RPINAME=",rpi_name)
                #print(frame)

                wname = videodev

                frames_total+= 1

                #======================================== GAMES WITH FRAMES
                #   hack-expand;  tracker; zoom; rotate; save; measure

                # cv2.namedWindow( wname, cv2.WINDOW_KEEPRATIO ,cv2.WINDOW_GUI_EXPANDED)
                cv2.namedWindow( wname , cv2.WINDOW_KEEPRATIO ) # 2 may allow resize on gigavg
                # cv2.namedWindow( wname , 2 ) # 2 may allow resize on gigavg
                if frames_total < 2:
                    #cv2.namedWindow(wname,cv2.WND_PROP_FULLSCREEN)
                    # ?https://stackoverflow.com/questions/62870031/pixel-coordinates-and-colours-not-showing
                    # TRICK !!!!!!!!!!!!
                    # https://stackoverflow.com/a/52776376
                    cv2.setWindowProperty(wname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    bit_fs = 0
                    if sme in ['gigavg','vaio']: # strange behavior on some PC concerning resize...(checked in MS with vadim)
                        bit_fs =1
                    cv2.setWindowProperty(wname, cv2.WND_PROP_FULLSCREEN,  bit_fs)
                    cv2.resizeWindow(wname, frame.shape[1], frame.shape[0] )





                #-------- i tried all---no help for csrt tracking-------
                #-------- i tried all---no help for csrt tracking-------
                #-------- i tried all---no help for csrt tracking-------
                # frame = cv2.bilateralFilter(frame,5,100,20) # preserve edges
                #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                #(T,frame) = cv2.threshold(frame,  100, 255,
                #                          cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                #frame = cv2.blur( frame, (6,6) ) # doesnt help

                # ======================== track before zoom
                if (tracker1!=None) and (not pause):
                    #print("tracking",tracker1)
                    ok,bbox=tracker1.update(frame)
                    if not ok:
                        continue
                    bbox = [ round(i*10)/10 for i in bbox]
                    (x,y,w,h)=[v for v in bbox]
                    cx,cy = round( 10*(x+w/2))/10, round(10*(y+h/2))/10
                    #print("tracking",ok,bbox," ->", cx,cy)
                    with open( tracker1_fname , "a" ) as f:
                        f.write( f"{webframetime} {webframen} {cx} {cy}\n" )
                        #   f.write( f"{webframetime[11:]} {webframen} {cx} {cy}\n" )

                    if (webframen.strip(" ")==""):
                        webframen=frame_num
                        ttime = int(webframen)
                    else:
                        # better this, fractions are kept...
                        ttime  = datetime.datetime.strptime(webframetime,
                                                        "%Y-%m-%d %H:%M:%S.%f")


                    tracker_list.append( (round(cx), round(cy),  ttime ) )
                    colmax=255
                    colmaxb=0
                    for i in reversed(tracker_list):
                        x2,y2,ttime=i
                        frame[ y2,x2 ] = (colmaxb,255-colmax-colmaxb,255)
                        if colmax>1:
                            colmax-=1
                        elif (colmaxb<255) and (colmaxb>1):
                            colmaxb+=1

                    # ------------ play on cropping -- may further stabilize
                    cropped = frame[round(y):round(y+h), round(x):round(x+w)]
                    # normalize region-   problems/crashes on pause
                    #resu = np.zeros((640,480))
                    #cropped = cv2.normalize(cropped, resu,0,255,cv2.NORM_MINMAX)
                    #    gray
                    ##cropped = cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)
                    ##cropped = cv2.blur( cropped, (2,2) )
                    ##(T,cropped) = cv2.threshold(cropped,  100, 255,  cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                    # merge back to BGR
                    ##cropped = cv2.merge([cropped,cropped,cropped] )

                    # # return cropped to main image -------------- problem on pause+normalize
                    #frame[round(y):round(y+h), round(x):round(x+w)] = cropped


                    # ---ORB feature matching...
                    #cropped = frame[round(y):round(y+h), round(x):round(x+w)]
                    #kp,des = orb.detectAndCompute(cropped,None)
                    #frame[round(y):round(y+h), round(x):round(x+w)] = cv2.drawKeypoints(cropped,kp,None)

                    #--- ups
                    #if not( (x<0)or(y<0)or(x+w>=frame.shape[1])or(y+h>=frame.shape[0]) ):
                    #print("rect")

                    # # - the other part HSV histo ---- HISTO TRACKING
                    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    # dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
                    # ret, track_window = cv2.meanShift(dst,track_window, term_crit)
                    # xh,yh,wh,hh = track_window

                    cv2.rectangle(frame,(round(x),round(y)),
                                  (round(x+w),round(y+h)),(0,255,0),1,1)
                    cv2.line(frame,(round(cx),round(cy)),
                             ( round(cx),round(cy) ) ,(0,255,0),2,1)

                    # cv2.rectangle(frame, (xh,yh), (xh+wh,yh+hh), (0,0,255),1,1)
                    # cxh,cyh= round( 10*(xh+wh/2))/10, round(10*(yh+hh/2))/10
                    # cv2.line(frame,(round(cxh),round(cyh)),(round(cxh),round(cyh)),
                    #          (0,0,255),2,1)

                # ================= track2
                if tracker2!=None:
                    #print("tracking",tracker)
                    # frame = cv2.blur( frame, (4,4) )
                    ok2,bbox2=tracker2.update(frame)
                    bbox2 = [ round(i*10)/10 for i in bbox2]
                    #print("\ntracking2",ok2,bbox2)
                    (x2,y2,w2,h2)=[v for v in bbox2]
                    #if not( (x<0)or(y<0)or(x+w>=frame.shape[1])or(y+h>=frame.shape[0]) ):
                    #print("rect")
                    cv2.rectangle(frame,(int(x2),int(y2)),(int(x2+w2),int(y2+h2)),(0,255,255),1,1)
                    cx2,cy2 = round( 10*(x2+w2/2))/10, round(10*(y2+h2/2))/10
                    cv2.line(frame,(int(cx2),int(cy2)),
                             ( int(cx2),int(cy2)
                             ),(0,255,255),2,1)
                    with open( tracker2_fname, "a" ) as f:
                        if webframen=="":
                            webframen=frame_num
                        f.write( f"{webframetime} {webframen} {cx2} {cy2}\n" )


                #------------------------redcross here: before zoom--------------------------------------
                #print(f" ... cross == {cross}")
                if not (cross is None):
                    if senh.add_frame(frame):
                        w,h,c = frame.shape
                        # print(w-centerY1, h-centerX1)
                        #print(f" ... cross {w} {h} /2")
                        senh.crosson( cross[0], cross[1] , color = "r" ) # dx dy
                        # senh.setbox(f"CROS",  senh.jpg)
                        frame = senh.get_frame(  )
                    else:
                        print("X... senh did not accept frame (in redcross)")

                #=========================== ZOOM ME and OTHERS =======

                if zoomme>1: # FUNNY - it continues to zoom where the mouse pointer is !!!!
                    if senh.add_frame(frame):
                        # print("avi..")
                        senh.setbox(f"z {zoomme}",  senh.scale)
                        w,h = frame.shape[0],frame.shape[1]
                        # print(w-centerY1, h-centerX1)
                        senh.zoom( zoomme , int(centerX1-h/2), int(centerY1-w/2)  )
                        frame = senh.get_frame(  )

                #---------------------------------------------------- rotate ------------------
                # if rotate180:
                #     if senh.add_frame(frame):
                #         senh.setbox(f"ROT",  senh.rot)
                #         # w,h,c = frame.shape
                #         # print(w-centerY1, h-centerX1)
                #        senh.rotate180( 180 )
                #        frame = senh.get_frame(  )
                if rotate == 180:
                    frame = cv2.rotate(frame, cv2.ROTATE_180)
                    #frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)


                if save:
                    # print("AVI")
                    saviout.write(frame)
                    if senh.add_frame(frame):
                        # print("avi..")
                        senh.setbox(f"AVI",  senh.avi)
                        frame = senh.get_frame(  )
                if saved_jpg:
                    if senh.add_frame(frame):
                        # print("avi..")
                        senh.setbox(f"JPG",  senh.jpg)
                        frame = senh.get_frame(  )




                if show_help:
                    # show_help = True
                    frame = disp_mutext( frame, HELPTEXT )


                if (allow_tracker_demand) and not(allow_tracker):
                    TRACKERHELP = """
u ... return back

t ... use tracker1
T ... use tracker2
  ...  ENTER or SPACE to accept region
  ...  c cancel
"""
                    frame = disp_mutext( frame, TRACKERHELP )




                # MEASUREMENT ==================================

                if measure>0:
                    h,w = frame.shape[0], frame.shape[1]
                    # measure_fov = 110.5 # notebook

                    # approximative, not precise... 5%
                    radians_per_pixel =  (measure_fov /180*math.pi) /w

                    # rad per pix * unit distance * better
                    radians_per_pixel2 =  math.tan(measure_fov /180*math.pi/2/w)


                    radians_per_pixel2/=zoomme

                    #print(f"RPPX {radians_per_pixel}  {radians_per_pixel2} ")

                    # now arbitrarily define 1 meter..like.. 100px =>
                    # alpha = 100*radians_per_pixel
                    # b = 1m / math.tan( alpha )

                    def get_order(dist = 1.7): #  determine order that fits
                        # list of marks on the ruler
                        wide=0.01
                        while True:
                            wide*=10
                            pixwid = math.atan( wide/dist ) / radians_per_pixel2
                            alpha = pixwid * radians_per_pixel2
                            if pixwid>w/2*0.8: # not full rANGE
                                wide/=10
                                pixwid = math.atan( wide/dist ) / radians_per_pixel2
                                alpha = pixwid * radians_per_pixel2
                                break
                        order = wide
                        row = []

                        while True:
                            wide+=order
                            pixwid = math.atan( wide/dist ) / radians_per_pixel2
                            alpha = pixwid * radians_per_pixel2
                            if pixwid>w/2*0.8: # not full rANGE:
                                wide-=order
                                pixwid = math.atan( wide/dist ) / radians_per_pixel2
                                alpha = pixwid * radians_per_pixel2
                                break
                            else:
                                row.append(wide)
                        #-----
                        #-----
                        row=row[::-1] # revert - we want Big to small
                        row.append(order)
                        if len(row)<4:
                            in0 = row[-1]/2
                            in1 = row[-1]/5
                            #in2 = row[-1]/10
                            row.append( in0 )
                            row.append( in1 )
                            #row.append( in2 )
                        return row # Big to small


                    def one_mark( dist = 1.7, wide=[1,2] , speed=0):
                        #  wide ...  # Big to small
                        #h,w = frame.shape[0], frame.shape[1]
                        # pixel distance of halfwidth

                        # alpha = pixwid * radians_per_pixel2
                        # dist = wide/math.tan( alpha)
                        # I need to calculate 1m
                        level=0
                        #print("XXXXX",wide)
                        for iwide in wide:
                            pixwid = math.atan( iwide/dist ) / radians_per_pixel2
                            alpha = pixwid * radians_per_pixel2

                            #print(f" {radians_per_pixel}radpp {pixwid}   {wide}m <- {dist} ")
                            step = 0
                            mX,mY = int(w/2),int(h/2)
                            if not(cross is None):
                                mX+=cross[0]
                                mY+=cross[1]
                            # here I addd the red cross position


                            mY= mY+level*step


                            yA, yB = mY, mY

                            xA = mX
                            xB = mX + int(pixwid)
                            color = (0,255,0) # BGR
                            color = (55,0,255) # BGR same as the red cross
                            if level==0:
                                # line
                                cv2.line(frame,
                                         (int(xA), int(yA)), (int(xB), int(yB)),
                                         color, 1)
                            # vet bars
                            cv2.line(frame,
                                     (int(xA), int(yA+2)), (int(xA), int(yA-2)),
                                     color, 1)
                            cv2.line(frame,
                                     (int(xB), int(yB+2)), (int(xB), int(yB-2)),
                                     color, 1)



                            unit = "m"
                            # --- check the biggest to set the unit
                            if wide[0]<=0.01:
                                iwide = round(iwide*100*1000)/1000
                                unit = "cm"
                            elif wide[0]<=0.1:
                                iwide = round(iwide*100*100)/100
                                unit = "cm"
                            elif wide[0]<1:
                                iwide = round(iwide*100)/100
                            else:
                                iwide = round(iwide*10)/10

                            # only properly round whatever unit
                            if iwide<=0.01:
                                iwide = round(iwide*1000)/1000
                            elif iwide<=0.1:
                                iwide = round(iwide*100)/100
                            elif iwide<1:
                                iwide = round(iwide*10)/10
                            else:
                                iwide = round(iwide)

                            if level>0: unit="" # no unit during the scale
                            unit2 = "m"



                            if str(iwide)[:2] == "0.":iwide=str(iwide)[1:]

                            # width on scale
                            cv2.putText(frame, f"{iwide}{unit}",
                                        (int(xB-10), int(  mY -7 )),  # little rightx a bit up y
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.35, color, 1)
                            if level >= 0:
                                # distance - only at first mark
                                cv2.putText(frame, f"  at {dist} {unit2}",
                                            (int(xA-130), int(  mY+5 )),  # little rightx a bit up y
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.35, color, 1)
                                cv2.putText(frame, f"  FOV {measure_fov:.1f}deg",
                                            (int(xA-130), int(  mY+15 )),  # little rightx a bit up y
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.35, color, 1)
                                # I add velocity
                                if (level==0) and not(tracker1 is None):
                                    cv2.putText(frame, f"speed {speed:6.2f}m/s",
                                            (int(xB-50), int(  mY+15 )),  # little rightx a bit up y
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.35, color, 1)
                            level+=1


                    # main part of the ruler making---------------
                    order = get_order(dist=measure)
                    # speed computation
                    if not(tracker1 is None) and len(tracker_list)>2:
                        b=tracker_list[-1]
                        try:
                            v_from = -2
                            a=tracker_list[ v_from]
                            while True:
                                dt=(b[2]-a[2]).total_seconds()
                                if dt>1.0:
                                    break
                                else:
                                    v_from-=1
                                if len(tracker_list)<abs(v_from): break
                                a=tracker_list[ v_from]
                        except:
                            dt=100000 # velocity 0
                        c= ( (b[0]-a[0])**2 + (b[1]-a[1])**2 )**0.5
                        v = c/dt * radians_per_pixel2
                        v = round( 100* math.tan(v) * measure )/100
                        # print(f"i... speed = {v} m/s  {dt:.2}==dt " )
                    else:
                        v = 0
                    # plot ruler
                    one_mark( dist=measure ,    wide=order ,  speed=v)



                if local_gamma!=1:
                    frame = adjust_gamma(frame, local_gamma)



                #======================================================== IMSHOW
                #======================================================== IMSHOW
                #======================================================== IMSHOW
                #======================================================== IMSHOW
                cv2.imshow(rpi_name, frame ) # 1 window for each RPi
                # this may be useful?
                if False:
                    if not (cropped is None):
                        cropped = cv2.resize(cropped, (640,480) )
                        cv2.imshow("tracking1", cropped ) # ZOOM ON TRACK
                        # cv2.resizeWindow(

                if expande >1 :
                    cv2.resizeWindow( rpi_name, int(expande*frame.shape[1]), int(expande*frame.shape[0]) )
                    #print(frame.shape)
                #cv2.setWindowProperty(rpi_name, cv2.WND_PROP_TOPMOST, 1)
                # cv2.namedWindow(rpi_name, cv2.WINDOW_GUI_EXPANDED)
                # time.sleep(0.2)
                cv2.setMouseCallback(rpi_name, MOUSE)
                key = cv2.waitKeyEx(1)
                key = remap_keys(key) # make compatible with waitKey()





                # print(f"{centerX1} {centerY1}")
                if (cross is None) and not greencross:
                    if (not frame is None) and (rpi_name!="") and (key == ord('h')):
                        print("h PRESSED! - ")
                        show_help = not(show_help)
                        print(HELPTEXT)



                #-----------------------------------------------------rotate zoom

                if (not frame is None) and (rpi_name!="") and (key == ord('r')):
                    print("r PRESSED! - rotate change")
                    if rotate == 180:
                        rotate = 0
                    else:
                        rotate = 180



                if (not frame is None) and (rpi_name!="") and (key == ord('z')):
                    print(f"z PRESSED! - ZOOM {zoomme}x")
                    zoomme*= 2
                    if zoomme>16:
                        zoomme=1
                    sfilenamea = ""


                if (not frame is None) and (rpi_name!="") and (key == ord('Z')):
                    print("Z PRESSED! - ZOOM ended")
                    zoomme = 1
                    sfilenamea = ""

                # ------------------------------------------ web  pause quit expa---------------


                if (not frame is None) and (rpi_name!="") and (key == ord('w')):
                    print("w PRESSED! - openning web browser")
                    webbrowser.open( videodev.replace("/video","" ) ) # BRUTAL


                if (not frame is None) and (rpi_name!="") and (key == ord(' ')):
                    print("SPC PRESSED! - pause/play")
                    pause = not pause
                    print(f" ... pause = {pause}" )

                if (not frame is None) and (rpi_name!="") and (key == ord('q')):
                    print("q PRESSED!")
                    sys.exit(1)



                if (not frame is None) and (rpi_name!="") and (key == ord('x')):
                    print("x PRESSED! - expand 2")

                    if expande == 2:
                        expande = 1
                    else:
                        expande = 2

                #-----------------------------------------------------save s a


                if (not frame is None) and (rpi_name!="") and (key == ord('a')):
                    print("a PRESSED! - saving AVI")
                    save = True
                    sfilenamea,saviout = setupsave()
                    print(">>>", sfilenamea )

                if (not frame is None) and (rpi_name!="") and (key == ord('A')):
                    print("A PRESSED! - STOPPING stopping saving AVI")
                    save = False
                    sfilenamea = ""

                saved_jpg = False
                if (not frame is None) and (rpi_name!="") and (key == ord('s')):
                    print("s PRESSED!")
                    sname = "snapshot"
                    saved_jpg = True
                    sfilename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    # defined above # sme = socket.gethostname()
                    sfilename = f"{sme}{sname}_{sfilename}.jpg"

                    dir2create = os.path.expanduser("~/DATA/")
                    if not os.path.isdir( os.path.expanduser(dir2create )):
                        print(f"D... trying to create directory {dir2create} for saving")
                        #result = False
                        os.mkdir( os.path.expanduser(dir2create ))


                    sfilename = os.path.expanduser( "~/DATA/"+sfilename )
                    # sfourcc = cv2.VideoWriter_fourcc(*'XVID')
                    # saviout = cv2.VideoWriter( sfilename , sfourcc , 25.0, (640,480))
                    isWritten = cv2.imwrite( sfilename, frame )
                    if isWritten:
                        print('Image is successfully saved as file.', sfilename)


                #------------------------- measure and cross -------------------------------

                if (not frame is None) and (rpi_name!=""):
                    if (key == ord('C')):
                        print(f"c PRESSED! - cross = {cross} OFF; saving {FILE_REDCROSS}")
                        with open( os.path.expanduser(FILE_REDCROSS) ,"w") as f:
                            f.write( f"{cross[0]}\n{cross[1]}\n" )
                            cross = None
                    if (key == ord('c')):
                        if cross is None:
                            cross = [ 0,0 ]
                            if os.path.exists( os.path.expanduser(FILE_REDCROSS) ):
                                try:
                                    with open( os.path.expanduser(FILE_REDCROSS) ) as f:
                                        cr = f.readlines()
                                        cross = [ int(cr[0]) ,  int(cr[1])  ]
                                except:
                                    print(f"X... problem to open {FILE_REDCROSS}")
                            print(f"c PRESSED! - cross = {cross} ON")

                #--------- redcross manip
                if not(cross is None):
                    if (not frame is None) and (rpi_name!="") and (key == ord('h')): #<
                        cross[0]-=4
                    if (not frame is None) and (rpi_name!="") and (key == ord('j')): #v
                        cross[1]+=4
                    if (not frame is None) and (rpi_name!="") and (key == ord('k')): #^
                        cross[1]-=4
                    if (not frame is None) and (rpi_name!="") and (key == ord('l')): #>
                        cross[0]+=4

                    if (not frame is None) and (rpi_name!="") and (key == ord('H')): #<
                        cross[0]-=17
                    if (not frame is None) and (rpi_name!="") and (key == ord('J')): #v
                        cross[1]+=17
                    if (not frame is None) and (rpi_name!="") and (key == ord('K')): #^
                        cross[1]-=17
                    if (not frame is None) and (rpi_name!="") and (key == ord('L')): #>
                        cross[0]+=17



                if (measure!=0) and (not frame is None) and (rpi_name!="") and (key == ord('n')):
                    print("n PRESSED! - measure distance - far")
                    measure = round(10*measure/1.15)/10
                    if measure <0.4:
                        measure = 0.4

                if  (measure!=0) and (not frame is None) and (rpi_name!="") and (key == ord('N')):
                    print("m PRESSED! - measure distance - closer")
                    if measure == 0:
                        measure = 1
                    measure = round(10*measure*1.15)/10
                    if measure >20000:
                        measure = 20000

                if (not frame is None) and (rpi_name!="") and (key == ord('m')):
                    print("m PRESSED! - measure distance - ON")
                    if measure == 0:
                        measure = 1

                if (not frame is None) and (rpi_name!="") and (key == ord('M')):
                    print("M PRESSED! - DEmeasure")
                    measure = 0

                if (not frame is None) and (rpi_name!="") \
                   and (measure!=0) and (key == ord('f')):
                    print("f PRESSED! - FOV increase")
                    measure_fov = measure_fov*1.25
                    if measure_fov>3:
                        measure_fov = round(measure_fov)
                    else:
                        measure_fov = round(measure_fov*10)/10
                    if measure_fov>180:
                        measure_fov = 180
                if (not frame is None) and (rpi_name!="") \
                   and (measure!=0) and (key == ord('F')):
                    print("F PRESSED! - FOV decrease")
                    measure_fov = measure_fov/1.25
                    if measure_fov>3:
                        measure_fov = round(measure_fov)
                    else:
                        measure_fov = round(measure_fov*10)/10

                    if measure_fov<0.3:
                        measure_fov=0.3




                #---------------- trackers--------------- t T u----------------


                # ------if ALLOWED - first - to have no display help
                # elif to skip one loop
                if (allow_tracker) and (not frame is None) \
                     and (rpi_name!="") \
                     and allow_tracker1:
                     # and (key == ord('t')):
                    # print("t PRESSED! - track" ,tracker1,"\n")
                    print("i ... setting allowed tracker1 \n")
                    allow_tracker = False
                    tracker1 = cv2.TrackerCSRT_create() # KCF GOTURN MIL
                    bbox = cv2.selectROI(frame)
                    if (len(bbox)<4)or(bbox[-1]<10):
                        tracker1 = None
                        print("i... fail init track")
                    else:
                        #bbox = tuple([ i+0.5 for i in bbox ])
                        ok = tracker1.init(frame,bbox)
                        tracker_list=[]
                        tracker1_fname = datetime.datetime.now().strftime("tracker1_%Y%m%d_%H%M%S.dat")
                        # #------------this is for histotracker
                        # x,y,w,h = bbox
                        # track_window = bbox
                        # # roi = frame[x:x+w, y:y+h]
                        # roi = frame[ y:y+h, x:x+w]
                        # hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                        # mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
                        # roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
                        # cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
                        # term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 200, 0.1 ) #iters, eps

                        # orb = cv2.ORB_create() # I dont use now

                if  (allow_tracker) and (not frame is None) \
                    and (rpi_name!="") \
                    and allow_tracker2:
                    # and (key == ord('T')):
                    print("t PRESSED! - track" ,tracker2)
                    print("i ... setting allowed tracker2 \n")
                    allow_tracker = False
                    tracker2 = cv2.TrackerKCF_create() # KCF GOTURN MIL
                    bbox2 = cv2.selectROI(frame)
                    if (len(bbox2)<4) or  (bbox2[-1]<10):
                        tracker2 = None
                        print("i... fail init track2")
                    else:
                        #bbox2 = tuple([ i+0.5 for i in bbox2 ])
                        ok2 = tracker2.init(frame,bbox2)
                        tracker2_fname = datetime.datetime.now().strftime("tracker2_%Y%m%d_%H%M%S.dat")





                # -----  allow display help, after allow tracker true
                if (not frame is None) and (rpi_name!="") \
                and (  (key == ord('t')) or (key == ord('T')) ) \
                and not(allow_tracker_demand) and not(allow_tracker):
                    print("i... allow tracker demand\n")
                    allow_tracker_demand = True
                    allow_tracker2 = False
                    allow_tracker1 = False
                    # switch on the menu display

                # --- 2nd 't' press :  is before demand=True, sets allow true
                elif (not frame is None) and (rpi_name!="") and (  (key == ord('t')) or (key == ord('T')) ) and (allow_tracker_demand) and not(allow_tracker):
                    print("i... allowing tracker, removing tracker_demand\n")
                    allow_tracker = True # but I need one loop to remove menu
                    # switch off the menudisplay
                    allow_tracker_demand = False
                    allow_tracker2 = False
                    allow_tracker1 = False
                    if key == ord('T'): allow_tracker2 = True
                    if key == ord('t'): allow_tracker1 = True





                if (not frame is None) and (rpi_name!="") and (key == ord('u')):
                    print("u PRESSED! - UNtrack" )
                    tracker1 = None
                    tracker2 = None
                    tracker_date = None
                    allow_tracker_demand = False
                    allow_tracker = False

                if (not frame is None) and (rpi_name!="") and (key == ord('v')):
                    print("v PRESSED! - green crosson" )
                    greencross = True
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'crosson':'CROSSON'}
                    post_response = requests.post(url=post_addr, data=post_data)

                if (not frame is None) and (rpi_name!="") and (key == ord('V')):
                    print("V PRESSED! - green crossoff" )
                    greencross = False
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'crossoff':'CROSSOFF'}
                    post_response = requests.post(url=post_addr, data=post_data)



                if (not frame is None) and (rpi_name!="") and (key == ord('b')):
                    print("b PRESSED! - substrac background" )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'subbg':'SUBBG'}
                    post_response = requests.post(url=post_addr, data=post_data)

                if (not frame is None) and (rpi_name!="") and (key == ord('B')):
                    print("B PRESSED! - save background" )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'savebg':'SAVEBG'}
                    post_response = requests.post(url=post_addr, data=post_data)


                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('f')):
                    print("f PRESSED! - mix foreground" )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'mixfg':'MIXFG'}
                    post_response = requests.post(url=post_addr, data=post_data)

                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('F')):
                    print("F PRESSED! - save foreground" )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'savefg':'SAVEFG'}
                    post_response = requests.post(url=post_addr, data=post_data)





                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('e')):
                    print("e PRESSED! - " )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'expo2':'EXPO2'}
                    post_response = requests.post(url=post_addr, data=post_data)

                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('E')):
                    print("e PRESSED! - " )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'expo05':'EXPO05'}
                    post_response = requests.post(url=post_addr, data=post_data)

                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == 1310821 ):
                    print("ctrl-e PRESSED! - " )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'expo':'EXPO'}
                    post_response = requests.post(url=post_addr, data=post_data)




                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('g')):
                    print("g PRESSED! - " )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'gain2':'GAIN2'}
                    post_response = requests.post(url=post_addr, data=post_data)

                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('G')):
                    print("G PRESSED! - " )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'gain05':'GAIN05'}
                    post_response = requests.post(url=post_addr, data=post_data)

                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == 1310823):
                    print("ctrl-g PRESSED! - " )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'gain':'GAIN'}
                    post_response = requests.post(url=post_addr, data=post_data)




                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('y')):
                    print("y PRESSED! - " )
                    local_gamma = local_gamma*1.4

                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('Y')):
                    print("Y PRESSED! - " )
                    local_gamma = local_gamma /1.4

                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == 1310841):
                    print("ctrl-y PRESSED! - " )
                    local_gamma = 1



                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('p')):
                    print("p PRESSED! - " )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'fixed':'FIXED'}
                    post_response = requests.post(url=post_addr, data=post_data)

                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('P')):
                    print("p PRESSED! - " )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'live':'LIVE'}
                    post_response = requests.post(url=post_addr, data=post_data)


                #--------- greencross manip
                if (cross is None) and greencross:
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {}

                    if (not frame is None) and (rpi_name!="") and (key == ord('h')): #<
                        post_data = {'left':'LEFT'}
                    if (not frame is None) and (rpi_name!="") and (key == ord('j')): #v
                        post_data = {'down':'DOWN'}
                    if (not frame is None) and (rpi_name!="") and (key == ord('k')): #^
                        post_data = {'up':'UP'}
                    if (not frame is None) and (rpi_name!="") and (key == ord('l')): #>
                        post_data = {'right':'RIGHT'}

                    if (not frame is None) and (rpi_name!="") and (key == ord('H')): #<
                        post_data = {'left2':'LEFT2'}
                    if (not frame is None) and (rpi_name!="") and (key == ord('J')): #v
                        post_data = {'down2':'DOWN2'}
                    if (not frame is None) and (rpi_name!="") and (key == ord('K')): #^
                        post_data = {'up2':'UP2'}
                    if (not frame is None) and (rpi_name!="") and (key == ord('L')): #>
                        post_data = {'right2':'RIGHT2'}

                    if post_data != {}:
                        post_response = requests.post(url=post_addr, data=post_data)



                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('i')):
                    integrate*=2
                    print(f"i PRESSED! - accum  {integrate} snapshots" )
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'accum':'ACCUM', 'accumtxt':int(integrate)}
                    post_response = requests.post(url=post_addr, data=post_data)

                if (not frame is None) and (rpi_name!="") \
                   and (measure==0) and (key == ord('I')):
                    print("i PRESSED! - accum integrate 1" )
                    integrate = 1
                    post_addr = videodev.replace("/video","/cross" )
                    post_data = {'accum':'ACCUM', 'accumtxt':0}
                    post_response = requests.post(url=post_addr, data=post_data)



#                if key!=-1:
#                    print(f"\n{key}\n")

if __name__=="__main__":
    Fire( display3)
    #Fire({ "disp":display2,   "disp2":display2    })
