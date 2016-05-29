#fondos usados.
image primer fondo="ciudad.png"
image segundo fondo="victimamuerta.png"
image tercer fondo="fuera_del_pueblo3.png"
image cuarto fondo="Silla de interrogatorio.jpg"
image quinto fondo="sala_interrogatorio2.jpg"
image sexto fondo="fuera_del_pueblo2.jpg"
image septimo fondo="fuera_del_pueblo1.jpg"
image octavo fondo="terminal.jpg"
image noveno fondo="captura.jpg"
image decimo fondo="cadeia4.jpg"
image undecimo fondo="sala_interrogatorio3.jpg"
image ultimo fondo="fin.jpg"
                    
#personajes.
image detective1="DetectiveEnoo.png"
image detective2="DetectivePruevass.png"
image detective3="Detectivee.png"
image detective4="DetectiveAjja.png"

image art1="Hablandoo 2.png"

image burt1="Captura de pantalla (113).png"
image burt2="hablando11.png"

image carl1="yonofui.png"
image carl2="Felizz.png"


image vict1="la foto2.png"

image asis1="20091115001443!Midori_Kuriyama_Profile.png"
image asis2="default_midori-kuriyama.png"

image ik="Ikaros_chibi.png"


# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.

define d = Character ('Detective', color="#8B4513")
define a = Character ('Art', color="#C0C0C0")
define b = Character ('Burt', color="#9932CC")
define c = Character ('Carl', color="#4169E1")
define i= Character ('Ikaros',color="#FA5882")
define as= Character ('Asistente',color="#B45F04")


# - El juego comienza aquí.
label start:
    
    scene primer fondo with fade 
    play music "Digimon Tamers OST #28 - Blue Card.mp3"
    
    d "La vida puede tener muchos riesgos, y más si tienes un trabajo como el mío"
    
    show detective3 with dissolve
    d "Me dedico al peligroso, pero emocionante oficio de investigador privado"
    d "Durante mis años de carrera, he resuelto numerosos crímenes de toda índole"
    d "Y hoy, llegó un nuevo crimen a mi despacho"
    
    hide show detective3
    
    scene undecimo fondo with fade
    
    show asis1 at right with dissolve
    
    as "Buenos días jefe, le ha llegado un nuevo trabajo..."
    
    hide asis1
    
    show detective2 with dissolve
    
    d "¿Otro trabajo?"
    
    hide detective2
    
    show asis1 at right with dissolve
    
    as "Para eso eres un detective, pero vayamos al grano"
    as "Ocurrió un horrendo en asesinato en el pueblo"
    
    hide asis1
    
    show detective2 with dissolve
    
    d "Maldición, cada vez hay más crimenes por el hampa"
    
    hide detective2
    
    show asis1 at right with dissolve
    
    as "Lo más triste fue el móvil del asesinato..."
    as "Dígame como cree que fue el crimen"
    
    hide asis1
    
    show detective2 with dissolve
    
    menu:
        "fue un robo.":
         jump rb
         
        "fue un femicidio.":
         jump fem
         
        "fue un homicidio.":
         jump hom    
    
    
    
    
  
