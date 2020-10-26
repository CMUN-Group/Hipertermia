@echo off 
title Makefile Maison

SET STR=main

echo Vous souhaitez compiler le document ? y/n
set /p sel1=
if %sel1% == y call :compile else (call :cobarde)
if %sel1% == n call :cobarde else (call :cobarde)

echo 
echo 
echo 

echo Voulez-vous que je supprime la poubelle ? y/n

set /p sel2=
if %sel2% == y call :eliminar else (call :comentarioElocuente) 
if %sel2% == n call :comentarioElocuente else (call :comentarioElocuente)

echo Quitter le programme
pause >nul
exit 

:compile
echo Je vais proceder a la compilation du document
pdflatex "%STR%.tex"
makeglossaries "%STR%"
makeindex "%STR%.idx" -s "StyleInd.ist"
biber "%STR%"
pdflatex "%STR%.tex"
goto :eof

:cobarde
echo J'espere que vous passez une bonne journee
goto :eof

:eliminar
echo Je vais proceder a supprimer la poubelle
DEL "%STR%.log"
DEL "%STR%.toc"
DEL "%STR%.aux"
DEL "%STR%.out"
DEL "%STR%.blg"
DEL "%STR%.bbl"
goto :eof

:comentarioElocuente
echo J'espere que vous passez une bonne journee
goto :eof
