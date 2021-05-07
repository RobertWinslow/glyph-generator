# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:36:53 2021

@author: RobertWinslow

This programmitically generates glyphs to include in the cards. I need about 5 thousand of them. Fortunarely, Unicode already contains thousands of distinct glyphs. So If I choose a few hundred I like and combine them with several distinct background decorations, that should do the trick.

The images also have a cycling pattern of colors applied,  but this is not used to dinstinguish between images; any two images should be dinstinct by shape alone.
"""
import os

#%% svg snippets

preamblesnippet = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="10in" height="10in" version="1.1" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
'''


textsnippet='<text x="500" y="720" font-size="750" font-family="Quivira, Ma Shan Zheng" fill="PLACEHOLDERCOLOR" text-anchor="middle">PLACEHOLDERTEXT</text>'
# CMU Serif, Ma Shan Zheng, Catrinity, DejaVu Sans 
#Unifont Upper, ZCOOL Kuaile ,Long Cang, Liu Jian Mao Cao, Symbola
# CMU Serif, Ma Shan Zheng, DejaVu Sans, Code2000
# WenQuanYi Zen Hei is GPL, not sure whether font exception exists
# Code2000 is "shareware", and I'm not entirely sure what that means.

endsnippet='</svg>'

#%% backgrounds. These use modified snippets of svgs with PLACEHOLDERCOLOR and PLACEHOLDER2COLOR as substrings to be replaced by the appropriate colors.

backgroundlist = [''' ''', #just the character
                  '''<rect x="0" y="0" width="1000" height="1000" style="fill:PLACEHOLDERCOLOR;stroke-width:100;stroke:PLACEHOLDER2COLOR"/>''',#solid square
                  '''<circle cx="500" cy="500" r="475"  style="fill:PLACEHOLDERCOLOR;stroke-width:50;stroke:PLACEHOLDER2COLOR"/>''', #solid circle
                  #'''<path d="m25 25   300 950   650 -750z" style="fill:PLACEHOLDERCOLOR;stroke-width:50;stroke:PLACEHOLDER2COLOR"/>''',
                  '''<path d="m0 800   1000 50   -425 -850z" style="fill:PLACEHOLDERCOLOR;stroke-width:0;stroke:PLACEHOLDER2COLOR"/>''', #faint triangle
                  '''<circle cx="500" cy="500" r="475"  style="fill:none;stroke-width:50;stroke:PLACEHOLDER2COLOR"/>''', #empty circle
                  '''<path d="m500 0   400 500   -400 500   -400 -500    400 -500z" style="fill:PLACEHOLDERCOLOR;stroke-width:0;stroke:PLACEHOLDER2COLOR"/>''',#faint diamond
                  '''<path d="m500 25   433 225   0 500   -433 225   -433 -225   0 -500    433 -225z" style="fill:PLACEHOLDERCOLOR;stroke-width:50;stroke:PLACEHOLDER2COLOR"/>''', #solid hex
                  '''<path transform="matrix(1.1328 0 0 1.1326 -66.404 -66.319)" d="m500 921.42-80.635-226.75-217.35 103.32 103.32-217.35-226.75-80.635 226.75-80.635-103.32-217.35 217.35 103.32 80.635-226.75 80.635 226.75 217.35-103.32-103.32 217.35 226.75 80.635-226.75 80.635 103.32 217.35-217.35-103.32z" style="fill:PLACEHOLDERCOLOR;stroke-width:0;stroke:PLACEHOLDER2COLOR"/>''', #starburst
                  '''<circle id="d" cx="134.03" cy="134.03" r="109.03" style="fill:PLACEHOLDERCOLOR;paint-order:stroke fill markers;stroke-linecap:round;stroke-width:50;stroke:PLACEHOLDER2COLOR"/>
 <use id="b" transform="translate(731.95)" width="100%" height="100%" xlink:href="#d"/>
 <use id="a" transform="translate(-731.95 731.95)" width="100%" height="100%" xlink:href="#b"/>
 <use transform="translate(731.95)" width="100%" height="100%" xlink:href="#a"/>
 <rect id="c" transform="rotate(45)" x="666.22" y="-575.61" width="81.78" height="1151.2" style="fill:PLACEHOLDERCOLOR;paint-order:stroke fill markers"/>
 <use transform="matrix(-1 0 0 1 1e3 -2.0361e-6)" width="100%" height="100%" style="stroke:PLACEHOLDERCOLOR" xlink:href="#c"/>
                  ''', #broken X
                  '''<path id="c" d="m50 50 149.78 149.78" style="fill:PLACEHOLDERCOLOR;paint-order:markers fill stroke;stroke-linecap:round;stroke-linejoin:round;stroke-width:100;stroke:PLACEHOLDER2COLOR"/>
 <path d="m549.52 995.22c-355.78 35.578 115.01-131.68-161.72-358.09-276.73-226.42-347.45 268.17-383.02-87.606-35.578-355.78 131.68 115.01 358.09-161.72 226.42-276.73-268.17-347.45 87.606-383.02 355.78-35.578-115.01 131.68 161.72 358.09 276.73 226.42 347.45-268.17 383.02 87.606 35.578 355.78-131.68-115.01-358.09 161.72-226.42 276.73 268.17 347.45-87.606 383.02z" style="fill:PLACEHOLDERCOLOR;paint-order:markers fill stroke"/>
 <use id="b" transform="translate(750.22 750.22)" width="100%" height="100%" xlink:href="#c"/>
 <use id="a" transform="matrix(-1 0 0 1 1e3 5e-6)" width="100%" height="100%" xlink:href="#b"/>
 <use transform="translate(750.22 -750.22)" width="100%" height="100%" xlink:href="#a"/>''',#weird blob
                 ''' <path d="m72.687 376.65 57.269-244.49 222.47-63.877 568.28 572.69-48.458 220.26-222.47 70.485z" style="fill:PLACEHOLDERCOLOR;paint-order:markers fill stroke"/>
 <circle id="e" cx="130.07" cy="136.67" r="75" style="fill:PLACEHOLDER2COLOR"/>
 <use id="d" transform="translate(217.49 -61.674)" width="100%" height="100%" xlink:href="#e"/>
 <use id="c" transform="translate(-272.56 297.25)" width="100%" height="100%" xlink:href="#d"/>
 <use id="b" transform="translate(792.84 480.18)" width="100%" height="100%" xlink:href="#c"/>
 <use id="a" transform="translate(-215.4 72.577)" width="100%" height="100%" xlink:href="#b"/>
 <use transform="translate(272.56 -283.57)" width="100%" height="100%" xlink:href="#a"/>''', #six spots
                  ]
    

#%% color schemes

textcolors = ["#652277","#742434","#724a38", '#997736',"#054208","#113074","#35301c","#222"]
textcolorindex = 0;


bgfillcolors = ["#BCE","#CEF","#CDA","#EEB","#FCC","#DDD","#FDF"]
bgfillindex = 0;


bgbordercolors = ["#225","#255","#252","#663","#633","#555","#525"]
bgborderindex = 0;


#%% characterlists
#'ⰀⰁⰂⰃⰅⰆⰇⰈ'

religious='☥☮☯☦☧☩☪☬☫☭☨☸♰♱'


charlist =  'ABCDEFGHIJKLMNOPQRSTUVWXYZabefghijklmnrstu'#latin
charlist += 'αβΓγΔδεζηΘθιλμΞξπρΣσςτΦφχΨψΩω' #greek
charlist += 'अइउऋऌएईओकचटतखछङञणनमबहसडद' #devanagari
charlist += 'অইউঋআঈঊশষকটতপফঠঢ' #bengali
#charlist += 'க்ங்ண்ல்ஜஅஇஈஉஐஒ' #tamil Complex multiple-character glyphs
charlist += 'ДИЛñѮѺѾᴥᴁᴂᴕᴤᴣᵫᵹꙮꙬԘѪѦ' #a few extra letters
charlist += '¡¿⅋⅊℞※†‡‰‽⁂⁖⁙⁞⁝℀℄℆№℗℥' #some letter-adjacent characters


charlist += '0123456789' #numerals
charlist += '一二三四五六七八九十百千万亿' #chinese numerals
#charlist += '๑๒๓๔๕๖๗๘๙' #thai numerals
charlist += '১২৩৫৬৯' #bengali numerals
charlist += '௧௨௩௪௫௬௭௮௯௰' #tamil numerals
charlist += '១២៣៤៥៦៧៨៩' #khmer numerals
charlist += 'דגאב' #hebrew numerals
charlist += 'ↀↁↂↅ' #weird roman numerals

charlist += '⨁♄♃♂☼♀☿☽♁⊛♆♅♇⚶⚵⚴⚳⚷⚸⚺⚼♈♉♊♋♌♍♎♏♐♑♒♓' #alchemical and astronomical
charlist += '☤♲♵♻⚚⚛⌬⏣⚕⚗' #alchemical adjacent
charlist += '♔♕♖♗♘♙♚♛♜♝♞♟' #chess set
charlist += '⚀⚁⚂⚃⚄⚅⚇' #dice set
charlist += '¤₿¢₡$€£₹₽¥₩₪₢₣₾₯'#currency symbols
charlist += '↛↣↬↻↹⇔⇝⇴⟲⟴➾' #arrows
charlist += '⑄⑀⑂⑅⑆⑇⑈⑉' #ocr
charlist += '𝄞𝅘𝅥𝅯𝅘𝅥𝅮𝄫𝄢'
charlist += '☺☻☹' +'😏😃😷😒😚😌😘😆😭😂😣😓😁😪😖😱😋😲😇' #faces
charlist += '★☆✪✵✯❉❋✺✹✸✶✲✱✧✦⍟❃❂✼⍣≛✫❀✿⚘❁✾✥❖❅❆❡❢❥❦❧⚙' #stars and flowers and pretty floral decorators⚝⚜☘
charlist += '▦▩▨▤▣▢⚔∛∢∦⌂⌇⌘⌗⌖⌕⌔⌑⌥⌫⌯⌱⌭⍲⍝⍗⍖⍕⌹⍼⍽⍾⎉⎌⎆⎄⎅⎇⎈⎊⎍⎒⎓⎔⎶⏅⏄⏍⏔⏚⏛⏥⧮⧯⧰⧱⧲⧳⨊⟅⟐⟠⟡⥾◰◔◕◷◒╬╦' #assorted weird bits of geometry, mostly technical symbols and operators⏻
charlist += '∜∬∭∮∯∰∲∻∺≋≎≜⋇⨷⩏⫺⪮⋛⫸⦄⦝⦞⦪⦻⦔⦕⦼⧈⧉⧎⧛⨌⨔⨖⨙⨮⩅⫘' #more math symbols
#charlist += '🀰🀱🀲🀳🀴🀵🀶🀷🀸🀹🀺🀻🀼🀽🀾🀿🁀🁁🁂🁃🁄🁅🁆🁇🁈🁉🁊🁋🁌🁍🁎🁏🁐🁑🁒🁓🁔🁕🁖🁗🁘🁙🁚🁛🁜🁝🁞🁟🁠🁡' #domino

charlist += '肉牛马羊鸟鱼龟狗猫鼠龙鹿虫' #animals
charlist += '人男女子鬼巫王工学生飞' #people and actions
charlist += '火土金木水日月山天川风雪雨电米果田葱松豆韭玉' #elements+nature
charlist += '中大小开上下出重凹凸左右不' #position/size/shape
charlist += '口心手齿羽爪目头耳舌面足鼻' #body parts
charlist += '画刀车网书矛串纸门弓舟油图国' #body parts
charlist += '赤黑白红黄蓝紫灰' #color terms
#charlist += '⼇⼉⼌⼎⼏⼐⼒⼜⼪⼫⼬⼮⼰⼱⼹⼺⼻⼾⽌⽍⽎⽏⽓⽗⽘⽙⽞⽠⽧⽫⽮⽯⽰⽱⽴⽵⽷⽽⽾⾂⾀⾅⾊⾋⾍⾑⾔⾕⾙⾞⾟⾣⾥⾨⾿⿒⿕' #loose radicals (don't render well)


#doublecheck for character collisions
for c1 in charlist:
    if charlist.count(c1) != 1:
        print(c1)


#%%

for i,background in enumerate(backgroundlist):
    for j,character in enumerate(charlist):
        f = open('outputvectors/glyph'+str(i)+'-'+str(j)+'.svg','w',encoding='utf8')
        
        textcontent = textsnippet
        textcontent = textcontent.replace('PLACEHOLDERCOLOR',textcolors[textcolorindex])
        textcolorindex = (textcolorindex+1)%len(textcolors)
        textcontent = textcontent.replace('PLACEHOLDERTEXT',character)
        
        newbackground = background.replace('PLACEHOLDERCOLOR',bgfillcolors[bgfillindex])
        bgfillindex = (bgfillindex+1)%len(bgfillcolors)
        
        newbackground = newbackground.replace('PLACEHOLDER2COLOR',bgbordercolors[bgborderindex])
        bgborderindex = (bgborderindex+1)%len(bgbordercolors)
        
        
        f.write(preamblesnippet+newbackground+textcontent+endsnippet)
        f.close()











