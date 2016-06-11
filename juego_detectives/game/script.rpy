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

image ik="Ikaros_chibi.png"


# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.

define d = Character ('Detective', color="#8B4513")
define a = Character ('Art', color="#C0C0C0")
define b = Character ('Burt', color="#9932CC")
define c = Character ('Carl', color="#4169E1")
define i= Character ('Ikaros',color="#FA5882")


# - El juego comienza aquí.
label start:
    
    scene primer fondo 
    play music "Digimon Tamers OST #28 - Blue Card.mp3" 

    d "Soy un reconocido detective, que resuelve todo tipo de crimenes, y hoy estoy en una pesquisa de un suceso que ha sido noticia"
    show detective1 with dissolve
    
    d " Se hizo el horripilante hallazgo de un cadáver a las afueras de un pueblo pacífico..."
   
    d "El móvil del crimen, fue un femicidio."
    scene segundo fondo with fade 
    show detective2 at right with dissolve
    
    d "El cuerpo de la víctima se encontró con indicios de asesinato y a partir de ellas encontraré al victimario."
    scene tercer fondo with fade
    show detective2 at right with dissolve
    

    d "A partir de las evidencias encontradas en el lugar de los hechos, pude dar con tres supuestos implicados."
     
  
    d"Los tres implicados corresponden a los nombres de Art, Burt y Carl."
    scene cuarto fondo with fade
   
    
    d "Cada implicado a sido arrestado provisionalmente, mientras dure las investigaciones pertinentes."
    
    d "El primer sospechoso en declarar fue Art."
    
    d "El sospechoso declaró a la fiscalía lo siguiente:"
    show art1 at right with dissolve
    
    a "¡Burt es amigo de la victima!..."
    
    a "Carl y la victima son enemigos a muerte..."

    hide art1   
    show detective3 with dissolve
    d "La declaración hecha por el primer sospechoso, involucró aún más a los otros implicados."

    d "Sin embargo, Burt y Carl aún deben ser indagados por la fiscalia."

    d "El segundo implicado, Burt, tiene rostro de pocos amigos."

    d "Pero, en su semblante se ve su inteligencia fria."

    hide detective3
    show burt1 with dissolve
    b "¡Yo no hice nada!"

    b "Yo estaba en las afueras...."

    b "¡No conozco a la víctima!"

    hide burt1
    show detective3 with dissolve
    d "Pude notar a Burt, notablemente nervioso y angustiado al dar su versión de los hechos."

    d "Pero es normal esto, y he visto muchas veces esto en mi tiempo como detective."

    d "Ahora solo queda escuchar la explicación del ultimo victimario, Carl"

    d "Ya con esta declaración, podre dar con el actor del crimen..."

    d "No obstante, necesito encajar las piezas de este rompecabezas"
    
    hide detective3
    show carl1 with dissolve
    c "¡Soy inocente!"
    
    c "Pero vi a Art y a Burt saliendo del pueblo"
    
    hide carl1
    scene quinto fondo
    show detective2 at right with dissolve
    
    d "Con las declaraciones que los tres implicados han dado"
    
    d "Procederé a deducir, quien de ellos está mintiendo"
    
    d "Pero para lograr esto, analizaré cada declaración"

    d "Primero tenemos a Art que manifestó:"

    hide detective2
    show art1 at right with dissolve
    
    a "¡Burt es amigo de la victima!..."
    
    a "Carl y la victima son enemigos a muerte..."
    
    hide art1
    show burt1 at right with dissolve
    show vict1 at left with dissolve 
    
    d "Art dice que Burt es amigo cercano de la victima"
    hide burt1
    hide vict1
    show carl2 with dissolve
    
    d "Pero tambien cuenta que Carl y la victima no se llevaban"
    
    hide carl2
    show detective2 at right with dissolve
    d "Esto reduce las pistas a dos sospechosos, pero esto no significa que Art no esté envuelto en esto"
    
    d "Muy bien, ahora analizaré lo que Burt, explicó"
   
    scene sexto fondo with fade
    hide detective2
    show burt2 with dissolve
    b "¡Yo no hice nada, Yo estaba en las afueras, No conozco a la víctima!"


    hide burt2
    show detective3 with dissolve
    d "Esta declaración me recuerda a la frase, por la boca muere el pez"
 
    d "Si el crimen se cometió en las afueras, que hacía el señor Burt allá???"

    d "Por último analizaré el ultimo testimonio brindado por Carl"

    hide detective3
    show carl1 with dissolve
    c "¡Soy inocente!"
    
    hide carl1
    show burt1 at left with dissolve
    show art1  at right with dissolve
    c "Pero vi a Art y a Burt saliendo del pueblo"

    d "Con estas ultimas declaraciones, puedo deducir que Art y Burt, tienen que ver mucho en este crimen, al lado de Carl"

    scene octavo fondo with fade
    hide burt1
    hide art1
    d "Pero para poder dar con el autor de éste crimen, recurriré al terminal de Ubuntu"

    d "Ikaros, es un IA que inculpa a cualquier criminal, a partir de sus declaraciones"

    show ik at right with dissolve
    i "Bienvenido estimado detective, por favor ingrese las declaraciones de los implicados en el crimen actual" 

    i "Recuerde separar cada sentencia con punto al final, para que yo no cometa ningún error de compilación"

    scene noveno fondo
    hide ik
    show ik at right with dissolve 
    
    python:
                from pyswip import Prolog
                prolog = Prolog()
                prolog.consult('/home/ikaros/Documentos/adriandetective.pl')
                asesino = list(prolog.query('murderer(X)'))
                i("El culpable de este homicidio es %s"%asesino[0]['X'])
                

    scene quinto fondo
    hide ik
    show detective4

    d "Gracias Ikaros, parece que tenemos gato encerrado"

    scene decimo fondo with dissolve
    hide detective4
    show burt2 with dissolve

    b "Maldito detective de los cojones, nunca me hubieses descubierto si la ayuda de la inepta de Ikaros"

    b "Juro que la pagarás caro, tú y tu asquerosa familia"

    hide burt2
    show detective4 with dissolve

    d "jajajajajajaja, ahora pasarás el resto de tus días encerrado y recuerda, el crimen jamás ganará"

    scene ultimo fondo
    
    "FIN"
    


    

    
    

    return
