#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
XML char version 1.0

Copyright (C)2008 Petr Nohejl, jestrab.net

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

This program comes with ABSOLUTELY NO WARRANTY!
"""

### IMPORT #####################################################################

import sys		# argv
import string	# prace s retezci
import re		# regularni vyrazy



### ERRORS A HELP ##############################################################

def ErrorArg():
	print "Error: Incorrect arguments!\nTo show help, run program with parameter -h."
	return
	
def ErrorFile(filename):
	print "Error: Cannot open file " + filename + "!"
	return

def Help():
	print "XML char version 1.0"
	print ""
	print "Copyright (c)2008 Petr Nohejl, jestrab.net"
	print ""
	print "Program convert special XML chars to standard ASCII chars and remove diacritic."
	print "For example: '&#65;' -> 'A'. Unknown chars are replaced by '#'"
	print ""
	print "Usage: xmlchar filename"
	print "       xmlchar -h"
	return
	
	
	
### XMLCHAR ####################################################################

# zruseni diakritiky v xml
def XmlChar(filename):
	try:
		file = open(filename, "r")	# xml soubror
	except:
		ErrorFile(filename)
		return False
	output = ""						# vystup
	
	# cteni souboru
	while 1:
		line = file.readline()
		if(line == ""):
			break
	
	
		#line = string.replace(line,"&amp;","&")
		#line = string.replace(line,"&nbsp;"," ")
		#line = string.replace(line,"&lt;","<")
		#line = string.replace(line,"&gt;",">")
		#line = string.replace(line,"<br>","<br />")


		line = string.replace(line,"&#33;","!") # 33: ! 
		line = string.replace(line,"&#34;",'"') # 34: " 
		line = string.replace(line,"&#35;","#") # 35: # 
		line = string.replace(line,"&#36;","$") # 36: $ 
		line = string.replace(line,"&#37;","%") # 37: % 
		line = string.replace(line,"&#38;","&") # 38: & 
		line = string.replace(line,"&#39;","'") # 39: ' 
		line = string.replace(line,"&#40;","(") # 40: ( 
		line = string.replace(line,"&#41;",")") # 41: ) 
		line = string.replace(line,"&#42;","*") # 42: * 
		line = string.replace(line,"&#43;","+") # 43: + 
		line = string.replace(line,"&#44;",",") # 44: , 
		line = string.replace(line,"&#45;","-") # 45: - 
		line = string.replace(line,"&#46;",".") # 46: . 
		line = string.replace(line,"&#47;","/") # 47: / 
		line = string.replace(line,"&#48;","0") # 48: 0 
		line = string.replace(line,"&#49;","1") # 49: 1 
		line = string.replace(line,"&#50;","2") # 50: 2 
		line = string.replace(line,"&#51;","3") # 51: 3 
		line = string.replace(line,"&#52;","4") # 52: 4 
		line = string.replace(line,"&#53;","5") # 53: 5 
		line = string.replace(line,"&#54;","6") # 54: 6 
		line = string.replace(line,"&#55;","7") # 55: 7 
		line = string.replace(line,"&#56;","8") # 56: 8 
		line = string.replace(line,"&#57;","9") # 57: 9 
		line = string.replace(line,"&#58;",":") # 58: : 
		line = string.replace(line,"&#59;",";") # 59: ; 
		line = string.replace(line,"&#60;","<") # 60: < 
		line = string.replace(line,"&#61;","=") # 61: = 
		line = string.replace(line,"&#62;",">") # 62: > 
		line = string.replace(line,"&#63;","?") # 63: ? 
		line = string.replace(line,"&#64;","@") # 64: @ 
		line = string.replace(line,"&#65;","A") # 65: A 
		line = string.replace(line,"&#66;","B") # 66: B 
		line = string.replace(line,"&#67;","C") # 67: C 
		line = string.replace(line,"&#68;","D") # 68: D 
		line = string.replace(line,"&#69;","E") # 69: E 
		line = string.replace(line,"&#70;","F") # 70: F 
		line = string.replace(line,"&#71;","G") # 71: G 
		line = string.replace(line,"&#72;","H") # 72: H 
		line = string.replace(line,"&#73;","I") # 73: I 
		line = string.replace(line,"&#74;","J") # 74: J 
		line = string.replace(line,"&#75;","K") # 75: K 
		line = string.replace(line,"&#76;","L") # 76: L 
		line = string.replace(line,"&#77;","M") # 77: M 
		line = string.replace(line,"&#78;","N") # 78: N 
		line = string.replace(line,"&#79;","O") # 79: O 
		line = string.replace(line,"&#80;","P") # 80: P 
		line = string.replace(line,"&#81;","Q") # 81: Q 
		line = string.replace(line,"&#82;","R") # 82: R 
		line = string.replace(line,"&#83;","S") # 83: S 
		line = string.replace(line,"&#84;","T") # 84: T 
		line = string.replace(line,"&#85;","U") # 85: U 
		line = string.replace(line,"&#86;","V") # 86: V 
		line = string.replace(line,"&#87;","W") # 87: W 
		line = string.replace(line,"&#88;","X") # 88: X 
		line = string.replace(line,"&#89;","Y") # 89: Y 
		line = string.replace(line,"&#90;","Z") # 90: Z 
		line = string.replace(line,"&#91;","[") # 91: [ 
		line = string.replace(line,"&#92;","\\") # 92: \
		line = string.replace(line,"&#93;","]") # 93: ] 
		line = string.replace(line,"&#94;","^") # 94: ^ 
		line = string.replace(line,"&#95;","_") # 95: _ 
		line = string.replace(line,"&#96;","`") # 96: ` 
		line = string.replace(line,"&#97;","a") # 97: a 
		line = string.replace(line,"&#98;","b") # 98: b 
		line = string.replace(line,"&#99;","c") # 99: c 
		line = string.replace(line,"&#100;","d") # 100: d 
		line = string.replace(line,"&#101;","e") # 101: e 
		line = string.replace(line,"&#102;","f") # 102: f 
		line = string.replace(line,"&#103;","g") # 103: g 
		line = string.replace(line,"&#104;","h") # 104: h 
		line = string.replace(line,"&#105;","i") # 105: i 
		line = string.replace(line,"&#106;","j") # 106: j 
		line = string.replace(line,"&#107;","k") # 107: k 
		line = string.replace(line,"&#108;","l") # 108: l 
		line = string.replace(line,"&#109;","m") # 109: m 
		line = string.replace(line,"&#110;","n") # 110: n 
		line = string.replace(line,"&#111;","o") # 111: o 
		line = string.replace(line,"&#112;","p") # 112: p 
		line = string.replace(line,"&#113;","q") # 113: q 
		line = string.replace(line,"&#114;","r") # 114: r 
		line = string.replace(line,"&#115;","s") # 115: s 
		line = string.replace(line,"&#116;","t") # 116: t 
		line = string.replace(line,"&#117;","u") # 117: u 
		line = string.replace(line,"&#118;","v") # 118: v 
		line = string.replace(line,"&#119;","w") # 119: w 
		line = string.replace(line,"&#120;","x") # 120: x 
		line = string.replace(line,"&#121;","y") # 121: y 
		line = string.replace(line,"&#122;","z") # 122: z 
		line = string.replace(line,"&#123;","{") # 123: { 
		line = string.replace(line,"&#124;","|") # 124: | 
		line = string.replace(line,"&#125;","}") # 125: } 
		line = string.replace(line,"&#126;","~") # 126: ~ 
	
		line = string.replace(line,"&#161;","i") # 161: ¡ 
		line = string.replace(line,"&#162;","c") # 162: ¢ 
		line = string.replace(line,"&#163;","L") # 163: £ 
		line = string.replace(line,"&#164;","o") # 164: ¤ 
		line = string.replace(line,"&#165;","Y") # 165: ¥ 
		line = string.replace(line,"&#166;",":") # 166: ¦ 
		line = string.replace(line,"&#167;","S") # 167: § 
		line = string.replace(line,"&#168;",'"') # 168: ¨ 
		line = string.replace(line,"&#169;","C") # 169: © 
		line = string.replace(line,"&#170;","a") # 170: ª 
		line = string.replace(line,"&#171;","<<") # 171: « 
		line = string.replace(line,"&#172;","!") # 172: ¬ 
		line = string.replace(line,"&#173;","-") # 173: ­ 
		line = string.replace(line,"&#174;","R") # 174: ® 
		line = string.replace(line,"&#175;","-") # 175: ¯ 
		line = string.replace(line,"&#176;","o") # 176: ° 
		line = string.replace(line,"&#177;","+-") # 177: ± 
		line = string.replace(line,"&#178;","2") # 178: ² 
		line = string.replace(line,"&#179;","3") # 179: ³ 
		line = string.replace(line,"&#180;","'") # 180: ´ 
		line = string.replace(line,"&#181;","u") # 181: µ 
		line = string.replace(line,"&#182;","P") # 182: ¶ 
		line = string.replace(line,"&#183;",".") # 183: · 
		line = string.replace(line,"&#184;",",") # 184: ¸ 
		line = string.replace(line,"&#185;","1") # 185: ¹ 
		line = string.replace(line,"&#186;","o") # 186: º 
		line = string.replace(line,"&#187;",">>") # 187: » 
		line = string.replace(line,"&#188;","1/4") # 188: ¼ 
		line = string.replace(line,"&#189;","1/2") # 189: ½ 
		line = string.replace(line,"&#190;","3/4") # 190: ¾ 
		line = string.replace(line,"&#191;","?") # 191: ¿ 
		line = string.replace(line,"&#192;","A") # 192: À 
		line = string.replace(line,"&#193;","A") # 193: Á 
		line = string.replace(line,"&#194;","A") # 194: Â 
		line = string.replace(line,"&#195;","A") # 195: Ã 
		line = string.replace(line,"&#196;","A") # 196: Ä 
		line = string.replace(line,"&#197;","A") # 197: Å 
		line = string.replace(line,"&#198;","AE") # 198: Æ 
		line = string.replace(line,"&#199;","C") # 199: Ç 
		line = string.replace(line,"&#200;","E") # 200: È 
		line = string.replace(line,"&#201;","E") # 201: É 
		line = string.replace(line,"&#202;","E") # 202: Ê 
		line = string.replace(line,"&#203;","E") # 203: Ë 
		line = string.replace(line,"&#204;","I") # 204: Ì 
		line = string.replace(line,"&#205;","I") # 205: Í 
		line = string.replace(line,"&#206;","I") # 206: Î 
		line = string.replace(line,"&#207;","I") # 207: Ï 
		line = string.replace(line,"&#208;","D") # 208: Ð 
		line = string.replace(line,"&#209;","N") # 209: Ñ 
		line = string.replace(line,"&#210;","O") # 210: Ò 
		line = string.replace(line,"&#211;","O") # 211: Ó 
		line = string.replace(line,"&#212;","O") # 212: Ô 
		line = string.replace(line,"&#213;","O") # 213: Õ 
		line = string.replace(line,"&#214;","O") # 214: Ö 
		line = string.replace(line,"&#215;","x") # 215: × 
		line = string.replace(line,"&#216;","r") # 216: Ø 
		line = string.replace(line,"&#217;","U") # 217: Ù 
		line = string.replace(line,"&#218;","U") # 218: Ú 
		line = string.replace(line,"&#219;","U") # 219: Û 
		line = string.replace(line,"&#220;","U") # 220: Ü 
		line = string.replace(line,"&#221;","Y") # 221: Ý 
		line = string.replace(line,"&#222;","s") # 222: Þ 
		line = string.replace(line,"&#223;","S") # 223: ß 
		line = string.replace(line,"&#224;","a") # 224: à 
		line = string.replace(line,"&#225;","a") # 225: á 
		line = string.replace(line,"&#226;","a") # 226: â 
		line = string.replace(line,"&#227;","a") # 227: ã 
		line = string.replace(line,"&#228;","a") # 228: ä 
		line = string.replace(line,"&#229;","a") # 229: å 
		line = string.replace(line,"&#230;","ae") # 230: æ 
		line = string.replace(line,"&#231;","c") # 231: ç 
		line = string.replace(line,"&#232;","e") # 232: è 
		line = string.replace(line,"&#233;","e") # 233: é 
		line = string.replace(line,"&#234;","e") # 234: ê 
		line = string.replace(line,"&#235;","e") # 235: ë 
		line = string.replace(line,"&#236;","i") # 236: ì 
		line = string.replace(line,"&#237;","i") # 237: í 
		line = string.replace(line,"&#238;","i") # 238: î 
		line = string.replace(line,"&#239;","i") # 239: ï 
		line = string.replace(line,"&#240;","o") # 240: ð 
		line = string.replace(line,"&#241;","n") # 241: ñ 
		line = string.replace(line,"&#242;","o") # 242: ò 
		line = string.replace(line,"&#243;","o") # 243: ó 
		line = string.replace(line,"&#244;","o") # 244: ô 
		line = string.replace(line,"&#245;","o") # 245: õ 
		line = string.replace(line,"&#246;","o") # 246: ö 
		line = string.replace(line,"&#247;","/") # 247: ÷ 
		line = string.replace(line,"&#248;","r") # 248: ø 
		line = string.replace(line,"&#249;","u") # 249: ù 
		line = string.replace(line,"&#250;","u") # 250: ú 
		line = string.replace(line,"&#251;","u") # 251: û 
		line = string.replace(line,"&#252;","u") # 252: ü 
		line = string.replace(line,"&#253;","y") # 253: ý 
		line = string.replace(line,"&#254;","y") # 254: þ 
		line = string.replace(line,"&#255;","y") # 255: ÿ 
		line = string.replace(line,"&#256;","A") # 256: Ā 
		line = string.replace(line,"&#257;","a") # 257: ā 
		line = string.replace(line,"&#258;","A") # 258: Ă 
		line = string.replace(line,"&#259;","a") # 259: ă 
		line = string.replace(line,"&#260;","A") # 260: Ą 
		line = string.replace(line,"&#261;","a") # 261: ą 
		line = string.replace(line,"&#262;","C") # 262: Ć 
		line = string.replace(line,"&#263;","c") # 263: ć 
		line = string.replace(line,"&#264;","C") # 264: Ĉ 
		line = string.replace(line,"&#265;","c") # 265: ĉ 
		line = string.replace(line,"&#266;","C") # 266: Ċ 
		line = string.replace(line,"&#267;","c") # 267: ċ 
		line = string.replace(line,"&#268;","C") # 268: Č 
		line = string.replace(line,"&#269;","c") # 269: č 
		line = string.replace(line,"&#270;","D") # 270: Ď 
		line = string.replace(line,"&#271;","d") # 271: ď 
		line = string.replace(line,"&#272;","D") # 272: Đ 
		line = string.replace(line,"&#273;","d") # 273: đ 
		line = string.replace(line,"&#274;","E") # 274: Ē 
		line = string.replace(line,"&#275;","e") # 275: ē 
		line = string.replace(line,"&#276;","E") # 276: Ĕ 
		line = string.replace(line,"&#277;","e") # 277: ĕ 
		line = string.replace(line,"&#278;","E") # 278: Ė 
		line = string.replace(line,"&#279;","e") # 279: ė 
		line = string.replace(line,"&#280;","E") # 280: Ę 
		line = string.replace(line,"&#281;","e") # 281: ę 
		line = string.replace(line,"&#282;","E") # 282: Ě 
		line = string.replace(line,"&#283;","e") # 283: ě 
		line = string.replace(line,"&#284;","G") # 284: Ĝ 
		line = string.replace(line,"&#285;","g") # 285: ĝ 
		line = string.replace(line,"&#286;","G") # 286: Ğ 
		line = string.replace(line,"&#287;","g") # 287: ğ 
		line = string.replace(line,"&#288;","G") # 288: Ġ 
		line = string.replace(line,"&#289;","g") # 289: ġ 
		line = string.replace(line,"&#290;","G") # 290: Ģ 
		line = string.replace(line,"&#291;","g") # 291: ģ 
		line = string.replace(line,"&#292;","H") # 292: Ĥ 
		line = string.replace(line,"&#293;","h") # 293: ĥ 
		line = string.replace(line,"&#294;","H") # 294: Ħ 
		line = string.replace(line,"&#295;","h") # 295: ħ 
		line = string.replace(line,"&#296;","I") # 296: Ĩ 
		line = string.replace(line,"&#297;","i") # 297: ĩ 
		line = string.replace(line,"&#298;","I") # 298: Ī 
		line = string.replace(line,"&#299;","i") # 299: ī 
		line = string.replace(line,"&#300;","I") # 300: Ĭ 
		line = string.replace(line,"&#301;","i") # 301: ĭ 
		line = string.replace(line,"&#302;","I") # 302: Į 
		line = string.replace(line,"&#303;","i") # 303: į 
		line = string.replace(line,"&#304;","I") # 304: İ 
		line = string.replace(line,"&#305;","i") # 305: ı 
		line = string.replace(line,"&#306;","IJ") # 306: Ĳ 
		line = string.replace(line,"&#307;","ij") # 307: ĳ 
		line = string.replace(line,"&#308;","J") # 308: Ĵ 
		line = string.replace(line,"&#309;","j") # 309: ĵ 
		line = string.replace(line,"&#310;","K") # 310: Ķ 
		line = string.replace(line,"&#311;","k") # 311: ķ 
		line = string.replace(line,"&#312;","k") # 312: ĸ 
		line = string.replace(line,"&#313;","L") # 313: Ĺ 
		line = string.replace(line,"&#314;","l") # 314: ĺ 
		line = string.replace(line,"&#315;","L") # 315: Ļ 
		line = string.replace(line,"&#316;","l") # 316: ļ 
		line = string.replace(line,"&#317;","L") # 317: Ľ 
		line = string.replace(line,"&#318;","l") # 318: ľ 
		line = string.replace(line,"&#319;","L") # 319: Ŀ 
		line = string.replace(line,"&#320;","l") # 320: ŀ 
		line = string.replace(line,"&#321;","L") # 321: Ł 
		line = string.replace(line,"&#322;","l") # 322: ł 
		line = string.replace(line,"&#323;","N") # 323: Ń 
		line = string.replace(line,"&#324;","n") # 324: ń 
		line = string.replace(line,"&#325;","N") # 325: Ņ 
		line = string.replace(line,"&#326;","n") # 326: ņ 
		line = string.replace(line,"&#327;","N") # 327: Ň 
		line = string.replace(line,"&#328;","n") # 328: ň 
		line = string.replace(line,"&#329;","n") # 329: ŉ 
		line = string.replace(line,"&#330;","N") # 330: Ŋ 
		line = string.replace(line,"&#331;","n") # 331: ŋ 
		line = string.replace(line,"&#332;","O") # 332: Ō 
		line = string.replace(line,"&#333;","o") # 333: ō 
		line = string.replace(line,"&#334;","O") # 334: Ŏ 
		line = string.replace(line,"&#335;","o") # 335: ŏ 
		line = string.replace(line,"&#336;","O") # 336: Ő 
		line = string.replace(line,"&#337;","o") # 337: ő 
		line = string.replace(line,"&#338;","CE") # 338: Œ 
		line = string.replace(line,"&#339;","ce") # 339: œ 
		line = string.replace(line,"&#340;","R") # 340: Ŕ 
		line = string.replace(line,"&#341;","r") # 341: ŕ 
		line = string.replace(line,"&#342;","R") # 342: Ŗ 
		line = string.replace(line,"&#343;","r") # 343: ŗ 
		line = string.replace(line,"&#344;","R") # 344: Ř 
		line = string.replace(line,"&#345;","r") # 345: ř 
		line = string.replace(line,"&#346;","S") # 346: Ś 
		line = string.replace(line,"&#347;","s") # 347: ś 
		line = string.replace(line,"&#348;","S") # 348: Ŝ 
		line = string.replace(line,"&#349;","s") # 349: ŝ 
		line = string.replace(line,"&#350;","S") # 350: Ş 
		line = string.replace(line,"&#351;","s") # 351: ş 
		line = string.replace(line,"&#352;","S") # 352: Š 
		line = string.replace(line,"&#353;","s") # 353: š 
		line = string.replace(line,"&#354;","T") # 354: Ţ 
		line = string.replace(line,"&#355;","t") # 355: ţ 
		line = string.replace(line,"&#356;","T") # 356: Ť 
		line = string.replace(line,"&#357;","t") # 357: ť 
		line = string.replace(line,"&#358;","T") # 358: Ŧ 
		line = string.replace(line,"&#359;","t") # 359: ŧ 
		line = string.replace(line,"&#360;","U") # 360: Ũ 
		line = string.replace(line,"&#361;","u") # 361: ũ 
		line = string.replace(line,"&#362;","U") # 362: Ū 
		line = string.replace(line,"&#363;","u") # 363: ū 
		line = string.replace(line,"&#364;","U") # 364: Ŭ 
		line = string.replace(line,"&#365;","u") # 365: ŭ 
		line = string.replace(line,"&#366;","U") # 366: Ů 
		line = string.replace(line,"&#367;","u") # 367: ů 
		line = string.replace(line,"&#368;","U") # 368: Ű 
		line = string.replace(line,"&#369;","u") # 369: ű 
		line = string.replace(line,"&#370;","U") # 370: Ų 
		line = string.replace(line,"&#371;","u") # 371: ų 
		line = string.replace(line,"&#372;","W") # 372: Ŵ 
		line = string.replace(line,"&#373;","w") # 373: ŵ 
		line = string.replace(line,"&#374;","Y") # 374: Ŷ 
		line = string.replace(line,"&#375;","y") # 375: ŷ 
		line = string.replace(line,"&#376;","Y") # 376: Ÿ 
		line = string.replace(line,"&#377;","Z") # 377: Ź 
		line = string.replace(line,"&#378;","z") # 378: ź 
		line = string.replace(line,"&#379;","Z") # 379: Ż 
		line = string.replace(line,"&#380;","z") # 380: ż 
		line = string.replace(line,"&#381;","Z") # 381: Ž 
		line = string.replace(line,"&#382;","z") # 382: ž 
		line = string.replace(line,"&#383;","i") # 383: ſ 
	
		line = string.replace(line,"&#399;","E") # 399: Ə 
	
		line = string.replace(line,"&#402;","f") # 402: ƒ 
	
		line = string.replace(line,"&#416;","O") # 416: Ơ 
		line = string.replace(line,"&#417;","o") # 417: ơ 
	
		line = string.replace(line,"&#431;","U") # 431: Ư 
		line = string.replace(line,"&#432;","u") # 432: ư 
	
		line = string.replace(line,"&#461;","A") # 461: Ǎ 
		line = string.replace(line,"&#462;","a") # 462: ǎ 
		line = string.replace(line,"&#463;","I") # 463: Ǐ 
		line = string.replace(line,"&#464;","i") # 464: ǐ 
		line = string.replace(line,"&#465;","O") # 465: Ǒ 
		line = string.replace(line,"&#466;","o") # 466: ǒ 
		line = string.replace(line,"&#467;","U") # 467: Ǔ 
		line = string.replace(line,"&#468;","u") # 468: ǔ 
		line = string.replace(line,"&#469;","U") # 469: Ǖ 
		line = string.replace(line,"&#470;","u") # 470: ǖ 
		line = string.replace(line,"&#471;","U") # 471: Ǘ 
		line = string.replace(line,"&#472;","u") # 472: ǘ 
		line = string.replace(line,"&#473;","U") # 473: Ǚ 
		line = string.replace(line,"&#474;","u") # 474: ǚ 
		line = string.replace(line,"&#475;","U") # 475: Ǜ 
		line = string.replace(line,"&#476;","u") # 476: ǜ 
	
		line = string.replace(line,"&#506;","A") # 506: Ǻ 
		line = string.replace(line,"&#507;","a") # 507: ǻ 
		line = string.replace(line,"&#508;","AE") # 508: Ǽ 
		line = string.replace(line,"&#509;","ae") # 509: ǽ 
		line = string.replace(line,"&#510;","O") # 510: Ǿ 
		line = string.replace(line,"&#511;","o") # 511: ǿ 
	
		line = string.replace(line,"&#601;","e") # 601: ə 
	
		line = string.replace(line,"&#710;","'") # 710: ˆ 
		line = string.replace(line,"&#711;","'") # 711: ˇ 
	
		line = string.replace(line,"&#713;","-") # 713: ˉ 
	
		line = string.replace(line,"&#728;","'") # 728: ˘ 
		line = string.replace(line,"&#729;","'") # 729: ˙ 
		line = string.replace(line,"&#730;","'") # 730: ˚ 
		line = string.replace(line,"&#731;",".") # 731: ˛ 
		line = string.replace(line,"&#732;","'") # 732: ˜ 
		line = string.replace(line,"&#733;","'") # 733: ˝ 
	
		line = string.replace(line,"&#768;","'") # 768: ̀ 
		line = string.replace(line,"&#769;","'") # 769: ́ 
	
		line = string.replace(line,"&#771;","'") # 771: ̃ 
		
		line = string.replace(line,"&#777;","'") # 777: ̉ 
		
		line = string.replace(line,"&#803;",".") # 803: ̣ 
		
		line = string.replace(line,"&#894;",";") # 894: ; 
		
		line = string.replace(line,"&#900;","'") # 900: ΄ 
		line = string.replace(line,"&#901;","'") # 901: ΅ 
		line = string.replace(line,"&#902;","A") # 902: Ά 
		line = string.replace(line,"&#903;",".") # 903: · 
		line = string.replace(line,"&#904;","E") # 904: Έ 
		line = string.replace(line,"&#905;","H") # 905: Ή 
		line = string.replace(line,"&#906;","I") # 906: Ί 
		
		line = string.replace(line,"&#908;","O") # 908: Ό 
		
		

		line = string.replace(line,"&amp;#33;","!") # 33: ! 
		line = string.replace(line,"&amp;#34;",'"') # 34: " 
		line = string.replace(line,"&amp;#35;","#") # 35: # 
		line = string.replace(line,"&amp;#36;","$") # 36: $ 
		line = string.replace(line,"&amp;#37;","%") # 37: % 
		line = string.replace(line,"&amp;#38;","&") # 38: &
		line = string.replace(line,"&amp;#39;","'") # 39: ' 
		line = string.replace(line,"&amp;#40;","(") # 40: ( 
		line = string.replace(line,"&amp;#41;",")") # 41: ) 
		line = string.replace(line,"&amp;#42;","*") # 42: * 
		line = string.replace(line,"&amp;#43;","+") # 43: + 
		line = string.replace(line,"&amp;#44;",",") # 44: , 
		line = string.replace(line,"&amp;#45;","-") # 45: - 
		line = string.replace(line,"&amp;#46;",".") # 46: . 
		line = string.replace(line,"&amp;#47;","/") # 47: / 
		line = string.replace(line,"&amp;#48;","0") # 48: 0 
		line = string.replace(line,"&amp;#49;","1") # 49: 1 
		line = string.replace(line,"&amp;#50;","2") # 50: 2 
		line = string.replace(line,"&amp;#51;","3") # 51: 3 
		line = string.replace(line,"&amp;#52;","4") # 52: 4 
		line = string.replace(line,"&amp;#53;","5") # 53: 5 
		line = string.replace(line,"&amp;#54;","6") # 54: 6 
		line = string.replace(line,"&amp;#55;","7") # 55: 7 
		line = string.replace(line,"&amp;#56;","8") # 56: 8 
		line = string.replace(line,"&amp;#57;","9") # 57: 9 
		line = string.replace(line,"&amp;#58;",":") # 58: : 
		line = string.replace(line,"&amp;#59;",";") # 59: ; 
		line = string.replace(line,"&amp;#60;","<") # 60: < 
		line = string.replace(line,"&amp;#61;","=") # 61: = 
		line = string.replace(line,"&amp;#62;",">") # 62: > 
		line = string.replace(line,"&amp;#63;","?") # 63: ? 
		line = string.replace(line,"&amp;#64;","@") # 64: @ 
		line = string.replace(line,"&amp;#65;","A") # 65: A 
		line = string.replace(line,"&amp;#66;","B") # 66: B 
		line = string.replace(line,"&amp;#67;","C") # 67: C 
		line = string.replace(line,"&amp;#68;","D") # 68: D 
		line = string.replace(line,"&amp;#69;","E") # 69: E 
		line = string.replace(line,"&amp;#70;","F") # 70: F 
		line = string.replace(line,"&amp;#71;","G") # 71: G 
		line = string.replace(line,"&amp;#72;","H") # 72: H 
		line = string.replace(line,"&amp;#73;","I") # 73: I 
		line = string.replace(line,"&amp;#74;","J") # 74: J 
		line = string.replace(line,"&amp;#75;","K") # 75: K 
		line = string.replace(line,"&amp;#76;","L") # 76: L 
		line = string.replace(line,"&amp;#77;","M") # 77: M 
		line = string.replace(line,"&amp;#78;","N") # 78: N 
		line = string.replace(line,"&amp;#79;","O") # 79: O 
		line = string.replace(line,"&amp;#80;","P") # 80: P 
		line = string.replace(line,"&amp;#81;","Q") # 81: Q 
		line = string.replace(line,"&amp;#82;","R") # 82: R 
		line = string.replace(line,"&amp;#83;","S") # 83: S 
		line = string.replace(line,"&amp;#84;","T") # 84: T 
		line = string.replace(line,"&amp;#85;","U") # 85: U 
		line = string.replace(line,"&amp;#86;","V") # 86: V 
		line = string.replace(line,"&amp;#87;","W") # 87: W 
		line = string.replace(line,"&amp;#88;","X") # 88: X 
		line = string.replace(line,"&amp;#89;","Y") # 89: Y 
		line = string.replace(line,"&amp;#90;","Z") # 90: Z 
		line = string.replace(line,"&amp;#91;","[") # 91: [ 
		line = string.replace(line,"&amp;#92;","\\") # 92: \
		line = string.replace(line,"&amp;#93;","]") # 93: ] 
		line = string.replace(line,"&amp;#94;","^") # 94: ^ 
		line = string.replace(line,"&amp;#95;","_") # 95: _ 
		line = string.replace(line,"&amp;#96;","`") # 96: ` 
		line = string.replace(line,"&amp;#97;","a") # 97: a 
		line = string.replace(line,"&amp;#98;","b") # 98: b 
		line = string.replace(line,"&amp;#99;","c") # 99: c 
		line = string.replace(line,"&amp;#100;","d") # 100: d 
		line = string.replace(line,"&amp;#101;","e") # 101: e 
		line = string.replace(line,"&amp;#102;","f") # 102: f 
		line = string.replace(line,"&amp;#103;","g") # 103: g 
		line = string.replace(line,"&amp;#104;","h") # 104: h 
		line = string.replace(line,"&amp;#105;","i") # 105: i 
		line = string.replace(line,"&amp;#106;","j") # 106: j 
		line = string.replace(line,"&amp;#107;","k") # 107: k 
		line = string.replace(line,"&amp;#108;","l") # 108: l 
		line = string.replace(line,"&amp;#109;","m") # 109: m 
		line = string.replace(line,"&amp;#110;","n") # 110: n 
		line = string.replace(line,"&amp;#111;","o") # 111: o 
		line = string.replace(line,"&amp;#112;","p") # 112: p 
		line = string.replace(line,"&amp;#113;","q") # 113: q 
		line = string.replace(line,"&amp;#114;","r") # 114: r 
		line = string.replace(line,"&amp;#115;","s") # 115: s 
		line = string.replace(line,"&amp;#116;","t") # 116: t 
		line = string.replace(line,"&amp;#117;","u") # 117: u 
		line = string.replace(line,"&amp;#118;","v") # 118: v 
		line = string.replace(line,"&amp;#119;","w") # 119: w 
		line = string.replace(line,"&amp;#120;","x") # 120: x 
		line = string.replace(line,"&amp;#121;","y") # 121: y 
		line = string.replace(line,"&amp;#122;","z") # 122: z 
		line = string.replace(line,"&amp;#123;","{") # 123: { 
		line = string.replace(line,"&amp;#124;","|") # 124: | 
		line = string.replace(line,"&amp;#125;","}") # 125: } 
		line = string.replace(line,"&amp;#126;","~") # 126: ~ 
	
		line = string.replace(line,"&amp;#161;","i") # 161: ¡ 
		line = string.replace(line,"&amp;#162;","c") # 162: ¢ 
		line = string.replace(line,"&amp;#163;","L") # 163: £ 
		line = string.replace(line,"&amp;#164;","o") # 164: ¤ 
		line = string.replace(line,"&amp;#165;","Y") # 165: ¥ 
		line = string.replace(line,"&amp;#166;",":") # 166: ¦ 
		line = string.replace(line,"&amp;#167;","S") # 167: § 
		line = string.replace(line,"&amp;#168;",'"') # 168: ¨ 
		line = string.replace(line,"&amp;#169;","C") # 169: © 
		line = string.replace(line,"&amp;#170;","a") # 170: ª 
		line = string.replace(line,"&amp;#171;","<<") # 171: « 
		line = string.replace(line,"&amp;#172;","!") # 172: ¬ 
		line = string.replace(line,"&amp;#173;","-") # 173: ­ 
		line = string.replace(line,"&amp;#174;","R") # 174: ® 
		line = string.replace(line,"&amp;#175;","-") # 175: ¯ 
		line = string.replace(line,"&amp;#176;","o") # 176: ° 
		line = string.replace(line,"&amp;#177;","+-") # 177: ± 
		line = string.replace(line,"&amp;#178;","2") # 178: ² 
		line = string.replace(line,"&amp;#179;","3") # 179: ³ 
		line = string.replace(line,"&amp;#180;","'") # 180: ´ 
		line = string.replace(line,"&amp;#181;","u") # 181: µ 
		line = string.replace(line,"&amp;#182;","P") # 182: ¶ 
		line = string.replace(line,"&amp;#183;",".") # 183: · 
		line = string.replace(line,"&amp;#184;",",") # 184: ¸ 
		line = string.replace(line,"&amp;#185;","1") # 185: ¹ 
		line = string.replace(line,"&amp;#186;","o") # 186: º 
		line = string.replace(line,"&amp;#187;",">>") # 187: » 
		line = string.replace(line,"&amp;#188;","1/4") # 188: ¼ 
		line = string.replace(line,"&amp;#189;","1/2") # 189: ½ 
		line = string.replace(line,"&amp;#190;","3/4") # 190: ¾ 
		line = string.replace(line,"&amp;#191;","?") # 191: ¿ 
		line = string.replace(line,"&amp;#192;","A") # 192: À 
		line = string.replace(line,"&amp;#193;","A") # 193: Á 
		line = string.replace(line,"&amp;#194;","A") # 194: Â 
		line = string.replace(line,"&amp;#195;","A") # 195: Ã 
		line = string.replace(line,"&amp;#196;","A") # 196: Ä 
		line = string.replace(line,"&amp;#197;","A") # 197: Å 
		line = string.replace(line,"&amp;#198;","AE") # 198: Æ 
		line = string.replace(line,"&amp;#199;","C") # 199: Ç 
		line = string.replace(line,"&amp;#200;","E") # 200: È 
		line = string.replace(line,"&amp;#201;","E") # 201: É 
		line = string.replace(line,"&amp;#202;","E") # 202: Ê 
		line = string.replace(line,"&amp;#203;","E") # 203: Ë 
		line = string.replace(line,"&amp;#204;","I") # 204: Ì 
		line = string.replace(line,"&amp;#205;","I") # 205: Í 
		line = string.replace(line,"&amp;#206;","I") # 206: Î 
		line = string.replace(line,"&amp;#207;","I") # 207: Ï 
		line = string.replace(line,"&amp;#208;","D") # 208: Ð 
		line = string.replace(line,"&amp;#209;","N") # 209: Ñ 
		line = string.replace(line,"&amp;#210;","O") # 210: Ò 
		line = string.replace(line,"&amp;#211;","O") # 211: Ó 
		line = string.replace(line,"&amp;#212;","O") # 212: Ô 
		line = string.replace(line,"&amp;#213;","O") # 213: Õ 
		line = string.replace(line,"&amp;#214;","O") # 214: Ö 
		line = string.replace(line,"&amp;#215;","x") # 215: × 
		line = string.replace(line,"&amp;#216;","r") # 216: Ø 
		line = string.replace(line,"&amp;#217;","U") # 217: Ù 
		line = string.replace(line,"&amp;#218;","U") # 218: Ú 
		line = string.replace(line,"&amp;#219;","U") # 219: Û 
		line = string.replace(line,"&amp;#220;","U") # 220: Ü 
		line = string.replace(line,"&amp;#221;","Y") # 221: Ý 
		line = string.replace(line,"&amp;#222;","s") # 222: Þ 
		line = string.replace(line,"&amp;#223;","S") # 223: ß 
		line = string.replace(line,"&amp;#224;","a") # 224: à 
		line = string.replace(line,"&amp;#225;","a") # 225: á 
		line = string.replace(line,"&amp;#226;","a") # 226: â 
		line = string.replace(line,"&amp;#227;","a") # 227: ã 
		line = string.replace(line,"&amp;#228;","a") # 228: ä 
		line = string.replace(line,"&amp;#229;","a") # 229: å 
		line = string.replace(line,"&amp;#230;","ae") # 230: æ 
		line = string.replace(line,"&amp;#231;","c") # 231: ç 
		line = string.replace(line,"&amp;#232;","e") # 232: è 
		line = string.replace(line,"&amp;#233;","e") # 233: é 
		line = string.replace(line,"&amp;#234;","e") # 234: ê 
		line = string.replace(line,"&amp;#235;","e") # 235: ë 
		line = string.replace(line,"&amp;#236;","i") # 236: ì 
		line = string.replace(line,"&amp;#237;","i") # 237: í 
		line = string.replace(line,"&amp;#238;","i") # 238: î 
		line = string.replace(line,"&amp;#239;","i") # 239: ï 
		line = string.replace(line,"&amp;#240;","o") # 240: ð 
		line = string.replace(line,"&amp;#241;","n") # 241: ñ 
		line = string.replace(line,"&amp;#242;","o") # 242: ò 
		line = string.replace(line,"&amp;#243;","o") # 243: ó 
		line = string.replace(line,"&amp;#244;","o") # 244: ô 
		line = string.replace(line,"&amp;#245;","o") # 245: õ 
		line = string.replace(line,"&amp;#246;","o") # 246: ö 
		line = string.replace(line,"&amp;#247;","/") # 247: ÷ 
		line = string.replace(line,"&amp;#248;","r") # 248: ø 
		line = string.replace(line,"&amp;#249;","u") # 249: ù 
		line = string.replace(line,"&amp;#250;","u") # 250: ú 
		line = string.replace(line,"&amp;#251;","u") # 251: û 
		line = string.replace(line,"&amp;#252;","u") # 252: ü 
		line = string.replace(line,"&amp;#253;","y") # 253: ý 
		line = string.replace(line,"&amp;#254;","y") # 254: þ 
		line = string.replace(line,"&amp;#255;","y") # 255: ÿ 
		line = string.replace(line,"&amp;#256;","A") # 256: Ā 
		line = string.replace(line,"&amp;#257;","a") # 257: ā 
		line = string.replace(line,"&amp;#258;","A") # 258: Ă 
		line = string.replace(line,"&amp;#259;","a") # 259: ă 
		line = string.replace(line,"&amp;#260;","A") # 260: Ą 
		line = string.replace(line,"&amp;#261;","a") # 261: ą 
		line = string.replace(line,"&amp;#262;","C") # 262: Ć 
		line = string.replace(line,"&amp;#263;","c") # 263: ć 
		line = string.replace(line,"&amp;#264;","C") # 264: Ĉ 
		line = string.replace(line,"&amp;#265;","c") # 265: ĉ 
		line = string.replace(line,"&amp;#266;","C") # 266: Ċ 
		line = string.replace(line,"&amp;#267;","c") # 267: ċ 
		line = string.replace(line,"&amp;#268;","C") # 268: Č 
		line = string.replace(line,"&amp;#269;","c") # 269: č 
		line = string.replace(line,"&amp;#270;","D") # 270: Ď 
		line = string.replace(line,"&amp;#271;","d") # 271: ď 
		line = string.replace(line,"&amp;#272;","D") # 272: Đ 
		line = string.replace(line,"&amp;#273;","d") # 273: đ 
		line = string.replace(line,"&amp;#274;","E") # 274: Ē 
		line = string.replace(line,"&amp;#275;","e") # 275: ē 
		line = string.replace(line,"&amp;#276;","E") # 276: Ĕ 
		line = string.replace(line,"&amp;#277;","e") # 277: ĕ 
		line = string.replace(line,"&amp;#278;","E") # 278: Ė 
		line = string.replace(line,"&amp;#279;","e") # 279: ė 
		line = string.replace(line,"&amp;#280;","E") # 280: Ę 
		line = string.replace(line,"&amp;#281;","e") # 281: ę 
		line = string.replace(line,"&amp;#282;","E") # 282: Ě 
		line = string.replace(line,"&amp;#283;","e") # 283: ě 
		line = string.replace(line,"&amp;#284;","G") # 284: Ĝ 
		line = string.replace(line,"&amp;#285;","g") # 285: ĝ 
		line = string.replace(line,"&amp;#286;","G") # 286: Ğ 
		line = string.replace(line,"&amp;#287;","g") # 287: ğ 
		line = string.replace(line,"&amp;#288;","G") # 288: Ġ 
		line = string.replace(line,"&amp;#289;","g") # 289: ġ 
		line = string.replace(line,"&amp;#290;","G") # 290: Ģ 
		line = string.replace(line,"&amp;#291;","g") # 291: ģ 
		line = string.replace(line,"&amp;#292;","H") # 292: Ĥ 
		line = string.replace(line,"&amp;#293;","h") # 293: ĥ 
		line = string.replace(line,"&amp;#294;","H") # 294: Ħ 
		line = string.replace(line,"&amp;#295;","h") # 295: ħ 
		line = string.replace(line,"&amp;#296;","I") # 296: Ĩ 
		line = string.replace(line,"&amp;#297;","i") # 297: ĩ 
		line = string.replace(line,"&amp;#298;","I") # 298: Ī 
		line = string.replace(line,"&amp;#299;","i") # 299: ī 
		line = string.replace(line,"&amp;#300;","I") # 300: Ĭ 
		line = string.replace(line,"&amp;#301;","i") # 301: ĭ 
		line = string.replace(line,"&amp;#302;","I") # 302: Į 
		line = string.replace(line,"&amp;#303;","i") # 303: į 
		line = string.replace(line,"&amp;#304;","I") # 304: İ 
		line = string.replace(line,"&amp;#305;","i") # 305: ı 
		line = string.replace(line,"&amp;#306;","IJ") # 306: Ĳ 
		line = string.replace(line,"&amp;#307;","ij") # 307: ĳ 
		line = string.replace(line,"&amp;#308;","J") # 308: Ĵ 
		line = string.replace(line,"&amp;#309;","j") # 309: ĵ 
		line = string.replace(line,"&amp;#310;","K") # 310: Ķ 
		line = string.replace(line,"&amp;#311;","k") # 311: ķ 
		line = string.replace(line,"&amp;#312;","k") # 312: ĸ 
		line = string.replace(line,"&amp;#313;","L") # 313: Ĺ 
		line = string.replace(line,"&amp;#314;","l") # 314: ĺ 
		line = string.replace(line,"&amp;#315;","L") # 315: Ļ 
		line = string.replace(line,"&amp;#316;","l") # 316: ļ 
		line = string.replace(line,"&amp;#317;","L") # 317: Ľ 
		line = string.replace(line,"&amp;#318;","l") # 318: ľ 
		line = string.replace(line,"&amp;#319;","L") # 319: Ŀ 
		line = string.replace(line,"&amp;#320;","l") # 320: ŀ 
		line = string.replace(line,"&amp;#321;","L") # 321: Ł 
		line = string.replace(line,"&amp;#322;","l") # 322: ł 
		line = string.replace(line,"&amp;#323;","N") # 323: Ń 
		line = string.replace(line,"&amp;#324;","n") # 324: ń 
		line = string.replace(line,"&amp;#325;","N") # 325: Ņ 
		line = string.replace(line,"&amp;#326;","n") # 326: ņ 
		line = string.replace(line,"&amp;#327;","N") # 327: Ň 
		line = string.replace(line,"&amp;#328;","n") # 328: ň 
		line = string.replace(line,"&amp;#329;","n") # 329: ŉ 
		line = string.replace(line,"&amp;#330;","N") # 330: Ŋ 
		line = string.replace(line,"&amp;#331;","n") # 331: ŋ 
		line = string.replace(line,"&amp;#332;","O") # 332: Ō 
		line = string.replace(line,"&amp;#333;","o") # 333: ō 
		line = string.replace(line,"&amp;#334;","O") # 334: Ŏ 
		line = string.replace(line,"&amp;#335;","o") # 335: ŏ 
		line = string.replace(line,"&amp;#336;","O") # 336: Ő 
		line = string.replace(line,"&amp;#337;","o") # 337: ő 
		line = string.replace(line,"&amp;#338;","CE") # 338: Œ 
		line = string.replace(line,"&amp;#339;","ce") # 339: œ 
		line = string.replace(line,"&amp;#340;","R") # 340: Ŕ 
		line = string.replace(line,"&amp;#341;","r") # 341: ŕ 
		line = string.replace(line,"&amp;#342;","R") # 342: Ŗ 
		line = string.replace(line,"&amp;#343;","r") # 343: ŗ 
		line = string.replace(line,"&amp;#344;","R") # 344: Ř 
		line = string.replace(line,"&amp;#345;","r") # 345: ř 
		line = string.replace(line,"&amp;#346;","S") # 346: Ś 
		line = string.replace(line,"&amp;#347;","s") # 347: ś 
		line = string.replace(line,"&amp;#348;","S") # 348: Ŝ 
		line = string.replace(line,"&amp;#349;","s") # 349: ŝ 
		line = string.replace(line,"&amp;#350;","S") # 350: Ş 
		line = string.replace(line,"&amp;#351;","s") # 351: ş 
		line = string.replace(line,"&amp;#352;","S") # 352: Š 
		line = string.replace(line,"&amp;#353;","s") # 353: š 
		line = string.replace(line,"&amp;#354;","T") # 354: Ţ 
		line = string.replace(line,"&amp;#355;","t") # 355: ţ 
		line = string.replace(line,"&amp;#356;","T") # 356: Ť 
		line = string.replace(line,"&amp;#357;","t") # 357: ť 
		line = string.replace(line,"&amp;#358;","T") # 358: Ŧ 
		line = string.replace(line,"&amp;#359;","t") # 359: ŧ 
		line = string.replace(line,"&amp;#360;","U") # 360: Ũ 
		line = string.replace(line,"&amp;#361;","u") # 361: ũ 
		line = string.replace(line,"&amp;#362;","U") # 362: Ū 
		line = string.replace(line,"&amp;#363;","u") # 363: ū 
		line = string.replace(line,"&amp;#364;","U") # 364: Ŭ 
		line = string.replace(line,"&amp;#365;","u") # 365: ŭ 
		line = string.replace(line,"&amp;#366;","U") # 366: Ů 
		line = string.replace(line,"&amp;#367;","u") # 367: ů 
		line = string.replace(line,"&amp;#368;","U") # 368: Ű 
		line = string.replace(line,"&amp;#369;","u") # 369: ű 
		line = string.replace(line,"&amp;#370;","U") # 370: Ų 
		line = string.replace(line,"&amp;#371;","u") # 371: ų 
		line = string.replace(line,"&amp;#372;","W") # 372: Ŵ 
		line = string.replace(line,"&amp;#373;","w") # 373: ŵ 
		line = string.replace(line,"&amp;#374;","Y") # 374: Ŷ 
		line = string.replace(line,"&amp;#375;","y") # 375: ŷ 
		line = string.replace(line,"&amp;#376;","Y") # 376: Ÿ 
		line = string.replace(line,"&amp;#377;","Z") # 377: Ź 
		line = string.replace(line,"&amp;#378;","z") # 378: ź 
		line = string.replace(line,"&amp;#379;","Z") # 379: Ż 
		line = string.replace(line,"&amp;#380;","z") # 380: ż 
		line = string.replace(line,"&amp;#381;","Z") # 381: Ž 
		line = string.replace(line,"&amp;#382;","z") # 382: ž 
		line = string.replace(line,"&amp;#383;","i") # 383: ſ 
	
		line = string.replace(line,"&amp;#399;","E") # 399: Ə 
	
		line = string.replace(line,"&amp;#402;","f") # 402: ƒ 
	
		line = string.replace(line,"&amp;#416;","O") # 416: Ơ 
		line = string.replace(line,"&amp;#417;","o") # 417: ơ 
	
		line = string.replace(line,"&amp;#431;","U") # 431: Ư 
		line = string.replace(line,"&amp;#432;","u") # 432: ư 
	
		line = string.replace(line,"&amp;#461;","A") # 461: Ǎ 
		line = string.replace(line,"&amp;#462;","a") # 462: ǎ 
		line = string.replace(line,"&amp;#463;","I") # 463: Ǐ 
		line = string.replace(line,"&amp;#464;","i") # 464: ǐ 
		line = string.replace(line,"&amp;#465;","O") # 465: Ǒ 
		line = string.replace(line,"&amp;#466;","o") # 466: ǒ 
		line = string.replace(line,"&amp;#467;","U") # 467: Ǔ 
		line = string.replace(line,"&amp;#468;","u") # 468: ǔ 
		line = string.replace(line,"&amp;#469;","U") # 469: Ǖ 
		line = string.replace(line,"&amp;#470;","u") # 470: ǖ 
		line = string.replace(line,"&amp;#471;","U") # 471: Ǘ 
		line = string.replace(line,"&amp;#472;","u") # 472: ǘ 
		line = string.replace(line,"&amp;#473;","U") # 473: Ǚ 
		line = string.replace(line,"&amp;#474;","u") # 474: ǚ 
		line = string.replace(line,"&amp;#475;","U") # 475: Ǜ 
		line = string.replace(line,"&amp;#476;","u") # 476: ǜ 
	
		line = string.replace(line,"&amp;#506;","A") # 506: Ǻ 
		line = string.replace(line,"&amp;#507;","a") # 507: ǻ 
		line = string.replace(line,"&amp;#508;","AE") # 508: Ǽ 
		line = string.replace(line,"&amp;#509;","ae") # 509: ǽ 
		line = string.replace(line,"&amp;#510;","O") # 510: Ǿ 
		line = string.replace(line,"&amp;#511;","o") # 511: ǿ 
	
		line = string.replace(line,"&amp;#601;","e") # 601: ə 
	
		line = string.replace(line,"&amp;#710;","'") # 710: ˆ 
		line = string.replace(line,"&amp;#711;","'") # 711: ˇ 
	
		line = string.replace(line,"&amp;#713;","-") # 713: ˉ 
	
		line = string.replace(line,"&amp;#728;","'") # 728: ˘ 
		line = string.replace(line,"&amp;#729;","'") # 729: ˙ 
		line = string.replace(line,"&amp;#730;","'") # 730: ˚ 
		line = string.replace(line,"&amp;#731;",".") # 731: ˛ 
		line = string.replace(line,"&amp;#732;","'") # 732: ˜ 
		line = string.replace(line,"&amp;#733;","'") # 733: ˝ 
	
		line = string.replace(line,"&amp;#768;","'") # 768: ̀ 
		line = string.replace(line,"&amp;#769;","'") # 769: ́ 
	
		line = string.replace(line,"&amp;#771;","'") # 771: ̃ 
		
		line = string.replace(line,"&amp;#777;","'") # 777: ̉ 
		
		line = string.replace(line,"&amp;#803;",".") # 803: ̣ 
		
		line = string.replace(line,"&amp;#894;",";") # 894: ; 
		
		line = string.replace(line,"&amp;#900;","'") # 900: ΄ 
		line = string.replace(line,"&amp;#901;","'") # 901: ΅ 
		line = string.replace(line,"&amp;#902;","A") # 902: Ά 
		line = string.replace(line,"&amp;#903;",".") # 903: · 
		line = string.replace(line,"&amp;#904;","E") # 904: Έ 
		line = string.replace(line,"&amp;#905;","H") # 905: Ή 
		line = string.replace(line,"&amp;#906;","I") # 906: Ί 
		
		line = string.replace(line,"&amp;#908;","O") # 908
	
	
	
		line = re.compile("&#\d+;", re.DOTALL).sub("#", line)
	
	
	
		output += line
	
	file.close
	
	# zapis do souboru
	try:
		file = open(filename, "w")	# xml soubror
	except:
		ErrorFile(filename)
		return False

	file.write(output)
	file.close
	
	print "XML chars was successfully converted!"
	
	return True



### MAIN #######################################################################

if (__name__=="__main__"):
	# osetreni parametru prikazove radky
	if(len(sys.argv) == 2 and sys.argv[1] == "-h"):
		Help()
	elif(len(sys.argv) == 2):
		XmlChar(sys.argv[1])
	else:
		ErrorArg()
