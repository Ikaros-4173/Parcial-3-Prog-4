﻿#fondos usados.
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
image duodecimo fondo="sala_interrogatorio.jpg"
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

image pol1="jefe-gorgori.png"
image pol2="wiggum.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.

define d = Character ('Detective', color="#8B4513")
define a = Character ('Art', color="#C0C0C0")
define b = Character ('Burt', color="#9932CC")
define c = Character ('Carl', color="#4169E1")
define i = Character ('Ikaros',color="#FA5882")
define s= Character ('Asistente',color="#B45F04")
define p= Character ('Policia',color="#FFFF00")

# - El juego comienza aquí.
label start:
    
    scene primer fondo with fade 
    play music "Digimon Tamers OST #28 - Blue Card.mp3"
    
    d "La vida puede tener muchos riesgos, y más si tienes un trabajo como el mío"
    
    show detective3 with dissolve
    d "Me dedico al peligroso, pero emocionante oficio de investigador privado"
    d "Durante mis años de carrera, he resuelto numerosos crímenes de toda índole"
    d "Y hoy, llegó un nuevo crimen a mi despacho"
    
    hide detective3
    
    scene undecimo fondo with fade
    
    show asis1 at right with dissolve
    
    s "Buenos días jefe, le ha llegado un nuevo trabajo..."
    
    hide asis1
    
    show detective2 with dissolve
    
    d "¿Otro trabajo?"
    
    hide detective2
    
    show asis1 at right with dissolve
    
    s "Para eso eres un detective, pero vayamos al grano"
    s "Ocurrió un horrendo asesinato en el pueblo"
    
    hide asis1
    
    show detective2 with dissolve
    
    d "Maldición, cada vez hay más crimenes por el hampa"
    
    hide detective2
    
    show asis1 at right with dissolve
    
    s "Lo más triste fue el móvil del asesinato..."
    s "Dígame como cree que fue el crimen"
    
    hide asis1
    
    show detective1 with dissolve
    
    menu:
        "fue un robo.":
    
             s "Si fuera el móvil un robo, la escena no fuera tan sangrienta"   
    
      
        "fue un femicidio.":
   
             s "Un hombre sin cojones sólo haría esto, y esta vez tendrás que investigar este crimen"
         

        "fue un accidente.":
    
             s "Este pueblo es muy pacífico para que ocurra hecho así"
             s "Sin embargo, si fuese un accidente, el culpable no se hubiese dado a la fuga"
            
    hide detective1
     
    show asis1 with dissolve      
    
    s "Ya dejemos las preguntas de un lado, lo que importa es que debo resolver otro crimen"
    s "exactamente, el crimen ocurrió en las afueras del pueblo, y necesitamos todas las pistas posibles"
    s "Así encontraremos al perpetrador de esto"

    hide asis1


    scene tercer fondo with fade

    show detective3 with dissolve

    d "Después de conversar con mi asistonta, me dirigí hacia el lugar de los hechos."
    d "Las dudas que tengo son: ¿Porqué la mataron? y ¿Quien hizo esto?"
    d "Pero saldré de esta duda cuando vea las pistas en la escena."

    hide detective2
    scene segundo fondo with fade
    
    show detective3 with dissolve

    d "Al llegar a la escena, vi que estaba acordonada y el cadáver yacía en el pavimento."
    d "Al cruzar la línea amarilla, un policía encargado del caso me explica lo ocurrrido."     

    hide detective3
    show pol1 with dissolve 

    p "Alto ahí, identifíquese!!!"

    hide pol1

    show detective3 with dissolve

    d "Soy detective del ministerio público y tengo toda la autorización de esta aquí"
    d "Dígame que ocurrió aquí?"

    hide detective3

    show pol2 with dissolve

    p "Testigos del área circundante, afirmaron escuchar disparos"
    p "Después de eso, un chaval encuentra a la victima en el suelo"
    p "Intentó socorrerla, pero ya no tenía signos vitales"

    hide pol2

    show detective3 with dissolve

    d "Y encontraron algun indicio, pista, o algo similar???"

    hide detective3

    show pol2 with dissolve

    p "Pudimos encontrar varios casquillos de bala y un revolver calibre 38"
   
    hide pol2

    show detective2 with dissolve

    d "Excelente, con esa pista podré dar con el perpetrador del crimen" 
 
    hide detective2

    scene sexto fondo

    show detective3 with dissolve

    d "Después del levantamiento del cádaver, tomé un casquillo de bala como prueba"
    d "Y con éste, haré un análisis para determinar si existe alguna huella digital"
    d "Hoy será una noche larga porque debo hallar al culpable"

    hide detective3

    scene duodecimo fondo

    d "Al caer la noche, me puse a analizar minusiosamente ese casquillo"
    d "Mediante métodos de alta tecnología, deduzco al culpable"

    show detective4 with dissolve

    d "Ajaa!, encontré huellas digitales, esto será de mucha ayuda"
    d "Ahora, podré deducir quien es el victimario de ello"
    d "Pero para tener una conclusión deberé repasar lo ocurrido en este crimen"
    d "Bueno comenzaré"

    hide detective4
    
    show detective3 with dissolve

    d "Dónde ocurrió el crimen suscitado?"
    menu:
        "En el centro del pueblo":
               jump centro
        "En las afueras del pueblo":
               jump afueras

    label centro:
    d "Donde yacía el cadáver de la victima??"
    menu:
       "En el pavimento de la calle":
           jump calle
       "En un terreno baldio":
           jump terreno
    
    label afueras:
    d "Quien fue la victima del mismo?"
    menu:
        "Un hombre":
            jump hombre
        "Una mujer":
            jump mujer
    
    
    
    return 
    
    
    
    
    
  
