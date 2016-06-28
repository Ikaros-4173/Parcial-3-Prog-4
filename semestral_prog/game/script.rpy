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
image duodecimo fondo="sala_interrogatorio.jpg"
image ultimo fondo="fin.jpg"
                    
#personajes.
image detective1="DetectiveEnoo.png"
image detective2="DetectivePruevass.png"
image detective3="Detectivee.png"
image detective4="DetectiveAjja.png"

image art1="Hablandoo 2.png"
image art2="Felizz.png"
image art3="Sorprenndido.png"

image burt1="Captura de pantalla (113).png"
image burt2="hablando11.png"

image carl1="yonofui.png"
image carl2="sospechoso.png"


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
    d "Según la prueba de ADN hecha a la huella digital"
    d "El resultado corresponde a un sujeto llamado Art"
    d "¡Ya tengo al primer sospechoso!"
    
    hide detective4

    scene quinto fondo with fade 

    d "Con el descubrimiento del primer sospechoso."
    d "Ordeno la detención preventiva del primer implicado."
    d "El acusado deberá dar su versión de los hechos, para seguir con la investigación"
    
    show detective3 with dissolve
    
    d "En cuestión de horas, llega el acusado"
    d "Tiene un rostro de yo no fui, pero no debo confiarme del chaval"

    hide detective3 with dissolve
    
    show art3 with dissolve
    
    a "¡Soy inocente, no sé de que diablos me acusan!"
    a "Dejenme ir!"

    hide art3

    show detective4 with dissolve
    
    d "Nunca, nunca te dejaré ir, al menos que seas inocente"

    hide detective4

    show detective1 with dissolve
    d "Joven Art, se descubrió en unos casquillos sus huellas digitales"
    d "Casquillos de bala, que se usaron en el asesinato de una mujer"
    d "Digame, todo lo referente al caso"
    d "Todo lo que diga ahora, será usado en pro o en su contra"
    d "Si llega a dar datos falsos, le caerá todo el peso de la ley" 
    
    hide detective1

    show art1 at right with dissolve
    
    a "Yo conozco a dos tipos, que tuvieron contacto alguna vez con la occisa"
    a "Le juro por Dios, que no tengo que ver con esto!"

    hide art1

    show detective2

    d "¿Me podrías indicar quienes son aquellos involucrados"
    d "Si lo que dice, ayuda a la resolución del crimen"
    d "Usted quedará absuelto de los cargos"

    hide detective2

    show art1 at right with dissolve

    a "Esta bien, acepto el trato"
    a "Sus nombres son Burt y Carl"
    a "Ellos se llevaban con aquella mujer"
    a "Yo sólo la vi de vista con ellos, pero no tuve alguna relación amistosa"

    hide art1

    show detective4 with dissolve

    d "Excelente joven Art, ahora mismo daré la orden de captura a ellos"
    d "Pero no cante victoria, ellos deberán dar su declaración a la fiscalía"
    d "Igual que usted, y alguno de ellos es culpable, usted quedará libre"

    hide detective4

    show art1 at right with dissolve
   
    a "Esta bien, no hay ningún problema"

    hide art1 

    scene undecimo fondo with fade

    d "Así pasó la primera noche de investigación"
    d "Art pasó su noche en una celda preventiva"
    d "Mientras tanto los otros compinches fueron capturados"
    d "Uno de ellos deambulaba por la calle, como si nada hubiera ocurrido"
    d "Mientras que el otro, intentó darse a la fuga"
    
    show detective3 with dissolve

    d "Llegó el día de la verdad"
    d "Los otros sospechosos llegaron escoltados por policías"
    d "Cada implicado dará su versión de los hechos"
    d "Sumado a esto, un polígrafo grabará toda la indagatoria y nos dirá quien miente"
    
    hide detective3

    show detective2 with dissolve

    d "Señor Art, usted dará su versión de los hechos"
    d "Su declaración será grabada y usted estará conectado a un polígrafo"
    d "Este aparato nos dirá su inocencia del crimen"
    d "¿Está listo?"

    hide detective2

    show art1 at right with dissolve
    
    a "Estoy listo"

    hide art1

    show detective2 with dissolve

    d "¿Cual era la relación de los sospechosos con la víctima?"
        menu:
            "Burt y la victima se odiaban a muerte; Carl era amigo de la mujer":
                 jump didNotKnowVic
             "Burt era el mejor amigo de la victima, Carl y la victima era enemigos mortales":
                 jump KnewVic

        label didNotKnowVic
            d "Correcto, joven art, continuemos con la siguiente pregunta"
           
            python:
                from pyswip import Prolog
                prolog= Prolog()


   
       
 



    return 
    
    
    
    
    

