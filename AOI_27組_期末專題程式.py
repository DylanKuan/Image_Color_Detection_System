# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 21:15:18 2022

@author: kuanc
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 02:17:28 2022

@author: kuanc
"""

import cv2;
import numpy as np;

def allocate_color_dict(color_dict) :
    
    color_dict['Snow'] = [255,250,250];
    color_dict['GhostWhite'] = [255,248,248];
    color_dict['WhiteSmoke'] = [245,245,245];
    color_dict['Gainsboro'] = [220,220,220];
    color_dict['FloralWhite'] = [240,250,255];
    color_dict['OldLace'] = [230,245,253];
    color_dict['Linen'] = [230,240,250];
    color_dict['AntiqueWhite'] = [215,235,250];
    color_dict['PapayaWhip'] = [213,239,255];
    color_dict['BlanchedAlmond'] = [205,235,255];
    color_dict['Bisque'] = [196,228,255];
    color_dict['PeachPuff'] = [185,218,255];
    color_dict['NavajoWhite'] = [173,222,255];
    color_dict['Moccasin'] = [181,228,255];
    color_dict['Cornsilk'] = [220,248,255];
    color_dict['Ivory'] = [240,255,255];
    color_dict['LemonChiffon'] = [205,250,255];
    color_dict['Seashell'] = [238,245,255];
    color_dict['Honeydew'] = [240,255,255];
    color_dict['MintCream'] = [250,255,245];
    color_dict['Azure'] = [255,255,240];
    color_dict['AliceBlue'] = [255,248,240];
    color_dict['lavender'] = [250,230,230];
    color_dict['LavenderBlush'] = [245,240,255];
    color_dict['MistyRose'] = [225,228,255];
    color_dict['White'] = [255,255,255];
    color_dict['Black'] = [0,0,0];
    color_dict['DarkSlateGray'] = [79,79,47];
    color_dict['DimGrey'] = [105,105,105];
    color_dict['SlateGrey'] = [144,128,112];
    color_dict['LightSlateGray'] = [153,136,119];
    color_dict['Grey'] = [190,190,190];
    color_dict['LightGray'] = [211,211,211];
    color_dict['MidnightBlue'] = [112,25,25];
    color_dict['NavyBlue'] = [128,0,0];
    color_dict['CornflowerBlue'] = [137,149,100];
    color_dict['DarkSlateBlue'] = [139,61,72];
    color_dict['SlateBlue'] = [205,90,106];
    color_dict['MediumSlateBlue'] = [238,104,123];
    color_dict['LightSlateBlue'] = [255,112,132];
    color_dict['MediumBlue'] = [205,0,0];
    color_dict['RoyalBlue'] = [225,105,65];
    color_dict['Blue'] = [255,0,0];
    color_dict['DodgerBlue'] = [255,144,30];
    color_dict['DeepSkyBlue'] = [255,191,0];
    color_dict['SkyBlue'] = [235,206,135];
    color_dict['LightSkyBlue'] = [250,206,135];
    color_dict['SteelBlue'] = [180,130,70];
    color_dict['LightSteelBlue'] = [222,196,176];
    color_dict['LightBlue'] = [230,216,173];
    color_dict['PowderBlue'] = [230,224,176];
    color_dict['PaleTurquoise'] = [238,238,175];
    color_dict['DarkTurquoise'] = [209,206,0];
    color_dict['MediumTurquoise'] = [204,209,72];
    color_dict['Turquoise'] = [208,224,64];
    color_dict['Cyan'] = [255,255,0];
    color_dict['LightCyan'] = [255,255,224];
    color_dict['CadetBlue'] = [160,158,95];
    color_dict['MediumAquamarine'] = [170,205,102];
    color_dict['Aquamarine'] = [212,255,127];
    color_dict['DarkGreen'] = [0,100,0];
    color_dict['DarkOliveGreen'] = [47,107,85];
    color_dict['DarkSeaGreen'] = [143,188,143];
    color_dict['SeaGreen'] = [87,139,46];
    color_dict['MediumSeaGreen'] = [113,179,60];
    color_dict['LightSeaGreen'] = [170,178,32];
    color_dict['PaleGreen'] = [152,251,152];
    color_dict['SpringGreen'] = [127,255,0];
    color_dict['LawnGreen'] = [0,252,124];
    color_dict['Green'] = [0,255,0];
    color_dict['Chartreuse'] = [0,255,127];
    color_dict['MedSpringGreen'] = [154,250,0];
    color_dict['GreenYellow'] = [47,255,173];
    color_dict['LimeGreen'] = [50,205,50];
    color_dict['YellowGreen'] = [50,205,154];
    color_dict['ForestGreen'] = [34,139,34];
    color_dict['OliveDrab'] = [35,142,107];
    color_dict['DarkKhaki	'] = [107,183,189];
    color_dict['PaleGoldenrod'] = [170,232,238];
    color_dict['LtGoldenrodYello'] = [210,250,250];
    color_dict['LightYellow'] = [224,255,255];
    color_dict['Yellow'] = [0,255,255];
    color_dict['Gold'] = [0,215,255];
    color_dict['LightGoldenrod'] = [130,221,238];
    color_dict['goldenrod'] = [32,165,218];
    color_dict['DarkGoldenrod'] = [11,134,184];
    color_dict['RosyBrown'] = [143,143,188];
    color_dict['IndianRed'] = [92,92,205];
    color_dict['SaddleBrown'] = [19,69,139];
    color_dict['Sienna'] = [45,82,160];
    color_dict['Peru'] = [63,133,205];
    color_dict['Burlywood'] = [135,184,222];
    color_dict['Beige'] = [220,245,245];
    color_dict['Wheat'] = [179,222,245];
    color_dict['SandyBrown'] = [96,164,244];
    color_dict['Tan'] = [140,180,210];
    color_dict['Chocolate'] = [30,105,210];
    color_dict['Firebrick'] = [34,34,178];
    color_dict['Brown'] = [42,42,165];
    color_dict['DarkSalmon'] = [122,150,233];
    color_dict['Salmon'] = [114,128,250];
    color_dict['LightSalmon'] = [122,160,255];
    color_dict['Orange'] = [0,165,255];
    color_dict['DarkOrange'] = [0,140,255];
    color_dict['Coral'] = [80,127,255];
    color_dict['LightCoral'] = [128,128,240];
    color_dict['Tomato'] = [71,99,255];
    color_dict['OrangeRed'] = [0,69,255];
    color_dict['Red'] = [0,0,255];
    color_dict['HotPink'] = [180,105,255];
    color_dict['DeepPink'] = [147,20,255];
    color_dict['Pink'] = [203,192,255];
    color_dict['LightPink'] = [193,182,255];
    color_dict['PaleVioletRed'] = [147,112,219];
    color_dict['Maroon'] = [96,48,176];
    color_dict['MediumVioletRed'] = [133,21,199];
    color_dict['VioletRed'] = [144,32,208];
    color_dict['Magenta'] = [255,0,255];
    color_dict['Violet'] = [238,130,238];
    color_dict['Plum'] = [221,160,221];
    color_dict['Orchid'] = [214,112,218];
    color_dict['MediumOrchid'] = [211,85,186];
    color_dict['DarkOrchid'] = [204,50,153];
    color_dict['DarkViolet'] = [211,0,148];
    color_dict['BlueViolet'] = [226,43,138];
    color_dict['Purple'] = [240,32,160];
    color_dict['MediumPurple'] = [219,112,147];
    color_dict['Thistle'] = [216,191,216];
    color_dict['JackieBlue'] = [70,23,11];
    color_dict['Indigo'] = [84,46,8];
    color_dict['DarkRed'] = [0,0,139];
    color_dict['DarkMagenta'] = [139,0,139];
    color_dict['DarkCyan'] = [139,139,0];
    color_dict['grey11'] = [28,28,28];
    color_dict['grey21'] = [54,54,54];
    color_dict['grey31'] = [79,79,79];
    color_dict['grey41'] = [105,105,105];
    color_dict['grey51'] = [130,130,130];
    color_dict['grey61'] = [156,156,156];
    color_dict['grey71'] = [181,181,181];
    color_dict['gray81'] = [207,207,207];
    color_dict['gray91'] = [232,232,232];
    color_dict['RosyBrown1'] = [193,193,255];
    color_dict['RosyBrown2'] = [180,180,238];
    color_dict['RosyBrown3'] = [155,155,205];
    color_dict['RosyBrown4'] = [105,105,139];
    color_dict['IndianRed1'] = [106,106,255];
    color_dict['IndianRed2'] = [99,99,238];
    color_dict['IndianRed3'] = [85,85,205];
    color_dict['IndianRed4'] = [58,58,139];
    color_dict['Sienna1'] = [71,130,255];
    color_dict['Sienna2'] = [66,121,238];
    color_dict['Sienna3'] = [57,104,205];
    color_dict['Sienna4'] = [38,71,139];
    color_dict['Burlywood1'] = [155,211,255];
    color_dict['Burlywood2'] = [145,197,238];
    color_dict['Burlywood3'] = [125,170,205];
    color_dict['Burlywood4'] = [85,115,139];
    color_dict['Wheat1'] = [186,231,255];
    color_dict['Wheat2'] = [174,216,238];
    color_dict['Wheat3'] = [150,186,205];
    color_dict['Wheat4'] = [102,126,139];
    color_dict['Tan1'] = [79,165,255];
    color_dict['Tan2'] = [73,154,238];
    color_dict['Tan3'] = [63,133,205];
    color_dict['Tan4'] = [43,90,139];
    color_dict['Chocolate1'] = [36,127,255];
    color_dict['Chocolate2'] = [33,118,238];
    color_dict['Chocolate3'] = [29,102,205];
    color_dict['Chocolate4'] = [19,69,139];
    color_dict['Firebrick1'] = [48,48,255];
    color_dict['Firebrick2'] = [44,44,238];
    color_dict['Firebrick3'] = [38,38,205];
    color_dict['Firebrick4'] = [26,26,139];
    color_dict['Brown1'] = [64,64,255];
    color_dict['Brown2'] = [59,59,238];
    color_dict['Brown3'] = [51,51,205];
    color_dict['Brown4'] = [35,35,139];
    color_dict['Salmon1'] = [105,140,255];
    color_dict['Salmon2'] = [98,130,238];
    color_dict['Salmon3'] = [84,112,205];
    color_dict['Salmon4'] = [57,76,139];
    color_dict['LightSalmon1'] = [122,160,255];
    color_dict['LightSalmon2'] = [114,149,238];
    color_dict['LightSalmon3'] = [98,129,205];
    color_dict['LightSalmon4'] = [66,87,139];
    color_dict['Orange1'] = [0,165,255];
    color_dict['Orange2'] = [0,154,238];
    color_dict['Orange3'] = [0,133,205];
    color_dict['Orange4'] = [0,90,139];
    color_dict['DarkOrange1'] = [0,127,255];
    color_dict['DarkOrange2'] = [0,118,238];
    color_dict['DarkOrange3'] = [0,102,205];
    color_dict['DarkOrange4'] = [0,69,139];
    color_dict['Coral1'] = [86,114,255];
    color_dict['Coral2'] = [80,106,238];
    color_dict['Coral3'] = [69,91,205];
    color_dict['Coral4'] = [47,62,139];
    color_dict['Tomato1'] = [71,99,255];
    color_dict['Tomato2'] = [66,92,238];
    color_dict['Tomato3'] = [57,79,205];
    color_dict['Tomato4'] = [38,54,139];
    color_dict['OrangeRed1'] = [0,69,255];
    color_dict['OrangeRed2'] = [0,64,238];
    color_dict['OrangeRed3'] = [0,55,205];
    color_dict['OrangeRed4'] = [0,37,139];
    color_dict['Red2'] = [0,0,238];
    color_dict['Red3'] = [0,0,205];
    color_dict['Red4'] = [0,0,139];
    color_dict['DeepPink1'] = [147,20,255];
    color_dict['DeepPink2'] = [137,18,238];
    color_dict['DeepPink3'] = [118,16,205];
    color_dict['DeepPink4'] = [80,10,139];
    color_dict['HotPink1'] = [180,110,255];
    color_dict['HotPink2'] = [167,106,238];
    color_dict['HotPink3'] = [144,96,205];
    color_dict['HotPink4'] = [98,58,139];
    color_dict['SlateBlue1'] = [255,111,131];
    color_dict['SlateBlue2'] = [238,103,122];
    color_dict['SlateBlue3'] = [205,89,105];
    color_dict['SlateBlue4'] = [139,60,71];
    color_dict['RoyalBlue1'] = [255,118,72];
    color_dict['RoyalBlue2'] = [238,110,67];
    color_dict['RoyalBlue3'] = [205,95,58];
    color_dict['RoyalBlue4'] = [139,64,39];
    color_dict['Blue2'] = [0,0,238];
    color_dict['Blue3'] = [0,0,205];
    color_dict['Blue4'] = [0,0,139];
    color_dict['DodgerBlue1'] = [255,144,30];
    color_dict['DodgerBlue2'] = [238,134,28];
    color_dict['DodgerBlue3'] = [205,116,24];
    color_dict['DodgerBlue4'] = [139,78,16];
    color_dict['SteelBlue1'] = [255,184,99];
    color_dict['SteelBlue2'] = [238,172,92];
    color_dict['SteelBlue3'] = [205,148,79];
    color_dict['SteelBlue4'] = [139,100,54];
    color_dict['DeepSkyBlue1'] = [255,191,0];
    color_dict['DeepSkyBlue2'] = [238,178,0];
    color_dict['DeepSkyBlue3'] = [205,154,0];
    color_dict['DeepSkyBlue4'] = [139,104,0];
    color_dict['SkyBlue1'] = [255,206,135];
    color_dict['SkyBlue2'] = [238,192,126];
    color_dict['SkyBlue3'] = [205,166,108];
    color_dict['SkyBlue4'] = [139,112,74];
    color_dict['LightSkyBlue1'] = [255,226,176];
    color_dict['LightSkyBlue2'] = [238,211,164];
    color_dict['LightSkyBlue3'] = [205,182,141];
    color_dict['LightSkyBlue4'] = [139,123,96];
    color_dict['SlateGray1'] = [255,226,198];
    color_dict['SlateGray2'] = [238,211,185];
    color_dict['SlateGray3'] = [205,182,159];
    color_dict['SlateGray4'] = [139,123,108];
    color_dict['LightSteelBlue1'] = [255,225,202];
    color_dict['LightSteelBlue2'] = [238,210,188];
    color_dict['LightSteelBlue3'] = [205,181,162];
    color_dict['LightSteelBlue4'] = [139,123,110];
    color_dict['LightBlue1'] = [255,239,191];
    color_dict['LightBlue2'] = [238,223,178];
    color_dict['LightBlue3'] = [205,192,154];
    color_dict['LightBlue4'] = [139,131,104];
    color_dict['LightCyan1'] = [255,255,224];
    color_dict['LightCyan2'] = [238,238,209];
    color_dict['LightCyan3'] = [205,205,180];
    color_dict['LightCyan4'] = [139,139,122];
    color_dict['Pink1'] = [197,181,255];
    color_dict['Pink2'] = [184,169,238];
    color_dict['Pink3'] = [158,145,205];
    color_dict['Pink4'] = [108,99,139];
    color_dict['LightPink1'] = [185,174,255];
    color_dict['LightPink2'] = [173,162,238];
    color_dict['LightPink3'] = [149,140,205];
    color_dict['LightPink4'] = [101,95,139];
    color_dict['PaleVioletRed1'] = [171,130,255];
    color_dict['PaleVioletRed2'] = [159,121,238];
    color_dict['PaleVioletRed3'] = [137,104,205];
    color_dict['PaleVioletRed4'] = [93,71,139];
    color_dict['Maroon1'] = [179,52,255];
    color_dict['Maroon2'] = [167,48,238];
    color_dict['Maroon3'] = [144,41,205];
    color_dict['Maroon4'] = [98,28,139];
    color_dict['VioletRed1'] = [150,62,255];
    color_dict['VioletRed2'] = [140,58,238];
    color_dict['VioletRed3'] = [120,50,205];
    color_dict['VioletRed4'] = [82,34,139];
    color_dict['Magenta2'] = [238,0,238];
    color_dict['Magenta3'] = [205,0,205];
    color_dict['Magenta4'] = [139,0,139];
    color_dict['Orchid1'] = [250,131,255];
    color_dict['Orchid2'] = [233,122,238];
    color_dict['Orchid3'] = [201,105,205];
    color_dict['Orchid4'] = [137,71,139];
    color_dict['Plum1'] = [255,187,255];
    color_dict['Plum2'] = [238,174,238];
    color_dict['Plum3'] = [205,150,205];
    color_dict['Plum4'] = [139,102,139];
    color_dict['MediumOrchid1'] = [255,102,224];
    color_dict['MediumOrchid2'] = [238,95,209];
    color_dict['MediumOrchid3'] = [205,82,180];
    color_dict['MediumOrchid4'] = [139,55,122];
    color_dict['DarkOrchid1'] = [255,62,191];
    color_dict['DarkOrchid2'] = [238,58,178];
    color_dict['DarkOrchid3'] = [205,50,154];
    color_dict['DarkOrchid4'] = [139,34,104];
    color_dict['Purple1'] = [255,48,155];
    color_dict['Purple2'] = [238,44,145];
    color_dict['Purple3'] = [205,38,125];
    color_dict['Purple4'] = [139,26,85];
    color_dict['MediumPurple1'] = [255,225,255];
    color_dict['MediumPurple2'] = [238,210,238];
    color_dict['MediumPurple3'] = [205,181,205];
    color_dict['MediumPurple4'] = [139,123,139];
    color_dict['Thistle1'] = [255,225,255];
    color_dict['Thistle2'] = [238,210,238];
    color_dict['Thistle3'] = [205,181,205];
    color_dict['Thistle4'] = [139,123,139];
    color_dict['Khaki1'] = [143,246,255];
    color_dict['Khaki2'] = [133,230,238];
    color_dict['Khaki3'] = [115,198,205];
    color_dict['Khaki4'] = [78,134,139];
    color_dict['LightGoldenrod1'] = [139,236,255];
    color_dict['LightGoldenrod2'] = [130,220,238];
    color_dict['LightGoldenrod3'] = [112,190,205];
    color_dict['LightGoldenrod4'] = [76,129,139];
    color_dict['LightYellow1'] = [224,255,255];
    color_dict['LightYellow2'] = [209,238,238];
    color_dict['LightYellow3'] = [180,205,205];
    color_dict['LightYellow4'] = [122,139,139];
    color_dict['Yellow2'] = [0,238,238];
    color_dict['Yellow3'] = [0,205,205];
    color_dict['Yellow4'] = [0,139,139];
    color_dict['Gold2'] = [0,201,238];
    color_dict['Gold3'] = [0,173,205];
    color_dict['Gold4'] = [0,117,139];
    color_dict['Goldenrod1'] = [37,193,255];
    color_dict['Goldenrod2'] = [34,180,238];
    color_dict['Goldenrod3'] = [29,155,205];
    color_dict['Goldenrod4'] = [20,105,139];
    color_dict['DarkGoldenrod1'] = [15,185,255];
    color_dict['DarkGoldenrod2'] = [14,173,238];
    color_dict['DarkGoldenrod3'] = [12,149,205];
    color_dict['DarkGoldenrod4'] = [8,101,139];
    color_dict['PaleTurquoise1'] = [255,255,187];	
    color_dict['PaleTurquoise2'] = [238,238,174];	
    color_dict['PaleTurquoise3'] = [205,205,150];	
    color_dict['PaleTurquoise4'] = [139,139,102];	
    color_dict['CadetBlue1'] = [225,245,152];	
    color_dict['CadetBlue2'] = [238,229,142	];
    color_dict['CadetBlue3'] = [205,197,122	];
    color_dict['CadetBlue4'] = [139,134,83];
    color_dict['Turquoise1'] = [255,245,0];
    color_dict['Turquoise2'] = [238,229,0];
    color_dict['Turquoise3'] = [205,197,0];	
    color_dict['Turquoise4'] = [139,134,0];
    color_dict['Cyan2'] = [238,238,0];
    color_dict['Cyan3'] = [205,205,0];
    color_dict['Cyan4'] = [139,139,0];
    color_dict['DarkSlateGray1'] = [255,255,151];
    color_dict['DarkSlateGray2'] = [238,238,141];
    color_dict['DarkSlateGray3'] = [205,205,121];
    color_dict['DarkSlateGray4'] = [139,139,82];
    color_dict['Aquamarine1'] = [212,255,127];
    color_dict['Aquamarine2'] = [198,238,118];
    color_dict['Aquamarine3'] = [170,205,102];
    color_dict['Aquamarine4'] = [116,139,69];
    color_dict['DarkSeaGreen1'] = [193,255,193];	
    color_dict['DarkSeaGreen2'] = [180,238,180];	
    color_dict['DarkSeaGreen3'] = [155,205,155];	
    color_dict['DarkSeaGreen4'] = [105,139,105];	
    color_dict['SeaGreen1'] = [159,255,84];
    color_dict['SeaGreen2'] = [148,238,78];	
    color_dict['SeaGreen3'] = [128,205,67];	
    color_dict['SeaGreen4'] = [87,139,46];
    color_dict['PaleGreen1'] = [154,255,154];
    color_dict['PaleGreen2'] = [144,238,144];
    color_dict['PaleGreen3'] = [124,205,124];
    color_dict['PaleGreen4'] = [84,139,84];
    color_dict['SpringGreen1'] = [127,255,0];
    color_dict['SpringGreen2'] = [118,238,0];
    color_dict['SpringGreen3'] = [	102,205,0];
    color_dict['SpringGreen4'] = [	69,139,0];
    color_dict['Green2'] = [0,238,0];
    color_dict['Green3'] = [0,205,0];
    color_dict['Green4'] = [0,139,0];
    color_dict['Chartreuse1'] = [0,255,127];
    color_dict['Chartreuse2'] = [0,238,118];
    color_dict['Chartreuse3'] = [0,205,102];
    color_dict['Chartreuse4'] = [0,139,69];	
    color_dict['OliveDrab1'] = [62,255,192];
    color_dict['OliveDrab2'] = [58,238,179];
    color_dict['OliveDrab3'] = [50,205,154];
    color_dict['OliveDrab4'] = [34,139,105];
    color_dict['DarkOliveGreen1'] = [112,255,202];
    color_dict['DarkOliveGreen2'] = [104,238,188];
    color_dict['DarkOliveGreen3'] = [90,205,162];
    color_dict['DarkOliveGreen4'] = [61,139,110];
    
    #print("number of dict : ",len(color_dict));

def findMarker(image) :
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
    blur = cv2.GaussianBlur(gray, (5,5), 0);
    #cv2.imshow("blur", blur);
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2);
    #cv2.imshow("thresh", thresh);
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE);
    #print(len(contours));
    #cv2.drawContours(image, contours, -1, (0,0,255), 2);
    cnt_max = max(contours, key = cv2.contourArea);
    
    return(cnt_max);

def find_color_name(color_dict, B, G, R, error_range) :
    
    nearestB = [];
    nearestG = [];
    nearestR = [];
    
    for i in color_dict.values() :
        
        if(abs(B - i[0]) < error_range and abs(G - i[1]) < error_range and abs(R - i[2]) < error_range):
            
            nearestB.append(i[0]);
            nearestG.append(i[1]);
            nearestR.append(i[2]);
    
    length = len(nearestB);
    
    if(length == 0) :
        
        return('none');
    
    min_error = 255 + 2 * error_range;
    
    for i in range (0,length) :
        
        cur_error = abs(nearestB[i] - B) + abs(nearestG[i] - G) + abs(nearestR[i] - R);
        
        if(min_error > cur_error) :
            
            min_error = cur_error;
            index_min = i;
    
    ans = [nearestB[index_min], nearestG[index_min], nearestR[index_min]];
    color_name = list(color_dict.keys())[list(color_dict.values()).index(ans)];
    
    return(color_name);

def putText(image, text, x, y, BGR) :
    
    cv2.putText(image, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, BGR, 1, cv2.LINE_AA);
    
    return(0);

def InitCanvas(width, height, BGR) :
    
    B = BGR[0];
    G = BGR[1];
    R = BGR[2];
    canvas = np.ones((height, width, 3), dtype="uint8");
    canvas[:] = (B, G, R);
    
    return canvas

def main() :
    
    print("按 g 會擷取當下畫面並顯示最大輪廓中心點的顏色,按任意鍵可退出並重新擷取畫面");
    print("按 c 會出現 frame2,滑鼠左鍵點兩下可得知該位置的顏色,按任意鍵可退出並重新擷取畫面");
    print("按 q 終止程式,再按任意鍵可關閉 frame");
    
    error = 40; # pixel
    Canvas_x = 500;
    Canvas_y = 300;
    
    
    color_dict = {};
    allocate_color_dict(color_dict);
    
    cap = cv2.VideoCapture(0);
    ret,frame = cap.read();
    
    while(ret == 1) :
        
        cv2.imshow("frame",frame);
        
        if(cv2.waitKey(100) & 0xFF == ord("g")) :
            
            cnt_max = findMarker(frame);
            
            rect= cv2.minAreaRect(cnt_max);
            #box = np.int0(cv2.boxPoints(rect));
            #cv2.drawContours(frame, [box], 0, (0,0,255), 2);
            #print(img.shape[0], img.shape[1]); # y,x
            xc = int(rect[0][0]);
            yc = int(rect[0][1]);
            B = frame[yc, xc, 0];
            G = frame[yc, xc, 1];
            R = frame[yc, xc, 2];
            
            color_name = find_color_name(color_dict, B, G, R, error);
            
            if(color_name == 'none') :
                
                color_dict[color_name] = [int(B), int(G), int(R)];
            
            print("{} {}\n".format(color_name, color_dict[color_name]));
            cv2.circle(frame, (xc,yc), 10, [0,0,255], 2);
            text = str(color_name) + str(color_dict[color_name]);
            putText(frame, text, int(xc-150), int(yc-20), [0,0,255]);
            
            Canvas = InitCanvas(Canvas_x, Canvas_y, color_dict[color_name]);
            cv2.rectangle(Canvas, (0,0), (Canvas_x,60), (0,0,0), -1);
            #textC = str('MediumAquamarine') + " " +  str([170,205,102]);
            textC = str(color_name) + " " +  str(color_dict[color_name]);
            cv2.putText(Canvas, textC, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, [255,255,255], 2, cv2.LINE_AA);
            cv2.imshow("Canvas", Canvas);
            
            cv2.imshow("frame",frame);
            cv2.waitKey(0);
            cv2.destroyAllWindows();
        
        if(cv2.waitKey(100) & 0xFF == ord("c")) :
            
            cv2.namedWindow("frame2");
            frame2 = frame.copy();
            
            def points(event, x, y, flags, param) :
                
                if event == cv2.EVENT_LBUTTONDBLCLK :
                    
                    #print("(x,y) = ", (x,y),"(B,G,R) = ",frame2[int(y), int(x), :]);
                    B2 = frame2[int(y), int(x), 0];
                    G2 = frame2[int(y), int(x), 1];
                    R2 = frame2[int(y), int(x), 2];
                    
                    color_name = find_color_name(color_dict, B2, G2, R2, error);
                    
                    if(color_name == 'none') :
                        
                        color_dict[color_name] = [int(B2), int(G2), int(R2)];
                    
                    print("{} {}\n".format(color_name, color_dict[color_name]));
                    cv2.circle(frame, (int(x),int(y)), 10, [0,0,255], 2);
                    text = str(color_name) + str(color_dict[color_name]);
                    putText(frame, text, int(x-150), int(y-20), [0,0,255]);
                    cv2.imshow('frame',frame);
                    
                    Canvas = InitCanvas(Canvas_x, Canvas_y, color_dict[color_name]);
                    cv2.rectangle(Canvas, (0,0), (Canvas_x,60), (0,0,0), -1);
                    textC = str(color_name) + " " +  str(color_dict[color_name]);
                    cv2.putText(Canvas, textC, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, [255,255,255], 2, cv2.LINE_AA);
                    cv2.imshow("Canvas", Canvas);
                    
            cv2.setMouseCallback("frame2", points);
            cv2.imshow("frame2",frame2);
            cv2.waitKey(0);
            cv2.destroyAllWindows(); 
            
        if(cv2.waitKey(100) & 0xFF == ord("q")) :
            
            break;
        
        ret,frame = cap.read();
        
    
    cap.release();
    cv2.waitKey(0);
    cv2.destroyAllWindows(); 
    
main();
    
    
    
    
    
    
    
    
    
    
    