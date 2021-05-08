
for %%f in (%*) do (
    echo %%~f
    "C:\Program Files\InkscapeAlpha\inkscape.exe" ^
      -z ^
      --export-background-opacity=0 ^
      --export-height=512 ^
      --export-png="%%~dpnf.png" ^
      --file="%%~f"

)