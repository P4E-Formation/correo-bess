# -*- coding: utf-8 -*-
import sys, urllib.parse
BASE = sys.argv[1] if len(sys.argv) > 1 else "img/"
OUT = sys.argv[2] if len(sys.argv) > 2 else "correo-bess.html"
if not BASE.endswith("/"): BASE += "/"

AZUL = "#0A75BC"; MARINO = "#1F3A6E"; CLARO = "#EAF2FB"; TXT = "#2B3440"; GRIS = "#6B7480"
FONT = "Arial, Helvetica, sans-serif"
WA = "https://wa.me/51997668631?text=" + urllib.parse.quote(
    "Hola, deseo información sobre el Programa de Capacitación Híbrido en Sistemas Fotovoltaicos y BESS (precio y reunión).")

def img(n, w, alt, extra=""):
    return f'<img src="{BASE}{n}" width="{w}" alt="{alt}" style="display:block;border:0;outline:none;text-decoration:none;height:auto;{extra}">'

def boton(txt, href, color=AZUL):
    return f'''<table role="presentation" align="center" border="0" cellspacing="0" cellpadding="0"><tr>
<td align="center" bgcolor="{color}" style="background-color:{color};border-radius:6px;padding:14px 34px;">
<a href="{href}" target="_blank" style="font-family:{FONT};font-size:16px;font-weight:bold;color:#ffffff;text-decoration:none;display:inline-block;">{txt}</a>
</td></tr></table>'''

def titulo(t, sub=""):
    s = f'<p style="margin:6px 0 0 0;font-family:{FONT};font-size:14px;line-height:21px;color:{GRIS};">{sub}</p>' if sub else ""
    return f'''<tr><td style="padding:34px 30px 6px 30px;" align="center">
<p style="margin:0;font-family:{FONT};font-size:12px;letter-spacing:2px;font-weight:bold;color:{AZUL};text-transform:uppercase;">&nbsp;</p>
<h2 style="margin:0;font-family:{FONT};font-size:24px;line-height:30px;color:{MARINO};font-weight:bold;">{t}</h2>
<table role="presentation" align="center" border="0" cellspacing="0" cellpadding="0" style="margin-top:10px;"><tr><td width="60" height="4" bgcolor="{AZUL}" style="background-color:{AZUL};font-size:0;line-height:0;">&nbsp;</td></tr></table>{s}
</td></tr>'''

# ---- Por qué ----
porque = [
 ("Visión integral", "de la ingeniería, el análisis financiero y la operación comercial de sistemas fotovoltaicos y BESS."),
 ("Aprendizaje flexible", "con contenido asíncrono, sesiones en vivo y taller práctico."),
 ("Alcance regional", "con casos reales y soluciones prácticas de comisionado."),
 ("Docentes de alto prestigio", "en Latinoamérica."),
 ("100% virtual", "para llevarlo desde cualquier país."),
 ("Networking internacional", "con profesionales del sector."),
]
porque_html = "".join(f'''<tr><td width="34" valign="top" style="padding:7px 0;"><table role="presentation" border="0" cellspacing="0" cellpadding="0"><tr><td width="24" height="24" align="center" bgcolor="#ffffff" style="background-color:#ffffff;border-radius:12px;font-family:{FONT};font-size:13px;font-weight:bold;color:{AZUL};">{i}</td></tr></table></td>
<td valign="top" style="padding:7px 0;font-family:{FONT};font-size:15px;line-height:22px;color:#ffffff;"><b>{a}</b> {b}</td></tr>''' for i,(a,b) in enumerate(porque,1))

# ---- Módulos ----
mods = [
 ("1","Aplicaciones de BESS","Fuentes de ingreso, modelos de aplicación, evaluación de riesgos, dimensionamiento y simulación de escenarios con visión técnica y financiera.","modulo1.png"),
 ("2","BESS-Mercados","Fundamentos eléctricos, arquitectura y criterios de diseño de BESS e híbridos en el contexto latinoamericano, con casos reales.","modulo2.png"),
 ("3","Gestión de Ingeniería BESS + FV","De la oportunidad de negocio a la operación: selección tecnológica, presupuestos, gestión EPC y control de riesgos.","modulo3.png"),
 ("4","Diseño híbrido con HOMER Pro","Viabilidad técnica y económica de proyectos híbridos: NPC, CAPEX, OPEX, sensibilidad y comparación de alternativas.","modulo4.jpg"),
 ("5","Diseño y operación de Sistemas Fotovoltaicos","Recurso solar, componentes, instalación, operación y mantenimiento de plantas solares para maximizar su desempeño.","modulo5.png"),
 ("6","Comisionamiento de BESS","Protocolos de pruebas, verificación de seguridad e interconexión, desde la inspección previa hasta la entrega operativa.","modulo6.jpg"),
]
def mod_row(n,t,d,im,flip):
    pic = f'<td width="170" valign="middle" align="center" style="padding:14px;">{img(im,142,"Módulo "+n)}</td>'
    txt = f'''<td valign="middle" style="padding:16px 18px;"><p style="margin:0 0 4px 0;font-family:{FONT};font-size:12px;font-weight:bold;letter-spacing:1px;color:{AZUL};">MÓDULO {n}</p>
<p style="margin:0 0 6px 0;font-family:{FONT};font-size:17px;line-height:22px;font-weight:bold;color:{MARINO};">{t}</p>
<p style="margin:0;font-family:{FONT};font-size:14px;line-height:21px;color:{TXT};">{d}</p></td>'''
    cells = (txt+pic) if flip else (pic+txt)
    return f'''<tr><td style="padding:0 24px 12px 24px;"><table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="{CLARO}" style="background-color:{CLARO};border-radius:10px;"><tr>{cells}</tr></table></td></tr>'''
mods_html = "".join(mod_row(*m, i%2==1) for i,m in enumerate(mods))

# ---- Agenda ----
def ag(fecha, curso, doc, tag, bg):
    return f'''<tr><td width="112" valign="middle" bgcolor="{bg}" style="background-color:{bg};padding:12px 14px;border-bottom:3px solid #ffffff;font-family:{FONT};font-size:15px;line-height:19px;font-weight:bold;color:{MARINO};">{fecha}</td>
<td valign="middle" bgcolor="{bg}" style="background-color:{bg};padding:12px 14px;border-bottom:3px solid #ffffff;font-family:{FONT};font-size:14px;line-height:19px;color:{TXT};"><b style="color:{MARINO};">{curso}</b><br><span style="color:{GRIS};">{doc}</span><br><span style="font-size:12px;color:{AZUL};font-weight:bold;">{tag}</span></td></tr>'''
def sec(t):
    return f'<tr><td colspan="2" bgcolor="{MARINO}" style="background-color:{MARINO};padding:9px 14px;font-family:{FONT};font-size:13px;letter-spacing:1px;font-weight:bold;color:#ffffff;">{t}</td></tr>'
B = "#F3F7FC"
agenda = (sec("BLOQUE DE CURSOS SÍNCRONOS (EN VIVO)") +
 ag("5 de octubre","Aplicaciones de Sistemas BESS","Mg. Ing. Juan Montoya · Ing. Emilio Grandy","Inicio del programa",B) +
 ag("27 de octubre","Dimensionamiento y Diseño de Sistemas de Almacenamiento","Ing. Héctor Arámbulo · Ing. Yerson García","Síncrono",B) +
 ag("29 de octubre","Diseño híbrido con HOMER Pro","Ing. Yerson García","Síncrono",B) +
 ag("30 de noviembre","Taller de comisionado en Sistemas BESS","Ing. Eliezer Barrientos","Taller práctico",B) +
 sec("BLOQUE DE CURSOS ASÍNCRONOS (CON SESIÓN EN VIVO DE 2 H)") +
 ag("29 de septiembre","BESS y Sistemas Híbridos en LATAM","Mg. Lucas Ponce","Sesión en vivo realizada · contenido grabado",B) +
 ag("15 de octubre","Diseño y operación de Sistemas Fotovoltaicos","MBA Ing. Guillermo Rubiano","Sesión en vivo",B) +
 ag("20 de octubre","Gestión financiera en Sistemas de Almacenamiento","Mg. Ing. Jorge Servan","Sesión en vivo",B))

# ---- Especialistas ----
esp = [
 ("jorge-servan.png","Mg. Ing. Jorge Servan","Gerente Comercial, TESGA Energy","Perú"),
 ("juan-montoya.png","Mg. Ing. Juan Montoya","Jefe de Planeamiento de Mercado, CELEPSA","Perú"),
 ("emilio-grandy.png","Ing. Emilio Grandy","Project and Engineering Manager, CELEPSA","Perú"),
 ("lucas-ponce.png","Mg. Lucas Ponce","Product &amp; Solution Manager, CATL","Argentina"),
 ("guillermo-rubiano.png","MBA Ing. Guillermo Rubiano","Gerente Técnico para Latinoamérica, JA Solar","Colombia"),
 ("hector-arambulo.png","Ing. Héctor Arámbulo","Gerente General, Planning for Evolution","Perú"),
 ("eliezer-barrientos.png","Ing. Eliezer Barrientos","Especialista en puesta en servicio de sistemas BESS","Perú"),
 ("yerson-garcia.png","Ing. Yerson García","Proyectos eléctricos en media tensión y estudios eléctricos","Perú"),
]
def card(e):
    f,n,c,p = e
    return f'''<td width="50%" valign="top" align="center" style="padding:10px 8px 16px 8px;">
{img(f,110,n,"margin:0 auto;")}
<p style="margin:10px 0 2px 0;font-family:{FONT};font-size:15px;line-height:19px;font-weight:bold;color:{MARINO};">{n}</p>
<p style="margin:0;font-family:{FONT};font-size:13px;line-height:18px;color:{TXT};">{c}</p>
<p style="margin:2px 0 0 0;font-family:{FONT};font-size:12px;color:{GRIS};">{p}</p></td>'''
esp_html = "".join(f'<tr>{card(esp[i])}{card(esp[i+1])}</tr>' for i in range(0,8,2))

html = f'''<!DOCTYPE html>
<html lang="es" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<title>Programa de Capacitación Híbrido: Sistemas Fotovoltaicos y BESS</title>
<!--[if mso]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
<style>
body,table,td,a{{-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}}
table,td{{mso-table-lspace:0pt;mso-table-rspace:0pt;}}
img{{-ms-interpolation-mode:bicubic;}}
@media only screen and (max-width:620px){{
 .wrap{{width:100% !important;}}
 .stack{{display:block !important;width:100% !important;}}
}}
</style>
</head>
<body style="margin:0;padding:0;background-color:#F4F6F8;">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;font-size:1px;line-height:1px;color:#F4F6F8;">6 módulos, 8 expertos y 70 horas de certificación. Inicio: 5 de octubre. 100% virtual.</div>
<table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#F4F6F8" style="background-color:#F4F6F8;"><tr><td align="center" style="padding:20px 10px;">
<!--[if mso]><table role="presentation" width="600" align="center" border="0" cellspacing="0" cellpadding="0"><tr><td><![endif]-->
<table role="presentation" class="wrap" width="600" border="0" cellspacing="0" cellpadding="0" bgcolor="#ffffff" style="width:600px;max-width:600px;background-color:#ffffff;">

<tr><td align="center" style="padding:22px 20px;">{img("logo-p4e.png",230,"Planning for Evolution","margin:0 auto;")}</td></tr>

<tr><td>{img("portada-bess.jpg",600,"Sistema de almacenamiento de energía BESS","width:100%;max-width:600px;")}</td></tr>

<tr><td align="center" bgcolor="{MARINO}" style="background-color:{MARINO};padding:30px 30px 26px 30px;">
<p style="margin:0 0 8px 0;font-family:{FONT};font-size:13px;letter-spacing:2px;font-weight:bold;color:#8FC8F2;">PROGRAMA DE CAPACITACIÓN HÍBRIDO</p>
<h1 style="margin:0;font-family:{FONT};font-size:26px;line-height:33px;color:#ffffff;font-weight:bold;">Diseño, operación, análisis financiero y comisionado de sistemas fotovoltaicos y BESS</h1>
</td></tr>

<tr><td bgcolor="{AZUL}" style="background-color:{AZUL};padding:16px 10px;">
<table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0"><tr>
<td width="33%" align="center" style="font-family:{FONT};color:#ffffff;"><span style="font-size:26px;font-weight:bold;">6</span><br><span style="font-size:12px;letter-spacing:1px;">MÓDULOS</span></td>
<td width="34%" align="center" style="font-family:{FONT};color:#ffffff;border-left:1px solid #5BA6D9;border-right:1px solid #5BA6D9;"><span style="font-size:26px;font-weight:bold;">8</span><br><span style="font-size:12px;letter-spacing:1px;">EXPERTOS</span></td>
<td width="33%" align="center" style="font-family:{FONT};color:#ffffff;"><span style="font-size:26px;font-weight:bold;">70 h</span><br><span style="font-size:12px;letter-spacing:1px;">CERTIFICACIÓN</span></td>
</tr></table></td></tr>

<tr><td style="padding:28px 30px 8px 30px;font-family:{FONT};font-size:16px;line-height:25px;color:{TXT};text-align:left;">
Desde <b>Planning for Evolution</b>, lo invitamos a participar en el <b>Programa de Capacitación Híbrido en Sistemas Fotovoltaicos y BESS</b>, un espacio diseñado para dominar el diseño, la operación, la evaluación financiera y el comisionado de proyectos de almacenamiento de energía y generación solar.<br><br>
El programa inicia el <b>5 de octubre</b> y combina <b>clases en vivo, contenido asíncrono y un taller práctico</b>, en <b>modalidad 100% virtual</b>, con especialistas de Perú, Colombia y Argentina.
</td></tr>

<tr><td style="padding:14px 30px 8px 30px;">{boton("Quiero información por WhatsApp", WA)}</td></tr>

{titulo("¿Por qué llevar el programa?")}
<tr><td style="padding:16px 24px 8px 24px;"><table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="{AZUL}" style="background-color:{AZUL};border-radius:10px;"><tr><td style="padding:18px 22px;"><table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0">{porque_html}</table></td></tr></table></td></tr>

{titulo("Plan de estudios", "Seis módulos que cubren el ciclo completo de un proyecto FV + BESS.")}
<tr><td style="font-size:0;line-height:0;height:14px;">&nbsp;</td></tr>
{mods_html}

{titulo("Agenda", "Septiembre – noviembre · 70 horas cronológicas")}
<tr><td style="padding:16px 24px 6px 24px;"><table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0">{agenda}</table></td></tr>
<tr><td style="padding:6px 30px 0 30px;font-family:{FONT};font-size:12px;line-height:18px;color:{GRIS};">Cada curso asíncrono incluye una sesión en vivo de 2 horas con el ponente; el inscrito accede a las sesiones grabadas y debe revisarlas antes de la sesión en vivo. Todos los cursos quedan grabados en un repositorio durante 6 meses.</td></tr>

{titulo("Especialistas", "Docentes con trayectoria en proyectos solares y de almacenamiento en Latinoamérica.")}
<tr><td style="padding:14px 22px 0 22px;"><table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0">{esp_html}</table></td></tr>

<tr><td align="center" bgcolor="{CLARO}" style="background-color:{CLARO};padding:30px 30px 30px 30px;">
{img("certificado.jpg",300,"Certificación por 70 horas","margin:0 auto 18px auto;")}
<h2 style="margin:0 0 10px 0;font-family:{FONT};font-size:22px;line-height:28px;color:{MARINO};">Reserve su cupo</h2>
<p style="margin:0 0 20px 0;font-family:{FONT};font-size:15px;line-height:23px;color:{TXT};">Consulte por el precio y las modalidades de inscripción por WhatsApp. Podemos agendar una reunión para presentarle una oferta a su medida.</p>
{boton("Escribir por WhatsApp · 997 668 631", WA)}
</td></tr>

<tr><td align="center" style="padding:26px 30px 10px 30px;font-family:{FONT};font-size:13px;line-height:21px;color:{GRIS};">
<b style="color:{MARINO};">Planning for Evolution S.A.C.</b><br>
<a href="mailto:comercial@planning4evolution.com" style="color:{AZUL};text-decoration:underline;">comercial@planning4evolution.com</a><br>
WhatsApp: <a href="{WA}" style="color:{AZUL};text-decoration:underline;">+51 997 668 631</a><br>
YouTube: <a href="https://www.youtube.com/@academiaplanning" style="color:{AZUL};text-decoration:underline;">@academiaplanning</a>
</td></tr>
<tr><td align="center" style="padding:10px 30px 28px 30px;font-family:{FONT};font-size:11px;line-height:16px;color:#9AA2AD;">Si no desea recibir más información sobre nuestros programas, responda a este correo con la palabra BAJA.</td></tr>

</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr></table>
</body></html>'''
open(OUT, "w", encoding="utf-8").write(html)
print("OK", OUT, len(html))
