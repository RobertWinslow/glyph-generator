# -*- coding: utf-8 -*-
"""
Created on Tue May 6
@author: RobertWinslow

Problem: Inkscape's batch svg-to-png image conversion mangles some of my glyphs.

Solution that works for individual images: Use a web browser to render and convert the svg files.

Bulk Solution: Rewrite the glyph generator to directly generate PNGs.

Sidenote: Since I need to rewrite the image generation code, I may as well play around with a different aesthetic.

"""
#%%
import os
from PIL import Image, ImageDraw, ImageFont




#%% PARAMETER Color list for text
textcolors = ["#742434","#823322","#814a25",'#705420',"#64591a","#495b22",
              "#2f5d3a","#164e3d","#154b4d","#134a60","#173459",
              "#222248","#34254d","#563762","#5f3458","#6e294c",
              "#461d1e","#442112","#50341a","#3f2c10","#352e0a","#20340b",
              "#2b292b",
              ]
tci = 0; #text color index (introduce irregularity by not restarting the color cycle for each bg) There are 23 entries, which should hopefully be coprime with any other numbers that pop up in cycles.

#Some of the public domain fonts I found have multiple layers. So lets add another list of coprime size to cycle through those.
textcolors2 = ["#d51c3c","#e83b1b","#ff9d50",'#ffbe50',"#f7ce50",
               "#e9dc55","#c3df69","#87d989","#49d0a3","#35d7ce",
               "#2dbce2","#419ded","#9099ff","#ad90fa","#ce8ce3",
               "#d23f83","#fca1e7","#f48fa0","#c49a74","#f1bf15",
               "#ebdd21","#a7dc26","#e7e1e9",]
tci2 = 0




#%% FUNCTION Create an image with the indicated background and with a character in the middle.

def genglyph(background,textcontent,textcolor,font, outfile,font2=None):
    W,H = (512,512)
    img=Image.new("RGBA", (W,H),(0,0,0,0))
    draw = ImageDraw.Draw(img)
    
    img.paste(background,(0,0))
    
    contentbbox = draw.textbbox((0,0) ,textcontent, font=font)
    w,h = contentbbox[2]-contentbbox[0],contentbbox[3]-contentbbox[1],
    w2,h2 = draw.textsize(textcontent, font=font)
    topmargin = h2-h
    
    draw.text(((W-w)//2,0-topmargin+(H-h)//2), textcontent, font=font, fill=textcolor)
    
    if font2:
        global tci2
        draw.text(((W-w)//2,0-topmargin+(H-h)//2), textcontent, font=font2, fill=textcolors2[tci])

    img.save(outfile)

#%% FUNCTION turn some characters into images
def genglyphset(characterlist,fontname,setid,fontsize,fontname2=None):
    font = ImageFont.truetype(fontname,fontsize)
    font2 = None
    if fontname2:
        font2 = ImageFont.truetype(fontname2,fontsize)
    
    # For each background folder
    for ibg, folder in enumerate(os.listdir('backgrounds')):
        # Get all the backgrounds
        backgrounds = []
        for file in os.listdir('backgrounds/'+folder):
            backgrounds.append(Image.open('backgrounds/'+folder+'/'+file))
            
        # Then cycle through the backgrounds until we've made an image for every character.
        global tci
        for i, c in enumerate(characterlist):
            bg = backgrounds[i%len(backgrounds)]
            genglyph(bg,c,textcolors[tci],font,'output/'+folder+'-'+setid+'-'+str(i)+'.png',font2)
            tci = (tci+1)%len(textcolors)

#%% PARAMETER Define character lists
#ⰀⰁⰂⰃⰅⰆⰇⰈ

# Curated list of distinctive looking characters supported by Quivira
quiviralist = ''
quiviralist += '¡¢£¤¥§©«®±¶¿ÆÐÑ×ØÞßæçîðñö÷þĦĲĳĿŊŋŒœſƁƂƐƑƒƓƔƕƗƠƢƥƦƪƫƱƲǁǂǃǅǇǶȡȢȴȵȶɁɮʬʭᴥ' #latin adjacent
quiviralist += '℅℄℔№℗℞℟℠℡™℣℥℻⅊⅋⅌⅍⅏' #letterlike
quiviralist += 'ⅆⅇⅈⅉℂⅅℍℕℙℚℝℤℼℽℾℿ⅀ℓ℘ℬℰℱℋℐℒℳℛℭℌℑℜℨ' #math scripts

quiviralist += '𐄡𐄨𐄷𐄸𐄺𐄽' #Aegean Numbers 
quiviralist += '𐅌𐅫𐅯𐅲𐅿𐆇𐆉' #Ancient Greek Numbers 𐅮
quiviralist += 'ⅢⅤⅪↀↁↂↇↈ⅜↉⅐' #roman numerals, fractionsⅧ
quiviralist += '๑๒๓๔๕๖๗๘๙๚๛' #thai numerals
quiviralist += '➑⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴' #enclosed numbers

quiviralist += 'ͲͼϏϘϞϠϡϢϤϧϨϪⲀⲮⲴⲶⳢ⳥⳦⳧⳨⳩⳪ⳫⳭ' #greek + coptic
quiviralist += 'ѢѤѦѨѪѬѲѸѺѼҒҔҖҦҨԄԆԘԠԬꙈꙊꙌꙒꙖꙚꙜꙞꙫꙬꙮꚄꚎꚖ' #cyrillic
quiviralist += 'ᚡᚣᚥᚧᚩᚬᚱᚸᚻᚼᛃᛄᛈᛓᛔᛗᛠᛤᛥᛨᛪᛯᛵ' #futhark et al
quiviralist += 'ՋՖ՞եթխձջֆև֍֏' #armenian
quiviralist += '׆ׇאבגדהלצקש' #hebrew
quiviralist += 'ࠀࠄࠅࠆࠈࠌࠎ࠴࠽' #samaritan
quiviralist += 'ᚗᚘᚙ' #ogham
quiviralist += 'ᜀᜁᜃᜄᜅᜆᜈᜎᜐ' #tagalog
quiviralist += 'ᝆᝇᝌᝎᝐ' #buhid
quiviralist += '𐋃𐋄𐋈' #Carian
quiviralist += '𐌸𐍆' #Gothic
quiviralist += '𐎄𐎌𐎗𐎑𐎝𐎋' #Ugaritic

quiviralist += '†‡‰※‼‽⁂⁆⁇⁈⁉⁋⁌⁐⁑⁗⁙⁝⁞⸎⸙⸶⸽⸾⸿' #punctuation‱
quiviralist += '₠₡₢₤₦₧₨₩₪₫€₯₰₱₳₴₵₷₹₺₻💲💳' #currency 💱💴💵💶💷
quiviralist += '↝↫↭↶↹⇌⇏⇒⇔⇚⇞⇣⇦⇪⇮⇯⇰⇲⇿⍆⌰⌱⌮⍼⎆⎇⎋⎌⏎'+'⭚⭯⭾⮉⮏⮐⮓⮔⮳'+'⤭⥾⟴⟼⟿☛☞➶➳➠' #arrows 
quiviralist += '∅∊√∛∝∡∫∬∭∮∯∰∱∲∳∻≁≇≉≋≍≎≒≝≟≠≡≣≥≪≬≭≰≶≹≼⊊⊌⊍⊎⊛⊜⊞⊟⊠⊡⊰⊶⊿⋐⋗⋘⋛'+'⨊⨋⨌⨒⨓⨕⨖⨗⩎⩐⩴⩷⫎⫸⫹' #math operators
quiviralist += '' #misc math symbols


quiviralist += '⌀⌂⌖⌘⌚⌥⌨⌫⌬⌭⌯⌹⌺⌻⌼⍄⍌⍽⍾⎃⎄⎅⎈⎉⎊⎍⎎⎑⎗⎘⎙⎚⏍⏏⏚⏛⏣⏦⏧⏯⏰⏳' #misc technical ⌡
quiviralist += '⑀⑁⑄⑆⑇⑈⑉' #ocr  
quiviralist += '╤╦╬░▒▓▚▣▥▦▨▩▱◈◉◌◍◎◒◔◕◙◚◧◪◰◷🞋🞖🞠' #box, block, geometric 
quiviralist += '☼☾☿♀♂♃♄♅♆♇♈♉♊♋♌♍♎♏♐♑♒♓⚳⚴⚵⚶⚷⚸⚺⚼' #astronomical
quiviralist += '🜀🜈🜉🜋🜎🜏🜐🜑🜒🜓🜚🜛🜝🜟🜡🜣🜤🜦🜧🜩🜪🜯🜰🜱🜲🜳🜴🜵🜶🜷🜸🜹🜼🜾🝀🝁🝂🝃🝄🝆🝉🝊🝋🝍🝏🝐🝖🝙🝚🝛🝜🝩🝭🝮🝰🝲🝳' #alchemical 🝝
quiviralist += '𝄇𝄜𝄞𝄡𝄢𝄩𝄪𝄫𝄮𝄼𝄽𝄾𝄿𝅀𝅁𝅂𝅘𝅥𝅮𝅘𝅥𝅯𝅘𝅥𝅰𝅘𝅥𝅱𝆶𝆺𝅥𝅮𝆹𝅥𝅯🎵🎶🎼♩♪♫♬' #music
quiviralist += '♔♕♖♗♘♙♚♛♜♝♞♟' #chess (including quivira-specific symbols) 
quiviralist += '♠♡♢♣♤♥♦♧⛀⛁⛂⛃🎯🎴⚀⚁⚂⚃⚄⚅⚆⚇⚈⚉☗☖' #game symbols (some are specific to quivira)
#quiviralist += '' #quivira-specific misc symbols
quiviralist += '' #quivira-specific: genji-mon (Orange blossoms, bamboo river, butterflies, oak tree)

quiviralist += '☹☺☻🐵👀👂👃👄👅👽💀😀😁😂😆😇😈😉😋😌😍😎😏😐😑😒😓😔😕😖😗😘😚😜😟😠😤😧😨😩😬😭😯😱😳😴😵😷😸😹😺😻😼😽😾😿🙀🙅🙇🙈🙉🙊🙋🙌🙍🙎🙏〠' #faces: emoticons and misc symbols
quiviralist += '🌀🌁🌂🌈🌍🌎🌏🌐🌙🌟🌠🌢🌲🌳🌴🌵🏠🏡🏢🏣🏥🏪🏬🏭🏮👍👤👥👪💋💓💔💕💖💗💘💙💚💛💣💤💥💧💩💿📞📤📥📦📧📨📩📯📶🔇🔉🔊🔎🔑🔒🔓🔘🔠🔡🔢🔣🔤🔥🖂🗚🕱🗡🗺〄〶'+'☀☁☂☃☄☎☏☕☠☢☣☤☥☮☯♨⚢⚣⚤⚧⚐⚑⚒⚓⚔⚖⚗⚘⚙⚚⚛⚠⚡⛄⛅⛆⛇⛈⛤⛨⛩⛪⛫⛱⛲⛳⛴⛵⛶⛺⛻⛼⛽⛾⛿⚰⚱⚿⛞⛔⛮♼♽'+'✂✇✈✉✎✑✒✯❄❉❖⭔⯌⯏⯐⭖' # Miscellaneous Symbols and Pictographs⚥⚨⚕


#quiviralist += '' #quivira-specific laundry, commented out because the symbols are copyrighted in some countries (!??)
#quiviralist += '🀀🀁🀂🀃🀄🀅🀆🀇🀈🀉🀊🀋🀌🀍🀎🀏🀐🀑🀒🀓🀔🀕🀖🀗🀘🀙🀚🀛🀜🀝🀞🀟🀠🀡🀢🀣🀤🀥🀦🀧🀨🀩🀪🀫' #mahjong tiles
#quiviralist += '🀰🀱🀲🀳🀴🀵🀶🀷🀸🀹🀺🀻🀼🀽🀾🀿🁁🁂🁃🁄🁅🁆🁇🁈🁉🁊🁋🁌🁍🁎🁏🁐🁑🁒🁓🁔🁕🁖🁗🁘🁙🁚🁛🁜🁝🁞🁟🁠🁡🁢🁣🁤🁥🁦🁧🁨🁩🁪🁫🁬🁭🁮🁯🁰🁱🁲🁳🁴🁵🁶🁷🁸🁹🁺🁻🁼🁽🁾🁿🂀🂁🂂🂃🂄🂅🂆🂇🂈🂉🂊🂋🂌🂍🂎🂏🂐🂑🂒🂓' #domino tiles
#quiviralist += '🂡🂼🃍🃞🃵' #playing cards
#quiviralist += '🂠🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂬🂭🂮🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂼🂽🂾🂿🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃌🃍🃎🃏🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃜🃝🃞🃟🃠🃡🃢🃣🃤🃥🃦🃧🃨🃩🃪🃫🃬🃭🃮🃯🃰🃱🃲🃳🃴🃵' #playing cards

#Check for uniqueness (in terms of codepoint) and lack of spaces.
for c in quiviralist:
    if quiviralist.count(c) != 1:
        print(c, 'duplicated')
for c in [' .?!&*."/\[]:;|,$'+"'"]:
    if c in quiviralist:
        print(c,'should be removed')

hanzilist = '肉牛马羊鸟鱼龟狗猫鼠龙鹿虫' #animals
hanzilist += '人男女子鬼巫王工学生飞' #people and actions
hanzilist += '火土金木水日月山天川风雪雨电米果田葱松豆韭玉' #elements+nature
hanzilist += '中大小开上下出重凹凸左右不' #position/size/shape
hanzilist += '画刀车网书矛串纸门弓舟油图国' #body parts
hanzilist += '赤黑白红黄蓝紫灰' #color terms
#charlist += '⼇⼉⼌⼎⼏⼐⼒⼜⼪⼫⼬⼮⼰⼱⼹⼺⼻⼾⽌⽍⽎⽏⽓⽗⽘⽙⽞⽠⽧⽫⽮⽯⽰⽱⽴⽵⽷⽽⽾⾂⾀⾅⾊⾋⾍⾑⾔⾕⾙⾞⾟⾣⾥⾨⾿⿒⿕' #loose radicals (don't render well)


CLIST="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
llist="abcdefghijklmnopqrstuvwxyz"
dlist="0123456789"

#%% PARAMETER create font objects
tfont = ImageFont.truetype('TwitterColorEmoji-SVGinOT_1.ttf',450)
qfont = ImageFont.truetype('Quivira.otf',450)
CMUfont = ImageFont.truetype('cmunbx.ttf',450)

MSZfont = ImageFont.truetype('MaShanZheng-Regular_0.ttf',440)
djfont = ImageFont.truetype('DejaVuSans.ttf',450)
tdfont1 = ImageFont.truetype('Counterscraps.otf',450)



#%% PROCEDURE Make the things

#genglyphset('012345678','ComputerMavisSerif-Roman_0.ttf','xkcd',450) #xkcd.com/2206. I made the font.

genglyphset(quiviralist,'Quivira.otf','quivira',430)
genglyphset('🂡🂼🃍🃞🃵🀐🀟🀔🀄🀃','Quivira.otf','quivira-cards',650)
genglyphset('🁢🁣🁤🁥🁦🁧🁨🁩🁫🁬🁭🁮🁯🁰🁳🁴🁵🁶🁷🁻🁼🁽🁾🂃🂄🂅🂋🂌🂓','Quivira.otf','quivira-domino',380)


genglyphset(CLIST+llist+dlist,'Counterscraps.otf','TDcounter',420) #Typodermic CC0
genglyphset(CLIST+llist+dlist,'Sappy Mugs.otf','TDsappy',420)

genglyphset(CLIST+dlist,'Neurochrome.otf','TDchrome',420,)
genglyphset('EUap','Oil Crisis A.otf','TDcar',170,) #only chose a few characters with very distinctive vehicles.
genglyphset(CLIST+dlist,'Pop Up Fontio.otf','TDpopup',500,)

genglyphset(CLIST+dlist,'Hawkeye Back.otf','TDhawkeye',420, 'Hawkeye Front.otf')
genglyphset(CLIST+'012345678','Groovy Ghosties Back.otf','TDghost',420, 'Groovy Ghosties Front.otf')
genglyphset(CLIST+dlist,'Graffiti Treat Back.otf','TDgraffiti',420, 'Graffiti Treat Front.otf')
genglyphset(CLIST+dlist,'Riot Act 2 Back.otf','TDriot',420, 'Riot Act 2 Front.otf')
genglyphset(CLIST+'012345678','Got No Heart.otf','TDheart',375, 'Got No Heart Solid.otf')

#genglyphset(CLIST+llist+dlist,'Bocartes-fritos.otf','OFLBocartes',375)
#genglyphset('ABCDEFGHIJKLMNOPQRSTUVWXYZabefghijklmnrstu0123456789αβΓγΔδεζηΘθιλμΞξπρΣσςτΦφχΨψΩω',CMUfont,'CMUmathy')
#genglyphset('一二三四五六七八九十百千万亿肉牛马羊鸟鱼龟狗猫鼠龙鹿虫人男女子鬼巫王工学生飞火土金木水日月山天川风雪雨电米果田葱松豆韭玉中大小开上下出重凹凸左右不口心手齿羽爪目头耳舌面足鼻画刀车网书矛串纸门弓舟油图国赤黑白红黄蓝紫灰',MSZfont,'hanzi')













