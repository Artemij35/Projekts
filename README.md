# Projekts : Automatizēta e-pasta plānotājs

Šis Python skripts ir izstrādāts, lai automatizētu e-pasta plānošanas un sūtīšanas procesu, izmantojot schedule bibliotēku un smtplib e-pasta funkcionalitātei.
Skripts ļauj lietotājiem ievadīt nepieciešamos datus, piemēram, saņēmēja e-pasta adresi, e-pasta temu un tekstu.

,,Funkcijas :,,
Automatizēta e-pasta plānošana: Skripts izmanto schedule bibliotēku, lai automatizētu e-pasta sūtīšanas plānošanu. Lietotāji var norādīt datumu un laiku, kad vēlas nosūtīt e-pastu, un skripts pārvaldīs plānošanu.
Lietotājam draudzīgs ievads: Skripts lietotājam piedāvā ievadīt saņēmēja e-pasta adresi, e-pasta temu un e-pasta tekstu, padarot to ērtu un interaktīvu.
Droša e-pasta autentifikācija: Skripts izmanto smtplib bibliotēku, lai izveidotu drošu savienojumu ar Gmail SMTP serveri. 
Autentifikācijai nepieciešama sūtītāja e-pasta adrese un parole.

,,Izmantotās bibliotēkas:,,

schedule:
Pielietojums: Bibliotēka schedule tiek izmantota, lai automatizētu procesu, plānojot uzdevumus atbilstoši iepriekš noteiktajam laika grafikam. Šajā projektā tā nodrošina iespēju plānot un automātiski nosūtīt e-pastu saskaņā ar lietotāja ievadīto laiku.
Iemesls izmantošanai: schedule ir ērta un vienkārša bibliotēka, kas ļauj izveidot notikumu plānotāju ar minimālu kodu. Tā ir noderīga, lai izpildītu darbības periodiski vai noteiktos laika punktos.
smtplib:
Pielietojums: smtplib tiek izmantota e-pasta sūtīšanai, nodrošinot saskarni ar SMTP (Simple Mail Transfer Protocol) serveri. Šī bibliotēka palīdz nodrošināt drošu savienojumu un veikt e-pasta autentifikāciju.
Iemesls izmantošanai: smtplib ir standarta bibliotēka Python, kas piedāvā vienkāršu un efektīvu veidu, kā sūtīt e-pastu no skripta, izmantojot SMTP protokolu.
email.mime.text un email.mime.multipart:
Pielietojums: Šīs bibliotēkas, kas ir daļa no email pakotnes, tiek izmantotas, lai izveidotu MIME (Multipurpose Internet Mail Extensions) formāta ziņu ar teksta un vairāku daļu iekļaušanu, piemēram, teksta un pielikumiem.
Iemesls izmantošanai: email.mime bibliotēkas nodrošina iespēju veidot struktūrizētas e-pasta ziņas, kas var saturēt gan tekstu, gan pielikumus. Tas ir noderīgi, lai veidotu kompleksākus e-pastus ar dažādām daļām.

,,Instalācija:,,
Pirms sākt lietot šo programmatūru, pārliecinieties, ka jums ir uzstādītas nepieciešamās Python bibliotēkas. To var izdarīt, izmantojot komandu:pip install schedule
,,Skripta palaišana:,,
Palaidiet skriptu, izmantojot Python interpretatoru. To var izdarīt, izpildot šo komandu:python email_scheduler.py
,,Ievades dati:,,
Skripts jautās jums par nepieciešamajiem ievades datiem, tai skaitā saņēmēja e-pasta adresi, e-pasta tēmu un tekstu. Ievadiet šos datus, kad tiks pieprasīts.
,,Autentifikācija:,,
Kad pieprasīts, ievadiet sūtītāja e-pasta adresi un paroli. Tas nodrošina drošu savienojumu ar Gmail SMTP serveri, lai nodrošinātu e-pasta sūtīšanu.
,,Izpilde:,,
Pēc ievades datu un plānošanas iestatīšanas skripts autonomi pārvalda sūtīšanas procesu. Tas automātiski nosūta e-pastu 
