


init 990 image bg black = "bg/black.png"
init 990 image bg white = "bg/white.png"


define wake = Fade(2.0, 1.0, 3.0, color='#ffffff')
define pain = Fade(0.1, 0.0, 0.8, color='#de0000')
define flash = Fade(0.1, 0.0, 0.8, color='#ffffff')


init 990 image cg meeting = "cg/1.png"
init 990 image cg tentacles = "cg/2.png"
init 990 image cg undressing = "cg/3.png"
init 990 image cg shredding = "cg/4.png"
init 990 image cg shower = "cg/5.png"
init 990 image cg running = "cg/6.png"
init 990 image cg slime = "cg/7.png"
init 990 image cg swimsuits = "cg/8.png"
init 990 image cg wetclothes = "cg/9.png"
init 990 image cg underwear = "cg/10.png"
init 990 image cg darkmeeting = "cg/11.png"
init 990 image cg darkfinal = "cg/12.png"

init 990 image cg arguing = "cg/14.png"
init 990 image cg sayakaaction = "cg/15.png"
init 990 image cg hikariaction = "cg/16.png"
init 990 image cg slimeappears = "cg/18.png"
init 990 image cg eating = "cg/19.png"
init 990 image cg monsterappears = "cg/20.png"







define p = Character('Kenta', color="#c8ffc8")




define cg = Character('????', color="#ffc184")

define s = Character('Sayaka', color="#ffc184")




define tg = Character('????', color="#fbb5ba")

define h = Character('Hikari', color="#fbb5ba")




define dg = Character('????', color="#907aa1")

define y = Character('Yuzuki', color="#907aa1")




define dq = Character('????', color="#a00000")



define teacher = Character('Teacher', color="#c8ffc8")


label main_menu:
    play music "bgm/titleintro.ogg"
    queue music "bgm/titleloop.ogg"

    jump main_menu_screen

label start:


    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ qquit = False
    $ cookedpreviously = False

    $ hikari = 0
    $ sayaka = 0



    stop music fadeout 2.0
    scene bg black with wake
    with Pause(2.5)

    play music "bgm/ominousintro.ogg" fadein 2.0 
    queue music "bgm/ominousloop.ogg"

    "Jede Nacht ...{w} habe ich denselben Traum."

    "Jede Nacht ...{w} werde ich unweigerlich an diesen Ort zurückgebracht."

    "Und jeden Morgen wache ich auf, ohne mich an diesen Ort erinnern zu können.{w} Bis ich wieder einschlafe."

    "Keine Nacht ist vergangen, ohne dass mein Bewusstsein in diesen Abgrund gezogen wurde."

    "In diesem Gefilde mangelt es so sehr an Licht, dass ich nicht einmal meine Hand vor meinem Gesicht sehen kann."

    "Die Geräuschkulisse der Umgebung ist ebenso fehlend wie das Geräusch meiner Schritte. Selbst meine verzweifelten Schreie werden unverzüglich von der Dunkelheit verschluckt, sobald sie meinen Mund verlassen."

    "Ein Ödland des Nichts sozusagen.{w} Verbringt man eine längere Zeit hier, fängt man noch an, an seiner eigenen Existenz zu zweifeln."

    "Und trotz dieses erstickenden Gefühls, weiß ich, dass ich nicht allein bin."

    "Mich beobachtet etwas.{w} Mich verfolgt etwas.{w} Aus den Schatten."

    "Ich kann nicht mit Sicherheit sagen, was es ist, aber hin und wieder sehe ich etwas in der letzten Ecke meines Blickwinkels."

    "Ein Paar brennender, strahlender Augen, die auf mich fixiert sind.{w} Sie hassen mich.{w} Sie verabscheuen mich.{w} Eine überwältigende Ausstrahlung von Feindseligkeit geht von ihnen aus."

    "Ich weiß, dass sie nichts anderes wollen, als mich anzugreifen, aber irgendwas hält sie zurück.{w} Eine Kraft, die sie wahrlich verachten.{w} Es sind unsichtbare Ketten, die sie von ihrer Absicht abhalten und in ihren Bewegungen einschränken."

    "Anfangs, als ich anfing, von diesem Ort zu träumen, waren die Augen noch weit entfernt und sahen aus wie flimmernde Sterne."

    "Aber mit jeder Nacht, die verging, kamen sie näher, und das Leuchten der Augen wurde immer stärker.{w} Ich schätze, die Kraft, die sie zurückhielt, wird allmählich schwächer."

    "Was wird passieren, wenn mich ...{w} diese Augen ...{w} erreichen?{w} Ich erschaudere, wenn ich daran denke."

    "Ich weiß, es ist nur ein Traum, von daher sollte ich keine Angst haben ...{w} aber alles, was ich hier erlebe, ist so lebendig.{w} Keiner der Schleier, die man sonst aus einem Traum kennt, scheint hier zu existieren.{w} Ich nehme alles klar und deutlich wahr."

    "Ich kann die stagnierende, eiskalte Luft um mich herum spüren, weshalb mir immer wieder ein Schauer über den Rücken läuft."

    "Da ich so an diesen Traum gewöhnt bin, weiß ich, wie er enden wird.{w} Ich werde für eine scheinbare Ewigkeit durch die Dunkelheit waten und nie etwas finden, bis endlich der Morgen anbricht und mich aus diesem Albtraum reißt."

    "Zumindest ...{w} hat er für gewöhnlich so geendet."

    "Aber heute ist etwas anders."

    "Jene hasserfüllten Augen, die sich bisher aus meinem Blickfeld zu verstecken versuchten ...{w} sind plötzlich unmittelbar vor mir."

    "Sie waren noch nie zuvor so nahe.{w} Noch nie zuvor habe ich sie so sehr angestarrt."

    "Ihr durchdringender Blick fesselt mich am Boden fest und ein stechender Schmerz drängt sich durch mich hindurch.{w} Ich kann mich nicht bewegen.{w} Ich kann nicht atmen."

    "Und dann, aus der Dunkelheit heraus, breitet sich plötzlich ein schiefes Lächeln aus, welches genauso finster ist wie die Augen."

    stop music fadeout 8.0

    dq "So nah.{w} Ich kann die Freiheit wahrlich {i}schmecken{/i}.{w} ... Nicht mehr lang.{w} Genieße die Ruhe, solang du noch kannst, Junge, denn deine Tage sind gezählt."

    dq "Und dann wird sich alles ändern."

    scene bedroom day with wake

    "..."
    play music "bgm/everydayintro.ogg" fadein 2.0
    queue music "bgm/everydayloop.ogg"

    "Ugh.{w} Mein Kopf bringt mich noch um.{w} Diese Cluster-Kopfschmerzen sind echt unerträglich."

    "Jeden Morgen wache ich ungewollt auf. Dank eines Gefühls, das daran erinnert, als würde jemand mit einem Presslufthammer auf mein Gesicht schlagen."



    "{i}Klopf.{/i}"



    "{i}Klopf.{/i}"



    "{i}Klopf.{/i}"

    "Fast wie ein ...{w} Herzschlag."

    "Ich habe das Gefühl, als würde sich mein Kopf in zwei Teile spalten."

    "Es ist aber komisch, dass der Schmerz, obwohl er so stark ist, nie lange andauert.{w} Bis ich mich für die Schule fertiggemacht habe, spüre ich nur noch einen leichten Schmerz im Hinterkopf."

    "Im Großen und Ganzen betrachtet ist es also nicht {i}so{/i} schlimm.{w} Aber es ist ein lustiges Gefühl, wegen so was aufzuwachen.{w} Und auch irgendwie merkwürdig, wenn ich bedenke, dass ich mich jeden Tag so fühle."

    "Aber egal.{w} Genug über diese seltsamen Dinge nachgedacht.{w} Es ist Zeit, den Tag in Angriff zu nehmen!"



    with hpunch

    "Nach einem kurzen Kampf mit meiner Decke, schwinge ich meine Beine umher und ziehe mich irgendwie aus dem Bett.{w} Ein kurzer Blick auf meine Nachttischuhr belegt, dass es noch früh am Morgen ist.{w} ... {i}Zu{/i} früh."

    "Wenn es nach mir ginge, würde die Welt erst am Nachmittag anfangen, sich zu drehen.{w} Aber wie jeder weiß, das Leben ist kein Wunschkonzert."

    "Ich ziehe die Vorhänge zur Seite und lasse mein Zimmer vom Sonnenlicht erhellen.{w} Und blende mich dabei fast selbst!"

    "Der Rest meines Morgens besteht darin, meine Uniform anzuziehen und die Krawatte zu binden. Im Halbschlaf ist das echt nicht einfach!"

    "Nachdem ich mich fast zu Tode erstickt hätte, schaffte ich es dennoch irgendwann, die Krawatte anzuziehe."

    "Da ich keinen Kamm finden konnte, müssen meine Haare mit den Händen frisiert werden.{w} Als ich in den Spiegel blicke, starrt mich jemand mit schmutzigen, schwarzen Haaren an.{w} ... Passt doch fast."

    "Teils angezogen und teils fertig, verlasse ich mein Zimmer."

    scene kitchen day with dissolve

    "Über ungleichmäßige Treppen gelange ich gefährlich hinuntern und in die Küche."

    "Ich werde von der Stille begrüßt.{w} ... Die Küche ist leer.{w} Aber dieser Anblick ist für mich mittlerweile alltäglich."

    "Meine Eltern sind das, was man auch gern als {w}Workaholics{w} bezeichnet. Das heißt, sie verbringen mehr Zeit in ihrer Arbeit als zu Hause.{w} Ich sehe sie nur abends, und sobald wir da mit dem Essen fertig sind, geht auch schon wieder jeder schlafen."

    "Versteh mich nicht falsch. Ich verstehe, dass sie arbeiten müssen, dass es uns gut geht, daher hasse ich sie auch nicht.{w} Es ist bloß so ...{w} Ich weiß nicht so genau ... Einsam?"

    "Aber na ja.{w} Es bringt nichts, sich darüber Gedanken zu machen.{w} Es ist schon seit Jahren so, also keine Ahnung, warum ich jetzt wieder daran denke!"

    "Das Gute an der ganzen Sache ist, dass ich lernen musste, wie man kocht.{w} Echt wahnsinnig, wie schnell man so was lernt, wenn man mal kurz davor ist, dem Hungertod zu erliegen!"

    "Ich glaube nicht, dass ich noch genug Zeit habe, um mir etwas Prunkvolles zum Frühstück herbeizuzaubern, von daher mache ich mir nur Toast.{w} Mit Toast liegt man nie falsch."

    "...Okay, man {i}könnte{/i} damit falsch liegen.{w} Plötzlich werden traumatische Erinnerungen an eine Zeit, als mein Toast in Flammen aufging, in mir wach.{w} ... Ah, das war ein Tag."

    "Aber ich habe von meinen Fehlern gelernt.{w} Es wird kein zweites, äh ... drittes Mal mehr passieren!"

    with Pause(2.5)

    "Nachdem ich meinen leicht verkohlten Toast verschlungen habe, werfe ich mir meine Tasche über die Schulter und gehe zur Haustür."

    "Bevor ich aus dem Haus gehe, werfe ich noch einen Blick darauf.{w} Irgendwie einsam, wenn dich keiner verabschiedet ...{w} Aber ich habe es ja schon einmal gesagt, es ist morgens schon seit langer Zeit so."

    scene town street day with dissolve

    "Die Sonne steht hoch am Himmel, die Vögel zwitschern über mir und Scharen von Schülern überholen mich auf ihrem Weg zur Schule."

    "...Es ist alles so schrecklich."

    "Ich bin nicht gerade ein Morgenmensch, von daher kann ich überhaupt nicht verstehen, wie manche Leute schon in aller Früh so fröhlich sein können.{w} Ich meine, in meinem Fall braucht es all meine Willenskraft, um überhaupt mal einen Fuß vor den anderen zu setzen."

    "Ich muss nur hoffen, dass sich die Energie, die ich beim Frühstück zu mir genommen habe, bald bemerkbar macht. Hoffentlich noch, bevor ich die Schule erreiche."

    with Pause(2.5)

    "..."

    stop music fadeout 8.0

    with Pause(2.5)

    "Während ich meinen Kopf unten halte und meine Augen an den Boden geklebt sind, bemerke ich plötzlich, dass die lebhafte Atmosphäre auf einmal verschwunden ist."

    "Die Stille hat die Oberhand gewonnen - meine Schritte sind das Einzige, das ein Geräusch erzeugt.{w} Es geht überhaupt kein Wind.{w} Häh ...{w} Das ist schon ein bisschen komisch."

    "Als ich meinen Kopf erhebe, erblicken meine Augen etwas Beunruhigendes."

    "Die Straße ist menschenleer."

    "Keine Schüler.{w} Keine Autos.{w} Selbst das Gezwitscher der Vögel ist auf einmal verschwunden."
    play music "bgm/ominousintro.ogg" fadein 2.0 
    queue music "bgm/ominousloop.ogg"
    "Was ...?"

    "In der Hoffnung, wenigstens irgendjemanden zu treffen, eile ich vorwärts."

    "Sogar die Sonnenstrahlen scheinen verblasst zu sein, wodurch alles in einen düsteren Farbton gefärbt wurde.{w} Aber ...{w} im Himmel ist weit und breit keine Wolke zu sehen."

    "Okay, das macht mich jetzt aber wirklich ein wenig verrückt.{w} Ich muss doch nur--"



    "Ein spaltender Schmerz schießt durch meinen Kopf und stoppt meine Bewegungen.{w} Wie ein glühender Schürhaken, der durch meinen Schädel gestoßen wird."

    "Kopfschmerzen?{w} Jetzt?"

    "Das ergibt doch alles keinen Sinn!"

    "Verzweifelt versuche ich, mich aufrecht zu halten, während ich eine Hand an meinen Kopf halte.{w} Im Gegensatz zu den Kopfschmerzen am Morgen, die immer schwächer werden, werden diese hier immer schlimmer!"



    "{i}Klopf.{/i}"



    "{i}Klopf.{/i}"



    "{i}Klopf.{/i}"

    "Die Schmerzen möchten nicht mehr aufhören."

    "Sie zwingen mich auf die Knie.{w} Ich kann kaum noch klar denken. Mein Kopf droht jeden Augenblick zu explodieren."



    "Und dann ...{w} anhand von abgerissenen Zähnen und einen schmerzhaften Ausdruck ...{w} sehe ich es."

    "Etwas, das nicht existieren sollte.{w} Und trotzdem nehme ich es mit meinen eigenen Augen wahr."

    scene cg20 with fade

    "Ein Monster.{w} Das ist das einzige Wort, das mir gerade einfällt."

    "Eine groteske Masse aus Fleisch, mit krummen Reißzähnen und roten Schlitzaugen voller Hass.{w} Am ehesten würde ich es als Hund bezeichnen, aber ich kenne keinen Hund, der dreimal so groß ist wie ich."

    "Das Monster faucht und scheint dabei eine Dampf-ähnliche Substanz auszuatmen.{w} Angesichts der Haltung und der Tatsache, dass es mir den Weg versperrt, kann ich nur vermuten, dass es hinter mir her ist."

    "Aber ...{w} warum?"

    "Was zur Hölle ist das?{w} Wo kommt es her?{w} Warum ist es ausgerechnet hinter mir her?!"

    "Unzählige Fragen gehen mir gerade durch den Kopf, aber ich bezweifle, dass sie mir irgendjemand beantworten kann. Erst recht nicht ...{w} dieses ...{w} Ding."

    "Es gibt nur eine Sache, die ich in einen solchen Augenblick tun kann--"

    menu:
        "Standhaft bleiben.":
            "Na klar.{w} Ich weiß nicht, was das für ein Ding ist, und schon gar nicht, wo es herkommt, aber ich gebe mich nicht kampflos geschlagen!"

            "Ich ignoriere den Schmerz, der meinen Schädel zu verzehren droht, richte mich auf und starre in die Augen des hasserfüllten Monsters zurück."

            play music "bgm/battleintro.ogg" fadein 1.0
            queue music "bgm/battleloop.ogg"

            "Dann balle ich meine Hand zu einer Faust, schlage blitzartig nach vorne und lande einen direkten Treffer in der Fresse des Monsters.{w} Nimm das, du scheiß Vieh!"

            with hpunch
            "{i}BAM!{/i}"

            "..."

            stop music fadeout 2.0
            scene town street day with fade

            "Okay, nein.{w} Das war 'ne ganz schlechte Idee.{w} Das hat ja überhaupt nichts bewirkt.{w} Das Monster sieht jetzt nur noch wütender aus als vorhin."
            play music "bgm/ominousintro.ogg" fadein 2.0 
            queue music "bgm/ominousloop.ogg"
            "Das einzige, was mein Schlag bewirkt hat, war, dass ich mir selbst weh getan hab.{w} Ich hoffe, ich hab mir nichts gebrochen ..."

            "Ich gehe wieder ein paar Schritte zurück und schüttle meine Hand erstmal aus.{w} Das tut noch immer höllisch weh.{w} Au!"

            "...Was jetzt?"

            "Mein Überraschungsangriff wurde mit völliger Gleichgültigkeit begegnet, und ich schätze, jetzt ist es schon zu spät, um wegzurennen."

            "Das war wohl ein riesengroßer Fehler."

            "Ich versuche, mich umzudrehen und wegzulaufen, aber das Monster stürmt geradewegs auf mich zu."

            "Mir bleibt keine andere Wahl.{w} Ich bereite mich bestmöglich auf den unvermeidlichen, knochenbrechenden Zusammenstoß vor."
        "Flieh.":

            "Ja.{w} Na klar.{w} Alles andere wäre ja idiotisch."

            "Wenn man mit so was, etwas, das über die Natur hinausgeht, konfrontiert wird, und dessen Blick 'Ich werd dich fressen' ausdrückt, dann läuft man aus Instinkt schon davon."

            scene town street day with fade
            with hpunch
            with hpunch

            "Ich warte keinen Augenblick länger, drehe mich um und laufe in die entgegengesetzte Richtung."

            "Die Ermüdung von vorhin ist wie von Zauberhand verschwunden.{w} Es ist erstaunlich, was Angst bewirken kann!"

            "Ich laufe so schnell ich nur kann, aber in meiner Eile stolpere ich über meinen eigenen Fuß und lande wie ein Häufchen Elend auf dem Boden."

            with hpunch

            "Die Schmerzen meiner Knie ignorierend, versuche ich verzweifelt, mich aufzurichten.{w} Aber ich schaffe es nicht."

            "Ich höre, wie das Monster hinter mir wütet."

            "Die Angst vor dem bevorstehenden Tod betäubt meine Gliedmaßen und zerstreut meinen Verstand so sehr, dass ich meinem Körper keine Befehle mehr erteilen kann.{w} Ich kann jetzt nur noch meinen Kopf umdrehen und dem Tod in die Augen sehen."

            "Es ...{w} Es ist aus."

    stop music fadeout 5.0 
    scene bg white
    with flash

    "Kurz bevor mich das Monster verspeist und mein Leben zu einem Ende bringt, dringt ein strahlend helles Licht in mein Blickfeld, welches sowohl mich als auch das Monster verschlingt."

    "Das Monster bleibt regungslos stehen und schreit, ehe es vor meinen Augen 'verdampft'."

    "...{w}Was ...{w} Was zum Teufel ist da gerade passiert?"

    cg "Geez, that was a close one!{w} Are you alright?"
    play music "bgm/magicalgirlintro.ogg" fadein 6.0
    queue music "bgm/magicalgirlloop.ogg"
    "Eine fröhliche Stimme zwitschert.{w} Ein willkommenes Geräusch nach dem Schrecken ...{w} dieses Monsters."

    tg "Rede nicht mit ihm!{w} Wir müssen gehen bevor--"

    "Und dann eine weitere Stimme, die weniger ...{w} fröhlich klingt.{w} Um ehrlich zu sein, klingt sie sogar eher verägert."

    scene cg1 with wake


    "Kurz darauf verlasst das Licht, was meine Retter zum Vorschein bringt."

    "...Wobei ...{w} ich das echt als {i}letztes{/i} erwartet hätte."

    "Zwei Mädchen, in etwa in meinem Alter, stehen vor mir."

    "Ich blinzle ein paar Mal und wische meine Augen aus, in der Hoffnung, dass all das ein wenig mehr Sinn ergeben würde.{w} Das kann unmöglich wahr sein."

    "Um ehrlich zu sein, glaube ich, dass mir meine Augen jetzt gerade einen größeren Streich spielen als sie es vorhin getan haben, als das Monster da war!"

    "Diese Waffen und Kleidung, die direkt aus einem Fantasy-Buch stammen könnten, sind zu viel für mein kleines Gehirn."

    p "Wa ...{w} Was zur Hölle war das?!"

    cg "A shadow."

    "Das fröhlichere der beiden Mädchen antwortet mir unverblümt und entspannt sich dabei wenig."

    p "H-Häh?"

    "Das war jetzt die Erklärung?{w} Ich blicke hinunter zu meinen Füßen, wo sich mein eigener Schatten erstreckt, aber das Mädchen fängt an zu lachen."

    cg "Not your own shadow, silly!{w} That thing we just took care of--which you're welcome for, by the way--is what we call a shadow."

    cg "The physical manifestation of all the hatred and negative emotions that might lurk in one's heart."

    cg "Normally they're not so aggressive during the day, though...{w} It was really out for you!"

    cg "We're usually pretty good at nabbing them before they get to you, but this one completely took us by surprise.{w} I'm happy we got here in time!"

    cg "You're not hurt, are you?"

    p "Nein, alles gut, aber--"

    tg "Als ob die Dinge nicht schlimm genug wären, dass wir uns ihm offenbaren mussten, jetzt redest du mit im über Sachen, die kein normaler Mensch wissen sollte. {W} Hast du den Verstand verloren ?!"

    "Das aggressivere Mädchen, dessen Ausdruck immer düsterer wurde, während die andere sprach, unterbrach plötzlich. Anscheinend konnte sie es nicht länger ertragen."

    cg "Aww, but he looks so confused!{w} And now that he's seen one of the shadows first-hand, don't you think it's just a {i}little{/i} too late for us to quietly slip back into the shadows?"

    tg "..."

    "Mit verengten Augen starrt sie uns an.{w} Man erkennt, dass sie eindeutig wütend ist ...{w} aber ich glaube nicht, dass sie etwas dagegen unternehmen kann."

    cg "See?{w} You worry too much!{w} We'll only tell him what he needs to know, nothing more, nothing less!"

    "Das fröhliche Mädchen schenkt mir mit einem Funkeln in ihren Augen wieder ihre Aufmerksamkeit."

    scene town street day
    $ sayapose='magical_1'
    $ hikapose='magical_1'
    $ hikaface='normal'
    $ sayaface='smiling'
    show Sayaka at left
    show Hikari at right
    with dissolve

    cg "Right, so, Kenta, where were we?"

    p "Äh, wir waren--"

    "Warte ..."

    p "Woher kennst du überhaupt meinen Namen?!"

    $ sayaface='shocked'
    show Sayaka

    cg "Huh?{w} Oh...{w} Whoops!"

    "Mit einer Hand verdeckt sie ihren Mund - so, als wolle sie versuchen, das Gesagte rückgängig zu machen.{w} Es häufen sich immer mehr Fragen an, und ich habe noch immer keine einzige Antwort erhalten!"

    with hpunch
    $ hikapose='magical_2'
    $ hikaface='angry'
    $ sayaface='joking'
    show Sayaka
    show Hikari with dissolve

    tg "Du Idiot!"

    "{i}Whap!{/i} Das ernstere Mädchen 'schlägt' mir ihrer Faust auf den Kopf des anderen Mädchens, die gerade in einer 'Tut mir leid, mein Fehler'-Art und Weise ihre Zunge ausstreckt."

    p "Ihr kennt mich also?"

    $ sayaface='smiling'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka
    show Hikari with dissolve

    "Ich hab sie noch nie in meinem Leben gesehen.{w} Und so wie sie aussehen, würde ich mich {i}auf jeden Fall{/i} an sie erinnern."

    $ sayapose='magical_2'
    show Sayaka with dissolve

    cg "Well, we don't know {i}you{/i} personally, but we've been watching over you for a while now.{w} You've become quite the point of interest recently, you know!"

    p "Ich ...?"

    "Was hab ich in meinem Leben bloß falsch gemacht, dass mir so viel Aufmerksamkeit geschenkt wird?{w} Soviel ich weiß, bin ich doch nur ein normaler Schüler.{w} Der ein durchschnittliches Leben führt.{w} Und normale Dinge macht.{w} Wobei, nach all diesen Ereignissen trifft das wohl alles nicht länger zu."

    cg "Mmhmm.{w} Can't really go into details, 'cause you know, top secret and all, but let's just say...{w} It's not in our best interest for you to fall into the wrong hands."

    $ sayaface='happy'
    show Sayaka

    cg "You wouldn't believe how much effort we've been putting into keeping you safe, you know!{w} Actually, I'm kind of relieved we finally get to meet, so you can finally appreciate all our hard work!"

    "Sie strahlt mich an und lehnt sich ein wenig zu nah an mich heran."

    "Ich ...{w} Sie konfrontiert mich mit so viel, dass ich kaum mehr klar denken kann."

    p "{i}Wer{/i} seid ihr überhaupt?"

    $ sayaface='normal'
    show Sayaka

    cg "Hmmm..."

    "Sie fängt an nachzudenken.{w} Ich schätze, sie wählt die Worte, die sie gleich sagen wird, sorgfältig aus, um zu verhindern, dass ihre Partnerin wieder auszuckt."

    $ sayaface='happy'
    $ sayapose='magical_1'
    show Sayaka

    cg "Think of us as your guardian angels, okay?"

    "Als sie das sagt, macht sie mit ihrem Bogen eine schwungvolle Bewegung, woraufhin dieser kurz darauf zwischen ihren Fingern zerbricht.{w} Wenige Augenblicke später bilden sich diese Scherben hinter ihrem Rücken wieder zusammen, bis sich ein paar Flügel gebildet hat."

    "Die Flügel, die zwar nicht fest mit ihr verbunden sind, scheinen zumindest zu funktionieren. Oder sagen wir so, sie bewegen sich im Wind zumindest hin und her."

    "Warte, sind das buchstäblich Engel?!"

    p "Um mal ein paar Dinge abzuklären ..."

    p "Fangen wir mal von vorne an: das Ding, das mich gerade angegriffen hat - dieses Monster da - nennt ihr Schatten"

    $ sayaface='smiling'
    show Sayaka

    cg "Yup!"

    p "Und diese 'Schatten' jagen mich nun schon seit einer geraumen Zeit?"

    cg "Mmhmm!"

    p "Denn, wenn sie mich fangen ...{w} wär das offensichtlich 'nicht gut' ... Einfach so, aus nicht näher beschriebenen Gründen?"

    cg "Yup.{w} Really bad!"

    p "Und ihr, wer auch immer ihr seid, agiert von den Schatten heraus und bekämpft sie, um mich zu beschützen?"

    "Sie nickt begeistert.{w} Es sieht so aus, als hätte ich langsam begriffen, was hier los ist, auch wenn ich die kleinen Details noch nicht zusammenfügen konnte."

    "Mit all diesem Wissen, komme ich zu dem Entschluss, dass ..."

    menu:
        "Ich muss ihnen einfach glauben.":
            "So verrückt es auch klingt, ich kann es nicht leugnen.{w} Das Monster war eindeutig echt und ich habe auch keinen Grund, an diesen Mädchen zu zweifeln, schließlich haben sie mich gerettet."
        "Diese Mädchen spinnen doch.":

            p "Okay.{w} Ja.{w} Jetzt versteh ich's."

            $ sayaface='happy'
            show Sayaka

            cg "You do?"

            p "Ja.{w} Ihr habt sie nicht mehr alle."

            $ sayaface='shocked'
            $ hikaface='angry'
            show Sayaka
            show Hikari

            cg "L-lost it?!"

            "Meine Worte scheinen sie zu überraschen.{w} Vielleicht bin ich ein bisschen gemein, aber das ist die einzig plausible Erklärung!"

            p "Absolut durchgeknallt.{w} Ich weiß nicht, ob ihr nicht einfach nur Cosplayer seid und ich nicht nur in eine Vorführung gestolpert bin ...{w} aber das kann unmöglich real sein."

            "Es ist die einzige Schlussfolgerung, zu der mein Verstand kommt.{w} Sie hat doch wohl nicht wirklich erwartet, dass ich ihr den Mist mit dem 'Schutzengel' glaube, oder?{w} Hah!"

            p "Bleibt ruhig in eurer kleinen Fantasiewelt, aber haltet mich da bitte raus, okay?"

            hide Sayaka
            hide Hikari
            with dissolve
            stop music fadeout 5.0

            "Mit diesen Worten mache ich mich wieder auf in Richtung Schule.{w} Meine Fresse, haben mich die jetzt wirklich so lang aufgehalten?{w} Wenn ich Glück hab, komm ich noch vor dem Ende der ersten Stunde in die Schule!"

            cg "Hey, wait!{w} This is--"

            "Ich kann es mir echt nicht leisten, noch mehr von diesem Wahnsinn zu hören, deshalb ignoriere ich sie jetzt einfach und stelle ein wenig Abstand zwischen uns her."

            with Pause(2.0)

            with hpunch
            with hpunch

            p "Hrrk!"
            play music "bgm/magicalgirlintro.ogg" fadein 3.0
            queue music "bgm/magicalgirlloop.ogg"
            "Irgendwas packt mich am Kragen und zwingt mich dadurch stehenzubleiben. Dass ich fast erstickt wäre, ist unwichtig."

            "Bevor ich überhaupt darüber nachdenken kann, was das war, wandert die Kraft, die mich gerade noch aufhielt, plötzlich zu meiner Schulter und zwingt mich dazu, mich umzudrehen."

            $ hikaface='angry'
            show Hikari
            with dissolve

            "Ich werde von einem furcherregenden Gesicht - das Gesicht, welches vorhin noch ruhig war - konfrontiert."

            tg Wirklich?{w} Ich meine--wirklich?!{w} Bist du {i}wirklich{/i} so ein grßer Idiot?!"

            p "I-Ich ... Äh ..."

            "Ich spüre, wie mich ihr Blick immer kleiner aussehen lässt.{w} Sie ist eindeutig noch gruseliger als das Monster!"

            tg "Es ist schon schlimm genug, dass wir uns zeigen mussten, aber jetzt tust du nur so, als wären wir verrückt?!"

            "Mit einem finsteren Blick ballt sie ihre Fäuse zusammen und hinterlässt den Eindruck, als würde sie am liebsten zuschlagen."

            tg "Ich weiß nicht einmal, warum wir uns um dich kümmern, wenn du uns so behandelst!{w} Vielleicht sollten wir, sie dich nächstes mal einfach fressen lassen.{w} Hmph."

            $ hikapose='magical_2'
            $ hikaface='normal'
            show Hikari
            with dissolve

            "Sie verschränkt ihre Arme und dreht den Kopf zur Seite.{w} Sie gehört echt ...{w} zu der emotionalen Sorte."

            $ sayaface='shocked'
            show Sayaka at left
            show Hikari at right
            with dissolve

            cg "Wah!{w} Don't say that!"

            "Das fröhliche Mädchen stolpert, als sie sich zwischen uns drängt, und wirft mir ein entschuldigendes Lächeln zu."

            cg "I-I'm sure she didn't mean that!{w} She just gets a little grouchy sometimes."

            $ sayaface='angry'
            show Sayaka

            cg "And you--don't get all angry with him.{w} It's only natural he would be skeptical of us at first!"

            $ hikapose='magical_1'
            show Hikari
            with dissolve

            tg "Hmph, was auch immer.{w} Er ist wirklich so dumm, wie er aussieht."

            "Autsch ...{w} Ich {i}bin{/i} noch immer hier, nur damit ihr wisst!"

            $ sayaface='joking'
            show Sayaka

            cg "Oh?{w} That's not what I remember.{w} In fact, I remember you saying he looked quite cu--"

            $ hikaface='embarrassed'
            $ sayaface='shocked'
            show Sayaka
            show Hikari
            with hpunch

            "{i}BAM.{/i} Da landet die Faust direkt im Gesicht des fröhlichen Mädchens.{w} Und dieses Mal war es ernst gemeint, denn sie hielt kein bisschen zurück.{w} Das sah aus, als hätte es echt weh getan ..."

            tg "Halt dein Mund!{w} Ich habe soetwas nicht gesagt!"

            $ sayaface='scared'
            show Sayaka

            cg "Wahh!{w} Okay, okay, fine!"

            "Meine Güte ...{w} Die beiden sind echt komisch.{w} Aber sie schien es wirklich ernst zu meinen.{w} Vielleicht war meine Schlussfolgerung, sie als Verrückte abzustempeln, etwas voreilig."

            "Ich mein, sie sind verrückt, das stimmt schon, aber vielleicht steckt ja doch ein Fünkchen Wahrheit darin.{w} Die Existenz dieses Monsters kann ich schließlich auch nicht leugnen, so schwer es mir auch fällt."

    $ sayaface='smiling'
    $ hikaface='normal'
    show Sayaka
    show Hikari

    p "Okay, also, äh, was passiert jetzt?"

    cg "Hmm."

    cg "Well, now that the shadows have gotten more aggressive, I really don't think we can go back to our old job of watching you from afar.{w} We were lucky to just barely catch that thing just now after all."

    "...Irgendwie gefällt mir diese Wortwahl nicht.{w} Kein bisschen."

    cg "So, we'll be parting ways for now, but expect us to be keeping an {i}extremely{/i} close eye on you from now on, okay?"

    $ sayaface='happy'
    show Sayaka

    cg "Bye-bye for now!"

    hide Sayaka
    hide Hikari
    with dissolve

    "Sie zwinkert und winkt mir zu, bevor sie in die andere Richtung abhebt.{w} Ihre weniger begeisterte Partnerin dreht hingegen einfach nur ihren Kopf von mir weg."

    "Und kurz darauf stehe ich wieder ganz allein in dieser Straße."

    "Ich ..."

    "Ist das gerade wirklich passiert?"

    "Ah, pfeif drauf, das Ganze muss erstmal warten.{w} Jetzt muss ich mich erstmal auf was anderes konzentrieren: Ich komme noch zu spät zur Schule!"

    "Im Versuch, die verlorengegangene Zeit wieder aufzuholen, sprinte ich los, und hoffe, nicht noch einmal auf die beiden Mädchen zu treffen."
    stop music fadeout 3.0
    scene bg black
    with fade



    "Irgendwie geht es sich doch noch rechtzeitig aus.{w} Es kam mir vor wie ein Fotofinish - genau in dem Moment, wo die Glocke läutete!"

    scene classroom
    with fade
    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"    

    "Ich nehme mir einen Moment Zeit, um Luft zu holen, bevor ich mich zum Tisch schleppe. Ein paar Sekunden später kommt auch schon der Lehrer ins Klassenzimmer.{w} War das knapp!"

    "Irgendwie scheint kein anderer Mitschüler mein spätes Erscheinen wahrgenommen zu haben.{w} Vielleicht liegt das daran, dass sie von mir sowieso nichts anderes erwarten würden?"

    "Manchmal bin ich echt spät dran, und gelegentlich komme ich sogar erst nach dem Glockenläuten.{w} Das passiert meistens, weil ich verschlafe.{w} Aber dieses Mal hätte ich ja einen richtigen Grund, wäre ich zu spät gekommen!"

    "Aber nach all dem, was vorhin passiert ist, bezweifle ich, dass ich mich auf den Unterricht konzentrieren kann.{w} Ich fange an, mich zu fragen, ob ich jemals eine Erklärung für all das bekommen werde."

    "Unvorstellbar große Kreaturen ...{w} Mädchen mit magischen Waffen ...{w} Klar, dass mein Hirn das nicht wahrnehmen möchte."

    "Ich glaub, ich bin in einem Film oder so!"

    "Am Hinterkopf ist noch immer ein leichter Schmerz zu spüren."

    "So glücklich wie ich bin, hab ich zumindest einen Platz beim Fenster. SO kann ich zumindest nach draußen und in den blauen Himmel blicken."

    "Der Lehrer hält seine übliche Morgenrede und spricht über die bevorstehenden Ereignisse in unserer Schule, aber in meinen Ohren sind seine Worte nur dumpfes Gemurmel."

    "Diese Mädchen kannten meinen Namen ...{w} Und egal, wie sehr ich auch nachdenke, ich kann mich nicht daran erinnern, sie jemals gesehen zu haben.{w} Zumindest {i}glaube{/i} ich, sie noch zu gesehen zu haben."

    "Ich denke stark nach.{w} Vielleicht sogar zu stark, in Anbetracht dessen, dass der Kopfschmerz wieder stärker wird."

    "...Nein.{w} Nichts.{w} Mir fällt überhaupt nichts ein."

    "Vorerst besiegt, fokussiere ich mich wieder auf den Unterricht, während ich noch immer nach draußen blicke."

    teacher "Now, uh, I know it's a bit sudden, but as of today, we have two transfer students that will be joining our class."

    "Schulwechsler?{w} Um diese Zeit?{w} Schon ein bisschen spät, die Schule zu wechseln, oder nicht?{w} Selbst der Lehrer scheint ein bisschen verwirrt zu sein, als er es ankündigt."

    "Und nicht nur einer, sondern {i}zwei{/i}?{w} Warum hab ich bloß das Gefühl ... dass hier etwas vor sich geht?{w} Fast so, als ob es irgendwie mit den Ereignissen vorhin in Zusammenhang steht?"

    "Hah.{w} Nein.{w} Das kann unmöglich sein."

    teacher "I'd like you all to make them feel welcome as they transition in.{w} Uh, what did you say your names were?"

    cg "I'm Sayaka, it's nice to meet you all.{w} I hope we can all get along!"

    stop music fadeout 2.0

    "...!{w} Ich setze mich schlagartig aufrecht hin und drehe meinen Kopf nach vorne.{w} Diese fröhliche Stimme.{w} Ist das wirklich ...?"

    play music "bgm/magicalgirlintro.ogg" fadein 1.0
    queue music "bgm/magicalgirlloop.ogg"

    $ sayapose='school_1'
    $ hikapose='school_1'
    $ sayaface='smiling'
    $ hikaface='normal'

    show Sayaka at left
    show Hikari at right
    with dissolve

    "Sie sind es. Die beiden Mädchen, von denen ich hoffte, sie nie wieder zu sehen.{w} In meiner Schule.{w} In meinem Klassenzimmer, und noch dazu in der Schuluniform."

    "Das fröhliche - äh, Sayaka - verbeugt sich höflich vor der Klasse und wirft mir ein Grinsen zu.{w} Was ...{w} Was soll das?"

    "Das andere Mädchen ist weniger höflich und steht mit verschränkten Armen da.{w} Es sieht so aus, als sei sie nicht freiwillig hier.{w} Auch ihr Blick richtet sich auf mich, aber anstatt mich anzulächeln, starrt sie mich an."

    "Gibt sie etwa mir die Schuld dafür?{w} Es fühlt sich echt so an ..."

    s "The grumpy one beside me here is Hikari.{w} Go on, say hi!"

    $ sayaface='happy'
    show Sayaka

    h "H-Hey,l-lass das--"

    $ hikaface='embarrassed'
    hide Sayaka
    show Hikari at center
    with dissolve

    "Sayaka verpasst ihr einen spielerischen Schubs, woraufhin sie in die Mitte des Klassenzimmers stolpert und alle Aufmerksamkeit erregt."

    "Sie sieht aus, als hätte sie vergessen, was sie sagen wollte.{w} Auch ihr Gesicht wird allmählich immer roter.{w} Da hat wohl jemand Lampenfieber."

    h "I-Ich bin... {size=12}Hikari...{w} F-Freut mich euch k-kennenzulernen...{/size}"

    $ hikaface='shy'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "Sie nuschelt kurz etwas vor sich hin, ehe sie sich gleich darauf wieder umdreht und sich hinter Sayaka versteckt."

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "See, that wasn't so hard was it?"

    "Hikari kocht augenscheinlich innerlich nur so vor Wut.{w} Ich bin sicher, dass es mit Sicherheit nicht so ruhig geblieben wäre, wären wir hier nicht in einem Klassenzimmer."

    stop music fadeout 4.0
    hide Sayaka
    hide Hikari
    with dissolve

    "Nach den Vorstellungen ersuchte der Lehrer die beiden, sich einen freien Platz zu suchen.{w} Warte mal.{w} Da fällt mir gerade ein, dass die einzigen freien Plätze in der Klasse ..."

    "...Direkt hinter mir, ebenfalls neben dem Fenster, und rechts neben mir, sind.{w} Das heißt also, dass beide neben mir sitzen werden?"

    "Wobei, das trifft sich ja eigentlich ziemlich gut.{w} Jetzt kann ich sie endlich fragen, was die ganze Scheiße soll!"
    play music "bgm/mischiefintro.ogg" fadein 1.0
    queue music "bgm/mischiefloop.ogg"
    "Sayaka geht zum Schreibtisch hinter mir und nimmt dort platzt.{w} Hikari setzt sich zum freien Platz rechts neben mir."

    "Ich mache mich breit und versuche dadurch, ihre Aufmerksamkeit zu erregen, aber ich werde kurzerhand vom Lehrer daran gehindert, der wieder zu reden begann."

    "Verdammt.{w} Ich möchte echt keinen Ärger hier bekommen, weil ich während des Unterrichts tratsche.{w} Da muss ich wohl oder übel auf die Pause warten."

    "Bis dahin sind es aber noch ganze zwei Stunden ...{w} also eine halbe Ewigkeit, um es anders auszudrücken!"

    "Ich drehe mich wieder nach vorne.{w} Da ich momentan sowieso nichts machen kann, konzentriere ich mich vorerst einfach auf den Lehrer und--"

    with hpunch

    "Argh, nein!{w} Wie soll ich mich konzentrieren, wenn neben mir zwei so komische Mädchen sitzen?!{w} Ich möchte Antworten, und zwar sofort!"

    "Ich trommle mit den Fingern gegen den Schreibtisch und überlege mir, wie ich weiter vorgehen soll."

    "Es ist besser, still zu bleiben, von daher ..."

    "..."

    "Ah!{w} Na klar, das ist ja offensichtlich."

    "Ich hole einen Notizblock und einen Kugelschreiber aus meiner Schultasche raus.{w} Ich schreib ihnen einfach!{w} Altmodisch, aber zweckdienlich."

    "Es ist zwar eine eher unreife Art der Kommunikation, das geb ich zu, aber ich bin schließlich auch verzweifelt, da sollte man es mir nicht so übel nehmen."

    "Ich schreibe meine Frage: {i}'Was macht ihr hier?'{/i}{w} Kommen wir gleich zur Sache."

    "Ich reiße die Seite heraus - so kräftig, dass ich sie fast in zwei Teile gerissen hätte.{w} Jetzt stellt sich nur noch die Frage ... Wem soll ich den Zettel geben?"

    menu:
        "Sayaka.":
            $ sayaka += 1

            "Obwohl es zwar schwieriger ist, den Zettel nach hinten zu reichen, ohne verdächtig zu wirken, versuche ich es trotzdem bei Sayaka ... Irgendwie habe ich das Gefühl, als würde sie mir eher antworten."

            "Ich lehne mich zurück und fange an, mit dem Stuhl zu schaukeln und lasse den Zettel auf ihren Tisch fallen.{w} Oder zumindest ...{w}{i}glaube{/i} ich, dass es ihr Tisch war."

            "Nach ein oder zwei Minuten, die ich mit Däumchendrehen verbracht habe, verliere ich langsam die Hoffnung.{w} Vielleicht war das--"

            with hpunch

            "Plötzlich spüre ich etwas an meiner Schulter.{w} Es war derselbe Zettel, den ich Sayaka gab.{w} SIEG!"

            "Und meiner hastig geschriebenen und kaum lesbaren Frage steht eine Antwort in einer weitaus ordentlicheren Handschrift."

            "{i}'Wir sind hier, um dich zu beschützen, Dummerchen!'{/i}"

            "Mich beschützen?{w} Stimmt ...{w} Ich erinnere mich daran, dass sie so was wie 'Schutzengel' oder so gesagt hatten, und dass sie mich besser im Auge behalten würden ... aber das ist jetzt echt lächerlich!"

            "Ich schreibe meine Antwort drunter. Allerdings muss ich einige Wörter mehrmals schreiben, da ich vor lauter Eile ein paar Fehler eingebaut habe."

            "{i}'Okay, das versteh ich ja noch, aber müsst ihr mir dabei so nahe sein?{w} Wie habt ihr es überhaupt geschafft, auf diese Schule zu kommen?'{/i}"

            "{i}Schon vergessen, dass du heute fast als Hundefutter geendet hättest?{w} Das wird nicht nochmal passieren, dafür sorgen wir!{w} Und wegen der Schule ...{w} Na ja ...{w}sagen wir so, wir können ziemlich überredend sein.{w} Eh-heh-heh.{/i}"

            "...Ernsthaft, wer schreibt heutzutage noch 'eh-heh-heh'?{w} Ach, scheiß drauf.{w} Sie hat mir zumindest geantwortet.{w} Einigermaßen."

            "Jetzt, wo ich darüber nachdenke, erinnere ich mich daran, dass auch der Lehrer ein bisschen verwirrt war, als er sie vorstellte. Ich wette, sie haben ihre magischen Kräfte spielen lassen.{w} Der Gedanke ist schon irgendwie gruselig ..."

            "'Magie'.{w} Ich verwende dieses Wort so beiläufig.{w} Heißt das, ich akzeptiere damit ihre Existenz?{w} Und auch, wenn die Beweise für die Magie sprechen, werde ich vorerst dennoch skeptisch bleiben."
        "Hikari.":

            $ hikari += 1

            "Genau.{w} Es ist leichter, ihr den Zettel zu geben, da sie unmittelbar neben mir sitzt."

            "Mit nach vorne gerichteten Augen lehne ich mich ein wenig zur Seite und 'schubse' den Zettel auf ihren Tisch.{w} Nur knapp entkomme ich den wachsamen Augen des Lehrers.{w} Puh!"

            $ hikaface='normal'
            show Hikari at center
            with dissolve

            "Ich bin zuversichtlich, dass sie mir antworten wird.{w} Sie schaut mich seitwärts an und hebt den Zettel mit zwei Fingern auf ... Das kommt mir so vor, als würde sie glauben, sie hätte es mit einem verseuchten Zettel zu tun."

            "Sie bringt ihn in die Nähe ihres Gesicht, überfliegt ihn einmal und dann ..."

            $ hikaface='joking'
            show Hikari

            "...Zerknittert sie ihn und wirft ihn zu mir zurück.{w} ... Das war jetzt echt gemein."

            hide Hikari
            with dissolve

            "Was soll man dazu sagen ...{w} Das war ein Misserfolg.{w} Und ich habe das Gefühl, als würde der Lehrer nun vermehrt seine Aufmerksamkeit auf mich richten. Daher ist es wahrscheinlich nicht mehr möglich, Sayaka ebenfalls noch zu fragen."

            "Ein bisschen verletzt von ihrer Zurückweisung, lasse ich mich nach vorne fallen und stütze meinen Kopf auf meiner Hand ab."

            "Wenn sie so drauf ist, sollte ich wohl vorerst versuchen, alle noch so kleinen Details zusammenzusetzen, und dann bei Gelegenheit mit ihnen reden."

            "Mal sehen ..."

            "Sie haben gesagt, sie wären meine 'Schutzengel', oder?"

            "Und dieser Angriff vorhin muss sie so sehr erschreckt haben, dass sie beschlossen haben, es wäre zu unsicher, sollten sie mich weiterhin aus der Ferne beobachten ...?"

            "Das ist zumindest die logischste Erklärung, die mir einfällt.{w} Mehr fällt mir momentan nicht ein, da sich die Eiskönigin dort drüben ja weigert, mit mir zu reden."


    stop music fadeout 4.0

    "Die erste Stunde des Tages vergeht elends langsam.{w} Ich kann mich überhaupt nicht konzentrieren, egal wie sehr ich es auch versuche."

    "Nach einer gefühlten Ewigkeit ertönt schlussendlich doch noch die Glocke.{w} Die erste Stunde ist endlich vorbei."

    "Vor der Pause haben wir aber noch eine Stunde. Und wäre das nicht schon schlimm genug, haben wir nächste Stunde auch noch Sportunterricht. Und da Jungen und Mädchen getrennt turnen, kann ich sowieso nicht mit ihnen reden."

    "Argh, warum muss das alles so kompliziert sein?!"

    scene bg black
    with fade
    play music "bgm/everydayintro.ogg" fadein 1.0
    queue music "bgm/everydayloop.ogg"
    "Nachdem ich mir meine Sportsachen angezogen hab, stehe ich nun mit den anderen Jungs meiner Klasse am Schulhof.{w} Genauso wie in der ersten Stunde, konnte ich mich auch im Sportunterricht nicht wirklich konzentrieren."

    "Ich mache die Übungen mit ... mit der Begeisterung eines Zombies."

    "Den Rest der Stunde nehme ich nur noch verschwommen wahr, zumindest bis einige meiner Mitschüler zur Laufbahn schauen, wo gerade die Mädels unterwegs sind.{w} Vor lauter Unglaubwürdigkeit, fangen einige der Schüler sogar an, sich ihre Augen auszureiben.{w} Was ist daran denn so besonders?"



    p "Was guckt ihr denn alle so?"

    "Ich dränge mich durch die Menge, die sich gebildet hat, damit ich einen guten Überblick habe."

    p "...Das gibt's doch nicht."

    "Die Mädels laufen auf der Bahn, was ja nichts Besonderes ist, aber das Besondere ist, {i}wer{/i} auf der Bahn läuft."

    scene cg6
    with fade

    "Sayaka flitzt förmlich über die Strecke und lässt die anderen im Staub zurück.{w} Sie läuft buchstäblich im Kreis um sie herum!"

    "Sie sieht, abgesehen von den Schweißtropfen, auch kein bisschen müde oder erschöpft aus - im Gegenteil, sie lächelt sogar."

    "Wer es vorher noch nicht wusste, sollte spätestens jetzt erkennen, dass diese Mädchen von einer anderen Welt sind.{w} Ich bin sicher, dass sie mit ihrer Leistung gerade einen Rekord nach dem anderen bricht."

    "Die anderen Mädchen versuchen mit Gesichtsausdrücken von purer Verzweiflung bis hin zu Neid, hoffnungslos mit ihr mithalten zu können."

    "Einige dieser Mädchen sind - oder besser gesagt {i}waren{/i} - die besten der Klasse, wenn es ums Laufen geht, aber selbst die lässt sie alt aussehen.{w} Ich möchte nicht wissen, wie es sich anfühlt, von jemandem vorgeführt zu werden, der gerade mal einen Tag auf diese Schule geht."

    "Selbst meine Augen haben Probleme damit, mit ihrer Geschwindigkeit mitzuhalten.{w} Sie scheint mit jeder Runde schneller zu werden."

    "Das kann doch unmöglich ein Mensch sein, oder?"

    "Nach dieser übermenschlichen Leistung fange ich echt an, daran zu zweifeln.{w} Ich glaube, nicht mal die besten Sportler des Landes hätten eine Chance gegen sie!"

    "Und während Sayaka all die Aufmerksamkeit erregt, fehlt jemand - und zwar ihr mürrisches Gegenstück: Hikari.{w} Wenn man jetzt logisch nachdenkt ... Sollte sie nicht auch so schnell sein?"

    "Ich suche die Umgebung ab, kann sie aber nirgends finden.{w} Wo bist du bl--oh."

    "Hinter den Mädchen, die verzweifelt versuchen, mit Sayaka mitzuhalten, sehe ich noch jemanden mit einem sauren Gesichtsausdruck.{w} Sie ... Sie geht einfach nur, und wie immer sind ihre Arme dabei verschränkt.{w} Ich frage mich, ob ihre Arme aneinanderkleben?{w} Sie versucht doch nicht einmal zu laufen."

    "Anscheinend möchte sie wirklich nicht hier sein.{w} Das war wohl alles Sayakas Idee."

    teacher "What are you all staring at?{w} Come on, let's get back to it!"

    "Da wir anscheinend alle vergessen hatten, dass wir selbst Unterricht haben, bringt uns der Lehrer zurück in die Realität.{w} Vorbei ist's mit dem schönen Anblick."

    scene bg black
    with fade

    "Der Rest der Stunde vergeht ohne großartige Ereignisse, und dann endlich, {i}ENDLICH{/i} ... Mittagspause."

    scene classroom
    with fade



    "I spot the 'magic' girls in the classroom, casually chatting away with some of the other students.{w} Huh, I didn't think they'd be able to make friends already.{w} Though after Sayaka's little display earlier, she's probably the talk of the class."

    $ sayaface='smiling'
    $ sayapose='school_1'
    show Sayaka at center
    with dissolve

    s "Oh, Kenta.{w} Hi there!"

    "She gives me a wave and a cheery smile, but I can hardly say I do the same."

    p "Okay, ja, hi.{w} Äh, können wir reden?"

    $ sayaface='normal'
    show Sayaka

    s "Hm?{w} Go for it!"

    p "Nein, nicht hier, ich mein ... Können wir unter vier Augen reden?"

    $ sayaface='shy'
    show Sayaka

    "...Crap.{w} That might have came out weird.{w} I'm getting weird looks from everyone in the class, a few of them breaking into whispers and giggles.{w} Even Sayaka is feigning surprise, despite full well knowing what I mean!"

    s "Oh my, this is a bit sudden!{w} I don't know what to say..."

    p "Komm schon, hör auf rumzualbern.{w} Ich möchte einfach nur mit euch reden, und das schon seid heute morgen."

    "Oh god...{w} I made it worse, didn't I?{w} I've somehow turned this into looking like one of the most awkward confessions ever."

    $ sayaface='joking'
    show Sayaka

    s "Are you always this forward with girls you've just met?"

    "She giggles, going along with the continued painful, {i}painful{/i} stares from the class."

    "Well...{w} If she's going to be like this, I have no choice."

    "This is going to make me look even worse in front of the class, but I need answers!"

    "I take a deep breath to steel myself.{w} And then..."

    $ sayaface='shocked'
    show Sayaka
    with hpunch

    s "Wh-wha--hey, what are you doing?"

    "I grab her by the wrist, pulling her along towards the classroom door whether she likes it or not.{w} Given what I witnessed before, I'm sure she could have me flat on the floor if she was truly opposed to this.{w} I think she's just messing around at this point, though."

    hide Sayaka
    with dissolve

    p "Und du kommst auch schön mit!"

    $ hikaface='shocked'
    show Hikari
    with dissolve

    h "Kyaa!{w} Wer hat gesagt das du mich berühren darfst?!"

    hide Hikari
    with dissolve

    "With my free hand I take hold of Hikari's wrist, no doubt cementing myself as some sort of deviant within my class.{w} Thankfully they both follow along without too much resistance."

    "Ignoring the brunt of Hikari's verbal abuse, I continue on to the doorway.{w} I just have to find somewhere quiet where no one will hear us discuss this magic and monster business.{w} The question is--"

    stop music fadeout 7.0

    p "Oof!"

    $ yuzupose='school_1'
    $ yuzuface='shocked'
    show Yuzuki
    with dissolve
    with hpunch
    with hpunch

    "In all my haste to escape the classroom with both the girls in tow, I crash into someone who was already making their way through the door."

    "They stumble backwards, looking slightly dazed.{w} Thankfully they don't look hurt."

    p "Ahh, alles in Ordnung?{w} Tut mir leid."

    "I offer her an apologetic smile.{w} ...Who is she again?{w} She must be from my class...{w}I can't recall her name at all though."

    $ yuzuface='angry'
    show Yuzuki

    dg "...Es ist gut."

    "She speaks in a cold tone, her equally cold eyes locked onto my own in an intense stare that completely betrays her words.{w} Yikes.{w} I guess she has a reason to be annoyed given my clumsiness, but this is a look of pure hate."

    p "Ähh, o-okay."

    hide Yuzuki
    with dissolve

    "Confirming she's okay, I continue on with Hikari and Sayaka, their protesting--mostly from Hikari's side--increasing in volume.{w} I can't even begin to imagine what this must look like for people passing by."

    "...I'm sure even as I head for the stairs, that girl is still staring at me.{w} Did I do something to annoy her?{w} I mean, {i}besides{/i} the clumsiness from today of course."

    "Ah, I can't worry about her for now.{w} I have bigger problems to worry about.{w} Namely, two big problems, one in each hand of mine."
    play music "bgm/magicalgirlintro.ogg" fadein 5.0
    queue music "bgm/magicalgirlloop.ogg"
    scene school roof
    with fade

    "Emerging onto the roof, I'm thankful to see it's devoid of life.{w} Safely walled by tall mesh fences, the roof is technically a spot students can spend their break at, but it really isn't that popular.{w} Works for me!"

    p "Okay, könnt ihr mir jetzt erstmal in aller Ruhe dieses Chaos hier erklären?"


    $ sayaface='happy'
    $ hikaface='angry'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "I release both of their wrists simultaneously.{w} Sayaka bounces happily, completely unbothered, while Hikari on the other hand rubs at her wrist as if I had assaulted her."

    h "Wie wäre es nächstes mal zu fragen bevor du jemanden anfässt?!{w} Du hast Glück dass wir auf einem öffentlichen Platz sind, sonst hätte ich dich in zwei Teile geschnitten!"

    s "Oh, this is exciting!{w} Is this gonna be one of those confessions I've heard so much about?"

    $ hikaface='embarrassed'
    show Hikari

    h "E-eh?{w} E-Ein L-Liebesgeständnis?{w} Zu wem?{w} Wir beide?!"

    "What the heck are they even...{w} I shake my head."

    p "Das ist kein Geständnis!{w} Ihr wisst genau, worum es geht!"

    "I can feel my face burning up.{w} It really is exhausting dealing with them."

    $ hikaface='shy'
    show Hikari

    "Sayaka gives me a teasing smile before bursting into a giggle.{w} Apparently this is the funniest thing in the world to her."

    $ sayapose='school_2'
    $ sayaface='smiling'
    show Sayaka
    with dissolve

    s "I know, I know.{w} You want an actual explanation for all of this, don't you?{w} I just couldn't help myself."

    $ hikaface='normal'
    show Hikari

    p "Danke ..."

    "I let out a sigh, my shoulders drooping.{w} Finally.{w} {i}Finally.{/i}"

    s "So what did you want to know about first?"

label rooftopexplanation:

    $ sayaface='smiling'
    $ hikaface='normal'
    show Hikari
    show Sayaka

    menu:
        "Just {i}who{/i} exactly are you guys?" if q1 is False:

            "Okay, this should be an obvious one to ask.{w} I asked it before, but only got the vague answer of them being my supposed 'guardian angels'.{w} I'm hoping she feels more generous right now though."

            $ sayaface='happy'
            $ sayapose='school_1'
            show Sayaka
            with dissolve

            s "Well, I'm Sayaka, and this is Hikari.{w} Did you forget our names already, silly?"

            "I might actually rip my hair out here."

            "I open my mouth to once more say that she knows damn well that's not what I mean, but it seems she's way ahead of me."

            $ sayaface='smiling'
            show Sayaka

            s "In all seriousness, I'm not really sure how much I'm allowed to say.{w} We're already bending the rules as it is with showing ourselves to you."

            $ hikapose='school_2'
            $ hikaface='angry'
            show Hikari
            with dissolve

            h "Ich meine wirklich, diese ganze Sache ist eine komplette Katastrophe.{w} Warum musstest du uns so viele Probleme bereiten?"

            p "Hey, das ist nicht meine Schuld!{w} G-Glaub ich zumindest ..."

            h "Sei einfach froh, dass du mir so wichtig bist, oder wir hätten dich zurückgelassen, um von diesem Ding gefressen zu werden."

            $ sayaface='shocked'
            show Sayaka

            "..."

            $ sayaface='laughing'
            show Sayaka

            "Uh...?"

            $ hikaface='embarrassed'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            "The realisation of what she said slowly dawns on her.{w} It was quite fun to watch her usually grumpy face gradually go red before she stomps in a fluster."

            h "I-Ich meinte w-wichtig für uns!{w} {i}Uns!{/i}"

            $ sayaface='joking'
            $ hikaface='shy'
            show Hikari
            show Sayaka

            s "Smooth."

            "Sayaka giggles and gives her a playful punch on the shoulder."

            $ hikaface='normal'
            show Hikari

            h "H-hmph!"

            $ sayaface='shocked'
            show Sayaka
            with hpunch

            s "Wahh!"

            $ sayaface='scared'
            show Sayaka

            "...Hikari responds in kind by giving her a wallop to the shoulder, with nothing playful about it.{w} Are these two even partners?"

            p "Wie auch immer ..."

            $ sayaface='smiling'
            show Sayaka

            "I try my best to keep things on track, though I'm sure it won't be long before it devolves into violence again."

            s "I think the most we can tell you is...{w} Hmm..."

            s "We're not from around here--rather, we were sent here specifically to ensure your safety."

            p "Gehört ihr einer Gruppe an?{w} Wartet, gibt es mehr von eurer Sorte?!"

            $ sayaface='joking'
            show Sayaka

            s "Eh-heh, I might have said too much already..."

            "She rubs at the back of her head with a grin that pretty much says, 'whoops'.{w} I probably won't be able to get any more out of her on this subject...{w}for today at least.{w} Maybe if I catch her off guard another day, she might let slip more."

            $ q1 = True

        "What was that monster?" if q2 is False:

            "I want to know more about what the heck that...{w}thing was that they saved me from earlier.{w} A 'shadow', I think she called it."

            p "Ich schätze, von diesen Dingern ... gibt es da draußen noch mehr?"

            s "Mmhmm."

            p "Und sie sind hinter mir her?"

            $ sayaface='happy'
            $ sayapose='school_2'
            show Sayaka
            with dissolve

            s "Well, in this particular case they are.{w} Though, usually they're not so aggressive.{w} But they've always been around, lurking in the, uh, shadows."

            $ sayaface='normal'
            show Sayaka

            s "It's really weird.{w} I've never seen one so brave as to attack someone in broad daylight.{w} It was like something had gotten it {i}really{/i} riled up.{w} Or...maybe..."

            "She falls into thought, leaving Hikari and I to stand awkwardly, exchanging even more awkward glances."

            p "Äh, Sayaka?"

            $ sayapose='school_1'
            $ sayaface='smiling'
            show Sayaka
            with dissolve

            "She snaps out of her stupor, blinking back to reality."

            s "Huh?{w} Oh, sorry!{w} Don't worry, it's nothing."

            p "Was hab ich verdammt nochmal getan, um diese Monster zu verärgern?"

            s "It's not what you did, it's because of who you are."

            p "Wer ... bin ich denn?"

            s "Yeah, your bloo--"

            $ sayaface='shocked'
            $ hikaface='angry'
            show Sayaka
            show Hikari
            with hpunch

            h "Sayaka!"

            s "Wahh!{w} Okay, okay.{w} Sorry."

            $ sayaface='smiling'
            show Sayaka

            "Sayaka is cut off by an ear piercing cry from Hikari.{w} Oww...{w} I guess I'll never know now.{w} Hikari seems adamant about keeping this a secret."

            $ hikaface='normal'
            show Hikari

            h "Er weiß nichts davon.{w} Es ist besser so.{w} Wie werden das Problem lösen, und endlich diese grausame Schule verlassen."

            s "You're no fun.{w} ...You're right, though.{w} Sorry, Kenta."

            "She gives me an apologetic look.{w} She really sounds sincere too.{w} Like, she's practically bursting to tell me, but just can't.{w} No use pressing it, I suppose.{w} Maybe one day..."

            $ q2 = True

        "How long are you going to stay here?" if q3 is False:
            "This is an important one.{w} Just exactly how long do they plan on staying here, to, uh, watch over me?"

            $ sayaface='scared'
            show Sayaka

            "Sayaka pulls a frown at my question, a genuinely sad looking one that tugs at my heart strings.{w} ...Was it really that bad?"

            s "It's almost like you don't want us around.{w} Are we that much of a nuisance?"

            "Damn it.{w} Why does she have to phrase it like that?{w} That's clearly not what I meant!{w} ...I think."

            "It's just...{w} As long as they're here, I'm sure there's going to be nothing but trouble in my life."

            p "Aw, komm schon, so hab ich's auch nicht gemeint ..."

            "She suddenly bursts into a bright, beaming smile again, almost blinding me."

            $ sayaface='happy'
            show Sayaka

            s "I know!{w} You're just easy to mess with.{w} I couldn't help myself!"

            "This girl..."

            "She breaks into a laugh.{w} One I'm sure can be heard by the entire school, from all the way up here."

            $ sayaface='smiling'
            show Sayaka

            s "We won't be here long, I promise.{w} Just until we've sorted things out."

            p "Ich schätze, ihr könnt mir nicht sagen, was ihr zuerst 'klären' müsst, oder?"

            $ sayapose='school_2'
            show Sayaka
            with dissolve

            "She puts a finger to her nose and winks.{w} I thought so."

            s "Top secret and all that.{w} But we're in the process of figuring this whole mess out.{w} It shouldn't take long.{w} Maybe a couple of days.{w} A week at the most!"

            $ hikapose='school_2'
            show Hikari
            with dissolve

            h "Was, eine Woche?!{w} Würde es nach mir gehen, wären wir schon morgen weg.{w} Ich hasse diesen Ort...{w} Er ist so laut."

            s "Well, if somebody was more useful, and helped me instead of just complaining all the time, we might get things done quicker, hmm?"

            "Whoa, she said that without her smile faltering one bit, her tone just as cheery despite the biting words.{w} ...That's kind of scary."

            $ hikaface='scared'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            "Even Hikari has no argument against that, those words causing her to fall silent as she shrinks back from her deceptively bright partner."

            "Uh...{w} Moving on..."

            $ q3 = True

        "That's all for now." if qquit is True:
            "I guess that's all we have time for now.{w} I think the bell for the second half is about to--"

            "Yup.{w} There it is."

            s "Oh?{w} Time to go back now, is it?"

            $ sayapose='school_1'
            show Sayaka
            with dissolve

            "She stretches her arms into the air, giving a small yawn."

            s "Well, I hope we were able to clear things up a little."

            "...Something like that."

            $ sayaface='happy'
            show Sayaka

            s "C'mon, we don't want to be late!"

            hide Sayaka
            show Hikari at center
            with dissolve

            "Sayaka bounds for the stairs as if we were in some sort of race, her partner trailing behind as she gives me one last look."

            "She stops, her eyes cast downward for a moment before flickering back up."

            h "Hey, umm..."

            p "Was ist los?"

            $ hikaface='shy'
            show Hikari

            h "...Nichts.{w} Es ist...nichts."

            hide Hikari
            with dissolve

            "And like that, she disappears down the stairs too, leaving me alone on the roof.{w} Huh.{w} I wonder what that was about?"

            "I guess I should follow after them.{w} I don't want to be late again!"

            "As I start for the stairs, my stomach makes a terrifying sound.{w} One that screams for food."

            "Oh, right, in all my haste to figure out what the girls were doing, I neglected to get any lunch at all.{w} Aww..."

            scene bg black
            with fade


            jump explanationover

    s "So, was there anything else you wanted to know?"

    $ qquit = True

    jump rooftopexplanation

label explanationover:

    stop music fadeout 4.0
    with Pause(2.5)

    "..."

    "And so, classes resume."

    "..."
    play music "bgm/everydayintro.ogg" fadein 3.0
    queue music "bgm/everydayloop.ogg"
    "After all the initial excitement in the morning, not a lot happens throughout the remaining lessons.{w} They drag on at a glacial pace, somehow even more dull than usual."

    "It also hard to keep my mind focused on anything with Sayaka and Hikari on each side.{w} There to protect me."

    "I was half expecting a monster to just burst its way through the window and for the whole place to just turn into a battleground.{w} Though...{w} It might have at least made things more lively."

    with Pause(2.5)

    scene classroom
    with fade

    "With one final ring of the bell, school comes to a close, a hazy amber glow taking over the classroom as the sun begins to set.{w} The majority of the students begin to filter out of the class to start their clubs, or part-time jobs.{w} Not me though, I'm off home!"

    "While joining a club is certainly encouraged, thankfully this isn't a place where it's enforced.{w} Meaning I'm free to loaf all I want."

    "It might make me come across as a bit of a slacker in the eyes of the other students, but eh.{w} They're not exactly wrong!"

    scene bg black
    with fade

    "Wasting no time, I set out of the school and begin to head home.{w} Something that should have been fairly stress free, but..."

    "I mean, I should have expected this, but it's still a bit much."

    scene town street night
    with fade

    "The horizon grows darker with each step I make through the quiet streets, a pale moon slowly making its presence known in the sky."

    "{i}Thud, thud, thud.{/i}{w} My heavy steps resound down the narrow road, quickly swallowed into the night.{w} But there's also another set of steps, or rather, two sets of steps that sound to either side of me.{w} Far lighter steps, with far more grace than I could ever hope to achieve. "

    p "Schau ...{w} Ich weiß, dass ihr mich nur beschützen wollt, aber müsst ihr dafür, äh, so {i}an mir kleben{/i}?"

    "Yes.{w} Those steps belonged to none other than my self professed 'guardian angels'.{w} Sayaka to my left, and Hikari to my right, they practically walk in unison with me, their shoulders inches away from mine."

    $ hikapose='school_2'
    $ hikaface='normal'
    show Hikari
    with dissolve

    h "Sei doch nicht dumm!{w} Nachts alleine heimzugehen wäre der Perfekte Moment, für den Feind, zuzuschlagen.{w} Hier müssen wir am meisten auf der Hut sein."

    "Yikes.{w} She doesn't have to yell so loud right into my ear like that.{w} I think I must be just a little bit deafer just from spending time with her today alone."

    $ hikaface='angry'
    show Hikari

    h "Denkst du ich {i}mag{/i} es, so nah zu sein?{w} Du solltest dankbar dafür sein, dss ich das überhaupt mache."

    $ hikapose='school_1'
    $ hikaface='normal'
    show Hikari
    with dissolve

    "Another 'hmph' and a turn of her head, her vibrant hair swaying gently."

    p "Ja, ja ...{w} Entschuldige."

    play music "bgm/mischiefintro.ogg" fadein 1.0
    queue music "bgm/mischiefloop.ogg"

    hide Hikari
    with dissolve
    $ sayapose='school_1'
    $ sayaface='joking'
    show Sayaka
    with dissolve

    s "Aww, don't be like that, Hikari.{w} Don't think I don't catch you sneaking glances at his face while he's looking elsewhere."

    "As she walks, Sayaka leans across me to smirk at Hikari.{w} This is getting really awkward, guys."

    hide Sayaka
    with dissolve
    $ hikaface='embarrassed'
    show Hikari
    with dissolve

    h "E-eh?{w} Du hast gesehen wie... I-Ich meine, Ich hab einfach nur nachgeguckt ob der Gegner einen Überraschungs-Angriff durchgeführt hat!"

    hide Hikari
    with dissolve
    show Sayaka
    with dissolve

    s "Sure, whatever you say~"

    with hpunch
    with hpunch
    $ sayaface='laughing'
    show Sayaka

    "My left ear is rocked by a mischievous giggle as Sayaka breaks into hysterics, all the while Hikari's face begins to turn an interesting shade of red."

    hide Sayaka
    with dissolve
    $ hikaface='shy'
    show Hikari
    with dissolve

    h "W-Wie auch immer!{w} Du bist doch diejenige, die immer deine Schulter gegen ihn drückt !{w} Was versuchst du zu tuhen?!"

    "Huh?{w} She...she was doing that?{w} Now that she mentions it, the left side did feel cozier for a time..."

    hide Hikari
    with dissolve
    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Hm?{w} I was just trying to keep him warm.{w} See, I {i}care{/i} for his wellbeing, and wouldn't want him to catch a cold."

    s "And he's not complaining, so he must like it!"

    with hpunch

    "Without warning she latches onto my arm, pulling herself in and almost sending me toppling to the ground."

    s "See~?"

    p "H-Hey, das ist jetzt aber--"

    hide Sayaka
    with dissolve
    $ hikaface='angry'
    show Hikari
    with dissolve

    h "Was machst du?{w} Du wirst ihm noch denn Arm abreißen!{w} D-Du must es sanfter machen, so wie ich..."

    $ hikaface='shy'
    $ hikapose='school_2'
    show Hikari
    with dissolve
    with hpunch

    "E-eh?{w} Hikari latches onto my other arm, hooking it within hers in an attempt to tug me away from Sayaka.{w} What the heck did this turn into?"

    p "Mädels, ihr müsst echt nicht--"

    hide Hikari
    with dissolve
    show Sayaka
    $ sayaface='smiling'
    $ sayapose='school_1'
    with dissolve

    s "Mmm.{w} No.{w} That isn't how you do it all, Hikari!{w} It's more like..."

    $ sayaface='happy'
    show Sayaka
    with hpunch

    "Sayaka pulls back on my arm, and soon they both have a firm grip of each of my arms, determination across their faces as I become some sort of human rope."

    with hpunch

    "What is this, tug of war?{w} They're going to rip me apart!"

    hide Sayaka
    with dissolve
    $ hikaface='embarrassed'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Hah!{w} B-Bitte!{w} {i}Das{/i} wird so gemacht!"

    with hpunch

    "Do they even remember what they were trying to do?!{w} What started innocently enough has now spurred into some sort of contest between them.{w} They really are competiti--ow!{w} Now's not the time to think about stuff like that!"

    p "Könntet ihr mich bitte ...{w} LOSLASSEN!?"

    hide Hikari
    with dissolve
    with hpunch

    "Raising my voice more than I've ever done in a while, I explode, my body at stake here!"

    "And like that, they both let go of my arms at once, leaving me free to ensure they're both still fully intact."

    "I'm glad they listened to reason.{w} I really thought I was going to die there.{w} Apparently it's not the monsters I have to worry about anymore, it's these two!"

    p "Äh, Mädels?"

    stop music fadeout 2.0
    $ sayaface='normal'
    $ hikaface='normal'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "...At least, I had {i}thought{/i} it had been my desperate cry that had gotten through to them, but they seem completely transfixed by something up above."

    "What are they looking at?{w} I squint my eyes and gaze high above the rooftops."

    "And then, as the clouds part and the pale moonlight shines down, I see her."

    scene cg11
    with dissolve
    play music "bgm/evilgirlintro.ogg"
    queue music "bgm/evilgirlloop.ogg"

    "A girl sits on the ledge of the highest point of one of the tallest buildings in the area."

    "Silvery hair that seems to glimmer in the moonlight, and an outfit as dark as the night sky, she gives off a awe inspiring look, almost angelic.{w} Like...she's some sort of angel, gazing down from the heavens."

    "At least, I {i}would{/i} call her an angel if it wasn't for that unsettling grin that just now spread across her face at the sight of us."

    dg "Ahhh.{w} Da bist du ja."

    "She murmurs something to herself that I can't make out at all from the distance between us.{w} Whatever it was she said, it was enough to make her shoulders shake with laughter."

    "I can't help but feel like I've seen her somewhere before...{w} I wonder why that is?"

    "No matter how hard I try to think back, I can't recall her face at all, though."

    "In a burst of feathers, obsidian wings unfurl from behind her.{w} Now those {i}definitely{/i} aren't holy.{w} I've got a bad feeling about this..."



    "Amber eyes peer down at the three of us, narrowed in determination as the same unsettling grin remains.{w} ...It might just be my imagination, but I think she's looking at {i}me{/i} specifically.{w} I can...almost feel her stare."

    "It's enough to send a chill down my spine, and sparks a faint pulse at the back of my skull."

    p "Eine ... Eine Freundin?"

    "I force out a laugh, though I know the truth.{w} The air is growing tense, like that time with the monster before, and the looks on both Hikari's and Sayaka's faces can only suggest something bad is about to go down."

    s "Hah.{w} 'Fraid not.{w} Kenta, get back.{w} I don't like this at all..."

    p "Aber ...{w} Okay, okay."

    "I do as I'm told and retreat back a good distance, not really wanting to argue when they look as scary as they do."

    s "So, what do you think we're dealing with here?"

    h "Sie sieht viel zu nach Mensch aus, um ein Schatten zu sein...{w} Aber, ich bekomme das gleiche Gefühl von Angst, in ihrer Anwesenheit."

    s "Ahh, gotcha.{w} ...I think.{w} ...Wait, so {i}is{/i} she a monster or not?"

    h "Das versuch ich rauszufinden!{w} Wenn du für eine Sekunde aufhören würdest, in mein Ohr zu schreien, könnte ich mich konzentrieren..."

    s "I'm not yelling!{w} Sheesh."

    h "Richtig.{w} Ich hab's vergessen.{w} Das ist ja deine Standard Lautstärke.{w} Also dann, sei einfach ruhig und lass mich über die Dinge nachdenken."

    s "You're so cruel sometimes, Hikari..."

    "The silver haired girl, still high atop the roof, gives me one last look, before turning her gaze to the girls.{w} And then she jumps."

    scene town street night
    with dissolve

    "...What?!{w} Why did she jump?!{w} I-I can barely watch."

    "She plummets downwards, towards where my guardians are stood, no hint of even beginning to slow down.{w} Are those wings just for show?"

    "Faster and faster she descends, before finally the pavement closes in...{w} I don't want to watch.{w} But...{w} Somehow I get the feeling she wouldn't have jumped without a good reason.{w} At least, I {i}hope{/i} she didn't."

    p "...!"

    "Mere inches from smashing into the ground, her wings spread wide as if brakes, before bringing her to a sudden stop.{w} Not even a gradual halt.{w} She just comes to a complete, grinding halt, as if the laws of gravity don't apply to her."

    "Even with wings, something like that shouldn't be possible.{w} I mean, if a pigeon were to attempt something like that, they'd barely be recognisable on the pavement right now!"

    "In fact, her feet aren't even touching the ground.{w} She hovers above ever so slightly, before stepping onto the solid surface, as if stepping off of an invisible platform."

    "Part of me is relieved that she isn't hurt from that little stunt.{w} But then part of me is also terrified as to what might happen next."

    $ yuzupose='magical_1'
    $ yuzuface='joking'
    show Yuzuki at left
    show Sayaka at right
    show Hikari at center
    with dissolve

    "The silver haired girl stands before Hikari and Sayaka, her expression still as unsettling as ever.{w} Despite the smile though, there's nothing in her posture that would suggest she has any bad intentions, yet the other two girls are tense."



    "My head rings just trying to focus on her, like that monster from before.{w} Is she...related to them?{w} I clutch a hand to my head and try to steady myself.{w} It's taking all of my willpower just to keep upright at the moment."

    dg "Guten Abend, Mädchen."

    "She greets them so casually, despite the intense glares directed her way.{w} Somehow...{w} I get the feeling she didn't leap off a freaking {i}roof{/i} just to exchange pleasantries."

    h "...Lass uns der auf Jagd gehen, sollen wir?{w} Wer bist du, und was willst du?"

    $ yuzupose='magical_2'
    $ yuzuface='happy'
    show Yuzuki
    with dissolve

    dg "Bist du nicht mein feinlicher Haufen?"

    "She lets out a devious giggle, doing little to ease the tension in the air."

    dg "Sehr Gut.{w} Du kannst mich Yuzuki nennen.{w} was ich mein ist später...{w} Gut..."

    $ yuzuface='joking'
    show Yuzuki

    "Her eyes flit from the girls and settle straight onto me, her smile enough to send a chill down my spine."

    y "Ich werde den Jungen nehmen, wenn es dir nichts ausmacht.{w} Siehst du, er ist {i}sehr{/i} wichtig für mich."

    $ hikaface='angry'
    $ sayaface='scared'
    show Hikari
    show Sayaka



    "...!"

    "I knew it.{w} Of course she would be linked to this whole mess.{w} Why wouldn't she be?"

    "Today is the day where everything apparently wants me dead."

    $ hikaface='normal'
    $ sayaface='normal'
    show Hikari
    show Sayaka

    "Sayaka and Hikari refuse to comply.{w} I mean, of course they wouldn't.{w} They wouldn't be very good guardian angels if they had just stepped aside for this maniacal girl."

    $ yuzupose='magical_1'
    $ yuzuface='happy'
    show Yuzuki
    with dissolve
    stop music fadeout 9.0
    y "...Nein?{w} Ich denke wir müssen die Dinge auf die harte Tour machen, hmm?"

    "The pair stand tall before me, their fists tightened.{w} I think there's only one way this is going to end up."

    "The air around them seems to crackle, the amount of power contained within them all immense."

    "..."

    "I'm afraid to even take in a breath, in case I set something off.{w} This is dangerous.{w} Even {i}I{/i} can see that."

    with Pause(3.5)

    "I blink, and..."


    play music "bgm/battleintro.ogg"
    queue music "bgm/battleloop.ogg"


    $ yuzuface='angry'
    $ hikapose='magical_2'
    $ sayaface='scared'
    $ hikaface='scared'
    show Yuzuki
    show Hikari
    show Sayaka
    with flash
    show Hikari at right
    show Sayaka at offscreenright
    with move

    "Yuzuki lunges for them in a flash, with a scythe seemingly torn out from the air itself."

    $ hikaface='angry'
    $ hikapose='magical_1'
    show Hikari
    with dissolve

    s "W-wahh!"

    "Sparks fly from the collision of metal against metal.{w} Hikari was just barely able to react in time, changing her outfit in a flash and blocking the blow with her sword.{w} If she had been any slower there, they might not have had their heads still."

    h "Nnngh.{w} Ich wusste es!{w} Du bist einfach nur eine Puppe zu {i}ihr{/i}!"

    "She speaks through gritted teeth, pushing with all her might to try and keep the scythe at bay as it draws ever closer.{w} It seems like a fight she might lose though, as the silver haired girl presses on without even so much as a bead of sweat on her brow."

    show Yuzuki at center
    show Hikari at center
    with MoveTransition(0.2)
    with hpunch
    show Yuzuki at right
    show Hikari at left
    with move

    h "Sayaka!{w} Fühl dich frei mir jederzeit--grghh-- zu helfen!"

    hide Yuzuki
    hide Hikari
    $ sayaface='shocked'
    show Sayaka at center
    with dissolve

    s "Huh?{w} Oh, right!"

    "Losing ground quite rapidly, her feet beginning to slide back from the force, Hikari barks at her partner who had just about recovered from the shock of the strike."

    "They really are in trouble here...{w} And all I can do is stand gawking.{w} I know for sure if I go anywhere near them, I'll be torn apart.{w} This is a fight on a completely different level than me."

    $ sayaface='normal'
    $ sayapose='magical_1'
    show Sayaka
    with flash

    "There's another blinding flash as Sayaka transforms herself, wielding the same bow I had seen her use this morning."

    scene cg15
    with dissolve

    "She dashes back a little from the clashing girls and preps her bow, pulling back the string.{w} I was about to wonder just where the arrow was, but one seems to just blink into reality, already fully nocked onto the bow."

    "She lets the magical arrow fly, her target obvious."

    with flash

    "Caught up in the clash, Yuzuki has no choice but to pull away from Hikari.{w} She kicks back gracefully, the arrow just inches away from grazing her cheek."

    h "Genau rechtzeitig!"

    scene town street night
    show Hikari at center
    show Sayaka at right
    with dissolve

    "Hikari heaves a sigh of relief as she eases her shoulders, finally able to rest, if only for a moment.{w} The fight is clearly {i}far{/i} from over."

    "The girls regroup, and ready themselves, their mysterious opponent now going over them with her unsettlingly cold eyes."

    h "Sei vorsichtig, Sayaka.{w} Sie ist stark.{w} Ich konnte sie kaum zurückhalten."

    "Sayaka nods, a look of determination painting her face that I wasn't even aware she was capable of."

    $ yuzupose='magical_2'
    show Yuzuki at left
    with moveinleft

    "Taking just a moment to analyze the situation, the dark girl closes in again for a second round."

    $ yuzuface='joking'
    show Yuzuki

   y "hah, ist das alles was du kannst?{w} Das wird viel {i}einfacher{/i} als ich mir vorgestellt habe."

    $ yuzupose='magical_1'
    $ yuzuface='happy'
    show Yuzuki
    with dissolve
    $ hikaface='scared'
    $ sayaface='scared'
    show Yuzuki at right
    show Hikari at left
    show Sayaka at center
    with MoveTransition(0.2)
    with Pause(1.5)
    $ hikaface='angry'
    show Hikari at center
    show Yuzuki at center
    show Sayaka at left
    with MoveTransition(0.2)
    with hpunch
    show Hikari at right
    show Yuzuki at left
    show Sayaka at offscreenleft
    with move
    show Hikari at center
    show Yuzuki at center
    with MoveTransition(0.2)
    with hpunch
    show Hikari at left
    show Yuzuki at right
    with move

    y "Ah, das macht so viel Spass! {w}Und da dachte ich, dass die kleinen "Wächter" dieses Jungen tatsächlich eine Bedrohung darstellen könnten. {w} Wie dumm von mir!"

    h "S-Sei ruhig!{w} Es ist noch nicht vorrüber!"

    "She twirls her scythe with ease and swipes at the pair with the same maniacal expression.{w} Each strike is either just barely dodged by the girls, or just about deflected by Hikari's desperate counter-attacks."

    "This is a completely one-sided fight...{w} If that wasn't already clear from the moment this girl had made her first move."

    "She's able to take both of them on with no problem, blocking whatever attack Hikari might be able to muster in her position, and chasing after Sayaka whenever she attempts to make some distance between them for her bow."

    h "Fein!{w} Mal sehen, ob du bei dieser Geschwindigkeit ausweichen kannst!"

    show Hikari at center
    show Yuzuki at center
    with MoveTransition(0.2)
    with hpunch
    show Hikari at offscreenright
    show Yuzuki at offscreenleft
    with MoveTransition(0.3)

    "...Whoa."

    with hpunch

    "They're moving so fast now my eyes can hardly keep up with it all, the action eventually just turning to colorful blurs as the fight drags on, battle cries and the clash of steel filling the air."

    with hpunch
    with hpunch

    "The street around them is becoming completely wrecked.{w} Lampposts are split in two, parked cars are being sent flying, and even chunks of the road itself are being chipped away every time they collide together."

    show Sayaka at right
    with moveinleft
    $ sayaface="shocked"
    $ hikaface="scared"
    show Hikari at offscreenleft with dissolve
    show Sayaka
    show Hikari at center
    with move
    with hpunch
    show Sayaka at offscreenright
    show Hikari at offscreenright
    with move
    show Yuzuki at left
    with moveinleft

    "Without warning the intense speed grinds to a halt.{w} Sayaka is suddenly sent tumbling to the ground, Hikari shortly following as the silver haired girl stands triumphant, not a single scratch upon her."

    stop music fadeout 6.0
    scene cg14
    with fade

    s "Wahhh!"

    h "Oof!"

    "They end up tangled in a heap together, both of them fairly dazed."

    "Thankfully they don't seem too hurt, but they certainly each have their fair share of bruises."

    p "G-Geht es euch gut?!"

    "Unable to keep myself from cowering any longer, I call out to them, taking a step towards the carnage."



    "I freeze up completely as the silver haired girl's hollow eyes flutter onto me.{w} Her gaze is frightening.{w} Paralyzing.{w} She came here for me.{w} Just like that monster did before."

    "Do I have a sign on my back that says 'kill me' or something?!"

    h "Was machst du, du Idiot?!{w} Bleib zurück!{w} W-wir sind ...-- argh -- uns geht es gut!"

    "Hikari rouses me to my senses with her harsh cry.{w} It's a bit hard to believe she's fine when she's completely tangled up with her partner though...{w} They're both flailing helplessly in an effort to get up."

    play music "bgm/mischiefintro.ogg"
    queue music "bgm/mischiefloop.ogg"

    s "Is this my leg or your leg?{w} I can't tell!"

    h "Ow!{w} Schlag es nicht!{w} Das wird nichts lösen!"

    s "Ohh...{w} So it was {i}your{/i} leg.{w} Okay, I get it!"

    h "Warum schlägst du es immer noch?!"

    h "Aber...{w}geh einfach von mir runter!{w} Nnghh, du bist so schwer!"

    s "H-heavy?{w} Me?!"

    h "Ja, du!{w} Wenn du nicht so ein Vielfraß wärst, wären wir vielleicht nicht in dieser Situation!"

    s "It's not my fault I like to eat!{w} I think you're just jealous I can eat tons and get away with it."

    s "I've seen what happens when you pig out, Hikari.{w} It's like, you triple in size!"

    h "E-Entschuldige?!{w} Du hast Glück dass ich nicht an mein Schwert komme, oder ich würde..."

    h "Ow!{w} Hast du mich gerade gebissen?!"

    s "Mmm.{w} You can't prove anything!"

    h "D-Du bist so ein Wilder!"

    "This is a complete disaster..."

    stop music fadeout 1.0

    "With my supposed guardians still trying to sort themselves out, I'm left helpless as Yuzuki advances towards me.{w} She takes slow, deliberate steps, almost as if she was enjoying the look of sheer terror across my face."

    scene town street night
    $ yuzupose='magical_2'
    $ yuzuface='joking'
    show Yuzuki at center
    with dissolve
    play music "bgm/evilgirlintro.ogg"
    queue music "bgm/evilgirlloop.ogg"
    
    y "Jetzt sind sie aus dem Weg...{w} Lass uns ein bisschen Spass haben, sollen wir?"

    "{i}Thump.{w} Thump.{w} Thump.{/i}{w} My heart is going to rip out of my chest at this rate."

    "I should run.{w} But I can't.{w} Why can't I run?{w} My body isn't listening to anything I tell it at all."

    "The distance between us is almost gone.{w} Is she going to kill me?{w} ...Why me?{w} What did I ever do to deserve this?!{w} I mean, as far as I know, I've lived a normal, peaceful life."



    "The closer she gets, the more vivid my headache becomes.{w} The air around me is heavy, suffocating.{w} Even the simple act of taking in a breath is becoming too much for me in this state."



    "Her amber eyes narrow.{w} She tightens her grip on her scythe."

    p "W--...{w}Warum ...?"

    y "Oh, es ist nichts persönliches.{w} So müssen die Dinge sein, wenn ich mein Leben wieder auf Kurs bringen will."
   

    $ yuzupose='magical_1'
    $ yuzuface='angry'
    show Yuzuki
    with dissolve

    y "Jetzt.{w} Sag Gute Nacht."

    "She lashes at me like lightning, a clear intent to kill.{w} I can't even lift my arms to try and defend myself.{w} It's...it's over."

    $ yuzuface='shocked'
    show Yuzuki
    with flash
    hide Yuzuki
    with dissolve

    "Right before the wicked blade comes into contact with me, a bright bolt of what I can only assume is magic whizzes in from the side and catches the girl off-guard, knocking her off balance and prolonging my life for just a little while longer."

    $ sayaface='angry'
    $ hikaface='normal'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "Looking back over at what was once a disaster zone, it appears that Hikari and Sayaka are finally back on their feet.{w} Sayaka has her hand outstretched, plumes of smoke rising from the tips of her fingers.{w} I guess I owe her one here."

    $ sayaface='normal'
    show Sayaka

    s "That was too close.{w} I...{w} I think it's time for a 'tactical retreat', wouldn't you agree?"

    $ hikaface='shocked'
    show Hikari

    h "Eh?{w} Werden wir wirklich einfach rennen?!{w} Ich kann noch --nggh-- {w} Ich kann noch kämpfen!"

    s "Oh, shush!{w} You can barely stand.{w} Come on!"

    hide Hikari
    hide Sayaka
    with dissolve

    "While our opponent is still reeling from the attack, my saviours take this opportunity to dash toward me, each of them hooking an arm around me as their weapons shatter into crystals and begin reforming into familiar wings upon their backs."

    p "W-Wartet, was macht ihr?"

    s "Hold on tight, okay?"

    "Before I can protest any further, they both kick off of the ground, and we...{w}begin to ascend.{w} Up.{w} Into the air.{w} We're...{w}we're flying.{w} We're actually flying."

    p "Was?!{w} Hey, nein, lasst mich runter!{w} Können wir nicht einfach weglaufen?!"

    with hpunch

    h "Hör auf herumzuprügeln, wir werden fallen, du Idiot!"

    p "Da mach ich nicht mit!{w} Das ist verrückt!{w} Uff.{w} Ich ...{w} Ich ...{w} Ich glaub, ich muss kotzen."

    h "Hey, wag es nicht, oder du wirst dir wünschen, du wärst noch da unten bei diesem Freak eines Mädchens!"

    "We continue to trail through the sky, bursting through the clouds as if it were nothing."

    "The wind roaring past me, the glimmering city lights below, the...{w}the turbulence from being carried by the pair...{w} It's all so nauseating.{w} I really don't know if I can stand much more of this."

    s "Do you think we lost her?"

    "Slowing to a gentle hover, and keeping me firmly in their grip--I hope, at least--they throw a glance over their shoulders only just now being able to catch a breath."

    h "Ich denke schon.{w} ...Ich kann nicht glauben, dass wir fliehen mussten."

    s "Hey.{w} Hey.{w} We didn't {i}flee{/i} okay.{w} It was a tactical retreat!"

    h "Ugh.{w} Nenn es so wie du willst, aber wir hatten Glück dass wir unsere Köpfe intakt gehalten haben."

    "...Silence takes over the pair as they fall into thought."

    p "Also, äh ..."

    s "Huh?{w} Kenta?{w} Oh, I'd almost forgotten about you, sorry!"

    "That's a bit worrying...{w} Considering you're the only thing keeping me from falling to a painful and gruesome death!"

    s "You're not hurt, are you?"

    p "Nein, mir geht's gut.{w} Es ist nur ...{w} Könntest du mich, äh, du weißt schon ..."

    with hpunch

    p "MICH RUNTERLASSEN?!"

    s "Right, right.{w} I think it's safe now.{w} Down we go!"

    "We begin to descend, from out of the clouds, and it isn't long before my feet finally come into contact with the ground again.{w} The safe, wonderful ground!{w} I have to restrain myself from wanting to kiss it."

    "I collapse onto my knees, my stomach heaving.{w} Never again.{w} Flying just isn't for me."

    $ sayaface='scared'
    show Sayaka at center
    with dissolve
    with hpunch

    s "You okay there?"

    "Sayaka gives me a solid pat on the back, which does little in the way of helping my stomach."

    p "...Hör auf ..."

    $ sayaface='smiling'
    show Sayaka

    s "Hmm?"

    "I can barely get my words out, after such a traumatic experience!{w} I take in a deep breath and try again."

    p "Macht das ja nicht noch einmal.{w} Zumindest nicht, ohne mich vorher zu fragen!"

    $ hikapose='magical_2'
    $ hikaface='angry'
    show Sayaka at left
    show Hikari at right
    with dissolve

    h "Es war ein Notfall, du Schwächling!"

    with hpunch

    "Hikari takes her turn to pat me on the back.{w} Though, it's more of a thump than anything, like a punch.{w} Urff..."

    h "Glaubst du, ich hab es genossen dich so lange festzuhalten?"

    p "Okay, okay, ich versteh schon.{w} Hört bloß auf ...{w} mich zu tätscheln.{w} Urghh ..."

    "Sayaka circles around and bends forward to look at me, concern across her face."

    $ hikaface='normal'
    $ sayaface='shocked'
    show Sayaka
    show Hikari

    s "Whoa, I don't think I've ever seen someone's face go so green before!{w} Not a big fan of flying, I guess?"

    p "Ach, echt jetzt? Wie kommst du darauf?"

    "I take a moment before finally straightening myself up.{w} Okay.{w} I think I'm good now."

    $ sayaface='normal'
    show Sayaka

    "While I was recovering, it looks like Sayaka and Hikari were keeping guard, watching deep into the night for any signs of life.{w} But, it looks like they weren't bothered enough to pursue.{w} Weird."

    p "Okay, ich weiß, dass ich euch seit unserem ersten Treffen nur Fragen gestellt hab, aber--"

    s "If you're wondering who that creepy girl is, I honestly have no idea."

    p "Bist du dir da sicher?{w} Sie sieht genauso aus wie ihr.{w} Ihr wisst schon, wie eine Zauberin, und mit Flügel ..."

    $ sayaface='angry'
    $ hikaface='angry'
    $ hikapose='magical_1'
    show Sayaka
    show Hikari
    with dissolve

    "...Whoops.{w} I might have said the wrong thing here.{w} They both turn to me, fire in their eyes.{w} Even Sayaka, who I thought was pretty easy going, seems angry at me here."

    h "Hast du uns damit verglichen...{w}dem Ding?!"

    p "Ahh, das wollte ich nicht--"

    with hpunch

    h "Es gibt eine Welt aus Unterschieden zwischen uns, und was auch immer sie war!"

    h "Zum einen, hast du nicht {i} ihre {/i} Augen gesehen?{w} Sie war komplett verrückt .{w} Es gab keine Spur von Vernunft."

    $ hikaface='scared'
    show Hikari

    "Hikari wraps her arms around herself to fight off a shiver."

    h "Schon allein an sie zu denken, macht mir Angst."

    $ sayaface='normal'
    show Sayaka

    s "I guess looking at it from your perspective, Kenta, she might seem the same as us...{w}with her general look, and how her magic seems to work."

    s "But everything about her is twisted.{w} The dark shades, the black wings, even those horns!{w} It's like they set out to become the complete opposite of what we are."

    s "Nothing about her power seems natural either..."

    $ hikaface='normal'
    show Hikari

    p "Äh, und ... welche Kraft hast du?"

    $ sayaface='smiling'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Of course!{w} We worked hard to get to where we are today, you know!{w} It's not like we were just born like this!"

    $ sayaface='normal'
    show Sayaka

    s "With her though, it's like it was just..."

    "She falls silent, deep in thought.{w} Man, I really don't get any of this.{w} All I know, is that apparently those monsters aren't the only thing I have to fear now."

    "Apparently done thinking, Sayaka snaps back into reality and grins."

    $ sayaface='smiling'
    show Sayaka

    s "I think we've had enough excitement for one day, anyway.{w} How about we get you home now?"

    "She reaches out to take a hold of my arm, but I'm one step ahead and jump back.{w} I can already tell what she had in mind!"

    $ sayaface='shocked'
    show Sayaka

    p "Bitte nicht nochmal fliegen!{w} Wir gehen, okay?{w} Wir GEHEN!"

    $ sayaface='happy'
    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "Aww.{w} If you're sure.{w} It's much safer in the skies, though."

    "Like hell it is!{w} I was lucky I didn't have a heart attack when they were dragging me through the clouds like that."

    "Completely shattered after all the events of today, we start the journey back home."


    stop music fadeout 4.0
    scene bg black
    with fade

    "It isn't long before we arrive back at my house.{w} And I can happily say we ran into no more monsters or crazy scythe wielding girls along the way.{w} ...I can't believe I even have to take them into consideration now.{w} What has my life become?!"

    "Reaching the front door of my house however, I'm posed with a problem.{w} These two girls insist on protecting me, and were just about to follow me straight into my house before I realised they were still there."
    play music "bgm/ominousintro.ogg"
    queue music "bgm/ominousloop.ogg"
    "Somehow I get the idea my parents might be opposed to me bringing in two complete strangers.{w} Girls, at that.{w} Plus that would just lead to a whole new line of questions from them, and I'd rather not get them involved into this mess too."

    "So, it took a while, and a {i}lot{/i} of negotiating--and I really mean a lot, I was pretty much on my knees at one point--but I was able to persuade them that I would be perfectly safe in my house."

    "They finally withdrew for the night, giving me some much needed room to breathe.{w} They did say they wouldn't be too far away, though, if I ever needed them...{w}and that worries me."

    scene kitchen night
    with fade

    "I close the front door and almost collapse against it with a drawn out sigh, any borrowed strength I might have had up until this point draining from me completely."

    p "Was für ein Tag."

    "My head aches.{w} My arms throb.{w} My legs feel like they're about to give way.{w} I can't believe I'm even still standing after all that."

    "The smell of food is heavy in the air, the aroma enough to make my mouth water.{w} Oh.{w} Right.{w} I think I had forgotten to eat today.{w} I should probably fix that, if I want any chance in surviving what tomorrow might bring me."

    "Apparently I'm just in time, as the food is all set on the table, with my parents about to dig in."

    "This short window of time in the evening is really the only chance I ever get to see my parents outside of the holidays.{w} So I usually cherish these dinners, and try to engage with them as best I can."

    "But today I can hardly even get a word out.{w} I sort of just, grunt in their direction before I collapse into the dining chair."

    "As the meal goes on, the usual questions come up between us, such as how our days had went, and if I had been up to much.{w} ...Hah.{w} Despite looking completely shattered, I say it was just like any other day."

    "I get concerned looks, but they don't have any reason to doubt me."

    "Before long, dinner is finished.{w} And after several extra helpings, I can't think of anything better to do than to call it an early night.{w} I make myself excused and head for my room, my steps unsteady."

    scene bedroom night
    with fade

    "I drop onto my bed, face first, the mattress giving out a groan.{w} It can't be any later than 9PM, and already I want to sleep.{w} Is every day going to be like this from here on out?{w} I hope not."

    "While I could just as easily fall asleep in the current position I'm in, there's probably a good risk I might suffocate, so I guess I might as well do things the proper way.{w} If I have to.{w} Ugh."

    "I push up off of the bed and go to close the curtains."

    "..."

    "Huh.{w} Maybe I already fell asleep."

    "As I went to close the curtains, my eyes are drawn to an amber glow down in my garden.{w} A fire.{w} A campfire, to be precise.{w} I'll give you three guesses as to who that campfire belongs to."

    "Yup.{w} The two 'magical' girls."

    "Sayaka and Hikari seem to have taken it upon themselves to set up a little base camp in my back garden, complete with a tent and fire.{w} I guess when they said they'd be close by, they {i}really{/i} meant close by."

    "I think they're trying to cook something, going by the pan over the fire.{w} I didn't realise their lives were so rough, with how glamorous they generally look."

    "Oh, they saw me.{w} Sayaka gives an enthusiastic wave my way, taking her eyes off the pan.{w} Yeah, okay, hi.{w} I give a feeble wave back."

    "Somehow I get the feeling I should be worrying about this far more than I am.{w} But.{w} Whatever.{w} This can wait until tomorrow."

    "I draw the curtains shut, right as whatever Sayaka was cooking in the pan ignites into a tremondous fire.{w} I can just about hear Hikari's cry of terror through the window panes."

    "Letting out one final, mighty yawn, I flop backwards onto my bed, and it's not long before whatever semblance of consciousness I might have had left drifts into the night."
    stop music fadeout 4.0
    scene bg black
    with fade





    scene bedroom day
    with wake
    play music "bgm/everydayintro.ogg"
    queue music "bgm/everydayloop.ogg"
    "Streams of light filter in from the curtains, rousing me out of sleep that I wanted to last forever."

    p "Blughh ..."

    "I have half a mind to just turn over and wrap myself tighter in my blanket, but I guess I have enough to worry about right now without adding 'being late to school' on top of everything else."

    "Let's...{w}tackle the day.{w} I guess."

    with hpunch

    "I roll out from under the covers, and crash to the floor with the grace of a sloth.{w} Ow."

    "On top of everything else still aching from yesterday, my head thumps once more, right on schedule.{w} I really wish it would cut me a break.{w} Just this one time!"

    "Starting from a crawl along the floor, and gradually pulling myself up into a walk as if I was evolving in real time, I tug the curtains open."

    "Huh.{w} I look down at the garden to find it completely empty.{w} Not a trace of a fire, the tent, or the girls.{w} Maybe I really was dreaming last night?"

    "I mean, they couldn't really be as stupid as to camp in plain sight like that.{w} The fire alone would be enough for the police to be brought down!"

    "That's one less thing for me to stress about at least.{w} Thank god."

    "Right!{w} I better not waste any more time, or I'm going to miss my chance to have a proper breakfast like yesterday."

    "Pawing at the dust around my eyes, I start for the bathroom.{w} A nice, hot shower should do wonders."

    "I pull open the door to the bathroom and--"

    scene cg3
    with wake

    p "Wa ..."

    "The bathroom is occupied."

    h "W-Was zum Teufel gaffst du hier?{w} Schließ die Tür!"

    p "'Tschuldige, mein Fehler ..."

    scene bg black
    with fade

    "I slam the door back shut, my heart an erratic mess.{w} That was a close one."

    "...Wait a second.{w} Something isn't adding up here."

    scene cg3
    with dissolve

    "I swing open the door again, the sight taking away my breath once more, even though I already knew what to expect."

    h "Ahh!{w} Was machst du jetzt?!{w} Du Perversling!"

    "I knew it!{w} It {i}is{/i} Hikari!{w} An, uh...{w}rather under-dressed Hikari at that.{w} She's caught like a deer frozen in headlights, her entire body tensing up in a near statuesque pose."

    "She's down to her rather extravagant underwear, if you don't count the socks she was in the process of taking off.{w} Huh, they match and everything."

    "With how she's bent forwards like this, my eyes can't help but gravitate to her rather ample--"

    with hpunch

    h "Kenta!"

    p "H-Häh?"

    "I'm snapped out of whatever daze I might have been in by her shrill tone.{w} What...{w}what was I doing again?"

    h "Was machst du?! Mach jetzt endlich die Tür zu!"

    p "Warte.{w} Wartewartewarte.{w} Sollte ich nicht dir die Frage stellen, was {i}du{/i} in {i}meinem{/i} Haus machst?!"

    h "Wie siehts wohl aus, du Genie?!{w} Jetzt geh weg!"

    "Her face is beet red.{w} She's practically trembling with anger, though still frozen in place.{w} But how am I the one at fault here?"

    p "Hey, werd jetzt bloß nicht wütend!{w} Ich kann mich nicht erinnern, dass ich euch die Erlaubnis gegeben hab, mein Haus zu betreten.{w} Und erst recht nicht meine Dusche!"

    h "SCHLIEß{w} DIE{w} TÜR."

    p "Erst, wenn du--"

    with hpunch

    h "{i}SCHLIEß{w} DIE{w} TÜR!{/i}"

    p "Okay, aber könntest du ...{w} Äh ..."

    "Her eyes give off a dangerous glow, the room rumbling ever so slightly with a frightening power.{w} ...Uh, I guess this can wait until afterwards.{w} If I want to keep my house intact, at least."

    p "O-Okay, okay!{w} Es tut mir leid ...{w} Wirklich!"

    "Flashing an apologetic smile and laughing nervously, I bring the door to a close once more.{w} As demonstrated last night, sometimes retreating is the best course of action."
    stop music fadeout 3.0
    scene bg black
    with fade

    "Well.{w} After that little, uh, 'situation'--I find myself downstairs, both of the girls present."

    scene kitchen day
    $ sayapose='school_1'
    $ sayaface='smiling'
    $ hikapose='school_2'
    $ hikaface='angry'
    show Sayaka at left
    show Hikari at right
    with fade
    play music "bgm/everydayintro.ogg"
    queue music "bgm/everydayloop.ogg"

    "Sayaka has the same cheerful grin as ever, while Hikari looks like she wants to grab the nearest sharp object she can find and gut me with it.{w} Again--that wasn't my fault, how was I supposed to know?!"

    p "So ...{w} Findet ihr nicht, dass ihr mir eine Erklärung schuldig seid?"

    s "Hmm?"

    "She tilts her head, giving me a confused look.{w} Oh, come on!{w} How can I be the only one to find something strange with this?"

    p "Na ja, ich mein ...{w} Was macht ihr bei mir Zuhause?{w} Und warum benutzt ihr mein Eigentum!?"

    $ sayaface='happy'
    $ sayapose='school_2'
    $ hikaface='normal'
    show Hikari
    show Sayaka with dissolve

    s "Oh, that's simple!{w} Since we've been watching over you for a while now, we noticed that your parents always seem to leave really early in the morning, and that you're the only other one that lives here."

    s "So we figured it'd be fine if we just...{w}y'know, let ourselves in, to borrow the shower and stuff."

    p "...Um es anders auszudrücken, ihr seid eingebrochen."

    $ sayaface='joking'
    show Sayaka

    s "Eh-heh-heh-heh, that's a bit of an extreme way to put it.{w} We made sure to fix the window, you know!"

    p "WIE BITTE?!"

    "I quickly throw a glance about, looking for any windows in sight.{w} No trace of a break in at least...{w} Jeez, what did they do, throw a brick through one?{w} I thought people who knew magic would be more subtle!"

    s "See?{w} It's all good."

    $ sayaface='happy'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    "She tries her best to reassure me with her limitless optimism, her hands on her hips with a blinding smile.{w} I can't say I mirror her enthusiasm though."

    "I bring a palm to my forehead, a headache beginning to set in.{w} And for once, I know the cause of this one."

    p "Ist das echt nötig?{w} Könnt ihr euch nicht einfach, ihr wisst schon, sauber zaubern, oder so?"

    $ sayaface='normal'
    $ hikapose='school_1'
    show Sayaka
    show Hikari with dissolve

    "..."

    "I get cold stares from both of them.{w} ...I said the wrong thing again, didn't I?"

    h "Kenta, deine Magie ist nicht einfach nur ein bequemes Werkzeug, dass wir es sorglos im Altag benutzen können!"

    "Hikari finally speaks up again, having got over her mini-sulk."

    h "Es brauch schon viel Energie, um etwas einfaches wie Fliegen zu tun .{w} Und wir müssen immer sicherstellen, das wir genung Energie auf Reserve haben, im Falle eines Überaschungsangriff wie letzte Nacht."

    h "Glaubst du wirklich, es wäre eine kluge Idee, diese kostbare Energie auf etwas zu verschwenden, das mit einer Dusche so leicht gemacht werden kann?"

    "Fair point.{w} But, what I'm getting out of this is..."

    p "Ihr wollt damit also sagen, ihr {i}könntet{/i} es?"

    $ hikaface='angry'
    show Hikari

    "Her eyes narrow.{w} She takes in a deep breath, her cheeks puffing out dangerously.{w} Why do I suddenly fear for my ears?"

    $ hikaface='joking'
    show Hikari

    h "...Du bist ein Idiot."

    $ hikaface='normal'
    show Hikari

    "She sighs instead, the air escaping her in one long, drawn out breath of defeat.{w} My eardrums are safe for another day.{w} Phew."

    with Pause(3.5)

    "I catch a glance at the clock on the wall.{w} All this drama has really eaten into my free time before school.{w} If I don't start breakfast now, there'll be no way I'll make it in time."

    p "Dann macht doch, was ihr wollt.{w} Ich mach erstmal was zu futtern."

    hide Sayaka
    hide Hikari
    with dissolve
    with Pause(2.5)
    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka at center
    with dissolve

    "I start for the kitchen, but Sayaka cuts me off, sliding in front of me.{w} Her eyes are almost sparkling as she leans forward."

    s "Oh, you don't have to worry about that!{w} Let {i}us{/i} make breakfast instead!{w} Consider it our way of saying sorry for this little mess.{w} Right, Hikari?"

    $ hikaface='shocked'
    show Hikari at right
    show Sayaka at left
    with dissolve

    "She pulls Hikari in by the arm."

    h "W-Was?{w} Ich war nicht einverstanden--"

    s "Right, Hikari?"

    with hpunch
    $ hikaface='scared'
    show Hikari

    "She tightens her grip on Hikari's arm, a deadly edge behind her otherwise cheerful words."

    h "O-ow, okay!"

    "Hmmm.{w} Letting them cook...{w} I'm not so sure."

    menu:
        "What's the worst that could happen?":


            $ cookedpreviously = True

            "I don't see the harm in it, I suppose.{w} She seems to mean well, and it would be nice to take it easy after all of this stress."

            p "Klar.{w} Nur zu."

            $ sayapose='school_1'
            show Sayaka
            with dissolve

            "Sayaka beams, making me feel confident in my choice.{w} I...I think."

            s "You won't regret it!{w} You just sit back, and we'll have something amazing whipped up for you in a flash!"

            show Sayaka at center with move
            with Pause(0.5)
            show Sayaka at offscreenright
            show Hikari at offscreenright
            with move

            "With that, she spins on her heel and waltzes into the kitchen, dragging along with her a very reluctant Hikari."

            "I take a seat in the connected dining room, and ease myself into a chair.{w} This'll be fine.{w} Right?"

            with Pause(2.5)

            "It starts off well enough anyway.{w} I hear plates and utensils clatter about, with cupboard doors battering along."

            play music "bgm/mischiefintro.ogg" fadein 3.0
            queue music "bgm/mischiefloop.ogg"

            h "Weißt du überhaupt, was du machst?"

            s "We'll worry about that later!{w} Now put some of this stuff in too!"

            "...I'll pretend I didn't hear that."

            "The frantic chopping of vegetables sound out from behind me, mixed with Hikari's panicked yelps."

            h "Pass auf wo du das hinschwingst, du wirst noch meinen Kopf abschlagen!"

            s "It's fiiiine."

            h "B-Bist du dir sicher dass es dazu passt?"

            s "Sure it does!{w} I have a creative eye for these things."

            h "...Soll es Grün werden?"

            s "Uh."

            s "Mmhmm!"

            h "Also werden wir es einfach so machen, wie das?"

            "I hear the unsettling fwoosh of flames.{w} Just how high are they putting it on at?!"

            s "Hmm.{w} What do you think this stuff is?"

            h "Ich habe keine Ahnung."

            s "Oh well, in it goes anyway!"

            "..."

            "Things go silent in the kitchen.{w} I can't tell if that's good or bad.{w} I'm too scared to look."

            h "I-Ist es wirklich in Ordnung?"

            s "Yup!{w} This is how it's supposed to--"

            with hpunch

            s "Wahhh!"

            "Something explodes in the kitchen.{w} Thick plumes of acrid smoke waft into the dining space.{w} Hmm."

            h "Mach es aus, schnell, es wird sich ausbreiten!"

            s "How do I do that?!"

            h "I-Ich weiß es nicht!{w} Probier es einfach!"

            "Fwooom.{w} The roar of flames.{w} I can see the flickering of amber in my peripheral vision.{w} {i}Hmmmm{/i}."

            s "Nope!{w} That made it worse!"

            h "Wie wäre es...{w}damit?!"

            s "M-maybe!{w} It might have worked!"

            s "...Or not.{w} No more magic, okay?"

            h "Dieses mal wird es funktionieren--"

            s "No more magic!"

            h "Ich weiß sonst nicht, was ich tuhen soll!"

            s "Hyah!"

            h "A-ah, du bekommst es überall!"

            "I hear water splash.{w} A good deal of it.{w} Like, an entire bucket's worth of the stuff."

            h "Ist es...{w}ist es vorbei?"

            s "Hahhh...{w} I think so!{w} And look, the food is done!"

            h "Ich denke wirklich nicht, dass--"

            s "I said--the food is done!"

            with Pause(2.5)
            play music "bgm/everydayintro.ogg" fadein 2.0
            queue music "bgm/everydayloop.ogg"


            $ sayaface='smiling'
            $ hikaface='scared'
            $ sayapose='school_2'
            show Sayaka at center

            with dissolve

            "Apparently done, uh, 'cooking', the pair enter the dining space.{w} Sayaka has a plate in hand, a good amount of steam--or maybe smoke--drifting from it."

            s "I hope you're hungry, Kenta!{w} We really went all out to make this, you know!"

            "She puts a plate before me, a sincere smile on her face."

            "I...I guess she really gave it her all.{w} But...{w}this can't be called food."

            p "O-Oh.{w} Das ist ...{w} äh ..."

            "Charred, burnt, crisp remains of what might have been food at some point sit on the plate.{w} It feels like it might be hazardous to even breathe in this stuff."

            "I can see Hikari lurking further back, clearly ashamed of whatever...{w}substance they had created."

            "I guess this is my fault for letting them anywhere near the kitchen.{w} I should take responsibility, and--"

            menu:
                "Eat the food.":
                    "I have no choice, do I?{w} I don't want to make her feel bad, after she worked so hard to create...{w}whatever this is."

                    p "D-Dann probier ich mal ..."

                    "I give the substance a poke.{w} It crumbles into a fine powder at the slightest touch.{w} Okay."

                    "I'm sure even though it {i}looks{/i} absolutely terrifying, it can't be that bad.{w} Maybe there's something good, under all these layers of...{w}burnt stuff."

                    "I scoop up as much as I can that doesn't crumble away from my hold, and force it into my mouth, despite all my instincts screaming at me not to."

                    "It's...{w}it's..."

                    $ sayaface='happy'
                    show Sayaka

                    s "Well, is it amazing or what?"

                    "Sayaka leans in expectantly as I swallow it down."

                    "I think this must be what charcoal tastes like."

                    "I fight back the urge to choke, and give her smile and a nod."

                    p "M-Mmm!"

                    $ sayapose='school_1'
                    show Sayaka
                    with dissolve

                    s "Really?{w} Yay, I knew it!{w} You should let us cook for you {i}every{/i} morning!"

                    "Oh god.{w} What have I done?{w} And I still have an entire plate of this stuff left!{w} These girls are clearly the real danger to my health and well being right now."
                "Refuse to eat the 'food'. I don't want to die!":

                    "Okay, yeah, no.{w} I have to make a stand here, or things are only going to get worse."

                    p "Schau, es tut mir leid, Sayaka, aber ich krieg das echt nicht runter."

                    $ sayaface='normal'
                    show Sayaka

                    s "Huh?{w} Why not?"

                    "She tilts her head to the side, a small frown beginning to grow on her face.{w} Great, make me feel like a monster why don't you!"

                    p "Es ist ...{w} na ja ...{w} wie soll ich sagen, ohne ausfällig zu werden?"

                    "I give the toxic substance another look, sure that it's beginning to move of its own accord."

                    p "Würde ich es essen, könnte ich heute nicht mehr zur Schule gehen.{w} Oder den Tag danach."

                    s "Oh?"

                    p "Sayaka, was ich damit sagen möchte, ist ... Ich würde sterben.{w} Es sieht verdammt giftig aus."

                    $ sayaface='scared'
                    show Sayaka

                    s "Oh."

                    "Her frown deepens.{w} I'm sorry.{w} It had to be done."

                    $ sayaface='normal'
                    show Sayaka

                    s "Are you sure?{w} It can't be {i}that{/i} bad."

                    "Really?{w} Really?!{w} How could anyone defend this...{w}this...{w} I can't even call it food!"

                    p "Okay, warum probierst du dann nicht zuerst?"

                    $ sayaface='scared'
                    $ sayapose='school_1'
                    show Sayaka
                    with dissolve

                    "She pulls a face.{w} I knew it."

                    s "U-uhh, I already ate."

                    p "Schau, warum versuchst du--"

                    $ sayaface='happy'
                    show Sayaka

                    s "But. I know Hikari hasn't!{w} She can show you how totally safe and tasty it is!"

                    $ hikaface='shocked'
                    $ hikapose='school_2'
                    hide Sayaka
                    show Hikari at center
                    with dissolve

                    h "E-eh?{w} Ich?!"

                    "Hikari jumps as her name is called, still lurking quite a distance away from the 'food' that she had helped give life to."

                    $ sayaface='smiling'
                    show Sayaka at left
                    show Hikari at right
                    with dissolve

                    s "Yeah!{w} Come on over here, show Kenta how delicious it is!"

                    h "Das kann nicht dein Ernst sein.{w} Das Zeug ist--"

                    s "Totally safe and edible!{w} Now get over here.{w} Please."

                    $ sayapose='school_2'
                    $ hikaface='scared'
                    with hpunch
                    show Sayaka
                    show Hikari
                    with dissolve

                    "Sayaka thrusts a finger at the table with enough force that I think the plate rattled.{w} Yikes.{w} Despite the wide grin, though, I can't help but feel there's something sinister behind that."

                    h "...Fein."

                    "She approaches the food slowly, each step taking longer than the next, as if she was marching to her death.{w} Actually, that might very well be a possibility here."

                    $ sayaface='happy'
                    show Sayaka

                    h "Wir haben es geschafft...{w}also kann es nicht so schlecht sein.{w} Es ist einfach nur ein bisschen ...{w}knusprig."

                    "She outstretches a trembling hand towards the food, like it might bite her if she's not careful enough.{w} And then..."

                    $ sayapose='school_1'
                    $ hikapose='school_1'
                    $ sayaface='shocked'
                    $ hikaface='normal'
                    show Sayaka
                    show Hikari
                    with flash

                    "A bolt of magic erupts from her palm and hits the food, disintegrating it completely.{w} Along with the plate.{w} ...And a good portion of the table."

                    $ hikaface='joking'
                    show Hikari

                    h "Oops!{w} Ich bin ja so tolpatschig.{w} Meine Hand ist wohl...{w}ausgerutscht.{w} Was eine Schande!{w} Und ich habe mich schon {i}so{/i} gefreut alles zu essen."

                    "...I'm pretty sure magic doesn't just 'slip'!{w} And wasn't she the one that said they can't waste it on trivial things?"

                    "...Maybe it was an emergency in her eyes."

                    $ sayaface='scared'
                    show Sayaka

                    s "Hikari!"

                    "Sayaka pulls another heartwrenching frown, but it doesn't last long before her usual optimism returns."

                    $ sayapose='school_2'
                    $ sayaface='happy'
                    $ hikaface='scared'
                    show Sayaka
                    show Hikari
                    with dissolve

                    s "Oh well.{w} How about I make some more?"

                    $ sayaface='shocked'
                    show Sayaka
                    with hpunch

                    p "Nein!"

                    "I bolt upright in my chair, almost taking it up with me in the process.{w} I don't think my house would survive!"

                    "Maybe being a little louder than intended, I catch her off-guard and she jumps."

                    s "H-huh?"

                    p "Ich mein, wir würden zu spät zur Schule kommen, wenn ihr noch was kochen würdet."

                    s "Oh...{w} You're right.{w} Look at the time!"

                    "Phew.{w} Good save, me!"
        "Absolutely not!":

            "As if receiving a fiery premonition of what might happen if I do let them cook, I put my foot down without hesitation."

            "Even if I'm not the greatest cook in the world, at least I can be safe in the knowledge that what I make won't bring about the ruination of everything I know and love.{w} ...Most of the time, anyway."

            $ sayapose='school_1'
            $ sayaface='normal'
            $ hikaface='normal'
            show Sayaka
            show Hikari
            with dissolve

            s "Awww.{w} Are you sure?"

            p "Und wie.{w} Aber ich weiß den Gedanken zu schätzen."

            "She puffs her cheeks out in a rather adorable pout, but it doesn't last long before her usual bright smile returns."

            $ sayaface='smiling'
            show Sayaka

            s "Okay.{w} You really don't know what you're missing out on though!{w} I've been told my cooking 'really is something' by people before!"

            $ hikaface='scared'
            show Hikari

            h "Sayaka, Ich denke nicht dass sie meinten--"

            $ sayaface='happy'
            show Sayaka

            s "In fact, they said I should never cook again, because of how jealous it made other people feel!{w} Can you believe it?"

            "Yeah.{w} I'm definitely happy with my decision now.{w} I feel like I dodged a bullet.{w} A horrible tasting one that might have burned my insides."

            "I head for the kitchen to make the simplest meal I know, all the while keeping a watchful eye over my shoulder in case either of them attempt to assist me.{w} Which I can totally see in Sayaka's eyes as she fidgets just by counter.{w} I'm on to you!"

    stop music fadeout 5.0        
    scene bg black
    with fade

    "Breakfast soon comes to a close, with perhaps a more lively start to the morning than I'm generally used to."

    "As much of a headache as they can be, it was actually sort of nice to not be completely alone in the morning.{w} I wasn't about to tell them that, though, or I'd only encourage their almost criminal behaviour in just waltzing into my house like that!"

    "I head out for school, my two bodyguards naturally at my side.{w} I'm almost sort of getting used to this.{w} I don't know if that's a good or a bad thing."
    play music "bgm/everydayintro.ogg" fadein 2.0
    queue music "bgm/everydayloop.ogg"

    with Pause(3.5)

    "The journey to school goes by peacefully, not a monster in sight.{w} Though, I can't help but shake the feeling that something is watching me."

    "Ah, maybe I'm just getting a little paranoid after, you know, two attempts on my life have been made already.{w} I'm sure it's all in my head!"



    scene classroom
    with fade

    "I arrive at school with time to spare.{w} Huh.{w} That's a first."

    $ sayaface='smiling'
    $ hikaface='normal'
    $ sayapose='school_1'
    $ hikapose='school_1'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "Sayaka and Hikari keep close to my side.{w} So very close.{w} I practically feel the stares of my classmates, their looks ranging from resentful to jealous.{w} I can't imagine what they must think of this whole situation."

    p "Hey, Mädels?"

    s "Hm?{w} What's up?"

    p "Müsst ihr mir echt so sehr auf die Pelle rücken?{w} Ich weiß zu schätzen, was ihr alles für mich tut, aber wir sind hier in der Schule."

    $ hikaface='angry'
    show Hikari

    h "Aber was ist wenn--"

    p "Solange ihr in meiner Nähe bleibt, sollte es doch passen, oder?{w} Außerdem glaub ich kaum, dass es ein Monster so einfach ins Klassenzimmer schafft, ohne vorher einen Wirbel zu machen."

    $ hikaface='normal'
    show Hikari

    "Hikari falls silent.{w} She narrows her eyes into a glare and folds her arms together, tossing her head to the side."

    h "Fein.{w} Was auch immer."

    hide Hikari
    show Sayaka at center
    with dissolve

    "She storms over to her desk and drops into the chair, her eyes straight forward, leaving me and Sayaka together."

    p "Ähh ...{w} Hab ich sie wütend gemacht?"

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Ah, don't worry.{w} She's always like this.{w} Give it time and she'll be back to her, uh, less grumpier self."

    s "She only has your safety in mind, and is just worried about what might happen if she has to leave you."

    s "Heck, if I had it my way we wouldn't even let you go to school.{w} We'd just keep you locked up in a nice room until this all blows over."

    "...I don't think she realises how scary that sounded, coupled with her usual grin."

    $ sayaface='smiling'
    show Sayaka

    s "You're right, though.{w} Maybe we {i}have{/i} been suffocating you a bit too much.{w} I think we can afford to at least ease up during school."

    p "Danke."

    "I let out a sigh.{w} They're finally starting to listen to reason, if only a little!"

    hide Sayaka
    with dissolve

    "The bell sounds, signifying the start of class.{w} I pass by a disgruntled Hikari on the way to my own desk.{w} She doesn't even look my way.{w} Harsh."

    scene bg black
    with fade

    with Pause(5.0)

    scene classroom
    with fade

    "The morning classes pass by in the blink of an eye, the lunch break soon arriving."

    "I stand up and let out a yawn, only to find I'm not alone."

    $ sayapose='school_1'
    $ hikapose='school_2'
    show Sayaka at left
    show Hikari at right
    with dissolve

    p "...Jetzt kommt schon.{w} Darüber haben wir schon mal geredet!"

    "As if the conversation this morning had never happened, I find both my guardians standing around me, oblivious to my irritation."

    s "What's up, Kenta?{w} Aren't we going to go get lunch now?"

    p "Ich hol mir mein eigenes Essen.{w} Ihr müsst nicht an mir kleben.{w} Ihr habt doch bestimmt auch andere Dinge zu erledigen, oder?"

    $ sayaface='normal'
    show Sayaka

    s "But what are we supposed to--"

    p "Was weiß ich!{w} Irgendetwas.{w} Scheißegal was!{w} Ich hab euch erst gestern kennengelernt, und ihr seid schon so anhänglich.{w} Ich hätte gern etwas Platz für mich selbst!"

    "I really am grateful that they're here.{w} Otherwise, I might have met a grisly end yesterday.{w} But this is borderline stalking.{w} I'm not even going to bring up how they camped outside, and then proceeded to break into my house!"

    $ sayaface='smiling'
    show Sayaka

    s "Oh, okay then.{w} I getcha.{w} Hikari understands too.{w} I think."

    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Hmph."

    s "Come on, Hikari!{w} It might be fun to explore the school a bit, and see what it has to offer.{w} We've never really had the chance to attend one before after all!"

    "She's never been to school...?{w} Just where do these two come from?{w} The more I talk to her, the more she makes herself sound like like an alien."

    s "Alright then, Kenta.{w} We'll go do our own thing for a bit.{w} Just yell if you need us, and try not to die!"

    hide Sayaka
    show Hikari at center
    with dissolve

    "And like that, she marches off, humming a happy tune.{w} Hikari follows in her wake, but not before giving me one last icy look.{w} ...I can almost feel my shoulders begin to frost.{w} Brrr."

    hide Hikari
    with dissolve
    with Pause(2.5)

    "Well.{w} I did it.{w} I somehow convinced them to give me some peace.{w} For the time being anyway."

    "..."

    "But now what?"

    "First and foremost, I should probably try not to forget about lunch again.{w} Otherwise I might just keel over and have finished the job for whatever dark forces that are lurking out there."

    "I head to the cafeteria."

    scene cafeteria
    with dissolve

    "The cafeteria is as you would expect during lunchtime--completely packed.{w} Throngs of students take up what little walking space might have existed between the tables, equally as populated."

    "I stand my ground, and gradually work my way past the crashing waves of students that impede my path.{w} Of course getting food would never be so simple!"

    "Eventually I work my way to the front of the line and approach the counter.{w} Naturally, after all the students before me, there was very little in the way of choice."

    "I guess it's either...{w}this sandwich.{w} Or this other sandwich.{w} Neither of which seem amazingly appetising.{w} Ah, whatever.{w} Anything will do after how much food I've missed out on!"

    "Cheap, bland sandwich in hand, I give a look over the tables.{w} Like before, they're all pretty packed.{w} Though I do see one fairly empty table at the far end, with a familiar someone happily digging away at their lunch."

    "Even from this distance I can tell it's Sayaka, her vibrant brown hair instantly distinguishable from everyone else's."

    "I don't see Hikari anywhere in sight.{w} They must have decided to do their own things for the break."

    "I guess if I want to sit down here to eat, Sayaka's table is the only choice, but do I really want to eat here?{w} It's so noisy, I can hardly even think."

    "She hasn't noticed me either, completely absorbed in the demolition of her food.{w} Maybe I can slip away to the roof, where no doubt it'll be more peaceful."

    menu:
        "Head for the roof.":

            $ hikari += 1

            "The roof it is.{w} It's just too noisy here, and I get the feeling sitting with Sayaka will only make things worse."

            "I sneak past her and head for the stairwell.{w} Though, it wasn't exactly difficult with how into her food she was."

            scene bg black
            with fade

            "The higher I scale the stairs, the more quiet my surroundings become, until eventually the bustling racket of the students softens to a dull mumble below.{w} Ah, peace at last."

            scene school roof
            with wake

            "I emerge out onto the rooftop.{w} A gentle breeze graces my face as the sun shines high in a near cloudless sky.{w} It's perfect out here."

            "Only...{w}it seems I wasn't the only one that had decided to come up here."

            $ hikaface='normal'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            "Hikari stands at the edge of the rooftop, facing outwards as she peers down at the countless people.{w} Given how intently she seems to be analysing them, I can only guess that she's keeping guard."

            "I have to admire her dedication towards this whole thing.{w} I actually do feel pretty safe knowing she's this serious about it all."

            "She's so absorbed in what she's doing, I don't think she's even noticed me yet."

            "Making no real effort to conceal myself, I close up right behind her.{w} Still nothing.{w} She's miles away."

            "I reach out and give a gentle tap to her shoulder."

            p "Yo."

            $ hikaface='shocked'
            show Hikari
            with hpunch
            with hpunch

            h "Wahh!"

            "She jumps a good several feet into air at my touch, and lets out an ear piercing scream.{w} A...{w}a bit of an overreaction maybe?{w} Or am I just that scary?"

            "A hand to her chest as if to keep her heart from breaking free, she spins around to face me.{w} Her stern expression softens a little as she realises it's me, but only a little.{w} She still seems pretty mad."

            $ hikaface='angry'
            $ hikapose='school_2'
            show Hikari
            with dissolve

            h "Oh, Kenta, du bist es nur.{w} Erschreck mich doch nicht so!{w} Du hattest Glück dass ich dich nicht sofort zerfetzt habe!"

            "I scrub at the back of my head with a grin.{w} I really did spook her."

            p "Meine Schuld.{w} Hältst du die Stellung?"

            $ hikaface='normal'
            show Hikari

            h "Huh?"

            "Her eyes flicker back to where she was watching for a moment."

            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "Ja.{w} Obwohl die Schule selbst bisher friedlich war, weiß man nie, wann der Feind zuschlagen könnte."

            p "Danke.{w} Ich weiß es zu schätzen."

            $ hikaface='shy'
            show Hikari

            h "E-Es ist kein Problem.{w} Ich mach das für die Sicherheit der Schule, nicht nur für dich !"

            "Her face goes an interesting shade of pink.{w} It doesn't take much to fluster her, huh?"

            p "Klar, schon gut.{w} Ich hab schon verstanden."

            $ hikapose='school_2'
            $ hikaface='angry'
            show Hikari
            with dissolve

            h "Denn während Sayaka und ich den Anstand haben, unsere Kräfte vor normalen Menschen zumindest zu verbergen, kann ich nicht sagen, dass die Schatten dasselbe tun werden. Es ist schon schlimm genug, dass sie versucht haben, dich am helllichten Tag anzugreifen."

            $ hikaface='normal'
            show Hikari

            h "Ich versteh es einfach nicht.{w} Es wiederspricht allem, was wier bisher über sie wissen."

            "She sighs dramatically and turns to resume watch over the school."

            $ hikaface='embarrassed'
            show Hikari

            "I open my mouth to maybe say something to her, but a low, rumbling sound cuts me short."

            p "...Hikari?"

            h "J-Ja...?"

            "She answers without turning around, her ears clearly burning.{w} It wasn't difficult to discern what the sound was, given that I saw no sign of any lunch out here at all."

            p "Hast du, äh, noch nicht gegessen?"

            "..."

            "Silence.{w} I think I hit the nail on the head."

            $ hikaface='normal'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "Es ist nicht meine Schuld!{w} Diese Cafeteria ist so laut und dreckig, dass ich keinen weiteren Moment darin ertragen kann. {W} Ich weiß nicht, wie Sayaka da unten freiwillig essen kann."

            h "Ich hab sowieso wichtigere Sachen zu tuhen."

            p "Und kannst du mit einem leeren Magen auch kämpfen?"

            h "Natürlich!{w} Wer denkst du--"

            $ hikaface='shy'
            show Hikari

            "Her stomach growls again, arguing against her words."

            h "..."

            p "Ah."

            $ hikaface='normal'
            $ hikapose='school_2'
            show Hikari
            with dissolve

            h "Okay, ich bin vielleicht etwas hungrig.{w} Aber ich werde nicht in diese Grube zurückkehren."

            "Yeesh.{w} I know that place can get pretty packed sometimes, but she's making it out to be something far worse.{w} She really can't deal with crowds, I guess."

            "I unwrap the sandwich I had almost forgotten about, and take a bite out of it, not wanting to forget about lunch completely myself."

            "Hikari watches me intently as I take several more bites, her eyes flickering to the sandwich every now and again.{w} I can practically see the hunger in her eyes."

            "I stop mid-bite, and offer the sandwich her way, since I'm beginning to feel terrible for eating in front of her.{w} And I think if I don't, she might just snatch it out of my hands at any moment anyway."

            p "Willst du auch was?{w} Falls ja, ich kann mit dir teilen."

            $ hikaface='angry'
            show Hikari

            "Her mouth hangs open and her brow furrows in concentration, as if to seriously consider it.{w} I swear, she's almost drooling at this point."

            $ hikapose='school_1'
            show Hikari
            with dissolve

            "She comes to her decision with an abrupt 'hmph' and turns her head to the side, her hair whipping along with it.{w} I should have expected that."

            h "S-Sei doch nicht lächerlich!{w} Warum würde ich etwas wollen, worauf du schon gesabbert hast?"

            h "Ich würde lieber verhungern...{w}als..."

            $ hikaface='scared'
            show Hikari

            "{i}Gruuuu{/i}.{w} Her stomach beckons for the food."

            h "O-okay, fein.{w} Vielleicht ein bisschen."

            with hpunch
            $ hikaface='normal'
            $ hikapose='school_2'
            show Hikari
            with dissolve

            "I break off half, before she snatches it away with reluctance."

            h "Danke dir.{w} I-Ich nehme an."

            "I don't think she's used to saying something like that.{w} We're finally making progress!{w} I can't help but smile."

            $ hikaface='angry'
            show Hikari

            h "Wisch dieses ekliche Grinsen aus deinem Gesicht.{w} Ich weiß nicht an was du denkst, aber ich bin mir sicher dass es etwas unanständiges ist."

            "She says with a snarl, before she violently rips a chunk of the sandwich away with her teeth."

            p "Und, gut?"

            $ hikaface='normal'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "...Es ist Okay.{w} Nicht das beste was ich hatte, aber auch nicht das schlechteste. Zurück an der Akadmie, ich-"

            $ hikaface='shocked'
            show Hikari

            "She stops herself, her eyes widening some.{w} I think she almost let slip something there.{w} I really wish they weren't so secretive about all this stuff."

            p "Die Akademie, hm?"

            $ hikaface='normal'
            show Hikari

            h "E-Es ist nichts."

            p "Aber ich bin mir ziemlich sicher, dass ich was--"

            with hpunch
            $ hikapose='school_2'
            $ hikaface='angry'
            show Hikari
            with dissolve

            h "Du hast nichts gehört! {i}Nichts{i}!"

            "Yikes."

            "Despite her small frame, whenever she uses that commanding voice of hers, I feel about the size of a mouse before her.{w} I guess it's no use in pushing her for more information, unless I want to end up like that monster from before."

            p "Okay, okay!{w} Ich hab überhaupt nichts gehört.{w} War ...{w} wohl nur der Wind oder so"

            $ hikaface='normal'
            show Hikari

            "She sighs as she gives her hair a toss, the anger leaving her as suddenly as it had built."

            h "Wir halten keine Informationen zurück um einfach nur mysteriös zu sein, weißt du."

            "Could have fooled me!"

            h "Es ist...{w}der einfachere Weg.{w} Es hat keinen Sinn, dich in dieses Durcheinander zu ziehen, wenn wir ihm helfen können.{w} Es ist kein Leben das ich jemandem Wünsche..."

            "Her expression darkens, yet her mouth still works, the majority of her half of the sandwich already gone.{w} I'm not even sure if she realises she's eating it at the moment."

            "She spends a good moment or two debating something in her head, before she finally looks up at me with serious eyes."

            h "Kenta, was würdst du tuen wenn du..."

            "A group of chatty students emerge out onto the roof from the stairs, lunches in hand.{w} Hikari clamps up at the sight of them and turns back to her guard post."

            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "...Vergiss es.{w} Es ist nich wichtig."

            p "Wenn du, äh, meinst."

            "It sure {i}looked{/i} important, since I don't think I've ever seen her give me that serious a look before.{w} Just my luck that of all the times people would choose to eat here, it would have to be now."

            "Any semblance of a conversation we may have had before is well and truly dashed now.{w} She seems a lot more reserved in the presence of other people.{w} Plus, I guess what we were discussing wasn't exactly appropriate for their ears."

            h "...Nebenbei, das Sandwich hat wirklich gut geschmeckt."

            p "Häh?"

            $ hikaface='shy'
            show Hikari

            h "N-Nichts."
        "Sit at Sayaka's table.":


            $ sayaka += 1

            "Then again...{w} I can't really be bothered to scale all the way up to the roof when there's a seat right before me.{w} And, it might be a wasted journey if for whatever reason, people are up there.{w} The table it is."

            scene cg19
            with dissolve
            play music 'bgm/magicalgirlintro.ogg' fadein 2.0
            queue music 'bgm/magicalgirlloop.ogg'

            "I approach Sayaka, whose eyes light up at the sight of me."

            s "Mffgh!"

            "Her cheeks full to bursting, she attempts to address me, frantically waving her hand in the air as food flies everywhere.{w} Yeesh, don't talk with your mouth full."

            p "Hey.{w} Kann ich mich hier hinsetzen?"

            s "Mgffgh, mff!"

            "She nods enthusiastically, shovelling another mouthful of food in.{w} I'm no expert in the 'mouth full' language, but I think she said 'be my guest'."

            "...I didn't notice it before, but she has {i}tons{/i} of food on her tray.{w} Enough for ten students at least!"

            "I'm not really sure how she got away with so many portions.{w} It's no wonder the pickings were slim by the time I got there."

            "I'm wondering if magic was used in persuading them to so willingly give her all of this?{w} ...It's scary to think just how easily she's been wrapping the school around her finger since she arrived."

            "I mean, right now, she's only used it to enroll herself, and get extra portions.{w} But where does it end?{w} There's almost something...{w}sinister...{w}to it all."

            "Joining her at the table, I unwrap my sandwich and take a bite.{w} Yup.{w} Just as bland as I thought it'd be.{w} Just the way I like it."

            s "Hey there!{w} I thought you wanted some time away from us?"

            "Apparently done with whatever food it was she had crammed into her mouth like some kind of hamster, she's finally free to talk.{w} Though, I can see her begin to amass another shovel's worth.{w} She's like a machine."

            scene cafeteria
            $ sayaface='smiling'
            $ sayapose='school_1'
            show Sayaka at center
            with dissolve

            p "Ah, ja.{w} Hab ich, aber, äh, sonst ist nicht wirklich wo ein Platz ..."

            $ sayaface='happy'
            $ sayapose='school_2'
            show Sayaka
            with dissolve

            s "It's okay, you can admit that you just missed me {i}so{/i} much and couldn't bear another moment alone without me.{w} I won't tell Hikari."

            "She grins, and takes another bite."

            p "Hah.{w} Lustig.{w} ... Wo ist Hikari?{w} Ich dachte, sie wär bei dir."

            $ sayapose='school_1'
            show Sayaka
            with dissolve

            s "Omff!{w} Shmff--"

            p "Äh, schon okay, nur keine Hektik.{w} Es ist nicht dringend."

            "I bring up my arm to shelter myself from flecks of stray food as she excitedly tries to explain things.{w} ...Gross."

            $ sayapose='school_2'
            show Sayaka
            with dissolve
            $ sayapose='school_1'
            show Sayaka
            with dissolve
            $ sayaface='smiling'
            $ sayapose='school_2'
            show Sayaka
            with dissolve

            s "I was saying, she doesn't like all the crowds and noise, so she wandered off on her own, mumbling something about finding a more quiet place."

            p "Glaubst du, dass es ihr gut geht?"

            s "Mff--probably."

            $ sayaface='happy'
            show Sayaka

            "She wolfs down another bite.{w} Less than half of the food left from what I first saw before I sat down.{w} Where is it all going in that slim figure of hers?"

            $ sayaface='smiling'
            $ sayapose='school_1'
            show Sayaka
            with dissolve

            s "I think we'll know if something happens to her.{w} Or more like, the whole school will know.{w} She gets crazy strong when she's angry!"

            p "Das hört man gerne.{w} ... Hoff ich zumindest."

            "So basically, if we feel the entire school rumble, we can assume something has happened to Hikari."

            p "Äh, wie gefällt es dir hier?{w} Wenn ich mich recht erinnere, hast du doch gesagt, dass du noch in einer Schule warst, oder?"

            $ sayaface='happy'
            show Sayaka

            s "Oh, yeah!{w} It's great.{w} Everyone is so friendly, and the food is {i}amazing{/i}!"

            "As if to emphasise that point, she stabs into her food, her face practically glowing."

            $ sayaface='smiling'
            show Sayaka

            s "And, maybe I should have worded it better.{w} It's not that Hikari and I have never been to a school...{w} We just haven't been to a...{w}well, normal one."

            p "Was, wart ihr etwa auf einer Zauberschule, oder so was in der Art?"

            $ sayapose='school_2'
            show Sayaka
            with dissolve

            s "Mmhmm!"

            "I wasn't really being serious...{w}and I didn't expect her to answer so honestly either."

            p "W-Wirklich?"

            $ sayaface='happy'
            show Sayaka

            "Her mouth full again, she nods, having learned at least some manners.{w} That's a 'really, really!' by the looks of things."

            p "Hm.{w} Eine Zauberschule.{w} Wo man ...{w}Magie erlernt?{w} Das hört sich nach Spaß an."

            $ sayaface='normal'
            $ sayapose='school_1'
            show Sayaka
            with dissolve

            "Sayaka's expression darkens.{w} ...Did I say the wrong thing {i}again{/i}?!"

            s "It's not something I'd ever like to go through again.{w} Let's just say that."

            s "Magic isn't something you just pick up in a day.{w} There's years of studying, training, and--"

            $ sayaface='scared'
            show Sayaka

            "She clamps her mouth shut and slaps a hand across as if to stop any more words from leaking out.{w} Damn it.{w} She realised."

            $ sayaface='smiling'
            show Sayaka

            s "Whoops!{w} Silly me.{w} That was a close one."

            "One of these days I'm going to find out just what the heck these two are.{w} Any day now, and she'll slip up completely and spill everything!"

            p "Okay, wenn ich schon nichts über eure Organisation erfahren darf, darf ich dann zumindest etwas mehr über dich erfahren?"

            s "Huh?{w} Me?"

            p "Ich mein, aus irgendeinem Grund scheint ihr fast alles über mich zu wissen, aber ich weiß gar nichts über euch, außer, dass ihr keine normalen Menschen seid."

            $ sayaface='normal'
            $ sayapose='school_1'
            show Sayaka
            with dissolve

            s "Hmmm."

            "Man, she really has to think about this.{w} Is it really that difficult for her to think of something that {i}isn't{/i} magic related that she can actually share with me?"

            $ sayaface='smiling'
            show Sayaka

            s "This is pretty much a full time job, so I don't really get much time to myself.{w} I'm not sure if there's much I can tell you without the big guys back at home getting grumpy at me."

            s "But, you know..."

            "She sweeps her gaze over the cafeteria, a small smile growing on her face."

            s "Being assigned to watch over you has actually been one of the most laid back assignments we've had."

            $ sayaface='happy'
            show Sayaka

            s "We've been given the chance to enroll and live out something of a normal life here in the school."

            "Well...{w} I'm not really sure if I'd classify what they did as 'enroll', but I get what she means."

            $ sayaface='smiling'
            show Sayaka

            s "Just being able to kick back and take things easy...{w}like a normal girl.{w} I didn't think I'd ever be able to do that."

            s "You know, I'm gonna miss this place when everything is finished here."

            $ sayaface='normal'
            show Sayaka

            "She falls silent, her eyes distant.{w} She's lost in another world right now, deep in her thoughts.{w} I never figured her as the kind to do all this deep thinking."

            "'Like a normal girl'...{w} Does that mean she doesn't like her magic way of life?{w} I can see how it might get tiring if you had to battle things constantly like that monster I saw the other day."

            "But she chose that lifestyle, right?{w} At least, I think she must have.{w} I can't really ask her, as I don't think I'll get away with more magic related questions for the day."

            with Pause(2.5)

            "..."

            s "Hey, Kenta?"

            $ sayaface='smiling'
            $ sayapose='school_2'
            show Sayaka
            with dissolve

            p "Ja?"

            "Eyes glimmering, and glistening lips parted ever so slightly, she gives me a look that makes my heart throb.{w} Why do I get the feeling she's about to ask me something really important here?"

            s "Are you gonna...{w}finish that?"

            "Her eyes fall to the sandwich in my hand, still with only one bite in it."

            p "Ah, nein, alles in Ordnung.{w} H-Hier."

            $ sayaface='happy'
            show Sayaka

            s "Thanks!{w} You're the best!"

            "Still in a daze from the look she gave me a moment ago, she snatches the sandwich out of my hand without resistance."

            "...Wait, what just happened?"

            "I'm left staring blankly at my empty hand, the majority of my sandwich already lost to the black hole that is Sayaka's stomach.{w} I may have made a mistake here."

            "I notice her tray is completely empty too.{w} Spotless, even.{w} She's a monster!"

    scene bg black
    with fade
    stop music fadeout 4.0

    "The lunch break soon comes to an end, and we're whisked back to class."

    "The rest of the school day goes by fairly normally.{w} No crazy attacks.{w} No monsters."

    "I still can't shake the feeling something is watching me, though."


    play music "bgm/ominousintro.ogg" fadein 4.0
    queue music "bgm/ominousloop.ogg"
    scene town street night
    $ sayaface='normal'
    $ sayapose='school_1'
    $ hikaface='normal'
    $ hikapose='school_1'
    show Sayaka at left
    show Hikari at right
    with fade

    "Another day down, another walk home.{w} My two guardians by my side."

    "They seem noticably more tense compared to last night.{w} After how close that fight was, I really don't blame them.{w} We were lucky she didn't pursue us back then, or that could have been it for me--no, it would have spelled the end for everyone."

    "The journey back is silent, both the girls' faces mirroring each other in a look of sheer determination.{w} They seem ready to spring to action at the slightest sign of danger, so I don't want to break their concentration with mindless small talk."

    "Gradually, the sun sets on our route ahead, street lights flickering to life overhead one by one.{w} Great.{w} The more the shadows begin to creep in all around us, the more tense I can feel myself become."

    "I come to a stop.{w} Something doesn't feel right..."

    s "Kenta?{w} What's wrong?"



    "There it is again.{w} That damn headache, out of nowhere."

    "Wait.{w} Hasn't there always been a pattern with these headaches?{w} They don't usually happen during the day, unless--"



    y "Ah, pünktlich.{w} Du machst das wirklich leicht, weißt du?"

    "Of course.{w} We walked right into it!{w} I really need to start to find a new route home..."

    $ sayaface='angry'
    $ hikaface='angry'
    show Sayaka
    show Hikari

    "A sultry laugh drifts from out of the darkness, causing both the girls to assume offensive positions.{w} It could only be one person..."

    hide Sayaka
    hide Hikari
    $ yuzuface='joking'
    $ yuzupose='magical_2'
    show Yuzuki at center
    with dissolve



    "Obsidian wings unfurl from amidst the night sky, and the amber eyed adversary from before makes her presence known in a storm of black feathers."

    "What was her name...?{w} Yuzuki?{w} I guess it doesn't matter.{w} Names mean nothing right now."

    "She has a maniacal look in her eye--a killer glint.{w} Much like before, she isn't here to play around.{w} There's only one thing she's after."

    "...Me."

    $ hikapose='magical_1'
    $ sayapose='magical_1'
    $ hikaface='normal'
    hide Yuzuki
    show Sayaka at left
    show Hikari at right
    with flash
    stop music fadeout 6.0

    "Light floods in and dispels the darkness for only a moment as the pair don their battle gear, weapons at hand."

    s "Kenta, get back!"

    p "Schon gut.{w} Ich weiß, wie das funktioniert, okay!?"

    "Not needing to be told twice, I sprint a good distance from the three girls as to not get caught up in any crossfire."

    "But...{w}are they going to be able to win?{w} Yuzuki hardly broke a sweat last night, and was able to keep both of them at bay at once with that scythe of hers.{w} The difference in power was just too much."

    "Not to mention my guardians have some serious issues with working together as a team.{w} Last night was a complete disaster!"

    "I fear we might have to take another 'tactical retreat'...{w} And I'm not sure if I have the stomach for it."

    $ yuzuface='smiling'
    $ yuzupose='magical_1'
    show Yuzuki at left
    show Sayaka at center
    show Hikari at right
    with dissolve
    play music "bgm/evilgirlintro.ogg" fadein 1.0
    queue music "bgm/evilgirlloop.ogg"
    "Yuzuki lands gracefully before Sayaka and Hikari, an unsettling grin spreading from ear to ear on her face."


 y "Ich muss sagen, ich bin überrascht, dass du überhaupt kämpfen willst.{w} Ich dachte, du würdest einfach wieder den Schwanz drehen.{w} Ich nehme an, dass die Dinge auf diese Weise mehr Spaß machen!"

    "Her dark wings erupt into a stream of feathers, which reform into a deadly scythe within her hands."

    y "Nun, wer von euch möchte zuerst einen erbärmlichen Tod sterben?"

    s "Hikari, now!"

    play music "bgm/battleintro.ogg"
    queue music "bgm/battleloop.ogg"

    $ yuzuface='joking'
    $ hikaface='angry'
    show Sayaka at offscreenright
    show Hikari at center
    show Yuzuki at center
    with move
    with hpunch
    show Yuzuki at left
    show Hikari at right
    with move


    "Hikari nods and lunges for Yuzuki before she can make the first move.{w} Sayaka kicks off of the ground and flies a good deal backwards as she readies an arrow in her bow.{w} Am I...{w}witnessing team play here?{w} It certainly makes a change after last night's disaster."

    y "Es ist alles nutzlos!"

    "Yuzuki reacts like lightning and brings her scythe to a whirl, clashing with Hikari's sword.{w} A shockwave bursts through the street as the two weapons collide, shattering nearby glass and warping street signs; a testament to just how strong these girls are."

    "I'm beginning to see shades of last night's fight.{w} Yuzuki has the advantage in terms of brute strength, so she'll no doubt push back against Hikari's blade.{w} But, Hikari doesn't seem nervous at all.{w} In fact, she seems confident!"

    h "Hrghh!{w} Licht, komm hervor!"

    scene bg white
    with wake

    "Hikari stands her ground in the clash with gritted teeth, and her sword gives off a vibrant glow at her command.{w} A glow that continues to intensify until it engulfs the clashing pair in a blinding light."

    "I'm forced to shield my eyes with my arm, as if I were staring at the sun itself.{w} If it was bad enough for me at this distance, I can't imagine how bad it must have been for both of them."

    scene town street night
    $ yuzupose='magical_2'
    $ yuzuface='shocked'
    show Yuzuki at left
    show Hikari at right
    with wake

    "From the safety of my sleeve I peer back out at the battle, the light fading slightly."

    "It seems Yuzuki wasn't expecting that at all, as she's reeling back from it all, a hand to her face."

    y "U-ugh.{w} Woran denkst du, dass du spielst?!"

    scene cg15
    with flash

    s "Aaaand, Hikari, duck!"

    "Sayaka lets loose the arrow she'd been charging since the pair had clashed.{w} It rockets off with unreal speed, leaving a trail of glimmering sparks in its wake as it homes in on Yuzuki."

    "Hikari pulls back at Sayaka's voice, and ducks to just barely avoid the arrow coming her way."

    scene town street night
    $ yuzupose='magical_1'
    show Yuzuki at right
    with dissolve

    $ yuzuface='scared'
    with flash
    with hpunch
    show Yuzuki at left
    with MoveTransition(0.2)

    "It's a direct hit!{w} The arrow bursts upon impact and sends Yuzuki skidding backwards as she desperately tries to keep upright."

    show Hikari at right
    with moveinright

    "It doesn't end there, though.{w} Hikari hops to her feet and charges in for a follow-up attack whilst Yuzuki is trying her best to recover from the arrow."

    scene cg16
    with dissolve

    "Steel sings as Hikari kicks off of the ground and goes for a crushing blow to the head.{w} This should be it.{w} I can't see how she'll escape from Hikari's blade now!"

    h "Es ist vorbei!"

    with hpunch
    with hpunch

    "The ground under my feet gives off a quake as she lands.{w} A good half of the road splits under her blade and chunks of concrete rain everywhere."

    "It was a devastating attack to be sure.{w} Surely no one could have survived a blow like that.{w} But..."

    scene town street night
    $ hikaface='shocked'
    show Hikari at center
    with dissolve

    h "W-Was...?"

    "Hikari is just as bewildered as I am.{w} The dark girl is nowhere to be seen.{w} A single black feather drifts down from where she once stood.{w} She just...{w}vanished."

    "A sinister giggle echoes from the shadows.{w} Did Yuzuki...{w}teleport?{w} Or is she just so fast I couldn't keep up?"

    $ hikaface='scared'
    show Hikari

    "Hikari bolts up at the sound and shoots Sayaka a frenzied look."

    $ hikaface='shocked'
    show Hikari

    h "Sayaka, sieh o--"

    hide Hikari
    $ sayaface='shocked'
    show Sayaka at center
    with dissolve

    s "Huh?"

    "Something glimmers from out of the darkness behind her and then lashes out with a vicious swing.{w} Sayaka just barely reacts in time, jumping to avoid the fatal slash."

    "At least...{w}I thought she had avoided it."


    scene cg4
    with flash

    s "Kyahhh!"

    "There's a sudden burst, and Sayaka lets out a shriek.{w} She herself looks unharmed, but a good portion of her outfit is in tatters."

    "Fragments of what used to be her outfit rain down from above, well and truly diced by the mad girl's scythe."

    "I mean, it's horrible, there's hardly anything left of her outfit!{w} From where I'm standing I can practically see...{w}huh?{w} I lost track of what I was thinking about there.{w} Sorry."

    "Ahem."

    "Fight, bad.{w} Damage, terrible.{w} Okay, I'm back on track."

    "This is insane.{w} If she had reacted just a fraction of a second slower, her outfit wouldn't have been the only thing cut to ribbons by that attack."

    "I thought Yuzuki seemed bad before, but if anything tonight she seems even stronger.{w} Or is it just all in my head?"

    "The pair learned from their mistakes the previous night and devised something almost resembling teamwork tonight to try and put an end to her, but she hits back twice as hard anyway."

    "Sayaka and Hikari have given it their all and this monster still has the upper hand.{w} I wonder if they have any tricks left?"

    "I suppose I should put more faith in my 'guardian angels', even if things look dire right now.{w} They're surely trained for these kinds of intense battles, and must have at least {i}something{/i} to fall back on."

    "...Something that I hope doesn't involve flying again.{w} I really, {i}really{/i} don't want to fly again.{w} At this point, I'll take my chances with Yuzuki."

    "Sayaka hugs herself in an effort to cover up, her face flush with embarrassment.{w} I can't imagine this being convenient at all during a fight.{w} Especially not one as serious as this!"

    "I feel like I shouldn't be watching this...{w}but this is an important fight I can't afford to take my eyes off of!{w} ...Or something like that."

    s "Ahh!{w} Th-this is terrible!{w} I...{w}I can't fight like this!"

    s "Ohh, what do I do?!"
    stop music fadeout 4.0
    "With what should be a fairly troubling scene for her partner, Hikari actually seems more annoyed than anything as she rushes over."

    h "Komm schon, hör auf herumzualbern!"

    "She stomps her foot, and scolds her half-naked partner.{w} That seems like a rather bizarre way to treat someone in such a state."

    h "Du weißt verdammt gut, dass du dein Outfit regenerieren kannst."

    "Eh...?{w} She can?{w} So why has she been acting like she has?"

    s "Ahhh, this is so b--...{w} Huh?{w} Oh.{w} Right!"

    scene town street night
    $ sayaface='joking'
    $ hikaface='angry'
    show Sayaka at left
    show Hikari at right
    with flash
    play music "bgm/mischiefintro.ogg"
    queue music "bgm/mischiefloop.ogg"

    "There's another flash, and her outfit is restored to what it once was.{w} Huh.{w} It really was that easy."

    s "Eh-heh-heh...{w}my bad.{w} I totally forgot."

    "Hikari hoists her sword up onto her shoulder and lets out a sigh, a dangerous vein just faintly visible on her forehead."

    h "Weißt du, ich denke ein Teil von dir {i}wollte{/i} sich so zeigen.{w}Vielleicht zu jemanden speziellem..."

    s "Me?{w} Never!{w} Though, you're sure one to talk, 'accidentally' leaving the door unlocked--"



    with hpunch

    $ hikaface='embarrassed'
    $ hikapose='magical_2'
    $ sayaface='scared'
    show Sayaka
    show Hikari with dissolve

    "{i}Bonk{/i}.{w} Hikari raps her on the head.{w} What is even..."

    s "Ow!{w} I was kidding!"

    "Guys, aren't you forgetting something...?"

    stop music fadeout 3.0

    "I mean, it's not like you were in the middle of a fight or anything."

    "Wait, that's a point.{w} Yuzuki could have torn these two up while they were arguing.{w} Where did she go after that attack?"

    $ sayaface='normal'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka
    show Hikari with dissolve

    "As if suddenly realising this fact as well, both the girls jump into 'serious mode'--if that's even really possible--and assume offensive stances once more."

    h "Hast du verstanden, wohin sie gegangen ist?"

    s "Uhh..."

    $ hikaface='angry'
    show Hikari

    h "Warum hab ich überhaupt gerfragt?"

    "I'm beginning to grow uneasy...{w} I instinctively throw a glance over my shoulder, only to be met with a maniacal smile."
    play music "bgm/ominousintro.ogg"
    queue music "bgm/ominousloop.ogg"
    hide Sayaka
    hide Hikari
    $ yuzupose='magical_1'
    $ yuzuface='joking'
    show Yuzuki at center
    with dissolve

    y "Boo."

    p "D-Du ...!"

    "She's right behind me.{w} How did she manage that?!{w} ...Then again, I guess it probably wasn't {i}that{/i} difficult a feat with how distracted my supposed guardians can get."

    with hpunch

    "I stumble backwards with a gasp, just narrowly avoiding her outstretched grasp as she reaches for me with a limp."

    s "Kenta!"

    $ yuzuface='scared'
    show Yuzuki

    y "Ah, verdammt{w} Ich bin so nah dran."

    "The dark girl winces and her shoulders sink.{w} It seems like she barely any strength left, as she just barely keeps a hold of her scythe, limply at her side."

    "Maybe the combined attack before was more effective than I thought, and it finally all caught up to her, her energy reserves well and truly spent."

    "This was probably her last ditch attempt to get me.{w} I'm lucky I turned around when I did!"

    $ yuzuface='angry'
    show Yuzuki

    "She gives me a narrowed glare as she staggers back a few steps, my bodyguards catching up to me."

    "Amber eyes full of hatred, she shifts her gaze to Sayaka and Hikari."

    y "Es sieht so aus, als wäre ich an der Reihe, mich für die Nacht zurückzuziehen.{w} Glaub nichts, du hast noch nichts gewonnen!"
    
     y "Du hast Glück mit diesem schlechten Schuss, aber erwarte nicht, dass es ein zweites Mal funktioniert.{w} Kenta {i}wird{/i} mir gehören!"

    $ yuzuface='joking'
    $ yuzupose='magical_2'
    show Yuzuki
    with dissolve

    y "Aber mach dir keine Sorgen, ich bin nicht grausam genug, um Wege zu trennen, ohne dir etwas zum Spielen zu überlassen.{w} Bis wir uns wieder treffen!"

    hide Yuzuki
    with dissolve

    "She begins to sink back into the shadows, giving off another devious laugh despite her limping retreat.{w} That last part of what she said worries me...{w} 'Something to play with'?"

    show Hikari at right
    show Sayaka at left
    with dissolve

    h "Zum Teufel gehst du irgendwo anders hin!{w} Wir werden den Kampf hier und jetzt beenden!"

    s "Ah, Hikari, maybe we should be--"

    $ sayaface='shocked'
    show Sayaka
    show Hikari at offscreenright with MoveTransition(0.3)

    "Hikari disregards her partner's advice and blazes forward, sword at the ready."

    "It seems like her blade is just about to connect with Yuzuki before she can make her escape...{w}but something suddenly whips out, as if appearing out of nowhere, and takes Hikari off of her feet hoisting her high into the air."

    "A thick, slimy appendage.{w} A...{w}a tentacle?"

    scene cg2
    with dissolve

    "Hikari drops her sword after being blindsided by the beast, and is left wrestling helplessly against the writhing tendrils as they work to ensnare her."

    h "Wahh!{w} H-hey, nein!{w} Lass mich gehen!"

    "I see her hands give off a glow.{w} That's right!{w} If she doesn't have a weapon, she still has her magic.{w} She should be able to make quick work of this thing, sword or not."

    h "Jetzt zeig ich dir--huh?!"

    "...Or maybe not.{w} The beast is one step ahead of her, and works to bind her hands, leaving her well and truly helpless.{w} The tentacles creep in ever closer, oozing a pungent substance that coats a good majority of her."

    h "Urghh...{w} Das...{w}ist so eklich!{w} Ich denke nichtmal alle Duschen der Welt werden das ,Zeug in meinen Harren, rausbekommen!"

    "She bemoans her disgusting predicament as she thrashes around, ultimately only resulting in the tentacles constricting tighter against her."

    "Okay...{w} So she can't save herself.{w} But, her trusty partner should be able to pierce the tentacles with a well placed arrow, right?"

    "Right?!"

    s "B-bad doggies!{w} Sit!{w} Down!{w} Stay!"

    "What, when did they show up?!{w} Sayaka is surrounded by a pack of those demonic dogs from before--the ones that nearly took my life."

    "They must have charged in at the same time as the tentacle creature made itself known.{w} Were they summoned by Yuzuki, I wonder?{w} Wait...{w}can she control them?"

    h "H-Hallo?{w} Wird mir irgendjemand helfen?!{w} Es ist nicht so lustig, wie es aussieht!"

    "Hikari keeps up a brave front, but I can see the tentacles are taking their toll on her."

    "This is bad.{w} Both of them are held up by monsters."

    "While Sayaka is handy with a bow, I don't think she's all that good at close up combat, so she might be in trouble here."

    "And then...{w} Hikari is {i}clearly{/i} in need of assistance, the tentacles might completely crush her if nothing is done soon."

    scene town street night
    with dissolve

    "So with both of them struggling...{w} Who's left to help them?"

    "Me?"

    "But...{w} I haven't ever fought anything in my life.{w} I would have been dead long ago if these two hadn't made themselves known in my life."

    "I clench my fists tight and throw a glance between the two girls.{w} They've risked so much to help me before, while I've just stood on on the sidelines like some sort of coward."

    "They need my help."

    "What can I do?{w} I don't have any magic powers.{w} I don't have super strength.{w} I can't fly.{w} I'm useless.{w} Useless!"

    "I stomp at the ground, cursing my weak nature."

    "Huh...?"

    "Something clatters at my foot.{w} Hikari's sword.{w} A sizeable amount of steel that almost rivals Hikari herself in height."

    "I crouch down to pick it up.{w} Despite its size, it's surprisingly light.{w} I'm able to take it up with just a single hand."

    "This is crazy.{w} I can't believe I'm even thinking about doing this."

    "I straighten up and tighten my hold on the sword, giving it a test swipe into the air.{w} It slices through without much resistance, and gives off a satisfying swish."

    "It'll be just this easy, right?{w} Air is one thing...{w}but to even think about using this thing on something living...{w} Even if they're monsters."

    "I'm just not sure if I can follow through with this..."

    s "Kyahh!{w} Don't touch me!{w} Back, back!"

    h "E-Es zerdrückt mich!{w} H-Hilfe!"

    "I can hear cries of distress from both sides.{w} Time is running out.{w} I've made up my mind!"

    "I can't save them both at once, though.{w} Who needs help more urgently?"

    menu:
        "Sayaka.":

            $ sayaka += 1

            "Right.{w} Sayaka has numerous, far more threatening foes than just a couple of slimy tentacles.{w} These things might tear her apart if I wait too long!"

            p "Sayaka, halt durch!"

            play music "bgm/battleintro.ogg" fadein 2.0
            queue music "bgm/battleloop.ogg"

            "I kick off and head to Sayaka's side first, the sword held awkwardly at my side.{w} ...I really don't know how to even hold this properly.{w} I must look so stupid right now."

            $ sayaface='scared'
            show Sayaka at center
            with dissolve

            s "Shoo, shoo!"

            "She frantically bobs and weaves her way out of the incoming claws and fangs, unable to find a spare moment to get an arrow out."

            "I pick up the pace, nearing the beasts.{w} There isn't a moment to lose!{w} This is my time to shine.{w} I can be the hero--"

            hide Sayaka
            with dissolve
            with hpunch


            p "Oof!"

            "In my haste to reach Sayaka in time, I put a foot in the wrong place and trip myself up in a spectacular display of heroism."

            "I pull into a tumble, and barrel straight into one of the creatures, sword outstretched."

            "It lets out an ear piercing howl as the blade comes into contact with it, and leaps back, distracting all the others in the process."

            "Well.{w} Not exactly what I had in mind, but it worked.{w} Somewhat."

            scene cg20
            with dissolve

            "After that little stunt, all their burning eyes are on me now.{w} N-no problem."

            "I hold up a shaky sword toward one of them as they begin to circle me, rather than Sayaka.{w} This was what I wanted, right?{w} I...{w}I mean, I saved Sayaka at least."

            "The beasts all leap at once.{w} An assault from four sides.{w} Oh god, this is going to end badly.{w} Even a seasoned swordsman would be at a disadvantage here!"

            scene town street night
            with flash

            "Four arrows fly at once and nail each of the creatures in the head before they can reach me, each of them exploding into a cloud of black smoke."

            $ sayaface='happy'
            $ sayapose='magical_2'
            show Sayaka at center
            with dissolve

            s "Phew.{w} Another close call, huh?"

            "Sayaka grins as she lowers her bow.{w} ...Ah, that's right.{w} By taking on the monsters, I was able to give Sayaka the room she needed to launch her arrows.{w} ...All according to plan!"

            p "Was heißt ...{w} Ich frag mich echt, wie ihr das tagtäglich durchhaltet!"

            $ sayaface='smiling'
            show Sayaka

            s "It's something you get used to!"

            s "Anyway, Kenta, you really surprised me!{w} I didn't think I'd ever be saved by {i}you{/i}!"

            p "Ah, das war doch gar nichts ...{w} Warte, was soll denn das heißen?"

            $ sayapose='magical_1'
            show Sayaka
            with dissolve

            s "Nothing!{w} Thank you, for real."

            "She beams with an innocent grin.{w} I'm sure she definitely meant {i}something{/i} by that, though..."

            $ sayaface='shocked'
            show Sayaka

            "Her mouth opens wide as she looks over Hikari's sword that I still hold in a trembling hand.{w} Even now, I still can't stop shaking after confronting those things!"

            s "Is that...{w}Hikari's?{w} How on earth did you..."

            $ sayaface='smiling'
            show Sayaka
            with hpunch

            h "Hallo?!{w} Wenn ihr Typen da hinten aufgehört habt zu reden, wäre gerade etwas Hilfe gut!"

            s "Okay, okay.{w} Calm down.{w} We were getting to it!"

            "Sayaka sighs and nocks a magic arrow into her bow, before letting it loose with a bored expression, as if she wasn't even that concerned with Hikari."

            with flash

            "The lazy yet somehow precise arrow pierces through all the tentacles at once, severing them cleanly.{w} The monster still hidden in the shadows lets out some kind of shriek and drops Hikari to the ground before retreating."

            h "Oof!"

            "She lands with a slimy splash.{w} ...Eurgh.{w} That can't be pleasant."

            $ sayaface='happy'
            show Sayaka

            s "See, you're fine!"

            $ hikaface='angry'
            show Sayaka at left
            show Hikari at right
            with dissolve

            "Hikari rises, and takes in a deep breath, about to yell at her partner, but she stops when she notices her sword in my fairly incapable hands."

            $ hikaface='shocked'
            show Hikari

            h "Kenta...?"

            "I grin nervously and scrub at the back of my head."

            p "A-Ah ...{w} Ich hoffe, ihr habt nichts dagegen.{w} Es war ein Notfall."

            $ hikaface='normal'
            $ hikapose='magical_2'
            $ sayaface='smiling'
            show Sayaka
            show Hikari with dissolve

            h "Das ist nicht das Problem.{w} Ich bin überrascht dass du es benuten kannst."

            p "Wenn es euch beruhigt, ich konnte nicht wirklich viel damit anfangen."

            $ sayapose='magical_2'
            $ sayaface='happy'
            show Sayaka
            with dissolve

            s "Psh, don't be so modest!{w} You were my hero, Kenta!"

            "Sayaka clasps her hands together and chirps playfully, batting her eyelashes at me with a dreamy expression."

            "Even though she's clearly just messing around, I still can't help but let out an awkward laugh as my cheeks flare up."

            s "You should have seen him, Hikari.{w} He came in charging and took all four of them on at once!{w} In fact, I think he might be even better than you with a sword!"

            $ hikapose='magical_1'
            show Hikari
            with dissolve

            "Okay, now she's {i}really{/i} making it obvious that I did nothing."

            "Hikari squelches over to me and snatches the sword back with a sour expression.{w} ...Urgh...{w}she got some of her slime on me."

            $ hikaface='angry'
            show Hikari

            h "Sei nicht lächerlich.{w} Ich bin mir nicht sicher, was genau da passiert ist, aber ich bin mir sciher, dass Glück eine {i}große{/i} gespielt hat."

            $ sayaface='smiling'
            $ sayapose='magical_1'
            show Sayaka
            with dissolve

            s "No, I mean it!{w} In fact, maybe I should just partner up with Kenta instead.{w} We'd make the best team ever!"

            $ sayaface='happy'
            show Sayaka

            s "What do you say, Kenta?{w} I'm sure I could get you sorted out with a nice magical outfit too!"

            "Hikari continues to simmer as Sayaka goes on.{w} I can't even tell if she's being serious at this point!"

            p "Ähh ...{w} Darauf kann ich verzichten."

            $ sayaface='smiling'
            show Sayaka

            s "Aww.{w} Okay.{w} I still think you'd look great in one of these outfits!"

            "I wonder...{w} Would my magical outfit be as, uh...{w}light on materials as theirs are?"

            "...I feel cold just thinking about wearing one.{w} I don't know how they manage."
        "Hikari.":


            $ hikari += 1

            "I think it's clear that Hikari is the one in danger here.{w} Those tentacles are pretty much squeezing the life out of her!"

            "I'm sure Sayaka has been in tougher situations before, so I feel confident in letting her handle those monsters."

            p "Hikari, halt durch!"

            "I break into a sprint and head for the writhing mass of tentacles that have laid their assault on an unfortunate Hikari."

            play music "bgm/battleintro.ogg"
            queue music "bgm/battleloop.ogg"

            scene cg2
            with dissolve

            h "Nngh!{w} D-Dummes Ding!{w} Hättest du mich nicht überrascht, könnte ich es..."

            "She continues to kick and wriggle around in its hold, but if anything, I think she's only making the whole situation worse on herself."

            "I come to a screeching halt as I reach the monster, sword in hand."

            "The tentacles seem like they want nothing to with me, only focused on continuing their attack on Hikari.{w} ...Funny that."

            "Okay.{w} This should be easy.{w} It's just like cutting away some weeds, right?{w} ...Wriggling, slimy weeds...{w}but weeds no less!"

            "I steel myself as I pull back the sword.{w} I can't hesitate any longer, or it might be too late."

            "One clean swing is all I need to end this."

            "So...{w} Here I go."

            p "Hyahh!"

            scene town street night
            with flash


            "The sword slices through the tentacles like butter, severing them in two and relinquishing their hold on Hikari."

            $ hikaface='scared'
            $ hikapose='magical_1'
            show Hikari
            with dissolve

            h "Oof!"

            "She lands with a sticky, and slimy splash, looking somewhat dazed from the whole experience."

            "Huh.{w} I did it.{w} I actually did something useful!"

            "The monster's body slinks into the shadows with a low groan.{w} I guess it can't really do much when the majority of its tentacles are now writhing around on the ground."

            h "Ughnn...{w} Kenta...?"

            p "Alles in Ordnung?{w} Hier, nimm meine Hand."

            "I hold my free hand out to her with an exhausted smile."

            $ hikaface='angry'
            show Hikari

            h "D-Du musst nicht..."

            $ hikapose='magical_2'
            show Hikari with dissolve
            $ hikapose='magical_1'
            show Hikari with dissolve

            "She takes a good moment to debate things in her mind, even attempting to push herself up off the ground several times only to slip right back down into the puddle of...{w}whatever the heck that monster oozed.{w} I get the feeling she isn't used to accepting help from people."

            $ hikaface='shy'
            show Hikari

            h "Okay, f-fine.{w} Whatever."

            with hpunch

            "She finally grabs hold of my hand, and I hoist her up.{w} ...Eurgh.{w} Her hand is coated in that foul slime.{w} I hope this stuff washes off."

            $ hikaface='normal'
            show Hikari

            "Once back on her feet, she takes a good moment to recompose herself.{w} She tries to keep an air of dignity about herself, despite being drenched head to toe in that stuff."

            $ hikaface='shocked'
            show Hikari

            "She surveys the scene, her eyes moving from the wriggling tentacles cast aside on the ground, before finally settling on her sword, still held firmly within my grasp.{w} Her mouth open in shock, having finally pieced together what happened."

            h "War es...{w}Warst du es der mich gerettet hat, Kenta?"

            "She's completely taken aback.{w} Is it really that unbelievable that I did something useful for once?{w} ...Okay, maybe it is."

            p "Ah, ja.{w} Ich hoffe, ihr habt nichts dagegen, dass ich es ausgeliehen hab."

            "I can't help but feel embarrassed about this all.{w} I was practically like...{w}a hero!{w} It's a bizarre feeling."

            $ hikaface='normal'
            $ hikapose='magical_2'
            show Hikari
            with dissolve

            "I hold out the sword towards her, still as lightweight as ever.{w} This thing is amazing.{w} It felt like I was swinging a feather back then."

            "She takes it, after a few attempts of grabbing at air, her eyes still focused intently on me.{w} She truly is shocked here."

            h "Das ist gur.{w} Aber wie warst du in der Lage..."

            with hpunch

            s "Wahh!{w} Down, boy!{w} Get back!"

            "Sayaka's cries of distress cut things short.{w} Uh, whoops.{w} I got so caught up with saving Hikari, I had forgotten about Sayaka completely."

            "She's still dancing about, just barely keeping up with the rabid monsters."

            $ hikaface='angry'
            $ hikapose='magical_1'
            show Hikari
            with dissolve

            "Hikari sighs and gives her sword a flourish."

            h "Ugh.{w} Dass muss bis später warten."

            show Hikari at offscreenleft
            with MoveTransition(0.2)
            with flash

            "She dashes towards her partner with a burst of speed and makes short work of the offending creatures, killing them all with one precise slash.{w} They erupt into smoke which is whisked away by the night air."

            $ sayaface='scared'
            $ sayapose='magical_1'
            show Sayaka at left
            show Hikari at right
            with dissolve

            h "Sheesh, Sayaka.{w} Was hast du geamcht währen du mit den Dingern gespielt hast?{w} Ich wäre umgebracht worden, wäre Kenta nicht da gewesen!"

            $ sayaface='normal'
            show Sayaka

            s "Huh?{w} Kenta?"

            "Finally able to catch her breath, Sayaka gives me a puzzled look as I wander over to them."

            $ hikaface='shy'
            show Hikari

            h "Kenta...{w} Er...{w}naja...{w}e-er hat mich gerettet."

            $ sayaface='shocked'
            show Sayaka

            s "Really?!{w} How on earth did he manage that?!"

            "She's in as much of a state of disbelief as Hikari was."

            $ hikaface='normal'
            $ hikapose='magical_2'
            show Hikari
            with dissolve

            h "I-Ich weiß es nicht.{w} Er hat einfach mein Schwert aufgehoben und dann--"

            with hpunch

            s "Your sword?!{w} But how did he--"

            $ hikaface='angry'
            show Hikari

            h "Ich weiß!{w} Deine Vermutung ist genauso gut wie meine.{w} Lasst uns dankbar sein, dass er es konnte, oder dieser Abend wäre unser letzter gewesen."

            "...I get the feeling I'm missing something really important here.{w} What's so special about me using her sword?{w} I mean, I just picked it up, and swung it.{w} No big deal, right?"

    stop music fadeout 4.0
    $ hikaface='normal'
    $ sayaface='normal'
    show Hikari
    show Sayaka

    "Hikari suddenly lights up, and strikes a pose, blade at the ready."

    h "Oh!{w} Das Mädchen...{w} Hat sie...?"

    s "Yuzuki?{w} Yeah, it looks like she got away while we were fussing over her pals."

    $ hikaface='angry'
    show Hikari
    play music "bgm/seriousintro.ogg" fadein 5.0
    queue music "bgm/seriousloop.ogg"
    h "Verdammt!{w} Wir waren zu nah!"

    "She stomps her foot in frustration, the slime that no doubt oozed between her toes giving off a squelch."

    $ sayaface='smiling'
    show Sayaka

    s "Maybe it's for the best?{w} I don't think either of us are in any kind of condition to fight anymore."

    "Sayaka sighs dramatically and throws her hands up in the air.{w} She's right.{w} I can't imagine how much worse things could have been if that girl had still been around."

    $ hikaface='normal'
    $ hikapose='magical_1'
    show Hikari
    with dissolve

    s "How about you, Kenta?{w} How are you holding up?"

    p "Meinst du mich?"

    "Let's see...{w} I'm drenched in sweat and my heart is still thumping like crazy from the adrenaline rush.{w} I think I might throw up.{w} And my head feels like it might split open at any moment."

    p "Ich, äh ...{w} Es geht so, um ehrlich zu sein."

    "Oddly enough, I really do feel fine.{w} Better than fine, in fact.{w} I'm happy I could finally do something, even if it wasn't much, so I'm not as much a burden for these two."

    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "I think it's safe to say that we should call it a night now, huh?"

    "Hikari peers into the darkness, still holding her sword firmly.{w} She seems reluctant about giving up on the fight so soon."

    $ sayaface='happy'
    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "C'mon, Hikari!{w} It's over.{w} We won!"

    "Sayaka slaps a hand down on Hikari's tense shoulder, and she loosens up.{w} Just a little."

    h "Ich weigere mich zu glauben, dass sie so einfach aufgeben würde.{w} Es macht keinen Sinn."

    s "Didn't you see her?{w} She was really beat up.{w} I think we did more damage to her than she's letting on.{w} I'd be surprised if she even shows up tomorrow night!"

    h "Vielleicht..."

    "Hikari finally gives up, her sword fading with a dim light."

    "She reluctantly joins the pair of us, and we begin the journey home once more."

    scene bg black
    with fade

    "And with that, the chaotic night finally comes to an end.{w} I get to live for yet another day!"

    "After tonight, I'm more grateful than ever for the existence of my 'guardian angels'...{w} However bizarre they might be at times."

    "We part ways once we reach my house...{w} Though I know they'll be just a shout away if I need them, since they'll no doubt be camped in my garden again.{w} ...I really don't understand how they don't get caught."

    scene kitchen night
    with fade

    "I shut the door behind me, and I'm greeted with the familiar aroma of home cooking."

    "Safe at last.{w} ...I think.{w} At least, the monsters haven't attacked me here, anyway.{w} They seem to only want to get me when I'm isolated from mostly everyone else."

    "Let's hope things stay that way.{w} No one else has to be dragged into this mess.{w} Heck, I still don't even know why {i}I'm{/i} in this situation to begin with."

    "I join my parents at the table, the plates only just being set up.{w} I get the same questioning looks as before, maybe more so today because of how taxing that encounter had been on my body."

    "I'm lucky enough to have not suffered any real damage, or at least anything noticeable at first glance, so they don't chase up any further on the matter."

    "The usual conversations unfold, and once more it becomes my turn to talk about my day.{w} I can only let out an awkward laugh and say it was the same as any other day."

    "I wonder how they'd react if I told them there are two complete strangers potentially camping in our back yard?"

    with Pause(2.0)
    stop music fadeout 5.0
    "The peaceful, relaxing dinner comes to an end.{w} Much like last night, I make myself scarce and drag myself up to my room, wanting nothing more than to collapse onto my bed for a good several days."

    scene bedroom night
    with fade

    "Thankfully it's the weekend tomorrow, at least.{w} So there's no worry about having to get up too early.{w} But, I get the feeling with those two girls around, I'm not going to be able to get much of a lie in."

    "...Speaking of the girls.{w} Do I even want to check?"

    "I heave a reluctant sigh and peek through the curtains.{w} Yup.{w} Tent.{w} Camp fire.{w} An over-cooked meal catching alight as the pair scramble to put it out.{w} ...That's about what I expected."

    "I shut the curtains and ignore the fact the entire garden is in danger from catching fire.{w} I'm far too exhausted to worry about that.{w} I'm sure it'll be fine.{w} Most likely.{w} ...Eh."

    "Crawling into bed, the distressed cries of two supposed 'professionals' are the last thing I hear before I drift off into the world of dreams."

    scene bg black
    with fade


    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"
    scene bedroom day
    with wake

    "I awake with a groan, warm rays of the sun pulling me out of my slumber whether I like it or not."



    "Alongside the expected headache, every muscle in my body screams out in protest as I try to push myself up."

    "I don't get it.{w} I didn't even exert myself {i}that{/i} much the other day.{w} So why do I feel so weak?"

    with hpunch

    "It takes a good moment or so of struggling before my body finally complies, and I tumble out of bed."

    "I'm left staring at the ceiling in a daze for a second, before I boot to life once more.{w} What is wrong with me?!"

    "Rising on shaky legs, I totter back and forth before I almost crash into the wall in an effort to support myself."

    "Okay.{w} Deep breaths.{w} It appears I may have forgotten how to walk properly.{w} No big deal."

    "Let's see if I can remember, before I even {i}think{/i} of attempting the stairs."

    "It's just one foot in front of the other.{w} Left foot.{w} Right foot."

    "Slowly, but surely, I become steadier with each step I take.{w} Phew.{w} Maybe I'm just more tired than I realise?"

    with Pause(2.5)

    "Having remembered the basics of human mobility once more, I head for the bathroom."

    "As I approach the door, I can't help but feel a sense of deja vu about the whole thing.{w} Why is that, I wonder?{w} I get the feeling there's something important I'm forgetting.{w} Something potentially life threatening."

    "But...{w}I can't recall it at all in such a groggy state.{w} I'm sure I'll remember after a shower!"

    scene cg5
    with wake

    "Shower...{w}shower...{w}shower...?"

    "As I open the door, I'm greeted by a wisp of steam and the sound of running water."

    "It looks like I won't be able to use the shower right now...{w}since it's...{w}being used...?"

    "At least I think it is.{w} I'm having a little bit of trouble coming to terms with the sight before me."

    s "Wahh!{w} Kenta?!{w} Wh-what are you doing?"

    "I blink a few times.{w} Yup.{w} Still there."

    "Sayaka is really there.{w} ...Using my shower.{w} Huh."

    "I gawk for a while longer, my hand fumbling limply at the door handle.{w} All I have to do is close the door again, and stop this being any more awkward than it's already become for us."

    "Setting aside the fact they've broke into my house yet again, how is this {i}my{/i} fault?{w} I thought they would have learned how basic locks work after the mishap from yesterday morning!"

    "If anything, I'm the victim here!{w} It's not fair!"

    s "H-hello?{w} Is anyone there?{w} Y-you can close the door now!"

    "Sayaka breaks me out of my thoughts as she attempts to cover herself the best she can, her face flush with embarrassment."

    "She's a lot more subdued compared to her usual, outgoing self.{w} I guess that's to be expected in an awkward situation like this."

    "A situation that I'm only making more awkward the longer I stand here wide-eyed by the door."

    s "If you don't mind..."

    p "Äh, genau.{w} Mein Fehler ..."

    "At least Sayaka is more reasonable about this whole thing.{w} I have a feeling if I had walked in on Hikari like this again, the house might not be standing."

    "I avert my gaze--somehow--and pull the door to a close."

    "Locks, people.{w} Locks!{w} They exist for a reason.{w} Sheesh."

    "...I'm not sure if I'll ever be able to get that image of her out of my head now."

    "Her wet hair, the water cascading down her body, the--"

    "Argh!{w} I shake my head.{w} Bad Kenta!{w} You're better than this!"

    scene bg black
    with fade

    "After all the commotion from what I'm hoping won't be a regular thing, I find myself downstairs with both of the girls."

    scene kitchen day
    $ sayaface='smiling'
    $ hikaface='normal'
    $ sayapose='school_1'
    $ hikapose='school_1'
    show Sayaka at left
    show Hikari at right
    with fade




    p "Echt jetzt, ist das echt nötig?{w} Heute ist keine Schule, schon vergessen?"

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "But that's exactly why we're here!"

    "Sayaka beams with a smile almost as bright as the sun itself."

    p "Was ...?"

    s "Kenta, you don't have many friends, do you?"

    $ sayaface='smiling'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    "Where on earth did that come from?{w} She isn't joking around either as she says it with such a sincere look."

    p "S-Sei doch nicht dumm.{w} Ich hab genug Freunde!"

    $ hikaface='joking'
    show Hikari

    h "Oh?{w} Nenn mir einen."

    "Hikari, too?{w} I'm beginning to feel ganged up on here..."

    p "Freunde?{w} Das ist einfach!{w} Da hätten wir ..."

    "Uh...{w} Well, let's see.{w} How about...{w}no...{w}I guess I just say good morning to them and that's it."

    "But surely--...{w} I guess I can't really count them either, since I've only worked a couple of times on projects with them."

    "Uh-oh.{w} This is bad.{w} I can't actually come up with anybody.{w} The look on my face says it all, as Hikari has a smug look about her."

    "I better change the subject.{w} Fast!"

    p "I-Ist doch egal!{w} Wie kommt ihr jetzt überhaupt da drauf?"

    $ hikaface='normal'
    $ sayapose='school_2'
    show Hikari
    show Sayaka with dissolve

    s "It's just, we noticed at school that you never really seem to talk to anyone."

    p "Naja, das ... äh ... weil ich mich mit euch rumschlagen muss!"

    "Okay, grasping at straws here, but it's the best I can come up with.{w} Somehow I get the feeling they're not convinced.{w} Heck, {i}I'm{/i} not convinced, even by my own words."

    s "And over the past few weeks we've been watching over you, you only seem to ever leave the house for school, before you come right back."

    p "Ich ..."

    $ sayaface='normal'
    show Sayaka

    s "Don't you get lonely, Kenta?{w} It's not good for someone to completely shut themselves away like that."

    s "And to add to that, your parents always seem to be away working.{w} So it's just you, all on your own."

    "Hey now, you shouldn't be worried about that part, or you wouldn't be able to use my house as freely as you do!"

    "But...{w}I guess she has a point.{w} One I have realised myself, even if I don't want to fully admit it."

    $ sayaface='happy'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Which is why we're going to do something fun today!{w} All three of us!"

    "She claps her hands together and snaps me out of my depressing thoughts."

    s "Believe it or not, Hikari and I don't really get a lot of free time, so we've never really been able to enjoy a weekend like this."

    $ hikaface='angry'
    show Hikari

    h "H-hey!{w} Wir sind immernoch im Dienst.{w} Vergiss das nicht!"

    $ hikaface='joking'
    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "Aber wenn Kenta sich entscheiden würde and einem sonnigen Tag auszugehen...{w}naja, wir hätten keine Chance und müssten mit ihm gehen."

    p "Okay, okay.{w} Ich schätze mal, ich hab hier kein Wörtchen mitzureden, oder?"

    $ hikaface='smiling'
    $ sayaface='smiling'
    show Hikari
    show Sayaka

    "They both smile innocently.{w} ...I'm sure I'm being manipulated here."

    p "Also, was habt ihr für heute geplant?"

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Ah!{w} That's a secret.{w} But first, there's the matter of breakfast."

    "Right.{w} Breakfast."

    if cookedpreviously == True:
        "I have a terrifying flashback to yesterday and their supposed 'breakfast' they had made for me.{w} Not to mention the state they left the kitchen in afterwards.{w} It looked like a bomb had went off in there!"

        s "I think Hikari and I should handle breakfast again today!{w} We've totally got it under control this time."

        $ hikapose='school_1'
        $ hikaface='scared'
        show Hikari
        with dissolve

        h "W-Wir müssen?"

        s "Yep!"

        "Hikari's face grows pale.{w} She shoots me a look that says she wants me to put my foot down and end this madness before it can spiral any further out of control."

        s "How about it, Kenta?"

        "After careful deliberation, I say..."

        menu:
            "No.":
                jump cookingprevious
            "Nope.":

                jump cookingprevious
            "Nuh-uh.":

                jump cookingprevious
            "How about...no.":

                jump cookingprevious
            "Hah. Ahahaha. Ahahahahahahahaha. No.":

                jump cookingprevious
            "Let's not.":

                jump cookingprevious
            "Mmm...no.":

                jump cookingprevious
            "I'll think about it. Okay, I'm done thinking. No.":

                jump cookingprevious
            "Sure, okay.":


                "Well, sure, I can't see any reason why not!"

                "...Is the complete opposite of what I'm about to say.{w} I'd be insane to consider otherwise!"

                jump cookingprevious

        label cookingprevious:
            p "Äh, schon gut.{w} Ich kümmer mich ums Essen."

            $ sayaface='normal'
            $ hikaface='normal'
            show Sayaka
            show Hikari

            s "Aw..."

            "She looks absolutely crushed.{w} But I had to do it!{w} For both Hikari's and my own safety!"

            p "I-Ich mein, ihr müsst nach dem gestrigen Tag doch echt müde sein.{w} Und mit dem Kochen könnte ich mich auch gleich bedanken!"

            $ sayaface='smiling'
            $ sayapose='school_1'
            show Sayaka
            with dissolve

            s "Really?"

            p "Wirklich!"

            $ sayaface='happy'
            show Sayaka

            s "Well...{w}okay.{w} Your loss!{w} Breakfast really would have been better today, too."

            "Somehow I doubt that.{w} I think destruction just comes naturally to both this girl and her partner in crime."

            p "Bleibt einfach hier sitzen ...{w} und fasst bloß nichts Brennbares an, während ich weg bin, okay?"

            $ hikaface='smiling'
            hide Sayaka
            show Hikari at center
            with dissolve

            stop music fadeout 6.0

            "They both comply and take a seat at the table.{w} Hikari seems relieved and mouths a 'thank you' my way as she passes by.{w} The house is safe for another day!"

            scene bg black
            with fade

            "I quickly cook up something edible and disaster free."

            "Several times did I find myself having to shoo Sayaka away from the kitchen as she snuck her way in insisting she could help in some way.{w} I almost had a heart attack at one point as I turned around to find her standing there with a knife and a dangerous expression on her face."

            "I know she's just trying to help, but really now!"
    else:

        "Hmm.{w} I did put my foot down the other day, since we were in a bit of a rush for school."

        "But I'm sure whatever they can come up can't be {i}that{/i} bad."

        "Plus, Sayaka seems so enthusiastic about the whole thing.{w} I don't think I have it in me to refuse to a face that cute."

        p "Okay, okay.{w} Ihr könnt das Frühstück machen.{w} Macht ...{w} nur bitte keinen Saustall, okay?"

        "Sayaka's eyes light up and she claps her hands together."

        s "Really?{w} Yay!{w} You won't regret it, I promise!"

        "I sure hope not..."

        stop music fadeout 6.0

        "I don't see the harm in it I suppose.{w} She seems to mean well, and it would be nice to take it easy after all of this stress."

        p "Klar.{w} Nur zu."

        $ sayapose='school_1'
        show Sayaka
        with dissolve

        "Sayaka beams, making me feel confident in my choice.{w} I...I think."

        s "You won't regret it!{w} You just sit back, and we'll have something amazing whipped up for you in a flash!"

        show Sayaka at center with move
        with Pause(0.5)
        show Sayaka at offscreenright
        show Hikari at offscreenright
        with move

        "With that, she spins on her heel and waltzes into the kitchen, dragging along with her a very reluctant Hikari."

        "I take a seat in the connected dining room and ease myself into a chair.{w} This'll be fine.{w} Right?"

        with Pause(2.5)

        "It starts off well enough anyway.{w} I hear plates and utensils clatter about with cupboard doors battering along."

        play music "bgm/mischiefintro.ogg" fadein 3.0
        queue music "bgm/mischiefloop.ogg"

        h "Weißt du überhaupt, was du machst?"

        s "We'll worry about that later!{w} Now put some of this stuff in too!"

        "...I'll pretend I didn't hear that."

        "The frantic chopping of vegetables sound out from behind me mixed with Hikari's panicked yelps."

        h "Pass auf wo du das hinschwingst, du wirst mir noch den Kopf abschlagen!"

        s "It's fiiiine."

        h "B-Bist du sicher dass das geht?"

        s "Sure it does!{w} I have a creative eye for these things."

        h "...Soll es Grün werden?"

        s "Uh."

        s "Mmhmm!"

        h "Also werden wir es einfach so machen, wie das?"

        "I hear the unsettling fwoosh of flames.{w} Just how high are they putting it?!"

        s "Hmm.{w} What do you think this stuff is?"

        h "Ich habe keine Ahnung."

        s "Oh well, in it goes anyway!"

        "..."

        "Things go silent in the kitchen.{w} I can't tell if that's good or bad.{w} I'm too scared to look."

        h "I-Ist es wirklich okay?"

        s "Yup!{w} This is how it's supposed to--"

        with hpunch

        s "Wahhh!"

        "Something explodes in the kitchen.{w} Thick plumes of acrid smoke waft into the dining space.{w} Hmm."

        h "Mach es aus, schnell, es wird sich sonst ausbreiten!"

        s "How do I do that?!"

        h "I-Ich weiß nicht!{w} Versuch es einfach!"

        "Fwooom.{w} The roar of flames.{w} I can see the flickering of amber in my peripheral vision.{w} {i}Hmmmm{/i}."

        s "Nope!{w} That made it worse!"

        h "Wie wäre es...{w}damit?!"

        s "M-maybe!{w} It might have worked!"

        s "...Or not.{w} No more magic, okay?"

        h "Dieses mal wird es funktionieren--"

        s "No more magic!"

        h "Ich weiß sonst nicht was ich tuhen soll!"

        s "Hyah!"

        h "A-Ah, du verschüttest es überall!"

        "I hear water splash.{w} A good deal of it.{w} Like, an entire bucket's worth of the stuff."

        h "Ist es...{w}Ist es vorbei?"

        s "Hahhh...{w} I think so!{w} And look, the food is done!"

        h "Ich denke wirklich nicht das--"

        s "I said--the food is done!"

        with Pause(2.5)
        play music "bgm/everydayintro.ogg" fadein 2.0
        queue music "bgm/everydayloop.ogg"


        $ sayaface='smiling'
        $ hikaface='scared'
        $ sayapose='school_2'
        show Sayaka at center

        with dissolve

        "Apparently done, uh, 'cooking', the pair enter the dining space.{w} Sayaka has a plate in hand, a good amount of steam--or maybe smoke--drifting from it."

        s "I hope you're hungry, Kenta!{w} We really went all out to make this, you know!"

        "She puts a plate before me, a sincere smile on her face."

        "I...I guess she really gave it her all.{w} But...{w}this can't be called food."

        p "O-Oh.{w} Es ist ...{w} äh ..."

        "Charred, burnt, crisp remains of what might have been food at some point sit on the plate.{w} It feels like it might be hazardous to even breathe in this stuff."

        "I can see Hikari lurking further back, clearly ashamed of whatever...{w}substance they had created."

        "I guess this is my fault for letting them anywhere near the kitchen.{w} I should take responsibility, and--"

        menu:
            "Eat the food.":
                "I have no choice, do I?{w} I don't want to make her feel bad, after she worked so hard to create...{w}whatever this is."

                p "D-Dann probier ich mal ..."

                "I give the substance a poke.{w} It crumbles into a fine powder at the slightest touch.{w} Okay."

                "I'm sure even though it {i}looks{/i} absolutely terrifying, it can't be that bad.{w} Maybe there's something good, under all these layers of...{w}burnt stuff."

                "I scoop up as much as I can that doesn't crumble away from my hold and force it into my mouth, despite all my instincts screaming at me not to."

                "It's...{w}it's..."

                $ sayaface='happy'
                show Sayaka

                s "Well, is it amazing or what?"

                "Sayaka leans in expectantly as I swallow it down."

                "I think this must be what charcoal tastes like."

                "I fight back the urge to choke, and give her smile and a nod."

                p "M-Mmm!"

                $ sayapose='school_1'
                show Sayaka
                with dissolve

                s "Really?{w} Yay, I knew it!{w} You should let us cook for you {i}every{/i} morning!"

                "Oh god.{w} What have I done?{w} And I still have an entire plate of this stuff left!{w} These girls are clearly the real danger to my health and well being right now."
            "Refuse to eat the 'food'. I don't want to die!":

                "Okay, yeah, no.{w} I have to make a stand here, or things are only going to get worse."

                p "Schau, es tut mir leid, Sayaka, aber ich krieg das echt nicht runter."

                $ sayaface='normal'
                show Sayaka

                s "Huh?{w} Why not?"

                "She tilts her head to the side, a small frown beginning to grow on her face.{w} Great, make me feel like a monster why don't you!"

                p "Es ist ...{w} naja ...{w} wie soll ich es sagen, ohne ausfällig zu werden?"

                "I give the toxic substance another look, sure that it's beginning to move of its own accord."

                p "Würde ich es essen, könnte ich heute nicht mehr zur Schule gehen.{w} Oder den Tag danach."

                s "Oh?"

                p "Sayaka, what I'm trying to say is, I would be dead.{w} This stuff looks toxic."

                $ sayaface='scared'
                show Sayaka

                s "Oh."

                "Her frown deepens.{w} I'm sorry.{w} It had to be done."

                $ sayaface='normal'
                show Sayaka

                s "Are you sure?{w} It can't be {i}that{/i} bad."

                "Really?{w} Really?!{w} How could anyone defend this...{w}this...{w} I can't even call it food!"

                p "Okay, warum probierst du dann nicht zuerst?"

                $ sayaface='scared'
                $ sayapose='school_1'
                show Sayaka
                with dissolve

                "She pulls a face.{w} I knew it."

                s "U-uhh, I already ate."

                p "Schau, warum versuchst du--"

                $ sayaface='happy'
                show Sayaka

                s "But. I know Hikari hasn't!{w} She can show you how totally safe and tasty it is!"

                $ hikaface='shocked'
                $ hikapose='school_2'
                hide Sayaka
                show Hikari at center
                with dissolve

                h "E-eh?{w} Ich?!"

                "Hikari jumps as her name is called, still lurking quite a distance away from the 'food' that she had helped give life to."

                $ sayaface='smiling'
                show Sayaka at left
                show Hikari at right
                with dissolve

                s "Yeah!{w} Come on over here, show Kenta how delicious it is!"

                h "Das kann nicht dein Ernst sein.{w} Das Zeug ist--"

                s "Totally safe and edible!{w} Now get over here.{w} Please."

                $ sayapose='school_2'
                $ hikaface='scared'
                with hpunch
                show Sayaka
                show Hikari
                with dissolve

                "Sayaka thrusts a finger at the table with enough force that I think the plate rattled.{w} Yikes.{w} Despite the wide grin, though, I can't help but feel there's something sinister behind that."

                h "...Fein."

                "She approaches the food slowly, each step taking longer than the next, as if she was marching to her death.{w} Actually, that might very well be a possibility here."

                $ sayaface='happy'
                show Sayaka

                h "Wir haben es gemacht...{w}also kann es nicht so schlecht sein.{w} Es ist einfach nur ein wenig...{w}knusprig."

                "She outstretches a trembling hand towards the food, like it might bite her if she's not careful enough.{w} And then..."

                $ sayapose='school_1'
                $ hikapose='school_1'
                $ sayaface='shocked'
                $ hikaface='normal'
                show Sayaka
                show Hikari
                with flash

                "A bolt of magic erupts from her palm and hits the food, disintegrating it completely.{w} Along with the plate.{w} ...And a good portion of the table."

                $ hikaface='joking'
                show Hikari

                h "Oops!{w} Bin ich tollpatschig.{w} Meine Hand muss ausgerutscht...{w}sein.{w} Was eine Schande!{w} Und ich habe mich schon {i}so{/i} darauf gefreut, alles zu essen."

                "...I'm pretty sure magic doesn't just 'slip'!{w} And wasn't she the one that said they can't waste it on trivial things?"

                "...Maybe it was an emergency in her eyes."

                $ sayaface='scared'
                show Sayaka

                s "Hikari!"

                "Sayaka pulls another heartwrenching frown, but it doesn't last long before her usual optimism returns."

                $ sayapose='school_2'
                $ sayaface='happy'
                $ hikaface='scared'
                show Sayaka
                show Hikari
                with dissolve

                s "Oh well.{w} How about I make some more?"

                $ sayaface='shocked'
                show Sayaka
                with hpunch

                p "Nein!"

                "I bolt upright in my chair, almost taking it up with me in the process.{w} I don't think my house would survive!"

                "Maybe being a little louder than intended, I catch her off-guard and she jumps."

                s "H-huh?"

                p "Ich mein, wir würden zu spät zur Schule kommen, wenn ihr noch was kochen würdet."

                s "Oh...{w} You're right.{w} Look at the time!"

                "Phew.{w} Good save, me!"




    scene kitchen day
    $ hikaface='normal'
    $ sayaface='smiling'
    $ sayapose='school_1'
    $ hikapose='school_1'
    show Sayaka at left
    show Hikari at right
    with fade

    "So, with breakfast out of the way, it seems like Sayaka is finally ready to tell me what she had planned for the day."

    "I can tell she's had trouble keeping it to herself this entire time, as she looks like she might burst at any moment, practically shaking with excitement."

    "I don't even think Hikari truly knows what Sayaka has in mind, as she seems uneasy."

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    play music "bgm/everydayintro.ogg" fadein 2.0
    queue music "bgm/everydayloop.ogg"

    s "Okay!{w} It's time to discuss the plans for today!"

    $ sayaface='happy'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Kenta!"

    "She suddenly thrusts a finger at me, catching me off-guard as I jump a little."

    p "Äh ...{w} J-Ja?"

    $ sayaface='smiling'
    show Sayaka

    s "How do you feel about the beach?"

    $ hikaface='scared'
    show Hikari

    p "Strand?{w} Ich weiß nicht so recht--"

    s "Great!{w} So it's decided."

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    "But I didn't agree to anything!"

    h "S-Sayaka!"

    "Hikari is as distraught as I am about the whole thing.{w} Sayaka seems like she's made up her mind, though.{w} It's settled.{w} Whether we like it or not!"

    s "Come on!{w} It's the perfect weather.{w} We'd be crazy {i}not{/i} to go!"

    h "Aber an den Strand zu gehen meint..."

    "Hikari falls into troubled thoughts, her brow furrowing.{w} I'm sure she has her own personal reasons to hate this, as I have my own."

    s "It'll be fine!{w} Quit worrying, guys."

    "I know she said she was doing this for my benefit, since I don't get out that much.{w} But at the moment, I think the only person benefiting from this is Sayaka herself."

    "Clearly she just wants to do all the stuff she hasn't been able to do before, and drag me along as the perfect excuse."

    $ sayaface='smiling'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    "She's so fired up about the whole thing now, I don't think I can say no.{w} Heck, even if I said no, I get the feeling she'd just drag me down there anyway."

    p "Okay ...{w} okay.{w} Aber sollte ich in Flammen aufgehen, sobald ich dem Strand nahekomm, seid ihr schuld.{w} Meine Haut ist da sehr empfindlich!"

    $ hikaface='shocked'
    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "Kenta!{w} Du musst nicht alles tun was sie sagt, es ist manchmal wirklich perfekt--"

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Hush now, Hikari.{w} It's two against one.{w} You don't get any further say in the matter!"

    $ hikaface='angry'
    show Hikari

    h "A-Aber--"

    $ sayaface='smiling'
    show Sayaka

    s "You seemed excited about going out earlier!"

    h "Ich dachte nicht, dass wir ausgerechnet an den Strand gehen würden!"

    s "I don't know what it is that you're so afraid about, Hikari."

    $ hikaface='shy'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "D-Du weißt genau um was ich mich Sorge!"

    "Sayaka takes a moment to think, before she gives a teasing grin."

    $ sayaface='joking'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Ohhh.{w} I see.{w} But, I'm not sure why you're worried about that, you have an amazing b--"

    $ sayaface='scared'
    $ hikaface='embarrassed'
    show Sayaka
    show Hikari
    with hpunch

    h "Halt dein Mund!"

    "{i}Wham{/i}.{w} Hikari drives the wind out of her partner with a flashing straight to the stomach.{w} I...{w}don't even get what it is that they were arguing about.{w} Maybe it's for the best."

    $ sayaface='smiling'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Hrkk.{w} O-okay...{w} No need to get violent!"

    "Sayaka keeps up her grin, despite the fact she's doubled over and clutching at her core.{w} That really did look painful..."

    $ hikaface='angry'
    $ hikapose='school_2'
    show Hikari
    with dissolve

    "Hikari pulls her arms together and lets out a huff, turning her head to the side.{w} She's really against this thing, huh?"

    h "Wenn Kenta wirklich gehen will, hab ich keine Entscheidung...{w} Aber das sollte sich nicht zu einer normalen Sache werden!"

    $ sayaface='happy'
    show Sayaka

    s "Y-yay!"

    "Sayaka gives a hoarse cheer, still struggling to catch her breath."

    stop music fadeout 2.0

    scene bg black
    with fade

    "With everyone coming to an agreement on going to the beach today--some more reluctantly than others--we make preparations before heading out into the world.{w} The blindingly bright and hot world."

    "For whatever reason, halfway into the journey to the beach, the girls sprinted ahead and told me they'd be waiting for me there."

    "I thought they were supposed to always be by my side and protect me, especially when we were outside...{w} The beach is clearly more important than my own life though, so I'll let it slide this time."

    "And they left me to carry the majority of things too--all of the lunches and towels and whatever else Sayaka loaded up in a frenzy.{w} I'm just about able to keep upright with all these bags weighing down on me."

    "Combine all that with the blazing sun in a near cloudless sky, and I'm lucky I didn't pass out on the way there."
    play music "bgm/magicalgirlintro.ogg" fadein 2.0
    queue music "bgm/magicalgirlloop.ogg"
    scene beach
    with wake


    "I take the first step onto the sand.{w} The beach, at long last!"

    "The waves of the ocean lap gently at the shore, the water itself almost crystal clear as it stretches far into the horizon, merging with the blue sky.{w} It's a beautiful sight to be sure.{w} ...I just wish it wasn't so hot!"

    "Surprisingly enough, the beach isn't that populated.{w} There's a few people here and there, but it isn't as packed as I thought it would be.{w} I suppose we are nearing the end of the season for this sort of stuff.{w} I hope we don't stick out too much..."

    "That's a point.{w} Just where exactly are the girls?{w} I give the beach a scan over.{w} Where could they be...?"

    "I wander further onto the beach, the sand threatening to set fire to my feet the more I idle in it."

    s "Yoo-hoo, Kenta, over here!"

    "A familiar voice catches my attention.{w} Finally!"

    scene cg8
    with dissolve



    "I turn to the source of the voice to find...{w}oh, wow.{w} Okay, I wasn't expecting {i}that{/i}."

    "I can see why they ran ahead now.{w} To change into their rather...{w}let's say, flashy...{w}swimsuits."

    "They're sharing the same beach chair, hugging together in a pose I can only guess they've been holding for a while as they waited for me to finally catch up."

    s "Look, Hikari, he's speechless!"

    "Sayaka giggles, and hugs tighter against Hikari, who surprisingly, also has a smile on her face.{w} She must be enjoying this to a degree too, though, her cheeks are definitely burning up."

    h "D-Du must mich nicht so anstarren...{w}e-es ist peinlich."

    "She tries to shy away, but she doesn't really have anywhere to go with Sayaka still on top of her.{w} It's...{w}quite the compromising position."

    s "C'mon, Hikari, you don't have to be so modest.{w} You look great and should show a little pride!"

    s "You know, you've been turning heads ever since we showed up here!"

    h "W-Was?{w} Lüg nicht!"

    s "It's true.{w} I'm pretty jealous, actually.{w} It looks like you've stolen the show completely!"

    "Sayaka turns her attention to me.{w} Uh-oh.{w} I have a bad feeling about this."

    s "So, what do you think, Kenta?{w} Which one of us looks better?"

    "Oh, geez.{w} Really?{w} You're going to hit me with that?{w} I should think carefully before I answer..."

    menu:
        "It has to be Sayaka!":

            $ sayaka += 1

            p "I-Ich schätze, wenn ich mich wirklich entscheiden müsste, dann für ...{w} Sayaka."

            "Her face lights up at my answer, going just the slightest tinge of pink."

            s "Aww.{w} Really?{w} You're so sweet, Kenta."

            "She gives me a smile that's enough to make my heart throb.{w} Hikari, on the other hand..."

            "Her rare moment of happiness from before quickly sours, and she turns her head away from me with a 'hmph'.{w} That was to be expected, I suppose.{w} I can't win them all!"

            s "Even if the rest of the beach has fallen under Hikari's spell, I'm glad Kenta still has some sense."

            "Maybe I fed her ego too much?{w} She continues to glow, and prods at Hikari a couple of times with a smug grin."

            "Hikari's expression grows darker with each repeated prod, until..."

            stop music fadeout 4.0

            with hpunch
            scene beach
            $ hikaface='angry'
            $ hikapose='bikini_1'
            show Hikari at center
            with dissolve

            h "Okay, das ist genung!"

            s "Wahh!"

            "She pushes Sayaka off of her with one swift shove, her temper exploding."

            $ hikapose='bikini_2'
            show Hikari
            with dissolve

            h "Das ist so dumm!{w} M-Mich interessiert eh nicht, was Kenta denkt."

            "Sayaka tumbles into the sand face first with a yelp.{w} She lays still for a good moment, making me wonder if perhaps she lost consciousness in that fall.{w} But, as I stretch my hand out to see if she's okay, she bounds to her feet with a grin."

            hide Hikari
            with dissolve
            $ sayapose='bikini_1'
            $ sayaface='smiling'
            show Sayaka
            with moveinbottom

            s "Ahh, I'm okay, I'm okay!"

            "Saying that, she spits out a fair amount of sand.{w} ...Okay, whatever you say."
        "Hikari, of course!":


            $ hikari += 1

            p "Na ja, ich schätze ...{w} Hikari."

            h "E-eh?!"

            "If it was even possible, her face goes a deeper shade of red, and she fidgets some underneath Sayaka."

            h "D-Du kannst das nicht so meinen..."

            s "See?{w} I told you!{w} Even Kenta can't help but gawk at you."

            s "You and this perfect body of yours!"

            "Sayaka giggles and begins prodding all over Hikari."

            h "Ahh--haha--s-stop, k-kitzel mich nicht d-da!"

            "Hikari tries her best to stifle her own laughing as she writhes underneath Sayaka, who continues to assault her relentlessly.{w} ...I think they've forgotten about me completely."

            s "So...jealous!"

            h "O-okay, dass reicht...{w} Du kannst jetzt aufhören, S-Sayaka!"

            "Sayaka pays her desperate pleas no mind, and carries on."

            stop music fadeout 4.0
            with hpunch
            scene beach
            $ hikapose='bikini_2'
            $ hikaface='angry'
            show Hikari
            with dissolve

            h "Ich hab gesagt es ist genug!"

            s "Huh--waah?!"

            "Having finally had enough, Hikari explodes and pushes her off of the chair.{w} Sayaka tumbles down onto the sand, caught completely off-guard."

            $ hikapose='bikini_1'
            show Hikari
            with dissolve

            h "Ich schwöre, manchmal stimmt etwas nicht mit dir, Sayaka!"

            "Hikari heaves a sigh, finally able to recover after Sayaka's brutal assault of...{w}whatever that just was."

            $ sayaface='happy'
            $ sayapose='bikini_1'
            show Hikari at right
            with dissolve
            show Sayaka at left
            with moveinbottom

            "Sayaka leaps up to her feet and holds her arms out wide with a grin, as if to say, \"tah-dah, I'm still alive!\"."

            s "Yeesh.{w} No need to be so grumpy.{w} You could have just asked me nicely!"

            $ hikaface='normal'

            h "Hmph."

            "Hikari throws herself back and lounges in her chair.{w} Let's, uhh...{w}have some fun now?"
        "Meh.":

            p "Ihr wisst hoffentlich, dass ich hier gerade gegrillt werde.{w} Und um zu verhindern, dass ich ganz verkohlt werd, würde ich mich liebend gerne irgendwo in den Schatten setzen."

            "Shading my eyes as best I can with my hand, I look down the length of the beach, searching for the perfect spot to set all this stuff down."

            s "H-huh?{w} Kenta?{w} You don't have anything to say to this at all?"

            "Huh?{w} What's Sayaka so worked up for?"

            s "Nothing at all...?"

            "I shake my head and shrug my shoulders.{w} Am I missing something here?"

            scene beach
            $ hikaface='normal'
            $ sayaface='scared'
            $ hikapose='bikini_1'
            $ sayapose='bikini_1'
            show Sayaka at left
            show Hikari at right
            with dissolve

            stop music fadeout 2.0

            "Even Hikari seems offended, and does her usual turn of the head, her hair swishing along with her.{w} But it doesn't really take much for her to do that, so I'm not that surprised."

            s "Kenta!{w} You better just be messing around here.{w} After we spent ages picking these out..."

            p "Nop.{w} Ich steh gerade echt auf der Leitung.{w} Worum geht's denn?"

            $ sayaface='angry'
            show Sayaka

            s "It...{w}it doesn't matter."

            "Sayaka puts on a scary expression that's similar to that of Hikari's own.{w} Honestly, what did I do wrong?!"

            p "Ä-Äh ...{w} egal.{w} Ich such mir ...{w} erstmal ein schattiges Plätzchen."

            "I turn to wander further down the beach, while still feeling the painful, {i}painful{/i} stares of the two girls.{w} I'm not really sure what I did to invoke their ire, but I should probably figure it out soon, unless they just decide they don't want to protect me anymore."

    scene bg black
    with fade

    scene beach
    with fade

    play music "bgm/everydayintro.ogg" fadein 2.0
    queue music "bgm/everydayloop.ogg"

    "We finally set up our own little spot on the beach at a fairly shady area away from the general crowds.{w} It's pretty much isolated here.{w} Even peering down both sides of the beach, I only rarely see someone going by.{w} It's perfect!"

    $ sayaface='smiling'
    $ sayapose='bikini_1'
    show Sayaka at center
    with dissolve

    s "Ahh!"

    "Sayaka stretches her arms high into the sky as she basks in the sun's intense rays."

    s "See?{w} Isn't this the best?{w} And to think you guys didn't wanna come out here!"

    "I'm glad someone's enjoying themselves.{w} It really is far too hot, though.{w} Hikari seems to agree with my sentiment, as she keeps to the shade and lounges lazily in the beach chair."

    $ sayapose='bikini_2'
    show Sayaka
    with dissolve

    s "Hmm, what to do first...?"

    "Sayaka mumbles to herself as she makes her way to one of the bags that I was pretty much forced into dragging all the way over here."

    "She starts to rustle through the bag.{w} ...I don't even know what she's put in there.{w} But from the sounds of it, there's a {i}lot{/i} of stuff.{w} More than we'll ever need for today, I'm sure."

    $ sayaface='happy'
    show Sayaka

    s "Here we go.{w} Perfect!"

    s "Catch, Kenta!"

    $ sayaface='smiling'
    $ sayapose='bikini_1'
    show Sayaka
    with dissolve

    "She pulls out something colourful, and tosses it my way."

    p "Häh?"

    "I wrestle with it for a moment before I finally understand what it is.{w} It's a deflated beach ball.{w} I think.{w} I'm not really an expert with these things."

    s "You can handle that, right?"

    p "Na klar!"

    "I say that with confidence, but it really does take me a good moment or two to even find where to inflate it.{w} Argh, it's like trying to solve a damn puzzle.{w} Complicated thing!"

    with Pause(3.5)
    with fade

    "I just about nearly kill myself in the process of inflating it, as Sayaka continues to rummage around in the bags for whatever treasure it is she has in mind."

    p "O-Okay ...{w} Nicht nur beinahe."

    "I let out a wheeze as I present the beach ball to her, my lungs on the verge of exploding."

    $ sayaface='happy'
    show Sayaka

    s "Oh, good job!{w} Throw it back over!"

    "I pass it over to her with a feeble throw.{w} It just barely sails through the air, enough for her to reach out and catch it.{w} ...That was embarrassing."

    "Sayaka clutches the ball as she mulls over how best to use it.{w} She gives me a look, before she gazes over towards Hikari, who seems to be fast asleep on the chair at this point."

    $ sayaface='joking'
    show Sayaka

    "A dangerous expression takes over Sayaka's face.{w} She couldn't possibly think to--"

    $ sayaface='happy'
    $ sayapose='bikini_2'
    show Sayaka
    with dissolve

    s "Hikari, catch!"

    with hpunch

    "She flings the ball at her partner, and it rebounds off of her skull with a far heavier impact than something that's inflated should have."

    hide Sayaka
    $ hikaface='shocked'
    $ hikapose='bikini_1'
    show Hikari
    with dissolve

    "Hikari awakes with a start, and lets out a pained yelp, almost falling off of the chair completely."

    h "H-huh...?{w} Wer...Was?!"

    $ sayapose='bikini_1'
    show Hikari at right
    show Sayaka at left
    with dissolve

    s "I said to catch, Hikari!{w} I gave you fair warning and everything."

    "Sayaka lets out an exaggerated sigh, a dangerous glint behind her cheerful eyes.{w} ...Was that payback for what happened earlier?{w} Remind me to never get on Sayaka's bad side."

    $ hikaface='normal'
    show Hikari

    h "Was?{w} Ich erinnere mich nicht..."

    "Hikari gives us both a startled and confused look.{w} She still has no idea what happened.{w} Maybe it's better this way, so the pair don't break out into a fight again.{w} We're here to have fun after all!"

    $ sayaface='smiling'
    show Sayaka

    s "Enough slacking, guys!{w} C'mon, let's play for real!"

    hide Sayaka
    show Hikari at center
    with dissolve

    "Sayaka collects the ball from the ground and dashes out from under the shade, and into the hot sun.{w} She beckons for both of us to follow after her."

    h "..."

    "A dazed Hikari totters from out of her chair and goes to join Sayaka.{w} She blinks unevenly as she passes by me.{w} ...Is she okay?"

    hide Hikari
    with dissolve

    "I'm...{w} I'm sure she's fine."

    s "C'mon!{w} Kenta?{w} What're you waiting for?"

    p "Komm schon!"

    "If I stand around over here any longer, I fear Sayaka might 'accidentally' hurl the beach ball my way, and let me suffer the same fate as her partner."

    "I dash out onto the hot sand, taking care not to stand in one place for too long in fear of catching alight.{w} Did I mention how hot is it was?{w} Hot, hot, hot!"

    $ sayaface='happy'
    $ sayapose='bikini_1'
    show Sayaka at center
    with dissolve

    s "Heads up, Kenta!"

    "She tosses the ball into the air, leaps, and then spikes it towards me with a heavy fist.{w} Oh god, that thing is going way too fast.{w} There's no possible way I can--"

    with hpunch

    p "Oof!"

    "Yup.{w} That's about what I expected."

    "The ball bounces off my head with enough force to leave me seeing stars, and rebounds back towards Sayaka.{w} I...{w}I sort of hit it back.{w} That counts for something, right?"

    $ sayaface='smiling'
    show Sayaka

    s "Okay, your turn, Hikari!"

    "Not content with just bludgeoning me, she sets her sights on poor Hikari again, giving the ball another good thwack."

    hide Sayaka
    show Hikari at center
    with dissolve

    h "H-huh?"

    "Still not all quite there, she bops it away with an awkward slap.{w} The ball sails past both of us and lands with a splash, just at the water's edge."

    h "Oh.{w} Oops.{w} Ich werde es holen!"

    $ hikaface='shocked'
    $ hikapose='bikini_2'
    show Hikari
    with dissolve

    "She hurries on over to collect the ball, but stops in her tracks as her eyes fixate onto something in the sea.{w} At first, she squints, as if unsure...{w}but very slowly her eyes widen in shock."

    h "Uhhh...{w} Ich denke ihr zwei solltet rüberkommen."

    $ sayaface='smiling'
    show Sayaka at left
    show Hikari at right
    with dissolve

    s "Hmm?{w} What's up?"


    stop music fadeout 4.0

    "I feel a twinge of pain strike my skull, my vision blurring for just a moment.{w} Oh, you've got to be kidding me..."

    "I hope in vain that it's just a normal headache, maybe started from the beach ball.{w} But as I look at Hikari's face as she stares into the ocean, I know it's going to be something worse."

    h "Sagt mir, ich bin nicht der einzige der das sieht..."

    $ sayaface='shocked'
    show Sayaka

    s "What are you...{w}wahh!"

    "I join the pair by the shore.{w} What on earth are they staring at?"

    "I peer out into the deep blue.{w} I'm still not sure what all the fuss is about."

    p "Ich ...{w} Ich versteh's nicht.{w} Verarscht ihr mich gerade?"

    $ hikaface='angry'
    $ hikapose='bikini_1'
    show Hikari
    with dissolve
    play music "bgm/ominousintro.ogg" fadein 2.0
    queue music "bgm/ominousloop.ogg"
    h "Nein!{w} Schau untem im Wasser!{w} Siehst du es nicht?"

    "Eh?{w} Under?"

    "Wait...{w}was the water always that dark?"

    "Hang on.{w} That's..."

    p "Das ist ein Schatten?!{w} Der ...{w} ist ja riesig!"

    "Something is coming up from the ocean, slowly making its way towards us.{w} Why can't I even get a single day off from all of this madness?!"

    "What can only be described as a gargantuan mass of ooze begins to emerge, bringing up half the sea with it as it towers...{w}and towers...{w}and towers over us."

    "It's a grotesque creature, that lets out a sinister gargle as it sets what I think are its eyes upon us.{w} It towers up so high it eclipses even the sun behind it.{w} It has to be at least as big as a common building, if not more so!"

    p "Und dagegen wollt ihr kämpfen?{w} ... {i}Könnt{/i} ihr dagegen überhaupt kämpfen?"

    scene cg18
    with dissolve


    "It continues to drag itself from out of the sea, slimy tendrils thrashing as it draws ever closer.{w} I can't imagine conventional weapons even scratching something as big as this."

    h "Das?{w} Hah.{w} Das ist...{w}kein Problem!"

    "She doesn't sound very sure of herself there.{w} I don't blame her, at all."

    "Hmm.{w} It moves so slow...{w}maybe we could just walk away from it?"

    "But, then it might cause complete mayhem if it were to get anywhere further than the beach.{w} I shudder to imagine the chaos that thing could cause in a busy street."

    h "Wir haben das!{w} Wirklich!"

    "Again, you're not filling me with confidence here."

    "And Sayaka hasn't even donned her battle gear yet.{w} Does she maybe realise how useless it is?{w} She's simply analysing it, a finger to her chin."

    h "Diese Art von Dingen mag gegen physische Angriffe resistent sein, aber Magie sollte sie durchbrechen! {W} ... Zumindest in der Theorie."

    "Her hand gives off a faint glow and she furrows her brow in determination."

    h "Ja.{w} Das sollte funktionieren.{w} Guck, ich werde es mit einer einzigen Explosion beenden!"

    "The light in her hand intensifies, growing into a pulsating orb that hovers just above her palm.{w} I wonder how this magic stuff works anyway?{w} It's always so surreal whenever I see them just casually wield it like this."

    with hpunch

    "Something taps at my shoulder."

    p "Häh?{w} Sayaka--"

    s "Shh."

    "She shushes me with a finger to her mouth, before taking hold of my wrist and dragging me a good distance from Hikari, who is still focused fully on the slime."

    stop music fadeout 7.0
    scene beach
    $ sayaface='smiling'
    $ sayapose='bikini_1'
    show Sayaka
    with dissolve

    "Eventually we end up behind a large rock cropping up from out of the sand, out of sight from both Hikari and the monster.{w} Understandably, I'm more than a little confused."

    p "Was ist los?{w} Solltest du ihr nicht helfen?"

    "Sayaka stifles a giggle and peeks back out at the scene unfolding on the shore.{w} It looks like Hikari is just about ready to attack."

    s "I don't think she's realised it."

    p "Was bemerkt?"

    $ sayapose='bikini_2'
    show Sayaka
    with dissolve

    s "Well, think about it.{w} That thing is huge.{w} And she's about to strike its core with a blast of pure magic.{w} What'll happen, do you think?"

    "I raise an eyebrow.{w} How the heck am I supposed to know something like that?"

    p "Häää ...?"

    "Sayaka sighs, before she slaps her hands together."
    play music "bgm/mischiefintro.ogg" fadein 2.0
    queue music "bgm/mischiefloop.ogg"
    s "It'll go boom!{w} Explode!{w} Those kinds of shadows are super volatile when you throw magic into the mix."

    p "Das ist mir zu hoch.{w} Ist das nicht gut?{w} Ein Monster weniger, um das wir uns Sorgen machen müssen."

    $ sayaface='joking'
    show Sayaka

    s "Just watch."

    "A mischievous grin flashes across her face.{w} I wonder if I should call out for Hikari to stop...?"

    hide Sayaka
    $ hikaface='angry'
    $ hikapose='magical_1'
    show Hikari at center
    with dissolve

    "But as I peek out from our shelter, it's too late.{w} Hikari unleashes the magic she had built up, and it strikes the towering abomination in its center."

    "...Nothing happened?{w} The orb of light was just swallowed up by the slime, as if nothing had struck it."

    "I don't see what Sayaka was so worried about.{w} Volatile?{w} Hah, there was no reaction at--"

    scene bg white
    with flash

    "The monster detonates without warning in a dazzling explosion of harsh light that takes over my vision.{w} Shortly after, I hear a terrified cry from Hikari."

    "As the light begins to fade, I hear the pitter-patter of something falling against the sand.{w} ...Rain?{w} No, the skies are practically clear today.{w} I think it's much worse."

    "I carefully take another look at the shore, making sure to stay well behind the rocky shelter."

    scene cg7
    with wake

    "It's...{w}it's raining slime?{w} A good amount of the vile ooze continues to coat the beach, all that remains of what was once a giant creature.{w} Huh.{w} I thought it would have put up a bigger fight."

    "And at the center of the mess is a very traumatised Hikari, coated in a great deal of the stuff."

    "The slime around her gives off a violent sizzle.{w} Thankfully it doesn't seem strong enough to cause any real harm, but it's ate away a good portion of her outfit.{w} ...It's really not a pretty sight."

    h "..."

    "She says nothing.{w} She doesn't even move.{w} She's seized up completely under the foul substance, only occasionally blinking as the situation soaks in.{w} Literally."

    "The rain of slime finally comes to an end, making it safe to step out.{w} Though, I have to be careful not to step into any of this slime.{w} Eurgh.{w} I can't even begin to imagine how Hikari must be feeling."

    p "H-Hikari, bist du ...?"

    h "...Kein einziges Wort."

    p "Aber--"

    h "Ich sagte, 'kein{w} {i}einziges{/i}{w} Wort'."

    "Her shoulders are visibly shaking.{w} Uh-oh.{w} The world might have survived the giant slime, but it looks like we might have someone else that's about to go on a rampage."



    s "My, this is quite a mess."

    "Sayaka chirps, as she slinks from behind the rock too, a grin across her face."

    h "S-Sayaka, nicht einmal..."

    s "I wonder what they'd think of all this back home, hmm?"

    h "Ich habe nich nachgedacht!{w} Denn Strand-Ball denn du nach mir geworfen hast..."

    "Sayaka clicks her tongue and nimbly evades the slime across the sand as she approaches her partner, still bearing the same smug look."

    s "Excuses, excuses!{w} I didn't think one of the top students would pull a blunder like this."

    h "Es ist nicht meine Schuld!"

    "Wait...{w}something doesn't make sense."

    p "Sayaka."

    s "Hmm?"

    p "Wenn du wusstest, dass das passiert, warum hast du sie dann nicht aufgehalten?"

    s "Ah, a good point.{w} I could've...{w}but..."

    s "Where's the fun in that?"

    "...Her smile suddenly looks all the more devious.{w} This girl is pure evil!"

    h "Warum passiert soetwas immer mir?!"

    "Hikari lets out a groan as she attempts to pry herself free of the sticky substance that clings to her skin.{w} ...Be strong, Hikari!"

    stop music fadeout 6.0

    scene bg black
    with fade

    "Our fun at the beach comes to a rather abrupt and messy end, thanks to the unwanted guest having crashed the party."

    "Naturally, we couldn't just leave the slime there as it was, so several more hours were spent in cleaning it up to make the beach safer."

    "It wasn't a fun job.{w} At all.{w} In fact, I think some of that slime must have still had some semblance of sentience to it, as it stubbornly fought back against my best efforts to sweep it back into the ocean."

    "Man, I can't believe I had to spend the good part of a day off sweeping up goop off the beach.{w} I can't blame Sayaka, though.{w} It's not like she knew this was going to happen when she came up with the idea."

    "But, her insistence on watching Hikari make a mess of things didn't help matters!"
    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"
    scene town street night
    with fade

    "We trudge through the streets, the day well and truly gone.{w} The sun sinks in the horizon, basking the world in a hazy, orange glow."

    $ sayaface='normal'
    $ hikaface='normal'
    $ sayapose='school_1'
    $ hikapose='school_1'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "Nobody says anything, and I can only see an exhausted face to either side of me.{w} All the fuss at the beach really took it out of us.{w} I don't think Hikari has even said more than a few words since she was first covered in slime."

    "Despite the exhaustion, both of them still seem to be on guard, their eyes scanning over the shadows as we continue on."

    "Right.{w} So far with each walk home, Yuzuki has ambushed us.{w} That deranged dark angel."

    "It would only make sense if she were to swoop in while we were exhausted like this.{w} It'd be an easy win.{w} I don't even know if the girls have it in them to fight at the moment."

    "But...{w}nothing.{w} Nothing attacks us."

    "No mad giggle from the shadows.{w} No more monsters striking from the darkness.{w} Just...{w}nothing."

    "It's bit hard to believe that after all the effort she had went through in past nights, that she would simply just let us go this time around."

    "Unless she's deliberately trying to get us to lower our guard, and is hidden further up ahead?"

    "Argh!{w} I'm getting paranoid now."

    "At the very least, I haven't had any more headaches since the slime at the beach.{w} And usually they're the most intense when I'm confronted by Yuzuki, for whatever reason."

    "I'll trust my head.{w} It seems to be the most reliable thing when it comes to these otherworldly encounters."

    scene bg black
    with fade

    "We make it home, not a single dark angel in sight."

    "I part ways with the girls with a lazy wave and a grunt, both of them responding with about the same level of enthusiasm.{w} I think we all just want to pretend today didn't happen.{w} Well, mostly Hikari."

    "I somehow get the feeling she'll probably be the one to remember it the most, however."

    "The rest of the evening is a blur.{w} I think I ate dinner at some point, and maybe lazed around on the couch for a while watching a show I can't really remember much about, before finally crashing for the night."



    "As I'm dragged into my dreams, I get the feeling that something terrible is lurking within them.{w} Something I shouldn't ignore.{w} ...But, all I know is that I won't remember any of this the moment I wake up."

    with Pause(3.5)
    scene bedroom day
    with wake

    "Morning arrives.{w} Again.{w} My head is killing me.{w} Again."

    "I'm going to bed earlier each night, yet somehow I'm feeling more and more like garbage each time I wake up.{w} I don't get it."

    "The only difference today is that the usual cheery rays of the morning sun are nowhere to seen.{w} In their place is the heavy sound of rain, hammering against the window."

    "Pulling back the curtains, today looks to be a gloomy day.{w} Gray skies overhead cast a depressing shadow on the town below, the torrential downpour showing no signs of stopping any time soon.{w} Great!"

    "And I have to go out in this weather and all.{w} It's not going to be a fun day, that much I can already tell."

    "I stretch and let out a drawn out yawn, before I stagger towards the bathroom."

    "Wait."

    "My hand hovers over the handle as I just about stop myself from carelessly swinging the door open.{w} That was a close one!"

    "I need to approach this situation carefully.{w} Too many mistakes have been made before.{w} I've been lucky to escape with my life before, but they might not be so forgiving a second time."

    "Okay.{w} Deep breaths.{w} I can do this."

    "I thump the door a good several times with the back of my fist."

    p "Hallo?{w} Jemand zuhause?"

    "..."

    "No response.{w} But I've been fooled before.{w} This proves nothing."

    "I bang on the door again, even louder than the previous time."

    "Nothing."

    "Surely someone would have heard that if they were on the other side.{w} Which means it...{w}might be safe?"

    "I bring the door open a crack.{w} Just a little, and peer through."

    "So far, so good."

    "I continue to open the door just a little more, and a little more...{w}until..."

    "I see it.{w} A most wondrous sight takes my breath away."

    "It's...{w}it's so beautiful.{w} It's enough to move a man to tears."

    "...The bathroom is actually empty for once.{w} No wacky misunderstandings, no awkward stares...{w} I can actually just freely use the bathroom today without the threat of being torn apart."

    "I waste no time in slipping inside and firmly locking the door.{w} I even double--triple check the lock--something they should have been doing too, but always forgot!"

    scene bg black
    with fade

    "After a peaceful shower, I make my way down to the kitchen, where Hikari and Sayaka are waiting for me."

    scene kitchen day
    $ hikaface='normal'
    $ sayaface='smiling'
    $ hikapose='school_2'
    $ sayapose='school_1'
    show Sayaka at left
    show Hikari at right
    with fade

    h "Ugh, es ist schrecklich dort draußen."

    "Hikari gazes out of the window, a look of disgust across her face.{w} With the laundry list of other things that annoy her, I guess it's no surprise she hates rain too."

    h "Müssen wir heute wirklich in die Schule, Kenta?"

    s "Aww, c'mon.{w} It's just a bit of water.{w} You're not gonna melt in it or anything."

    $ sayaface='joking'
    show Sayaka

    "Sayaka grins dangerously as something sparkles in her eyes.{w} Uh-oh..."

    s "It's less harmful than the stuff you got covered in yesterday, anyway."

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    "She tries her best to suppress a giggle, but fails, her laughter soon rocking the house.{w} Conversely, Hikari is less than amused."

    $ hikaface='embarrassed'
    show Hikari

    h "S-Sayaka!{w} Können wir das jetzt endlich vergessen?{w} Ich war dumm, Ich hab ein Fehler gemacht.{w} Große Sache!"

    "Flustered, Hikari stomps a foot towards her mischievous partner.{w} We haven't even reached school yet, and they're already arguing!{w} I think that's a new record."

    h "Und außerdem weiß ich noch, dass {i}du{/i} es warst, die kurz davor war mit deinen Mätzchen von der Akademie ausgeschlossen zu werden."

    $ sayaface='joking'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Eh-heh-heh...{w} What can I say, they just don't appreciate a good joke!"

    $ hikaface='angry'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Scherz?!{w} Du hast fast alles in die Luft gespr--"

    "Realising I am indeed still in the room, Hikari cuts herself short and clamps up.{w} Aww.{w} I guess I'll never be able to hear about this old school of theirs.{w} The 'magic' one that taught them all they know."

    h "Belassen wir es doch jetzt einfach dabei und ich stimme dir zu das wir beide einmal dumm waren, okay?"

    $ sayaface='smiling'
    show Sayaka

    s "'Kay.{w} I really don't think I was that bad, though..."

    $ hikaface='normal'
    show Hikari

    s "Anyway, Kenta, how about I cook us all some--"

    $ sayaface='shocked'
    show Sayaka

    p "Nein!{w} Sicher nicht!"

    s "But you didn't even let me--"

    p "Brauch ich nicht.{w} Wenn es darum geht, dass du in der Küche das Essen anrührst, egal in welcher Farbe, Form oder sonst was, gibt's nur eine richtige Antwort."

    $ sayaface='scared'
    show Sayaka

    s "This time it'll really be--"

    p "Nop."

    s "I'll be careful--"

    p "Nööö."

    $ sayaface='angry'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Aww, you're being--"

    p "Nein!"

    "Yeah, I'm not letting her {i}or{/i} Hikari anywhere near the kitchen again.{w} Even if they do somehow manage to leave the kitchen standing, I'm sure whatever monstrosity they concoct would do more damage to me than any monster lurking out there!"

    "Sayaka heaves a dramatic sigh, purses her lips in a pout, and gives me a look that suggests I've been nothing but a massive disappointment to her.{w} Hey, I'm not the bad guy here!"

    $ sayaface='smiling'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    "It doesn't last long though, before her usual cheery expression takes over again.{w} I think it must be impossible to truly upset this girl."

    scene bg black
    with fade

    "After that little dose of excitement for the morning, I quickly prepare a meal for the three of us before we set out into the town and brave the storm."

    scene town street day
    with fade

    "The rain shows no signs of letting up.{w} It's hard to believe that the weekend was as bright and cheerful as it was, when dark clouds have completely eclipsed the sun overhead now."

    "We have nothing but flimsy umbrellas to defend ourselves with, that just barely hold under the immense downpour.{w} I have my doubts if we'll even be able to make it to school dry."

    "I'm not really sure how it got this bad all of a sudden.{w} If it keeps up throughout the day, we might even have flooding to worry about."

    "...I feel a little silly for even have this cross my mind, but I can't help but feel that this is maybe the land lamenting in some way.{w} A sign of things to come.{w} I don't know I'm even thinking such nonsense, but it won't leave my head no matter how hard I try."

    "Looking back up at the skies, the clouds seem even more sinister than before..."

    scene bg black
    with fade

    with Pause(2.5)

    scene classroom
    $ sayaface='smiling'
    $ sayapose='school_1'
    $ hikaface='normal'
    $ hikapose='school_1'
    show Sayaka at left
    show Hikari at right
    with fade

    "We make it to school without drowning.{w} Somehow."

    s "Whew.{w} It was pretty intense out there!"

    "As we enter the classroom, Sayaka shakes herself dry, her hair swishing wildly.{w} Right beside Hikari."

    $ hikaface='angry'
    show Hikari

    h "Ugh, schau es dir an!{w} Du bist fast wie ein Hund!"

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Hmm?"

    "She stops and blinks innocently, the last drops of water splashing to the ground.{w} I can't tell if she's just playing dumb here, or if she really did it by accident.{w} ...That's what makes her so scary sometimes."

    $ hikaface='normal'
    show Hikari

    h "Vergiss ess."

    hide Hikari
    hide Sayaka
    with dissolve

    "Hikari huffs and stomps over to her seat, with class just about to start."

    "I follow suit and crumple into my seat with a sigh.{w} What a depressing day it's turning out to be."

    "As the teacher shows up and class begins, I give one last look out the window, water streaming so heavily down the glass I can just barely make out what's on the other side."

    with Pause(2.5)

    "..."

    "The lesson goes on, though with each passing moment, I find it more and more difficult to focus on the subject at hand, the writing on the board blurring into an incomprehensible mess."

    "I can feel it.{w} At the back of my skull.{w} That familiar, creeping pain."



    "Why here?{w} I've never had these headaches at school.{w} They usually only crop up when something bad is about to happen..."

    "I guess it's not a full blown headache, so I shouldn't have anything to worry about for now."

    "Is it a warning?{w} That something's coming?{w} I don't know what to make of it at all."

    s "Kenta?{w} Are you okay?"

    "I hear Sayaka whisper from her seat behind me, a gentle hand on my shoulder.{w} I look to my side and see Hikari giving me an equally worried glance."

    "Did I look that bad?{w} Maybe the headaches are affecting me more than I think."

    "I nod my head and muster up a faint smile.{w} I can just barely even convince myself I'm fine, but it's enough to make them focus back on the lesson at hand."

    scene bg black
    with fade

    "Lunchtime arrives, and I can just barely recollect what I was taught.{w} What subject even was it...?{w} Ah, that's not important right now."

    "At least now I have the time to collect my thoughts and get a grip on the situation."

    scene classroom
    $ sayaface='smiling'
    $ sayapose='school_1'
    show Sayaka at center
    with fade

    s "We're gonna go get lunch, Kenta.{w} Do you wanna come with us, or...?"

    "Having hopped out of her seat, Sayaka skips to the front of my desk and peers down at me with a grin."

    "I blink.{w} It takes me a good second to register that anything has been said to me."

    p "Häh ...?{w} Oh.{w} Geht ihr ruhig vor.{w} Mir tut gerade mein Kopf ein bisschen weh ..."

    $ sayaface='normal'
    show Sayaka

    "Sayaka offers a sympathetic look when I mention the headache."

    s "Kenta, about the headaches..."

    s "They're..."


    $ sayaface='shocked'
    $ hikaface='angry'
    show Hikari at right with moveinright
    show Sayaka at offscreenleft
    show Hikari at offscreenleft
    with move
    with hpunch

    s "Mmppff!"

    "Hikari pops up out of nowhere and stifles Sayaka with a hand to her mouth, before she begins dragging her out of the class."

    h "Komm schon, Sayaka.{w} Er muss nichts davon wissen, und die Warteschlangen werden zu groß, wenn wir hier nur rumstehen!"

    s "Mmmff!"

    "Sayaka's muffled cries of distress are the last thing I hear before the pair vanish into the corridor.{w} Huh."

    "Wait...{w} 'Headaches'?{w} Does that mean she knows I've been having them frequently?"

    "And more than likely, knows the cause of them?"

    "If they know anything that will enlighten me on this bizarre series of recent events, then I really have to chase them up on it.{w} I can't let something as important as this be slipped under the rug like everything else they've tried to keep from me."

    "I rise up from my desk with a wobble, my legs not quite all there.{w} They should be at the cafeteria, right?"

    "I start for the corridor myself, but someone catches my eye amongst the waves of students going by."

    $ yuzuface='normal'
    $ yuzupose='school_1'
    show Yuzuki at center
    with dissolve

    "Silver hair, and amber eyes, a female student marches along with a blank expression."

    "My head rings.{w} Where have I seen her before?"

    "Wait...{w} Is she really...?"

    show cg11 with dissolve
    hide cg11 with dissolve

    "There's no doubt about it.{w} She's the dark angel that has been making our lives a living hell.{w} Yet, she seems like a completely different person right now.{w} Gone is any trace of madness.{w} All I see right now is an emotionless schoolgirl."

    p "...Yuzuki?"

    "Her name falls out of my mouth the moment I come to the realisation."

    "Has she always been at this school...?{w} How did I not notice something as obvious as this before?!"

    "Our eyes lock across the crowds.{w} I fear something terrible is going to happen as dread sets in...{w}but her gaze quickly flickers away before she carries on about her business."

    hide Yuzuki
    with dissolve

    "Huh?{w} She was so intent on getting me before, and now she wants nothing to do with me?{w} Something isn't adding up here."

    "I know it's a stupid, and reckless thing to do, but I can't help but chase after her.{w} If I go to get Sayaka and Hikari, she might be gone by then."

    with hpunch

    "It's hard to keep up with her as the waves of students crash against me--everyone in a frenzy to get their lunch--but I just about manage to catch a glimpse of her heading for the staircase."

    p "Yuzuki, warte!"

    "She pays me no mind, and continues to ascend the stairs."

    "...Why am I following her?{w} I don't know what I can possibly get out of this, beyond an early demise.{w} Yet I still insist on hiking up the stairs after her."

    "She seems so different.{w} Maybe I'm just secretly hoping that there's more to her than the initial, crazed monster that confronted us two times before.{w} Something that will help me make sense of this mess."

    "I reach the top floor, breathless after climbing the stairs two steps at a time.{w} I peer out into the corridor to try and see where she might have gone to, but there's nothing."

    "I'm sure I wasn't that far behind, though.{w} So where did she disappear to?!{w} I mean, this is where the stairs end.{w} Unless..."

    "Would she really be out there?{w} In {i}this{/i} weather?!"

    "I make for the staircase again, and go up a short flight of stairs leading to the rooftop.{w} The rain sounds more violent than ever outside.{w} I can't possibly imagine someone willingly wanting to be out there.{w} But I have to check, just to be sure."
    stop music fadeout 3.0
    "I fight against the raging winds and heave the door open."

    scene school roof
    with dissolve

    p "Y-Yuzuki ..."

    scene cg9
    with dissolve
    play music "bgm/sadintro.ogg" fadein 2.0
    queue music "bgm/sadloop.ogg"

    "There she is, standing by the fencing, gazing out over the town with a hand idly gripping the mesh.{w} Already the rain has drenched her completely, her soaked uniform clinging to her skin."

    "She seems completely unbothered by it though, as if she doesn't feel the rain at all.{w} I've only been out here for a second, and I can already feel the urge to sneeze creep up as the chilling rain makes short work of me."

    "Yuzuki ignores me, her amber eyes vacant."

    "At the very least, she doesn't seem hostile at the moment.{w} Right now, I think the rain has a more likely chance of killing me than she does."

    "I take a step toward her, my foot splashing into a sizeable puddle."

    y "Was willst du?"

    "She responds bluntly.{w} I may as well be talking to a completely different person than the girl that went after my life."

    "I think carefully before opening my mouth.{w} While things are peaceful right now, it might take saying only one wrong thing to set her off."

    "But, I can't be too reserved.{w} I want answers!"

    "After hesitating for a moment, my voice initially coming out in a croak, I finally confront her."

    p "Ich ...{w} Warum willst du mich unbedingt umbringen?{w} Ich versteh es einfach nicht!"

    p "Was ich damit mein, ist ..."

    p "Warum ausgerechnet ich?"

    "She tenses up for a moment at the sound of my voice.{w} I fear I might have said the wrong thing already, but she gradually relaxes again."

    y "Ich bin überrascht, dass du mich heute überhaupt bemerkt hast..."

    y "Sag es mir Kenta..."

    y "Wie lange sind wir schon in der gleichen Klasse?"

    p "Was ...?"

    "Has she really...{w}been in the same class as me?{w} I'm sure I would have pieced together things a lot sooner if that were the case."

    "Yuzuki lets out a bitter laugh."

    y "Du hast es nicht einmal bemerkt, oder?"

    p "Ich bin mir nicht ganz sicher ..."

    y Ich kann auch ein Geist sein.""

    y "Weißt du, wie es sich anfühlt, vollkommen unsichtbar zu sein? Wenn niemand auch nur einen Blick in meine Richtung wirft?"

    "Her grip tightens on the fence, the wires sinking into her flesh.{w} What is she talking about...?"

    y "Nie als Partner für Projekte ausgewählt werden...{w}niemals gebeten werden, mit jemandem Mittag zu essen...{w}im Unterricht sogar vom Lehrer ignoriert zu werden."

    y "Sie alle scheinen kleine, kleine Dinge zu sein.{w} Aber im Laufe der Jahre summieren sie sich.{w} Und langsam setzte der Hass ein."

    y "Menschen sind selbstsüchtig, unhöflich, arrogant."

    y "Und du denkst wahrscheinlich nur, 'warum machst du dir nicht die Mühe, selbst Freunde zu finden?'"

    "I...{w}I guess that thought did come to mind.{w} All I can do is stand and listen as she continues, ignoring the urge to shiver."

    y "Glaubst du, ich habe es nicht versucht ?!{w}Ich habe mich so sehr bemüht, mich einzufügen. {w} Um sozial zu sein, mit Leuten zu reden."
    
    y "Aber nach einem gewissen Punkt sind die sozialen Kreise fest und werden zu unpassierbaren Mauern für diejenigen, die mitmachen wollen."

    y "Meine fröhlichen Grüße wurden völlig gleichgültig aufgenommen.{w} Meine Versuche, mit Klassenkameraden zu sprechen, wurden mit schmerzhaften Blicken beantwortet."

    y "Und dann ist es wieder zu Hause, um in einem dunklen, einsamen Zuhause zu sitzen, bevor ich mich zwingen muss, wieder zur Schule zu kommen.{w} Ein Ort voller Menschen, doch hier fühle ich mich am einsamsten."

    y "War es zu viel verlangt nach einem Freund zu suchen?{w} Mit jemandem, mit dem ich reden konnte, dem ich mich anvertraue und mit dem ich Spaß habe...{w}genau wie in den TV-Shows.{w} Ist das wirklich zu viel ?!"

    scene school roof
    $ yuzuface='normal'
    $ yuzupose='school_1'
    show Yuzuki
    with dissolve

    "So she's just lonely...?"

    p "Aber warum ..."



    "She cuts me off as she suddenly spins to meet me eye to eye.{w} The vacant stare is gone, and in its place one of hate.{w} Aimed directly at me."

    y "Aber es tut mir nicht leid.{w} Nichts davon zählt mehr.{w} Nicht nach morgen.{w} Alles wird sich verändern."

    p "Morgen?"



    "As I ask her, a searing heat surges through my skull and forces a wince out of me."

    $ yuzuface='smiling'
    show Yuzuki

    "Yuzuki smirks at my pain."

    y "Du kannst es fühlen, oder?{w} Sie ist jetzt so nahe daran, frei zu sein.{w} Mit jedem Tag vergeht ihre Macht."
    
    p "Was redest du da?{w} Wer wird frei sein?!"

    $ yuzuface='joking'
    $ yuzupose='school_2'
    show Yuzuki
    with dissolve

    y "Oh, also haben sie es dir nicht gesagt?{w} Interessant.{w} Ich frage mich, warum sie so sehr darauf bedacht sind, es geheim zu halten?"

    y "Egal, alles wird morgen Sinn machen.{w} Ich werde endlich bekommen, was ich will, und sie wird endlich bekommen, was sie will. "

    "Yuzuki drifts past me as I struggle to keep upright, the headache refusing to die down."

    y "Auf Wiedersehen für jetzt.{w} Das nächste Mal treffen wir uns als Letztes."

    hide Yuzuki
    with dissolve
    stop music fadeout 6.0
    p "W-Warte, Yuzuki, was hast du--"

    "It's too late.{w} She's gone."

    "I'm left alone on the rooftop, in the pouring rain."

    "I wanted to try to get to the bottom of things...{w}but if anything, I think I'm even more confused now."

    with hpunch

    p "Ha-tschi!"

    "...Okay, I should get back inside now."

    scene bg black
    with fade

    with Pause(2.5)

    scene classroom
    with fade
    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"
    "Soaked to the bone, I squelch into the classroom.{w} I didn't see Yuzuki on the way down, and she doesn't appear to be here, either...{w}so I have no idea where she might have vanished to."

    "So I've lost her, and now I'm probably going to succumb to pneumonia.{w} Great."

    $ sayaface='shocked'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Wahh!{w} Kenta!{w} What on earth happened?!"

    "Oh.{w} I guess Sayaka came to check up on me since I was taking too long to get to the cafeteria.{w} I turn to meet her with a faint smile, my hair dripping wet."

    p "Ich, äh ..."

    "If I tell her Yuzuki is here, or that I went to confront her on my own, she might worry needlessly, so I'll keep it a secret for now."

    p "Alles in Ordnung, mach dir keine Sorgen."

    s "Nothing?!{w} Kenta, you're completely drenched!{w} What were you doing?"

    p "Ich war eigentlich schon draußen, um was zu holen, hab aber vor lauter Eile meinen Regenschirm vergessen.{w} Aber mir wird schon nichts passieren!"

    p "Ah ...{w} Hatschi!"

    "Okay, the sneeze isn't really doing me any favours."

    $ sayaface='smiling'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Come on, let's go get you all dried off.{w} You're going to catch a cold at this rate.{w} And Hikari will flip if you she sees you like this!"

    "Ah, true...{w} I'm lucky it was Sayaka that found me first."

    "I offer no resistance as Sayaka takes me by the wrist and guides me out of the classroom.{w} She doesn't question me any further on the subject either, of which I'm thankful for."

    scene bg black
    with fade

    "Almost dying in the rain aside, the rest of the school day goes by without much more happening."

    "I catch no further sign of Yuzuki, though my headache lingers."

    "I try to piece together everything Yuzuki had said."

    "From what I can understand, she's doing this all because...{w}she wants friends?"

    "It doesn't make sense.{w} How did she end up the way she is to begin with?{w} And who is this 'she' Yuzuki kept referring to?"

    "Someone that is somehow linked to my headaches, and by extension I can only assume she's the cause of the monsters, and everything else that has been going weird lately in my life."

    "Yuzuki also implied that Sayaka and Hikari know more than they're letting on.{w} Which I could tell already, but not to this extent."

    "I want to question them about all this.{w} But I'm sure I'll be met with the same silence."

    "Argh!{w} Why is everyone so damn secretive?!{w} I feel like I'm the only person in the world left out of the loop right now."

    "I keep to my thoughts on the wet journey home, and before long I find myself in my room gazing listlessly at the ceiling."

    scene bedroom night
    with fade

    "The rain gradually dies down as the evening settles in.{w} Things are finally calm.{w} But for how long?"

    "Yuzuki's words are still repeating in my muddled mind.{w} Something is going to happen tomorrow.{w} Something bad.{w} And I have no idea what."

    "I glimpse out of my window.{w} The usual tent is there, albeit a little more wet than usual.{w} I feel sorry for them having to camp out there in this sort of weather..."

    "Those two girls...{w} They've got to know everything that I'm struggling to understand here."

    "It's not fair that even though this entire situation supposedly revolves around me, I somehow know the least."

    "I don't know if they're doing it to protect me or what, but I'm beginning to feel like it's too late for that."

    "I continue to stare at the tent.{w} It's not that late...{w} So they might still be awake."

    "..."

    "Okay.{w} Yeah.{w} I've decided.{w} I'm going to go down there and demand they explain everything to me.{w} I have to make a stand, and be assertive.{w} No more secrets.{w} No more games!"

    "I'll refuse to leave them alone until they tell me all I need to know.{w} I'll leave them no choice!"

    scene bg black
    with fade

    "Steeling myself, I slip on my shoes and sneak out into the garden.{w} Yup.{w} This is happening.{w} I'm finally going to learn everything!"

    "I approach the tent, its entrance securely zipped.{w} But that won't stop me.{w} I know how these things work!"

    "I grab hold of the zip.{w} No hesitating here.{w} I'll give them no time to stop me."

    "And then, in one swift motion, I unzip the tent's door."

    p "Okay, von nun an keine Geheimnisse mehr!{w} Ich will Antworten hören, und zwar ...{w} äh ...?"

    scene cg10
    with wake
    play music "bgm/mischiefintro.ogg" fadein 2.0
    queue music "bgm/mischiefloop.ogg"

    s "Kyahh!{w} Kenta?"

    h "W-Was zur Hölle denkst du was du da tust?!"

    "Oh no.{w} I may have made a mistake here.{w} Apparently past experiences have taught me nothing.{w} My jaw drops, and I find myself unable to put together any form of reply at the sight before me."

    "Upon opening the tent, I'm greeted by the pair of them undressing in a space that looks far bigger on the inside than it does from outside."

    "A dizzying fragrance drifts forth from the tent and stirs my senses, rendering me more dazed than I already was before."

    "My eyes are torn between the pair, unsure of where to settle as they flit between them.{w} They're both so, uh...{w}pleasing to the eyes."

    "While both of them are clearly embarrassed, Sayaka only seems surprised about the whole ordeal.{w} But...{w}I can see Hikari practically shaking with what I can only assume is rage."

    "This...{w}this isn't fair.{w} How was I supposed to know?!{w} They do this stuff on purpose, I swear!"

    h "Kenta!"

    "Hikari barks, scrambling for something within their oddly spacious tent to cover herself with."

    p "G-Genau, entschuldige, das war ..."

    "The right thing to do here would be to zip the tent back up and to wait for them to get dressed, but all I can do is gawk, possibly making the situation much worse than it should be."

    "Curse my natural instincts!{w} I can't help but look, it's what I'm programmed to do!"

    h "'Einfach' was?!{w} Ein Perverser sein?!{w} Ich kann das nämlich deutlich sehen!"

    "Oh god, I hope none of the neighbours can hear this."

    p "Das habt ihr komplett falsch verstanden. Ich wollte lediglich--"

    "She cuts me off.{w} Naturally.{w} Of course I was never going to be allowed to explain myself.{w} That's just not how it works with these girls."

    h "K-Keine Entschuldigungen mehr!{w} Ich habe dich letztes Mal in Ruhe gelassen, aber diesmal..."

    "With a blanket covering most of her bare body, Hikari marches towards me with a scary expression, all the while Sayaka stands by."

    s "Maybe we should hear him out?{w} I'm sure he wouldn't just barge in here without a good reason!"

    h "Oh, er hatte einen guten Grund? In Ordnung.{w} Ein perversen Grund!"

    p "Nein, Hikari, hör ihr zu, ich hab wirklich einen Grund, und zwar einen guten--"

    "She cracks her fist."

    p "H-Hab doch Erbarmen mit mir!"

    scene bg black
    with flash

    stop music 

    "Her fist flies, and I soon see stars as I'm left flat on my back and gazing skywards within my garden."

    "I'm left sprawled out for a good moment before Sayaka and Hikari approach me, now fully dressed.{w} Why does everything have to be so difficult...?"

    scene bedroom night
    $ sayaface='smiling'
    $ sayapose='school_1'
    $ hikaface='normal'
    $ hikapose='school_1'
    show Sayaka at left
    show Hikari at right
    with fade

    "After explaining how I met Yuzuki the other day, and what she had told me, it seems I've finally convinced them to explain things."

    "I led them to my room so we could more comfortably explain things.{w} The tent was an option...{w}but I have bad memories of that place now."

    "Sayaka plops down onto my bed and excitedly looks about the room, while Hikari stands by the door, still angry about before.{w} I said I was sorry!"

    s "So this is your room, huh?{w} It's nice to finally be able to see it from the inside after spying on it all this time."

    "...I'll pretend I didn't hear that."

    h "Es ist überraschenderweise ordentlich..."

    p "Okay, also ...{w} Wollt ihr mir endlich erzählen, was hier los ist?"
    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"
    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Hmm, I wonder what sort of things Kenta has saved on his computer..."

    "Sayaka reaches over and prods at my laptop."

    p "L-Leute, konzentriert euch, okay?"

    $ sayaface='smiling'
    show Sayaka

    s "Hmm?{w} Oh, right, yeah!"

    "Thank you..."

    $ sayaface='normal'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    "Sayaka sits up straight and takes on a serious expression.{w} One that I wasn't even sure she was capable of."

    s "We really were gonna to tell you, Kenta.{w} It wasn't something we wanted to keep a secret..."

    s "We just thought we could handle things on our own, before letting you in on it all."

    s "But as you've heard from that Yuzuki person, time really is running short now."

    $ hikaface='angry'
    show Hikari

    h "Was ich dir {i}immernoch{/i} nicht glauben kann, dass du uns bisher nichts davon erzählt hast.{w} Weißt du in welche Gefahr du dich gebracht hast, als du sie getroffen hat?!"

    "Hikari cuts in, and stomps her way across to join Sayaka, fire in her eyes.{w} ...See, this is why I didn't tell her anything."

    p "Ich weiß, es war dumm ...{w} aber es war der einzige Weg, damit ich was lern. Ihr wart schließlich nicht gerade hilfreich."

    h "Das..."

    $ hikaface='normal'
    $ hikapose='school_2'
    show Hikari
    with dissolve

    "She falls silent.{w} Guess I got her there."

    $ sayaface='joking'
    show Sayaka

    s "He has a good point, Hikari."

    $ hikaface='angry'
    show Hikari

    h "S-Stell dich nicht auf seine Seite!{w} Du sollst {i}mein{/i} Partner sein!"

    p "So, alles, was ich immer hör, ist, dass die Zeit davonläuft ...{w}Aber warum?{w} Was passiert morgen?"

    $ hikaface='normal'
    $ sayaface='normal'
    show Hikari
    show Sayaka

    s "The start of something really bad."

    p "Ach, echt jetzt?!{w} Jetzt hört endlich auf mit diesem mysteriösen Schwachsinn!"

    $ sayaface='scared'
    show Sayaka

    s "Don't yell at me, Kenta.{w} Sheesh.{w} Calm down, I was just getting to that!"

    "I may have lost it a little there...{w} I pull back from her, and quiet down."

    $ sayaface='smiling'
    $ sayapose='school_2'
    show Sayaka
    with dissolve
    play music "bgm/seriousintro.ogg" fadein 2.0
    queue music "bgm/seriousloop.ogg"

    s "Tell me, Kenta, what do you know about your bloodline?{w} Your ancestors?"

    p "Ähh ...{w} Nicht wirklich viel ...{w} Inwiefern ist das überhaupt wichtig?"

    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Dein Blut ist das wichtigste hier!{w} Deshalb beschützen wir dich."

    $ sayaface='scared'
    show Sayaka

    s "Hikari, don't be mean."

    $ sayaface='normal'
    show Sayaka

    s "But...{w}your blood is why we were sent.{w} If it fell into the wrong hands--namely Yuzuki's--we'd all be in a lot of trouble."

    p "Warum {i}mein{/i} Blut ...?{w} Was ist daran so besonders?"

    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "It might be a little hard to believe, but you're...{w}well, you're the descendant of a long running line of mages--people with magical abilities."

    p "...Wie bitte?"

    "Where on earth did they did that dig that up from?{w} I think if they came to me with that on the first day we met, I would have labelled them as crazy...{w}but after all I've seen, it's a bit easier to believe."

    $ hikaface='angry'
    show Hikari

    h "Wie oft muss ich es dir noch sagen?{w} Du{w} hast{w} Magier{w} Blut!"

    "Shouting it into my ear doesn't really help me process it better, you know..."

    $ hikaface='normal'
    show Hikari

    p "Und warum wolltet ihr mir das nie sagen?{w} Es hört sich schließlich verdammt wichtig an ..."

    $ sayaface='smiling'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Well, the world in general doesn't really know about the existence of magic anymore.{w} It's sort of just something that got lost in the history books as technology slowly began to take over."

    s "So, y'know, most families with magic in their blood at this point don't even know about it.{w} It's just something that lies dormant now."

    p "Okay.{w} Wenn also viele Leute dieses ...{w} Magierblut in sich tragen, warum ist meines dann so besonders?{w} ... Was macht es so wertvoll?"

    $ sayapose='school_1'
    $ sayaface='happy'
    show Sayaka
    with dissolve

    s "I'm glad you asked!"

    "Sayaka hops to her feet from the bed, taking me by surprise.{w} This girl can't sit still for more than a minute, I swear!"

    $ sayaface='smiling'
    show Sayaka

    s "I won't bore you with all the details, so here's the story in short."

    "She clears her throat, as if this were a school presentation she had been been practicing for."

    s "Hundreds of years ago, back when magic was still prevalent in the world, there existed a mage with tremendous power."

    s "So much power in fact, that she was pretty much {i}the{/i} mage at the time.{w} Everyone looked up to her, and she was an inspiration to all."

    s "But, you know what happens to people with all the power in the world, right?"

    $ sayaface='normal'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    "She frowns, and lets out a sigh."

    s "They always want more power."

    s "It changes people.{w} Corrupts them."

    s "So, she soon wanted dominion over everything.{w} Over every{i}one{/i}, even."

    s "All the respect that people once had for her turned to fear.{w} And she became a blight on the land."

    s "Everywhere she went, darkness followed, and spread across the land as she went about her conquest."

    "This is getting pretty lengthy...{w} And why do I feel like I know this person she's talking about...?"

    $ sayaface='smiling'
    show Sayaka

    s "Are you still with me, Kenta?"

    "She leans forward and raises an eyebrow as I let out a yawn."

    p "H-Häh?{w} Ja, total!{w} Glaub ich zumindest ..."

    p "Und was hat diese Person mit mir zu tun?"

    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "I'm getting there, gosh!"

    $ hikaface='joking'
    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "Im Grunde bist du mit der Person verwandt, die den Mut hat, sich gegen die dunkle Königin zu stellen und sich an ihre Stelle setzt."

    $ sayaface='shocked'
    show Sayaka

    s "H-Hikari!{w} Why did you have to spoil things?!"

    $ hikaface='angry'
    show Hikari

    h "Wenn du die ganze Geschichte erzählst, werden wir hier noch bis zum Sonnenaufgang sitzen!{w} Und Zeit ist hier essentiell."

    $ sayaface='normal'
    show Sayaka

    s "Aww...{w} I was really getting into it there and everything."

    p "Äh, danke, Hikari."

    $ hikaface='normal'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Hmph."

    p "Und...{w}Weiter?{w} Mein Vorfahre hat diese böse Königin getötet?"

    h "Wenn er es getan hätte, würden wir nicht hier sein und ein Gespräch führen."

    h "Nein, mit all der Macht die sie hatte, war es unmöglich sie zu töten.{w} Ich würde nicht so weit gehen zu sagen, dass sie unsterblich war ... {w} aber ich bin mir sicher, dass es ziemlich nah dran ist."

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "The best he could do was seal her.{w} Using the most powerful sealing magic he could muster.{w} Which leads us back to that magical ol' blood pumping around inside you, Kenta."

    s "Essentially, he tied his fate with hers when locking her away.{w} A seal so powerful that it will only unlock when one strict condition is met!"

    p "Und ...{w} wie lautet die?"

    $ hikaface='angry'
    show Hikari

    h "Ich denke dass soltest du jetzt schon wissen!"

    p "Lass mich raten ... Es hat etwas ...{w} mit meinem Blut zu tun, stimmt's?"

    $ hikaface='normal'
    $ sayaface='smiling'
    show Hikari
    show Sayaka

    s "Bingo!{w} Her seal will only truly unlock if it comes into contact with the blood of the one who sealed her away, or by extension, any of his descendants."

    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Well, actually, not just {i}any{/i} descendant.{w} It has to be one who has latent magical power residing within them."

    p "Das heißt dann also ..."

    s "It means your dad is safe, and that the shadows have no interest in him.{w} He does have {i}some{/i} magic in his blood, but it's not really enough to realise any abilities."

    "Huh...{w} That's pretty convenient."

    $ sayaface='normal'
    show Sayaka

    "Sayaka stretches and lets out a tiny yawn.{w} It must have been exhausting for her to focus on one subject for so long.{w} But I think things are finally starting to make sense..."

    $ sayaface='smiling'
    show Sayaka

    s "So, are you following so far?"

    p "Ja.{w} Glaub schon.{w} Um es kurz zusammenzufassen ... Mein Blut ist der Schlüssel dafür, etwas Schreckliches in Bewegung zu setzen?"

    $ sayaface='happy'
    show Sayaka

    s "Pretty much!"

    p "Aber wenn es mit meinem Blut in Verbindung steht ...{w} Warum läuft uns dann die Zeit davon?"

    $ sayaface='smiling'
    $ hikapose='school_2'
    show Hikari with dissolve
    show Sayaka

    h "Das Siegel wird glücklicherweise nie brechen, wenn dein Blut nicht vergossen wird ... {w}, aber es ist schon lange her, seit sie eingesperrt wurde."

    h "Das bedeutet, dass das Siegel mit jedem Tag in seiner Wirksamkeit schwächer wird, und ihr Einfluss schleicht sich so langsam in die Welt ein."

    s "Kenta, your headaches..."

    p "Verstehe ...{w} Sie ruft also schon nach mir ...{w} um es metaphorisch auszudrücken?"

    h "Deshalb sind die Monster so gut organisiert.{w} Und warum dieses Mädchen, Yuzuki..."

    h "Sie gab diesem Mädchen die Kraft, die sie aufbringen konnte, und benutzte sie als Marionette, bis sie sich schließlich selbst befreien konnte."

    $ hikaface='angry'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Ich bin mir nicht sicher, welche Lügen sie diesem Mädchen gesagt haben muss, um sie dazu zu bringen, zu gehorchen, aber ihre Gedanken sind infiziert."

    h "Und angesichts der gegenwärtigen Rate, dass ihre Niedertracht aus ihrem Gefängnis gesickert ist ... wird sie morgen noch mehr Einfluss auf die Welt bekommen."

    h "Die Monster werden stärker und aggressiver werden...{w} Yuzuki wird auch stärker werden."

    $ sayaface='normal'
    show Sayaka

    s "Basically, our job will become even more difficult than it already is."

    p "Das ...{w} Das ist nicht gut, oder?"

    s "Very!"

    $ sayaface='smiling'
    $ hikaface='normal'
    show Sayaka
    show Hikari

    s "Which brings us to our next order of business."

    s "When we were first assigned to watch over you, all we had to do was take care of a stray shadow or two if they suddenly decided to act on instinct."

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "And that was easy enough.{w} You had no idea those things even existed, and we were able to keep hidden and watch from afar."

    s "But then, things started to go wrong...{w}when you saw that shadow...{w} it really took both Hikari and I by surprise!"

    s "It was like it was on a mission, and completely slipped past our super vigilant watch."

    h "Wenn ich mich zurückerinnere, war das nicht der Tag wo du auf das Sandwich bestanden hast--"

    $ sayaface='happy'
    show Sayaka

    s "Nope!{w} We were ever vigilant!"

    "Hmm...{w} I guess I was even luckier than I thought that they had managed to save me back then."

    $ sayapose='school_1'
    $ sayaface='smiling'
    show Sayaka
    with dissolve

    s "So, anyway, once we were forced to show ourselves to you, it was clear that something wasn't right.{w} At all."

    s "And that was only even more obvious when Yuzuki assaulted us.{w} Wielding a power unlike anything we'd seen before!"

    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "Wir haben nachgesehen als Freizeit war...{w} Das ist selten, wenn es darum geht, auf dich aufpassen zu müssen."

    "Well excuse me for existing!"

    h "Und es wurde schnell klar, dass sich die Dinge nicht lösen würden, wenn wir erst einmal erfahren hätten, dass dieses Siegel an Ort und Stelle langsam geschwächt ist."

    $ sayaface='normal'
    show Sayaka

    s "We need to reinforce her prison.{w} Strengthen it, so that her influence can't affect the outside world anymore."

    s "Only, if it were that easy...{w} We could have done it ourselves without bothering you."

    "Sayaka pulls a complicated expression...{w} I don't think I'm going to like what she has to say next."

    s "Kenta...{w} We...{w}we need your help."

    p "M-Meine?!{w} Wie zum Teufel soll ich helfen?{w} Ihr habt doch die Zauberkräfte, nicht ich!"

    h "Es ist nicht gerade ideal, dass wir uns auf dich verlassen müssen, ich weiß, aber wir haben keine Wahl. {W} Und wir haben keine Zeit mehr, nach alternativen Mitteln zu suchen."

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Basically, since the seal was created by someone in your bloodline and linked directly to them, it can only be strengthened by someone bearing the same blood."

    $ sayaface='scared'
    show Sayaka

    s "I mean, technically, we {i}could{/i} break the seal that's there and trap her in a new one...{w} But I don't think we'd last long enough to do that."



    "So, in other words, I'm really the only solution here.{w} I'm...{w}I'm not sure how to take this."

    p "Ich hab von diesem Magier-Zeugs überhaupt keinen Plan.{w} Bin ich dazu überhaupt in der Lage?"

    $ sayapose='school_1'
    $ sayaface='normal'
    show Sayaka
    with dissolve

    "Sayaka takes a moment to ponder things, a finger held to her chin as her eyes run over me."

    s "Do you remember the night when Hikari was having fun with that tentacle shadow?"

    $ hikaface='embarrassed'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Ich hatte {i}kein{/i} Spaß!"

    p "Kann ich mir vorstellen.{w} Aber was hat das damit zu tun?"

    $ hikaface='normal'
    show Hikari

    s "You used Hikari's sword, didn't you?"

    p "Ja.{w} Aber ich ..."

    h "Kenta, du musst selbst bemerkt haben, wie leicht das Schwert war, trotz seiner Größe, richtig?"

    h "Es ist eine Klinge, die von Magie durchdrungen ist und sich mit dem Träger verbindet, um schnelle und kraftvolle Schläge mit Leichtigkeit auszuführen."

    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "So durchdrungen, dass jemand, der nicht in der Lage war, diese Menge an Magie zu kontrollieren, versuchen würde, sie auszuüben..."

    $ sayaface='smiling'
    show Sayaka

    s "They'd go boom.{w} The magic would be too much for them to handle."

    p "B-BUMM?"

    s "Well, maybe not explode.{w} But at the very least it'd bring about a messy end."

    s "And given that you're still standing after swinging that thing around, it's safe to say you have the potential in you."

    "Yikes...{w} I can't believe there was the possibility of...{w}exploding from picking up her sword.{w} What I did back then was even more reckless than I realised!"

    $ sayaface='happy'
    show Sayaka

    s "So, if you can handle that sword, I think a little sealing magic should be no problem!"

    h "Aber dann, bedeutet es auch, dass wir dorthin gehen müssen wo sie versiegelt ist...{w} und die eine Sache mitnehmen die sie seit Jahren beghert."

    $ sayaface='normal'
    show Sayaka

    h "Es würde leichtsinnig sein.{w} Und ein Fehler, kann die ganze Welt in Gefahr bringen."

    p "Wir haben also überhaupt keinen Stress, hm?"

    "I try my best to keep things light hearted and force out an awkward laugh, but it's difficult after hearing all of this.{w} To think that somehow I'm both the key to unlocking this woman from her prison, and the only thing that can put her away for good."

    h "Morgen ist unsere letzte Chance, das zu stoppen, bevor es außer Kontrolle gerät."

    $ hikaface='joking'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Ich denke du musst ein Tag in der Schule überspringen müssen, Kenta."

    "...Hmm.{w} I wonder if 'out saving the world' is a valid enough excuse to miss a day of school?"

    $ hikaface='normal'
    show Hikari

    h "Das ist es, wenn du uns helfen willst.{w} Ich verstehe es, wenn du dafür nicht bereit bist...{w} Vielleicht können wir einen anderen Weg finden..."

    p "Anderen Weg gibt's wohl keinen, oder?{w} Sonst würdet ihr mir das alles ja nicht erzählen, oder?"

    "I heave out a sigh, and give my guardians a look over.{w} They've done so much for me in this past week.{w} And even more than I realised behind the scenes.{w} If anything, I owe them this."

    "I swallow hard.{w} I can feel my hands begin to tremble.{w} I might die if I go with them."

    "But then, if we leave it, things will only get worse.{w} So..."

    p "Dann hab ich wohl keine andere Wahl.{w} Ich ...{w} Ich werd beim Versiegeln helfen.{w} Wenn ihr so zuversichtlich seid, dass ich es kann."

    $ sayapose='school_2'
    $ sayaface='happy'
    $ hikaface='shocked'
    show Hikari
    show Sayaka with dissolve

    s "You will?!"

    "Sayaka looks ecstatic as she claps her hands together.{w} Was she not expecting me to help?{w} Hikari looks equally surprised.{w} Jeez, a little faith goes a long way, guys!"

    p "Das ist das Mindeste, was ich tun kann, nachdem ihr immer euer Leben für mich riskiert habt.{w} Es ist egal, wie ich euch helfen kann, Hauptsache ich kann helfen!"

    h "Kenta..."

    $ sayaface='joking'
    show Sayaka

    s "You know, you almost sounded cool there.{w} Almost!{w} I think we need to work on your heroic dialogue."

    $ hikaface='normal'
    $ sayaface='normal'
    show Hikari
    show Sayaka

    s "But that'll have to come later.{w} We have lots to cover if you're going to seal away this dark queen, so pay attention!"
    stop music fadeout 6.0
    "And just when I thought the night couldn't get any longer, yet another lecture begins."

    scene bg black
    with fade

    "I'm sure it wasn't easy for the pair of them to teach someone like me the basics of magic--someone who only just barely was aware of its existence at all."

    "I'm not even sure if I've got the steps down...{w}but after hours of practicing, they've assured me I've got it down."

    "I won't be able to tell for sure until the real thing.{w} That's what scares me.{w} What if they've misjudged what I'm really capable of?{w} Or I mess up?{w} Or...{w}there's a whole range of possibilities of things messing up on the day."

    "These are the thoughts that stay with me, long after the girls return to their tent to catch whatever rest they can get before the morning."

    "The last thoughts I have before I finally drift off to sleep is that the toughest day of my life is now lying ahead of me."

    with Pause(3.5)
    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"
    scene bedroom day
    with wake

    "I slowly come to my senses.{w} Morning has arrived."

    "There's no time to waste!{w} I slip out of the covers and steel myself for what's to come, feeling more awake than I ever have in previous mornings.{w} Which is surprising, seeing as I probably got at best a few hours of sleep."

    "I guess the fear of what's to come if I mess this up is what's keeping me going.{w} A better motivation than any other!"

    p "Okay, dann an die Arbeit!"

    "I peer at a pair of determined eyes that stare back at me from the mirror.{w} This is the most focused I've ever been in my life."

    "It's funny how much has changed in these past few days.{w} And it's even more weird how I seem to accept it.{w} As if, deep down, I knew all of this to begin with."

    "I slip on my casual clothes and make for the dining room."

    scene kitchen day
    $ sayaface='smiling'
    $ sayapose='magical_1'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "I find the two girls waiting for me, as expected.{w} Though, I'm caught a little off-guard by the fact that they're in their battle outfits."

    s "G'morning.{w} Did you sleep well?"

    p "Wenn ich daran denke, was mich erwartet ... Ja."

    $ hikapose='magical_2'
    show Hikari
    with dissolve

    h "Achte darauf, gut zu essen bevor wir gehen.{w} Du wirst die Kraft brauchen."

    "Right, right.{w} Of course.{w} I start for the kitchen and prepare the most simple food I can think of."

    p "Was ich gestern ganz vergessen hab zu fragen ...{w} Aber wo ist diese 'Königin' überhaupt gefangen?"

    $ sayaface='normal'
    show Sayaka

    s "Huh?{w} Didn't we say?{w} She's sealed just outside this town."

    p "Was?!"

    "I almost drop the plate I'm holding."

    p "So nah?!"

    $ hikaface='angry'
    show Hikari

    h "Natürlich.{w} Warum sonst denkst du, dass sich ihr Einfluss hier so leicht ausbreitet??"

    p "Ich ...{w} Damit hab ich jetzt echt nicht gerechnet.{w} Aber wenn man so sieht, ist es irgendwie logisch ..."

    $ hikaface='normal'
    show Hikari

    "But to think she's been this close the whole time.{w} No wonder things have been getting progressively more crazy around here..."

    "She must be furious...{w} to have the key to her freedom just out of grasp like this."

    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "To be fair, while we knew she was at least in the area, we didn't pinpoint her exact location until last night."

    s "Apparently she's in a forest on the outskirts of town, holed up in some cave out of sight.{w} There's a lot of history around this place, I suppose."

    s "Maybe the forest used to be part of something greater.{w} Her old base of operations, perhaps?"

    $ hikapose='magical_1'
    show Hikari
    with dissolve

    h "Nichts davon ist wichtig.{w} Wir müssen einfach nur da reinkommen, das Siegel stärken, und dann sollte unser Leben {i}viel{/i} einfacher sein."

    p "Und wird sich das alles wirklich einfach so von selbst in Ordnung bringen, wenn wir Magie verwenden?"

    h "Naja, es wird die Macht, die sie hat, ausschalten .{w} Das heißt, die Monster werden zu ihren geistlosen Hülsen zurückkehren, und die Dinge sollten sich hier unten beruhigen."

    $ hikaface='angry'
    show Hikari

    h "Und nachdem können wir endlich heimgehen, nachdem alles sortiert ist.{w} Ich schwöre, ich werde verrückt wenn ich noch ein Tag mehr an dieser Schule verbringen muss."

    $ sayaface='joking'
    show Sayaka

    s "Aww, don't act like you're so desperate to leave.{w} I know for a fact you've had fun spending time with Kenta."

    $ hikaface='embarrassed'
    show Hikari

    h "S-Sei nicht lächerlich!{w} Ich mach nur mein Job..."

    $ sayapose='magical_1'
    $ sayaface='happy'
    show Sayaka
    with dissolve

    s "You can't fool me.{w} Not when your face is such an adorable shade of red!"

    h "H-hmph.{w} Werden wir jetzt gehen oder was?!"

    "Sayaka giggles and jabs at her partner's ribs.{w} I suppose it's good they can stay in such high spirits despite the task that lays before us...?"

    scene bg black
    with fade
    stop music fadeout 3.0
    "We set out.{w} I let the girls lead the way as we take the lesser-travelled routes through town so as to not draw attention to their outfits."

    "They offered to fly me there, as it would be much faster.{w} But...{w}hah.{w} No.{w} Walking is fine.{w} I'm sure things aren't {i}that{/i} urgent."

    "Before long, our surroundings become less urban, the buildings shrinking in number the longer we travel, until finally we cross over a fence and into the wilderness."

    scene forest trail
    with fade

    "Branches overhead shade us from the sun as we walk across the faint trail laid out across the ground.{w} Only the faintest hints of light that filter through illuminate the way."

    "..."
    play music "bgm/magicalgirlintro.ogg" fadein 5.0
    queue music "bgm/magicalgirlloop.ogg"
    "I'm beginning to wonder if the girls even know the way, as we pass by a tree I swear I've seen at least three times before."

    $ sayaface='smiling'
    $ sayapose='magical_1'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka at left
    show Hikari at right
    with dissolve

    s "Hmmm.{w} Maybe we should have brought a map?"

    "Well.{w} That just confirms it.{w} We're hopelessly lost!"

    "Any tension that might have existed before is sucked away the moment Sayaka begins to scratch her head and glance around the place."

    $ hikaface='angry'
    show Hikari

    h "Wirklich?{w} Uns wurde die Wegbeschreibung vorher klar gesagt.{w} Wie kannst du sie einfach vergessen?!"

    $ sayaface='happy'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Okay, you lead the way, then."

    $ hikaface='scared'
    $ hikapose='magical_2'
    show Hikari
    with dissolve

    h "Ich...{w} Bah, fein.{w} Ich hab es auch vergessen!"

    $ sayaface='joking'
    show Sayaka

    s "See!{w} Nobody is perfect, even if you'd like to think you are sometimes."

    $ hikaface='angry'
    show Hikari

    h "Ich denke nicht, dass ich perfekt bin!{w} Im Vergleich zu dir, aber--"

    p "Äh, Leute?{w} Muss das jetzt sein?"

    h "Aber sie...{w} Fein.{w} Du hast recht.{w} Konzentrieren wir uns, Sayaka."

    $ sayaface='smiling'
    $ sayapose='magical_1'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka
    show Hikari
    with dissolve

    "And here I thought the sealing part of this operation would be the most difficult part...{w} Sheesh."

    s "Okay, the forest isn't that big.{w} I think.{w} If we stumble around some more, we're bound to find the cave!"

    "Hasn't stumbling around randomly only made us go around in circles?{w} I fear the sun might set before we ever find this darn cave now!"

    "I know it won't help, but I join the pair in surveying the land.{w} I don't even know what I'm supposed to be looking out for, apart from..."

    p "Eine Höhle ...?"

    s "Hm?{w} Something up?"

    "I squint at something in the distance.{w} A cluster of boulders that had caught my attention.{w} My eyes were practically drawn there like some kind of magnetic force was at work."

    "I've never been here before...{w}yet somehow it seems familiar."

    p "Können wir da kurz nachsehen?"

    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Sure!{w} We don't have any better leads right now, anyway.{w} Eh-heh-heh..."

    with Pause(2.5)

    "We trek over to the oddly suspicious rock formation.{w} I wonder, could this really be it?"

    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "Hmm, hmm.{w} What made you want to look over here?"

    "Sayaka begins to poke about the boulders, a hand to her chin."

    "Circling around the cluster reveals nothing too out of the ordinary, but...{w}there has to be more."

    p "Weiß nicht.{w} Mir ist vorgekommen, als hätt ich was gespürt."

    $ hikaface='angry'
    show Hikari

    h "Das sind einfach nur ein paar dumme Steine.{w} Wir verschwenden Zeit!"

    s "Aww.{w} We should at least investigate them a bit more if Kenta says there's something up.{w} He's connected to the dark queen, remember?{w} He's bound to know at least a few things relating to her, even if it's only on a sub-conscious level."

    "She says that as she raps gently at one of the rocks with her knuckle, one eye closed to better examine it."

    $ hikaface='normal'
    $ sayaface='happy'
    show Sayaka
    show Hikari

    s "Oh!{w} This one seems kinda loose."

    "Sayaka takes a grip of the rock in question and begins to pull at it with all her might, her teeth gritting in determination."

    $ sayaface='scared'
    show Sayaka

    s "Hrghh!{w} S-some help would be much appreciated!"

    "Oh, right.{w} Yeah.{w} I should probably help!{w} It was almost amusing to see her feet wildly kicking in place with the rock refusing to budge."

    $ sayaface='normal'
    show Sayaka
    with hpunch

    "I take up the other side of the rock, and begin to push against it with what little strength I might possess."

    "..."

    "We still don't manage to move the rock.{w} It doesn't budge.{w} At all.{w} Even with all our combined effort.{w} And I really am trying here!"

    "It certainly does feel loose, though.{w} Apparently not loose enough!"

    "I think we could move it for sure if one last person were to..."

    $ hikaface='angry'
    show Hikari

    h "Oh, für's Laute rumschreien!{w} So werden wir nirgendwo hinkommen.{w} Bleib zurück!"

    $ hikapose='magical_2'
    show Hikari
    with dissolve

    "Her sword appears in a flash.{w} Hey, wait, we're still right beside it, isn't it dangerous to just--"

    "She strikes out without any further warning, unleashing a single, precise slash that splits the rock clean in two."

    $ sayaface='shocked'
    show Sayaka

    s "Wahh!"

    p "Oof ..."

    $ hikaface='normal'
    show Hikari

    "We both fell backwards as the two pieces of the rock collapse opposite ways.{w} ...I feel like my hair might be just a little shorter than it was, too, after how close that was."

    $ sayaface='angry'
    show Sayaka

    s "H-Hikari!"

    $ hikaface='joking'
    show Hikari

    h "Siehst du?{w} Problem gelöst."

    s "That's..."

    $ sayaface='normal'
    show Sayaka

    "She falls silent, unable to argue there.{w} It {i}did{/i} move the rock after all."

    $ hikaface='normal'
    $ hikapose='magical_1'
    show Hikari
    with dissolve

    "We both hop to our feet to join Hikari in peering over the results of her destruction as the dust begins to settle."

    "I almost forget how to breathe in the excitement of it all.{w} ...Could this really be it...?"

    "...!"

    $ sayaface='shocked'
    $ hikaface='shocked'
    show Sayaka
    show Hikari

    "We all gasp at once.{w} I knew it!{w} I'm not sure how, but somehow I knew it!"

    "Behind where the rock lay is a tunnel that trails downwards, deep into the darkness."

    "There's no telling how far it might stretch, or if there's anything on the other end."

    "But, if someone went to such lengths to hide this tunnel from existence, then it has to lead {i}somewhere{/i}, right?"

    $ hikaface='normal'
    show Hikari

    h "Ist es...{w}das wirklich?"

    $ sayaface='smiling'
    show Sayaka

    s "Sure feels like it!{w} You can practically {i}see{/i} all that darkness and evil flooding out of it."

    "That's not really something you should be saying so happily..."

    "She is right, though.{w} There's a foreboding sense of despair as I peer deep into the hole.{w} A heavy tension in the air, as if the sheer presence of whatever lurks down there seeks to consume us all."

    "Once we go down there...{w} This will be it.{w} We'll finally put an end to this madness, and I might finally be able to get some peace after all of this is done."

    "...Do I really have the strength to go through with this?{w} To reseal a long forgotten evil that tormented--"

    $ sayaface='happy'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Welp.{w} Time's a wastin'!{w} In we go!"

    p "H-Hey, warte!"

    hide Sayaka
    show Hikari at center
    with dissolve

    "Sayaka apparently doesn't have the decency to wait for me to battle out my internal struggles, and cuts things short as she plops down onto her knees and begins to shuffle into the hole, its size just about big for us to fit if we crawl."

    h "Sie hat recht.{w} Wir können nicht noch mehr Zeit verschwenden.{w} Los geht's, Kenta!"

    hide Hikari
    with dissolve

    "Hikari follows after Sayaka, looking somewhat more hesitant towards the whole thing compared to her partner."

    "They disappear into the darkness completely, as if consumed by the tunnel.{w} It's scary just how little light seems to shine down there."

    "Hmm..."

    h "Hör auf, herumzualbern, oder du wirst zurückbleiben!"

    "Hikari's harsh tones sound out from the tunnel, making it all the more frightening."

    p "Okay, okay!{w} Ich komm ja schon."

    "It's not like the world is going to end just because I take an extra minute or two to prepare for diving into the heart of evil.{w} At least, I hope it isn't."

    "I drop to my knees and shuffle into the tunnel, my world quickly becoming dark as all traces of light begin to fade."

    scene bg black
    with fade

    "I can just about make out the scuffling sounds of the other two crawling along ahead of me.{w} Their presence the one thing keeping me calm during all of this."

    "My surroundings are dark.{w} Cold.{w} Slimy to the touch.{w} So far it hasn't been a very pleasant experience."

    p "Weißt du ..."

    s "Hmm, something up?"

    p "Das hab ich mir echt nicht vorgestellt, als ich daran gedacht hab, wie es wär, ein Held zu sein."

    p "In einem engen, kleinen Tunnel rumkriechen ...{w} Ich hab mir das irgendwie Dramatischer vorgestellt."

    "Sayaka lets out a giggle as she soldiers on ahead."

    s "I'm sure we'll have plenty of dramatic moments ahead!{w} We've just gotta get through the...{i}less{/i}...dramatic moments."

    s "And hey, this isn't so bad.{w} At the very least, we're not having to fight through swarms of shadows to reach her."

    s "It's not the most glamorous way of going about things, but at least we get to save some strength for when it counts..."

    "She brings up a good point.{w} However..."

    p "Aber was, wenn ...{w} {i}in{/i} diesem Tunnel Monster auf uns warten?{w} Falls das der Fall ist, können wir nicht wirklich viel tun."

    h "S-Sag das nicht!{w} Ich hab nichtmal über soetwas nachgedacht..."

    s "Oh, wow, you're right.{w} We'd be completely defenseless!"

    h "Sayaka!"

    s "They would completely massacre us.{w} Since I can't use my bow here, and Hikari certainly wouldn't be able to use her sword."

    s "I wonder what kind of shadows would be able to fit through this tunnel?{w} Oh!{w} Maybe something with tentacles, since I know they {i}love{/i} you, Hikari!"

    h "Sei ruhig!{w} Jetzt bist du einfach nur böse!"

    "Hmm...{w} Maybe I should have kept my thoughts to myself?{w} Sayaka is having way too much fun with this."

    s "Or, maybe, how about--"

    h "H-hiyahh!{w} Irgendwas hat mich berührt!"

    "Hikari shrieks, almost bursting my eardrums in the process."

    h "Warst du das, Kenta?!{w} Ich wusste, ich hätte als Letzt einsteigen sollen..."

    p "Ich?!{w} Natürlich nicht!{w} Ich bin ja ganz woanders!{w} Wofür hältst du mich eigentlich?"

    h "...Willst du wirklich, dass ich das beantworte, nach dem, was du in den letzten Tagen getan hast??"

    p "D-Das waren Unfälle! UNFÄLLE!"

    h "Naja, vielleicht war das wieder einer deiner "Unfälle", hmm?{w} Ein Mädchen greifen whärend sie komplett hilflos ist?"

    p "Komm schon, ich bin ja nicht mal in deiner Nähe!{w} ... Vielleicht bildest du dir das auch einfach nur ein?"

    "I can just about hear Sayaka stifle a giggle as we continue to argue.{w} Hmmm."

    play music "bgm/mischiefintro.ogg" fadein 2.0
    queue music "bgm/mischiefloop.ogg"

    h "F-Fein.{w} Wenn du es nicht warst, wer dann?{w} Es hätte nicht Sayaka sein, da sie vor mir ist."

    s "Maybe it was a big, slimy tentacle coming to say hello."

    "She says it in an almost sing-song manner.{w} Okay, yeah, I see what's happening now.{w} I'm hoping Hikari will realise soon, too."

    h "E-ES hätte aber nicht--kyahh!{w} There it is again!"

    h "Okay, ernsthaft was ist--a-ah!"

    "This bizarre series of events continues for longer than I feel is necessary, until finally I feel I have to speak up, or we might be stuck in this tunnel all day."

    p "Okay, komm, Sayaka, das reicht jetzt.{w} Du hattest deinen Spaß.{w} Jetzt müssen wir uns aber wieder konzentrieren, okay?"

    h "W-Was...?{w} Sayaka?{w} Aber sie hätte nicht..."

   "Confirming my suspicions, Sayaka lets out another one But, she couldn't possibl of her devious laughs."

    s "Aww, okay, okay.{w} I couldn't resist.{w} She's just too easy to mess with!"



    h "..."

    "Hikari takes in a deep breath.{w} ...Uh-oh."

    h "Ich werde dich umbringen, Sayaka!"

    s "You'll have to catch me, first!"

    "I hear the pair of them shuffle ahead at an accelerated pace, Sayaka's manic laughter trailing into the distance."

    "I suppose it's good they can keep in such high spirits despite the task that lies ahead of us."

    "...I really don't appreciate them just leaving me behind like this, however."

    "I contemplate continuing on at my own pace, sure that I'll catch up to them eventually, but I feel something slimy lap at my hand, forcing me to break into some sort of bizarre sprint-crawl."

    "I don't know if there really are things lurking around in this tunnel, but I certainly don't want to stick around to find out."

    with Pause(3.0)

    "I eventually manage to catch up to them, the pair seeming to have calmed down somewhat."

    "I'm not sure just how long we've been trekking through this tunnel now, but it feels like it's been an eternity."

    "There wasn't even any guarantee that this would lead us to where we wanted to go, and we went with blind faith, going off of my instinct alone."

    "So if this turns out to be a massive waste of time, it's going to have been my fault."

    "And so far, we haven't found anything to suggest we're on the right path."

    "I feel despair begin to set in."
    stop music fadeout 4.0
    "What if we end up running into a dead end?{w} Or worse, get stuck somehow?"

    "What if..."

    s "Ooh, hey!{w} I think I see something up ahead."

    h "Es ist Zeit!"

    "Sayaka's cheerful voice snaps me out of dark, unnecessary thoughts.{w} I guess I really should trust my own instincts a little more sometimes."

    "True to her word, I can begin to see light seep into the tunnel as we inch ever closer to our goal."

    "Just a little more, and..."
    play music "bgm/seriousintro.ogg" fadein 2.0
    queue music "bgm/seriousloop.ogg"

    scene cave
    with fade

    "I drag myself out into a much larger opening, Sayaka and Hikari already on their feet as they take the time to stretch."

    $ sayaface='smiling'
    $ sayapose='magical_1'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka at left
    show Hikari at right
    with dissolve

    s "Whew!{w} That was quite a journey.{w} How's everybody holding up?"

    $ hikaface='angry'
    show Hikari

    h "Ich bin okay.{w} Es wäre besser gewesen wenn nicht {i}jemand{/i} mit mir da unten rumgespielt hätte."

    $ sayaface='joking'
    show Sayaka

    s "Eh-heh-heh...{w} I was...{w}trying to keep the mood light?"

    $ sayaface='scared'
    show Sayaka
    with hpunch

    "{i}Bop{/i}.{w} Wrong answer.{w} Hikari raps her partner on the head."

    h "Idiot."

    hide Hikari
    hide Sayaka
    with dissolve


    "Finally up off of the ground, I survey my surroundings."

    "It looks like we've found our way into some kind of large chamber."

    "And, almost instantly, my eyes are drawn to it."

    "Right in the center of the cave.{w} Glimmering in an unnatural light.{w} A crystal."

    p "Das ist ..."

    "I don't even need to be told what it is.{w} I already know."

    "It's her.{w} The one behind all this madness.{w} The supposed 'dark queen'."

    "Even just looking at the crystal is enough to make my head spin and threaten to tear open."

    "I feel like I'm going to be sick.{w} My mind is set aflame with a raging cry.{w} {i}Her{/i} cry."

    "A cry of sheer, burning hatred.{w} There are no words to pick up on, just an incoherent garble of screaming and curses."

    "This is it.{w} We've finally reached her."

    "I can stop this once and for all.{w} After this is over, I can go back to living my carefree life."

    "She's the last obstacle.{w} I can..."

    p "Ich kann es schaffen."

    "I murmur to myself, and tighten my fists in an effort to still the trembling."

    "It's funny how crazy things have turned out these past few days.{w} To think those headaches would have led to all this.{w} All those weird dreams..."

    "I've never dedicated myself to anything before.{w} I've never been one to put in anything more than the minimum amount of effort required of me in life."

    "Yet, here I am, risking my life, and possibly the entire world, for something I'm not even entirely sure I can pull off."

    "I don't know what's gotten into me recently...{w} Those girls really are a bad influence on me.{w} Making me do such crazy things."

    "I heave in an unsteady breath.{w} I can just about keep myself standing in the face of this pure evil."

    "It's okay.{w} I can do this.{w} I just need to keep telling myself that."

    "I can do this...{w} I can...do...this...?"

    "Crap.{w} The doubts are beginning to set in."

    "{i}How{/i} can I do this?!{w} I'm not a mage.{w} I don't know any magic!{w} I'm not even sure if I remembered what they told me correctly..."



    with hpunch

    "Someone sets their hand on my shoulder, rousing me from my thoughts."

    $ sayaface='smiling'
    $ sayapose='magical_1'
    show Sayaka at center
    with dissolve

    s "Kenta?"

    "It's Sayaka.{w} Her face is brimming with the usual optimism I've come to expect from her, even in the face of evil."

    s "Don't worry!{w} We can do this.{w} Together."

    with hpunch

    "A second hand lands on my free shoulder...{w}more awkwardly than the previous."

    $ hikaface='shy'
    show Sayaka at left
    show Hikari at right
    with dissolve

    h "J-Ja.{w} Was sie gesagt hat."

    "It's Hikari, of course.{w} Even behind the tinge of red that paints her face, I can see her limitless determination shine through."

    $ hikaface='normal'
    $ hikapose='magical_2'
    show Hikari
    with dissolve

    h "Du musst dich vor nichts fürchten, solange du an unserer Seite bist."

    p "Ja."

    "I nod, their words calming me."

    p "Du hast recht.{w} Wir haben es schon so weit geschafft.{w} Nur noch ein bisschen, dann ist alles vorbei."

    p "Ich danke euch.{w} Für alles, was ihr für mich getan habt.{w} Ohne euch wär ich jetzt nicht hier.{w} Ich schulde euch was."

    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Hmmm, well, I think we can discuss an appropriate reward once this is all over."

    h "Ein...Preis...?"

    "Hikari falls silent at the prospect.{w} ...Suspiciously so."

    $ sayaface='happy'
    show Sayaka

    s "Gosh, Hikari, what sort of reward did {i}you{/i} have in mind?{w} Your face is going all sorts of interesting colours!"

    $ hikaface='embarrassed'
    $ hikapose='magical_2'
    show Hikari
    with dissolve

    h "Nichts!{w} Absolute nichts!{w} Kenta's Dank ist alles was wir brauchen.{w} W-Wier machen foch nur unseren Job."

    $ sayaface='joking'
    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "Smooth."

    "She jabs at Hikari's side with a teasing look.{w} It's probably better I don't ask."

    $ sayaface='smiling'
    $ hikaface='normal'
    show Sayaka
    show Hikari
    stop music fadeout 6.0
    s "Right, then!{w} Let's get to it!"

    p "Verstanden.{w} I-Ich ...{w} Ich glaub, ich hab mir alles gemerkt."

    s "You'll be fine.{w} But, if on the off-chance, you goof things up, we'll help you through it, okay?"

    "That makes me feel a bit better.{w} But, I have to make sure I get it right on the first try.{w} I can't be a burden.{w} Not now."

    hide Sayaka
    hide Hikari
    with dissolve

    "We carefully make our way to the center of the cave, where my worst nightmares lie."

    "The cave {i}seems{/i} empty...{w} I think it's too good to be true, however.{w} There's no way it could be this easy."

    "Step after step, we edge closer."

    "Sayaka and Hikari keep to my side, weapons at the ready.{w} Who knows what could be lurking behind the rocks in this place."

    "We've pretty much stumbled right into their lair.{w} I'm surprised these 'shadow' things aren't completely swarming us."

    y "Hah, du bist wirklich dümmer als ich dachte!"

    "A familiar voice floats in.{w} Of course.{w} Why {i}wouldn't{/i} she be here?"

    p "Yuzuki!"

    scene cg12
    play music "bgm/evilgirlintro.ogg" fadein 2.0
    queue music "bgm/evilgirlloop.ogg"

    "In a flurry of feathers black as the night, she appears beside the crystal--beside her mistress."

    "She clutches her scythe in an overwhelmingly hostile stance, and gives us a violent scowl.{w} It seems even she realises the severity of this situation."

    y "So bereitwillig sich anzubieten, nachdem ich all die Nächte damit verbracht habe, dich zu jagen.{w} Du hast wirklich einen Todeswunsch."

    y "Aber das ist in Ordnung.{w} Ich gebe dir ein schnelles und schmerzloses Ende."

    h "Du redest nur mit dirselber!{w} Denk nicht, ich kann nicht sehen das du Angst hast.{w} Du weißt, dass das Ende der Linie für dich ist."

    h "Ich weiß nicht, was du von alldem willst, aber was auch für verrückte Fantasien du hast, werden zu einem Ende kommen. {w} Jetzt!"

    "Yuzuki grits her teeth, a bead of sweat creeping across her brow.{w} So she really is scared...?"

    y "Halt den Mund!{w} Du weißt nichts.{w} Ich...{w}Ich brauche das!"

    p "Yuzuki, es muss nicht so enden.{w} Ich weiß, du wirst mir nicht glauben, aber ich weiß, was du durchmachst.{w} Den Schmerz, den du fühlst.{w} Vielleicht können wir--"

    with hpunch

    y "Ich sagte sei ruhig!"

    "The entire cavern quakes under her rage.{w} Debris rains down from above.{w} This is getting dangerous."

    y "Ich brauche deine Hilfe oder dein Mitgefühl nicht.{w} Ich repariere Dinge selbst.{w} Alles wird gut, wenn ich dich wie einen Feuerhydranten aufreiße und dein Blut magisch wirken lasse."

    "My face grows pale as a maddening laugh escapes her lips.{w} How can she say something so twisted?{w} ...I really did try, but maybe her sanity is too far gone?"

    "I can't give up so easily!{w} One more try...{w} Maybe I'll get through to her?"

    p "Ich weiß, dass du kein schlechter Mensch bist, Yuzuki.{w} Du bist nur ...{w} einsam, oder?"

    y "Ich bin nicht allein!{w} Mindestens...{w}Ich werde nie wieder einsam sein, wenn das einmal vorbei ist."

    s "Kenta...{w} I understand you want to help her, but...{w}well, just look at her."

    "Sayaka looks solemnly towards the dark angel."

    "...She's right.{w} I give Yuzuki a proper look over for the first time since we arrived here."

    "Her face is crooked, her expression unhinged.{w} Every once in a while her head gives off a twitch as she clenches the scythe tightly."

    "She seems even worse than she did before.{w} Maybe the darkness has fully eaten away at her?{w} Does the old Yuzuki even exist?"

    "I have to admit it.{w} We can't save her."

    "I let out a heavy sigh."

    p "Okay.{w} Tut, was ihr tun müsst."

    "Sayaka and Hikari nod.{w} They understand that this is going to be a fight with consequences."

    "There's no running away.{w} Each side has too much at stake now."

    y "Ich habe das Gefühl, dass du mich vielleicht unterschätzt.{w} Es ist wahr, ich musste bei unserer letzten Begegnung beschämend den Schwanz drehen, aber ..."

    "Yuzuki grunts, and a dark aura begins to set in around her.{w} This is new..."

    y "Wir kämpfen auf meinem Heimatmarkt.{w} Ich habe hier eine direkte Verbindung zu ihr.{w} Ich kann..{w} Ich kann sie in mir fühlen."

    y "Ich kann jetzt nicht verlieren!{w} Nicht mit {i}ihr{/i} auf meiner Seite!"

    "She lets out another crazed laugh as the cavern gives a violent rumble.{w} I don't think this is all talk...{w} Sayaka and Hikari might really have their work cut out here."

    stop music fadeout 2.0

    y "Nun Dann...{w}stirb!"

    scene cave

    $ yuzuface='angry'
    $ yuzupose='magical_1'
    show Yuzuki at center
    with dissolve

    play music "bgm/dramaticintro.ogg" fadein 2.0
    queue music "bgm/dramaticloop.ogg"

    "Yuzuki closes the distance between us in the blink of an eye, and heaves her scythe up high.{w} I can't tell if she's aiming for me specifically, or hoping to catch us all in a single, crushing blow."

    s "Wahh, look out!"

    hide Yuzuki
    with dissolve

    "Sayaka tugs at my arm and pulls me away, with Hikari jumping to the opposite side."

    with hpunch

    "The ground where I was standing just moments ago is shattered, only a crater and the smouldering of dark magic remaining in the wake of her scythe."

    "Unreal.{w} If Sayaka hadn't reacted in time...{w} I shudder to think."

    show Yuzuki at right
    with moveinright

    "Yuzuki sets her sights on me again, lifting the deadly scythe up for another attack.{w} I wonder if the other girls are even registering in her crazed eyes right now?"

    "I must be the top priority.{w} If she gets me, she wins."

    $ hikaface='angry'
    $ hikapose='magical_1
    show Hikari at left
    with moveinleft
    show Hikari at center
    show Yuzuki at center
    with MoveTransition(0.2)
    with hpunch
    show Hikari at left
    show Yuzuki at right
    with move

    "She attempts to kick off of the ground, but Hikari bursts from the side and catches her off-guard, locking blades with her."

    h "Oh nein, das tust du nicht!{w} Bevor du ihn bekommst, musst du erst an {i}mir{/i} vorbei!"

    y "Das kann sein...{w}vereinbart worden!"

    "The pair grit teeth as they push against one another, the magic practically crackling around them in a fierce storm."

    "Yuzuki must be stronger than ever right now, yet Hikari seems to be able to stand her ground, her feet sinking slightly into the ground as the pressure pushes against her."

    "She must be pushing well past her limits to even be able to stand a chance against this monster.{w} I can already see the strain it must be putting on her body, as sweat takes over her face."

    h "Hrghh...{w} L-Los!{w} Ich hab sie...{w}abgehalten!{w} Ihr Typen...{w}beendet das!"

    "She hisses through gritted teeth, her feet beginning to slip."

    $ sayaface='shocked'
    hide Hikari
    hide Yuzuki
    show Sayaka at center
    with dissolve

    s "Hikari!{w} You can't possibly--"

    hide Sayaka
    show Hikari at right
    with dissolve

    h "Ich sagte los!"

    "Her voice booms and the magic around her violently crackles.{w} I've never seen her like this before..."

    h "Oder willst du, das alles hier für nichts ist?!{w} Ich kann...{w}halte sie für eine Weile in Schach.{w} Kein Problem!"

    "That's..."

    "I give her a worried look, but Sayaka tugs at my arm once more and urges me towards the crystal."

    $ sayaface='normal'
    hide Hikari
    show Sayaka at center
    with dissolve

    s "Come on.{w} She's right.{w} She's tougher than she lets on, and I'm sure she'll be fine!"

    "Even Sayaka doesn't sound so sure of that herself.{w} ...I just have to trust in Hikari, and end this before she slips up."

    "I nod and we hurry ever closer to the center of all this chaos.{w} I can still hear the clash of magic behind me, along with pained cries.{w} I can't look back now, though.{w} She'll be fine."

    "We're almost there.{w} Just a few more steps closer, and--"

    $ sayaface='scared'
    show Sayaka

    s "Oh, you've got to be kidding me..."

    "Sayaka preps her bow and shoots a sharp look towards the rocks scattered around in the distance."

    p "H-Häh?{w} Was meinst du damit?"

    scene cg20
    with dissolve

    "Harsh, guttural growls fill the air, and several of those demonic, almost dog looking shadows I've encountered before make their presence known.{w} ...And several more."

    "They circle us and block off the crystal completely.{w} Great."

    scene cave
    with dissolve

    s "Okay.{w} This is...{w}not a problem!"

    "We end up back to back and we face off against the ever enclosing circle of shadows.{w} Their fangs are bared, and there's nothing but hate for us in those burning eyes of theirs."

    "I should have known things weren't going to be this easy.{w} Of {i}course{/i} she wasn't going to just rely on Yuzuki to defend her!"

    p "Irgendwelche, äh ...{w} Ideen?"

    s "I was going to ask you that!"

    "...I think we {i}know{/i} we're done for when we have to rely on me for ideas."

    p "Ich hoff doch, dass das ein Scherz ist!"

    "The monsters close in.{w} They're acting like an intelligent pack of sorts, ensuring there's no escape for their prey."

    s "Oh!{w} I've got it!{w} Why didn't I think of it sooner?"

    "There's a glimmering light as Sayaka's bow fades out of view, and I feel something begin to form on her back."

    "Ah, the wings!{w} Of course.{w} We can just fly out of this."

    "As much as I hate flying, I'm willing to make an exception this one time."

    s "Hold on tight, Kenta!"

    with hpunch

    "I take a solid grip of both Sayaka's hands, and she kicks off of the ground, right as the shadows around us decide to make their move."

    "It's a close call.{w} I just about feel the snarling heat from one of the savage beasts' growls as we lift into what little vertical space we have in the cave."

    s "That was easy enough!{w} Next stop, the dark queen!"

    "We sail through the air, our goal in sight.{w} Okay, I think we might actually make it this time--"

    with hpunch

    s "Ahh!"

    "Sayaka lets out a pained gasp, and our momentum grinds to a halt.{w} Her grip loosens considerably on one of my hands."

    p "S-Sayaka?"

    s "Ahh, this is no good.{w} One of them must have nicked me on the side before we could get away."

    "She forces out an awkward laugh as we begin to wobble in the air, her grip on my other hand also slipping."

    s "I'm not sure how much longer I'll be able to...{w}keep us up here..."

    "I throw a glance down to see the snapping pack of savage monsters almost right at our heels.{w} Things are looking bleak..."

    s "Hmmm..."

    "Sayaka debates something as we sink ever lower to our demise.{w} No!{w} We were so close!"

    s "Well.{w} I trust you'll be able to set everything right, Kenta.{w} I won't be there to help you, like I said I would...{w}but, I believe in you!"

    "Her voice is pained.{w} Weak.{w} That little 'nick' must hurt more than she's letting on."

    p "Sayaka ...?{w} Was sagst du da ...?"

    s "You can do it.{w} I know you can!"

    p "Was--"

    with hpunch
    stop music fadeout 4.0

    "A burst of energy detonates at my back, almost like a gust of wind.{w} It splits me from Sayaka's hold and sends me hurtling towards the crystal, where {i}she{/i} lies."

    "Sayaka must have known she wouldn't be able to carry me here, so she...{w}boosted me across with magic?{w} But then, what happened to her?"

    with hpunch

    p "Oof!"
    play music "bgm/seriousintro.ogg" fadein 5.0
    queue music "bgm/seriousloop.ogg"
    "I land with a gentle thud at the foot of the crystal.{w} It seems her magic was even set to cushion my fall.{w} Sayaka..."

    "I throw a glance over my shoulder.{w} She isn't in the air anymore.{w} And right below her was..."

    "No!{w} I refuse to believe it.{w} She'll be fine.{w} I just need to end this.{w} Now!"

    "I turn back to face the crystal with more determination than ever."

    "They're both out there risking their lives for me.{w} I can't let them down."

    "I stare down the crystal and try my best to ignore the headache that thumps like a jackhammer.{w} Naturally, it's the most intense it's ever been.{w} But I can't let the pain get to me.{w} This?{w} This is nothing!"

    "I can just about make out a human-like form embedded within the crystal, though I can't make out any discerning features."

    "You.{w} This is all your fault.{w} Because of...{w}you...{w}Sayaka and Hikari are hurt.{w} It's unforgivable."

    "I hold up my right hand and pull back my sleeve.{w} Drawn on the back of my hand is a supposedly mystic symbol.{w} Something that Sayaka and Hikari had scribbled on the night previous."

    "They said this should help in drawing out any power that might lie dormant in me, if I'm inexperienced enough to not be in full control of it myself.{w} So it's sort of like...{w}a syphon, that can bring up magic with ease."

    "I give the hand a flex, and the symbol glows.{w} Okay.{w} So far, so good."

    "Now, I just have to..."

    "I steady my nerves.{w} I'm not sure what's going to happen when I do this, but I have to be prepared."

    "I can't stand around and hesitate forever, though.{w} Not with everything going on around me."

    "Sayaka.{w} Hikari.{w} I can do this!"

    "I thrust my hand out and make contact with the crystal."

    with hpunch

    "There's an immediate response, as a violent current jolts through me.{w} That's fine, though.{w} It was to be expected.{w} No problem."

    "It hurts, but I've felt worse.{w} Is this the best you've got?!"

    "I press my hand in deeper into the crystal's surface.{w} The pain gradually grows stronger, and a terrified shriek floods my ears."

    "And it's not from any of the girls in the cavern.{w} It's from {i}her{/i}.{w} She knows what's about to happen."

    "Well, she can cry all she wants, but it's not going to change a damn thing!"

    scene bg black
    with fade

    "Amidst all this chaos, I need to clear my mind.{w} Filter out all the noise.{w} A near impossible task with the current state of things, but I have to try."

    "From what I was told, magic is controlled mostly through thought.{w} Spells need to be envisioned--created within the mind."

    "Apparently those with vivid imaginations are often the kind that excel with this sort of thing."

    "I'm not sure if I've ever been much of a creative type, but there's a first for everything."

    "I need to envision a prison.{w} A closed off space.{w} Something unbreakable--closed off from the outside world."

    "Something so secure that this will never happen again."

    "And then I bind that prison, just like my ancestor did before me, with my own soul.{w} I have to tie myself to all of this, and remain the only key capable of unlocking it."

    "..."

    "I'm not sure if it's working, but the pain is rising with each passing moment I spend connected to this thing.{w} I feel faint.{w} I might pass out at any moment.{w} But I have to stand strong!"

    "I grit my teeth and let out a pained groan."

    "Why isn't this working?!"

    "Am I not imagining the spell correctly?"

    "I was sure I had it down perfectly."

    "I continue to repeat the process, my strength sapping rapidly as I struggle to keep upright."

    "It's no use.{w} This is completely futile."

    "No matter how hard I try, nothing seems to change.{w} Maybe I lack the magical capability, just as I feared?"

    p "Argh!{w} Scheiße!"

    "In a fit of rage, I clench my free hand into a fist and give the accursed crystal a good punch."

    "...It responds in turn, and lets out one final jolt of magic through my body before the pain dies down.{w} As does the screaming."

    "The resealing has been...completed."

    scene cave
    with dissolve

    "...You're kidding me.{w} All I had to do was punch the damn thing?!"

    "I...I don't..."

    "Wait.{w} I remember now.{w} From what I was taught that night."

    "While most magic could be done with just the dominant hand, in some cases--like the sealing--the other hand was required to complete the circuit and let the magic properly flow."

    "How on earth did I forget something as simple as that at such a crucial time?!"

    "I'm...{w} I'm such an idiot.{w} I almost feel like laughing."

    "In fact..."

    p "Hah ...{w} Ahahahaha ..."

    "Having perhaps finally lost it after all the things I've been subjected to in these recent days, I let out a feeble laugh as I topple over backwards, the strength draining from me completely."

    scene bg black
    with fade

    "And as darkness takes over, I pass out at least safe in the knowledge that I did it.{w} I actually...won."

    with Pause(4.0)

    "..."

    "Here I am, back in my dreams.{w} And there's nothing here.{w} She's gone.{w} For good this time, I hope."

    "Maybe now I can start to have more normal dreams.{w} And start to live out a more normal life again."

    "I roam the vast void with nothing to fear this time.{w} Peace.{w} At last."

    scene bg white
    with wake

    "I slowly come to my senses."

    "I'm on a cold, rough, uneven surface."

    "Stones scatter as I try to move my legs."

    "Where am I?{w} I don't..."

    "I squint through a harsh light to try and make sense of things."



    if sayaka > hikari:


        cg "It's a bit late to be sleeping in, don't ya think?"

        "A cheerful voice chirps, rousing me to my senses."

        "It could be none other than..."

        scene cg13_2
        with wake
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"

        p "S-Sayaka ...?"

        "I mutter her name, as it seems too good to be true."

        s "Yup.{w} That's me!"

        "She's kneeling over me, offering a helping hand with the sweetest smile I've ever seen."

        "Things were looking bleak back then...{w}but I never should have doubted she wouldn't pull through."

        "I'm so happy she's okay that I just about fight back the urge to cry."

        p "Sayaka, ich ..."

        p "Hab ich ...?"

        s "...Reseal the dark queen?{w} You betcha.{w} You did a perfect job!"

        "She beams as she takes a hold of my limp hand and gently props me up to a sitting position."

        s "I was worried there for a moment, you know.{w} I thought maybe the spell might have been too much for your body to handle..."

        p "W-Warte, du hast dir um {i}mich{/i} Sorgen gemacht?!{w} Ich dachte, diese Monster wären--"

        s "Them?{w} Pff.{w} That was nothing!{w} I took care of them no problem, you just missed it."

        p "Ich konnte dich nicht mal sehen!"

        s "I was...{w}playing dead...?"

        p "Sayaka ..."

        s "Eh-heh-heh..."

        "She scrubs at the back of her head and gives me the same goofy grin.{w} This girl..."

        p "Ich hab mir wirklich Sorgen um dich gemacht ..."

        p "Wenn dir was passiert wäre ...{w} Ich weiß echt nicht, was ich dann getan hätte ..."

        s "Aww, I didn't know you could get this sappy, Kenta."

        s "Am I going to need an umbrella for all the tears?"

        "It seems words aren't getting through to her, so..."

        scene cave
        $ sayaface='shy'
        $ sayapose='magical_1'
        show Sayaka
        with dissolve
        with hpunch

        s "E-eh?{w} Kenta?!"

        "I wrap my arms around her and pull her into a tight embrace.{w} It isn't enough just to be able to see her again, I wanted to make sure she was really there."

        p "Ich bin froh, dass es dir gut geht."

        s "I, uh..."

        "She seems to be at a loss for words, as her arms hang limply by her sides.{w} She's really making this awkward for me."

        $ sayaface='happy'
        show Sayaka

        s "Aw, what the heck!{w} C'mere, you big ol' softie."

        "She brings her arms up and returns the hug, squeezing me in a similarly tight embrace.{w} ...Maybe {i}too{/i} tight."

        $ sayaface='joking'
        show Sayaka

        s "Let's hope Hikari doesn't find out about this, huh?{w} Or she's gonna flip."

        "She stifles a giggle as she nestles into my shoulder."

        "Wait...{w} That's a point."

        "I pull back from the hug."

        p "Hikari!{w} Geht es ihr gut?"

        $ sayaface='smiling'
        show Sayaka

        "Sayaka tilts her head, looking confused for a moment."

        s "Hm?{w} She's fine!"

        p "Und ...{w} Yuzuki ...?"

        "She musters up a small smile, which instills some amount of hope in me."

        $ sayapose='magical_2'
        show Sayaka
        with dissolve

        s "Follow me!"



        "I do as instructed and follow along, almost hand in hand before we come to our senses."

        $ sayaface='happy'
        show Sayaka

        s "Tah-dah!{w} See?{w} One Hikari and one Yuzuki."

        "Hikari is standing guard, her sword drawn as she keeps the sharp end pointed firmly at a very...{w}tattered...{w}Yuzuki."

        "While unconscious, it doesn't look like Yuzuki is badly hurt.{w} She's breathing steadily, and I don't see too much damage beyond the cosmetic stuff."

        $ hikaface='angry'
        $ hikapose='magical_2'
        show Sayaka at left
        show Hikari at right
        with dissolve

        h "Da seid ihr zwei!{w} Was um alles in der Welt hast ihr so lange gemacht?!"

        "Yup.{w} She seems fine.{w} There isn't a scratch on her, and she's as lively as ever."

        $ sayaface='joking'
        $ sayapose='magical_1'
        show Sayaka
        with dissolve

        s "Well.{w} We were...{w}eh-heh-heh."
        stop music fadeout 5.0
        "Sayaka hides nothing and grins sheepishly, rocking on her heels as she does so."

        "Hikari furrows her brow, the faintest traces of anger visible across her forehead.{w} I think she pieced it together..."

        h "...Ugh, vergiss es.{w} Tiere."

        $ sayaface='normal'
        $ hikaface='normal'
        show Sayaka
        show Hikari

        "Yuzuki begins to stir from her slumber, forcing the attention on her as Sayaka and Hikari stand ready for the worst."



    if hikari > sayaka:


        tg "Sleeping on the job?{w} What a surprise.{w} What are we going to do with you?"

        "I hear a familiar voice.{w} One that's stern, yet...{w}there's a surprising amount of affection to it.{w} Unusually so."

        "I have a hunch who it could be...{w}but, I wonder...?"

        scene cg13_3
        with wake
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"    
        p "Hikari ...?"

        "It really is her.{w} She's okay!{w} Thank god..."

        h "Niemand anders.{w} Du hast dir auf dem Weg nach unten nicht den Kopf gestoßen, oder?...?"

        "Okay, yeah, it's Hikari."

        "Despite her usual scolding words, I can't help but there's a softer edge to them.{w} But maybe I'm just imagining things?"

        "And maybe I'm just imagining that smile, too, as she leans down to help me up."

        p "Hab ich ...{w} Ich mein ...{w} Ist es vorbei?"

        "She helps me up to a sitting position as I slowly regain my senses."

        h "Ja.{w} Die dunkle Königin ist wieder versiegelt, dank dir."

        h "Ich hatte meine Zweifel, dass die Dinge wirklich gut enden würden, mit dem Monster Yuzuki, das den Job beenden würde... "

        h "Aber, es sieht so aus als ob {i}du{/i} Helden-Material wärst."

        p "Es freut mich, dass es euch gut geht ...{w} und es tut mir leid, dass ihr euch wegen mir einer solchen Gefahr aussetzen musstet."

        h "Nein, entschuldige dich doch nicht!{w} Du hast nichts falsch gemacht.{w} Ich würde mein Leben immer für dich reskieren, Kenta."

        "..."

        "Ah, she did it again.{w} She said something super embarrassing without realising it."

        "I'm sure any moment now she'll realise her mistake, and her face will go an interesting shade of red again."

        "Or...{w}stay as that same sincere smile that the more I look at, the more I can feel my heart begin to throb."

        "Okay...{w} Maybe she just didn't realise what she said?{w} I'm sure I can still get a reaction out of her somehow.{w} I just need to say something like..."

        p "Ihr müsst euch ja wirklich große Sorgen um mich machen, hm?"

        "Unflinching in the face of my question, she takes a moment to think things over, before..."

        h "...{w}Ja.{w} I-Ich tuh es."

        "Her smile remains, even if her cheeks are flaring up."

        "What is this?!{w} Now {i}I'm{/i} the one getting all flustered here!"

        p "W-Was zur Hölle sagst du da?!{w} Du ...{w} Du Idiot!"

        "I'm not sure if she can tell if I'm being genuine, or just making fun of her here.{w} ...I honestly can't tell myself at this point."

        h "Muss ich...{w}es wirklich aussprechen?"

        "She's getting close now.{w} {i}Way{/i} too close."

        p "H-Hey, was--"

        scene cave
        $ hikaface='shy'
        $ hikapose='magical_1'
        show Hikari
        with dissolve

        "She yanks me up to a standing position, before she brings both of her arms around me in a warm embrace.{w} Oh.{w} {i}Ohhh.{/i}"

        "She doesn't say anything, and simply holds me.{w} I'm fairly sure I can feel the intense heat radiating from her face, however."

        "I'm almost scared to reciprocate here, in case I ruin everything.{w} She's unpredictable enough that anything I might do might end with me flat on my back again."

        "We stand together awkwardly for an indeterminate amount of time.{w} I think there was supposed to be something sweet about this moment?{w} I'm not so sure anymore."

        "Still, I'm glad she's okay.{w} Things were looking bleak back there.{w} Both her, and--"

        p "Sayaka!"



        $ hikaface='shocked'
        show Hikari

        h "H-huh?{w} Was?!"

        "I awkwardly blurt out her name as Hikari stumbles backwards, at a loss for words.{w} Maybe that wasn't the best time?"

        p "Äh, entschuldige ...{w} Ich mein ... Geht es Sayaka gut?"

        $ hikaface='angry'
        show Hikari
        $ hikaface='normal'
        $ hikapose='magical_2'
        show Hikari
        with dissolve

        "She gives me a sour look before huffing out a sigh."

        h "Sie ist völlig in Ordnung."

        p "Oh, Gott sei Dank ..."

        h "Es ist der {i}andere{/i} Unruhestifter."

        "She scoffs and throws a sneer towards some other part of the cave.{w} It's amazing how quickly I was able to turn things from heartwarming to having her revert to her usual, annoyed self."

        "Other troublemaker...?{w} Oh!{w} She has to mean..."

        p "Yuzuki?!{w} Ihr geht es auch gut?!"

        $ hikaface='angry'
        show Hikari

        h "Sie hat wirklich Glück, dass sie okay ist.{w} Und nach aldem was sie uns angetan hat, weiß ich nicht ob sie das {i}verdient{/i} hat."

        "She motions over somewhere."

        $ hikaface='normal'
        show Hikari

        h "Komm, Ich werde es dir zeigen.{w} ...Idiot."

        "I follow after her as she takes off at a pace far too fast for my unsteady legs."

        p "H-Hey, beruhig dich!"

        h "Siehst du, sie sind okay.{w} ...und anscheinend sind sie dir wichtiger als ich."

        $ hikapose='magical_1'
        show Hikari
        with dissolve

        "She thrusts out a violent finger towards Sayaka, who is standing guard close by an unconscious Yuzuki"

        $ sayaface='happy'
        $ sayapose='magical_2'
        show Sayaka at left
        show Hikari at right
        with dissolve

        s "Ah, there they are!"

        "Sayaka is safe and sound, the same blinding grin on her face as always as she greets us with a friendly chirp.{w} ...That's a relief."

        "Yuzuki looks a bit more worse for wear, her outfit in tatters and bearing a multitude of bruises that cover her body.{w} But, the important thing is that she's alive, which I can safely say is true from the gentle rise and fall of her chest."

        $ sayaface='joking'
        show Sayaka

        s "You know, you could have taken your time getting over here.{w} I understand if you two want your--ahem--alone time."

        $ sayaface='smiling'
        $ hikaface='shy'
        $ hikapose='magical_2'
        show Sayaka
        show Hikari
        with dissolve

        h "D-Das hätten wir getan, wenn Mister Dense hier nicht darauf bestanden hätte, direkt zu dir zu marschieren."

        "Uhh...?{w} I'm not really sure what to make of this.{w} She continues to say such embarrassing things without a care in the world.{w} ...Is this really Hikari?"

        "Wait, 'dense'?!{w} Who's dense here?!"

        $ sayapose='magical_1'
        $ sayaface='happy'
        show Sayaka
        with dissolve

        s "Oh, you should have seen her, Kenta.{w} Once the resealing was done, she was in such a frenzy to reach you.{w} I've never seen something so adorable!"

        $ hikaface='embarrassed'
        show Hikari

        s "'Kyahh!{w} Is Kenta okay?!{w} I'll go get him, you watch over Yuzuki!'"

        "She puffs out her chest and puts on a silly voice as she recalls the moment.{w} Is this supposed to be her Hikari impression?"

        p "V-Verstehe."

        $ sayaface='smiling'
        show Sayaka

        s "Hmm?{w} That's all you've got to say to such a heartfelt moment?"

        "If I'm being honest, I really didn't know Hikari cared for me {i}this{/i} much.{w} I thought she was just shy in general around people before!"

        "I mean, she's always been there for me.{w} Putting her life on the line.{w} And after today...{w}I've realised there's perhaps a bit more to it than just her working out of duty."

        "But, I've been through so much in these last few moments, I'm really not sure how to process it at all.{w} All I can do is stand with my mouth slightly ajar."

        p "Ähhh ..."

        $ hikaface='normal'
        $ hikapose='magical_1'
        show Hikari
        with dissolve

        s "Hmm.{w} Well, better luck next time, Hikari.{w} It looks like he's already fallen for me, and there's nothing that can change his mind!"

        $ sayaface='joking'
        show Sayaka

        "She lets out a cackle as she jabs at Hikari's side, whose mood sours with each increasing poke.{w} Don't...{w}don't poke the wild animal, Sayaka!"

        s "Hmm, hmm, hmmm?"

        "She continues to prod.{w} I fear for her safety."
        stop music fadeout 4.0
        $ hikaface='angry'
        show Hikari

        "Hikari opens her mouth.{w} I can see the fire in her eyes.{w} Something bad is going to happen here!"

        h "Okay, das tut es!{w} Sayaka, Ich werde wirklich--"

        $ hikaface='normal'
        $ sayaface='normal'
        show Hikari
        show Sayaka

        h "Huh?"

        "Yuzuki stirs, forcing the pair back into their serious mode.{w} Oh, thank god!"



    if sayaka == hikari:


        cg "There he is, safe and sound!{w} Our hero."

        tg "Is...{w}is he really okay?{w} After a spell like that, there's a good chance it could have--"

        with hpunch

        cg "Yup!{w} Look!{w} Still breathing."

        "Something prods at my face.{w} A warm, tender touch."

        with hpunch

        "...And it prods some more.{w} And more."

        tg "What are you doing?!{w} You can't just poke at him like that!"

        cg "Hmm?{w} Is someone jealous?{w} That I'm getting to be all intimate, and you're not?"

        tg "P-please!{w} In what world is that 'intimate'?{w} You're being a nuisance, more than anything.{w} Give him some room!"

        cg "Okay, okay!"

        cg "...One last poke!"

        "{i}Smush{/i}.{w} The left side of my cheek is pushed a great deal up.{w} Okay, this is weird.{w} I should probably wake up now."

        p "Nghh."

        tg "A-ah!{w} He's waking up!{w} Sayaka, get away!"

        cg "Wahh, okay, okay!{w} You don't need to haul on me like that."

        scene cg13_1
        with wake
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"    
        "I awake to a familiar, comforting sight.{w} My guardian angels--Sayaka and Hikari."

        "They're both perfectly fine.{w} Not a single scratch on either of them.{w} I'm...{w}I'm so glad."

        p "M-Mädels ...?"

        "I have to call out to both of them, just to confirm that this is real."

        s "Good morning!{w} How are you feeling there?"

        h "Gott sei Dank geht es dir gut...{w} Du solltest uns keine Sorgen machen, Kenta!"

        "They both look relieved as they offer their hands my way."

        s "Can you stand?"

        "...I try my best to heave myself up off the ground, but my feeble arms give way.{w} Whoops.{w} Guess that resealing business really took more out of me than I thought."

        "Sayaka giggles at my attempt, while Hikari flashes me a look of concern."

        s "I'll take that as a 'no'.{w} C'mon, up we get!"

        h "Du solltest dich danach nicht drängen. {W} Wenn du unsere Hilfe brauchst... {w} Alles, was du tun musst, ist es zu sagen, und ich werde glücklich sein..."

        "She trails off into a murmur inaudible to even herself, I'm sure."

        "Sayaka and Hikari both take up a hand of mine, and they help me up to a sitting position."

        "As I sit up, the fog begins to clear within my mind and I recollect my senses."

        s "There we go.{w} All good?"

        h "Ja, wenn es etwas gibt was du brauchst, halte dich nicht zurück zu fragen!"

        "Sayaka kneels at my side, her eyes glimmering.{w} ...As does Hikari, who kneels at my opposite side.{w} This is getting a bit weird now.{w} What is this?"

        p "Es geht mir, äh, entsprechend.{w} Macht euch keine Sorgen.{w} Ich bin nur ein bisschen schwach auf den Beinen."

        p "Ich ...{w} Ich hab mir ehrlich gesagt mehr Sorgen um euch gemacht.{w} Ich hatte echt Angst um euch!"

        s "Psh, us?{w} We're tougher than we look.{w} And we've been through worse.{w} We're a-okay!"

        h "Exact.{w} Wir wurden dafür trainiert.{w} Es hätte vielleicht schlecht ausgesehen, aber ich versichere dir, alles war ... {w}unter Kontrolle!!"

        "They're trying their best to assure me things were okay, but things really did look dire back then..."

        "Sayaka suddenly leans in, a dangerous smile creeping upon her face."

        s "Now, when you say you were worried about 'us'...{w} Was there anyone in particular who you were {i}more{/i} worried for?"

        p "Ähh ...?{w} K-Kann ich nicht ..."

        h "S-Sayaka!{w} Was hast du hier versucht?!"

        s "Ohh, nothing."

        s "Clearly, Kenta's hesitance to say anything means he doesn't want to hurt either one of us.{w} Or, hurt {i}you{/i} in particular."

        h "W-Was?{w} Was macht dich so sicher, dass er mehr über dich besorgt war, als über mich?!"

        p "Ey, jetzt kommt schon ..."

        "I'm not really sure what this has turned into.{w} Of all the times for their competitive nature to kick in..."

        scene cave
        $ sayaface='smiling'
        $ sayapose='magical_1'
        $ hikaface='normal'
        $ hikapose='magical_1'
        show Sayaka at left
        show Hikari at right
        with dissolve

        p "Kann das nicht erstmal warten?{w} Wie wär's, wenn wir erstmal nach Hause gehen und--"

        "I let out a sharp gasp of pain as I try to stand up.{w} Yup.{w} Still not all there, yet."

        $ sayaface='happy'
        $ sayapose='magical_2'
        show Sayaka
        with dissolve

        s "Oh, let me help you!"

        "Sayaka gladly swoops in and hooks an arm under mine."

        $ hikaface='shy'
        show Hikari
        
        h "I-Ich kann auch helfen!"

        "And, of course, Hikari takes up my other arm with just a little less grace than Sayaka."

        "Somehow, the pair are able to get me to a standing position without tearing me apart."

        $ sayaface='smiling'
        $ sayapose='magical_1'
        show Sayaka
        with dissolve

        s "Now, before we leave, I think there's somebody you should see first."

        $ hikaface='normal'
        show Hikari

        h "Ugh.{w} Ist es wirklich so wichtig?{w} Ich habe ihr Leben verschont.{w} Können wir sie nicht einfach zurücklassen?"

        "Sayaka and Hikari both vie for different directions as we stumble along as one just barely functional unit."

        "Wait, are they talking about..."

        p "Yuzuki?!{w} Du meinst, es geht ihr gut?"

        s "Yup!{w} Right this way!"

        stop music fadeout 5.0

        "We swerve wildly as Sayaka takes command, Hikari reluctantly following along."

        $ sayaface='joking'
        show Sayaka

        s "Look, see!{w} She's fine.{w} And...{w}we probably shouldn't have left her alone.{w} But, we just couldn't come to an agreement on who should come help you!"

        "Slumped against a nearby rock is an unconscious Yuzuki, her outfit in tatters and her body bruised.{w} But, beyond that, she seems alive, breathing gently as she rests from what must have been a tough battle beforehand."

        $ sayaface='smiling'
        show Sayaka

        "I begin to wonder just how long she might be out for, but already I can see her begin to stir."

        $ sayaface='normal'
        show Sayaka

        "Hikari and Sayaka put on their serious faces and take up defensive positions before me, leaving me to wobble on my feet as I try to stand upright on my own."


    scene cg17
    with dissolve

    play music "bgm/sadintro.ogg" fadein 2.0
    queue music "bgm/sadloop.ogg"

    y "Nghh..."

    "She winces, and gives us all an intense look-over."

    "Slowly, she comes to the realisation of what has happened."

    y "Es ist...{w}Es ist vorbei, oder?{w} Ich...{w}hab verloren."

    s "'Fraid so."

    y "Sie ist...{w}Sie ist jetzt komplett weg.{w} Meine Königin...{w} Ich kann sie überhaupt nicht fühlen."

    "She seems a lot more subdued now.{w} The madness is gone, and in its place, all I can see is a sad girl.{w} One that was misguided."

    y "Aber ich war so nah!{w} Ich...{w}Ich konnte es haben...{w} Argh, verdammt!"

    "She thumps a feeble fist against the floor.{w} There's no strength left at all."

    y "Na, und?{w} Sind Sie hier, um sich zu freuen?"

    h "Hey jetzt!!{w} Du solltest dankbar sein, dass ich dein Leben vorhin verschont habe.{w} Ich hätte dich locker in zwei Teile zerschneiden können, als dich die Kraft verlassen hat!"

    y "Vielleicht wäre es besser gewesen, wenn du es getan hättest.{w} Ich habe keinen Grund, jetzt zu leben.{w} Ich bin...{w}Ich bin ein Versager."

    p "Sag das nicht!"

    "I can't stand aside any longer while she puts herself down like this.{w} I push past Sayaka and Hikari to face her."

    "Yuzuki meets me with some surprise in her eyes, but it quickly turns to the same look of defeat she had a moment ago."

    y "Warum nicht?{w} Es ist die Wahrheit, nicht wahr?"

    y "Ich war so verzweifelt nach einer Art Gesellschaft in meinem Leben, dass ich ihr mein Leben freiwillig gab."

    y Sie erzählte mir alles, was ich hören wollte."{w} Dass jeder mich anbeten und mir gehorchen würde, wenn ich ihr helfen würde..."

    h "Was?!{w} Das ist das Dümmste was ich je gehört--"

    y "Es klingt dumm, ich weiß.{w} Zu denken, dass ich all das in der vergeblichen Hoffnung getan habe, dass es mich bekommen würde ...{w}Freunde."

    y "Ich habe gerade nicht nachgedacht.{w} Ich war so besessen davon, dass ich niemals daran dachte, irgendwas zu hinterfragen."

    "So she isn't a bad person.{w} Just misguided.{w} And did the wrong things for an innocent enough goal.{w} I can't help but feel sorry for her...{w} for things to have ended up this way."

    y "Und jetzt, mit der einzigen Chance, die ich hatte, war mein Ziel immer dahin.{w} Warum sollte ich weiterleben?{w} Es ist hoffnugslos..."

    s "Hmm.{w} I see, I see."

    "Sayaka cups a hand to her chin and nods to herself, as if intensely thinking about what she's been told."

    stop music fadeout 2.0

    s "I think I know an easy solution to all of this!"

    y "...?"

    h "D-Du tust es?"

    s "Yup!"

    "Sayaka bounces forward and extends a hand to Yuzuki, a blinding smile upon her face."

    s "{i}We'll{/i} be your friends, Yuzuki."

    scene cave
    $ sayaface='smiling'
    $ sayapose='magical_1'
    $ hikaface='shocked'
    $ hikapose='magical_1'
    $ yuzuface='shocked'
    $ yuzupose='magical_1'
    show Sayaka at left
    show Hikari at right
    show Yuzuki at center
    with dissolver

    play music "bgm/magicalgirlintro.ogg" fadein 2.0
    queue music "bgm/magicalgirlloop.ogg"    

    "Yuzuki is taken aback by the sudden gesture, but not as much as Hikari."

    h "Eh?!{w} W-Wier werden?!"

    y "...Wirklich!?"

    $ sayaface='happy'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Of course!{w} You don't seem like a bad person.{w} I think you were just going about things the wrong way."

    $ hikaface='angry'
    show Hikari

    h "S-Sie hat uns versucht zu töten, Sayaka!{w} Wie kannst du sagen, dass sie nicht--"

    $ sayaface='joking'
    show Sayaka

    s "Ahh, that's all in the past.{w} I'm fairly sure you've tried to kill me several times, too, Hikari!"

    $ yuzuface='angry'
    show Yuzuki

    y "I-ist das eine Art Trick?{w} Verspottest du mich...?"

    $ sayaface='smiling'
    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "No tricks.{w} Me, Kenta, and {i}even{/i} Hikari are all happy to be your friends."

    s "Right, guys?"

    p "Klar.{w} Ich hab kein Problem damit."

    $ hikaface='normal'
    show Hikari

    h "Jetzt warte mal kurz--"

    s "{i}Right{/i}, Hikari?"

    "Sayaka twists her head to meet Hikari in a most unnatural fashion, her smile widening.{w} It's like something out of a horror movie..."

    $ hikaface='scared'
    $ hikapose='magical_2'
    show Hikari
    with dissolve

    h "U-uh...{w} R-Richtig!"

    $ yuzuface='shy'
    show Yuzuki

    y "I-ihr..."

    $ yuzuface='smiling'
    show Yuzuki

    "Yuzuki doesn't know how to process this.{w} Her face flickers through a range of emotions before she settles on a smile, the faint trace of tears bubbling up in the corners of her eyes."

    y "Ich...{w}Ich verdiene nichts davon.{w} Warum bist du so nett?"

    $ hikaface='normal'
    $ sayaface='happy'
    show Sayaka
    show Hikari

    s "Aw, don't be like that.{w} Everyone deserves friends!{w} Who cares if you might have done a few silly things before?{w} True friends overlook those sorts of things!"

    "I'm not really sure if we should be fully overlooking the fact she was that twisted, dark angel before, but Sayaka still has a good point."

    $ sayaface='smiling'
    show Sayaka

    s "Now, come on.{w} Let's get out of this creepy cave and put this all in the past.{w} I dunno about you guys, but I'm feeling pretty exhausted right about now."



    scene bg black
    with fade

    "And so, after perhaps the most dramatic moments of my life, we all exit the cave, with the hope that we never have to return."

    "A long-lost evil was put back in its place and we made a new friend today.{w} All in all, I'd say it's been a fairly eventful day!"

    "Thankfully, thanks to Yuzuki, we find an alternative way out of the cave that didn't involve squeezing ourselves into an impossibly small tunnel.{w} I'm not sure I could have made the journey back if that were the case."

    "I can actually think clearly now.{w} The headaches are gone.{w} For good, I hope."

    scene forest trail
    with fade

    "We emerge back into the forest, the warm, vibrant rays of the sun a welcome change after being in that cave for so long."

    show Sayaka
    $ sayaface='happy'
    $ sayapose='magical_1'
    with dissolve

    s "Ahhh, fresh air at last!"

    "Sayaka bounds out a few steps ahead to take in the crisp air.{w} Hikari and Yuzuki are trailing behind, seemingly still not comfortable with one another.{w} I guess they always had the biggest rivalry during their encounters."

    s "Well, that took less than time than I thought it would.{w} Looks like we still have plenty of the day!"

    "She continues to radiate optimism as she takes in the sights, but I can't shake the one question that has been on my mind since we started this whole crusade."

    p "Was ...{w} Was geschieht jetzt?"

    $ sayaface='smiling'
    show Sayaka

    s "Hmm?"

    p "Ich mein, haben wir diesen einen Grund, weshalb ihr hier seid, nicht gerade aus der Welt geschafft?"

    $ sayaface='normal'
    show Sayaka

    s "Ohh..."

    "It seems she realises what I mean, as her smile shrinks.{w} And...{w}it seems like that reaction answered my question for me."

    s "That's...{w} Well..."

    $ hikaface='normal'
    show Hikari at right
    show Sayaka at left
    with dissolve

    h "Du hast recht.{w} Unser Job {i}is{t/i} fertig hier."

    "They both give me solemn looks.{w} I knew it.{w} I didn't want to accept it, but I knew this was going to happen..."

    $ yuzuface='shocked'
    $ yuzupose='magical_1'
    show Yuzuki at center
    with dissolve

   y "Warte, du wirst jetzt gehen?!{w} Ich dachte, du hättest es versprochen--"

    $ sayaface='smiling'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Hey!{w} Who said anything about us leaving?"

    $ yuzuface='normal'
    show Yuzuki

    s "It's true that we have no {i}official{/i} reason to stay any longer."

    $ sayaface='joking'
    show Sayaka

    s "But, I think we've got a lot of holiday time that we could cash in.{w} Right, Hikari?"

    h "Ferien?{w} Was um alles in der Welt bist du--"

    $ sayaface='happy'
    $ hikaface='scared'
    show Hikari
    show Sayaka

    "That smile.{w} That look.{w} It cuts Hikari off mid-sentence as she changes her mind about things.{w} I think I'm quickly learning who is the boss in this group."

    $ hikaface='normal'
    show Hikari

    h "A-ah!{w} Ja, natürlich!{w} Wir haben viel Freizeit, wir könnnen uns mal frei nehmen."

    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "See!{w} It isn't goodbye yet, so don't you guys worry.{w} I wouldn't be so mean as to deprive you all of me!"

    $ sayaface='smiling'
    show Sayaka

    s "And we'll make the most of the time we have together.{w} As friends!{w} There's still so much around here I have to try!"

    "She trails off into a list of things she wants to do, as Hikari struggles to come to terms with their impromptu 'holiday'."

    "I'm guessing whichever top secret magic organisation they belong to isn't going to be happy when they learn about this..."

    "Still, I'm somewhat relieved that they'll be sticking around a bit longer.{w} Even if only for a while."

    "While things have certainly been crazy these past few days...{w} I definitely can't say I hated all of it."

    "The parts where things were trying to kill me were bad, sure, but, I really had a lot of fun."

    "I've never really had much of a social life these days, so all these experiences had been pretty new to me in more than one way."

    "They haven't just been my guardian angels, they've also been my friends.{w} Damn good ones, at that."

    "Okay, so maybe Sayaka's jokes can be a bit much, and Hikari can be a little bossy at times...{w}but that just adds to their charm."

    $ sayaface='happy'
    show Sayaka

    "They pulled me into a completely new and unknown world when we first met.{w} And I might have been just a {i}tiny{/i} bit reluctant at first about accepting things."

    $ hikaface='angry'
    show Hikari

    "I wouldn't change any of these experiences for the world, though."

    "I feel they've helped shape me into a better person.{w} Pulled me out of whatever shell I might have been hiding away in these past years."

    $ sayaface='joking'
    show Sayaka

    "I can't help but smile as my guardians break into an argument once more.{w} I'm not even sure what started it this time."

    "I need to make sure I enjoy the little time I have left with them, before they leave.{w} Probably for good."

    "It's a bit depressing to know that this won't last forever, but then that's just all the more incentive to make this time count and create as many happy memories as possible."

    h "Ich werde dich umbringen!"

    $ sayaface='scared'
    show Sayaka

    s "Wahh, calm down, it was just a joke!{w} Kenta, protect me!"

    $ yuzuface='scared'
    show Yuzuki

   y "Du bist sicherlich ein seltsamer Haufen..."

    "...Yup.{w} Happy memories."

    scene bg white
    with wake
    with Pause(3.0)
    scene bedroom day
    with wake

    "I wake up feeling better than ever.{w} No headaches.{w} No feeling of having dreamt something terrible.{w} Just...{w}bliss."

    "It's been about a week now since we resealed the dark queen.{w} And true to their word, Sayaka and Hikari have stuck around."

    "They continue to go to school, and we continue to hang out, making the most of the free time we have."

    "...They still insist on camping outside, though.{w} There was really no need for that, since there haven't been any more monster attacks."

    "Maybe they've just gotten too used to it?{w} Or they're just as stubborn as ever, I don't know."

    "I guess it's not {i}that{/i} bad.{w} I'm just surprised they haven't been caught yet.{w} And when that time comes, I'm only going to say I told them so."
    stop music fadeout 2.0
    p "Hm?"

    "There's a knock at my door.{w} I wonder who it is?"



    if sayaka > hikari:


        s "Yo!{w} I hope you're all like, dressed and stuff, or this is going to be super embarrassing.{w} Oh well!"
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"
        $ sayaface='smiling'
        $ sayapose='school_1'
        show Sayaka
        with dissolve

        "Saying that and giving me no time to react, she swings the door open and dances into my room."

        "She looks almost disappointed with the results and lets out a sigh."

        s "Aww."

        p "Äh, guten Morgen, Sayaka."

        "I finish doing my tie.{w} Unfortunately for her, I {i}am{/i} in fact fully dressed.{w} Something of a rarity at this time of the morning, but I've learned to be wary with her on the prowl."

        $ sayaface='happy'
        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Mornin'!{w} It seems my attempt to sneak up on you while you were all helpless and defenseless has backfired on me."

        $ sayaface='smiling'
        show Sayaka

        s "Maybe I'm getting too predictable?"

        p "Vielleicht."

        $ sayaface='joking'
        $ sayapose='school_1'
        show Sayaka
        with dissolve

        s "Hmm.{w} Perhaps next time I should come in from the window?"

        "...Please don't."

        $ sayaface='happy'
        show Sayaka

        "Sayaka breaks into hysterics, before she begins to poke about my room."

        $ sayaface='smiling'
        show Sayaka

        "Lately she's been making it a habit to get me up in the mornings.{w} I can't tell you how scared I was the first time to wake up with her peering over with that same grin."

        "She says it's because she wants to make sure I'm up on time for school, but I'm sure there must be other reasons behind it."

        "In fact, I feel like we've grown a lot closer since the events in that cave."

        "She's always been really friendly and affectionate, sure, but there's definitely been in increase in said friendliness and affection."

        "At lunchtimes she'll always grab me by the hand and drag me to the cafeteria, whether I like it or not.{w} And during our walks home, I can't help but feel like she's making a conscious effort to make us outpace Hikari."

        "Maybe I'm just imagining things?{w} I don't know.{w} All I know is--"

        p "H-Hey!{w} Wer hat gesagt, dass du das anfassen kannst?!"

        "She pokes at my laptop, something she's always had her eye on every time she's been in here."

        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Hm?{w} I just wanted to have a look.{w} I mean, {i}surely{/i} a nice innocent boy such as yourself wouldn't have anything to hide on here, hmm?"

        p "Ähm.{w} Genau.{w} A-Aber wir kommen noch zu spät zur Schule, wenn du hier rumblödelst!"

        $ sayapose='school_1'
        show Sayaka
        with dissolve

        s "Mmm.{w} I'll just have a quick look then.{w} Let's see...{w} Where might the 'important school work' folder be?{w} Or, what is this strangely named one that seems to have a password--"

        p "Sayaka!"

        $ sayaface='joking'
        show Sayaka

        s "I'm kidding, I'm kidding!{w} I haven't even turned the thing on."

        "She swivels the laptop around my way with a grin, its screen indeed blank."

        p "O-Ohh ..."

        $ sayaface='smiling'

        s "That sure is an interesting reaction, though.{w} Almost as if you {i}did{/i} have a folder like that, hmm?"

        "..."

        "It's not classified as lying if I don't say anything.{w} I meet her head on with a blank stare."

        "She opens her mouth to say something, no doubt to tease me further."

        with hpunch

        h "Wir werden noch zuspät kommen, wenn ihr zwei nur rumalbert!"

        "Hikari saves the day, her commanding voice enough to sound up the stairs and into my room."

        $ sayaface='happy'
        show Sayaka

        s "Well.{w} We'll save this matter for another day, hmm?{w} Don't think you're off the hook so easily, mister!"

        hide Sayaka
        with dissolve

        "Saying that, she bounds on out and down the stairs.{w} I think she leapt the entire flight of them in one go."

        stop music fadeout 2.0

        scene kitchen day
        with dissolve

        "I follow shortly after, and I'm met by two additional house guests."

        $ sayaface='smiling'
        $ sayapose='school_1'
        $ hikaface='normal'
        $ hikapose='school_1'
        $ yuzuface='normal'
        $ yuzupose='school_1'
        show Yuzuki at center
        show Hikari at right
        show Sayaka at left
        with dissolve

        play music "bgm/everydayintro.ogg" fadein 2.0
        queue music "bgm/everydayloop.ogg"

        "Hikari and Yuzuki stand in the dining room, at an awkward distance from one another, still yet to fully become friends."

        "Much like Sayaka and Hikari, Yuzuki apparently has no qualms with breaking into my house while I sleep to wait for me to get up."

        "...When I think about it this way, it's a bit worrying.{w} I'll just do the smart thing and ignore it."

        p "Guten Morgen, meine Lieben."

        $ hikaface='angry'
        show Hikari

        h "Es ist Zeit.{w} Was wllt ihr beide jetzt tun?"

        $ sayaface='happy'
        show Sayaka

        s "Well, if you {i}really{/i} have to know, we--"

        h "Eigentlich, will ich es garnicht hören!{w} Ich bin sicher, es war etwas unangebrachtes."

        "Hey now, why am I getting lumped in with her?{w} I'm an innocent, pure-hearted boy!"

        $ sayaface='joking'
        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Ah well.{w} Your loss."

        $ yuzuface='smiling'
        show Yuzuki

        y "Kenta.{w} Guten Morgen."

        "Yuzuki greets me quietly, a faint smile on her face."

        hide Sayaka
        hide Hikari
        show Yuzuki at center
        with dissolve

        "Since we started hanging out, it's been a gradual process of her opening up more to us.{w} She's still pretty quiet most of the time, and won't dive into many conversations, but I think she enjoys our company."

        "It must be tough for her to adjust to things after she's finally obtained the friends she so desired for all these years."

        "I'm sure it won't be long until she's out of her shell with Sayaka and Hikari at the helm, though.{w} They seem to be able to bring out the best in people."

        "I greet her back with a nod of my head, but my eyes are quickly fixed to Sayaka, who is heading somewhere dangerous."

        $ sayaface='smiling'
        $ sayapose='school_1'
        hide Yuzuki
        show Sayaka at center
        with dissolve

        s "So!{w} Who wants breakfast?"

        p "Oh nein, das kommt gar nicht in Frage!"

        $ sayaface='scared'
        show Sayaka

        "She stops in her tracks, inches from the kitchen."

        s "Aw, but I was only gonna--"

        p "Nop."

        $ sayaface='smiling'
        show Sayaka

        s "Fine, fine.{w} I tried."

        p "Das hast du, und ich bewundere dich auch dafür ... Aber es wird nicht passieren.{w} NIE WIEDER."

        $ sayaface='shocked'
        show Sayaka

        s "It wasn't even that bad!"

        $ sayaface='smiling'
        show Sayaka

        "I sidle past her and enter the kitchen myself.{w} She gives me the usual pout, but, like always, it soon melts away and her smile returns."

        s "Well...{w} Can I at least...{w}watch?{w} Maybe I'll be able to learn better for some time in the future!"

        "She gives me a look that's impossible to say no to.{w} Damn it!"

        p "Argh, gut, von mir aus!{w} Fass aber bloß nichts an."

        $ sayaface='happy'
        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Yay!"

        "She watches over my shoulder.{w} Literally.{w} Her head is resting on my shoulder.{w} It makes it a bit more difficult to do things, but honestly...{w}it's not bad."

        scene bg black
        with fade
        with Pause(3.0)
        scene kitchen day
        $ sayaface='happy'
        $ sayapose='school_1'
        $ hikaface='normal'
        $ hikapose='school_1'
        $ yuzuface='normal'
        $ yuzupose='school_1'
        show Sayaka at left
        show Hikari at right
        show Yuzuki at center
        with fade

        s "Ahh, delicious!"

        "Sayaka lets out a content sigh, having devoured her meal in record time.{w} I'm not even sure she has any time to taste with how fast she wolfs this stuff down."

        $ sayaface='smiling'
        show Sayaka

        y "Ja.{w} Es war nett.{w} Ich habe nicht erwartet, dass du so ein guter Koch bist, Kenta."

        $ hikaface='angry'
        show Hikari

        h "Vielleicht heute ein bisschen übertrieben.{w} Ich mache dir jedoch keine Vorwürfe, dass sich dieses {i}Ding{/i}" in der Küche zu dir gesellt hat.

        s "Careful now, Hikari, your jealousy is showing!"

        $ hikaface='embarrassed'
        $ hikapose='school_2'
        show Hikari
        with dissolve

        h "H-Halt dein Mund!{w} Der Schwachsinn, auf den du kommst..."

        $ hikaface='normal'
        show Hikari

        h "W-Wie auch immer, wir werden zu spät zur Schule kommen, wenn wir noch mehr Zeit verschwenden.."

        $ sayaface='joking'
        show Sayaka

        s "Wow!{w} I don't think I've ever seen you in such a rush to get to school before, Hikari."

        $ hikaface='angry'
        show Hikari

        h "Hmph!"

        hide Hikari
        show Sayaka at left
        show Yuzuki at right
        with dissolve

        "Hikari storms on out of the front door, leaving the rest of us to scramble for our bags and shoes.{w} Maybe one day I'll finally understand her?"

        $ sayaface='happy'
        show Sayaka

        s "C'mon, adventure awaits us, Kenta!"

        hide Yuzuki
        show Sayaka at center
        with dissolve

        "Sayaka extends me a hand as Yuzuki shuffles on by."

        p "Also den Test, den wir heute haben, würd ich wohl kaum als 'Abenteuer' bezeichnen ..."

        $ sayaface='shocked'
        show Sayaka

        s "Wait.{w} We have a test?!"

        p "Na ja.{w} Schon.{w} Es wurde immer wieder diese Woche erwähnt!{w} Sag jetzt bloß nicht ..."

        $ sayaface='joking'
        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Eh-heh-heh..."

        "Hopeless.{w} I can't help but smile."

        $ sayaface='happy'
        $ sayapose='school_1'
        show Sayaka
        with dissolve

        s "Ah, it's okay.{w} I'll just take the answers from you, if I need them!{w} Now...{w}onwards!"

        "She takes a firm hold of my hand and begins to drag me out of the house."

        p "S-Sayaka, warte, ich hab nicht mal meine Schuhe an!"

        s "Onwards!"

        stop music fadeout 2.0

        scene bg white
        with wake


    if hikari > sayaka:


        h "Kenta?{w} Bist du schon wach?{w} Jeder ist schon hier, und...{w}wir sind hungrig!"

        p "Ja, kommt rein."

        h "O-okay."

        $ hikaface='shy'
        $ hikapose='school_1'
        show Hikari
        with dissolve

        "The handle goes down slowly, before she gradually opens the door.{w} Even as she steps in, she does so with a hand covering her eyes, like she was expecting to see something indecent or something."
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"        
        $ hikaface='smiling'
        show Hikari

        "Relieved to see I am in fact dressed, she greets me with a smile."

        h "Oh.{w} Guten Morgen."

        p "Morgen!"

        "Her smile is something I'm still having to adjust to."

        "Something definitely changed for us back then in the cave.{w} I don't know how to put it, but she's more...{w}friendly?"

        "Like, a lot of the grumpiness will still show up from time to time, but she smiles a lot more now.{w} Which is nice.{w} It definitely suits her."

        "She stands by awkwardly, as if unsure what to do with herself."

        p "Warte ...{w} Du hast gesagt, ihr seid schon alle da und ihr habt Hunger, oder?"

        $ hikaface='normal'
        show Hikari

        h "Huh?{w} Ja.{w} Warum?"

        p "Und du, äh ...{w} und du hast Sayaka unbeaufsichtigt lassen ...?"

        h "Ich bin mir nicht sicher was du..."

        $ hikaface='shocked'
        show Hikari

        "Her eyes widen as she comes to the realisation.{w} {i}Yeah{/i}."

        h "Vielleicht ist es noch nicht zuspät."

        p "Ich hoff's doch!"

        stop music fadeout 2.0

        scene kitchen day
        with dissolve

        "We both race down and are met with what we feared the most."

        show Hikari
        with dissolve

        h "S-Sayaka, stop!"

        play music "bgm/mischiefintro.ogg" fadein 2.0
        queue music "bgm/mischiefloop.ogg"

        hide Hikari
        $ sayaface='smiling'
        $ sayapose='school_1'
        $ yuzuface='normal'
        $ yuzupose='school_1'
        show Sayaka at left
        show Yuzuki at right
        with dissolve

        "Sayaka and Yuzuki are in the kitchen.{w} Making...{w}something.{w} Maybe it started out as a bowl of cereal at some point?{w} I'm really not sure anymore."

        s "Ooh, and hand me that, and that.{w} And we've gotta get some of this in there, too!"

        y "Interessant.{w} Ich wusste nie, dass du so ein Auge für diese Dinge hast, Sayaka."

        "Yuzuki responds calmly as she hands over whatever Sayaka instructs, only further adding to the mess.{w} She acknowledges me with a nod of her head, before returning to the mayhem."

        "Since we started hanging out, it's been a gradual process of her opening up more to us.{w} She's still pretty quiet most of the time, and won't dive into many conversations, but I think she enjoys our company."

        "It must be tough for her to adjust to things after she's finally obtained the friends she so desired for all these years."

        "I'm sure it won't be long until she's out of her shell with Sayaka and Hikari at the helm, though.{w} They seem to be able to bring out the best in people."

        "I greet her back with a nod of my head, but my eyes are quickly fixed to Sayaka, who is a high-level threat at the moment."

        "Our desperate cries go unheard.{w} They're having way too much fun here."

        $ sayaface='happy'
        show Sayaka

        s "Now then, I'm sure this is supposed to go in here too.{w} ...Probably!"

        hide Sayaka
        hide Yuzuki
        show Hikari at center
        with dissolve

        h "Kenta...{w} Sie hört nicht auf Vernunft.{w} Hab ich die Erlaubnis um...?"

        p "B-Bitte, mach es!"

        stop music fadeout 2.0

        $ hikaface='angry'
        show Hikari

        h "Sayaka, bleib zurück!"

        $ sayaface='shocked'
        show Sayaka at left
        show Hikari at right
        with dissolve

        "Hikari leaps into action and slides over the counter, almost like an action hero would do, before she shoots a bolt of magic from her fingertips, evaporating the foul substance that Sayaka might have called 'breakfast'."

        $ hikaface='normal'
        $ hikapose='school_2'
        show Hikari
        with dissolve

        h "Phew.{w} Krise abgewendet."

        s "W-wahh!{w} What the heck was that for?"

        $ hikaface='angry'
        show Hikari

        h "Das weißt du genau!"

        $ sayaface='smiling'
        show Sayaka

        play music "bgm/everydayintro.ogg" fadein 2.0
        queue music "bgm/everydayloop.ogg"

        "Sayaka sighs and flaps her arms in defeat."

        s "I was just trying to be nice and prepare breakfast for you guys, while you were being all lovey-dovey upstairs."

        $ hikaface='shy'
        show Hikari

        h "L-lovey-dovey?{w} Sayaka, ich denke du hast--"

        $ sayaface='joking'
        show Sayaka

        s "Aww, you don't have to hide it from me.{w} I can always pick up on these sorts of things.{w} Just say the word, and Yuzuki and I will head off early and give you two some time alone."

        $ hikaface='embarrassed'
        show Hikari

        h "S-Sayaka, ich werde..."

        "Hikari is practically shaking at this point, her entire face flush with either anger or embarrassment.{w} Maybe...{w}both?"

        hide Sayaka
        show Hikari at center
        with dissolve

        "Apparently proud of herself, Sayaka skips out of the kitchen with Yuzuki in tow."

        p "Nun.{w} Äh.{w} Sieht aus, als müssten wir uns auf dem Weg zur Schule irgendwo was zu essen kaufen."

        p "Ähh ...{w} H-Hikari?"

        "Hikari hasn't said anything since Sayaka left.{w} She simply stands there.{w} Like a statue."

        h "S-Sind...wir..."

        p "Hmm?"

        "She mumbles, just barely audible as I lean in closer and strain my ears."

        h "Sind wir wirklich...{w}l-lovey-dovey...?"

        p "Ähh.{w} Ich weiß jetzt echt nicht, wie ich darauf antworten soll.{w} {i}Sind{/i} wir das?"

        "I mean, we've definitely gotten a lot closer to each other this past week, after the resealing."

        "She's been a lot nicer to me, and has always tried her best to drag me out of Sayaka's grasp during the school breaks.{w} Which is a tough feat to do sometimes.{w} I think my arms might be just that extra little bit longer than before..."

        $ hikaface='shy'
        $ hikapose='school_1'
        show Hikari
        with dissolve

        h "Ich...{w}Ich meine...{w} Wenn du {i}willst{/i} das wir--"

        "She lets out a yelp and scrubs her hands through her hair frantically, catching me off-guard."

        h "Ahh!{w} N--Nein!{w} Was sage ich da?!{w} Es ist Sayaka...{w} Sie kommt wirklich zu mir!"

        h "Kenta, I-Ich hoffe du hast das nicht gehört..."

        "I offer her a smile, to reassure her.{w} Sayaka can say what she wants, but I think we both already know what we are."

        p "Hikari, schon gut.{w} Mach dir keine Sorgen.{w} Ich bin glücklich mit der momentanen Situation."

        p "Lass es uns einfach, äh, langsam angehen, okay?{w} Ignorier Sayaka einfach."

        $ hikaface='normal'
        show Hikari

        h "..."

        "She nods.{w} Phew.{w} I was worried I might have said something wrong there.{w} You can never know for sure with Hikari!"

        p "Also vergessen wir das Ganze erstmal und holen wir uns was zu frühstücken!"

        h "Ja.{w} Das hört sich gut an."

        p "Okay, Mädels, wir--häh ...?"

        "Sayaka and Yuzuki are already gone.{w} She really did give us time alone!"

        p "Wir sollten uns wohl besser beeilen.{w} So wie ich Sayaka kenn, ist sie wahrscheinlich schon meilenweit voraus."

        hide Hikari
        with dissolve

        "I start to slip on my shoes, but something tugs at my sleeve."

        p "Hikari ...?"

        $ hikaface='smiling'
        show Hikari at center
        with dissolve

        "She has a bashful look about her."

        h "Können wir vielleicht in unserem eigenen Tempo gehen??{w} Ich denke, ihnen wird's auch gut gehen, ohne uns."

        "Saying that, she hooks her arm around mine."

        p "O-Oh.{w} Äh, okay.{w} Klar, kein Problem!"

        "I'm still struggling to adapt to this new Hikari, but I think I'm getting there."

        "Arm in arm, we head out the front door, ready to tackle whatever challenges might await us."

        stop music fadeout 2.0

        scene bg white
        with wake



    if sayaka == hikari:


        "..."

        "The knock is shortly followed by another one, and another one."

        h "Sayaka, ich bin mir sicher er hat es schon gehört!"

        s "Nonsense, you can never be too careful."

        "Hmm, I really wonder who it could be..."

        "I say nothing, just to see what will happen."

        s "Hmm?{w} Nothing?{w} Maybe he really is asleep, still?"

        "{i}Thump, thump, thump.{/i}{w} She hammers the door once more."

        h "Denkst du er ist okay...?{w} Er war wirklich müde, als wir uns letzte Nacht trennten."

        "That's because I don't think the pair realise just how exhausting they've become lately."

        "Don't get me wrong, I'm happy they've stuck around for a little longer..."

        "But, after the resealing, they've become {i}way{/i} more competitive.{w} I'm really not sure what they're trying to prove anymore."

        s "Hmm...{w} Now that you mention it, he really did look pale the other day.{w} Maybe he got afflicted with some kind of deadly illness and didn't want to worry us?"

        h "W-Was?!"

        "The door handle rattles.{w} But there's some hesitation."

        h "Aber wenn er nur schläft...{w} Ist es wirklich okay, für uns da reinzufahren?"

        s "Sure it is!{w} I do it all the time.{w} Have you ever seen him sleeping, Hikari?{w} It's so adorable!{w} Here, I've got pictures I can show you."

        "...I feel so violated.{w} I'm glad I actually am awake at this point."

        h "Sayaka!{w} Du hättest wirklich nicht--awww..."

        s "I know, right?{w} I can't tell you how tempted I was to draw on his face."

        h "W-Wie auch immer!{w} Du lenkst mich ab.{w} Ich muss nachgucken ob es ihm gutgeht!"

        s "Maybe I want to check {i}more!{/i}"

        h "Hör auf zu schubsen, oder du wirst--"

        $ sayaface='shocked'
        $ sayapose='school_1'
        $ hikaface='shocked'
        $ hikapose='school_1'
        show Sayaka at left
        show Hikari at right
        with dissolve
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"

        "The door swings open and the pair come tumbling in.{w} They really do make an entrance sometimes."

        p "Ähh ...{w} Guten Morgen?"

        $ sayaface='smiling'
        show Sayaka

        s "Oh, hey, Kenta!"

        "Sayaka speaks from under Hikari, greeting me casually."

        $ hikaface='angry'
        show Hikari

        h "Warte, du warst wach?{w} Warum hast du nicht's gesagt?!{w} Weißt du wie besorgt wir waren?"

        p "Ahh ..."

        $ hikaface='scared'
        show Hikari

        "Hikari opens her mouth to scold me further, but Sayaka catches her off-guard as she leaps to her feet."

        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Maybe he just doesn't like you, Hikari, and was waiting for you to give up so we could have our alone time?"

        $ hikaface='angry'
        show Hikari

        h "A-absurd!{w} Und woher weißt du dass es nicht andersrum ist?!"

        $ sayaface='happy'
        $ sayapose='school_1'
        show Sayaka
        with dissolve

        s "Well, come on.{w} Have you {i}seen{/i} me?"

        "She strikes a pose she must deem 'sexy', but if anything it looks like she has a bad knot in her back."

        $ hikapose='school_2'
        show Hikari

        "Hikari is less than amused, and gives her a forceful shove which sends her toppling to the ground."

        $ sayaface='shocked'
        show Sayaka

        s "W-wahh!"

        p "Kommt schon, es ist noch zu früh zum Kämpfen ...{w} Kann das nicht bis zum Frühstück warten?"

        $ sayaface='shocked'
        $ hikaface='shocked'
        show Sayaka
        show Hikari

        "Both of them light up at the mention of breakfast.{w} Ohh, maybe I should have--"

        $ hikaface='smiling'
        show Hikari

        h "Gute Idee!{w} Ich werde etwas für uns machen, Kenta!"

        $ sayaface='angry'
        show Sayaka

        s "Hey, I'm the master chef here, {i}I{/i} should be doing the cooking!"

        hide Sayaka
        hide Hikari

        "Before I can say anything further, the pair of them barrel out of the room, neck and neck.{w} Oh god."

        stop music fadeout 2.0

        scene kitchen day
        with dissolve

        "I quickly follow them down, only to find I'm too late."

        "They're both in the kitchen, working on their own things as they frantically contest for space and utensils.{w} This is a nightmare."

        play music "bgm/mischiefintro.ogg" fadein 2.0
        queue music "bgm/mischiefloop.ogg"

        $ sayaface='angry'
        $ hikaface='angry'
        show Sayaka at left
        show Hikari at right
        with dissolve

        h "H-hey, ich wollte das benutzen!"

        $ sayaface='joking'
        show Sayaka

        s "You snooze, you lose!"

        $ hikaface='normal'
        show Hikari

        h "Fein.{w} Ich werde einfach das benutzen.{w} Ich denke es ist gut genug..."

        $ sayapose='school_2'
        $ sayaface='happy'
        show Sayaka
        with dissolve

        "I'm not even sure what either of them are trying to make.{w} It certainly doesn't look edible, though."

        $ sayaface='joking'
        show Sayaka

        "It doesn't help that I can see Sayaka sneaking extra salt into Hikari's meal while her back is turned.{w} That minx."

        "I suppose I should be flattered they're doing this for me, but...{w}yeah, no.{w} I'll die if I eat either of those...{w}creations."

        hide Sayaka
        hide Hikari
        with dissolve

        y "Guten Morgen."

        "Yuzuki greets me quietly from behind, almost giving me a heart attack.{w} Right.{w} I had almost forgotten she joins us in the mornings now."

        $ yuzuface='normal'
        $ yuzupose='school_1'
        show Yuzuki at center
        with dissolve

        p "A-Ah.{w} Guten Morgen."

        y "Das ist...{w}interessant."

        "She watches over the spectacle with a blank look, the kitchen becoming more and more of a mess with each passing second."

        "Since we started hanging out, it's been a gradual process of her opening up more to us.{w} She's still pretty quiet most of the time, and won't dive into many conversations, but I think she enjoys our company."

        "It must be tough for her to adjust to things after she's finally obtained the friends she so desired for all these years."

        "I'm sure it won't be long until she's out of her shell with Sayaka and Hikari at the helm, though.{w} They seem to be able to bring out the best in people."

        p "Interessant ist ein Wort dafür ..."

        hide Yuzuki
        $ sayaface='happy'
        $ sayapose='school_2'
        $ hikaface='shocked'
        show Sayaka at left
        show Hikari at right
        with dissolve

        stop music fadeout 2.0

        s "Aaaand...{w}done!"

        h "W-Was?!{w} Uh, ich auch!"

        $ hikaface='angry'
        show Hikari

        "Hikari mashes one last thing into her meal as she says so.{w} An entire egg.{w} Shell and all."

        p "Das ist, äh ...{w} großartig."

        $ sayaface='smiling'
        $ hikaface='normal'
        show Sayaka
        show Hikari

        s "So, so, so...{w} Whose meal do you want to eat?"

        "She proudly presents her...{w}something...{w}with a beaming smile.{w} Hikari seems more reserved, as if she might actually have some awareness about how bad the meal she's made is."

        p "Ohh ...{w} Wisst ihr was?{w} Ich hab gar keinen Hunger.{w} Ich wollte es euch ja eigentlich schon vorher sagen, aber ihr hattet es ja so eilig."

        $ sayaface='normal'
        $ sayapose='school_1'
        show Sayaka
        with dissolve

        s "Aww...{w}really?"

        p "Und das ist echt schade, denn das hier sieht echt aus wie ...{w} Irgendwas."

        s "Maybe we can wrap it up, and you can try some later?{w} Or we could take some with us to school, or--"

        $ sayaface='scared'
        show Sayaka

        p "Nein!"

        s "H-huh?"

        "I catch her off-guard with my sudden, desperate yell.{w} {i}Anything{/i} but that."

        $ sayaface='smiling'
        show Sayaka

        s "Well.{w} Fine."

        play music "bgm/everydayintro.ogg" fadein 2.0
        queue music "bgm/everydayloop.ogg"

        "She huffs a sigh of defeat.{w} It doesn't last long, however, before her gaze settles on Yuzuki."

        $ sayaface='happy'
        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Ah, YuzukI!{w} You're still hungry, right?{w} How about you try some!"

        hide Sayaka
        hide Hikari
        $ yuzuface='scared'
        show Yuzuki
        with dissolve

        y "..."

        "She makes a complicated face.{w} I think she's struggling to think of what to do in this social situation, as to not lose her newfound friends."

        y "Ich..."

        $ yuzuface='normal'
        show Yuzuki

        y "Ich passe.{w} Tut mir Leid."

        "She looks to me, as if wondering if this was the right move to make.{w} I give her a small nod.{w} If you enable Sayaka and her madness, things would only get worse!"

        hide Yuzuki
        with dissolve

        "Sayaka and Hikari both leave the kitchen, caring little for the mess they left in their wake.{w} Great.{w} I wonder who's going to be expected to clean that up, huh?"

        $ sayaface='smiling'
        $ sayapose='school_1'
        $ hikaface='normal'
        $ hikapose='school_1'
        show Sayaka at left
        show Hikari at right
        with dissolve

        s "Oh well."

        h "Vielleicht war es das Beste?"

        $ sayaface='happy'
        show Sayaka

        s "Yeah.{w} Things only would have ended in tears the moment Kenta declared my cooking better than yours."

        "...I'd have to be alive to declare such a thing."

        $ hikaface='angry'
        $ hikapose='school_2'
        show Hikari
        with dissolve

        h "Also ob!{w} Ich denke mein's hätte gewonnen!"

        "They butt heads again.{w} Seriously.{w} Can we not go five minutes without this?"

        p "Ähh.{w} Na kommt schon.{w} Ab in die Schule."

        $ hikaface='smiling'
        $ hikapose='school_1'
        $ sayaface='smiling'
        $ sayapose='school_2'
        show Hikari
        show Sayaka
        with dissolve

        "The aggression in their eyes quickly melts as they turn back to face me."

        s "Good idea!{w} You should follow me, Kenta, I know a really good shortcut!"

        "She bounds over and grabs hold of my hand, giving me no say in the matter."

        p "Äh ..."

        $ hikaface='embarrassed'
        show Hikari

        h "I-Ich weiß einen noch kürzeren Schnitt!"

        "That doesn't even make sense!"

        "Hikari takes a firm grasp of my other hand as the pair contest for me, fire in their eyes."

        p "Das muss echt nicht sein, oder?{w} Wollten wir nicht sowieso alle gemeinsam zur Schule gehen?"

        "...They don't listen."

        hide Sayaka
        hide Hikari
        with dissolve

        "They continue to tug at me every which way as we head out the front door, Yuzuki calmly following behind."

        s "You know...{w} It'll be even faster if we fly!"

        h "Nein!{w} Es wird am schnellsten sein, wenn wir {i}diesen{/i} Weg fliegen!"

        p "Mädels, wenn ihr so weitermacht, reißt ihr mich noch auseinander!{w} Arghhh!"

        stop music fadeout 2.0

        scene bg white
        with wake



    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
