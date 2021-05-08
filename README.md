# Open Glyph Generator
These scripts generate a large number of simple, visually distinct, open-license images.

After watching [this video by Matt Parker](https://www.youtube.com/watch?v=VTDKqW_GLkw), I was inspired to make my own version of "Myriad Monomatch" using only open-license images.


**Problem:** I need over 10,000 such images to make the cards.

**Solution:** Unicode fonts already contain many visually distinct glyphs. So I multiply several-hundred characters from open fonts with a set of backgrounds I made myself.

Varying colors are added as an extra source of visual distinction, but are not themselves used to distinguish between glyphs. That is, there isn't a pair of glyphs with the same background and character.



## Examples

Here are some examples of output from version 2 of the generator, which outputs PNG images.

<table><tr><td>
<img src="v2-PythonPIL/output/blob-TDchrome-34.png" width="80">
<img src="v2-PythonPIL/output/blob-TDchrome-34.png" width="80">
<img src="v2-PythonPIL/output/blob-TDchrome-34.png" width="80">
<img src="v2-PythonPIL/output/blob-TDchrome-34.png" width="80">
<img src="v2-PythonPIL/output/blob-TDchrome-34.png" width="80">
<img src="v2-PythonPIL/output/blob-TDchrome-34.png" width="80">
<img src="v2-PythonPIL/output/blob-TDchrome-34.png" width="80">
<img src="v2-PythonPIL/output/blob-TDchrome-34.png" width="80">
</td></tr></table>


Here are some examples of output from version 1 of the generator, which outputs vector graphics. These may not display properly if you don't have the right fonts installed. 

<table><tr><td>
<img src="v1-SVGfill/outputvectors/glyph3-127.svg" width="80">
<img src="v1-SVGfill/outputvectors/glyph4-147.svg" width="80">
<img src="v1-SVGfill/outputvectors/glyph5-28.svg" width="80">
<img src="v1-SVGfill/outputvectors/glyph2-400.svg" width="80">
<img src="v1-SVGfill/outputvectors/glyph1-299.svg" width="80">
<img src="v1-SVGfill/outputvectors/glyph6-36.svg" width="80">
<img src="v1-SVGfill/outputvectors/glyph7-99.svg" width="80">
<img src="v1-SVGfill/outputvectors/glyph8-536.svg" width="80">
</td></tr></table>

---

## Licensing and Attribution.


### Images
All generated images in this repo are usable under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/), 
meaning you can use them in any way you like as long as you provide attribution and link to the license. 
Something like the following in a readme will suffice:

> Copyright 2021 Robert Winslow, CC-BY-4.0

_Of course, many of the resulting images are things like 'yellow square with a big S on it', and are too simple to individually fall under copyright, but attribution would be appreciated nonetheless._

### Color Schemes Used
- [Paul Tol's colorblind friendly color schemes.](https://personal.sron.nl/~pault/)
- [Paul Centore's conversion of Munsell centroids into RGB](https://www.munsellcolourscienceforpainters.com/ISCCNBS/ISCCNBSSystem.html)


### Fonts used

The generated images make use of the following typefaces:
- [Quivira 4.1](http://www.quivira-font.com/), kindly released by Alexander Lange into the public domain 
- [Ma Shen Zheng](https://fonts.google.com/specimen/Ma+Shan+Zheng#glyphs), used under the [Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL)
- Computer Modern by Donald Knuth, used under the [Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL)


