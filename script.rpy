


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

    "In diesem Gefilde ist es so finster, dass ich nicht einmal meine Hand vor meinem Gesicht sehen kann."

    "Die Geräuschkulisse der Umgebung ist ebenso fehlend wie das Geräusch meiner Schritte."
    
    "Selbst meine verzweifelten Schreie werden unverzüglich von der Dunkelheit verschluckt, sobald sie meinen Mund verlassen."

    "Ein Ödland des Nichts sozusagen.{w} Verbringt man eine längere Zeit hier, fängt man noch an, an seiner eigenen Existenz zu zweifeln."

    "Und trotz dieses erstickenden Gefühls, weiß ich, dass ich nicht allein bin."

    "Mich beobachtet etwas.{w} Mich verfolgt etwas.{w} Aus den Schatten."

    "Ich kann nicht mit Sicherheit sagen, was es ist, aber hin und wieder sehe ich etwas am äußersten Rand meines Blickfelds."

    "Ein Paar brennender, strahlender Augen, die auf mich fixiert sind.{w} Sie hassen mich.{w} Sie verabscheuen mich.{w} Eine überwältigende Ausstrahlung von Feindseligkeit geht von ihnen aus."

    "Ich weiß, dass sie danach lechzen, über mich herzufallen, aber irgendwas hält sie zurück.{w} Eine Kraft, die sie wahrlich verachten."
    
    "Es sind unsichtbare Ketten, die sie von ihrer Absicht abhalten und in ihren Bewegungen einschränken."

    "Anfangs, als ich anfing, von diesem Ort zu träumen, waren die Augen noch weit entfernt und sahen aus wie flimmernde Sterne."

    "Aber mit jeder Nacht, die verging, kamen sie näher, und das Leuchten der Augen wurde immer stärker.{w} Ich schätze, die Kraft, die sie zurückhält, wird allmählich schwächer."

    "Was wird passieren, wenn mich ...{w} diese Augen ...{w} erreichen?{w} Ich erschaudere, wenn ich daran denke."

    "Ich weiß, es ist nur ein Traum, von daher sollte ich keine Angst haben ...{w} aber alles, was ich hier erlebe, wirkt so lebendig."
    
    "Keiner der Schleier, die man sonst aus einem Traum kennt, scheint hier zu existieren.{w} Ich nehme alles klar und deutlich wahr."

    "Ich kann die stagnierende, eiskalte Luft um mich herum spüren, weshalb mir immer wieder ein Schauer über den Rücken läuft."

    "Da ich so an diesen Traum gewöhnt bin, weiß ich, wie er enden wird."
    
    "Ich werde für eine scheinbare Ewigkeit durch die Dunkelheit waten und nie etwas finden, bis endlich der Morgen anbricht und mich aus diesem Albtraum reißt."

    "Zumindest ...{w} hat er für gewöhnlich so geendet."

    "Aber heute ist etwas anders."

    "Jene hasserfüllten Augen, die sich bisher vor meinem Blick zu verstecken versucht hatten ...{w} sind plötzlich unmittelbar vor mir."

    "Sie waren noch nie zuvor so nahe.{w} Noch nie zuvor habe ich sie so sehr angestarrt."

    "Ihr durchdringender Blick fesselt mich am Boden fest und ein stechender Schmerz drängt sich durch mich hindurch.{w} Ich kann mich nicht bewegen.{w} Ich kann nicht atmen."

    "Und dann, aus der Dunkelheit heraus, breitet sich plötzlich ein schiefes Lächeln aus, welches genauso finster ist wie die Augen."

    stop music fadeout 8.0

    dq "So nah.{w} Ich kann die Freiheit wahrlich {i}schmecken{/i}{w} ... Nicht mehr lang.{w} Genieße die Ruhe, solang du noch kannst, Junge, denn deine Tage sind gezählt."

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

    "Meine Eltern sind das, was man auch gern als {w}Workaholics{w} bezeichnet. Das heißt, sie verbringen mehr Zeit in ihrer Arbeit als zu Hause."
    
    "Ich sehe sie nur abends, und sobald wir da mit dem Essen fertig sind, geht auch schon wieder jeder schlafen."

    "Versteh mich nicht falsch. Ich verstehe, dass sie arbeiten müssen, dass es uns gut geht, daher hasse ich sie auch nicht.{w} Es ist bloß so ...{w} Ich weiß nicht so genau ... Einsam?"

    "Aber na ja.{w} Es bringt nichts, sich darüber Gedanken zu machen.{w} Es ist schon seit Jahren so, also keine Ahnung, warum ich jetzt wieder daran denke!"

    "Das Gute an der ganzen Sache ist, dass ich lernen musste, wie man kocht.{w} Echt wahnsinnig, wie schnell man so was lernt, wenn man mal kurz davor ist, dem Hungertod zu erliegen!"

    "Ich glaube nicht, dass ich noch genug Zeit habe, um mir etwas Prunkvolles zum Frühstück herbeizuzaubern, von daher mache ich mir nur Toast.{w} Mit Toast liegt man nie falsch."

    "...Okay, man {i}könnte{/i} damit falsch liegen.{w} Plötzlich werden traumatische Erinnerungen an jenen Morgen, als mein Toast in Flammen aufgegangen ist, in mir wach.{w} ... Ah, das war ein Tag."

    "Aber ich habe von meinen Fehlern gelernt.{w} Es wird kein zweites, äh ... drittes Mal mehr passieren!"

    with Pause(2.5)

    "Nachdem ich meinen leicht verkohlten Toast verschlungen habe, werfe ich mir meine Tasche über die Schulter und gehe zur Haustür."

    "Bevor ich aus dem Haus gehe, werfe ich noch einen Blick darauf.{w} Irgendwie einsam, wenn dich keiner verabschiedet ...{w} Aber ich habe es ja schon einmal gesagt, es ist morgens schon seit langer Zeit so."

    scene town street day with dissolve

    "Die Sonne steht hoch am Himmel, die Vögel zwitschern über mir und Scharen von Schülern überholen mich auf ihrem Weg zur Schule."

    "...Es ist alles so schrecklich."

    "Ich bin nicht gerade ein Morgenmensch, von daher kann ich überhaupt nicht verstehen, wie manche Leute schon in aller Früh so fröhlich sein können ..."
    
    "Ich meine, in meinem Fall braucht es all meine Willenskraft, um überhaupt mal einen Fuß vor den anderen zu setzen."

    "Ich muss nur hoffen, dass sich die Energie, die ich beim Frühstück zu mir genommen habe, bald bemerkbar macht. Hoffentlich noch, bevor ich die Schule erreiche."

    with Pause(2.5)

    "..."

    stop music fadeout 8.0

    with Pause(2.5)

    "Während ich meinen Kopf unten halte und meine Augen an den Boden geklebt sind, bemerke ich plötzlich, dass die lebhafte Atmosphäre auf einmal verschwunden ist."

    "Die Stille hat die Oberhand gewonnen - das einzige Geräusch weit und breit ist das meiner Schritte.{w} Es geht überhaupt kein Wind.{w} Häh ...{w} Das ist schon ein bisschen komisch."

    "Als ich meinen Kopf erhebe, erblicken meine Augen etwas Beunruhigendes."

    "Die Straße ist menschenleer."

    "Keine Schüler.{w} Keine Autos.{w} Selbst das Gezwitscher der Vögel ist auf einmal verschwunden."
    play music "bgm/ominousintro.ogg" fadein 2.0 
    queue music "bgm/ominousloop.ogg"
    "Was ...?"

    "In der Hoffnung, wenigstens irgendjemanden zu treffen, eile ich vorwärts."

    "Sogar die Sonnenstrahlen scheinen verblasst zu sein, wodurch alles in einen düsteren Farbton getaucht wurde.{w} Aber ...{w} im Himmel ist weit und breit keine Wolke zu sehen."

    "Okay, das macht mich jetzt aber wirklich ein wenig verrückt.{w} Ich muss doch nur--"



    "Ein spaltender Schmerz schießt durch meinen Kopf und stoppt meine Bewegungen.{w} Wie ein glühender Schürhaken, der durch meinen Schädel gestoßen wird."

    "Kopfschmerzen?{w} Jetzt?"

    "Das ergibt doch alles keinen Sinn!"

    "Verzweifelt versuche ich, mich aufrecht zu halten, während ich eine Hand an meinen Kopf halte."
    
    "Im Gegensatz zu den Kopfschmerzen am Morgen, die immer schwächer werden, werden diese hier immer schlimmer!"



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

    "Es gibt nur eine Sache, die ich in einem solchen Augenblick tun kann--"

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

            "Die Angst vor dem bevorstehenden Tod betäubt meine Gliedmaßen und zerstreut meinen Verstand so sehr, dass ich meinem Körper keine Befehle mehr erteilen kann ..."
            
            "Ich kann jetzt nur noch meinen Kopf umdrehen und dem Tod in die Augen sehen."

            "Es ...{w} Es ist aus."

    stop music fadeout 5.0 
    scene bg white
    with flash

    "Kurz bevor mich das Monster verspeist und meinem Leben ein Ende setzt, dringt ein strahlend helles Licht in mein Blickfeld, welches sowohl mich als auch das Monster verschlingt."

    "Das Monster bleibt regungslos stehen und schreit, ehe es vor meinen Augen 'verdampft'."

    "...{w}Was ...{w} Was zum Teufel ist da gerade passiert?"

    cg "Meine Güte, das war echt knapp!{w} Alles in Ordnung?"
    play music "bgm/magicalgirlintro.ogg" fadein 6.0
    queue music "bgm/magicalgirlloop.ogg"
    "Eine fröhliche Stimme zwitschert.{w} Ein willkommenes Geräusch nach dem Schrecken ...{w} dieses Monsters."

    tg "Rede nicht mit ihm!{w} Wir müssen gehen, bevor--"

    "Und dann eine weitere Stimme, die weniger ...{w} fröhlich klingt.{w} Genauer gesagt klingt sie sogar eher verägert."

    scene cg1 with wake


    "Kurz darauf verlasst das Licht, was meine Retter zum Vorschein bringt."

    "...Wobei ich ...{w} das echt als {i}Letztes{/i} erwartet hätte."

    "Zwei Mädchen, in etwa in meinem Alter, stehen vor mir."

    "Ich blinzle ein paar Mal und wische meine Augen aus, in der Hoffnung, dass all das ein wenig mehr Sinn ergeben würde.{w} Das kann unmöglich wahr sein."

    "Um ehrlich zu sein, glaube ich, dass mir meine Augen jetzt gerade einen größeren Streich spielen als sie es vorhin getan haben, als das Monster da war!"

    "Diese Waffen und Kleidung, die direkt aus einem Fantasy-Buch stammen könnten, sind zu viel für mein kleines Gehirn."

    p "Wa...{w} Was zur Hölle war das?!"

    cg "Ein Schatten."

    "Das fröhlichere der beiden Mädchen antwortet mir unverblümt und entspannt sich dabei wenig."

    p "H-Häh?"

    "Das war jetzt die Erklärung?{w} Ich blicke hinunter zu meinen Füßen, wo sich mein eigener Schatten erstreckt, aber das Mädchen fängt an zu lachen."

    cg "Nicht dein eigener Schatten, du Idiot!{w} Das Ding, worum wir uns gerade gekümmert haben, bezeichnen wir als Schatten."

    cg "Die physische Manifestation all des Hasses und der negativen Emotionen, die jemand in sich trägt."

    cg "Normalerweise sind sie tagsüber nicht so aggressiv, aber ...{w} Kurzum, du hattest echt Glück!"

    cg "Wir erwischen sie eigentlich immer, bevor sie in deine Nähe kommen, aber der hier hat uns echt überrascht.{w} Ich bin echt froh, dass wir es noch geschafft haben!"

    cg "Du bist doch nicht verletzt, oder?"

    p "Nein, alles gut, aber--"

    tg "Als ob die Dinge nicht schlimm genug wären, dass wir uns ihm offenbaren mussten, redest du mit ihm auch noch über Sachen, die kein normaler Mensch wissen sollte.{w} Hast du den Verstand verloren?!"

    "Das aggressivere Mädchen, dessen Ausdruck immer düsterer wurde, während die andere sprach, mischte sich plötzlich ein. Anscheinend konnte sie es nicht länger ertragen."

    cg "Aww, aber er sieht so verwirrt aus!{w} Und denkst du nicht, dass es jetzt, wo er die Schatten schon aus erster Hand erlebt hat, ein {i}wenig{/i} zu spät ist, um wieder abzuhauen?"

    tg "..."

    "Mit verengten Augen starrt sie uns an.{w} Man erkennt, dass sie eindeutig wütend ist ...{w} aber ich glaube nicht, dass sie etwas dagegen unternehmen kann."

    cg "Siehst du?{w} Du machst dir zu viele Sorgen!{w} Wir erzählen ihm nur, was er wissen muss, mehr nicht!"

    "Das fröhliche Mädchen schenkt mir mit einem Funkeln in ihren Augen wieder ihre Aufmerksamkeit."

    scene town street day
    $ sayapose='magical_1'
    $ hikapose='magical_1'
    $ hikaface='normal'
    $ sayaface='smiling'
    show Sayaka at left
    show Hikari at right
    with dissolve

    cg "Genau ... Also Kenta, wo waren wir?"

    p "Äh, wir waren--"

    "Warte ..."

    p "Woher kennst du überhaupt meinen Namen?!"

    $ sayaface='shocked'
    show Sayaka

    cg "Hm?{w} Oh ...{w} Ups!"

    "Mit einer Hand verdeckt sie ihren Mund - so, als wolle sie versuchen, das Gesagte rückgängig zu machen.{w} Es häufen sich immer mehr Fragen an, und ich habe noch immer keine einzige Antwort erhalten!"

    with hpunch
    $ hikapose='magical_2'
    $ hikaface='angry'
    $ sayaface='joking'
    show Sayaka
    show Hikari with dissolve

    tg "Du Idiot!"

    "{i}Bam!{/i} Das ernstere Mädchen 'schlägt' mir ihrer Faust auf den Kopf des anderen Mädchens, die gerade in einer 'Tut mir leid, mein Fehler'-Art und Weise ihre Zunge ausstreckt."

    p "Ihr kennt mich also?"

    $ sayaface='smiling'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka
    show Hikari with dissolve

    "Ich hab sie noch nie in meinem Leben gesehen.{w} Und so wie sie aussehen, würde ich mich {i}auf jeden Fall{/i} an sie erinnern."

    $ sayapose='magical_2'
    show Sayaka with dissolve

    cg "Na ja, wir kennen {i}dich{/i} nicht persönlich, aber wir beobachten dich schon eine Weile.{w} Du wurdest in letzter Zeit ziemlich beliebt!"

    p "Ich ...?"

    "Was hab ich in meinem Leben bloß falsch gemacht, dass mir so viel Aufmerksamkeit geschenkt wird?{w} Soviel ich weiß, bin ich doch nur ein normaler Schüler.{w} Der ein durchschnittliches Leben führt ..."
    
    "Und normale Dinge macht.{w} Wobei, nach all diesen Ereignissen trifft das wohl alles nicht länger zu."

    cg "Mmhmm.{w} Ich kann nicht zu viel verraten, weil du weißt schon, streng geheim und so, aber sagen wir mal so ...{w} Es liegt nicht in unserem Interesse, dass dir was zustößt."

    $ sayaface='happy'
    show Sayaka

    cg "Du glaubst doch sowieso nicht, wie viel Mühe wir uns geben, um dich zu beschützen!{w} Ich bin ehrlich gesagt ziemlich erleichtert, dass wir uns endlich kennenlernen, so lernst du zumindest unsere Arbeit zu schätzen."

    "Sie strahlt mich an und lehnt sich ein wenig zu nah an mich heran."

    "Ich ...{w} Sie konfrontiert mich mit so viel, dass ich kaum mehr klar denken kann."

    p "{i}Wer{/i} seid ihr überhaupt?"

    $ sayaface='normal'
    show Sayaka

    cg "Hmmm ..."

    "Sie fängt an nachzudenken.{w} Ich schätze, sie wählt die Worte, die sie gleich sagen wird, sorgfältig aus, um zu verhindern, dass ihre Partnerin wieder ausflippt."

    $ sayaface='happy'
    $ sayapose='magical_1'
    show Sayaka

    cg "Betrachte uns als deine Schutzengel, okay?"

    "Als sie das sagt, macht sie mit ihrem Bogen eine schwungvolle Bewegung, woraufhin dieser kurz darauf zwischen ihren Fingern zerbricht."
    
    "Wenige Augenblicke später bilden sich diese Scherben hinter ihrem Rücken wieder zusammen, bis sich ein paar Flügel gebildet hat."

    "Die Flügel, die zwar nicht fest mit ihr verbunden sind, scheinen zumindest zu funktionieren. Oder sagen wir so, sie bewegen sich im Wind zumindest hin und her."

    "Warte, sind das buchstäblich Engel?!"

    p "Um mal ein paar Dinge abzuklären ..."

    p "Fangen wir mal von vorne an: das Ding, das mich gerade angegriffen hat - dieses Monster da - nennt ihr Schatten"

    $ sayaface='smiling'
    show Sayaka

    cg "Jup!"

    p "Und diese 'Schatten' jagen mich nun schon seit einer geraumen Zeit?"

    cg "Mmhmm!"

    p "Denn, wenn sie mich fangen ...{w} wär das offensichtlich 'nicht gut' ... Einfach so, aus nicht näher beschriebenen Gründen?"

    cg "Jup.{w} Ganz und gar nicht gut!"

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

            cg "Wirklich?"

            p "Ja.{w} Ihr habt sie nicht mehr alle."

            $ sayaface='shocked'
            $ hikaface='angry'
            show Sayaka
            show Hikari

            cg "W-Wir haben sie nicht mehr alle?!"

            "Meine Worte scheinen sie zu überraschen.{w} Vielleicht bin ich ein bisschen gemein, aber das ist die einzig plausible Erklärung!"

            p "Absolut durchgeknallt.{w} Ich weiß nicht, ob ihr nicht einfach nur Cosplayer seid und ich nicht nur in eine Vorführung gestolpert bin ...{w} aber das kann unmöglich real sein."

            "Es ist die einzige Schlussfolgerung, zu der mein Verstand kommt.{w} Sie hat doch wohl nicht wirklich erwartet, dass ich ihr den Mist mit dem 'Schutzengel' glaube, oder?{w} Hah!"

            p "Bleibt ruhig in eurer kleinen Fantasiewelt, aber haltet mich da bitte raus, okay?"

            hide Sayaka
            hide Hikari
            with dissolve
            stop music fadeout 5.0

            "Mit diesen Worten mache ich mich wieder auf in Richtung Schule.{w} Meine Fresse, haben mich die jetzt wirklich so lang aufgehalten?{w} Wenn ich Glück hab, komm ich noch vor dem Ende der ersten Stunde in die Schule!"

            cg "Hey, warte!{w} Das ist--"

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

            tg "Wirklich?{w} Ich meine ... wirklich?!{w} Bist du {i}wirklich{/i} ein so großer Idiot?!"

            p "I-Ich ... Äh ..."

            "Ich spüre, wie mich ihr Blick immer kleiner aussehen lässt.{w} Sie ist eindeutig noch gruseliger als das Monster!"

            tg "Es ist schon schlimm genug, dass wir uns zeigen mussten, aber jetzt tust du auch noch so, als wären wir verrückt?!"

            "Mit einem finsteren Blick ballt sie ihre Fäuse zusammen und hinterlässt den Eindruck, als würde sie am liebsten zuschlagen."

            tg "Ich weiß nicht einmal, warum wir uns um dich kümmern, wenn du uns so behandelst!{w} Vielleicht sollten wir das nächste Mal einfach zulassen, dass du gefressen wirst.{w} Hmph."

            $ hikapose='magical_2'
            $ hikaface='normal'
            show Hikari
            with dissolve

            "Sie verschränkt ihre Arme und dreht den Kopf zur Seite.{w} Sie gehört echt ...{w} zu der emotionalen Sorte."

            $ sayaface='shocked'
            show Sayaka at left
            show Hikari at right
            with dissolve

            cg "Wah!{w} Sag doch so was nicht!"

            "Das fröhliche Mädchen stolpert, als sie sich zwischen uns drängt, und wirft mir ein entschuldigendes Lächeln zu."

            cg "I-Ich bin sicher, sie hat es nicht so gemeint!{w} Sie wird nur manchmal ein bisschen griesgrämig."

            $ sayaface='angry'
            show Sayaka

            cg "Und du werd nicht so wütend auf ihn.{w} Es ist nur natürlich, dass er uns gegenüber anfangs skeptisch ist!"

            $ hikapose='magical_1'
            show Hikari
            with dissolve

            tg "Hmph, was auch immer.{w} Er ist wirklich so dumm, wie er aussieht."

            "Autsch ...{w} Ich {i}bin{/i} noch immer hier, nur damit ihr wisst!"

            $ sayaface='joking'
            show Sayaka

            cg "Oh?{w} Das hör ich zum ersten Mal.{w} Im Gegenteil, ich kann mich noch gut daran erinnern, dass du gesagt hast, er sieht ziemlich sü--"

            $ hikaface='embarrassed'
            $ sayaface='shocked'
            show Sayaka
            show Hikari
            with hpunch

            "{i}BAM.{/i} Da landet die Faust direkt im Gesicht des fröhlichen Mädchens.{w} Und dieses Mal war es ernst gemeint, denn sie hielt kein bisschen zurück.{w} Das muss echt wehgetan haben ..."

            tg "Halt dein Mund!{w} Soetwas habe ich nie gesagt!"

            $ sayaface='scared'
            show Sayaka

            cg "Wahh!{w} Okay, okay, schon gut!"

            "Meine Güte ...{w} Die beiden sind echt komisch.{w} Aber sie scheint es wirklich ernst gemeint zu haben.{w} Vielleicht war meine Entscheidung, sie als Verrückte abzustempeln, etwas voreilig."

            "Ich mein, sie sind verrückt, das stimmt schon, aber vielleicht steckt ja doch ein Fünkchen Wahrheit darin.{w} Die Existenz dieses Monsters kann ich schließlich auch nicht leugnen, so sehr ich es auch will."

    $ sayaface='smiling'
    $ hikaface='normal'
    show Sayaka
    show Hikari

    p "Okay, also, äh, was passiert jetzt?"

    cg "Hmm."

    cg "Nun, da die Schatten aggressiver wurden, glaub ich kaum, dass wir wieder so weitermachen können wie bisher.{w} Das gerade eben war nur Glück, mehr nicht."

    "...Irgendwie gefällt mir diese Wortwahl nicht.{w} Kein bisschen."

    cg "Von daher trennen sich hier erstmal unsere Wege, aber merk dir, dass wir eine Auge auf dich werfen ... Von {i}ganz nah{/i}, okay?"

    $ sayaface='happy'
    show Sayaka

    cg "Tschüssi!"

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

    "Manchmal bin ich echt spät dran, und gelegentlich komme ich sogar erst nach dem Glockenläuten.{w} Das passiert meistens, weil ich verschlafe."
    
    "Aber dieses Mal hätte ich ja einen richtigen Grund, wäre ich zu spät gekommen!"

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

    teacher "Nun, äh, ich weiß, dass es etwas plötzlich ist, aber wir haben ab heute zwei neue Schüler, die sich unserer Klasse anschließen."

    "Schulwechsler?{w} Um diese Zeit?{w} Schon ein bisschen spät, die Schule zu wechseln, oder nicht?{w} Selbst der Lehrer scheint ein bisschen verwirrt zu sein, als er es ankündigt."

    "Und nicht nur einer, sondern {i}zwei{/i}?{w} Warum hab ich bloß das Gefühl ... dass hier etwas vor sich geht?{w} Fast so, als ob es irgendwie mit den Ereignissen vorhin in Zusammenhang steht?"

    "Hah.{w} Nein.{w} Das kann unmöglich sein."

    teacher "Ich möchte, dass der Einzug in die Schule so reibungslos wie nur möglich verläuft. {w} Äh, wie waren nochmal Ihre Namen?"

    cg "Ich bin Sayaka ... Freut mich, euch alle kennenzulernen.{w} Ich hoffe, wir kommen alle gut miteinander aus!"

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

    s "Die mürrische Person neben mir ist Hikari.{w} Komm schon, sag hallo!"

    $ sayaface='happy'
    show Sayaka

    h "H-Hey, l-lass das--"

    $ hikaface='embarrassed'
    hide Sayaka
    show Hikari at center
    with dissolve

    "Sayaka verpasst ihr einen spielerischen Schubs, woraufhin sie in die Mitte des Klassenzimmers stolpert und alle Aufmerksamkeit erregt."

    "Sie sieht aus, als hätte sie vergessen, was sie sagen wollte.{w} Auch ihr Gesicht wird allmählich immer roter.{w} Da hat wohl jemand Lampenfieber."

    h "I-Ich bin ... {size=12}Hikari ...{w} F-Freut mich, euch k-kennenzulernen ...{/size}"

    $ hikaface='shy'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "Sie nuschelt kurz etwas vor sich hin, ehe sie sich gleich darauf wieder umdreht und sich hinter Sayaka versteckt."

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Das war doch nicht schwer, oder?"

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

            "{i}Schon vergessen, dass du heute fast als Hundefutter geendet hättest?{w} Das wird nicht nochmal passieren, dafür sorgen wir!{w} Und wegen der Schule ...{/i}"
            
            "{i}Na ja ...{w}sagen wir so, wir können ziemlich überredend sein.{w} Eh-heh-heh.{/i}"

            "...Ernsthaft, wer schreibt heutzutage noch 'eh-heh-heh'?{w} Ach, scheiß drauf.{w} Sie hat mir zumindest geantwortet.{w} Einigermaßen."

            "Jetzt, wo ich darüber nachdenke, erinnere ich mich daran, dass auch der Lehrer ein bisschen verwirrt war, als er sie vorstellte."
            
            "Ich wette, sie haben ihre magischen Kräfte spielen lassen.{w} Der Gedanke ist schon irgendwie gruselig ..."

            "'Magie'.{w} Ich verwende dieses Wort so beiläufig.{w} Heißt das, ich akzeptiere damit ihre Existenz?{w} Und auch, wenn die Beweise für die Magie sprechen, werde ich vorerst dennoch skeptisch bleiben."
        "Hikari.":

            $ hikari += 1

            "Genau.{w} Es ist leichter, ihr den Zettel zu geben, da sie unmittelbar neben mir sitzt."

            "Mit nach vorne gerichteten Augen lehne ich mich ein wenig zur Seite und 'schubse' den Zettel auf ihren Tisch.{w} Nur knapp entkomme ich den wachsamen Augen des Lehrers.{w} Puh!"

            $ hikaface='normal'
            show Hikari at center
            with dissolve

            "Ich bin zuversichtlich, dass sie mir antworten wird.{w} Sie schaut mich seitwärts an und hebt den Zettel mit zwei Fingern auf ..."
            
            "Das kommt mir so vor, als würde sie glauben, sie hätte es mit einem verseuchten Zettel zu tun."

            "Sie bringt ihn in die Nähe ihres Gesicht, überfliegt ihn einmal und dann ..."

            $ hikaface='joking'
            show Hikari

            "...Zerknittert sie ihn und wirft ihn zu mir zurück.{w} ... Das war jetzt echt gemein."

            hide Hikari
            with dissolve

            "Was soll man dazu sagen ...{w} Das war ein Misserfolg.{w} Und ich habe das Gefühl, als würde der Lehrer nun vermehrt seine Aufmerksamkeit auf mich richten ..."
            
            "Daher ist es wahrscheinlich nicht mehr möglich, Sayaka ebenfalls noch zu fragen."

            "Ein bisschen verletzt von ihrer Zurückweisung, lasse ich mich nach vorne fallen und stütze meinen Kopf auf meiner Hand ab."

            "Wenn sie so drauf ist, sollte ich wohl vorerst versuchen, alle noch so kleinen Details zusammenzusetzen, und dann bei Gelegenheit mit ihnen reden."

            "Mal sehen ..."

            "Sie haben gesagt, sie wären meine 'Schutzengel', oder?"

            "Und dieser Angriff vorhin muss sie so sehr erschreckt haben, dass sie beschlossen haben, es wäre zu unsicher, sollten sie mich weiterhin aus der Ferne beobachten ...?"

            "Das ist zumindest die logischste Erklärung, die mir einfällt.{w} Mehr fällt mir momentan nicht ein, da sich die Eiskönigin dort drüben ja weigert, mit mir zu reden."


    stop music fadeout 4.0

    "Die erste Stunde des Tages vergeht elends langsam.{w} Ich kann mich überhaupt nicht konzentrieren, egal wie sehr ich es auch versuche."

    "Nach einer gefühlten Ewigkeit ertönt schlussendlich doch noch die Glocke.{w} Die erste Stunde ist endlich vorbei."

    "Vor der Pause haben wir aber noch eine Stunde. Und wäre das nicht schon schlimm genug, haben wir nächste Stunde auch noch Sportunterricht."
    
    "Und da Jungen und Mädchen getrennt turnen, kann ich sowieso nicht mit ihnen reden."

    "Argh, warum muss das alles so kompliziert sein?!"

    scene bg black
    with fade
    play music "bgm/everydayintro.ogg" fadein 1.0
    queue music "bgm/everydayloop.ogg"
    "Nachdem ich mir meine Sportsachen angezogen hab, stehe ich nun mit den anderen Jungs meiner Klasse am Schulhof."
    
    "Genauso wie in der ersten Stunde, konnte ich mich auch im Sportunterricht nicht wirklich konzentrieren."

    "Ich mache die Übungen mit ... mit der Begeisterung eines Zombies."

    "Den Rest der Stunde nehme ich nur noch verschwommen wahr, zumindest bis einige meiner Mitschüler zur Laufbahn schauen, wo gerade die Mädels unterwegs sind."
    
    "Vor lauter Unglaubwürdigkeit, fangen einige der Schüler sogar an, sich ihre Augen auszureiben.{w} Was ist daran denn so besonders?"



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

    "Einige dieser Mädchen sind - oder besser gesagt {i}waren{/i} - die besten der Klasse, wenn es ums Laufen geht, aber selbst die lässt sie alt aussehen."
    
    "Ich möchte nicht wissen, wie es sich anfühlt, von jemandem vorgeführt zu werden, der gerade mal einen Tag auf diese Schule geht."

    "Selbst meine Augen haben Probleme damit, mit ihrer Geschwindigkeit mitzuhalten.{w} Sie scheint mit jeder Runde schneller zu werden."

    "Das kann doch unmöglich ein Mensch sein, oder?"

    "Nach dieser übermenschlichen Leistung fange ich echt an, daran zu zweifeln.{w} Ich glaube, nicht mal die besten Sportler des Landes hätten eine Chance gegen sie!"

    "Und während Sayaka all die Aufmerksamkeit erregt, fehlt jemand - und zwar ihr mürrisches Gegenstück: Hikari.{w} Wenn man jetzt logisch nachdenkt ... Sollte sie nicht auch so schnell sein?"

    "Ich suche die Umgebung ab, kann sie aber nirgends finden.{w} Wo bist du bl--oh."

    "Hinter den Mädchen, die verzweifelt versuchen, mit Sayaka mitzuhalten, sehe ich noch jemanden mit einem sauren Gesichtsausdruck.{w} Sie ..."
    
    "Sie geht einfach nur, und wie immer sind ihre Arme dabei verschränkt.{w} Ich frage mich, ob ihre Arme aneinanderkleben?{w} Sie versucht doch nicht einmal zu laufen."

    "Anscheinend möchte sie wirklich nicht hier sein.{w} Das war wohl alles Sayakas Idee."

    teacher "Worauf starren Sie denn? {w} Weitermachen, los!"

    "Da wir anscheinend alle vergessen hatten, dass wir selbst Unterricht haben, bringt uns der Lehrer zurück in die Realität.{w} Vorbei ist's mit dem schönen Anblick."

    scene bg black
    with fade

    "Der Rest der Stunde vergeht ohne großartige Ereignisse, und dann endlich, {i}ENDLICH{/i} ... Mittagspause."

    scene classroom
    with fade



    "Ich beobachte, wie die beiden Mädchen ganz entspannt im Klassenzimmer mit anderen Schülern plaudern.{w} Ich hätte nicht gedacht, dass sie so schnell Freunde finden würden."
    
    "Aber nach dem, was Sayaka vorhin abgeliefert hat, ist sie wahrscheinlich sowieso Gesprächsthema der Stunde."

    $ sayaface='smiling'
    $ sayapose='school_1'
    show Sayaka at center
    with dissolve

    s "Oh, Kenta.{w} Hallo!"

    "Sie winkt und lächelt mir zu, aber meine Reaktion ist nicht mal annähernd so fröhlich."

    p "Okay, ja, hi.{w} Äh, können wir reden?"

    $ sayaface='normal'
    show Sayaka

    s "Hm?{w} Nur zu!"

    p "Nein, nicht hier, ich mein ... Können wir unter vier Augen reden?"

    $ sayaface='shy'
    show Sayaka

    "...Scheiße.{w} Das hat sich vielleicht etwas komisch angehört.{w} Aus irgendeinem Grund sehen mich manche Schüler schon schief an."
    
    "Sogar Sayaka tut so, als wäre sie überrascht, obwohl sie genau weiß, was ich meine!"

    s "Oh, das ist aber schon ein bisschen plötzlich!{w} Ich weiß nicht, was ich sagen soll ..."

    p "Komm schon, hör auf rumzualbern.{w} Ich möchte einfach nur mit euch reden, und das schon seid heute morgen."

    "Oh Gott ...{w} Es wird nicht besser, oder?{w} Irgendwie hab ich aus der Situation das wohl peinlichste Geständnis ever gemacht."

    $ sayaface='joking'
    show Sayaka

    s "Bist du immer so stürmisch, was Mädchen anbelangt, die du gerade getroffen hast?"

    "Sie kichert und streut noch mehr Salz in die bereits tiefe Wunde."

    "Na ja ...{w} Wenn sie es so haben will, dann bleibt mir wohl keine andere Wahl."

    "Dadurch mache ich mich vor all den anderen wahrscheinlich zum größten Idioten, aber ich brauche Antworten!"

    "Ich hole tief Luft.{w} Und dann ..."

    $ sayaface='shocked'
    show Sayaka
    with hpunch

    s "Wh-Wha--Hey, was machst du da?"

    "...Packe ich sie am Handgelenk und ziehe sie zur Tür hinaus, ob sie will oder nicht.{w} Wäre sie aber wirklich dagegen, dann könnte sie mich, angesichts der Vorführung vorhin, jede Sekunde zu Boden werfen."
    
    "Aber ich denke, sie albert gerade nur ein wenig herum."

    hide Sayaka
    with dissolve

    p "Und du kommst auch schön mit!"

    $ hikaface='shocked'
    show Hikari
    with dissolve

    h "Kyaa!{w} Wer hat gesagt, dass du mich anfassen darfst?!"

    hide Hikari
    with dissolve

    "Mit meiner zweiten Hand packe ich auch Hikaris Handgelenk.{w} Zum Glück leisten sie nicht allzu viel Widerstand."

    "Hikaris Beleidigungen ignorierend gehe ich weiter in Richtung Tür.{w} Ich muss nur ein stilles Örtchen finden, wo ich die beiden befragen kann.{w} Die Frage ist nur--"

    stop music fadeout 7.0

    p "Oof!"

    $ yuzupose='school_1'
    $ yuzuface='shocked'
    show Yuzuki
    with dissolve
    with hpunch
    with hpunch

    "Durch meine überschnelle Absicht, mit den beiden Mädchen das Klassenzimmer schnellstmöglich zu verlassen, stoße ich mit jemandem zusammen, der gerade durch die Tür kam."

    "Sie stolpert nach hinten und sieht ein wenig benommen aus.{w} Gott sei Dank sieht es nicht schlimm aus."

    p "Ahh, alles in Ordnung?{w} Tut mir leid."

    "Ich entschuldige mich bei ihr.{w} ... Wer ist das nochmal?{w} Sie muss aus meiner Klasse sein ...{w} Ich kann mich aber überhaupt nicht an sie erinnern."

    $ yuzuface='angry'
    show Yuzuki

    dg "...Schon gut."

    "Sie spricht in einer eiskalten Tonlage - ebenso eiskalt, wie ihre Augen, die auf mich fokussiert sind.{w} Ui.{w} Ich schätze, sie hat einen Grund, weshalb sie so verägert aussieht ... oder zumindest hoffe ich das."

    p "Ähh, o-okay."

    hide Yuzuki
    with dissolve

    "Nachdem ich sichergestellt habe, dass es ihr gut geht, konzentriere ich mich wieder auf Hikari und Sayaka.{w} Ich will mir gar nicht vorstellen, wie das für Außenstehende gerade aussieht."

    "...Und ich bin sicher, das Mädchen von vorhin starrt mir ebenfalls noch hinterher.{w} Ist sie etwa auf mich so wütend?{w} Ich mein, das war doch nur ein {i}Unfall{/i}."

    "Ach, ich muss mich jetzt auf wichtigere Dinge konzentrieren.{w} Und diese zwei Dinge halte ich gerade in meinen Händen."
    play music "bgm/magicalgirlintro.ogg" fadein 5.0
    queue music "bgm/magicalgirlloop.ogg"
    scene school roof
    with fade

    "Als wir am Schuldach auftauchten, bin ich froh, dass wir alleine sind.{w} Theoretisch verbringen hier viele Schüler ihre Pausen, aber praktisch gesehen ist der Ort nicht sehr beliebt. Umso besser für mich!"

    p "Okay, könnt ihr mir jetzt erstmal in aller Ruhe dieses Chaos hier erklären?"


    $ sayaface='happy'
    $ hikaface='angry'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "Ich lasse sie beide gleichzeitig los.{w} Sayaka hüpft fröhlich herum, während Hikari im Gegenzug an ihrem Handgelenk reibt und so tut, als hätte ich sie angegriffen."

    h "Wie wäre es, nächstes Mal zu fragen, bevor du jemanden anfasst?!{w} Du hast Glück, dass das ein öffentlicher Platz sind, sonst hätte ich dich in zwei Teile geschnitten!"

    s "Oh, das ist ja spannend!{w} Wird das jetzt eine dieser Liebeserklärungen, von denen ich so viel gehört habe?"

    $ hikaface='embarrassed'
    show Hikari

    h "H-Hä?{w} E-Eine L-Liebeserklärung?{w} Wer?{w} Wir beide?!"

    "Was zum Teufel denken die beiden überhaupt ...{w} Ich schüttle einfach nur meinen Kopf."

    p "Das ist kein Geständnis!{w} Ihr wisst genau, worum es geht!"

    "Ich kann spüren, wie mein Gesicht immer heißer wird.{w} Die beiden sind echt anstrengend."

    $ hikaface='shy'
    show Hikari

    "Sayaka lächelt mir schelmisch zu, ehe sie zu kichern beginnt.{w} Für sie ist das Ganze anscheinend auch noch lustig."

    $ sayapose='school_2'
    $ sayaface='smiling'
    show Sayaka
    with dissolve

    s "Ich weiß, ich weiß.{w} Du willst für das alles eine Erklärung, oder?{w} Ich konnte einfach nicht anders."

    $ hikaface='normal'
    show Hikari

    p "Danke ..."

    "Ich seufze und lasse meine Schultern hängen.{w} Endlich.{w} {i}ENDLICH.{/i}"

    s "So, worüber willst du zuerst Bescheid wissen?"

label rooftopexplanation:

    $ sayaface='smiling'
    $ hikaface='normal'
    show Hikari
    show Sayaka

    menu:
        "{i}Wer{/i} seid ihr überhaupt?" if q1 is False:

            "Okay, die Frage ist ja wohl aufgelegt.{w} Ich hab sie zwar schon einmal gestellt, aber die Geschichte mit den 'Schutzengeln' kann unmöglich stimmen.{w} Hoffentlich ist sie jetzt ehrlicher zu mir."

            $ sayaface='happy'
            $ sayapose='school_1'
            show Sayaka
            with dissolve

            s "Also, ich bin Sayaka und das ist Hikari.{w} Hast du unsere Namen etwa schon vergessen, Dümmerchen?"

            "Das ist ja zum Haare ausreißen."

            "Ich öffne noch einmal meinen Mund, um ihr klar und deutlich zu sagen, was ich meine, aber es scheint, als wäre sie mir einen Schritt voraus."

            $ sayaface='smiling'
            show Sayaka

            s "Ich weiß nicht, wie viel ich dir sagen darf.{w} Wir haben schon die Regeln gebrochen, als wir uns dir gezeigt haben."

            $ hikapose='school_2'
            $ hikaface='angry'
            show Hikari
            with dissolve

            h "Ich meine, diese ganze Sache ist eine komplette Katastrophe.{w} Warum musstest du uns so viele Probleme bereiten?"

            p "Hey, das ist nicht meine Schuld!{w} G-Glaub ich zumindest ..."

            h "Sei einfach froh, dass du mir so wichtig bist, ansonsten hätten wir dich zurückgelassen, um von diesem Ding gefressen zu werden."

            $ sayaface='shocked'
            show Sayaka

            "..."

            $ sayaface='laughing'
            show Sayaka

            "Hä ...?"

            $ hikaface='embarrassed'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            "Langsam wird ihr bewusst, was sie gerade sagte.{w} Schon amüsant zuzusehen, wie ihr für gewöhnlich mürrisches Gesicht so ganz plötzlich vor Verlegenheit rot wird."

            h "I-Ich meinte-- w-wichtig für uns!{w} {i}Uns!{/i}"

            $ sayaface='joking'
            $ hikaface='shy'
            show Hikari
            show Sayaka

            s "Sauber."

            "Sayaka kichert und klopft ihr auf die Schulter."

            $ hikaface='normal'
            show Hikari

            h "H-Hmph!"

            $ sayaface='shocked'
            show Sayaka
            with hpunch

            s "Wahh!"

            $ sayaface='scared'
            show Sayaka

            "...Als Antwort wiederum klopf Hikari Sayaka auf die Schulter, wobei das nicht mal annähernd als Spaß gedacht war.{w} Gehören die beiden überhaupt zusammen?"

            p "Wie auch immer ..."

            $ sayaface='smiling'
            show Sayaka

            "Ich versuche mein Bestes, nicht vom Thema abzuschweifen, allerdings bin ich mir nicht sicher, ob diese Unterhaltung friedlich bleiben wird."

            s "Ich denke, das meiste, was wir dir sagen können ...{w} Hmm ..."

            s "Wir sind nicht von hier ... Besser gesagt, wir wurden geschickt, um dich zu beschützen."

            p "Gehört ihr einer Gruppe an?{w} Wartet, gibt es mehr von eurer Sorte?!"

            $ sayaface='joking'
            show Sayaka

            s "He-heh, jetzt hab ich vielleicht schon zu viel gesagt ..."

            "Sie kratzt sich meinem Grinsen am Hinterkopf.{w} In der Angelegenheit werd ich wahrscheinlich nichts mehr aus ihr rausbekommen ...{w} Zumindest für heute."
            
            "Vielleicht erzählt sie mir morgen ja mehr, sofern ich sie überraschen kann."

            $ q1 = True

        "Was war das für ein Monster?" if q2 is False:

            "Ich möchte mehr darüber wissen, was das ...{w}für ein Ding war, vor dem sie mich gerettet haben.{w} Ich glaube, sie haben es als 'Schatten' bezeichnet."

            p "Ich schätze, von diesen Dingern ... gibt es da draußen noch mehr?"

            s "Mmhmm."

            p "Und sie sind hinter mir her?"

            $ sayaface='happy'
            $ sayapose='school_2'
            show Sayaka
            with dissolve

            s "Also, in diesem speziellem Fall sind sie es.{w} Obwohl sie eigentlich nicht so aggresiv sind.{w} Aber sie waren schon immer da und lauern immer in den Schatten."

            $ sayaface='normal'
            show Sayaka

            s "Es ist wirklich komisch.{w} Ich hab noch nie einen gesehen, der sich getraut hat, am hellichten Tag anzugreifen.{w} Es ist, als ob es von etwas {i}wirklich{/i} aufgebracht wurde.{w} Oder ... vielleicht ..."

            "Sie denkt nach, wodurch sie Hikari und mich ungünstig dastehen lässt, und wirft uns dabei gelegentlich einen Blick zu."

            p "Äh, Sayaka?"

            $ sayapose='school_1'
            $ sayaface='smiling'
            show Sayaka
            with dissolve

            "She snaps out of her stupor, blinking back to reality."

            s "Häh?{w} Oh, tut mir leid!{w} Keine Sorge, es ist nichts."

            p "Was hab ich verdammt nochmal getan, um diese Monster zu verärgern?"

            s "Sie haben dich nicht angegriffen, weil du was getan hast, es liegt einfach daran, dass du du bist."

            p "Wer ... bin ich denn?"

            s "Ja, dein Blu--"

            $ sayaface='shocked'
            $ hikaface='angry'
            show Sayaka
            show Hikari
            with hpunch

            h "Sayaka!"

            s "Wahh!{w} Okay, okay.{w} Tut mir leid."

            $ sayaface='smiling'
            show Sayaka

            "Sayaka wird von einem Schrei von Hikari unterbrochen.{w} Au ...{w} Ich schätze, ich werd es nie rausfinden.{w} Hikari möchte dieses Geheimnis anscheinend um jeden Preis geheim halten."

            $ hikaface='normal'
            show Hikari

            h "Er muss davon nichts wissen.{w} Es ist besser so.{w} Wie werden das Problem lösen, und dann endlich diese grausame Schule verlassen."

            s "Mit dir macht es echt keinen Spaß{w} ... Aber du hast recht.{w} Tut mir leid, Kenta."

            "Sie sieht mich entschuldigend an.{w} Und es hört sich auch so an, als würde sie es ernst meinen.{w} So, als würde sie es mir gerne sagen, es mir aber nicht sagen kann.{w} Druck auszuüben wäre jetzt wohl auch nicht richtig."

            $ q2 = True

        "Wie lange werdet ihr hier bleiben?" if q3 is False:
            "Die Frage ist ganz wichtig.{w} Wie lange, äh, wollen sie überhaupt auf mich aufpassen?"

            $ sayaface='scared'
            show Sayaka

            "Sayaka reagiert mit einem traurigen Blick auf meine Frage.{w} ... Ist die Frage wirklich so schlimm?"

            s "Es ist fast so, als ob du uns gar nicht haben willst.{w} Sind wir etwa so lästig?"

            "Verdammt.{w} Warum muss sie es ausgerechnet so ausdrücken?{w} Das hab ich doch gar nicht gemeint!{w} ... Glaub ich zumindest."

            "Es ist nur ...{w} Solange die beiden in meiner Nähe sind, wird mir wahrscheinlich ein Problem nach dem anderen über den Weg laufen."

            p "Ach, komm schon, so hab ich's auch nicht gemeint ..."

            "Plötzlich zeigt sie mir wieder ihr strahlendes Lächeln."

            $ sayaface='happy'
            show Sayaka

            s "Ich weiß!{w} Man kann dich einfach nur leicht ärgern.{w} Ich konnte einfach nicht anders!"

            "Dieses Mädchen ..."

            "Sie bricht in ein Gelächter aus.{w} Und dieses Lachen ist so laut, dass man es bestimmt in der ganzen Schule hören kann."

            $ sayaface='smiling'
            show Sayaka

            s "Wir werden nicht lange hier sein, ich verspreche es.{w} Nur, bis wir alles geregelt haben."

            p "Ich schätze, ihr könnt mir nicht sagen, was ihr zuerst 'klären' müsst, oder?"

            $ sayapose='school_2'
            show Sayaka
            with dissolve

            "Sie zwinkert mir zu.{w} Dachte ich mir schon."

            s "Streng geheim und so.{w} Aber wir sind gerade dabei, etwas über dieses Durcheinander herauszufinden.{w} Es sollte nicht lange dauern.{w} Vielleicht ein paar Tage.{w} Höchstens eine Woche!"

            $ hikapose='school_2'
            show Hikari
            with dissolve

            h "Was, eine Woche?!{w} Würde es nach mir gehen, wären wir schon morgen weg.{w} Ich hasse diesen Ort...{w} Er ist so laut."

            s "Nun, wenn jemand nützlicher wäre und mir helfen würde, anstatt sich ständig zu beschweren, könnten wir die Dinge schneller erledigen, hmm?"

            "Whoa, sie sagte das gerade, ohne ihr Lächeln auch nur ein bisschen 'aufzugeben', und auch ihr Farbton ist trotz der scharfen Worte noch genauso fröhlich.{w} ... Das macht mir irgendwie Angst."

            $ hikaface='scared'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            "Nicht mal Hikari war darauf vorbereitet, da auch sie dadurch zum Schweigen gebracht wurde."

            "Äh ...{w} Weiter ..."

            $ q3 = True

        "Das wär's fürs Erste." if qquit is True:
            "Ich schätze, das reicht fürs Erste.{w} Die Glocke dürfte sowieso gleich--"

            "Jup.{w} Da haben wir sie ja schon."

            s "Oh?{w} Wir sollten langsam zurückgehen, oder?"

            $ sayapose='school_1'
            show Sayaka
            with dissolve

            "Sie streckt ihre Arme in die Luft und gähnt."

            s "Also, ich hoffe, wir konnten dir ein paar Sachen erklären."

            "...Mehr oder weniger."

            $ sayaface='happy'
            show Sayaka

            s "Komm schon, wir wollen doch nicht zu spät kommen!"

            hide Sayaka
            show Hikari at center
            with dissolve

            "Sayaka rast, so als wäre es ein Rennen, auf die Treppe zu, während ihre Partnerin hinter ihr herläuft und mir einen letzten Blick zuwirft."

            "Sie bleibt stehen und blickt einen kurzen Augenblick nach unten, ehe sie ihren Kopf wieder geradeaus richtet."

            h "Hey, ähm ..."

            p "Was ist?"

            $ hikaface='shy'
            show Hikari

            h "...Nichts.{w} Es ist ... nichts."

            hide Hikari
            with dissolve

            "Und so verschwindet auch sie die Treppe hinunter, wodurch sie mich allein auf dem Dach zurücklässt.{w} Hm.{w} Was sie wohl gerade wollte?"

            "Ich sollte mich aber jetzt besser beeilen.{w} Ich will nicht schon wieder zu spät kommen!"

            "Als ich mich auf dem Weg zur Treppe mache, macht sich plötzlich mein Magen bemerkbar.{w} Und der schreit nach Essen."

            "Ah, stimmt. Vor lauter Fragerei hab ich komplett auf mein Essen vergessen.{w} Fuck ..."

            scene bg black
            with fade


            jump explanationover

    s "So, gibt es da noch etwas, worüber du was wissen willst?"

    $ qquit = True

    jump rooftopexplanation

label explanationover:

    stop music fadeout 4.0
    with Pause(2.5)

    "..."

    "Und so geht der Unterricht weiter."

    "..."
    play music "bgm/everydayintro.ogg" fadein 3.0
    queue music "bgm/everydayloop.ogg"
    "Nach all dem Wirbel heute morgen, passiert in den restlichen Stunden nicht mehr sonderlich viel.{w} Die Stunden ziehen sich wie Kaugummi."

    "Umgeben von Sayaka und Hikari fällt es mir auch schwer, mich auf irgendwas zu konzentrieren."

    "Teilweise habe ich schon damit gerechnet, dass jeden Moment ein Monster durch das Fenster springt und das Klassenzimmer in ein Schlachtfeld verwandelt."
    
    "Obwohl ...{w} Dann wär zumindest wieder was los hier."

    with Pause(2.5)

    scene classroom
    with fade

    "Mit dem letzten Glockenläuten geht der Unterricht zu Ende.{w} Der Großteil der Schüler verlässt das Klassenzimmer in Richtung Club oder Teilzeit-Job.{w} Aber ich nicht, denn ich geh nach Hause!"

    "Obwohl der Beitritt zu einem Club zwar von der Schule gewünscht ist und gefördert wird, ist es - zum Glück - nicht verpflichtend.{w} Das heißt, ich kann nach dem Unterricht tun, was ich will."

    "Für andere seh ich vielleicht aus wie ein Faulpelz, aber pf, da scheiß ich drauf.{w} Sie haben ja schließlich auch recht!"

    scene bg black
    with fade

    "Ohne Zeit zu verschwenden, verlasse ich die Schule und mache mich auf den Weg.{w} Etwas, das eigentlich ziemlich stressfrei sein sollte, aber ..."

    "Ich mein, ich hätte schon damit rechnen können, aber das ist jetzt echt ein bisschen übertrieben."

    scene town street night
    with fade

    "Mit jedem Schritt, den ich durch die ruhigen Straßen mache, wird der Himmel dunkler und der Mond wird immer sichtbarer."

    "{i}Stampf, stampf, stampf.{/i}{w} Meine schweren Schritte hallen durch die Nacht.{w} Aber neben meinen sind auch noch andere Schritte zu hören - von zwei Personen, um genau zu sein."
    
    "Diese Schritte sind aber weitaus leiser als meine, und sie werden auch mit viel mehr Anmut gesetzt. "

    p "Schaut ...{w} Ich weiß, dass ihr mich nur beschützen wollt, aber müsst ihr dafür, äh, so {i}an mir kleben{/i}?"

    "Ja.{w} Die Schritte gehören zu niemand geringeren als zu meinen selbsternannten 'Schutzengeln'.{w} Sayaka links und Hikari rechts von mir."
    
    "Und obwohl ihre Schultern zwar Zentimeter von meinen entfernt sind, marschieren wir im Gleichschritt."

    $ hikapose='school_2'
    $ hikaface='normal'
    show Hikari
    with dissolve

    h "Sei doch nicht dumm!{w} Nachts alleine heimzugehen wäre der perfekte Moment für den Feind, um zuzuschlagen.{w} Hier müssen wir am meisten aufpassen."

    "Huch.{w} Sie muss mir echt nicht so laut ins Ohr schreien.{w} Ich denke, wenn ich noch mehr Zeit mit ihr verbringe, werd ich noch irgendwann taub."

    $ hikaface='angry'
    show Hikari

    h "Denkst du, ich {i}mag{/i} es, dir so nah zu sein?{w} Du solltest dankbar dafür sein, dass ich das überhaupt mache."

    $ hikapose='school_1'
    $ hikaface='normal'
    show Hikari
    with dissolve

    "Und wieder dreht sie ihren Kopf einfach gleichgültig weg."

    p "Ja, ja ...{w} Entschuldige."

    play music "bgm/mischiefintro.ogg" fadein 1.0
    queue music "bgm/mischiefloop.ogg"

    hide Hikari
    with dissolve
    $ sayapose='school_1'
    $ sayaface='joking'
    show Sayaka
    with dissolve

    s "Aww, sei doch nicht so, Hikari.{w} Denk nicht, ich sehe nicht, wie du ihn die ganze Zeit ansiehst, wenn er wegsieht."

    "Während sie geht, lehnt sich Sayaka etwas über mich und lächelt Hikari an.{w} Leute, die Situation wird langsam echt komisch."

    hide Sayaka
    with dissolve
    $ hikaface='embarrassed'
    show Hikari
    with dissolve

    h "H-Hä?{w} Du hast gesehen, wie ... I-Ich meine, ich hab einfach nur nachgeguckt, ob der Gegner eh noch keinen Überraschungsangriff durchgeführt hat!"

    hide Hikari
    with dissolve
    show Sayaka
    with dissolve

    s "Genau, was auch immer du sagst~"

    with hpunch
    with hpunch
    $ sayaface='laughing'
    show Sayaka

    "Mein linkes Ohr wird von einem schelmischen Kichern belästigt, da Sayaka anscheinend einen hysterischen Anfall hat. Und Hikari reagiert mit einem knallroten Gesicht darauf."

    hide Sayaka
    with dissolve
    $ hikaface='shy'
    show Hikari
    with dissolve

    h "W-Wie auch immer!{w} Du bist doch diejenige, die immer deine Schulter gegen ihn drückt!{w} Was versuchst du damit zu erreichen?!"

    "Häh?{w} Das ... hat sie getan?{w} Jetzt, wo sie's erwähnt, fällt mir ein, dass ich auf der linken Schulter wirklich ein eigenartiges Gefühl gespürt hab ..."

    hide Hikari
    with dissolve
    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Hm?{w} Ich wollte ihn nur warm halten.{w} Guck, ich {i}kümmere{/i} mich um seine Gesundheit und möchte nicht, dass er eine Erkältung bekommt."

    s "Er beschwert sich nicht, also muss er es ja auch mögen!"

    with hpunch

    "Ohne Vorwarnung hängt sie sich an meinen Arm, wodurch sie mich beinahe zu Boden drückt."

    s "Siehst du~?"

    p "H-Hey, das ist jetzt aber--"

    hide Sayaka
    with dissolve
    $ hikaface='angry'
    show Hikari
    with dissolve

    h "Was machst du?{w} Du wirst ihm noch den Arm abreißen!{w} D-Du musst das sanfter machen ... So wie ich ..."

    $ hikaface='shy'
    $ hikapose='school_2'
    show Hikari
    with dissolve
    with hpunch

    "H-Ha?{w} Als Reaktion darauf krallt sich Hikari meinen anderen Arm und versucht, mich von Sayaka wegzuziehen.{w} Das ist doch hoffentlich ein Traum, oder?"

    p "Mädels, ihr müsst euch echt nicht--"

    hide Hikari
    with dissolve
    show Sayaka
    $ sayaface='smiling'
    $ sayapose='school_1'
    with dissolve

    s "Mmm.{w} Nein.{w} So geht das auf gar keinen Fall, Hikari!{w} Eher so ..."

    $ sayaface='happy'
    show Sayaka
    with hpunch

    "Sayaka zieht stärker an meinen Arm, woraufhin sie beide meine Arme fest im Griff hatten. Leider voller Entschlossenheit, sie nicht so schnell loszulassen."

    with hpunch

    "Spielen die Tauziehen mit mir?{w} Die reißen mich noch auseinander!"

    hide Sayaka
    with dissolve
    $ hikaface='embarrassed'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Hah!{w} B-Bitte!{w} {i}Das{/i} geht so!"

    with hpunch

    "Haben die schon vergessen, wofür sie eigentlich da sind?!{w} Sie sind eigentlich meine SCHUTZENGEL!"

    p "Könntet ihr mich bitte ...{w} LOSLASSEN!?"

    hide Hikari
    with dissolve
    with hpunch

    "Ich erhebe meine Stimme - so laut, wie schon lange nicht mehr - und versuche, mein Leben zu retten!"

    "Und kurz darauf lassen sie beide meine Arme los ... Hoffentlich sind sie noch heil."

    "Ich bin froh, dass sie auf mich gehört haben.{w} Ich dachte echt, ich müsste sterben.{w} Anscheinend sind die Monster nicht mal halb so gefährlich wie die beiden!"

    p "Äh, Mädels?"

    stop music fadeout 2.0
    $ sayaface='normal'
    $ hikaface='normal'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "...Zumindest {i}dachte{/i} ich, es wäre mein Schrei gewesen, der sie zur Vernunft gebracht hat, aber ihre Aufmerksamkeit ist etwas ganz anderem gewidmet."

    "Wo sehen sie hin?{w} Ich konzentriere mich und blicke ebenfalls über die Dächer."

    "Und dann, als die Wolken sich teilen und das helle Mondlicht aufleuchtet, sehe ich sie."

    scene cg11
    with dissolve
    play music "bgm/evilgirlintro.ogg"
    queue music "bgm/evilgirlloop.ogg"

    "Auf dem Sims eines der höchsten Gebäude der Gegend sitzt ein Mädchen."

    "Silbernes Haar, das im Mondschein zu schimmern scheint, ein Outfit so finster wie die Nacht und ein beinahe engelhafter Blick{w} Als ... wäre sie eine Art Engel, der vom Himmel herabblickt."

    "Zumindest {i}würde{/i} würde ich sie als Engel betrachten, wäre da nicht dieses beunruhigende Grinsen, dass sie auf einmal aufgesetzt hat."

    dg "Ahhh.{w} Da bist du ja."

    "Sie murmelt etwas vor sich hin - etwas, was ich nicht verstehen konnte.{w} Was auch immer es war, es war zumindest so lustig, dass sie selbst zu lachen beginnen musste."

    "Irgendwie bekomme ich das Gefühl, als hätte ich sie schon mal gesehen ...{w} Aber wo nur?"

    "Egal, wie sehr ich mich auch anstrenge, es fällt mir nicht ein."

    "In einem Federsturm entfalten sich hinter ihr Flügel.{w} Okay, die sind {i}eindeutig{/i} nicht heilig.{w} Ich hab ein ganz schlechtes Gefühl bei der Sache ..."



    "Bernsteinfarbene Augen blicken voller Entschlossenheit auf uns drei herab."
    
    "Vielleicht bilde ich es mir auch nur ein, aber ihr Hauptaugenmerk scheint auf {i}mich{/i} gerichtet zu sein.{w} Sie starrt mich ja schon förmlich an."

    "All das reicht, um mir leichte Schmerzen im Hinterkopf zu verpassen{w} Und dass es mir bereits eiskalt den Rücken runterläuft, muss ich ja hoffentlich nicht extra erwähnen."

    p "Eine ... Eine Freundin?"

    "Ich zwinge mich zu einem Lachen, obwohl ich die Wahrheit schon kenne.{w} Die Atmosphäre wird immer angespannter, so wie damals mit dem Monster ..."
    
    "... und die Gesichtsausdrücke von Hikari und Sayaka lassen auf nichts Gutes rückschließen."

    s "Hah.{w} Ich hab keine Angst.{w} Kenta, komm zurück.{w} Das gefällt mir überhaupt nicht ..."

    p "Aber ...{w} Okay, okay."

    "Ich tu, was sie mir gesagt haben, und ziehe mich ein wenig zurück. Schließlich möchte ich in einer solchen Situation nicht mit ihnen zu streiten beginnen."

    s "So, mit was denkst du, haben wir es hier zu tun?"

    h "Sie sieht viel zu sehr nach Mensch aus, um ein Schatten zu sein ...{w} Aber ich bekomme in ihrer Anwesenheit das gleiche Gefühl von Angst."

    s "Ahh, ich verstehe{w} ... Ich denke{w} ... Warte, sie {i}ist{/i} also ein Monster, oder?"

    h "Das versuch ich rauszufinden!{w} Wenn du für eine Sekunde aufhören würdest, in mein Ohr zu schreien, könnte ich mich konzentrieren ..."

    s "Ich schreie nicht!{w} Mein Gott."

    h "Richtig.{w} Hab ich vergessen.{w} Das ist ja deine Standard-Lautstärke.{w} Dann sei einfach ruhig und lass mich nachdenken."

    s "Du bist manchmal so grausam, Hikari ..."

    "Das silberhaarige Mädchen wirft mir noch einen kurzen Blick zu, bevor es sich auf die Mädchen konzentriert.{w} Und dann springt sie."

    scene town street night
    with dissolve

    "Was?!{w} Warum ist sie gesprungen?!{w} I-Ich kann es kaum mitansehen."

    "Dort, wo meine beiden Wächterinnen stehen, stürzt sie nach unten.{w} Wofür hat sie überhaupt ihre Flügel?"

    "Sie fällt immer schneller und schneller, bis kurz darauf der Boden zum Greifen nahe ist ...{w} Ich möchte nicht zusehen."
    
    "Aber ...{w} irgendwie hab ich das Gefühl, als hätte sie einen guten Grund für diesen Sprung.{w} Ich {i}hoffe{/i} aber, das ist nicht der Fall."

    p "...!"

    "Nur wenige Zentimeter vor dem Aufprall breitet sie ihre Flügel aus, wodurch sie kurzerhand zum Stillstand kommt."
    
    "Und das geschieht von einer Sekunde auf die andere - so, als würde sie die Erdanziehungskraft komplett ignorieren."

    "Selbst mit Flügel sollte das nicht machbar sein.{w} Würde eine Taube so was machen, dann wär sie jetzt platt!"

    "Aber ihre Füße berühren ja nicht mal den Boden.{w} Sie schwebt über der Oberfläche. Man könnte fast meinen, sie schreitet auf einer unsichtbaren Plattform voran."

    "Ein Teil von mir ist froh, dass ihr nichts passiert ist.{w} Aber ein anderer Teil macht sich bereits Sorgen darüber, was als nächstes passiert."

    $ yuzupose='magical_1'
    $ yuzuface='joking'
    show Yuzuki at left
    show Sayaka at right
    show Hikari at center
    with dissolve

    "Das silberhaarige Mädchen steht vor Hikari und Sayaka.{w} Trotz ihres Lächelns lässt nichts auf mögliche böse Absichten hindeuten, und trotzdem sind die beiden Mädchen sichtlich angespannt."



    "Wenn ich versuche, mich auf sie zu konzentrieren, fängt mein Kopf wieder an zu schmerzen.{w} Hat sie ... irgendwas mit den Monstern zu tun?{w} Ich fasse mir mit einer Hand zum Kopf."
    
    "Es kostet mir schon extrem viel Willenskraft, aufrecht stehenzubleiben."

    dg "Guten Abend, Mädchen."

    "Sie begrüßt sie ganz lässig, als würde sie die beiden kennen.{w} Irgendwie ...{w} werd ich das Gefühl nicht los, dass sie nicht für diese Begrüßung von einem Dach gesprungen ist."

    h "...Lass uns zur Sache kommen, okay?{w} Wer bist du, und was willst du?"

    $ yuzupose='magical_2'
    $ yuzuface='happy'
    show Yuzuki
    with dissolve

    dg "Ihr seid ja mal ein feindseliges Pack, was?"

    "Sie kichert und versucht nichts, die Spannung, die in der Luft liegt, zu beseitigen."

    dg "Sehr Gut.{w} Ihr könnt mich Yuzuki nennen.{w} Und worauf ich es abgesehen habe ...{w} Nun ..."

    $ yuzuface='joking'
    show Yuzuki

    "Die Augen der Mädchen richten sich plötzlich alle auf mich. Irgendwie wird das immer merkwürdiger ..."

    y "Ich nehme den Jungen mit, wenn es euch nichts ausmacht.{w} Wisst ihr, er ist {i}sehr{/i} wichtig für mich."

    $ hikaface='angry'
    $ sayaface='scared'
    show Hikari
    show Sayaka



    "...!"

    "Ich wusste es.{w} Natürlich hat sie was mit diesem Schlamassel zu tun.{w} Warum auch nicht?"

    "Heute ist wohl der Tag, an dem mich alles und jeder anscheinend tot sehen will."

    $ hikaface='normal'
    $ sayaface='normal'
    show Hikari
    show Sayaka

    "Sayaka und Hikari sind aber dagegen.{w} Aber das hoffe ich auch.{w} Ansonsten wären sie auch keine 'Schutzengel'."

    $ yuzupose='magical_1'
    $ yuzuface='happy'
    show Yuzuki
    with dissolve
    stop music fadeout 9.0
    y "...Nein?{w} Ich denke, wir müssen die Dinge auf die harte Tour regeln, hmm?"

    "Die beiden stehen mit geballten Fäusten vor mir.{w} Ich befürchte langsam, dass ich schon weiß, wie es ausgeht."

    "Die Menge an Kraft in ihren Fäusten ist so immens, dass sie die Luft um sie herum förmlich zum Knistern bringt."

    "..."

    "Ich trau mich nicht mal zu atmen, weil ich mich nicht einmischen möchte.{w} Das ist gefährlich.{w} Das seh selbst {i}ich{/i}."

    with Pause(3.5)

    "Ich blinzle und ..."


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

    "Yuzuki stürzt sich, mit einer Sense, die sie scheinbar aus dem Nichts herbeigezaubert hätte, blitzschnell auf sie."

    $ hikaface='angry'
    $ hikapose='magical_1'
    show Hikari
    with dissolve

    s "W-Wahh!"

    "Der Aufprall von Metall gegen Metall löst Funken aus.{w} Hikari konnte gerade noch rechtzeitig reagieren, wodurch sie den Schlag mit dem Schwert noch gerade so abwehren konnte."
    
    "Wäre dem nicht so, wären sie einen Kopf kürzer."

    h "Nnngh.{w} Ich wusste es!{w} Du bist einfach nur eine Puppe von {i}ihr{/i}!"

    "Sie spricht zähneknirschend und versucht mit aller Kraft, den Abstand zu verkürzen."
    
    "Es scheint aber, als würde sie den Kampf verlieren, denn das silberhaarige Mädchen lässt sich überhaupt keine Anstrengungen anmerken."

    show Yuzuki at center
    show Hikari at center
    with MoveTransition(0.2)
    with hpunch
    show Yuzuki at right
    show Hikari at left
    with move

    h "Sayaka!{w} Fühl dich frei, mir jederzeit --grghh-- zu helfen!"

    hide Yuzuki
    hide Hikari
    $ sayaface='shocked'
    show Sayaka at center
    with dissolve

    s "Häh?{w} Oh, genau!"

    "Hikari verliert ziemlich schnell an Boden, woraufhin sie ihre Partnerin, die sich gerade vom Schock des Schlags erholt hatte, förmlich anschreit."

    "Das sieht echt nicht gut aus ...{w} Und ich kann nur zusehen.{w} Und ich weiß, dass ich, wenn ich in die Quere komme, als Hackfleisch ende.{w} Ich kann mit denen nicht mal annähernd mithalten."

    $ sayaface='normal'
    $ sayapose='magical_1'
    show Sayaka
    with flash

    "Mit einem weiteren Aufleuchten verwandelt sich Sayaka erneut - dieses Mal schwingt sie wieder ihren Bogen, den ich auch heute morgen bereits sah."

    scene cg15
    with dissolve

    "Sie springt ein wenig zurück und spannt den Bogen.{w} Als ich mich gerade fragte, wo der Pfeil sei, bemerkte ich, dass dieser ja bereits am Bogen befestigt ist."

    "Dann lässt sie ihren magischen Pfeil fliegen."

    with flash

    "Yuzuki hat keine andere Wahl, als von Hikari Abstand zu nehmen.{w} Sie springt anmutig zurück und kann dem Pfeil gerade noch ausweichen."

    h "Genau rechtzeitig!"

    scene town street night
    show Hikari at center
    show Sayaka at right
    with dissolve

    "Hikari seufzt erleichtert, als sie bemerkt, dass sie sich für einen Moment ausruhen kann.{w} Aber der Kampf ist noch lange nicht vorbei."

    "Die Mädels formieren sich neu, während sie von ihrer mysteriösen Gegnerin mit eiskalten Augen angestarrt werden."

    h "Sei vorsichtig, Sayaka.{w} Sie ist stark.{w} Ich konnte sie kaum zurückhalten."

    "Sayaka nickt mit einer solchen Entschlossenheit, die ich von ihr überhaupt nicht kannte."

    $ yuzupose='magical_2'
    show Yuzuki at left
    with moveinleft

    "Das silberhaarige Mädchen nimmt sich einen kurzen Augenblick Zeit, um die Situation zu analysieren, ehe sie für eine zweite Runde wieder die Distanz verringert."

    $ yuzuface='joking'
    show Yuzuki

    y "Hah, ist das alles, was du kannst?{w} Das wird viel {i}einfacher{/i}, als ich mir vorgestellt habe."

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

    y "Ah, das macht so viel Spaß! {w}Und ich dachte, die kleinen 'Wächter' dieses Jungen könnten tatsächlich eine Bedrohung darstellen. {w} Wie dumm von mir!"

    h "S-Sei ruhig!{w} Es ist noch nicht vorbei!"

    "Mit Leichtigkeit und einem wahnsinnigen Gesichtsausdruck schwingt sie ihre Sense.{w} Die Mädels können den Schlägen entweder nur ganz knapp ausweichen oder aber sie werden von Hikari geblockt."

    "Der Kampf ist komplett einseitig ...{w} Und das war bereits zu erwarten, als das Mädchen ihren ersten Zug gemacht hat."

    "Sie kann es ohne Probleme mit beiden aufnehmen und blockt jeden Angriff, den Hikari versucht, und immer wenn Sayaka versucht, sie auf Distanz zu halten, jagt sie ihr hinterher."

    h "Fein!{w} Mal sehen, ob du auch bei dieser Geschwindigkeit ausweichen kannst!"

    show Hikari at center
    show Yuzuki at center
    with MoveTransition(0.2)
    with hpunch
    show Hikari at offscreenright
    show Yuzuki at offscreenleft
    with MoveTransition(0.3)

    "...Whoa."

    with hpunch

    "Mittlerweile bewegen sie sich so schnell, dass meine Augen gar nicht mehr mitkommen. Im Endeffekt nehme ich die ganze Action nur noch unscharf wahr."

    with hpunch
    with hpunch

    "Die Straße um sie herum wird völlig zerstört.{w} Straßenlaternen werden entzweit, geparkte Autos werden durch die Luft geschleudert und selbst Teile der Straße selbst werden gelegentlich zerstört."

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

    "Ohne Vorwarnung kommt diese hochgradige Geschwindigkeit plötzlich zum Stillstand.{w} Und während Sayaka und kurz darauf auch Hikari zu Boden gehen, steht das silberhaarige Mädchen triumphierend da."

    stop music fadeout 6.0
    scene cg14
    with fade

    s "Wahhh!"

    h "Uuf!"

    "Sie fallen beide ziemlich benommen aufeinander."

    "Obwohl sie sichtbare, blaue Flecken haben, scheinen sie zum Glück nicht allzu schwer verletzt zu sein."

    p "G-Geht es euch gut?!"

    "Nicht länger in der Lage, das alles zu ertragen, begebe ich mich aus meiner Deckung und bewege mich schreiend auf sie zu."



    "Als sich die Augen des silberhaarigen Mädchens auf mich fixierten, bleibe ich wie eingefroren stehen.{w} Ihr Blick ist beängstigend.{w} Lähmend.{w} Sie hat es auf mich abgesehen.{w} Genauso wie auch das Monster."

    "Klebt auf meinem Rücken etwa ein Zettel, auf dem 'Bringt mich bitte um' steht?!"

    h "Was machst du, du Idiot?!{w} Bleib zurück!{w} W-Wir sind ...- argh - Es geht uns gut!"

    "Hikari bringt mich mit einem lauten Schrei wieder zur Besinnung.{w} Schwer vorstellbar, dass es ihnen gut geht, wenn man sie so ansieht ...{w} Wild um sich schlagend, versuchen sie beide aufzustehen."

    play music "bgm/mischiefintro.ogg"
    queue music "bgm/mischiefloop.ogg"

    s "Ist das mein Bein oder deins?{w} Ich kann es nicht sagen!"

    h "Au!{w} Schlag ja nicht drauf!{w} Das wird das Problem auch nicht lösen!"

    s "Ohh ...{w} Es war also {i}dein{/i} Bein.{w} Okay, ich verstehe!"

    h "Warum schlägst du immer noch drauf ein?!"

    h "Geh ...{w} einfach von mir runter!{w} Nnghh, du bist so schwer!"

    s "S-Schwer?{w} Ich?!"

    h "Ja, du!{w} Wenn du nicht so ein Vielfraß wärst, wären wir vielleicht nicht in dieser Situation!"

    s "Es ist nicht meine Schuld, dass ich so gerne esse!{w} Ich denke, du bist einfach neidisch, dass ich so viel essen kann und nicht zunehme."

    s "Ich habe gesehen, was passiert, wenn du dich vollfrisst, Hikari.{w} Du verdreifachst dich einfach!"

    h "E-Entschuldige?!{w} Du hast Glück, dass ich nicht an mein Schwert komme, sonst würde ich dich ..."

    h "Au!{w} Hast du mich gerade gebissen?!"

    s "Mmm.{w} Du kannst nichts beweisen!"

    h "D-Du bist so unzivilisiert!"

    "Das ist eine totale Katastrophe ..."

    stop music fadeout 1.0

    "Da meine vermeintlichen Wächter noch immer versuchen, wieder auf die Beine zu kommen, bin ich der auf mich zukommenden Yuzuki hilflos ausgeliefert."
    
    "Sie macht langsame und kleine Schritte und hinterlässt bewusst den Anschein, als würde sie meine Furcht genießen."

    scene town street night
    $ yuzupose='magical_2'
    $ yuzuface='joking'
    show Yuzuki at center
    with dissolve
    play music "bgm/evilgirlintro.ogg"
    queue music "bgm/evilgirlloop.ogg"
    y "Jetzt, wo die aus dem Weg geräumt sind ...{w} Lass uns doch ein bisschen Spaß haben, oder?"

    "{i}Klopf.{w} Klopf.{w} Klopf.{/i}{w} Wenn das so weitergeht, springt mein Herz noch aus meinem Körper."

    "Ich sollte wegrennen.{w} Aber ich kann nicht.{w} Warum kann ich nicht?{w} Ich habe überhaupt keine Kontrolle mehr über meinen Körper."

    "Der Abstand zwischen uns ist gleich Null.{w} Wird sie mich umbringen?{w} ...Warum mich?{w} Womit hab ich das bloß verdient?!{w} Ich mein, bis vor kurzem hab ich noch ein ganz normales Leben geführt."



    "Je näher sie kommt, desto stärker werden meine Kopfschmerzen.{w} Die Luft um mich herum ist erdrückend.{w} Selbst der einfache Akt des Atmens fällt mir in diesem Zustand viel zu schwer."



    "Ihre bernsteinfarbenen Augen werden schmaler.{w} Sie packt ihre Sense immer stärker."

    p "W--...{w}Warum ...?"

    y "Oh, es ist nichts Persönliches.{w} Es muss einfach so sein, wenn ich mein Leben wieder auf Kurs bringen will."
   
    $ yuzupose='magical_1'
    $ yuzuface='angry'
    show Yuzuki
    with dissolve

    y "Und jetzt ...{w} sag gute Nacht."

    "Mit einer klaren Absicht, mich zu töten, stürmt sie blitzartig auf mich zu.{w} Ich kann nicht einmal meine Arme heben, um mich zu verteidigen.{w} Das ... Das war's dann wohl."

    $ yuzuface='shocked'
    show Yuzuki
    with flash
    hide Yuzuki
    with dissolve

    "Kurz bevor mich die Klinge berührt, erscheint ein heller Lichtstrahl von der Seite, der das Mädchen augenscheinlich überascht und sie ins Wanken bringt."

    $ sayaface='angry'
    $ hikaface='normal'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "Mit einem Blick auf die Stelle, auf der Hikari und Sayaka lagen, sehe ich, dass die beiden wieder auf ihre Beine gekommen sind."
    
    "Sayaka hat ihre Hand ausgestreckt und lässt Rauchwolken aus ihren Fingern aufsteigen.{w} Da bin ich ihr wohl was schuldig."

    $ sayaface='normal'
    show Sayaka

    s "Das war zu knapp.{w} Ich ...{w} Ich denke, es ist Zeit für einen taktischen Rückzug, oder?"

    $ hikaface='shocked'
    show Hikari

    h "Hä?{w} Wir rennen einfach davon?!{w} Ich kann noch ... {w} Ich kann noch kämpfen!"

    s "Ach, erzähl mir doch nichts!{w} Du kannst ja kaum stehen.{w} Komm schon!"

    hide Hikari
    hide Sayaka
    with dissolve

    "Während sich unsere Gegnerin von diesem Angriff noch immer zu erholen scheint, nutzen meine Retter diese Möglichkeit, um sich bei mir neu zu formieren."
    
    "Gleichzeitig lösen sich langsam ihre Waffen aus und setzen sich auf ihren Rücken wieder zu Flügeln zusammen."

    p "W-Wartet, was macht ihr?"

    s "Halt dich gut fest, okay?"

    "Bevor ich noch irgendein Wort sagen konnte, heben beide vom Boden ab und ...{w} steigen auf.{w} Hinauf.{w} In die Luft.{w} Wir ...{w} Wir fliegen.{w} Wir FLIEGEN verdammt nochmal."

    p "Was?!{w} Hey, nein, lasst mich runter!{w} Können wir nicht einfach weglaufen?!"

    with hpunch

    h "Hör auf, rumzutreten, sonst fallen wir noch, du Idiot!"

    p "Da mach ich nicht mit!{w} Das ist verrückt!{w} Uff.{w} Ich ...{w} Ich ...{w} Ich glaub, ich muss kotzen."

    h "Hey, wag es ja nicht, sonst wirst du dir wünschen, du wärst noch da unten bei diesem Freak!"

    "Wir ziehen weiter durch den Himmel und durchdringen die Wolken, als ob es das Natürlichste der Welt wäre."

    "Der Wind weht an mir vorbei, unten in der Stadt flimmern die Lichter und ...{w} die Unruhe, die sich ergibt, da ich von den beiden getragen werde ..."
    
    "Mir wird schlecht.{w} Ich weiß nicht, ob ich das noch viel länger ertragen kann."

    s "Denkst du, wir haben sie abgehängt?"

    "Sie schalten um zu einem sanften Schwebeflug und halten mich fest in der Hand - hoffe ich zumindest - ehe sie sich kurz umdrehen, um zu bemerken, dass sie fürs Erste ein wenig durchatmen können."

    h "Ich denke schon.{w} Ich kann nicht glauben, dass wir fliehen mussten."

    s "Hey.{w} Hey.{w} Wir sind nicht {i}geflohen{/i}, okay?{w} Es war ein 'taktischer Rückzug'!"

    h "Ugh.{w} Nenn es, wie du willst, aber wir hatten Glück, dass wir heil rausgekommen sind."

    "...Während das Paar in Gedanken versinkt, übernimmt die Stille das Geschehen."

    p "Also, äh ..."

    s "Huh?{w} Kenta?{w} Oh, ich hab dich fast vergessen, sorry!"

    "Das macht mir ein bisschen Angst ...{w} Wenn man bedenkt, dass ihr die einzigen seid, die mich vor einem schmerzhaften und grausamen Tod bewahren!"

    s "Du bist nicht verletzt, oder?"

    p "Nein, mir geht's gut.{w} Es ist nur ...{w} Könntest du mich, äh, du weißt schon ..."

    with hpunch

    p "MICH RUNTERLASSEN?!"

    s "Richtig, richtig.{w} Ich denke, jetzt ist es sicher.{w} Und los!"

    "Aus den Wolken heraus beginnen wir einen langsamen Sinkflug, und es dauert nicht lange, bis ich unter meinen Füßen wieder festen Boden spüre.{w} Ich muss mich echt davon abhalten, ihn nicht gleich zu küssen."

    "Mit einem schweren Magen falle ich auf meine Knie.{w} Nie wieder.{w} Ich bin echt nicht fürs Fliegen gemacht."

    $ sayaface='scared'
    show Sayaka at center
    with dissolve
    with hpunch

    s "Bist du okay?"

    "Sayaka gives me a solid pat on the back, which does little in the way of helping my stomach."

    p "...Hört auf ..."

    $ sayaface='smiling'
    show Sayaka

    s "Hmm?"

    "Ich finde kaum Worte, nachdem ich diese traumatische Erfahrung gemacht habe!{w} Ich hole tief Luft und versuche es noch einmal."

    p "Macht das ja nicht noch einmal.{w} Zumindest nicht, ohne mich vorher zu fragen!"

    $ hikapose='magical_2'
    $ hikaface='angry'
    show Sayaka at left
    show Hikari at right
    with dissolve

    h "Es war ein Notfall, du Schwächling!"

    with hpunch

    "Hikari klopft mir auf den Rücken.{w} Obwohl, gemessen an der Kraft, die sie einsetzt, ist es schon eher ein Schlag.{w} Uff ..."

    h "Glaubst du, ich hab es genossen, dich so lange festzuhalten?"

    p "Okay, okay, ich versteh schon.{w} Hört bloß auf ...{w} mich zu tätscheln.{w} Urghh ..."

    "Sayaka kreist umher und beugt sich nach vorne, um mich besorgt anzusehen."

    $ hikaface='normal'
    $ sayaface='shocked'
    show Sayaka
    show Hikari

    s "Whoa, ich denke, ich hab noch nie jemanden so Grün anlaufen sehen!{w} Du bist kein großer Fan vom fliegen, was?"

    p "Ach, echt jetzt? Wie kommst du denn darauf?"

    "Ich brauche eine Weile, um mich wieder ordentlich aufrichten zu können.{w} Okay.{w} Ich denke, es geht wieder."

    $ sayaface='normal'
    show Sayaka

    "Während ich mich erholte, sah es so aus, als hätten Sayaka und Hikari bis tief in die Nacht Wache gehalten.{w} Aber es sieht so aus, als sie die Verfolgung nicht aufnehmen möchten.{w} Komisch."

    p "Okay, ich weiß, dass ich euch seit unserem ersten Treffen nur Fragen gestellt hab, aber--"

    s " Falls du dich fragst, wer das komische Mädchen ist ... Ich hab keine Ahnung."

    p "Bist du dir da sicher?{w} Sie sieht genauso aus wie ihr.{w} Ihr wisst schon, wie eine Zauberin, und mit Flügel ..."

    $ sayaface='angry'
    $ hikaface='angry'
    $ hikapose='magical_1'
    show Sayaka
    show Hikari
    with dissolve

    "...Ups.{w} Da hab ich wohl was Falsches gesagt.{w} Sie drehen sich beide mit Feuer in den Augen zu mir.{w} Selbst die sonst so lockere Sayaka scheint jetzt wütend auf mich zu sein."

    h "Hast du uns ernsthaft damit verglichen ...{w}Mit dem Ding?!"

    p "Ahh, das wollte ich nicht--"

    with hpunch

    h "Zwischen uns, und dem, was auch immer sie war, liegen Welten, die uns unterscheiden!"

    h "Zum einen, hast du nicht {i}ihre{/i} Augen gesehen?{w} Sie war komplett verrückt.{w} Keine Spur von Vernunft."

    $ hikaface='scared'
    show Hikari

    "Hikari wickelt ihre Arme um sich selbst, um ein Frösteln abzuwehren."

    h "Es macht mir schon Angst, wenn ich nur an sie denke."

    $ sayaface='normal'
    show Sayaka

    s "Ich schätze, aus deiner Perspektive, Kenta, sieht sie genauso aus wie wir ...{w} Zumindest was das allgemeine Aussehen und die Magie anbetrifft."

    s "Aber an ihr ist alles komisch.{w} Die schwarzen Schatten, die schwarzen Flügel, sogar diese Hörner!{w} Es ist so, als würde sie das komplette Gegenteil von dem sein, was wir sind."

    s "Nicht einmal ihre Magie scheint natürlich ..."

    $ hikaface='normal'
    show Hikari

    p "Äh, und ... eure etwa schon?"

    $ sayaface='smiling'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Natürlich!{w} Wir haben hart dafür gearbeitet, um das zu sein, was wir heute sind!{w} Wir wurden auch nicht so geboren!"

    $ sayaface='normal'
    show Sayaka

    s "Bei ihr ist es so, als wäre es ..."

    "Tief in Gedanken versunken verstummt sie.{w} Mein Gott, ich versteh kein bisschen.{w} Ich weiß nur, dass diese Monster nicht das einzige sind, vor dem ich mich fürchten muss."

    "Anscheinend fertig mit dem Nachdenken, kommt Sayaka wieder zurück zur Realität und lächelt."

    $ sayaface='smiling'
    show Sayaka

    s "Ich denke, wir hatten heute genug Aufregung.{w} Wie wäre es, wenn wir dich jetzt wieder heimbringen?"

    "Sie streckt ihre Hand aus, um mich am Arm zu nehmen, aber ich springe einen Schritt zurück.{w} Ich weiß schon, was sie vorhatte!"

    $ sayaface='shocked'
    show Sayaka

    p "Bitte nicht nochmal fliegen!{w} Wir gehen, okay?{w} Wir GEHEN!"

    $ sayaface='happy'
    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "Aww.{w} Wenn du meinst.{w} Im Himmel ist es aber viel sicherer."

    "Natürlich!{w} Ich kann froh sein, dass ich beim letzten Mal keinen Herzinfarkt bekommen hab."

    "Völlig erschüttert nach all den Ereignissen von heute, machen wir uns auf den Weg nach Hause."


    stop music fadeout 4.0
    scene bg black
    with fade

    "Es dauert nicht lange, bis wir bei mir ankommen.{w} Und ich kann mit Freude sagen, dass wir keine Monster oder Mädchen mit Sensen mehr begegnet sind."
    
    "Ich kann nicht glauben, dass ich mich jetzt jeden Tag darum sorgen muss.{w} Was ist nur aus meinem Leben geworden?!"

    "Als ich die Haustüre erreiche, werde ich jedoch vor einen Problem gestellt.{w} Diese beiden Mädchen bestehen darauf, mich zu beschützen, und waren gerade dabei, mich nach drinnen zu begleiten ..."
    
    "... In MEIN Zuhause."
    play music "bgm/ominousintro.ogg"
    queue music "bgm/ominousloop.ogg"
    "Irgendwie hab ich das Gefühl, als wären meine Eltern nicht wirklich damit einverstanden.{w} Es sind schließlich Mädchen.{w} Außerdem würde das nur noch mehr Fragen aufwerfen ..."
    
    "... und darüber hinaus will ich meine Eltern nur ungern da mitreinziehen."

    "Es dauerte also eine Weile und {i}jede Menge{/i} Verhandlungsgeschick, aber letztendlich konnte ich sie doch irgendwie überzeugen, dass ich zu Hause in Sicherheit bin."

    "Schlussendlich zogen sie sich für die Nacht zurück und gaben mir dadurch etwas Zeit für mich selbst.{w} Wobei sie gesagt haben, sie wären nicht allzu weit weg, sollte etwas sein ...{w} und das bereitet mir Sorgen."

    scene kitchen night
    with fade

    "Ich schließe die Türe und kollabiere fast, da mich selbst die letzte Kraft, die ich noch irgendwie aufbringen konnte, anscheinend verlassen hat."

    p "Was für ein Tag."

    "Mein Kopf und meine Arme tun weh.{w} Meine Beine fühlen sich an, als würden sie jeden Augenblick den Geist aufgeben.{w} Ich kann nicht glauben, dass ich noch immer stehen kann."

    "Der Geruch von Essen liegt und in der Luft und das reicht aus, um mir das Wasser im Mund zusammenlaufen zu lassen.{w} Ah.{w} Genau.{w} Ich hab heute noch gar nichts gegessen."
    
    "Wenn ich den morgigen Tag überleben will, sollte ich das schnellstmöglich nachholen."

    "Anscheinend bin ich gerade noch rechtzeitig, da meine Eltern gerade das Essen hergerichtet haben."

    "Dieses kurze Zeitfenster am Abend ist die einzige Chance, mit meinen Eltern zu essen - abgesehen von Ferien."
    
    "Aus dem Grund schätze ich jedes dieser Abendessen und versuche ihnen immer Gesellschaft zu leisten."

    "Aber heute kann ich kaum noch ein Wort aussprechen.{w} Und grunze - zumindest hört es sich danach an - gerade mal in Richtung, ehe ich in den Stuhl falle ."

    "Während das Essen andauert, tauchen die üblichen Fragen auf, wie zum Beispiel der Tag war.{w} ... Hah.{w} Obwohl man mir meine Erschöpfung ansieht, sage ich, dass der Tag wie jeder andere war."

    "Sie sehen mich besorgt an, aber sie haben keinen Grund, an mir zu zweifeln."

    "Bald darauf geht das Abendessen zu Ende.{w} Und nach einigen Extraportionen, kann ich mir nichts Besseres vorstellen, als ins Bett zu springen.{w} Mit unsicheren Schritten gehe ich auf mein Zimmer."

    scene bedroom night
    with fade

    "Mit dem Kopf voraus lasse ich mich ins Bett fallen.{w} Es ist maximal 21:00 Uhr und ich will schon schlafen.{w} Werden meine zukünftigen Tage alle so ablaufen?{w} Ich hoffe nicht."

    "Obwohl ich in dieser Position ohne Probleme einschlafen könnte, besteht dennoch die Gefahr, dass ich ersticke, von daher sollte ich mich besser anders hinlegen.{w} Ugh."

    "Ich zwinge mich irgendwie vom Bett auf und ziehe die Vorhänge zu."

    "..."

    "Hm.{w} Vielleicht bin ich schon eingeschlafen."

    "Als ich die Vorhänge schließe, werden meine Augen von einem bernsteinfarbenen Leuchten im Garten angezogen."
    
    "Ein Feuer.{w} Ein Lagerfeuer, um genau zu sein.{w} Du hast drei Möglichkeiten, um zu erraten, zu wem das Feuer gehört."

    "Jup.{w} Die beiden 'magischen' Mädchen."

    "Sayaka und Hikari scheinen es sich in meinem Garten gemütlich gemacht zu haben, so richtig mit Zelt und Lagerfeuer.{w} Als sie gesagt haben, sie wären in meiner Nähe, dachte ich nicht, dass sie {i}so{/i} nah sind."

    "Gemessen an der Pfanne über dem Feuer, schätze ich, dass sie versuchen, etwas zu kochen.{w} Mir war nicht klar, dass ihr Leben so hart war, wenn man bedenkt, wie glamourös sie aussehen."

    "Ah, sie haben mich gesehen.{w} Sayaka winkt mir enthusiastisch zu und nimmt dabei die Augen von der Pfanne.{w} Ja, okay, hi.{w} Ich winke halbherzig zurück."

    "Irgendwie habe ich das Gefühl, dass ich mir darüber mehr Sorgen machen sollte, als ich es tu.{w} Aber.{w} Scheiß drauf.{w} Das kann bis morgen warten."

    "Ich ziehe die Vorhänge genau in dem Moment zu, in dem sich unter der Pfanne ein gewaltiges Feuer entfacht.{w} Ich kann Hikaris Schrei des Entsetzens durch das Fenster hören."

    "Mit einem letzten, großen Gähner, falle ich rückwärts auf mein Bett, und es dauert nicht lange, bis ich vollständig ins Land der Träume versinke."
    stop music fadeout 4.0
    scene bg black
    with fade





    scene bedroom day
    with wake
    play music "bgm/everydayintro.ogg"
    queue music "bgm/everydayloop.ogg"
    "Lichtströme dringen durch den Vorhang zu mir durch und holen mich aus meinem so heiß ersehnten Schlaf."

    p "Blughh ..."

    "Mein halber Verstand sagt mir, ich solle mich einfach umdrehen und weiterschlafen, aber die andere Hälfte macht sich bereits Sorgen darüber, ob ich nicht zu spät in die Schule komme."

    "Gehen ...{w} wir's an.{w} Zumindest so gut wie möglich."

    with hpunch

    "Ich rolle unter der Decke hervor und falle mit dem Anmut eines Faultiers auf den Boden.{w} Autsch."

    "Zusätzlich zu dem, was mir gestern schon weh getan hat, tut mir nun auch noch der Kopf weh.{w} Ich wünsche mir nichts sehnlicher als eine Pause.{w} Nur dieses eine Mal!"

    "So als würde ich die Evolution der Menschheit nachholen, entwickle auch ich mich weiter - was mit dem Kriechen am Boden angefangen hat, endet in einem leichten Spaziergang."

    "Hm.{w} Ich sehe in den Garten und sehe nichts.{w} Kein Feuer, kein Zelt, und auch keine Mädchen.{w} Vielleicht hab ich das letzte Nacht alles nur geträumt?"

    "Ich mein, die sind doch sicherlich nicht so dämlich und übernachten direkt in meinem Garten.{w} Das Feuer allein wär schon Grund genug, die Polizei einzuschalten!"

    "Eine Sorge weniger, um die ich mich kümmern muss.{w} Gott sei Dank."

    "Genau!{w} Ich darf keine Zeit verschwenden, sonst verpasse ich noch meine Chance auf ein ordentliches Frühstück."

    "Ich reibe mir meine Augen und gehe ins Badezimmer.{w} Eine schöne, heiße Dusche am Morgen soll ja Wunder bewirken."

    "Ich öffne die Tür zum Badezimmer und--"

    scene cg3
    with wake

    p "Wa ..."

    "Das Badezimmer ist besetzt."

    h "W-Was zum Teufel gaffst du so?{w} Schließ die Tür!"

    p "'Tschuldige, mein Fehler ..."

    scene bg black
    with fade

    "Völlig durcheinander knall ich die Tür wieder zu.{w} Das war echt knapp."

    "...Warte mal 'ne Sekunde.{w} Irgendwas stimmt hier nicht."

    scene cg3
    with dissolve

    "Ich öffne die Tür noch einmal und der Anblick raubt mir den Atem ... Und das, obwohl ich schon wusste, was mich erwartet ..."

    h "Ahh!{w} Was machst du da?!{w} Du Perversling!"

    "Ich wusst ees!{w} Es {i}ist{/i} Hikari!{w} Eine, äh ...{w} eher unangemessen gekleidete Hikari noch dazu.{w} Sie ist genauso überrascht wie ein Reh, das von einem Scheinwerfer angeleuchtet wird."

    "Schenkt man den Socken, die sie gerade auszieht, keine Aufmerksamkeit, trägt sie nur ihre extravagante Unterwäsche.{w} Hm, das passt echt alles zusammen."

    "So wie sie sich nach vorne beugt, können meine Augen nicht anders, als auf ihre--"

    with hpunch

    h "Kenta!"

    p "H-Häh?"

    "Ihr schriller Ton reißt mich aus der Benommenheit, falls es überhaupt eine solche war.{w} Was ...{w} Was wollte ich nochmal machen?"

    h "Was machst du?! Mach jetzt endlich die Tür zu!"

    p "Warte.{w} Wartewartewarte.{w} Sollte ich nicht dir die Frage stellen, was {i}du{/i} in {i}meinem{/i} Haus machst?!"

    h "Wonach sieht's denn aus, du Genie?!{w} Jetzt geh weg!"

    "Ihr Gesicht ist knallrot.{w} Sie bebt fast schon vor Wut, obwohl sie immer noch wie eingefroren am selben Fleck steht.{w} Aber warum bin ich hier der Schuldige?"

    p "Hey, werd jetzt bloß nicht wütend!{w} Ich kann mich nicht erinnern, dass ich euch die Erlaubnis gegeben hab, mein Haus zu betreten.{w} Und erst recht nicht meine Dusche!"

    h "SCHLIESS{w} DIE{w} TÜR."

    p "Erst, wenn du--"

    with hpunch

    h "{i}SCHLIESS{w} DIE{w} TÜR!{/i}"

    p "Okay, aber könntest du ...{w} Äh ..."

    "Ihre Augen leuchten gefährlich und im Badezimmer poltert es durch diese erschreckende Kraft förmlich.{w} ... Äh, ich schätze, das kann warten.{w} Zumindest, wenn ich mein Haus noch länger haben möchte."

    p "O-Okay, okay!{w} Es tut mir leid ...{w} Wirklich!"

    "Mit einem entschuldigenden Lächeln schließe ich nervös wieder die Tür.{w} Wie sich gestern herausgestellt hat, ist der Rückzug manchmal die beste Entscheidung."
    stop music fadeout 3.0
    scene bg black
    with fade

    "Nun.{w} Nach dieser kleinen, äh, 'Situation', finde ich mich unten wieder - in der Gegenwart der beiden Mädchen."

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

    "Sayaka grinst so fröhlich wie immer, während Hikari so aussieht, als wolle sie nach dem nächstgelegenen, scharfen Objekt greifen und mich in Stücke schneiden."
    
    "Ich sag's noch einmal ... WARUM ist das meine Schuld?!"

    p "So ...{w} Findet ihr nicht, dass ihr mir eine Erklärung schuldig seid?"

    s "Hmm?"

    "Sie neigt den Kopf zur Seite und sieht mich verwirrt an.{w} Och, jetzt komm schon!{w} Wie kommt's, dass ich der einzige bin, der das als merkwürdig empfindet?"

    p "Na ja, ich mein ...{w} Was macht ihr bei mir Zuhause?{w} Und warum benutzt ihr mein Eigentum!?"

    $ sayaface='happy'
    $ sayapose='school_2'
    $ hikaface='normal'
    show Hikari
    show Sayaka with dissolve

    s "Oh, das ist einfach!{w} Als wir dich beobachtet haben, haben wir herausgefunden, dass deine Eltern schon früh am Morgen gehen und sonst niemand hier ist."

    s " Also haben wir uns gedacht ...{w} Du weißt schon, wir könnten uns die Dusche ausleihen und so."

    p "...Um es anders auszudrücken, ihr seid eingebrochen."

    $ sayaface='joking'
    show Sayaka

    s "He-hehe-heh-he, das klingt ein bisschen zu extrem.{w} Wir haben darauf geschaut, dass das Fenster auch wieder repariert ist!"

    p "WIE BITTE?!"

    "Ich werfe schnell einen Blick auf alle sichtbaren Fenster.{w} Zumindest ist keines kaputt ...{w} Mein Gott, haben sie etwa einen Stein durch irgendein Fenster geworfen?"
    
    "Und ich dachte, Leute, die die Magie beherrschen, wären schlauer!"

    s "Siehst du?{w} Alles ist gut."

    $ sayaface='happy'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    "Sie versucht ihr Bestes, um mich mit ihrem grenzenlosen Optimismus zu beruhigen.{w} Ich kann aber nicht behaupten, dass ich diesen Optimismus mit ihr teile."

    "Kurz darauf breiten sich auch wieder Kopfschmerzen aus.{w} Und ausnahmsweise kenne ich die Ursache dieses Mal."

    p "Ist das echt nötig?{w} Könnt ihr euch nicht einfach, ihr wisst schon, sauber zaubern, oder so?"

    $ sayaface='normal'
    $ hikapose='school_1'
    show Sayaka
    show Hikari with dissolve

    "..."

    "Sie starren mich beide kalt an.{w} ... Ich hab schon wieder was Falsches gesagt, oder?"

    h "Kenta, unsere Magie ist nicht einfach nur ein bequemes Werkzeug, das wir sorglos im Alltag benutzen können!"

    "Hikari spricht endlich mal wieder und scheint über ihre üble Laune hinweg zu sein."

    h "Es braucht schon viel Energie, um etwas Einfaches zu tun, wie beispielsweise fliegen.{w} Und wir müssen immer sicherstellen, dass wir im Falle eines Überaschungsangriffs genung Energiereserven haben."

    h "Glaubst du wirklich, es wäre eine kluge Idee, diese kostbare Energie für so was zu verschwenden?"

    "Da hat sie recht.{w} Was ich da aber raushöre ..."

    p "Ihr wollt damit also sagen, ihr {i}könntet{/i} es?"

    $ hikaface='angry'
    show Hikari

    "Ihre Augen verengen sich.{w} Sie holt tief Luft und bläst ihre Wangen bedrohlich weit auf.{w} Warum sorge ich mich jetzt plötzlich um meine Ohren?"

    $ hikaface='joking'
    show Hikari

    h "...Du bist ein Idiot."

    $ hikaface='normal'
    show Hikari

    "Stattdessen seufzt sie nur.{w} Mein Trommelfell ist somit für einen weiteren Tag in Sicherheit.{w} Puh."

    with Pause(3.5)

    "Ich werfe einen Blick auf die Uhr.{w} Dieses ganze Drama hat echt viel Zeit gekostet.{w} Wenn ich jetzt nicht bald was esse, schaffe ich es nie rechtzeitig in die Schule."

    p "Dann macht doch, was ihr wollt.{w} Ich mach erstmal was zu futtern."

    hide Sayaka
    hide Hikari
    with dissolve
    with Pause(2.5)
    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka at center
    with dissolve

    "Ich mache mich auf zur Küche, aber Sayaka schneidet mir den Weg ab.{w} Ihre Augen funkeln fast schon, als sie sich nach vorne lehnt."

    s "Oh, du musst dir darüber keinen Kopf machen!{w} Lass {i}uns{/i} Frühstück machen!{w} Betrachte es als Entschuldigung für das Chaos hier.{w} Nicht wahr, Hikari?"

    $ hikaface='shocked'
    show Hikari at right
    show Sayaka at left
    with dissolve

    "Sie zieht Hikari am Arm heran."

    h "W-Was?{w} Ich war nicht einverstanden--"

    s "Nicht wahr, Hikari?"

    with hpunch
    $ hikaface='scared'
    show Hikari

    "In einer fast schon bedrohlichen Tonlage verstärkt sie ihren Griff."

    h "O-Ow, okay!"

    "Hmmm.{w} Die beiden kochen lassen ...{w} Ich weiß ja nicht recht."

    menu:
        "Was soll schon Schlimmes passieren?":


            $ cookedpreviously = True

            "Ich sehe keinen Grund, der dagegen spricht.{w} Sie scheint es nett zu meinen und eine kleine Verschnaufpause nach all dem Stress schadet auch nicht."

            p "Klar.{w} Nur zu."

            $ sayapose='school_1'
            show Sayaka
            with dissolve

            "Sayaka strahlt, wodurch ich mich in meiner Entscheidung bestätigt fühle.{w} H-Hoff ich zumindest."

            s "Du wirst es nicht bereuen!{w} Lehn dich einfach zurück. Wir werden im Handumdrehen etwas Wunderbares für dich kochen!"

            show Sayaka at center with move
            with Pause(0.5)
            show Sayaka at offscreenright
            show Hikari at offscreenright
            with move

            "Und so begibt sie sich mit Hikari, der diese Idee anscheinend gar nicht gefällt, in die Küche."

            "Ich nehme in der Zwischenzeit im Esszimmer Platz und lehne mich zurück.{w} Wird schon schiefgehen.{w} Nicht wahr?"

            with Pause(2.5)

            "Es fängt zumindest schon mal gut an.{w} Ich höre Teller und Besteck klirren."

            play music "bgm/mischiefintro.ogg" fadein 3.0
            queue music "bgm/mischiefloop.ogg"

            h "Weißt du überhaupt, was du machst?"

            s "Darum kümmern wir uns später!{w} Gib davon auch erstmal was rein!"

            "...Ich tu mal so, als hätte ich das nicht gehört."

            "Zusätzlich höre ich auch noch das hektische Zerschneiden von Gemüse - und Hikaris panischen Schrei."

            h "Pass auf, wo du damit hinschwingst, sonst hackst du mir noch den Kopf ab!"

            s "Schon okay."

            h "B-Bist du dir sicher, dass das dazu passt?"

            s "Natürlich!{w} Ich hab ein kreatives Auge für so was."

            h "...Soll es Grün werden?"

            s "Uh."

            s "Mmhmm!"

            h "Das dreht man wohl einfach auf ... So, oder?"

            "Dann höre ich das beunruhigende Auflodern der Flammen.{w} Wie stark drehen sie die Kochplatte bitte auf?!"

            s "Hmm.{w} Was denkst du, was das für ein Zeug ist?"

            h "Ich habe keine Ahnung."

            s "Ach, egal, rein damit!"

            "..."

            "Auf einmal wird es in der Küche still.{w} Ich weiß nicht, ob das gut oder schlecht ist.{w} Ich traue mich ja nicht mal nachzusehen."

            h "I-Ist das wirklich in Ordnung?"

            s "Jup!{w} So soll es--"

            with hpunch

            s "Wahhh!"

            "Und mir nichts, dir nichts, explodiert auf einmal etwas.{w} Dicke Rauchschwaden breiten sich aus.{w} Hmm."

            h "Mach es aus, schnell, sonst breitet es sich noch aus!"

            s "Und wie soll ich das machen?!"

            h "I-Ich weiß nicht!{w} Probier das mal!"

            "Das Geräusch von tosendem Feuer.{w} Im Augenwinkel sehe ich etwas Aufflackern.{w} {i}Hmmmm{/i}."

            s "Nein!{w} Das macht es schlimmer!"

            h "Wie wäre es ...{w} damit?!"

            s "Vielleicht!{w} Es hat vielleicht funktioniert!"

            s "...oder doch nicht.{w} Keine Magie mehr, okay?"

            h "Dieses Mal wird es funktionieren--"

            s "Keine Magie mehr!"

            h "Ich weiß nicht, was wir sonst tun sollen!"

            s "Hyah!"

            h "A-Ah, du verschüttest ja alles!"

            "Spritzendes Wasser.{w} Und noch dazu jede Menge."

            h "Ist es ...{w} Ist es vorbei?"

            s "Hahhh ...{w} Ich denke schon!{w} Und guck, das Essen ist fertig!"

            h "Ich denke wirklich nicht, dass das--"

            s "Ich sagte, das Essen ist fertig!"

            with Pause(2.5)
            play music "bgm/everydayintro.ogg" fadein 2.0
            queue music "bgm/everydayloop.ogg"


            $ sayaface='smiling'
            $ hikaface='scared'
            $ sayapose='school_2'
            show Sayaka at center

            with dissolve

            "Augenscheinlich fertig mit dem, äh, 'Kochen', betreten die beiden den Speisesaal.{w} Sayaka hält einen Teller in ihrer Hand, von dem jede Menge Dampf - oder vielleicht auch Rauch - aufsteigt."

            s "Ich hoffe du bist hungrig, Kenta!{w} Wir haben wirklich alles getan, um das zu kochen!"

            "Mit einem aufrichtigen Lächeln stellt sie den Teller vor mich."

            "I-Ich schätze, sie hat wirklich ihr Bestes gegeben.{w} Aber ...{w} das kann man unmöglich als Essen bezeichnen."

            p "A-Ah.{w} Das ist ...{w} äh ..."

            "Auf dem Teller liegen verkohlte, verbrannte und knusprige Überreste von dem, was vielleicht irgendwann mal Essen war.{w} Selbst das Einatmen von dem Zeug könnte tödlich enden."

            "Ich sehe, wie Hikari in der Zwischenzeit weiter hinten lauert ...{w} Sichtlich enttäuscht von dem 'Gift', das sie mir da zubereitet haben."

            "Ich schätze, das ist meine Schuld, schließlich hab ich sie auch in die Küche gelassen.{w} Jetzt sollte ich auch die Verantwortung übernehmen und--"

            menu:
                "Iss das Essen.":
                    "Ich hab keine andere Wahl, oder?{w} Sie hat schließlich echt hart gearbeitet, um dieses...{w} 'ETWAS' zuzubereiten."

                    p "D-Dann probier ich mal ..."

                    "Ich steche leicht auf die Substanz ein.{w} Und das reicht, damit es zu einem feinen Pulver zerfällt.{w} Okay."

                    "Ich bin sicher, dass es, obwohl es so gefährlich {i}aussieht{/i}, ziemlich gut schmeckt.{w} Vielleicht verbirgt sich unter all diesem verbrannten Zeugs ...{w} ja irgendetwas Leckeres."

                    "Ich gebe so viel wie nur möglich auf meinen Löffel und koste es - trotz meiner Instinkte, die mich davor gewarnt hatten."

                    "Es ...{w} Es ist ..."

                    $ sayaface='happy'
                    show Sayaka

                    s "Es ist mega, oder?"

                    "Sayaka lehnt sich erwartungsvoll nach vorne."

                    "So schmeckt also Holzkohle."

                    "Ich wehre mich gegen den Drang, mich zu übergeben, und lächle ihr zu."

                    p "M-Mmm!"

                    $ sayapose='school_1'
                    show Sayaka
                    with dissolve

                    s "Wirklich?{w} Ja, ich wusste es!{w} Du solltest uns {i}jeden{/i} Morgen für dich kochen lassen!"

                    "Oh Gott.{w} Was hab ich bloß getan?{w} Und von dem ganzen Zeug gibt's noch einen ganzen Teller voll!{w} Diese Mädchen sind für meine Gesundheit und für mein Wohlbefinden eindeutig eine Gefahr."
                "Weigere dich, das zu essen. Ich möchte nicht sterben!":

                    "Okay, ja, also nein.{w} Ich muss hier endlich mal Stellung beziehen, sonst wird es nur noch schlimmer."

                    p "Schau, es tut mir leid, Sayaka, aber ich krieg das echt nicht runter."

                    $ sayaface='normal'
                    show Sayaka

                    s "Häh?{w} Warum nicht?"

                    "Sie neigt ihren Kopf zur Seite und sieht mich finster an.{w} Na großartig, wenn du mich jetzt auch noch wie ein Monster aussehen lässt!"

                    p "Es ist ...{w} na ja ...{w} wie soll ich sagen, ohne ausfällig zu werden?"

                    "Ich sehe noch einmal zu der giftigen Substanz hin, in der Hoffnung, dass sie nicht noch aufsteht und von selbst abhaut."

                    p "Würde ich es essen, könnte ich heute nicht mehr zur Schule gehen.{w} Oder den Tag danach."

                    s "Oh?"

                    p "Sayaka, was ich damit sagen möchte, ist ... Ich würde sterben.{w} Es sieht verdammt giftig aus."

                    $ sayaface='scared'
                    show Sayaka

                    s "Oh."

                    "Sie blickt immer finsterer drein.{w} Tut mir leid.{w} Das musste einfach sein."

                    $ sayaface='normal'
                    show Sayaka

                    s "Bist du dir sicher?{w} Es kann nicht {i}so{/i} schlecht sein."

                    "Wirklich?{w} WIRKLICH?!{w} Wie kann man so was überhaupt in Schutz nehmen? ...{w}Etwas ...{w} das ja nicht mal aussieht wie Essen!"

                    p "Okay, warum probierst du dann nicht zuerst?"

                    $ sayaface='scared'
                    $ sayapose='school_1'
                    show Sayaka
                    with dissolve

                    "Sie zieht ein langes Gesicht.{w} Wusst' ich's doch."

                    s "Ä-Ähh, ich hab schon gegessen."

                    p "Schau, warum versuchst du--"

                    $ sayaface='happy'
                    show Sayaka

                    s "Aber ich weiß, dass Hikari nichts gegessen hat!{w} Sie kann dir zeigen, wie ungefährlich und lecker es ist!"

                    $ hikaface='shocked'
                    $ hikapose='school_2'
                    hide Sayaka
                    show Hikari at center
                    with dissolve

                    h "H-Hä?{w} Ich?!"

                    "Noch immer in auflauernder Position, springt Hikari plötzlich, als ihr Name in Zusammenhang mit dem Essen, bei dem sie mitgeholfen hat, es zum Leben zu erwecken, erwähnt wurde."

                    $ sayaface='smiling'
                    show Sayaka at left
                    show Hikari at right
                    with dissolve

                    s "Ja!{w} Komm rüber und zeig Kenta, wie gut es schmeckt!"

                    h "Das kann nicht dein Ernst sein.{w} Das Zeug ist--"

                    s "Total ungefährlich und essbar!{w} Jetzt komm rüber.{w} Bitte."

                    $ sayapose='school_2'
                    $ hikaface='scared'
                    with hpunch
                    show Sayaka
                    show Hikari
                    with dissolve

                    "Sayaka stößt kraftvoll mit einem Finger auf den Tisch.{w} Trotz des breiten Grinsens habe ich das Gefühl, als würde sich dahinter etwas Unheimliches verbergen."

                    h "...Fein."

                    "Sie nähert sich langsam dem Essen, wobei jeder Schritt länger dauert als der vorige.{w} Es hinterlässt den Anschein, als würde sie in den Tod marschieren ... Was ja durchaus an das Mögliche grenzt."

                    $ sayaface='happy'
                    show Sayaka

                    h "Wir haben es gemacht ...{w} also kann es nicht so schlecht sein.{w} Es ist einfach nur ein bisschen ...{w}knusprig."

                    "Sie streckt eine zitternde Hand zum Essen hin aus ... So langsam, wie wenn das Essen beißen würde.{w} Und dann ..."

                    $ sayapose='school_1'
                    $ hikapose='school_1'
                    $ sayaface='shocked'
                    $ hikaface='normal'
                    show Sayaka
                    show Hikari
                    with flash

                    "...Dringt ein magischer Blitz aus ihrer Handfläche heraus, der das Essen vollständig zersetzt.{w} Leider auch den Teller.{w} ... Und ein gutes Stück vom Esstisch."

                    $ hikaface='joking'
                    show Hikari

                    h "Hoppla!{w} Ich bin ja so tollpatschig.{w} Meine Hand ist wohl ...{w} ausgerutscht.{w} Wie schade!{w} Und ich habe mich schon {i}so{/i} gefreut, alles aufzuessen."

                    "...Ich bin mir ziemlich sicher, die Hand ist dir nicht bloß 'ausgerutscht'.{w} Und war nicht sie diejenige, die gesagt hat, sie würde Magie nicht für belanglose Zwecke verschwenden?"

                    "...Vielleicht war es in ihren Augen ja ein Notfall."

                    $ sayaface='scared'
                    show Sayaka

                    s "Hikari!"

                    "Sayaka schaut ein weiteres Mal böse drein, aber es dauert nicht lang, bis ihr gewohnter Optimismus zurückkehrt."

                    $ sayapose='school_2'
                    $ sayaface='happy'
                    $ hikaface='scared'
                    show Sayaka
                    show Hikari
                    with dissolve

                    s "Oh, naja.{w} Wie wäre es, wenn ich mehr mache?"

                    $ sayaface='shocked'
                    show Sayaka
                    with hpunch

                    p "Nein!"

                    "Ich springe auf, wobei ich meinen Stuhl fast schon mitnehme.{w} Ich mach mir echt Sorgen um mein Haus!"

                    "Vielleicht etwas lauter als beabsichtigt, erwische ich sie unvorbereitet."

                    s "H-Häh?"

                    p "Ich mein, wir würden zu spät zur Schule kommen, wenn ihr noch was kochen würdet."

                    s "Oh ...{w} Du hast recht.{w} Guck auf die Uhr!"

                    "Puh.{w} Gerade noch mal gerettet"
        "Sicher nicht!":

            "Als ob ich schon eine Vorahnung von dem hätte, was passieren könnte, zögere ich keine Sekunde."

            "Selbst wenn ich nicht wirklich gut kochen kann, bin ich mir sicher, dass ich dabei nicht mein Haus zerstören werde."

            $ sayapose='school_1'
            $ sayaface='normal'
            $ hikaface='normal'
            show Sayaka
            show Hikari
            with dissolve

            s "Awww.{w} Bist du dir sicher?"

            p "Und wie.{w} Aber ich weiß den Gedanken zu schätzen."

            "Sie bläst ihre Wangen auf und macht einen hübschen Schmollmund, aber kurz darauf kehrt auch wieder ihr strahlendes Lächeln zurück."

            $ sayaface='smiling'
            show Sayaka

            s "Okay.{w} Du lässt dir aber echt was entgehen!{w} Mir wurde schon öfters nachgesagt, dass mein Essen 'speziell' ist!"

            $ hikaface='scared'
            show Hikari

            h "Sayaka, ich denke nicht, dass sie meinten--"

            $ sayaface='happy'
            show Sayaka

            s "Und ob. Sie sagten, ich sollte nie wieder kochen, weil ich andere Leute damit neidisch machen würde!{w} Kannst du dir das vorstellen?"

            "Ja.{w} Ich bin glücklich mit meiner Entscheidung.{w} Ich hab das Gefühl, als wär ich einer Kugel ausgewichen.{w} Einen schrecklichen Geschmack, der meine Geschmacksnerven zerstört hätte."

            "Ich mache die einfachste Speise, die mir einfällt, während ich gleichzeitig auf die beiden aufpasse.{w} Und so wie Sayaka herumzappelt, würde sie mir am liebsten dabei helfen.{w} Ich weiß, was du vorhast!"

    stop music fadeout 5.0        
    scene bg black
    with fade

    "Kurz darauf endet das Frühstück, das dieses Mal für einen etwas lebhafteren Start in den Tag sorgte, auch schon wieder."

    "So sehr sie mir auch Kopfzerbrechen bereiten, so war es dennoch schön, mal nicht allein zu sein.{w} Aber das sage ich den beiden natürlich nicht, weil wer weiß, was sie sich dann noch einfallen lassen."

    "Mit meinen beiden Bodyguards an meiner Seite gehe ich zur Schule.{w} Langsam gewöhne ich mich daran.{w} Allerdings weiß ich nicht, ob das gut oder schlecht ist."
    play music "bgm/everydayintro.ogg" fadein 2.0
    queue music "bgm/everydayloop.ogg"

    with Pause(3.5)

    "Die Reise zur Schule verläuft friedlich, ohne auch nur ein einziges Monster zu sehen.{w} Trotzdem hab ich das Gefühl, als würde mich irgendwas oder irgendjemand beobachten."

    "Ach, vielleicht werd ich nach den beiden Anschlägen auf mein Leben einfach ein wenig paranoid.{w} Ich bin sicher, ich bilde mir das bloß ein!"



    scene classroom
    with fade

    "Ich komme sogar überpünktlich in der Schule an.{w} Hm.{w} Das passiert mir auch nicht oft."

    $ sayaface='smiling'
    $ hikaface='normal'
    $ sayapose='school_1'
    $ hikapose='school_1'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "Sayaka und Hikari bleiben dicht an meiner Seite.{w} Zu dicht.{w} Ich spüre schon, wie mich meine Klassenkameraden schief anstarren.{w} Ich will gar nicht wissen, wie das für Außenstehende aussieht."

    p "Hey, Mädels?"

    s "Hm?{w} Was ist los?"

    p "Müsst ihr mir echt so sehr auf die Pelle rücken?{w} Ich weiß zu schätzen, was ihr alles für mich tut, aber wir sind hier in der Schule."

    $ hikaface='angry'
    show Hikari

    h "Aber was ist, wenn--"

    p "Solange ihr in meiner Nähe bleibt, sollte es doch passen, oder?{w} Außerdem glaub ich kaum, dass es ein Monster so einfach ins Klassenzimmer schafft, ohne vorher einen Wirbel zu machen."

    $ hikaface='normal'
    show Hikari

    "Hikari wird still.{w} Sie verengt ihre Augen, verschränkt ihre Arme und wirft den Kopf zur Seite."

    h "Fein.{w} Was auch immer."

    hide Hikari
    show Sayaka at center
    with dissolve

    "Sie stürmt zu ihrem Tisch und lässt sich in den Stuhl fallen, ihre Augen geradewegs nach vorne gerichtet."

    p "Ähh ...{w} Hab ich sie wütend gemacht?"

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Ah, keine Sorge.{w} Sie ist immer so.{w} Gib ihr einfach Zeit, bis sie, äh, weniger grimmig ist."

    s "Sie macht sich nur Sorgen um deine Sicherheit und darüber, was passieren würde, wenn sie weg wäre."

    s "Würde es nach mir gehen, dürftest du nicht mal in die Schule gehen.{w} Wir würden dich einfach in einem kleinen, schönen Raum einsperren und warten, bis alles vorbei ist."

    "...Ich bin mir nicht sicher, dass sie gemerkt hat, wie beängstigend sich das gerade angehört hat, wenn ich den Grinser in Betracht ziehe."

    $ sayaface='smiling'
    show Sayaka

    s "Du hast aber recht.{w} Vielleicht {i}haben{/i} wir dir ein bisschen die Lüft abgeschnürt.{w} Ich denke, wir können es uns leisten, wenigstens in der Schule zu entspannen."

    p "Danke."

    "Ich seufze.{w} Endlich lassen sie sich mal belehren ... Wenn auch nur ein kleines bisschen!"

    hide Sayaka
    with dissolve

    "Die Glocke läutet und signalisiert somit den Beginn des Unterrichts.{w} Auf dem Weg zu meinem Tisch komme ich an einer verärgerten Hikari vorbei.{w} Sie sieht mich nicht mal an.{w} Echt gemein."

    scene bg black
    with fade

    with Pause(5.0)

    scene classroom
    with fade

    "Der Vormittagsunterricht vergeht wie im Flug, wodurch auch die Pause nicht lange auf sich warten lässt."

    "Ich stehe auf und gähne, und bemerke dabei, dass ich nicht allein bin."

    $ sayapose='school_1'
    $ hikapose='school_2'
    show Sayaka at left
    show Hikari at right
    with dissolve

    p "...Jetzt kommt schon.{w} Darüber haben wir schon mal geredet!"

    "Als ob das Gespräch heute Morgen nie stattgefunden hätte, umgeben mich bereits meine beiden Beschützer."

    s "Was gibt's, Kenta?{w} Wollen wir nicht essen gehen?"

    p "Ich hol mir mein eigenes Essen.{w} Ihr müsst nicht an mir kleben.{w} Ihr habt doch bestimmt auch andere Dinge zu erledigen, oder?"

    $ sayaface='normal'
    show Sayaka

    s "Aber wir sind--"

    p "Was weiß ich!{w} Irgendetwas.{w} Scheißegal was!{w} Ich hab euch erst gestern kennengelernt, und ihr seid schon so anhänglich.{w} Ich hätte gern etwas Platz für mich selbst!"

    "Ich bin echt dankbar, dass sie hier sind.{w} Anderenfalls hätte ich den gestrigen Tag bestimmt nicht überlebt."
    
    "Aber das hier grenzt ja an Stalking.{w} Und vom Camping in meinem Garten möchte ich gar nicht erst anfangen!"

    $ sayaface='smiling'
    show Sayaka

    s "Oh, okay.{w} Ich versthe.{w} Hikari versteht's auch.{w} Denke ich."

    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Hmph."

    s "Komm schon, Hikari!{w} Es macht bestimmt Spaß, die Schule zu erkunden.{w} Wir hatten vorher schließlich keine Zeit, um uns mal umzugucken!"

    "Sie war nie in der Schule ...?{w} Wo kommen die beiden denn sonst her?{w} Desto mehr ich mit ihr rede, desto mehr hört sich das für mich nach einem Alien an."

    s "Also dann, Kenta.{w} Wir gehen dann mal unseren eigenen Weg.{w} Schrei einfach, wenn du uns brauchst und versuch, nicht zu streben!"

    hide Sayaka
    show Hikari at center
    with dissolve

    "Und so marschiert sie los und summt dabei eine fröhliche Melodie vor sich hin.{w} Hikari folgt ihr hinterher, aber nicht, ohne mir einen letzten eisigen Blick zuzuwerfen."
    
    "Irgendwie frieren meine Schultern auf einmal.{w} Brrr."

    hide Hikari
    with dissolve
    with Pause(2.5)

    "Na ja.{w} Ich hab's geschafft.{w} Ich hab die beiden endlich überredet, mir ein wenig Freiraum zu geben.{w} Zumindest fürs Erste."

    "..."

    "Aber was jetzt?"

    "Zuerst sollte ich mal schauen, dass ich nicht wieder auf mein Essen vergesse.{w} Ansonsten haben die dunklen Mächte, die da draußen auf mich lauern, ein leichtes Spiel."

    "Ich gehe in die Cafeteria."

    scene cafeteria
    with dissolve

    "Die Cafeteria ist, wie man es in der Pause erwartet, komplett voll.{w} Die Massen an Schülern beanspruchen selbst den kleinsten freien Platz, der sich zwischen den Tischen noch finden lässt."

    "Langsam arbeite ich mich nach vorne durch.{w} Aber es ist schließlich nie einfach, an Essen zu kommen!"

    "Irgendwann nähere ich mich dann dem Schalter.{w} Logisch, dass die Auswahl nach all den Schülern vor mir nur noch sehr beschränkt ist."

    "Na ja, ich schätze, entweder ...{w} dieses Sandwich{w} ... oder das hier.{w} Wobei keines von den beiden ziemlich appetitlich aussieht.{w} Ach, scheiß drauf.{w} Ich hab Hunger, da isst man alles!"

    "Mit einem billigen Sandwich in der Hand schaue ich mich nach einem Tisch um.{w} Aber sie sind alle besetzt.{w} Außer einer, am anderen Ende, auf dem eine mir vertraute Person sitzt."

    "Selbst aus der Entfernung kann ich dank dem braunen Haar sofort erkennen, dass es Sayaka ist."

    "Aber ich sehe Hikari nirgends.{w} Anscheinend haben sich ihre Wege irgendwo getrennt."

    "Ich schätze, Sayakas Tisch ist der einzige, an dem ich einen Platz finde, aber möchte ich dort wirklich sitzen?{w} Es ist so laut, dass es schon wieder nervig ist."

    "Völlig versunken in ihrem Essen, hat sie mich anscheinend auch noch nicht entdeckt.{w} Vielleicht schaff ich es noch, auf das Dach zu entkommen, wo es bestimmt ruhiger ist."

    menu:
        "Geh aufs Dach.":

            $ hikari += 1

            "Also auf zum Dach.{w} Es ist schon so extrem laut hier, und wenn ich mich mit Sayaka rumschlagen müsste, würde das das Ganze noch die Krone aufsetzen."

            "Ich schleiche mich an ihr vorbei und gehe zu den Treppen.{w} Allerdings war das nicht sonderlich schwer, wenn man bedenkt, wie vertief sie in ihr Essen ist."

            scene bg black
            with fade

            "Desto höher ich die Treppen hinaufsteige, desto ruhiger wird es, bis schließlich überhaupt nichts mehr zu hören ist.{w} Ah, endlich Ruhe."

            scene school roof
            with wake

            "Ich öffne die Tür.{w} Eine sanfte Brise und ein fast wolkenloser Himmel begrüßt mich.{w} Hier oben ist es perfekt."

            "Nur ...{w} eines stört mich, und das ist die Tatsache, dass ich anscheinend nicht der einzige bin, der diese Idee hatte."

            $ hikaface='normal'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            "Hikari steht am Rand des Daches und beobachtet die Menschen unten.{w} So aufmerksam wie sie die Menschen beobachtet, kann ich nur davon ausgehen, dass sie Wache hält."

            "Ich muss sie für ihre Hingabe echt bewundern.{w} Wenn sie es so ernst meint, fühle ich mich gleich wesentlich sicherer."

            "Da sie mich anscheinend noch nicht bemerkt hat, schätze ich mal, dass sie zu vertieft ist."

            "Ohne Bemühung, mich vor ihr zu verstecken, gehe ich zu ihr hin.{w} Noch immer nichts.{w} Sieht aus, als wäre sie geistig ganz woanders."

            "Ich klopfe ihr sanft auf die Schulter."

            p "Yo."

            $ hikaface='shocked'
            show Hikari
            with hpunch
            with hpunch

            h "Wahh!"

            "Sie springt ziemlich hoch in die Luft und lässt einen Schrei los, der mein Trommelfell beinahe zerplatzen lässt.{w} Éin ...{w} bisschen übertrieben, oder?{w} Oder muss man wirklich so viel Angst vor mir haben?"

            "Mit einer Hand zur Brust haltend, dreht sie sich zu mir um.{w} Als sie bemerkt, dass ich es bin, entspannt sie sich ein wenig.{w} Aber sie sieht trotzdem noch wütend aus."

            $ hikaface='angry'
            $ hikapose='school_2'
            show Hikari
            with dissolve

            h "Oh, Kenta, du bist es nur.{w} Erschreck mich doch nicht so!{w} Du hattest Glück, dass ich dich nicht sofort zerfetzt habe!"

            "Mit einem Grinsen kratze ich mich am Hinterkopf.{w} Ich hab sie wirklich erschreckt."

            p "Meine Schuld.{w} Hältst du die Stellung?"

            $ hikaface='normal'
            show Hikari

            h "Häh?"

            "Ihre Augen fixieren sich wieder auf die Stelle, die sie vor einem Moment noch beobachtet hatte."

            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "Ja.{w} Obwohl es in der Schule bisher friedlich verlaufen ist, weiß man nie, wann der Feind zuschlagen könnte."

            p "Danke.{w} Ich weiß es zu schätzen."

            $ hikaface='shy'
            show Hikari

            h "N-Nicht der Rede wert.{w} Ich mach das auch für die Sicherheit der Schule, nicht nur für dich!"

            "Ihr Gesicht zeigt einen interessanten Ton von Rosa.{w} Es braucht echt nicht viel, um sie aus der Fassung zu bringen, was?"

            p "Klar, schon gut.{w} Ich hab schon verstanden."

            $ hikapose='school_2'
            $ hikaface='angry'
            show Hikari
            with dissolve

            h "Denn während Sayaka und ich den Anstand haben, unsere Kräfte vor normalen Menschen zumindest zu verbergen, kann ich nicht sagen, dass die Schatten dasselbe tun werden. Es ist schon schlimm genug, dass sie versucht haben, dich am hellichten Tag anzugreifen."

            $ hikaface='normal'
            show Hikari

            h "Ich versteh es einfach nicht.{w} Es widerspricht allem, was wir bisher über sie wissen."

            "Sie seufzt pathetisch und dreht sich wieder um, um wieder über die Schule zu wachen."

            $ hikaface='embarrassed'
            show Hikari

            "Ich öffne meinen Mund, um ihr etwas zu sagen, aber ein leises, rumpelndes Geräusch unterbricht mich dabei."

            p "...Hikari?"

            h "J-Ja ..?"

            "Sie antwortet, ohne sich umzudrehen.{w} Es war nicht sonderlich schwer, um zu erkennen, was das für ein Geräusch war."

            p "Hast du, äh, noch nicht gegessen?"

            "..."

            "Stille.{w} Da hab ich den Nagel wohl auf den Kopf getroffen."

            $ hikaface='normal'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "Es ist nicht meine Schuld!{w} Diese Cafeteria ist so laut und dreckig, dass ich keinen weiteren Moment darin ertragen kann.{w} Ich weiß nicht, wie Sayaka freiwillig da unten essen kann."

            h "Ich hab sowieso wichtigere Sachen zu tun."

            p "Und kannst du mit einem leeren Magen auch kämpfen?"

            h "Natürlich!{w} Was denkst du--"

            $ hikaface='shy'
            show Hikari

            "Und wieder knurrt ihr Magen."

            h "..."

            p "Ah."

            $ hikaface='normal'
            $ hikapose='school_2'
            show Hikari
            with dissolve

            h "Okay, ich bin vielleicht etwas hungrig.{w} Aber ich werde nicht in diese Grube zurückkehren."

            "Meine Güte.{w} Ich weiß, dass es dort immer wieder viel los ist, aber so schlimm ist es nun auch wieder nicht.{w} Ich schätze, sie fühlt sich in solchen Menschenmassen einfach nicht wohl."

            "Und packe das Sandwich, das ich fast vergessen hatte, aus, und beiße einmal ab."

            "Hikari beobachtet mich aufmerksam, wie ich noch ein paar weitere Bissen vom Sandwich nehme.{w} Ich kann den Hunger in ihren Augen förmlich riechen."

            "Da ich mir fies dabei vorkomme, höre ich mittendrin auf.{w} Wahrscheinlich hätte sie mir das Sandwich anderenfalls sowieso mit Gewalt aus der Hand gerissen."

            p "Willst du auch was?{w} Falls ja, ich kann mit dir teilen."

            $ hikaface='angry'
            show Hikari

            "Ihre Fressluke hängt weit geöffnet nach unten.{w} Da fehlt nicht mehr viel, und sie sabbert."

            $ hikapose='school_1'
            show Hikari
            with dissolve

            "Mit einem abrupten 'Hmph' scheint sie ihre Entscheidung getroffen zu haben und dreht daraufhin ihren Kopf zur Seite.{w} Damit hätte ich rechnen sollen."

            h "S-Sei doch nicht lächerlich!{w} Warum würde ich etwas wollen, worauf du schon gesabbert hast?"

            h "Ich würde lieber verhungern ...{w} als ..."

            $ hikaface='scared'
            show Hikari

            "{i}Gruuuu{/i}.{w} Ihr Magen bettelt förmlich nach Nahrung."

            h "O-Okay, gut.{w} Vielleicht ein bisschen."

            with hpunch
            $ hikaface='normal'
            $ hikapose='school_2'
            show Hikari
            with dissolve

            "Ich breche die Hälfte vom Sandwich ab und gebe es ihr, ehe sie es mir noch widerwillig aus der Hand reißt."

            h "Danke dir.{w} S-Sagt man in einer solchen Situation wohl."

            "Ich glaube nicht, dass sie es gewohnt ist, so was zu sagen.{w} Wir machen endlich Fortschritt!{w} Da muss ich doch glatt lächeln."

            $ hikaface='angry'
            show Hikari

            h "Wisch dieses ekliche Grinsen aus deinem Gesicht.{w} Ich weiß nicht, woran du denkst, aber ich bin mir sicher, dass es etwas Unanständiges ist."

            "Sagt sie mit einem Knurren, bevor sie ihren Teil des Sandwichs mit den Zähnen zerfleischt."

            p "Und, gut?"

            $ hikaface='normal'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "...Es ist okay.{w} Nicht das beste, was ich hatte, aber auch nicht das schlechteste. Damals an der Akademie, habe ich-"

            $ hikaface='shocked'
            show Hikari

            "Sie hört kurz auf zu essen und macht große Augen.{w} Ich glaube, da hätte sie beinahe etwas ausgeplaudert.{w} Ich wünschte wirklich, sie würden daraus nicht so eine Art Staatsgeheimnis machen."

            p "Die Akademie, hm?"

            $ hikaface='normal'
            show Hikari

            h "S-Schon gut."

            p "Aber ich bin mir ziemlich sicher, dass ich was--"

            with hpunch
            $ hikapose='school_2'
            $ hikaface='angry'
            show Hikari
            with dissolve

            h "Du hast nichts gehört! {i}Nichts{i}!"

            "Huch."

            "Trotz ihrer kleinen Figur, komme ich mir dank ihrer dominanten Stimme immer wieder wie eine Maus vor."
            
            "Sofern ich nicht so enden möchte wie das Monster, sollte ich nicht versuchen, noch mehr Infos aus ihr rauszubekommen."

            p "Okay, okay!{w} Ich hab überhaupt nichts gehört.{w} War ...{w} wohl nur der Wind oder so"

            $ hikaface='normal'
            show Hikari

            "Sie seufzt und wirft ihr Haar zur Seite, wobei die Wut genauso schnell verschwand, wie sie aufgebaut wurde."

            h "Wir halten keine Informationen zurück, um einfach nur mysteriös zu wirken, weißt du."

            "Verarsch doch jemand anderen!"

            h "Es ist ...{w} der einfachere Weg.{w} Es hat keinen Sinn, dich in dieses Durcheinander zu ziehen, wenn wir es vermeiden können.{w} Ich wünsche niemandem ein solches Leben ..."

            "Und obwohl sie noch immer kaut, wird ihr Gesichtsausdruck immer düsterer - wahrscheinlich deshalb, weil das Sandwich immer kleiner wird."
            
            "Ich bin mir nicht mal sicher, ob sie überhaupt weiß, dass sie gerade isst."

            "Sie denkt ein paar Momente über etwas nach, bevor sie mich mit einem ernsten Blick ansieht."

            h "Kenta, was würdst du tun, wenn du ..."

            "Eine Gruppe von Schülern taucht plötzlich mit Essen in der Hand auf dem Dach auf.{w} Hikari hingegen wird mucksmäuschenstill und kehrt wieder zu ihrem Wachposter zurück."

            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "...Vergiss es.{w} Es ist nicht wichtig."

            p "Wenn du, äh, meinst."

            "Es {i}sah{/i} extrem wichtig aus, wenn ich bedenke, dass sie mich sonst nie so ernst angesehen hat.{w} Was für ein Gluck, dass die ausgerechnet jetzt auftauchen müssen."

            "Jeder Anschein eines Gesprächs ist jetzt vernichtet.{w} In der Gegenwart von anderen Menschen scheint sie viel zurückhaltender zu sein."
            
            "Und ich denke auch, dass das, worüber wir geredet haben, nicht für diese Ohren gedacht ist."

            h "...Nebenbei, das Sandwich hat wirklich gut geschmeckt."

            p "Häh?"

            $ hikaface='shy'
            show Hikari

            h "N-Nichts."
        "Setz dich zu Sayaka.":


            $ sayaka += 1

            "Aber ...{w} bin doch wohl nicht so dumm und mache mir die Arbeit, aufs Dach zu gehen, wenn hier ein Platz frei ist.{w} Und wer weiß, vielleicht wäre ich dort sowieso nicht allein.{w} Also auf zum Tisch."

            scene cg19
            with dissolve
            play music 'bgm/magicalgirlintro.ogg' fadein 2.0
            queue music 'bgm/magicalgirlloop.ogg'

            "Ihre gehe auf Sayaka, derer Augen beim Anblick von mir aufleichten, zu."

            s "Mffgh!"

            "Mit vollem Mund versucht sie, mich anzusprechen, aber stattdessen fliegt das Essen kreuz und quer.{w} Meine Fresse, mit vollem Mund spricht man nicht."

            p "Hey.{w} Kann ich mich hier hinsetzen?"

            s "Mgffgh, mff!"

            "Sie nickt energisch und schauffelt dabei weiter Essen in ihren Mund.{w} Ich weiß zwar nicht, was das heißen soll, aber ich nehme mal an, es geht in Ordnung."

            "...Ich hab es vorhin nicht wirklich bemerkt, aber auf ihrem Teller ist ja noch mehr Essen als erwartet.{w} Genug für ZEHN Schüler!"

            "Ich frage mich, wie sie an so viel gekommen ist.{w} Kein Wunder, dass die Auswahl so mickrig war."

            "Vielleicht hat sie ihre Magie eingesetzt, um andere dazu zu überreden, ihr mehr zu geben?{w} ... Gruselig, wenn es wirklich so einfach für sie ist, die Schule um ihren Finger zu wickeln."

            "Ich mein, sie hat gerade erst auf diese Schule gewechselt und bekommt schon Extraportionen.{w} Aber wo endet das Ganze?{w} Das lässt Schlimmes erahnen."

            "Mit zu ihr setzend packe ich mein Sandwich aus.{w} Jup.{w} Genauso fad, wie ich es mir vorgestellt hab.{w} Und genauso, wie ich es mag."

            s "Hey!{w} Ich dachte, du wolltest ein bisschen Zeit für dich selbst?"

            "Anscheinend fertig mit dem Essen, spricht sie schließlich mit mir.{w} Aber ich seh schon, dass das nicht lange dauern wird.{w} Sie ist schließlich wie eine Maschine."

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

            s "Schon okay, du kannst zugeben, dass du mich {i}so{/i} arg vermisst hast und keinen weiteren Moment ohne mich aushalten konntest.{w} Ich werde es Hikari schon nicht erzählen."

            "Sie grinst und beißt noch einmal ab."

            p "Hah.{w} Lustig.{w} ... Wo ist Hikari?{w} Ich dachte, sie wär bei dir."

            $ sayapose='school_1'
            show Sayaka
            with dissolve

            s "Omff!{w} Shmff--"

            p "Äh, schon okay, nur keine Hektik.{w} Es ist nicht dringend."

            "Ich hebe meinen Arm, um mich vor den heranfliegenden Essenresten zu beschützen.{w} ... Widerlich."

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

            s "Ich sagte, sie mag die Menschenmengen und den Lärm nicht, also ging sie alleine davon und da sagte sie irgendwas von einem ruhigeren Ort."

            p "Glaubst du, dass es ihr gut geht?"

            s "Mff--warscheinlich."

            $ sayaface='happy'
            show Sayaka

            "Und noch ein Bissen.{w} Die Hälfte von dem Essen, das noch da war, als ich ankam, ist schon weg.{w} Wo versteckt sie das in ihrem Körper bloß?"

            $ sayaface='smiling'
            $ sayapose='school_1'
            show Sayaka
            with dissolve

            s "Ich denke, wir werden es wissen, wenn ihr etwas zustößt.{w} Oder besser gesagt, die ganze Schule wird Bescheid wissen.{w} Sie entwickelt verrückte Kräfte, wenn sie wütend wird!"

            p "Das hört man gerne.{w} ... Hoff ich zumindest."

            "Heißt also, wenn die komplette Schule in Aufruhr verfällt, dann ist Hikari was passiert."

            p "Äh, wie gefällt es dir hier?{w} Wenn ich mich recht erinnere, hast du doch gesagt, dass du noch in einer Schule warst, oder?"

            $ sayaface='happy'
            show Sayaka

            s "Oh, ja!{w} Es ist super.{w} Es ist jeder so freundlich und das Essen schmeckt {i}ausgezeichnet{/i}!"

            "Als ob sie das besonders hervorheben wollte, sticht sie mit einem fast leuchtendem Gesicht in ihr Essen."

            $ sayaface='smiling'
            show Sayaka

            s "Und vielleicht hätte ich es besser formulieren sollen.{w} Es ist nicht so, als wären Hikari und ich nie zur Schule gegangen ...{w} Wir waren halt nicht ...{w} also, auf einer normalen Schule."

            p "Was, wart ihr etwa auf einer Zauberschule, oder so was in der Art?"

            $ sayapose='school_2'
            show Sayaka
            with dissolve

            s "Mmhmm!"

            "Ich meinte es nicht wirklich ernst ...{w} und ich hab auch nicht erwartet, dass sie mit solch einer Entschlossenheit darauf antwortet."

            p "W-Wirklich?"

            $ sayaface='happy'
            show Sayaka

            "Sie nickt, und das wieder mit vollem Mund.{w} Das soll wohl so was wie 'Ja, echt' bedeuten."

            p "Hm.{w} Eine Zauberschule.{w} Wo man ...{w}Magie erlernt?{w} Das hört sich nach Spaß an."

            $ sayaface='normal'
            $ sayapose='school_1'
            show Sayaka
            with dissolve

            "Sayakas Gesichtsausdruck wird wieder freudloser.{w} ... Hab ich {i}schon wieder{/i} was Falsches gesagt?!"

            s "Es ist etwas, was ich nur ungerne nochmal tun würde.{w} Sagen wir es einfach mal so."

            s "Magie lernt man nicht einfach an einem Tag.{w} Man muss jahrelang lernen, trainieren und--"

            $ sayaface='scared'
            show Sayaka

            "Sie schließt ihren Mund und schlägt ihre Hand drüber, als wolle sie versuchen, sich davon abzuhalten, noch mehr auszuplaudern.{w} Verdammt.{w} Sie hat's bemerkt."

            $ sayaface='smiling'
            show Sayaka

            s "Whoops!{w} Ich Dummerchen.{w} Das war knapp."

            "Eines Tages werde ich schon noch herausfinden, wer die beiden wirklich sind.{w} Irgendwann wird sie alles ausplaudern!"

            p "Okay, wenn ich schon nichts über eure Organisation erfahren darf, darf ich dann zumindest etwas mehr über dich erfahren?"

            s "Huh?{w} Ich?"

            p "Ich mein, aus irgendeinem Grund scheint ihr fast alles über mich zu wissen, aber ich weiß gar nichts über euch, außer, dass ihr keine normalen Menschen seid."

            $ sayaface='normal'
            $ sayapose='school_1'
            show Sayaka
            with dissolve

            s "Hmmm."

            "Mein Gott, sie muss wirklich darüber nachdenken.{w} Ist es wirklich so schwer für sie, sich irgendwas auszudenken, das nichts mit Magie zu tun hat, und worüber sie mit mir sprechen kann?"

            $ sayaface='smiling'
            show Sayaka

            s "Das ist wie ein Vollzeitjob, daher hab ich nicht so viel zeit für mich.{w} Ich bin mir nicht sicher, ob es viel gibt, was ich dir erzählen kann, ohne dass die Jungs zuhause böse werden."

            s "Aber, weißt du ..."

            "Mit einem kleinen Lächeln lässt sie ihren Blick über die Cafeteria schweifen."

            s "Der Auftrag, dich zu beschützen, war eine der entspanntesten Aufgaben, die wir bisher hatten."

            $ sayaface='happy'
            show Sayaka

            s "Uns wurde die Chance gegeben, hier in der Schule etwas zu lernen und ein normales Leben zu führen."

            "Na ja ...{w} Ich bin mir nicht sicher, ob man das wirklich als 'anmelden' bezeichnen kann."

            $ sayaface='smiling'
            show Sayaka

            s "In der Lage zu sein, sich zurückzulehnen und die Dinge leicht anzugehen ...{w} wie ein normales Mädchen.{w} Ich hätte nicht gedacht, dass ich jemals dazu in der Lage sein würde."

            s "Weißt du, ich werde das hier echt vermissen, wenn erstmal alles geregelt ist."

            $ sayaface='normal'
            show Sayaka

            "Sie verstummt.{w} Tief in ihren Gedanken verloren.{w} Ich hätte nie gedacht, dass sie der Typ wäre, der über so was so sehr nachdenken würde."

            "'Wie ein normales Mädchen' ...{w} Heißt das, dass sie ihren Lebensstil nicht mag?{w} Ich kann schon einsehen, dass es mit der Zeit anstrengend werden kann, immer gegen diese Monster zu kämpfen."

            "Aber sie hat diesen Lebensstil doch gewählt, oder?{w} Zumindest bin ich fest davon überzeugt."
            
            "Ich kann sie aber auch nicht fragen, schließlich wird sie mir heute erstmal keine Fragen mehr zu dem Thema beantworten."

            with Pause(2.5)

            "..."

            s "Hey, Kenta?"

            $ sayaface='smiling'
            $ sayapose='school_2'
            show Sayaka
            with dissolve

            p "Ja?"

            "Ihre glitzernden Augen und funkelnden Lippen bringen mein Herz zum Rasen.{w} Warum habe ich bloß das Gefühl, dass sie mich gleich etwas Wichtiges fragen wird?"

            s "Wirst du das noch ...{w} essen?"

            "Ihre Augen fallen auf das Sandwich in meiner Hand."

            p "Ah, nein, alles in Ordnung.{w} H-Hier."

            $ sayaface='happy'
            show Sayaka

            s "Danke!{w} Du bist der beste!"

            "Noch immer benommen von dem Anblick, schnappt sie das Sandwich aus meiner Hand - ohne Chance auf Gegenwehr."

            "...Warte, was ist gerade passiert?"

            "Ich starre auf meine leere Hand, in der bis vor kurzem noch mein Sandwich war.{w} War wohl ein Fehler, mich zu ihr zu setzen."

            "Ich bemerke, dass auch ihr Tablett völlig leer ist.{w} Nicht mal ein Krümel ist noch übrig.{w} Sie ist ein MONSTER!"

    scene bg black
    with fade
    stop music fadeout 4.0

    "Die Mittagspause neigt sich dem Ende zu und wir werden in die Klassen zurückgeschickt."

    "Der restliche Schultag verläuft ganz normal.{w} Keine verrückten Angriffe.{w} Keine Monster."

    "Aber ich kann das Gefühl, dass mich etwas beobachtet, noch immer nicht loswerden."


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

    "Ein Tag mehr, ein weiterer Spaziergang nach Hause.{w} Mit meinen zwei Beschützern an meiner Seite."

    "Im Vergleich zu gestern scheinen sie deutlich angespannter zu sein.{w} Aber das kann ich ihnen nicht übel nehmen."
    
    "Wir hatten Glück, dass sie uns nicht verfolgt hat - sonst würde ich jetzt womöglich nicht mehr leben."

    "Die Reise nach Hause verläuft still und die Gesichter der Mädchen spiegeln ihre Entschlossenheit wider."
    
    "Sie scheinen bereit zu sein, beim geringsten Anzeichen von Gefahr loszustürmen, von daher möchte ich ihre Konzentration nicht unterbrechen."

    "Die Sonne auf dem Weg vor uns geht allmählich unter.{w} Großartig.{w} Desto größer unsere Schatten werden, desto angespannter werde ich."

    "Ich halte an.{w} Irgendwas stimmt hier nicht ..."

    s "Kenta?{w} Was ist los?"



    "Nicht schon wieder.{w} Wieder diese verdammten Kopfschmerzen."

    "Warte.{w} Hatten diese Kopfschmerzen nicht immer etwas gemeinsam?{w} Normalerweise treten sie tagsüber nie auf, außer--"



    y "Ah, pünktlich auf die Uhr.{w} Ihr macht mir das wirklich leicht, weißt du?"

    "Natürlich.{w} Direkt in die Falle gelaufen!{w} Ich muss langsam echt mal einen neuen Weg nach Hause finden ..."

    $ sayaface='angry'
    $ hikaface='angry'
    show Sayaka
    show Hikari

    "Ein heißblütiges Lachen kommt aus der Finsternis hervor, woraufhin die beiden Mädchen in die Angriffsposition übergehen.{w} Das kann nur eine Person sein ..."

    hide Sayaka
    hide Hikari
    $ yuzuface='joking'
    $ yuzupose='magical_2'
    show Yuzuki at center
    with dissolve



    "Flügel, die aussehen wie ein Obsidian, entfalten sich inmitten des Nachthimmels, und die bernsteinäugige Gegnerin macht sich bemerkbar."

    "Wie war nochmal ihr Name ...?{w} Yuzuki?{w} Aber das ist ja wohl egal.{w} Wen kümmert in einem solchen Moment der Name."

    "Sie hat einen wahnsinnigen Blick in ihren Augen - die Lust zum Morden.{w} Sie ist auch sicher heute nicht zum Spielen hier.{w} Sie hat es nur auf eines abgesehen."

    "...Auf mich."

    $ hikapose='magical_1'
    $ sayapose='magical_1'
    $ hikaface='normal'
    hide Yuzuki
    show Sayaka at left
    show Hikari at right
    with flash
    stop music fadeout 6.0

    "Während die Mädchen ihre Kampfausrüstung anlegen, strömt für einen kurzen Moment Licht herein, welches die Dunkelheit vertreibt."

    s "Kenta, hau ab!"

    p "Schon gut.{w} Ich weiß, was ich zu tun hab, okay!?"

    "Da man es mir kein zweites Mal sagen muss, sprinte ich ein gutes Stück zurück, um nicht ins Kreuzfeuer zu geraten."

    "Aber ...{w} werden sie gewinnen?{w} Gestern Abend kam Yuzuki nicht mal ins Schwitzen und wurde trotzdem fertig mit den beiden.{w} Der Unterschied in Sachen Kräfteverhältnis ist einfach zu enorm."

    "Dazu kommt noch, dass meine zwei Beschützer irgendein Problem damit haben, als Team zu arbeiten.{w} Die letzte Nacht war eine totale Blamage!"

    "Ich befürchte, dass wir auch heute wieder den 'taktischen Rückzug' antreten müssen ...{w} Und ich bin mir nicht sicher, ob ich den Mut dazu habe."

    $ yuzuface='smiling'
    $ yuzupose='magical_1'
    show Yuzuki at left
    show Sayaka at center
    show Hikari at right
    with dissolve
    play music "bgm/evilgirlintro.ogg" fadein 1.0
    queue music "bgm/evilgirlloop.ogg"
    "Yuzuki landet mit einem beunruhigenden Grinsen anmutig vor Sayaka und Hikari."

    y "Ich muss sagen, ich bin überrascht, dass ihr überhaupt kämpfen wollt.{w} Ich dachte, ihr würdet wieder den Schwanz einziehen.{w} Aber ich schätze, so macht es mehr Spaß!"

    "Ihre dunklen Flügel verwandeln sich in Federn, die sich wiederum in eine tödliche Sense verwandeln."

    y "Nun, wer von euch möchte zuerst einen erbärmlichen Tod sterben?"

    s "Hikari, jetzt!"

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


    "Hikari nickt und stürzt sich auf Yuzuki, bevor diese den ersten Schritt machen kann."
    
    "Sayaka fliegt eine weitere Strecke nach hinten und hält bereits einen Pfeil in ihrem Bogen bereit."
    
    "Erlebe ich hier etwa ...{w} Teamplay?{w} Vielleicht wird das ja doch noch was."

    y "Es ist nutzlos!"

    "Yuzuki reagiert blitzartig und wirbelt mit ihrer Sense herum, die auf Hikaris Schwert prallt.{w} Eine Schockwelle breitet sich in der Straße aus und zerstört Scheiben und Straßenschilder."

    "Das erinnert mich teilweise an den letzten Kampf.{w} Yuzuki hat den Vorteil der rohen Gewalt, weshalb sie zweifellos zurückschlagen wird."
    
    "Aber Hikari scheint kein bisschen nervös zu sein.{w} Im Gegenteil, sie scheint sogar selbstsicher!"

    h "Hrghh!{w} Licht, komm hervor!"

    scene bg white
    with wake

    "Hikari hält zähneknirschend die Stellung und schwingt ihr Schwert hin und her.{w} Ein Leuchten, das sich so lange verstärkt, bis es zu einem blendenden Licht geworden ist."

    "Ich bin dazu gezwungen, meine Augen mit meinem Arm zu verdecken, um nicht geblendet zu werden.{w} Wenn das für mich auf diese Entfernung schon so schlimm ist, möchte ich nicht wissen, wie es für die beiden ist."

    scene town street night
    $ yuzupose='magical_2'
    $ yuzuface='shocked'
    show Yuzuki at left
    show Hikari at right
    with wake

    "Da das Licht allmählich verblasst, schaue ich im Augenwinkel wieder zurück auf den Kampf."

    "Es scheint, als hätte Yuzuki überhaupt nicht damit gerechnet, da sie sich mit der Hand vor dem Gesicht zurückzieht."

    y "U-Ugh.{w} Was glaubst du, womit du da spielst?!"

    scene cg15
    with flash

    s "Uuuuund, Hikari, duck dich!"

    "Sayaka lässt den Pfeil los, den sie seit Beginn des Kampfes gespannt hatte.{w} Und surrealer Geschwindigkeit fliegt er los in Richtung Yuzuki und hinterlässt dabei Funken."

    "Hikari duckt sich - auf Sayakas Aufforderung hin - um dem Pfeil auszuweichen."

    scene town street night
    $ yuzupose='magical_1'
    show Yuzuki at right
    with dissolve

    $ yuzuface='scared'
    with flash
    with hpunch
    show Yuzuki at left
    with MoveTransition(0.2)

    "Ein direkter Treffer!{w} Der Pfeil zerplatzt beim Einschlag und lässt Yuzuki nach hinten rutschen, während sie verzweifelt versucht, aufrecht stehenzubleiben."

    show Hikari at right
    with moveinright

    "Aber es ist noch nicht vorbei.{w} Während Yuzuki ihr Bestes gibt, um sich von dem Treffer zu erholen, springt Hikari auf sie zu und landet einen Folgetreffer."

    scene cg16
    with dissolve

    "Hikari springt hoch und führt einen vernichtenden Schlag gegen Yuzukis Kopf aus.{w} Das sollte es gewesen sein.{w} Ich kann mir nicht vorstellen, dass sie jetzt noch entkommen kann!"

    h "Es ist vorbei!"

    with hpunch
    with hpunch

    "Als Hikari landet, beginnt der Boden unter mir zu beben.{w} Gut die Hälfte der Straße spaltet sich unter ihrer Klinge entzwei."

    "Das war wahrhaftig ein vernichtender Treffer.{w} Einen solchen Schlag hätte niemand auf der Welt überleben können.{w} Aber ..."

    scene town street night
    $ hikaface='shocked'
    show Hikari at center
    with dissolve

    h "W-Was ...?"

    "Hikari ist genauso verwirrt wie ich.{w} Das Mädchen ist nirgends zu sehen.{w} Dort, wo sie stand, treibt nur noch eine einzelne Feder umher.{w} Sie ist einfach ...{w} verschwunden."

    "Ein fieses Kichern ertönt aus den Schatten.{w} Hat sich Yuzuki etwa ...{w} teleportiert?{w} Oder ist sie so schnell ausgewichen, dass es niemand mitbekommen hat?"

    $ hikaface='scared'
    show Hikari

    "Hikari springt auf das Geräusch zu und wirft Sayaka dabei einen wilden Blick zu."

    $ hikaface='shocked'
    show Hikari

    h "Sayaka, hin--"

    hide Hikari
    $ sayaface='shocked'
    show Sayaka at center
    with dissolve

    s "Huh?"

    "Aus der Dunkelheit hinter ihr schimmert etwas hervor, das anschließend auf sie zukommt.{w} Sayaka kann dem tödlichen Schlag gerade noch ausweichen."

    "Zumindest ...{w} dachte ich das."


    scene cg4
    with flash

    s "Kyahhh!"

    "Plötzlich gibt Sayaka einen Schrei von sich.{w} Sie selbst sieht unverletzt aus, aber ihre Kleidung ist zerfetzt."

    "Von oben regnen Überreste von dem, was vorhin noch ihre Kleidung war, herab."

    "Ich mein, das ist ja schrecklich ... Da ist ja kaum noch was übrig!{w} Ich kann von hier aus fast alles se...{w} Hm?{w} Jetzt hab ich vergessen, woran ich gerade gedacht hab.{w} Verdammt."

    "Ähem."

    "Kampf, übel.{w} Schaden, schrecklich.{w} Okay, jetzt bin ich wieder auf Kurs."

    "Das ist krank.{w} Hätte sie eine Sekunde langsamer reagiert, dann hätte es nicht nur ihre Kleidung zerfetzt."

    "Ich dachte, Yuzuki schien vorhin ziemlich mitgenommen aus, aber sie ist heute ja noch stärker.{w} Oder bilde ich mir das bloß ein?"

    "Die beiden haben aus den Fehlern gestern gelernt und haben sich eine Taktik einfallen lassen, um dem Ganzen ein Ende zu bereiten, aber sie schlägt einfach doppelt so hart zurück."

    "Sayaka und Hikari haben ihr Bestes gegeben, trotzdem behält dieses Monster die Oberhand.{w} Ich frage mich, ob sie noch ein Ass im Ärmel haben?"

    "Ich schätze, ich sollte meinen Schutzengeln mehr vertrauen, obwohl es gerade ziemlich düster aussieht.{w} Für solche Kämpfe wurden sie bestimmt ausgebildet, weshalb sie sicherlich noch {i}irgendeinen{/i} Plan haben."

    "...Hoffentlich ein Plan, bei dem wir nicht vom Boden abheben.{w} Ich möchte nicht noch einmal fliegen.{w} Bevor das passiert, hofft ein Teil in mir sogar, dass Yuzuki gewinnt."

    "Sayaka versucht ihr verlegenes Gesicht zu verdecken.{w} Ich kann mir vorstellen, dass das während eines Kampfes sicher nicht praktisch ist.{w} Vor allem in einem Kampf gegen so was!"

    "Eigentlich sollte ich ja nicht hinsehen ...{w} aber ich kann meinen Blick von diesem wichtigen 'Kampf' nicht abwenden!{w} ... Oder so ähnlich."

    s "Ahh!{w} D-Das ist nicht gut!{w} Ich ...{w} Ich kann so nicht kämpfen!"

    s "Ohh, was mach ich jetzt?!"
    stop music fadeout 4.0
    "Hikari scheint wirklich sehr verärgert zu sein, als sie zu ihr eilt, und das, obwohl diese Situation eigentlich für ihre Partnerin beunruhigend sein sollte."

    h "Komm schon, hör auf herumzualbern!"

    "Sie stampft auf den Boden und schimpft ihre halbnackte Partnerin.{w} Ziemlich merkwürdig, jemanden so zu behandeln, der sich gerade in einem solchen Zustand befindet."

    h "Du weißt verdammt gut, dass du dein Outfit regenerieren kannst."

    "Hä ...?{w} Das kann sie?{w} Warum hat sie sich dann so verhalten?"

    s "Ahhh, das ist so b--...{w} Häh?{w} Oh.{w} Stimmt!"

    scene town street night
    $ sayaface='joking'
    $ hikaface='angry'
    show Sayaka at left
    show Hikari at right
    with flash
    play music "bgm/mischiefintro.ogg"
    queue music "bgm/mischiefloop.ogg"

    "Mit einem weiteren Leuchten sieht ihre Kleidung wieder so aus wie vorhin.{w} Hm.{w} Das ging ja wirklich schnell."

    s "He-hehehe-heheh ...{w} mein Fehler.{w} Das hab ich voll vergessen."

    "Hikari legt ihr Schwert über ihre Schulter und seufzt."

    h "Weißt du, ich denke, ein Teil von dir {i}wollte{/i} sich so zeigen.{w} Vielleicht jemand speziellem ..."

    s "Ich?{w} Niemals!{w} Sagt die, die 'aus Versehen' die Tür öffen gelassen hat--"



    with hpunch

    $ hikaface='embarrassed'
    $ hikapose='magical_2'
    $ sayaface='scared'
    show Sayaka
    show Hikari with dissolve

    "{i}Bum{/i}.{w} Hikari klopft ihr auf den Kopf.{w} Was ist hier ..."

    s "Ow!{w} Ich hab nur Spß gemacht!"

    "Mädels, vergesst ihr nicht gerade etwas ...?"

    stop music fadeout 3.0

    "Ich mein, ihr wart gerade mitten in einem Kampf."

    "Warte ...{w} Yuzuki hätte sie in der Zwischenzeit in Stücke zerreißen können.{w} Wo ist sie nach dem Angriff überhaupt hin?"

    $ sayaface='normal'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka
    show Hikari with dissolve

    "Als ob sie es auch gerade bemerkt hätte, machen sie wieder einen auf Ernst - wenn das überhaupt möglich ist - und nehmen wieder ihre Kampfhaltung ein."

    h "Hast du verstanden, wohin sie gegangen ist?"

    s "Uhh..."

    $ hikaface='angry'
    show Hikari

    h "Warum hab ich überhaupt gerfragt?"

    "Ich fange langsam an, mich unwohl zu fühlen ...{w} Ich werfe instinktiv einen Blick über meine Schulter ... nur um von einem wahnsinnigen Lächeln begrüßt zu werden."
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

    "Sie ist direkt hinter mir.{w} Wie hat sie das geschafft?!{w} ... Wobei, wenn ich bedenke, wie abgelenkt ich war, war es wahrscheinlich nicht allzu schwer."

    with hpunch

    "Ich stolpere nach hinten und kann ihrer ausgestreckten Hand, mit der sie nach mir griff, noch gerade so entkommen."

    s "Kenta!"

    $ yuzuface='scared'
    show Yuzuki

    y "Ah, verdammt{w} Ich bin so nah dran."

    "Das Mädchen zuckt zusammen.{w} Gemessen daran, dass sie es kaum noch schafft, ihre Sense in der Hand zu halten, dürfte sie wohl nicht mehr viele Kraftreserven haben."

    "Vielleicht war dieser Angriff vorhin effektiver, als ich dachte."

    "Das war wahrscheinlich ihr letzter Versuch, mich zu kriegen.{w} Bin ich froh, dass ich mich rechtzeitig umgedreht hab!"

    $ yuzuface='angry'
    show Yuzuki

    "Mit verengten Augen beobachtet sie mich, als sie ein paar Schritte nach hinten macht, während in der Zwischenzeit meine Beschützer zu mir aufschließen."

    "Sie verlagert ihre bernsteinfarbenen Augen voller Hass auf Sayaka und Hikari."

    y "Es sieht so aus, als wäre ich an der Reihe, mich für die Nacht zurückzuziehen.{w} Glaub nichts, du hast noch nichts gewonnen!"
    
    y "Du hast Glück mit diesem schlechten Schuss, aber erwarte nicht, dass es ein zweites Mal funktioniert.{w} Kenta {i}wird{/i} mir gehören!"

    $ yuzuface='joking'
    $ yuzupose='magical_2'
    show Yuzuki
    with dissolve

    y "Aber mach dir keine Sorgen, ich bin nicht grausam genug, um Wege zu trennen, ohne dir etwas zum Spielen zu überlassen.{w} Bis wir uns wieder treffen!"

    hide Yuzuki
    with dissolve

    "Mit einem Lächeln zieht sie sich langsam in die Schatten zurück.{w} Das, was sie da am Schluss gesagt hat, bereitet mir irgendwie Sorgen ...{w} 'Etwas zum Spielen'?"


    show Hikari at right
    show Sayaka at left
    with dissolve

    h "Zum Teufel gehst du irgendwo anders hin!{w} Wir werden den Kampf hier und jetzt beenden!"

    s "Ah, Hikari, vielleicht sollten wir--"

    $ sayaface='shocked'
    show Sayaka
    show Hikari at offscreenright with MoveTransition(0.3)

    "Hikari ignoriert den Ratschlag ihrer Partnerin und stürmt mit gezogenem Schwert vorwärts."

    "Es sieht alles danach aus, als würde sie einen Treffer landen, bevor sie die Flucht ergreifen kann ...{w} aber plötzlich schießt etwas wie aus dem Nichts hervor, woraufhin Hikari hoch in die Luft geschleudert wird."

    "Ein schleimiges Körperglied.{w} Ein ...{w} Ein Tentakel?"

    scene cg2
    with dissolve

    "Hikari lässt ihr Schwert fallen und ringt hilflos umher, während das Monster versucht, sie zu fesseln."

    h "Wahh!{w} H-hey, nein!{w} Lass mich gehen!"

    "Ich sehe ein Leuchten in ihren Händen.{w} Genau!{w} Sie hat ja noch immer ihre Magie.{w} Mit diesem Ding sollte sie kurzen Prozess machen können, mit Schwert oder nicht ist völlig egal."

    h "Jetzt zeig ich dir--huh?!"

    "... Oder vielleicht auch nicht.{w} Das Monster ist ihr einen Schritt voraus und versucht ihre Hände zu fesseln."
    
    "Die Tentakel schleichen sich immer näher an sie heran und träufeln eine ätzende Substanz auf sie, die bereits mehr als die Hälfte von ihr bedeckt."

    h "Urghh...{w} Das...{w}ist so eklich!{w} Ich denke nichtmal alle Duschen der Welt werden das Zeug in meinen Harren, rausbekommen!"

    "Sie beklagt ihre missliche Lage und versucht sich noch immer zu befreien, was letztendlich nur dazu führt, dass sich die Tentakel immer enger zusammenziehen."

    "Okay ...{w} Sie kann sich also nicht selbst befreien.{w} Aber ihre treue Partnerin sollte diese Tentakel doch mit einem gut platzierten Pfeil durchbohren können, oder?"

    "STIMMT'S?!"

    s "B-Böse Hunde!{w} Sitzt!{w} Runter!{w} Bleib!"

    "Was, wann sind die denn aufgetaucht?!{w} Sayaka ist von einem Rudel dämonischer Hunde umgeben."

    "Sie müssen gleichzeitig mit dem Tentakel-Monster aufgetaucht sein.{w} Ich frage mich, ob Yuzuki dafür verantwortlich ist?{w} Warte ...{w} Kann sie diese Dinger kontrollieren?"

    h "H-Hallo?{w} Wird mir irgendjemand helfen?!{w} Es ist nicht so lustig, wie es aussieht!"

    "Hikari schlägt sich wacker, aber ich sehe, dass die Tentakel ihren Tribut fordern."

    "Nicht gut.{w} Beide werden von Monstern aufgehalten."

    "Sayaka kann zwar gut mit dem Bogen umgehen, aber im Nahkampf wird sie wohl kaum so gut sein, dass sie damit fertig wird."

    "Und ...{w} Hikari braucht {i}eindeutig{/i} Hilfe, ansonsten wird sie von den Tentakeln noch vollkommen zerquetscht."

    scene town street night
    with dissolve

    "In Anbetracht dieser Situation ...{w} Wer kann ihnen da noch helfen?"

    "Ich?"

    "Aber ...{w} ich hab noch nie in meinem Leben gekämpft.{w} Ohne die beiden hätte ich doch schon längst ins Gras gebissen."

    "Ich balle meine Fäuste und werfe einen Blick auf die Mädchen.{w} Sie haben schon so viel riskiert, um mich zu beschützen, während ich immer nur zugesehen hab."

    "Sie brauchen meine Hilfe."

    "Aber was kann ich tun?{w} Ich kann nicht zaubern, so wie sie.{w} Ich hab auch keine übermenschlichen Kräfte.{w} Ich kann nicht fliegen.{w} Ich bin nutzlos.{w} NUTZLOS!"

    "Ich stampfe auf den Boden und verfluche mich für diese Nutzlosigkeit."

    "Häh ...?"

    "An meinem Fuß klappert etwas.{w} Hikaris Schwert.{w} Ein so großer Haufen an Stahl, der fast schon so groß ist wie Hikari selbst."

    "Ich hebe es auf.{w} Trotz der Größe ist es ziemlich leicht.{w} Ich kann es sogar mit einer Hand aufheben."

    "Das ist doch verrückt.{w} Ich kann nicht glauben, dass ich überhaupt auf diese Idee komme."

    "Ich richte mich auf, kräftige meinen Griff am Schwert und wirble in der Luft umher.{w} Es lässt sich ohne großen Widerstand führen."

    "Ein Kinderspiel, oder?{w} Luft ist eine Sache ...{w} aber dieses Schwert an einem lebenden Wesen zu benutzen ...{w} Selbst, wenn das Monster sind."

    "Ich bin nicht sicher, ob ich das durchziehen kann ..."

    s "Kyahh!{w} Berühr mich nicht!{w} Zurück, zurück!"

    h "E-Es zerdrückt mich!{w} H-Hilfe!"

    "Auf beiden Seiten höre ich Hilfeschreie.{w} Die Zeit läuft davon.{w} Ich habe mich entschieden!"

    "Aber ich kann sie nicht beide gleichzeitig retten.{w} Wer braucht meine Hilfe dringender?"

    menu:
        "Sayaka.":

            $ sayaka += 1

            "Genau.{w} Sayaka hat es mit wesentlich gefährlicheren Gegnern zu tun.{w} Diese Hunde werden sie noch in Stücke zerreißen, wenn ich ihr nicht helfe!"

            p "Sayaka, halt durch!"

            play music "bgm/battleintro.ogg" fadein 2.0
            queue music "bgm/battleloop.ogg"

            "Mit dem Schwert seitwärts hängend sprinte ich los.{w} ... Ich weiß ja nicht mal, wie ich das Teil halten soll.{w} Das muss echt lächerlich aussehen."

            $ sayaface='scared'
            show Sayaka at center
            with dissolve

            s "Shoo, shoo!"

            "Verzweifelt weicht sie irgendwie den Klauen und Reißzähnen aus, allerdings findet sie nicht die Zeit dazu, einen Pfeil abzufeuern."

            "Ich nähere mich den Tieren.{w} Ich darf keine Zeit verlieren!{w} Zeit zu zeigen, was ich draufhab.{w} Ich kann ein Held sein--"

            hide Sayaka
            with dissolve
            with hpunch


            p "Oof!"

            "In meiner Eile, Sayaka rechtzeitig zu erreichen, stolpere ich plötzlich heldenhaft über meine eigenen Füße."

            "Ich schwanke nach vor und mit ausgestrecktem Schwert falle ich direkt in eines der Monster."

            "Das Monster lässt einen ohrenbetäubenden Schrei los, als es von der Klinge erfasst wurde, und lenkt die Aufmerksamkeit der anderen Monster auf sich."

            "Na ja.{w} War zwar nicht so geplant, aber es hat funktioniert.{w} Irgendwie."

            scene cg20
            with dissolve

            "Einen kurzen Augenblick später sind auf einmal alle Augen auf mich gerichtet.{w} K-Kein Problem."

            "Zittrig halte ich das Schwert in die Höhe, als sie anfangen, mich zu umzingeln.{w} Das wollte ich doch, oder?{w} Ich ...{w} Ich mein, zumindest konnte ich Sayaka retten."

            "Plötzlich springen sie alle gleichzeitig los.{w} Ein Angriff von allen Seiten.{w} Oh Gott, das wird so was von hässlich enden.{w} Selbst ein Schwertkämpfer hätte da Probleme!"

            scene town street night
            with flash

            "Bevor sie mich jedoch erreichen, steckt in dem Kopf ein jedes Monsters ein Pfeil fest. Kurzerhand später lösen sie sich in einer Wolke aus schwarzem Rauch auf."

            $ sayaface='happy'
            $ sayapose='magical_2'
            show Sayaka at center
            with dissolve

            s "Phew.{w} Das wat knapp, huh?"

            "Sayaka senkt grinsend ihren Bogen {w} ... Ah, genau.{w} Durch meine Hilfe konnte Sayaka ihre Pfeile abfeuern.{w} ... Lief alles nach Plan!"

            p "Ach ne ...{w} Ich frag mich echt, wie ihr das tagtäglich durchhaltet!"

            $ sayaface='smiling'
            show Sayaka

            s "Es ist etwas, an das man sich gewöhnt!"

            s "Egal, Kenta du hast mich überrascht!{w} Ich dachte nicht dass {i}du{/i} dich selber beschützen kannst!"

            p "Ah, das war doch gar nichts ...{w} Warte, was soll denn das heißen?"

            $ sayapose='magical_1'
            show Sayaka
            with dissolve

            s "Nichts!{w} Ich danke dir."

            "Sie strahlt förmlich.{w} Ich bin sicher, dahinter steckte {i}etwas{/i} mehr ..."

            $ sayaface='shocked'
            show Sayaka

            "Als sie Hikaris Schwert erblickt, das ich gerade in meiner zittrigen Hand halte, öffnet sich ihr Mund ganz weit."

            s "Ist das...{w}Hikari's?{w} Wie auf Erden hast du..."

            $ sayaface='smiling'
            show Sayaka
            with hpunch

            h "Hallo?!{w} Wenn ihr Typen da hinten aufgehört habt zu reden, wäre gerade etwas Hilfe gut!"

            s "Okay, okay.{w} Komm runter.{w} Wir haben es verstanden!"

            "Sayaka seufzt und spannt einen magischen Pfeil in ihrem Bogen, bevor sie ihn kurz darauf mit einem gelangweilten Gesichtsausdruck loslässt."

            with flash

            "Der lahme und doch präzise Pfeil durchdringt alle Tentakel auf einmal.{w} Das Monster, welches sich noch immer in den Schatten versteckt, kreischt und lässt Hikari zu Boden fallen."

            h "Oof!"

            "Sie landet ... aber ziemlich ungemütlich.{w} ... Iiih.{w} Das ist sicher nicht angenehm."

            $ sayaface='happy'
            show Sayaka

            s "Guck, du bist doch okay!"

            $ hikaface='angry'
            show Sayaka at left
            show Hikari at right
            with dissolve

            "Hikari steht auf und holt tief Luft, um ihre Partnerin anzuschreien, aber als sie ihr Schwert in meinen Händen erblickt, wird sie still."

            $ hikaface='shocked'
            show Hikari

            h "Kenta...?"

            "Nervös und grinsend kratze ich mich am Hinterkopf."

            p "A-Ah ...{w} Ich hoffe, ihr habt nichts dagegen.{w} Es war ein Notfall."

            $ hikaface='normal'
            $ hikapose='magical_2'
            $ sayaface='smiling'
            show Sayaka
            show Hikari with dissolve

            h "Das ist nicht das Problem.{w} Ich bin überrascht dass du es benutzen kannst."

            p "Wenn es euch beruhigt, ich konnte nicht wirklich viel damit anfangen."

            $ sayapose='magical_2'
            $ sayaface='happy'
            show Sayaka
            with dissolve

            s "Psh, sei nicht so bescheiden!{w} Du bist mein Held, Kenta!"

            "Sayaka klatscht ihre Hände zusammen und blickt mich mit einem verträumten Gesichtsausdruck an."

            "Auch wenn sie eindeutig nur Spaß macht, kann ich mir das Lachen nicht verkneifen."

            s "Du hättest in sehen müssen, Hikari.{w} Er kamm reingestürmt und hat alle auf einmal erledigt!{w} Er war vielleicht sogar besser, mit dem Schwert, als du!"

            $ hikapose='magical_1'
            show Hikari
            with dissolve

            "Okay, jetzt sorgt sie endgültig dafür, dass es so aussieht, als hätte ich gar nichts gemacht."

            "Hikari schreitet zu mir und schnappt mir mit einem sauren Gesichtsausdruck das Schwert aus der Hand.{w} ... Urgh ...{w} jetzt hat sie mich mit diesem Schleim angesteckt."

            $ hikaface='angry'
            show Hikari

            h "Sei nicht lächerlich.{w} Ich bin mir nicht sicher, was genau da passiert ist, aber ich bin mir sicher, dass Glück eine {i}große{/i} Rolle gespielt hat."

            $ sayaface='smiling'
            $ sayapose='magical_1'
            show Sayaka
            with dissolve

            s "Nein, ich meine dass so!{w} Vielleicht sollte ich mich stattdessen einfach mit Kenta zusammen tun.{w} Wir wären das beste Team!"

            $ sayaface='happy'
            show Sayaka

            s "Was sagst du, Kenta?{w} Ich bin sicher, ich könnte dich dir auch ein schönes magisches Outfit besorgen!"

            "Während Sayaka weitermacht, kocht Hikari weiterhin vor Wurt.{w} Ich kann jetzt nicht mal mehr sagen, ob sie das Ernst meint oder nicht!"

            p "Ähh ...{w} Darauf kann ich verzichten."

            $ sayaface='smiling'
            show Sayaka

            s "Aww.{w} Okay.{w} Ich denke, du würdest darin gut aussehen!"

            "Ich frage mich ...{w} ob mein Outfit ...{w} auch so notdürftig ausfallen würde?"

            "...Da läuft es mir ja schon kalt den Rücken runter, wenn ich bloß daran denke.{w} Ich frag mich echt, wie die das schaffen."
        "Hikari.":


            $ hikari += 1

            "Ich denke, Hikari steckt in größerer Gefahr.{w} Diese Tentakel quetschen ihr noch den letzten Hauch ihres Lebens aus dem Körper!"

            "Sayaka steckte auch bestimmt früher schon mal in einer solchen Situation, von daher sollten diese Monster kein Problem für sie sein."

            p "Hikari, halt durch!"

            "Ich sprinte los und bewege mich auf die Tentakeln zu, die unbeirrt ihren Angriff auf Hikari fortführen."

            play music "bgm/battleintro.ogg"
            queue music "bgm/battleloop.ogg"

            scene cg2
            with dissolve

            h "Nngh!{w} D-Dummes Ding!{w} Hättest du mich nicht überrascht, könnte ich es..."

            "Sie tritt und zappelt weiterhin um sich, aber ich schätze, dass sie dadurch nur noch alles schlimmer macht."

            "Als ich das Monster erreiche, bremse ich mit dem Schwert in der Hand abrupt ab."

            "Es scheint, als wollten die Tentakel nichts mit mir zu tun haben.{w} ... Merkwürdig."

            "Okay.{w} Desto einfacher für mich.{w} Das ist so, als würde man Unkraut schneiden, nicht wahr?{w} ... Ein sich schlängelndes und schleimiges Unkraut ...{w} Aber trotzdem noch Unkraut!"

            "Konzentriert hole ich mit dem Schwert aus.{w} Ich kann nicht länger warten, ansonsten könnte es bereits zu spät sein."

            "Ein sauberer Schwung, dann ist alles vorbei."

            "Also ...{w} los."

            p "Hyahh!"

            scene town street night
            with flash


            "Das Schwert gleitet durch die Tentakel als wären sie Butter und teilt sie in zwei Hälften."

            $ hikaface='scared'
            $ hikapose='magical_1'
            show Hikari
            with dissolve

            h "Oof!"

            "Hikari landet mit einem spritzenden Geräusch und etwas benommen auf dem Boden."

            "Häh?{w} Ich hab's geschafft.{w} Ich war doch tatsächlich hilfreich!"

            "Der Körper des Monsters bewegt sich stöhnend in die Schatten.{w} Ich schätze, mit dem Großteil seiner Tentakel abgetrennt, kann es nicht mehr viel anstellen."

            h "Ughnn...{w} Kenta...?"

            p "Alles in Ordnung?{w} Hier, nimm meine Hand."

            "Mit einem erschöpften Lächeln strecke ich meine freie Hand zu ihr aus."

            $ hikaface='angry'
            show Hikari

            h "D-Du musst nicht..."

            $ hikapose='magical_2'
            show Hikari with dissolve
            $ hikapose='magical_1'
            show Hikari with dissolve

            "Sie nimmt sich jede Menge Zeit, um über alles nachzudenken und versucht sogar aufzustehen, nur um gleich wieder hinzufallen.{w} Ich schätze, sie ist es nicht gewohnt, Hilfe von anderen anzunehmen."

            $ hikaface='shy'
            show Hikari

            h "Okay, f-fine.{w} Was auch immer."

            with hpunch

            "Schlussendlich greift sie doch irgendwann nach meiner Hand und ich helfe ihr auf.{w} Ihre Hand ist voller Schleim.{w} Ich hoffe, dass Zeug lässt sich runterwaschen."

            $ hikaface='normal'
            show Hikari

            "Wieder auf den Beinen, nimmt sie sich kurz Zeit, um sich zu sammeln.{w} Trotz der Tatsache, dass sie von Kopf bis Fuß voller Schleim ist, versucht sie, einen Hauch von Würde zu bewahren."

            $ hikaface='shocked'
            show Hikari

            "Sie beobachtet die Umgebung und bewegt ihre Augen von den zappelnden Tentakeln bis hin zu ihrem Schwert, das ich noch immer in der Hand halte.{w} Schockiert öffnet sie ganz weit ihren Mund."

            h "War es...{w}Warst du es der mich gerettet hat, Kenta?"

            "Sie ist völlig verblüfft.{w} Ist es wirklich so unglaubwürdig, dass ich einmal nützlich war?{w} ... Okay, vielleicht hat sie recht."

            p "Ah, ja.{w} Ich hoffe, ihr habt nichts dagegen, dass ich es ausgeliehen hab."

            "Ich bin wegen der ganzen Sache etwas verlegen.{w} Ich war im Grunde genommen gerade ...{w}ein Held!{w} Echt komisch dieses Gefühl."

            $ hikaface='normal'
            $ hikapose='magical_2'
            show Hikari
            with dissolve

            "Ich halte ihr das Schwert entgegen.{w} Das Teil ist unglaublich.{w} Es hat sich federleicht angefühlt."

            "Sie schnappt mir das Schwert aus der Hand weg.{w} Sie ist echt fassungslos."

            h "Das ist gut.{w} Aber wie warst du in der Lage..."

            with hpunch

            s "Wahh!{w} Komm runter, Junge!{w} Komm zurück!"

            "Sayakas Hilfeschrei hat uns unterbrochen.{w} Uh, hoppla.{w} Hikari hat mich so dermaßen abgelenkt, dass ich Sayaka ganz vergessen hab."

            "Sie ist noch immer damit beschäftigt, den Angriffen der Monster auszuweichen."

            $ hikaface='angry'
            $ hikapose='magical_1'
            show Hikari
            with dissolve

            "Hikari seufzt und schwingt ihr Schwert."

            h "Ugh.{w} Das muss bis später warten."

            show Hikari at offscreenleft
            with MoveTransition(0.2)
            with flash

            "Sie springt blitzartig vorwärts und tötet all die Kreaturen auf einen Streich."

            $ sayaface='scared'
            $ sayapose='magical_1'
            show Sayaka at left
            show Hikari at right
            with dissolve

            h "Sheesh, Sayaka.{w} Was hast du gemacht, während du mit den Dingern gespielt hast?{w} Ich wäre umgebracht worden, wäre Kenta nicht da gewesen!"

            $ sayaface='normal'
            show Sayaka

            s "Huh?{w} Kenta?"

            "Endlich in der Lage, Luft zu holen, wirft mir Sayaka einen verwirrten Blick zu."

            $ hikaface='shy'
            show Hikari

            h "Kenta...{w} Er...{w}naja...{w}e-er hat mich gerettet."

            $ sayaface='shocked'
            show Sayaka

            s "Wirklich?!{w} Wie hat er das gemacht?!"

            "Sie kann es genauso wenig glauben wie Hikari."

            $ hikaface='normal'
            $ hikapose='magical_2'
            show Hikari
            with dissolve

            h "I-Ich weiß es nicht.{w} Er hat einfach mein Schwert aufgehoben und dann--"

            with hpunch

            s "Dein Schwert?!{w} Wie hat er--"

            $ hikaface='angry'
            show Hikari

            h "Ich weiß!{w} Deine Vermutung ist genauso gut wie meine.{w} Lasst uns dankbar sein, dass er es konnte, oder dieser Abend wäre unser letzter gewesen."

            "...Ich hab irgendwie das Gefühl, als würde irgendwas an mir vorbeigehen.{w} Was ist so besonders daran, dass ich das Schwert benutze?{w} Ich hab es doch nur aufgehoben und geschwungen.{w} Nichts Besonderes, oder?"

    stop music fadeout 4.0
    $ hikaface='normal'
    $ sayaface='normal'
    show Hikari
    show Sayaka

    "Hikari leuchtet plötzlich auf und nimmt mit dem Schwert in der Hand eine Pose ein."

    h "Oh!{w} Das Mädchen...{w} Hat sie...?"

    s "Yuzuki?{w} Ja, es sieht so aus, als wäre sie entkommen, während wir uns um ihre Freunde gekümmert haben."

    $ hikaface='angry'
    show Hikari
    play music "bgm/seriousintro.ogg" fadein 5.0
    queue music "bgm/seriousloop.ogg"
    h "Verdammt!{w} Wir waren zu nah!"

    "Frustriert stampft sie auf den Boden."

    $ sayaface='smiling'
    show Sayaka

    s "Vielleicht ist es das Beste?{w} Wir sind nicht in der Lage, noch weiter zu kämpfen"

    "Sayaka seufzt dramatisch und wirft die Arme nach oben.{w} Sie hat recht.{w} Ich möchte nicht wissen, wie es weitergegangen wäre, wäre sie noch hier."

    $ hikaface='normal'
    $ hikapose='magical_1'
    show Hikari
    with dissolve

    s "Wie ist es bei dir, Kenta?{w} Wie geht es dir?"

    p "Meinst du mich?"

    "Mal sehen ...{w} Ich schwitze wie ein Schwein und mein Herz klopft immer noch wie verrückt.{w} Ich könnte jederzeit kotzen.{w} Und mein Kopf fühlt sich an, als würde er sich jederzeit spalten."

    p "Ich, äh ...{w} Es geht so, um ehrlich zu sein."

    "Aber es geht mir trotzdem ziemlich gut.{w} Besser als gut, um ehrlich zu sein.{w} Ich bin froh, dass ich den beiden endlich mal behilflich sein konnte, auch wenn es nicht wirklich viel war."

    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Ich denke, wir können jetzt sicher sagen, dass es eine Nacht ist, oder?"

    "Hikari hält ihr Schwert weiterhin fest in der Hand und blickt in die Dunkelheit.{w} Sie scheint es nicht akzeptieren zu wollen, dass der Kampf bereits vorbei ist."

    $ sayaface='happy'
    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "Komm schon, Hikari!{w} Es ist vorbei.{w} WIr haben gewonnen!"

    "Sayaka schlägt mit der Hand auf Hikaris angespannte Schulter, woraufhin sie sich ein wenig entspannt.{w} Aber auch nur ein bisschen."

    h "Ich weigere mich zu glauben, dass sie so einfach aufgeben würde.{w} Es macht keinen Sinn."

    s "Hast du sie nicht gesehen?{w} Sie wurde wirklich verprügelt.{w} Ich denke, wir haben ihr mehr Schaden zugefügt, als sie es zugelassen hat.{w} Es würde mich überraschen, wenn sie morgen Nacht überhaupt auftaucht!"

    h "Vielleicht..."

    "Letztendlich gibt Hikari auf und lockert den Griff um ihr Schwert."

    "Widerwillig gesellt sie sich zu uns und gemeinsam starten wir unsere Heimreise."

    scene bg black
    with fade

    "Und somit kommt diese chaotische Nacht endlich zu einem Ende.{w} Wieder einen Tag überlebt!"

    "Nach dem heutigen Tag bin ich für die Existenz meiner beiden Schutzengel dankbarer denn je ...{w} So merkwürdig sie auch sein mögen."

    "Zuhause angekommen trennen sich unsere Wege ...{w} Wobei, ich weiß ja, dass sie nur einen Katzensprung entfernt sind, da sie sowieso wieder in meinem Garten campen werden."
    
    "Ich versteh echt nicht, wie sie es schaffen, nicht entdeckt zu werden."

    scene kitchen night
    with fade

    "Ich schließe die Tür hinter mir zu und werde vom vertrauten Duft der Hausmannskost empfangen."

    "Endlich in Sicherheit.{w} ... Hoff ich zumindest.{w} Zumindest haben mich hier noch keine Monster angegriffen.{w} Anscheinend haben sie es nur auf mich abgesehen, wenn sonst fast niemand bei mir ist."

    "Hoffentlich bleibt es auch so.{w} Es müssen nicht noch mehr Leute da mitreingezogen werden.{w} Ich weiß ja nicht mal, warum {i}ich{/i} da mitreingezogen wurde."

    "Ich setze mich zu meinen Eltern an den Esstisch.{w} Dieselben Blicke wie letztens - vielleicht sogar stärker, wenn man bedenkt, wie erschöpfend das Ganze für mich war."

    "Ich habe Glück, keine wirklichen Schäden davongetragen zu haben, oder zumindest keine sichtbaren."

    "Die üblichen Gespräche beginnen und einmal mehr bin ich an der Reihe, über meinen Tag zu sprechen.{w} Ich lasse aber lediglich ein unangenehmes Lachen los und sage, dass der Tag war wie jeder andere auch."

    "Ich frage mich, wie sie darauf reagieren würden, wenn ich ihnen erzähle, dass in unserem Garten zwei völlig fremde Personen zelten?"

    with Pause(2.0)
    stop music fadeout 5.0
    "Das friedliche, entspannende Abendessen geht zu Ende.{w} So wie gestern schleppe ich mich irgendwie ins Zimmer und lasse mich ins Bett fallen."

    scene bedroom night
    with fade

    "Zum Glück ist morgen Wochenende.{w} Endlich ausschlafen!{w} Aber irgendwie werd ich das Gefühl nicht los, als würde ich dank diesen beiden nicht wirklich dazu kommen."

    "...Wo wir schon dabei sind ...{w} Möchte ich überhaupt nachsehen?"

    "Zurückhaltend blicke ich durch den Vorhang.{w} Jup.{w} Zelt.{w} Lagerfeuer.{w} Und eine Mahlzeit, die schon fast in Flammen aufgeht, die die beiden löschen wollen.{w} ... Was hab ich mir anderes erwartet?"

    "Ich ziehe die Vorhänge zusammen und ignoriere die Tatsache, dass mein Garten jederzeit in Flammen aufgehen könnte.{w} Ich bin viel zu müde, um mir darüber Sorgen zu machen."
    
    "Wird schon schiefgehen.{w} Höchstwahrscheinlich."

    "Die verzweifelten Schreie von den beiden vermeintlichen 'Profis' sind das letzte, was ich höre, bevor ich in die Welt der Träume versinke."

    scene bg black
    with fade


    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"
    scene bedroom day
    with wake

    "Ich wache mit einem Stöhnen auf und warme Sonnenstrahlen reißen mich aus meinem Halbschlaf - was mir ganz und gar nicht gefällt."



    "Während ich versuche, mein Bett zu verlassen, schmerzt nicht nur mein Kopf, sondern auch jeder einzelne Muskel in meinem Körper."

    "Ich versteh's nicht.{w} Ich hab mich doch gar nicht {i}so sehr{/i} mehr angestrengt als beim letzten Mal.{w} Warum fühl ich mich also so schwach?"

    with hpunch

    "Es dauert eine Weile, bevor sich mein Körper meinem Willen endlich fügt."

    "Bevor ich wieder vollkommen zum Leben erwache, starre ich noch eine Sekunde auf die Decke.{w} Was ist bloß los mit mir?!"

    "Auf wackeligen Beinen stehe ich auf, ehe ich gegen die Wand krache."

    "Okay.{w} Tief Luft holen.{w} Anscheinend hab ich vergessen, wie man geht.{w} Kein großes Ding."

    "Zuerst sollte ich mich mal daran erinnern, bevor ich überhaupt daran {i}denke{/i}, die Stiegen nach unten zu gehen."

    "Immer einen Fuß vor den anderen.{w} Linker Fuß.{w} Rechter Fuß."

    "Langsam - aber sicher - kehren die Erinnerungen zurück.{w} Puh.{w} Vielleicht bin ich auch einfach nur müder, als mir bewusst ist?"

    with Pause(2.5)

    "Nachdem ich die Grundlagen der Mobilität wiedererlangt habe, gehe ich ins Badezimmer."

    "Als ich mich der Tür nähere, fällt mir plötzlich etwas ein - Déjà-vu.{w} Warum das?{w} Anscheinend vergesse ich da irgendwas besonders Wichtiges.{w} Etwas Lebensgefährliches."

    "Aber ...{w} so wie ich drauf bin, kann ich mich nie und nimmer daran erinnern.{w} Nach einer kalten Dusche sieht das aber sicher ganz anders aus!"

    scene cg5
    with wake

    "Dusche ...{w} Dusche ...{w} Dusche ...?"

    "Als ich die Tür öffne, werde ich von Dampf und dem Geräusch von fließendem Wasser begrüßt."

    "Sieht aus, als müsste ich noch etwas warten ...{w} Seit wann ...{w} ist sie überhaupt besetzt ...?"

    "Zumindest glaub ich, dass sie besetzt ist.{w} Mein Hirn braucht ein wenig, um den Anblick vor mir zu verarbeiten."

    s "Wahh!{w} Kenta?!{w} W-Was machst du?"

    "Ich blinzle ein paar Mal.{w} Jup.{w} Noch immer."

    "Sayaka steht wirklich vor mir.{w} ... Und noch dazu in meiner Dusche.{w} Hm."

    "Mit meiner Hand an der Türschnalle glotze ich noch ein wenig länger drein.{w} Ich muss nur die Tür schließen, und schon wird diese Situation nicht noch unangenehmer, als sie eh schon ist."

    "Abgesehen davon, dass sie ja anscheinend wieder in mein Haus eingebrochen sind ... Warum ist das {i}meine{/i} Schuld?{w} Ich dachte, nach dem gestrigen Tag hätten sie gelernt, wie einfache Schlösser funktionieren!"

    "Ich bin das Opfer, nicht der Täter!{w} Das ist nicht fair!"

    s "H-Hallo?{w} Ist jemand da?{w} D-Du kannst die Tür jetzt schließen!"

    "Während Sayaka versucht, sich so gut wie nur möglich zu bedecken, unterbricht sie meine Gedankengänge."

    "Sie ist viel verhaltener als sonst.{w} Aber vielleicht ist das auch nur auf diese unangenehme Situation rückzuführen."

    "Eine Situation, die ich mit meiner Anwesenheit nur noch unangenehmer mache."

    s "Wenn es dir nichts ausmacht..."

    p "Äh, genau.{w} Mein Fehler ..."

    "Zumindest ist Sayaka ein bisschen einsichtig.{w} Wäre das wieder Hikari gewesen, würde das Haus hier wohl kaum noch stehen."

    "Ich wende meinen Blick ab - irgendwie - und schließe die Tür."

    "Schlösser, Leute.{w} Schlösser!{w} Ihre Existenz hat einen Grund.{w} Meine Fresse."

    "...Ich bin mir nicht sicher, ob ich diesen Anblick jemals vergessen kann."

    "Ihr nasses Haar, das Wasser, das ihren Körper hinunterfloss, ihre--"

    "Argh!{w} Ich schüttle meinen Kopf.{w} Schlimmer Kenta!{w} Du bist besser als das!"

    scene bg black
    with fade

    "Nach all der Aufregung, von der ich hoffe, dass es nicht zum Alltag wird, finde ich mich unten mit den beiden Mädchen wieder."

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

    s "Aber genau deshalb sind wir hier!"

    "Sayaka strahlt mit einem Lächeln, das selbst der Sonne konkurriert."

    p "Was ...?"

    s "Kenta, du hast nicht so viele Freunde, oder?"

    $ sayaface='smiling'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    "Wie kommt sie jetzt darauf?{w} Und das ist auch bestimmt kein Scherz, wenn ich ihren ernsten Blick betrachte."

    p "S-Sei doch nicht dumm.{w} Ich hab genug Freunde!"

    $ hikaface='joking'
    show Hikari

    h "Oh?{w} Nenn mir einen."

    "Hikari auch noch?{w} Ich fühl mich gerade wie ein Verbrecher ..."

    p "Freunde?{w} Das ist einfach!{w} Da hätten wir ..."

    "Äh ...{w} Mal überlegen.{w} Wie wär's mit ...{w} Nein ...{w} Ich schätze, ich wünsch ihnen einfach einen guten Morgen und sonst nichts."

    "Aber echt jetzt--...{w} Abgesehen davon, dass sie meine Schutzengel sind, kann ich ja nicht mal die beiden mitzählen."

    "Oh Gott.{w} Bitter.{w} Mir fällt echt niemand ein.{w} Mein Gesichtsausdruck verrät alles."

    "Ich sollte lieber das Thema wechseln.{w} Und zwar schnell!"

    p "I-Ist doch egal!{w} Wie kommt ihr jetzt überhaupt da drauf?"

    $ hikaface='normal'
    $ sayapose='school_2'
    show Hikari
    show Sayaka with dissolve

    s "Es ist nur, dass wir gesehen haben, dass du dich nicht mit Leute an der Schule redest."

    p "Naja, das ... äh ... weil ich mich mit euch rumschlagen muss!"

    "Okay, ich greife nach Strohhalmen, aber sonst fällt mir einfach nichts ein.{w} Irgendwie hab ich das Gefühl, als wären sie nicht überzeugt.{w} Verdammt, ich bin ja nicht mal selbst überzeugt."

    s "Und in den letzten Wochen haben wir dich überwacht, du scheinst das Haus nur für die Schule zu verlassen, bevor du gleich wieder zurück kommst."

    p "Ich ..."

    $ sayaface='normal'
    show Sayaka

    s "Bist du einsam, Kenta?{w} Es ist schlecht für jemanden, sich so auszugrenzen."

    s "And to add to that, your parents always seem to be away working.{w} So it's just you, all on your own."

    "Hey, also darüber solltest du dir mal keine Sorgen machen ... Wär es anders, könntet ihr jetzt nicht mal hier sein!"

    "Aber ...{w} ich denke, sie hat recht.{w} Es ist traurig, aber es ist die Wahrheit."

    $ sayaface='happy'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Deshalb werden wir heute ein bisschen Spaß haben!{w} Wir drei!"

    "Sie klatscht ihre Hände zusammen und reißt mich aus meinen deprimierenden Gedanken."

    s "Ob du es glaubst oder nicht, Hikari und ich haben nicht wirklich viel Freizeit, also haben wir nie wirklich ein Wochenende, wie dieses, genießen können."

    $ hikaface='angry'
    show Hikari

    h "H-hey!{w} Wir sind immernoch im Dienst.{w} Vergiss das nicht!"

    $ hikaface='joking'
    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "Aber wenn Kenta sich entscheiden würde an einem sonnigen Tag auszugehen...{w}naja, wir hätten keine Chance und müssten mit ihm gehen."

    p "Okay, okay.{w} Ich schätze mal, ich hab hier kein Wörtchen mitzureden, oder?"

    $ hikaface='smiling'
    $ sayaface='smiling'
    show Hikari
    show Sayaka

    "Beide lächeln sie unschuldig.{w} ... Ich bin mir sicher, dass ich manipuliert werde."

    p "Also, was habt ihr für heute geplant?"

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Ah!{w} Das war ein Geheimnis.{w} Aber erstmal, ist da dass Problem mit dem Frühstück."

    "Stimmt.{w} Frühstück."

    if cookedpreviously == True:
        "Plötzlich erinnere ich mich an ein schreckliches Ereignis von gestern und ihr angebliches 'Frühstück'.{w} An die Küche will ich erst gar nicht denken.{w} Selbst eine Bombe hätte weniger Schaden angerichtet!"

        s "Ich denke, Hikari und ich sollten das Frühstück heute machen!{w} Wir haben es heute totall unter kontrolle."

        $ hikapose='school_1'
        $ hikaface='scared'
        show Hikari
        with dissolve

        h "W-Wir müssen?"

        s "Yep!"

        "Hikaris Gesicht wird blass.{w} Sie wirft mir einen Blick zu, der zeigt, dass sie möchte, dass ich dem Ganzen ein für alle Mal ein Ende setze."

        s "Wie wäre es, Kenta?"

        "Nach reiflicher Überlegung sage ich ..."

        menu:
            "Nein.":
                jump cookingprevious
            "Nope.":

                jump cookingprevious
            "Nö.":

                jump cookingprevious
            "Wie wär's mit ... nein?":

                jump cookingprevious
            "Hah. Ahahaha. Ahahahahahahahaha. Nein.":

                jump cookingprevious
            "Lieber nicht.":

                jump cookingprevious
            "Hmmmm ... Nein.":

                jump cookingprevious
            "Ich denk darüber nach. Okay, fertig. NEIN!":

                jump cookingprevious
            "Klar, in Ordnung.":


                "Klar, es spricht schließlich nichts dagegen!"

                "...Sag ich bestimmt nicht.{w} Sonst wär ich ja verrückt!"

                jump cookingprevious

        label cookingprevious:
            p "Äh, schon gut.{w} Ich kümmer mich ums Essen."

            $ sayaface='normal'
            $ hikaface='normal'
            show Sayaka
            show Hikari

            s "Aw..."

            "Sie sieht niedergeschlagen aus.{w} Aber ich musste es tun!{w} Für Hikari und meinetwegen!"

            p "I-Ich mein, ihr müsst nach dem gestrigen Tag doch echt müde sein.{w} Und mit dem Kochen könnte ich mich auch gleich bedanken!"

            $ sayaface='smiling'
            $ sayapose='school_1'
            show Sayaka
            with dissolve

            s "Wirklich?"

            p "Wirklich!"

            $ sayaface='happy'
            show Sayaka

            s "Also...{w}okay.{w} Dein Verlust!{w} Das Frühstück wäre heute viel besser gewesen."

            "Das bezweifle ich irgendwie.{w} Für dieses Mädchen und ihre Komplizin steht Zerstörung doch an der Tagesordnung."

            p "Bleibt einfach hier sitzen ...{w} und fasst bloß nichts Brennbares an, während ich weg bin, okay?"

            $ hikaface='smiling'
            hide Sayaka
            show Hikari at center
            with dissolve

            stop music fadeout 6.0

            "Sie halten sich beide an die Regeln und setzen sich.{w} Hikari scheint erleichtert zu sein und murmelt ein 'Dankeschön' vor sich hin.{w} Das Haus ist erstmal für einen weiteren Tag gerettet!"

            scene bg black
            with fade

            "Ich koche schnell etwas."

            "Mehrmals musste ich Sayaka von der Küche wegscheuchen, als sie versuchte, einen Fuß reinzusetzen.{w} Einmal hätte das sogar fast zu einem Herzinfarkt geführt, da sie mit dem Messer da stand, als ich mich umdrehte."

            "Ich weiß, dass sie doch nur helfen möchte ... aber trotzdem!"
    else:

        "Hmm.{w} Ich hab schon einmal ein Machtwort gesprochen, da wir es eilig hatten."

        "Aber ich bin sicher, dass das, was sie machen, nicht {i}so{/i} schlecht sein kann."

        "Außerdem scheint sich Sayaka wirklich zu freuen.{w} Diesem süßen Gesicht kann ich doch nichts ausschlagen."

        p "Okay, okay.{w} Ihr könnt das Frühstück machen.{w} Macht ...{w} nur bitte keinen Saustall, okay?"

        "Sayakas Augen leuchten auf und sie klatscht ihre Hände zusammen."

        s "Wirklich?{w} Yay!{w} Du wirst es nicht berreuen, ich verspreche es!"

        "Hoff ich doch ..."

        stop music fadeout 6.0

        "Es schadet sicher nicht.{w} Sie scheint es nur gut zu meinen und nach all dem Stress hab ich mir die Pause auch verdient."

        p "Klar.{w} Nur zu."

        $ sayapose='school_1'
        show Sayaka
        with dissolve

        "Sayaka strahlt, sodass ich mich von meiner Entscheidung überzeugt fühle.{w} H-Hoffentlich bleibt es auch dabei."

        s "Du wirst es nicht berreuen!{w} Lehn dich einfach zurück, und wir kochen etwas Wunderbares für dich!"

        show Sayaka at center with move
        with Pause(0.5)
        show Sayaka at offscreenright
        show Hikari at offscreenright
        with move

        "Mit diesen Worten dreht sie sich um und schlenzt in die Küche. Hikari wehrt sich, wird aber einfach mitgeschliffen."

        "Ich setze mich in das Esszimmer.{w} Das war doch die richtige Entscheidung.{w} Nicht wahr?"

        with Pause(2.5)

        "Es fängt zumindest gut an.{w} Ich höre Teller und Besteck klirren."

        play music "bgm/mischiefintro.ogg" fadein 3.0
        queue music "bgm/mischiefloop.ogg"

        h "Weißt du überhaupt, was du machst?"

        s "Wir kümmern uns darum später!{w} Jetzt pack noch dieses Zeug dazu!"

        "...Das ignorier ich jetzt einfach mal."

        "Das hektische Schneiden von Gemüse wird von Hikaris panischen Schrei unterbrochen."

        h "Pass auf, wo du das hinschwingst, du wirst mir noch den Kopf abschlagen!"

        s "Es ist okay."

        h "B-Bist du sicher, dass das geht?"

        s "Natürlich tut es dass!{w} Ich hab ein kreatives Auge für sowas."

        h "...Soll es Grün werden?"

        s "Uh."

        s "Mmhmm!"

        h "Also werden wir es einfach so machen, wie das?"

        "Plötzlich höre ich Flammen.{w} Wie stark drehen die da drinnen bitte auf?!"

        s "Hmm.{w} Was denkst du was dieses Zeug ist?"

        h "Ich habe keine Ahnung."

        s "Oh also, es geht rein!"

        "..."

        "Auf einmal wird es leise.{w} Ich weiß nicht, ob das ein gutes oder schlechtes Zeichen ist.{w} Ich hab ehrlich gesagt auch Angst davor, nachzusehen."

        h "I-Ist es wirklich okay?"

        s "Yup!{w} So soll es--"

        with hpunch

        s "Wahhh!"

        "Und dann plötzlich eine Explosion.{w} Dicke Rauchschwaden wehen in den Speisesaal.{w} Hmm."

        h "Mach es aus, schnell, es wird sich sonst ausbreiten!"

        s "Wie mach ich dass?!"

        h "I-Ich weiß nicht!{w} Versuch es einfach!"

        "Das Lodern der Flammen ist zu hören.{w} Das Flackern kann ich gerade noch so in meinem Augenwinkel wahrnehmen.{w} {i}Hmmmm{/i}."

        s "Nein!{w} Das hat es nur schlimmer gemacht!"

        h "Wie wäre es...{w}damit?!"

        s "V-Vielleicht!{w} Es hat vielleicht funktioniert!"

        s "...oder nicht.{w} Keine Magie mehr, okay?"

        h "Dieses Mal wird es funktionieren--"

        s "Keine Magie mehr!"

        h "Ich weiß sonst nicht was ich tuhen soll!"

        s "Hyah!"

        h "A-Ah, du verschüttest es überall!"

        "Ich höre Wasser spritzen.{w} Jede Menge.{w} Mehr als ein ganzer Kübel, um ehrlich zu sein."

        h "Ist es...{w}Ist es vorbei?"

        s "Hahhh...{w} ich denke!{w} Und guck, das Essen ist fertig!"

        h "Ich denke wirklich nicht das--"

        s "Ich sagte--das Essen ist fertig!"

        with Pause(2.5)
        play music "bgm/everydayintro.ogg" fadein 2.0
        queue music "bgm/everydayloop.ogg"


        $ sayaface='smiling'
        $ hikaface='scared'
        $ sayapose='school_2'
        show Sayaka at center

        with dissolve

        "Anscheinend fertig mit dem, äh, 'kochen', kommen die beiden aus der Küche.{w} Sayaka hält einen Teller in der Hand, von dem eigentlich nur Rauch aufsteigt."

        s "Ich hoffe du bist hungrig, Kenta!{w} Wir haben wirklich alles getan, um dir dieses ssen zu machen!"

        "Mit einem aufrichtigen Lächeln stellt sie den Teller vor mich hin."

        "I...Ich schätze, sie hat wirklich ihr Bestes gegeben.{w} Aber ...{w} das ist alles andere als 'Essen'."

        p "O-Oh.{w} Es ist ...{w} äh ..."

        "Auf dem Teller liegen nur noch Überreste von dem, was anscheinend mal 'Essen' war.{w} Man könnte meinen, es wäre schon giftig, dieses Zeug nur einzuatmen."

        "Ich sehe Hikari weiter hinten auflauern ... Offensichtlich beschämt über das, was die beiden da erschaffen haben."

        "Ich denke mal, das ist alles meine Schuld ... Hätte ich sie nicht in die Küche gelassen ...{w} Ach, ich sollte einfach die Verantwortung übernehmen und--"

        menu:
            "Iss es.":
                "Mir bleibt nichts anderes übrig, oder?{w} Ich möchte nicht, dass sie meinetwegen ein schlechtes Gewissen hat. Außerdem hat sie daran echt hart gearbeitet ...{w} was auch immer das ist."

                p "D-Dann probier ich mal ..."

                "Ich drücke mit meinem Finger dagegen.{w} Schon bei der kleinsten Berührung zerfällt es zu Pulver.{w} Okay."

                "Ich bin mir sicher, dass es, obwohl es noch so schrecklich {i}aussieht{/i}, nicht so schlecht sein kann.{w} Vielleicht versteckt sich unter diesem verbrannten Zeug ja doch irgendwo was Gutes."

                "Ich gebe so viel wie nur möglich auf den Löffel und stopfe ihn in meinen Mund - trotz meiner Instinkte, die sich alle dagegen wehren."

                "Es schmeckt ...{w} Es schmeckt ..."

                $ sayaface='happy'
                show Sayaka

                s "Also, es ist super oder?"

                "Sayaka lehnt sich erwartungsvoll nach vor."

                "So muss dann wohl Holzkohle schmecken."

                "Ich unterdrücke das Gefühl, mich übergeben zu müssen, und lächle sie an."

                p "M-Mmm!"

                $ sayapose='school_1'
                show Sayaka
                with dissolve

                s "Wirklich?{w} Yay, ich hab es gewusst!{w} Du solltest uns {i}jeden{/i} Morgen für dich kochen lassen!"

                "Oh Gott.{w} Was hab ich nur getan?{w} Und da steht noch ein ganzer Teller vor mir!{w} Es sind eindeutig diese Mädchen, die eine Gefahr für mein Leben und Wohlbefinden darstellen."
            "Iss es nicht. Ich möchte noch nicht sterben!":

                "Okay, ja, sicher nicht.{w} Zeit, ein Machtwort zu sprechen, anderenfalls wird es nur noch schlimmer."

                p "Schau, es tut mir leid, Sayaka, aber ich krieg das echt nicht runter."

                $ sayaface='normal'
                show Sayaka

                s "Huh?{w}Warum nicht?"

                "Sie neigt ihren Kopf stirnrunzelnd zur Seite.{w} Großartig, wegen dir fühl ich mich jetzt auch noch wie ein Monster!"

                p "Es ist ...{w} naja ...{w} wie soll ich es sagen, ohne ausfällig zu werden?"

                "Ich werfe einen weiteren Blick auf die giftige Substanz auf dem Teller, die mittlerweile anfängt, sich zu bewegen."

                p "Würde ich es essen, könnte ich heute nicht mehr zur Schule gehen.{w} Oder den Tag danach."

                s "Oh?"

                p "Sayaka, what I'm trying to say is, I would be dead.{w} This stuff looks toxic."

                $ sayaface='scared'
                show Sayaka

                s "Oh."

                "Ihr Stirnrunzeln wird immer tiefer.{w} Tut mir leid.{w} Es musste sein."

                $ sayaface='normal'
                show Sayaka

                s "Bist du dir sicher?{w} Es kann nicht {i}so{/i} schlecht sein."

                "Wirklich?{w} Echt jetzt?!{w} Wie kannst du ...{w} DAS HIER{w} auch noch verteidigen!? Das ist doch gar kein Essen mehr!"

                p "Okay, warum probierst du dann nicht zuerst?"

                $ sayaface='scared'
                $ sayapose='school_1'
                show Sayaka
                with dissolve

                "Sie zieht ein langes Gesicht.{w} Ich wusste es."

                s "U-uhh, ich hab schon gegessen."

                p "Schau, warum versuchst du--"

                $ sayaface='happy'
                show Sayaka

                s "Aber, Hikari noch nicht!{w} Sie kann dir zeigen, wie sicher und lecker es ist!"

                $ hikaface='shocked'
                $ hikapose='school_2'
                hide Sayaka
                show Hikari at center
                with dissolve

                h "E-eh?{w} Ich?!"

                "Noch immer auf der Lauer - in der Hoffnung, nicht mitreingezogen zu werden - springt Hikari auf, als sie ihren Namen hört."

                $ sayaface='smiling'
                show Sayaka at left
                show Hikari at right
                with dissolve

                s "Yeah!{w} Komm rüber, zeig Kenta wie lecker es ist!"

                h "Das kann nicht dein Ernst sein.{w} Das Zeug ist--"

                s "Totall sicher und essbar!{w} Jetzt komm rüber.{w} Bitte."

                $ sayapose='school_2'
                $ hikaface='scared'
                with hpunch
                show Sayaka
                show Hikari
                with dissolve

                "Sayaka stoßt dermaßen stark mit ihrem Finger gegen den Teller, dass dieser zu klappern beginnt.{w} Obwohl sie dabei lächelt, habe ich das Gefühl, als würde etwas Unheimliches dahinterstecken."

                h "...Fein."

                "Sie geht langsam auf das 'Essen' zu, wobei jeder Schritt länger dauert als der vorige.{w} Sie lässt es aussehen, als begäbe sie sich auf ein Himmelfahrtskommando."

                $ sayaface='happy'
                show Sayaka

                h "Wir haben es gemacht...{w}also kann es nicht so schlecht sein.{w} Es ist einfach nur ein wenig...{w}knusprig."

                "Zitternd streckt sie ihre Hand nach dem Essen aus.{w} Und dann ..."

                $ sayapose='school_1'
                $ hikapose='school_1'
                $ sayaface='shocked'
                $ hikaface='normal'
                show Sayaka
                show Hikari
                with flash

                "Plötzlich tritt ein magischer Blitz aus ihrer Hand hervor, der geradewegs auf das 'Essen' zufliegt und dieses vollständig zersetzt.{w} Mit dem Teller.{w} ... Und einen Großteil vom Tisch."

                $ hikaface='joking'
                show Hikari

                h "Oops!{w} Bin ich tollpatschig.{w} Meine Hand muss ausgerutscht...{w}sein.{w} Was eine Schande!{w} Und ich habe mich schon {i}so{/i} darauf gefreut, alles zu essen."

                "...Ich bin mir ziemlich sicher, dass Magie nicht einfach so 'ausrutscht'!{w} Und war nicht sie diejenige, die gesagt hat, man solle Magie nicht für solch belanglose Dinge verschwenden?"

                "...Vielleicht war es in ihren Augen ein Notfall."

                $ sayaface='scared'
                show Sayaka

                s "Hikari!"

                "Sayaka setzt ein weiteres herzzerreißendes Stirnrunzeln auf, aber es dauert nicht lange, bis ihr üblicher Optimismus zurückkehrt."

                $ sayapose='school_2'
                $ sayaface='happy'
                $ hikaface='scared'
                show Sayaka
                show Hikari
                with dissolve

                s "Oh also.{w} Wie wäre es, wenn ich mehr mache?"

                $ sayaface='shocked'
                show Sayaka
                with hpunch

                p "Nein!"

                "Ich springe von meinem Stuhl so heftig auf, dass ich diesen fast mitgenommen habe.{w} Alter, mein Haus wär fast in die Luft geflogen!"

                "Ich antworte ihr - vielleicht etwas lauter als sonst."

                s "H-huh?"

                p "Ich mein, wir würden zu spät zur Schule kommen, wenn ihr noch was kochen würdet."

                s "Oh...{w} Du hast recht.{w} Guck auf die Uhr!"

                "Puh.{w} Gerettet!"




    scene kitchen day
    $ hikaface='normal'
    $ sayaface='smiling'
    $ sayapose='school_1'
    $ hikapose='school_1'
    show Sayaka at left
    show Hikari at right
    with fade

    "So, nach dem Frühstück sieht es so aus, als wäre Sayaka endlich bereit, mir zu sagen, was sie für den Tag geplant hatte."

    "Ich erkannte schon, dass es ihr schwer fällt, es für sich zu behalten, wenn man bedenkt, dass sie so aussieht, als könne sie vor Aufregung jeden Moment platzen."

    "Gemessen an ihrer Beunruhigung, glaube ich jedoch auch, dass nicht einmal Hikari weiß, was Sayaka im Sinn hat."

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    play music "bgm/everydayintro.ogg" fadein 2.0
    queue music "bgm/everydayloop.ogg"

    s "Okay!{w} Es wird Zeit über unsere heutigen Pläne zu reden!"

    $ sayaface='happy'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Kenta!"

    "Plötzlich zeigt sie mit dem Finger auf mich, woraufhin ich aufspringe."

    p "Äh ...{w} J-Ja?"

    $ sayaface='smiling'
    show Sayaka

    s "Was denkt ihr über den Strand?"

    $ hikaface='scared'
    show Hikari

    p "Strand?{w} Ich weiß nicht so recht--"

    s "Super!{w} Also ist es entschieden."

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    "Aber ich hab doch gar nicht zugestimmt!"

    h "S-Sayaka!"

    "Hikari ist in der Hinsicht genauso verzweifelt wie ich.{w} Sayaka hat sich aber schon darauf vorbereitet.{w} Es ist entschieden.{w} Ob es uns gefällt oder nicht!"

    s "Komm schon!{w} Es ist das perfekte Wetter.{w} Es wäre verrückt {i}nicht{/i} zu gehen!"

    h "Aber an den Strand zu gehen meint..."

    "Hikari versinkt in beunruhigende Gedanken.{w} Ich bin sicher, sie hat ihre eigenen Gründe, weshalb sie so sehr dagegen ist ... Und ich hab meine."

    s "Es wird alles gut sein!{w} Hört auf euch Sorgen zu machen."

    "Ich weiß, dass sie gesagt hat, sie würde es für mich tun, da ich nicht oft raus komme.{w} Aber im Moment glaube ich, ist Sayaka die einzige Person, die davon profitieren würde."

    "Sie will offensichtlich nur all die Dinge machen, die sie bis jetzt nicht tun konnte, und benutzt mich dabei als Ausrede."

    $ sayaface='smiling'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    "Jetzt, wo sie schon so aufgeregt ist, kann ich wohl kaum noch Nein sagen.{w} Und selbst wenn ich Nein gesagt hätte, hätte sie mich einfach mitgeschliffen."

    p "Okay ...{w} okay.{w} Aber sollte ich in Flammen aufgehen, sobald ich dem Strand nahekomm, seid ihr schuld.{w} Meine Haut ist da sehr empfindlich!"

    $ hikaface='shocked'
    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "Kenta!{w} Du musst nicht alles tun, was sie sagt, es ist manchmal wirklich perfekt--"

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Ruhe jetzt, Hikari.{w} Es ist zwei gegen einen.{w} Bei dem Thema darfst du nichts mehr sagen!"

    $ hikaface='angry'
    show Hikari

    h "A-Aber--"

    $ sayaface='smiling'
    show Sayaka

    s "Du sahst aufgereht aus, als ich über ein Ausflug geredet habe!"

    h "Ich dachte nicht, dass wir ausgerechnet an den Strand gehen würden!"

    s "Ich weiß nicht wovor du dich so fürchtest, Hikari."

    $ hikaface='shy'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "D-Du weißt genau, um was ich mich sorge!"

    "Sayaka nimmt sich einen Moment Zeit um nachzudenken, bevor sie einen fetten Grinser aufsetzt."

    $ sayaface='joking'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Ohhh.{w} Ich verstehe.{w} Aber, ich bin mir sicher, warum du dir darüber Sorgen machst, du hast ein erstaunlichen b--"

    $ sayaface='scared'
    $ hikaface='embarrassed'
    show Sayaka
    show Hikari
    with hpunch

    h "Halt dein Mund!"

    "{i}Bam{/i}.{w} Hikari nimmt ihrer Partnerin mit einem heftigen Schlag in den Magen den Wind aus den Segeln.{w} Ich ...{w} versteh ja nicht mal, worüber sie da diskutieren.{w} Vielleicht ist es auch besser so."

    $ sayaface='smiling'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Hrkk.{w} O-Okay...{w} Du must nicht gewaltätig werden!"

    "Sayaka grinst weiterhin, trotz der Tatsache, dass sie starke Magenschmerzen hat.{w} Das hat echt schmerzhaft ausgesehen ..."

    $ hikaface='angry'
    $ hikapose='school_2'
    show Hikari
    with dissolve

    "Hikari dreht ihren Kopf zur Seite.{w} Sie ist wirklich dagegen, was?"

    h "Wenn Kenta wirklich gehen will, hab ich keine Wahl...{w} Aber das sollt nicht zu einer normalen Sache werden!"

    $ sayaface='happy'
    show Sayaka

    s "Y-yay!"

    "Sayaka jubelt heiser und ringt um ihren Atem."

    stop music fadeout 2.0

    scene bg black
    with fade

    "Da wir uns alle einig waren, zum Strand zu gehen - einige widerstrebender als andere - treffen wir alle nötigen Vorbereitungen.{w} Auf in die weite Welt."

    "Aus welchem Grund auch immer sprinteten die beiden Mädchen auf halbem Wege zum Strand vor und sagten, sie würden auf mich warten."

    "Ich dachte, sie würden immer an meiner Seite bleiben, und erst recht, wenn wir draußen sind ...{w} Aber der Strand scheint den beiden ja noch wichtiger zu sein als ich."

    "Und dann haben sie mich auch noch mit all dem Zeug zurückgelassen. Mit dem ganzen Mittagessen und was Sayaka da auch immer eingepackt hat.{w} Ich kann mit all den Taschen ja nicht mal mehr noch gerade gehen."

    "In Kombination mit der prallen Sonne, kann ich mich glücklich schätzen, wenn ich am Weg dorthin nicht ohnmächtig werd."
    play music "bgm/magicalgirlintro.ogg" fadein 2.0
    queue music "bgm/magicalgirlloop.ogg"
    scene beach
    with wake


    "Ich betrete zuerst den Sand.{w} Der Strand, endlich!"

    "Die Wellen des Meeres kreisen sanft am Ufer entlang.{w} Ein wundervoller Anblick.{w} ... Wär es nur nicht so heiß!"

    "Überraschenderweise ist hier ziemlich wenig los.{w} Hier und dort sind ein paar Leute, aber das war's dann auch schon.{w} Ich schätze mal, die Badesaison ist schon fast wieder zu Ende.{w} Ich hoffe, wir fallen nicht zu sehr auf ..."

    "Wo wir schon beim 'wir' sind ...{w} Wo sind die Mädchen überhaupt?{w} Ich schaue mich um.{w} Wo könnten sie nur sein ...?"

    "Ich wandere weiter den Strand entlang und verbrenne mir mit jedem Schritt die Füße."

    s "Yoo-hoo, Kenta, hier drüben!"

    "Eine mir bekannte Stimme erregt meine Aufmerksamkeit.{w} Endlich!"

    scene cg8
    with dissolve



    "Ich drehe mich zur Stimme, um dort ...{w}Oh, wow.{w} Okay, {i}das{/i} hab ich nicht erwartet."

    "Jetzt versteh ich, warum sie vorgegangen sind.{w} Um ihre recht ...{w}sagen wir mal auffälligen ...{w} Badeanzüge anzuziehen."

    "Sie teilen sich dieselbe Strandliege, und gemessen an ihrer Reaktion vermute ich mal, dass sie schon eine Weile auf mich warten."

    s "Guck, Hikari, er ist sprachlos!"

    "Sayaka kichert und umarmt Hikari ziemlich fest.{w} Anscheinend gefällt es letztendlich doch beiden."

    h "D-Du must mich nicht so anstarren...{w}e-es ist peinlich."

    "Sie versucht zu entkommen, aber sie kommt nicht weit, da Sayaka sie festhält.{w} Eine ziemlich ...{w}bloßstellende Position."

    s "Komm schon, Hikari, du musst nicht so bescheiden sein.{w} Du siehst gut aus und solltest ein bisschen stolz sein!"

    s "Weißt du, seit wir hier aufgetaucht sind, hast du Leuten die Köpfe verdreht."

    h "W-Was?{w} Lüg nicht!"

    s "Es  ist wahr.{w} Ich bin wirklich neidisch.{w} Es sieht so aus, als ob du mir die Show gestohlen hastt!"

    "Sayaka richtet ihre Aufmerksamkeit auf mich.{w} Ich hab ein echt schlechtes Gefühl dabei."

    s "So, was denkst du, Kenta?{w} Wer sieht besser aus?"

    "Ach, echt jetzt?{w} Das wollt ihr von mir wissen?{w} Jetzt muss ich aufpassen, was ich sage ..."

    menu:
        "Sayaka!":

            $ sayaka += 1

            p "I-Ich schätze, wenn ich mich wirklich entscheiden müsste, dann für ...{w} Sayaka."

            "Als Reaktion auf meine Antwort fängt ihr Gesicht zu leuchten an."

            s "Aww.{w} Wirklich?{w} Du bist so süß, Kenta."

            "Sie wirft mir ein Lächeln zu, das mein Herz zum Klopfen bringt.{w} Hikari hingegen ..."

            "Ihr seltener Glücksmoment von vorhin verschwindet unverzüglich.{w} Das war wohl zu erwarten.{w} Ich kann sie schließlich nicht beide für mich haben!"

            s "Auch wenn der Rest des Strandes unter Hikaris Zauber gefallen ist, bin ich froh, dass Kenta immer noch einen Sinn hat."

            "Vielleicht hab ich ihr Ego zu sehr gefüttert?{w} Sie leuchtet weiterhin und grinst Hikari ein paar Mal selbstgefällig an."

            "Hikaris Gesichtsausdruck wird immer düsterer, bis sie ..."

            stop music fadeout 4.0

            with hpunch
            scene beach
            $ hikaface='angry'
            $ hikapose='bikini_1'
            show Hikari at center
            with dissolve

            h "Okay, das reicht!"

            s "Wahh!"

            "Plötzlic stoßt sie Sayaka von der Strandliege hinunter."

            $ hikapose='bikini_2'
            show Hikari
            with dissolve

            h "Das ist so dumm!{w} M-Mich interessiert eh nicht, was Kenta denkt."

            "Sayaka klatscht kopfüber in den Sand.{w} Da sie einen kurzen Moment regungslos liegen bleibt, mache ich mir Sorgen, ob sie nicht vielleicht das Bewusstsein verloren hat.{w} Aber als ich meine Hand ausstrecke, grinst sie mich schon wieder an."

            hide Hikari
            with dissolve
            $ sayapose='bikini_1'
            $ sayaface='smiling'
            show Sayaka
            with moveinbottom

            s "Ahh, es geht mir gut, es geht mir gut!"

            "Sie spuckt jede Menge Sand aus.{w} ... Okay, wenn du meinst."
        "Hikari, wer sonst!":


            $ hikari += 1

            p "Na ja, ich schätze ...{w} Hikari."

            h "E-eh?!"

            "Ihr Gesicht wird noch roter, was eigentlich gar nicht mehr möglich sein sollte."

            h "D-Du kannst das nicht so meinen ..."

            s "Siehst du?{w} Ich hab es dir gesagt!{w} Selbst Kenta kann nicht anders, als dich anzuschauen."

            s "Du und dein perfekter Körper!"

            "Sayaka kichert und fängt an, Hikari zu kitzeln."

            h "Ahh--haha--s-stop, k-kitzel mich nicht d-da!"

            "Hikari versucht ihr Bestes, nicht lachen zu müssen.{w} ... Meine Anwesenheit haben sie anscheinend komplett vergessen."

            s "So ... neidisch!"

            h "O-okay, das reicht ...{w} Du kannst jetzt aufhören, S-Sayaka!"

            "Sayaka schenkt ihr überhaupt keine Aufmerksamkeit und macht weiter."

            stop music fadeout 4.0
            with hpunch
            scene beach
            $ hikapose='bikini_2'
            $ hikaface='angry'
            show Hikari
            with dissolve

            h "Ich hab gesagt es ist genug!"

            s "Huh--waah?!"

            "Auf einmal explodiert Hikari förmlich, woraufhin sie Sayaka von der Liege stößt.{w} Sayaka fällt völlig unvorbereitet in den Sand."

            $ hikapose='bikini_1'
            show Hikari
            with dissolve

            h "Ich schwöre, manchmal stimmt etwas nicht mit dir, Sayaka!"

            "Hikari seufzt vor Erleichterung, dass der Angriff ...{w} oder was auch immer das war, endlich zu Ende ist."

            $ sayaface='happy'
            $ sayapose='bikini_1'
            show Hikari at right
            with dissolve
            show Sayaka at left
            with moveinbottom

            "Sayaka springt hoch und streckt grinsend ihre Arme weit nach vor, als wolle sie sagen, \"Tada, ich lebe noch!\"."

            s "Yeesh.{w} Sei doch nicht so grimmig.{w} Du hättest mich einfach nett fragen können!"

            $ hikaface='normal'

            h "Hmph."

            "Hikari schmeißt sich wieder in die Liege.{w} Lasst uns, äh ...{w} endlich Spaß haben?"
        "Mir egal.":

            p "Ihr wisst hoffentlich, dass ich hier gerade gegrillt werde.{w} Und um zu verhindern, dass ich ganz verkohlt werd, würde ich mich liebend gerne irgendwo in den Schatten setzen."

            "Die Augen mit meinen Händen verdeckend, suche ich am Strand entlang eine Stelle, an der ich endlich all diese Sachen hinstellen kann."

            s "H-huh?{w} Kenta?{w} Du hast dazu nichts zu sagen?"

            "Häh?{w} Warum ist Sayaka denn so aufgeregt?"

            s "Gar nichts ...?"

            "Ich schüttle meinen Kopf und zucke mit den Schultern.{w} Hab ich da was verpasst?"

            scene beach
            $ hikaface='normal'
            $ sayaface='scared'
            $ hikapose='bikini_1'
            $ sayapose='bikini_1'
            show Sayaka at left
            show Hikari at right
            with dissolve

            stop music fadeout 2.0

            "Selbst Hikari scheint beleidigt zu sein und dreht ihren Kopf einfach zur Seite.{w} Aber bei ihr braucht es dazu nicht viel, von daher wundert es mich nicht wirklich."

            s "Kenta!{w} Du solltest besser hier rüberkommen.{w} Wir haben Jahre gebraucht, um diese ..."

            p "Nop.{w} Ich steh gerade echt auf der Leitung.{w} Worum geht's denn?"

            $ sayaface='angry'
            show Sayaka

            s "Es ...{w} es ist egal."

            "Sayaka setzt einen so beängstigenden Gesichtsausdruck auf, der dem von Hikari ähnelt.{w} Ehrlich, was hab ich bloß falsch gemacht?!"

            p "Ä-Äh ...{w} egal.{w} Ich such mir ...{w} erstmal ein schattiges Plätzchen."

            "Ich drehe mich um und wandere weiter den Strand entlang, während ich hinter mir noch immer ihre Blicke spüre.{w} Ich weiß nicht wirklich, was ich angestellt hab, aber ich werde es wahrscheinlich bald herausfinden."

    scene bg black
    with fade

    scene beach
    with fade

    play music "bgm/everydayintro.ogg" fadein 2.0
    queue music "bgm/everydayloop.ogg"

    "Abseits der Massen haben wir schlussendlich doch noch ein schattiges Plätzchen gefunden.{w} Die Stelle ist so abgelegen, dass man nur gelegentlich jemanden vorbeigehen sieht.{w} Perfekt!"

    $ sayaface='smiling'
    $ sayapose='bikini_1'
    show Sayaka at center
    with dissolve

    s "Ahh!"

    "Sayaka streckt ihre Arme nach oben und sonnt sich."

    s "Siehst du?{w} Ist es nicht das beste?{w} Und ihr wolltet gar nicht erst herkommn!"

    "Bin ich froh, dass sich zumindest eine amüsiert.{w} Aber es ist echt zu heiß.{w} Hikari scheint mit mir mitzufühlen, wenn man betrachtet, wie sie im Schatten rumliegt."

    $ sayapose='bikini_2'
    show Sayaka
    with dissolve

    s "Hmm, was machen wir als Erstes ...?"

    "Als sich Sayaka zu einer der Taschen aufmacht, die ich bis hierher schleppen musste, murmelt sie etwas vor sich hin."

    "Sie wühlt in der Tasche rum{w} ... Ich weiß nicht mal, was da drinnen ist.{w} Aber so wie es sich anhört, ist da {i}jede Menge{/i} drinnen.{w} Mehr, als wir heute überhaupt brauchen werden."

    $ sayaface='happy'
    show Sayaka

    s "So.{w} Perfekt!"

    s "Fang, Kenta!"

    $ sayaface='smiling'
    $ sayapose='bikini_1'
    show Sayaka
    with dissolve

    "Sieh holt etwas Buntes aus der Tasche und wirft es mir zu."

    p "Häh?"

    "Ich brauche einen Moment, um zu erkennen, was es ist.{w} Es ist ein NICHT aufgeblasener Strandball.{w} Glaube ich zumindest."

    s "Das kannst du doch, oder?"

    p "Na klar!"

    "Sage ich völlig zuversichtlich, aber in Wirklichkeit habe ich sogar eine Weile gebraucht, um rauszufinden, wo die Luft reinkommt.{w} Argh, das kommt mir vor, als würde ich ein Rätsel lösen.{w} Ein echt kompliziertes Rätsel!"

    with Pause(3.5)
    with fade

    "Während ich den Strandball aufblase, stöbert Sayaka wieder in der Tasche rum."

    p "O-Okay ...{w} Fast fertig."

    "Keuchend präsentiere ich ihr den Strandball ... Meine Lunge hingegen könnte jederzeit platzen."

    $ sayaface='happy'
    show Sayaka

    s "Oh, gut gemacht!{w} Wirf ihn wieder zurück!"

    "Ich werfe ihr den Ball zu.{w} Er segelt so irgendwie durch die Luft ... Gerade so weit, dass sie ihn fangen kann.{w} Das war jetzt peinlich."

    "Sayaka umklammert den Ball und denkt darüber nach, was man damit am Besten machen kann.{w} Zuerst schaut sie mich kurz an, ehe sie zur eingeschlafenen Hikari blickt."

    $ sayaface='joking'
    show Sayaka

    "Auf Sayakas Gesicht formt sich ein gefährlicher Ausdruck.{w} Sie möchte doch wohl nicht allen Ernstes--"

    $ sayaface='happy'
    $ sayapose='bikini_2'
    show Sayaka
    with dissolve

    s "Hikari, fang!"

    with hpunch

    "Sie schleudert den Ball zu ihrer Partnerin, von deren Schädel er weitaus stärker abprallt, als etwas Aufgeblasenes eigentlich abprallen würde."

    hide Sayaka
    $ hikaface='shocked'
    $ hikapose='bikini_1'
    show Hikari
    with dissolve

    "Hikari wacht mit einem schmerzhaften Geheule auf und fällt dabei fast von der Liege."

    h "H-Häh ...?{w} Wer ... Was?!"

    $ sayapose='bikini_1'
    show Hikari at right
    show Sayaka at left
    with dissolve

    s "Ich sagte, dass du ihn fangen sollst, Hikari!{w} Ich hab dir eine faire Chance gegeben und so."

    "Sayaka seufzt übertrieben ... Mit einem alarmierenden Schimmer in ihren Augen{w} ... War das die Rache für vorhin?{w} Ich sollte mir merken, mich nie mit Sayaka anzulegen."

    $ hikaface='normal'
    show Hikari

    h "Was?{w} Ich erinnere mich nicht ..."

    "Hikari blickt verwirrt drein.{w} Sie hat noch immer keinen Plan, was gerade passiert ist.{w} Vielleicht ist es auch besser so.{w} Wir sind schließlich hier, um Spaß zu haben, und nicht um zu kämpfen!"

    $ sayaface='smiling'
    show Sayaka

    s "Genug rumgehangen!{w} Kommt schon, lasst uns spielen!"

    hide Sayaka
    show Hikari at center
    with dissolve

    "Sayaka sammelt den Ball auf.{w} Sie deutet uns beiden, dass wir ihr folgen sollen."

    h "..."

    "Eine verwirrte Hikari torkelt von ihrer Liege und geht zu Sayaka.{w} Sie blinzelt mich ungleichmäßig an, als sie an mir vorbeikommt{w} ... Ist mit ihr auch alles in Ordnung?"

    hide Hikari
    with dissolve

    "Ich bin sicher ...{w} es geht ihr gut."

    s "Komm schon!{w} Kenta?{w} Auf was wartest du?"

    p "Bin schon am Weg!"

    "Wenn ich hier noch länger rumstehe, befürchte ich, dass Sayaka den Ball auch noch 'versehentlich' in meine Richtung wirft."

    "Ich stürze mich in den heißen Sand und achte darauf, nicht zu lange an einem Fleck stehenzubleiben.{w} Hab ich schon erwähnt, dass es sau heiß ist?{w} Heiß, heiß, heiß!"

    $ sayaface='happy'
    $ sayapose='bikini_1'
    show Sayaka at center
    with dissolve

    s "Kopf hoch, Kenta!"

    "Sie wirft den Ball in die Luft und schlägt ihn mit ihrer Faust auf mich zu.{w} Oh Gott, ist der schnell.{w} Viel zu schne--"

    with hpunch

    p "Oof!"

    "Jup.{w} Genau das hab ich erwartet."

    "Der Ball prallt von meinem Kopf ab und fliegt zurück zu Sayaka ... und ich sehe Sterne.{w} Ich ...{w} Ich hab ihn irgendwie zurückgeschlagen.{w} Darum geht's doch, oder?"

    $ sayaface='smiling'
    show Sayaka

    s "Okay, du bist dran, Hikari!"

    "Als wäre sie mit meinem Opfer noch nicht zufrieden genug, setzt sie gleich wieder an ... Dieses Mal mit Hikari im Visier."

    hide Sayaka
    show Hikari at center
    with dissolve

    h "H-Häh?"

    "Noch immer ein wenig benommen, schlägt sie den Ball unbeholfen weg.{w} Der Ball segelt an uns beiden vorbei und - PLATSCH - landet im Wasser."

    h "Oh.{w} Ups.{w} Ich werde ihn holen!"

    $ hikaface='shocked'
    $ hikapose='bikini_2'
    show Hikari
    with dissolve

    "Sie eilt hinüber, um den Ball zu holen, bleibt aber plötzlich stehen, während ihre Augen auf etwas im Meer fixiert sind.{w} Zuerst blinzelt sie nur ...{w} aber ihre Augen werden immer größer."

    h "Ähhh ...{w} Ich denke, ihr zwei solltet mal rüberkommen."

    $ sayaface='smiling'
    show Sayaka at left
    show Hikari at right
    with dissolve

    s "Hmm?{w} Was gibt's?"


    stop music fadeout 4.0

    "Auf einmal wird mein Schädel von einem stechenden Schmerz heimgesucht.{w} Ach komm ..."

    "Ich hoffe vergeblich, dass das normale Kopfschmerzen sind, vielleicht sogar noch Übrigbleibsel vom Ball ...{w} aber als ich Hikari ansehe, weiß ich, dass es weitaus schlimmer ist."

    h "Sagt mir, ich bin nicht die Einzige, die das sieht ..."

    $ sayaface='shocked'
    show Sayaka

    s "Was siehst du de...{w} Wahh!"

    "Ich stelle mich zu den beiden.{w} Was sehen die beiden denn?"

    "Ich starre auf das weite Meer hinaus.{w} Verstehe aber noch immer nicht, was der ganze Wirbel soll."

    p "Ich ...{w} Ich versteh's nicht.{w} Verarscht ihr mich gerade?"

    $ hikaface='angry'
    $ hikapose='bikini_1'
    show Hikari
    with dissolve
    play music "bgm/ominousintro.ogg" fadein 2.0
    queue music "bgm/ominousloop.ogg"
    h "Nein!{w} Schau, unten im Wasser!{w} Siehst du es nicht?"

    "Hä?{w} Im Wasser?"

    "Warte ...{w} War das Wasser schon immer so dunkel?"

    "Moment mal ... Das ist doch ..."

    p "Ist das ein Schatten?!{w} Der ...{w} ist ja riesig!"

    "Unter dem Wasser kommt etwas langsam auf uns zu.{w} Kann mir dieser Wahnsinn nicht mal einen Tag erspart bleiben?!"

    "Etwas, was man nur als gigantische Masse an Schlamm bezeichnen kann, türmt sich allmählich vor uns auf."

    "Eine groteske Kreatur, die plötzlich etwas öffnet, von dem  ich denke, dass es die Augen sind.{w} Mittlerweile verdeckt sie selbst die Sonne.{w} Die Kreatur ist mindestens so groß wie ein Gebäude, wenn nicht sogar noch größer!"

    p "Und dagegen wollt ihr kämpfen?{w} ... {i}Könnt{/i} ihr dagegen überhaupt kämpfen?"

    scene cg18
    with dissolve


    "Das Wesen rückt immer näher.{w} Ich kann mir keine einzige herkömmliche Waffe vorstellen, die dagegen etwas ausrichten kann."

    h "Das?{w} Hah.{w} Das ist ...{w} kein Problem!"

    "Sie klingt nicht wirklich zuversichtlich.{w} Aber in Anbetracht der Situation nehme ich ihr das nicht übel."

    "Hmm.{w} Es bewegt sich ziemlich langsam ...{w} Vielleicht können wir einfach abhauen?"

    "Aber wenn es erstmal über den Strand hinaus ist, geht der richtige Krawall erst los.{w} Ich schaudere, als ich mir vorstelle, was dieses Ding anstellen könnte."

    h "Wir schaffen das schon!{w} Wirklich!"

    "Ehrlich, das hört sich für mich nicht wirklich zuversichtlich an."

    "Und Sayaka hat noch nicht mal ihre Ausrüstung parat.{w} Hat sie vielleicht schon eingesehen, wie aussichtlos es ist?{w} Mit einem Finger am Kinn analysiert sie einfach nur die Situation."

    h "Diese Dinger mögen gegen physische Angriffe resistent sein, aber Magie sollte sie durchbrechen! {w} ... Zumindest in der Theorie."

    "Ihre Hand gibt ein schwaches Leuchten von sich."

    h "Ja.{w} Das sollte funktionieren.{w} Schau gut zu ... Ich werde es mit einer einzigen Explosion beenden!"

    "Das Licht in ihrer Hand wird stärker und wächst zu einer pulsierenden Kugel heran.{w} Ich frage mich, wie diese Magie funktioniert?{w} Es sieht immer so surreal aus, wenn ich so zuschaue."

    with hpunch

    "Auf einmal klopft mir etwas auf die Schulter."

    p "Häh?{w} Sayaka--"

    s "Shh."

    "Sie hält mir ihren Finger vor den Mund und greift nach meiner Hand, um mich von Hikari wegzuziehen."

    stop music fadeout 7.0
    scene beach
    $ sayaface='smiling'
    $ sayapose='bikini_1'
    show Sayaka
    with dissolve

    "Schließlich verstecken wir uns hinter einem großen Felsen, von dem aus wir die Situation beobachten.{w} Verständlicherweise bin ich gerade ein wenig verwirrt."

    p "Was ist los?{w} Solltest du ihr nicht helfen?"

    "Sayaka kichert und starrt auf die Szene vor uns.{w} Sieht aus, als stehe Hikari kurz vor dem Angriff."

    s "Ich denke, sie hat es nicht bemerkt."

    p "Was bemerkt?"

    $ sayapose='bikini_2'
    show Sayaka
    with dissolve

    s "Na, denk mal darüber nach.{w} Das Ding ist groß.{w} Und sie ist dabei, den Kern mit einer Explosion reiner Magie zu treffen.{w} Was denkst du, was passieren wird?"

    "Wie zur Hölle soll ich so was denn wissen?"

    p "Häää ...?"

    "Sayaka seufzt und klatscht ihre Hände zusammen."
    play music "bgm/mischiefintro.ogg" fadein 2.0
    queue music "bgm/mischiefloop.ogg"
    s "Es wird BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM machen!{w} Explosion!{w} Diese Arten von Schatten sind sehr flüchtig, wenn man Magie an ihnen einsetzt."

    p "Das ist mir zu hoch.{w} Ist das nicht gut?{w} Ein Monster weniger, um das wir uns Sorgen machen müssen."

    $ sayaface='joking'
    show Sayaka

    s "Sieh einfach zu."

    "Ein schelmisches Grinsen macht sich auf ihrem Gesicht breit.{w} Sollte ich Hikari vielleicht doch davon abhalten ...?"

    hide Sayaka
    $ hikaface='angry'
    $ hikapose='magical_1'
    show Hikari at center
    with dissolve

    "Aber als ich aus unserem Versteck blicke, ist es bereits zu spät.{w} Hikari entfesselt all die Magie, die sie angesammelt hatte, und trifft die Abscheulichkeit mitten ins Zentrum."

    "...Es ist nichts passiert?{w} Die Lichtkugel wurde von der Kreatur geradewegs verschluckt."

    "Ich verstehe nicht, worüber sich Sayaka solche Sorgen gemacht hat.{w} Explosiv?{w} Hah, nicht mal irgendeine Reaktion--"

    scene bg white
    with flash

    "Plötzlich detoniert das Monster ohne Vorwarnung und die Explosion verdeckt kurzzeitig meine Sicht.{w} Kurz darauf höre ich Hikari aufschreien."

    "Als sich das Licht langsam auflöst, höre ich etwas in den Sand prasseln{w} ... Regen?{w} Nein, am Himmel ist nicht eine einzige Wolke zu sehen.{w} Ich befürchte, es ist weitaus schlimmer."

    "Ich fokussiere meinen Blick noch stärker auf das Ufer, achte aber darauf, unser Versteck nicht zu verlassen."

    scene cg7
    with wake

    "Es regnet ...{w} Schleim?{w} Ein Großteil der Kreatur bedeckt nun den Strand.{w} Hm.{w} Ich hätte mit mehr Gegenwehr gerechnet."

    "Und im Zentrum von all dem Chaos steht eine traumatisierte Hikari - voller Schlamm."

    "Der Schleim um sie herum knistert.{w} Glücklicherweise scheint der Schleim nicht wirklich gefährlich zu sein, aber ihr Outfit hat er dennoch weggeätzt{w} ... Kein schöner Anblick."

    h "..."

    "Sie sagt kein Wort.{w} Sie bewegt sich nicht mal.{w} Sie ist vollständig unter der Substanz vergraben und blinzelt ab und zu gerade mal."

    "Der Regen hört endlich auf, sodass man aus dem Versteck kommen kann.{w} Aber ich muss aufpassen, dass ich nicht in den Schleim trete.{w} Eurgh.{w} Ich kann mir gar nicht vorstellen, wie sich Hikari gerade fühlt."

    p "H-Hikari, bist du ...?"

    h "...Kein einziges Wort."

    p "Aber--"

    h "Ich sagte, 'kein{w} {i}einziges{/i}{w} Wort'."

    "Ihre Schultern zittern.{w} Uh.{w} Die Welt mag zwar diese riesige Kreatur überlebt haben, aber dafür haben wir jetzt jemand anderen, der kurz vor einem Wutanfall steht."



    s "Meine Güte, das ist ein ziemliches Durcheinander."

    "Sayaka pfeift, als sie sich mit einem Grinsen heimlich vom Felsen entfernt."

    h "S-Sayaka, nicht einmal ..."

    s "Ich frage mich, was sie von all dem zu Hause denken würden, hmm?"

    h "Ich habe nicht nachgedacht!{w} Den Strandball, den du nach mir geworfen hast ..."

    "Sayaka bewegt sich auf ihre Partnerin zu und weicht dabei geschickt dem Schleim aus."

    s "Entschuldigungen, Entschuldigungen!{w} Ich hätte nicht gedacht, dass einer der besten Schüler so einen Fehler machen würde."

    h "Es ist nicht meine Schuld!"

    "Warte ...{w} Irgendwas ergibt da gerade überhaupt keinen Sinn."

    p "Sayaka."

    s "Hmm?"

    p "Wenn du wusstest, dass das passiert, warum hast du sie dann nicht aufgehalten?"

    s "Ah, gutes Argument.{w} Ich hätte ...{w} aber ..."

    s "Wo ist da der Spaß?"

    "...Plötzlich sieht ihr Lächeln noch hinterhältiger aus.{w} Dieses Mädchen ist das Böse in seiner reinsten Form!"

    h "Warum passiert so etwas immer mir?!"

    "Als Hikari versucht, sich von der Substanz zu befreien, gibt sie ein Stöhnen von sich.{w} ... Sei stark, Hikari!"

    stop music fadeout 6.0

    scene bg black
    with fade

    "Dank eines unerwünschten Gastes, der die Party gesprengt hat, findet unser Spaß am Strand ein recht rasches Ende."

    "Da wir den Schleim natürlich nicht einfach so liegen lassen konnten, waren wir auch noch einige Stunden damit beschäftigt, den Strand sauberzumachen."

    "Das war nicht lustig.{w} Überhaupt nicht.{w} Ich denke sogar, dass der Schleim all das noch wahrgenommen hat, wenn man bedenkt, wie schwer es war, ihn ins Meer zurückzubringen."

    "Mein Gott, ich kann nicht glauben, dass ich den halben Tag lang den Strand saubergemacht hab.{w} Sayaka kann ich aber auch nicht beschuldigen.{w} Als sie die Idee hatte, wusste sie schließlich nicht, was danach passiert."

    "Aber Hikari, die darauf beharrt hat, die ganze Zeit zuzusehen ... Ja, der kann man die Schuld in die Schuhe schieben!"
    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"
    scene town street night
    with fade

    "Während der Tag langsam zu Ende geht, marschieren wir durch die Straßen.{w} Die Sonne versinkt hinter dem Horizont und die Welt färbt sich in einen orangenen Schimmer."

    $ sayaface='normal'
    $ hikaface='normal'
    $ sayapose='school_1'
    $ hikapose='school_1'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "Niemand sagt etwas und beide sehen sie erschöpft aus.{w} Das ganze Getue am Strand hat uns ziemlich mitgenommen.{w} Seitdem Hikari mit dem Schleim bedeckt war, hat sie nahezu kein einziges Wort gesagt, wenn ich mich nicht täusche."

    "Trotz der Erschöpfung scheinen beide immer noch auf der Hut zu sein."

    "Genau.{w} Yuzuki hat uns am Heimweg bisher IMMER angegriffen.{w} Dieser geistesgestörte, dunkle Engel."

    "Gut möglich, dass sie uns angreift, solange wir noch erschöpft sind.{w} Das wäre ein einfacher Sieg für sie.{w} Ich weiß nicht mal, ob die Mädchen im Moment überhaupt die Kraft für einen Kampf haben."

    "Aber ...{w} niemand.{w} Uns greift niemand an."

    "Kein krankes Kichern aus dem Schatten.{w} Keine Monster, die aus der Dunkelheit heraus angreifen.{w} Gar nichts ..."

    "Es ist schwer zu glauben, dass sie sich nach all den Mühen der letzten Nächte eine solche Chance entgehen lässt."

    "Es sei denn, sie verfolgt das Ziel, dass wir mit der Zeit unachtsam werden, damit sie uns weiter vorne angreifen kann."

    "Argh!{w} Jetzt werd ich langsam paranoid."

    "Zumindest sind die Kopfschmerzen wieder weg.{w} Und normalerweise sind sie am stärksten, wenn Yuzuki vor uns auftaucht ... Aus welchem Grund auch immer."

    "Ich vertraue meinem Kopf.{w} Er scheint am zuverlässigsten zu sein, wenn es um diese Begegnungen jenseits aller Vorstellungen geht."

    scene bg black
    with fade

    "Wir schaffen es nach Hause, ohne einem einzigen dunklen Engel zu begegnen"

    "Ich verabschiede mich winkend von den beiden Mädchen, welche mir ebenso 'enthusiastisch' antworten.{w} Ich denke, wir alle möchten den heutigen Tag einfach nur vergessen.{w} Vor allem Hikari."

    "Aber ich habe irgendwie das Gefühl, dass sie diejenige sein wird, die sich am meisten daran erinnern wird."

    "Den Rest des Abends nehme ich nur noch verschwommen wahr.{w} Ich glaube aber, ich habe noch zu Abend gegessen und mir eine Serie angeschaut, ehe ich ins Bett gegangen bin."



    "Als ich in meine Träume gezogen werde, befürchte ich bereits, das dort etwas Schreckliches lauert.{w} Etwas, das ich nicht ignorieren sollte{w} ... Aber in dem Moment, wo ich aufwache, weiß ich überhaupt nichts mehr von diesem Traum."

    with Pause(3.5)
    scene bedroom day
    with wake

    "Der Morgen bricht an.{w} Erneut.{w} Mein Kopf tut extrem weh.{w} Erneut."

    "Ich gehe jeden Abend früher ins Bett, trotzdem bin ich jedes Mal, wenn ich aufwache, müder als am Tag zuvor."

    "Der einzige Unterschied besteht darin, dass die Morgensonne heute nirgends zu sehen ist.{w} Stattdessen höre ich das heftige Geräusch des Regens, der gegen das Fenster hämmert."

    "Der heutige Tag scheint echt mies zu werden.{w} Der graue Himmel über der Stadt wirft einen deprimierenden Schatten auf die Stadt und es scheint, als würde es noch sehr lange regnen.{w} Na toll!"

    "Und ich muss bei dem scheiß Wetter nach draußen.{w} Das wird kein lustiger Tag, das weiß ich jetzt schon."

    "Ich strecke mich und gähne, bevor ich mich zum Badezimmer begebe."

    "Warte."

    "In dem Moment, wo sich meine Hand bereits am Türknauf befindet, fällt mir etwas ein.{w} Das war echt knapp!"

    "Ich muss vorsichtig sein.{w} Es wurden schon zu viele Fehler gemacht.{w} Ich kann von Glück sprechen, dass ich bisher immer mit dem Leben davongekommen bin."

    "Okay.{w} Tiefe Atemzüge.{w} Ich kann das."

    "Ich klopfe mehrmals mit meiner Faust gegen die Tür."

    p "Hallo?{w} Ist da jemand?"

    "..."

    "Keine Antwort.{w} Aber ich wurde schon einmal hinter das Licht geführt.{w} Das beweist gar nichts."

    "Ich klopfe noch einmal ... Dieses Mal sogar noch lauter."

    "Keine Reaktion."

    "Wäre jemand auf der anderen Seite der Tür, hätte er das Klopfen bestimmt gehört.{w} Das heißt ...{w} ich kann eintreten?"

    "Ich öffne die Tür ein kleines Stück.{w} Und spähe dann durch die winzige Öffnung."

    "So weit, so gut."

    "Ich öffne die Tür immer ein bisschen weiter ...{w} bis ..."

    "...ich es sehe.{w} Ein wundersamer Anblick, der mir den Atem raubt."

    "Es ist so ...{w} Es ist so wunderschön.{w} Ich könnte vor Freude fast heulen."

    "...Das Bad ist wirklich einmal leer.{w} Keine verrückten Missverständnisse, keine peinlichen Blicke ...{w} Ich kann doch tatsächlich das Badezimmer benutzen, ohne mir um mein Leben Sorgen machen zu müssen."

    "Hastig verschließe ich hinter mir die Tür.{w} Ich überprüfe das Schloss sogar zweifach - nein, sogar dreifach. Etwas, dass die anderen auch hätten tun sollen!"

    scene bg black
    with fade

    "Nach einer friedlichen Dusche mache ich mich auf den Weg in die Küche, wo Hikari und Sayaka bereits auf mich warten."

    scene kitchen day
    $ hikaface='normal'
    $ sayaface='smiling'
    $ hikapose='school_2'
    $ sayapose='school_1'
    show Sayaka at left
    show Hikari at right
    with fade

    h "Ugh, es ist schrecklich dort draußen."

    "Hikari sieht mit einem Blick der Entrüstung aus dem Fenster.{w} Mit einer ziemlich langen Liste an Dingen, die sie sonst noch so ärgern, wundert es mich nicht, dass der Regen auch dazu zählt."

    h "Müssen wir heute wirklich in die Schule, Kenta?"

    s "Aww, komm schon.{w} Es ist nur ein bisschen Wasser.{w} Du wirst davon nicht schmelzen oder so."

    $ sayaface='joking'
    show Sayaka

    "Sayaka grinst gefährlich - mit einem Funkeln in ihren Augen.{w} Uh ..."

    s "Es ist weniger schädlich als das Zeug, das du gestern abbekommen hast."

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    "Sie versucht ihr Bestes, ein Kichern zu unterdrücken ... Vergeblich.{w} Hikari hingegen ist weniger amüsiert."

    $ hikaface='embarrassed'
    show Hikari

    h "S-Sayaka!{w} Können wir das jetzt endlich vergessen?{w} Ich war dumm, ich hab einen Fehler gemacht.{w} Große Sache!"

    "Aufgeregt geht Hikari einen Schritt auf ihre Parnterin zu.{w} Wir sind noch nicht mal in der Schule, und die diskutieren schon wieder!{w} Ich glaube, das ist ein neuer Rekord."

    h "Und außerdem weiß ich noch, dass {i}du{/i} es warst, die kurz davor war, wegen deiner Mätzchen von der Akademie ausgeschlossen zu werden."

    $ sayaface='joking'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Eh-heh-heh ...{w} Sie mögen einfach keine guten Witze!"

    $ hikaface='angry'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Scherz?!{w} Du hast fast alles in die Luft gespr--"

    "Plötzlich bemerkt Hikari, dass auch ich noch anwesend bin, woraufhin sie still wird.{w} Aww.{w} Ich schätze, ich werde nie etwas über ihre alte Schule erfahren.{w} Die, in der sie alles über ihre Magie gelernt haben."

    h "Belassen wir es doch jetzt einfach dabei und ich stimme dir zu, dass wir beide einmal dumm waren, okay?"

    $ sayaface='smiling'
    show Sayaka

    s "'Kay.{w} Ich denke wirklich nicht, dass es so schlecht war ..."

    $ hikaface='north'
    show Hikari

    s "Egal, Kenta, wie wäre es, wenn ich etwas koche--"

    $ sayaface='shocked'
    show Sayaka

    p "Nein!{w} Sicher nicht!"

    s "Aber du hast mich nichtmal--"

    p "Brauch ich nicht.{w} Wenn es darum geht, dass du in der Küche das Essen anrührst, egal in welcher Farbe, Form oder sonst was, gibt's nur eine richtige Antwort."

    $ sayaface='scared'
    show Sayaka

    s "Dieses Mal wird es wirklich--"

    p "Nop."

    s "Ich werde aufpassen--"

    p "Nööö."

    $ sayaface='angry'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Aww, du bist--"

    p "Nein!"

    "Ja, ich lasse weder sie {i}noch{/i} Hikari auch nur in die Nähe der Küche.{w}"
    
    "Selbst wenn sie es irgendwie schaffen, die Küche heil zurückzulassen, bin ich mir sicher, dass mir ihre Kochkünste mehr Schaden zufügen würden, als es diese Monster jemals könnten."

    "Sayaka seufzt, formt einen Schmollmund und blickt mich an, als wäre ich für sie eine riesengroße Enttäuschung.{w} Hey, ich bin hier nicht der Bösewicht!"

    $ sayaface='smiling'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    "Doch es dauert nicht lange, bis ihr gewohnt fröhlicher Ausdruck zurückkehrt.{w} Ich denke, es ist unmöglich, dieses Mädchen so richtig zu verärgern."

    scene bg black
    with fade

    "Nach dieser kleinen Aufregung am Morgen bereite ich schnell eine Mahlzeit für uns zu, ehe wir uns in die Schule aufmachen."

    scene town street day
    with fade

    "Der Regen zeigt keine Anzeichen, dass er nachlässt.{w} Kaum zu glauben, dass das Wochenende so schön war und jetzt nur dunkle Wolken zu sehen sind."

    "Wir haben lediglich unsolide Regenschirme, mit denen wir uns gegen diesen Regenschauer wehren können.{w} Ich bezweifle, dass wir trocken in der Schule ankommen."

    "Ich weiß echt nicht, wie das Wetter plötzlich so schirch werden konnte.{w} Wenn das so weitergeht, haben wir vielleicht sogar Überschwemmungen zu befürchten."

    "...Ich fühle mich aufgrund des Gedanken zwar ein bisschen albern, aber vielleicht ist dieses Wetter ja ein Vorbote. Ich weiß, es ist unsinnig, aber ich kann den Gedanken trotzdem nicht abschütteln."

    "Als ich in den Himmel blicke, sehen die Wolken sogar noch düsterer aus als zuvor ..."

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

    "Wir schaffen es zur Schule, ohne am Weg dorthin abzusaufen."

    s "Puh.{w} War ja ziemlich heftig da draußen!"

    "Als wir das Klassenzimmer betreten, schüttelt Sayaka erstmal ihr Haar aus.{w} Direkt neben Hikari."

    $ hikaface='angry'
    show Hikari

    h "Ugh, schau dich bloß an!{w} Du bist fast wie ein Hund!"

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Hmm?"

    "Sie hört auf und blinzelt unschuldig.{w} Ich weiß nicht, ob sie sich nur dumm stellt, oder ob sie es wirklich unabsichtlich getan hat.{w} Und genau das macht sie so erschreckend."

    $ hikaface='normal'
    show Hikari

    h "Vergiss es."

    hide Hikari
    hide Sayaka
    with dissolve

    "Hikari schnaubt und stampft zu ihrem Sitzplatz hinüber."

    "Ich folge ihr und setze mich seufzend auf meinen Platz.{w} Was für ein deprimierender Tag."

    "Als der Lehrer auftaucht und den Unterricht beginnt, sehe ich noch einmal aus dem Fenster ... Und sehe nur Regentropfen, die am Fenster hinunter rinnen."

    with Pause(2.5)

    "..."

    "Der Unterricht dauert an, aber mir fällt es jede Sekunde schwerer, mich auf das Thema zu konzentrieren."

    "Ich kann es spüren.{w} Am Hinterkopf meines Schädels.{w} Dieser vertraute, schleichende Schmerz."



    "Warum hier?{w} Ich hatte in der Schule noch nie diese Kopfschmerzen.{w} Und sie beginnen normalerweise nur dann, wenn etwas Schlimmes passieren wird ..."

    "Ich schätze mal, dass diese Kopfschmerzen eine andere Ursache haben, von daher sollte ich mir keine allzu großen Sorgen machen."

    "Oder ist es doch eine Warnung?{w} Dass etwas auf uns, oder besser gesagt mich, zukommt?{w} Ich weiß nicht, was ich davon halten soll."

    s "Kenta?{w} Bist du okay?"

    "Ich höre, wie mir Sayaka zuflüstert, während sie ihre Hand auf meiner Schulter hat.{w} Ich schaue zu meiner Seite und sehe dort Hikari, die mir einen ebenso besorgten Blick zuwirft."

    "Hab ich es mir so dermaßen anmerken lassen?{w} VIelleicht beeinträchtigen mich die Kopfschmerzen doch mehr, als ich vermute."

    "Ich nicke und lächle ein wenig.{w} Ich kann mich kaum selbst davon überzeugen, dass es mir gut geht, aber es reicht, damit sich zumindest die beiden wieder auf den Unterricht konzentrieren."

    scene bg black
    with fade

    "Die Pause bricht an und ich kann mich an kaum was erinnern.{w} Was war das überhaupt für ein Fach ...?{w} Ah, egal, das spielt jetzt auch keine Rolle mehr."

    "Zumindest habe ich jetzt die Zeit, die ich brauche, um meine Gedanken und die Situation wieder richtig zuzuordnen."

    scene classroom
    $ sayaface='smiling'
    $ sayapose='school_1'
    show Sayaka at center
    with fade

    s "Wir holen uns was zu essen, Kenta.{w} Willst du mitkommen, oder ...?"

    "Nachdem Sayaka von ihrem Platz aufgesprungen ist, stolziert sie grinsend zur Vorderseite meines Tisches."

    "Ich blinzle.{w} Ich brauche einen Moment, um überhaupt zu verarbeiten, dass ich gerade angesprochen wurde."

    p "Häh ...?{w} Oh.{w} Geht ihr ruhig vor.{w} Mir tut gerade mein Kopf ein bisschen weh ..."

    $ sayaface='normal'
    show Sayaka

    "Sayaka wirft mir einen mitfühlenden Blick zu, als ich die Kopfschmerzen erwähne."

    s "Kenta, wegen den Kopfschmerzen ..."

    s "Die sind ..."


    $ sayaface='shocked'
    $ hikaface='angry'
    show Hikari at right with moveinright
    show Sayaka at offscreenleft
    show Hikari at offscreenleft
    with move
    with hpunch

    s "Mmppff!"

    "Plötzlich taucht aus dem Nichts Hikari auf, die ihre Hand vor Sayakas Mund hält, ehe sie sie aus dem Klassenzimmer zieht."

    h "Komm schon, Sayaka.{w} Er muss nichts davon wissen, und wenn wir hier nur rumstehen, werden die Warteschlangen auch nicht kürzer!"

    s "Mmmff!"

    "Sayakas Schreie sind das letzte, was ich höre, bevor die beiden im Flur verschwinden.{w} Hm."

    "Warte ...{w} 'Kopfschmerzen'?{w} Heißt das, sie weiß, warum ich sie in letzter Zeit so oft habe?"

    "Was widerum heißt, dass sie auch die Ursache dahinter kennt?"

    "Wenn sie auch nur irgendwas darüber wissen, wird es Zeit, dass ich ihnen an den Zahn fühle."
    
    "Ich kann schließlich nicht zulassen, dass etwas so Wichtiges einfach unter den Teppich geschoben wird."

    "Ich stehe etwas unsicher auf den Beinen auf.{w} Sie sind in die Cafeteria gegangen, oder?"

    "Ich begebe mich ebenfalls dort hin, aber eine der Schülerinnen, der ich am Weg dorthin begegne, erregt meine Aufmerksamkeit."

    $ yuzuface='normal'
    $ yuzupose='school_1'
    show Yuzuki at center
    with dissolve

    "Eine Schülerin mit silbernem Haar und bernsteinfarbenen Augen."

    "Da klingelt es in meinem Kopf.{w} Woher kenne ich sie bloß?"

    "Warte ...{w} Ist das wirklich ...?"

    show cg11 with dissolve
    hide cg11 with dissolve

    "Es gibt keine Zweifel.{w} Sie ist der dunkle Engel, der mir das Leben zur Hölle macht.{w} Dennoch scheint sie im Moment eine völlig andere Person zu sein - eine ganz normale Schülerin."

    p "...Yuzuki?"

    "Als es mir einfällt, entwischt ihr Name meinem Mund."

    "Ging sie schon immer hier zur Schule ...?{w} Wie konnte ich das erst jetzt bemerken?!"

    "Unsere Augen blicken über die Menschenmassen.{w} Ich befürchte, dass etwas Schreckliches passieren wird ...{w} aber ihr Blick wandert genauso schnell weiter, wie er auf mich gerichtet wurde."

    hide Yuzuki
    with dissolve

    "Häh?{w} Vorher wollte sie mich unbedingt in die Finger kriegen, und jetzt?{w} Irgendwas stimmt hier ganz und gar nicht."

    "Ich weiß, dass es dumm und rücksichtlos ist, aber ich verfolge sie dennoch.{w} Wenn ich zuerst Sayaka und Hikari hole, könnte sie längst weg sein."

    with hpunch

    "Durch die Massen an Schülern ist es schwer, sie nicht aus den Augen zu verlieren, aber ich schaffe es irgendwie, sie dabei zu beobachten, wie sie auf die Treppen zugeht."

    p "Yuzuki, warte!"

    "Sie schenkt mir keine Aufmerksamkeit und steigt die Treppen hinauf."

    "...Warum verfolge ich sie?{w} Ich weiß nicht, was ich mir dadurch erhoffe.{w} Und dennoch bestehe ich förmlich darauf, diese Treppen ebenfalls hinaufzusteigen."

    "Sie scheint so anders zu sein.{w} Vielleicht ist es auch nur mein Wunsch, dass sie nicht dieses Monster ist, das mich bereits zweimal angegriffen hat."

    "Außer Atem erreiche ich das oberste Stockwerk.{w} Ich schaue in den Flur, um eventuell rauszufinden, wohin sie gegangen sein könnte, aber nichts."

    "Ich bin mir aber sicher, dass ich nicht so viel Rückstand hatte.{w} Wo ist sie also hin?!{w} Ich mein, die Treppe endet hier.{w} Es sei denn ..."

    "Ist sie wirklich da draußen?{w} Bei {i}DEM{/i} Wetter?!"

    "Ich steige die Treppen weiter nach oben, bis ich das Dach erreiche.{w} Der Regen hört sich ja noch ärger an als vorhin.{w} Ich kann mir nicht vorstellen, dass bei dem Wetter jemand freiwillig nach draußen geht."
    stop music fadeout 3.0
    "Ich kämpfe gegen die stürmischen Winde an und öffne die Tür."

    scene school roof
    with dissolve

    p "Y-Yuzuki ..."

    scene cg9
    with dissolve
    play music "bgm/sadintro.ogg" fadein 2.0
    queue music "bgm/sadloop.ogg"

    "Da steht sie, mit einer Hand am Geländer festhaltend.{w} Der Regen hat sie bereits völlig durchnässt."

    "Sie scheint davon aber völlig unbehelligt zu sein.{w} Ich bin zwar erst eine Sekunde hier draußen, habe aber schon das Bedürfnis, mich von hier zu verziehen."

    "Yuzuki ignoriert mich - ihre bernsteinfarbenen Augen voller Leere."

    "Zumindest scheint sie mir im Moment nicht feindlich gesinnt zu sein.{w} Aktuell mache ich mir sogar mehr Sorgen darum, dass ich den Regen heil überstehe."

    "Ich gehe einen Schritt auf sie zu."

    y "Was willst du?"

    "Sie antwortet freiheraus.{w} Vielleicht vertausche ich sie aber auch nur."

    "Ich denke gut über meine nächsten Worte nach.{w} Es könnte schließlich fatale Folgen haben, sage ich auch nur ein falsches Wort."

    "Aber ich darf auch nicht zu zurückhaltend sein.{w} Ich möchte schließlich Antworten auf meine Fragen!"

    "Nach einem kurzen Moment des Zögerns erhebe ich schlussendlich meine Stimme."

    p "Ich ...{w} Warum willst du mich unbedingt umbringen?{w} Ich versteh es einfach nicht!"

    p "Was ich damit mein, ist ..."

    p "Warum ausgerechnet ich?"

    "Auf meine Frage hin verkrampft sie ein wenig.{w} Ich fürchte, das war schon eine falsche Frage ..."

    y "Ich bin überrascht, dass du mich heute überhaupt bemerkt hast ..."

    y "Sag, Kenta ..."

    y "Wie lange sind wir schon in der gleichen Klasse?"

    p "Was ...?"

    "Ist sie ...{w}wirklich in derselben Klasse wie ich?{w} Ich bin sicher, wenn das der Fall wäre, hätte ich nicht so lange gebraucht, um es zu bemerken."

    "Yuzuki gibt ein bitteres Lächeln von sich."

    y "Du hast es nicht einmal bemerkt, oder?"

    p "Ich bin mir nicht ganz sicher ..."

    y "Ich kann genauso gut ein Geist sein."

    y "Weißt du, wie es sich anfühlt, vollkommen unsichtbar zu sein? Wenn niemand auch nur einen Blick in deine Richtung wirft?"

    "Kraftvoll umklammert sie den Zaun am Dach.{w} Was meint sie damit ...?"

    y "Nie als Partner für Projekte ausgewählt zu werden ...{w} Niemals gebeten werden, mit jemandem Mittag zu essen ...{w} Im Unterricht sogar vom Lehrer ignoriert zu werden."

    y "Das scheinen alles kleine Dinge zu sein.{w} Aber im Laufe der Jahre summieren sie sich.{w} Und langsam setzt der Hass ein."

    y "Menschen sind selbstsüchtig, unhöflich ... arrogant."

    y "Und du denkst wahrscheinlich nur, 'warum suchst du dir dann nicht einfach Freunde?'"

    "Ich ...{w} Ich denke, das wäre mein erster Gedanke gewesen."

    y "Glaubst du, ich hätte es nicht versucht?!{w} Ich habe mich so sehr bemüht, mich einzufinden.{w} Um gesellig zu sein, mit Leuten zu reden."
    
    y "Aber ab einem gewissen Punkt werden die sozialen Kreise zu unpassierbaren Mauern für diejenigen, die mitmachen wollen."

    y "Meine fröhlichen Grüße wurden völlig gleichgültig aufgenommen.{w} Meine Versuche, mit Klassenkameraden zu sprechen, wurden mit schmerzhaften Blicken erwidert."

    y "Und dann sitze ich wieder in einem dunklen, einsamen Zuhause, bevor ich mich dazu zwingen muss, wieder zur Schule zu kommen.{w} Zwar ein Ort voller Menschen, dennoch fühle ich mich hier am einsamsten."
    
    y "War es zu viel verlangt, nach einem Freund zu fragen?{w} Jemandem, mit dem ich reden konnte, dem ich mich anvertraue und mit dem ich Spaß haben kann ...{w} Genau wie im Fernsehen.{w} Ist das wirklich zu viel verlangt?!"

    scene school roof
    $ yuzuface='normal'
    $ yuzupose='school_1'
    show Yuzuki
    with dissolve

    "Sie ist also nur einsam ...?"

    p "Aber warum ..."



    "Plötzlich unterbricht sie mich.{w} Sie dreht sich um und starrt mir in die Augen.{w} Der leere Blick ist inzwischen verschwunden, an seiner Stelle ist aber nun ein Blick voller Hass zu finden."

    y "Aber hab kein Mitleid mit mir.{w} Nichts davon zählt mehr.{w} Nicht nach dem morgigen Tag.{w} Alles wird sich verändern."

    p "Morgen?"



    "Als ich sie frage, strömt eine glühende Hitze durch meinen Schädel."

    $ yuzuface='smiling'
    show Yuzuki

    "Yuzuki schmunzelt."

    y "Du kannst es fühlen, oder?{w} Sie ist so nah dran, frei zu sein.{w} Ihre Macht steigt mit jedem Tag."
    
    p "Was redest du da?{w} Wer wird frei sein?!"

    $ yuzuface='joking'
    $ yuzupose='school_2'
    show Yuzuki
    with dissolve

    y "Oh, also haben sie es dir nicht gesagt?{w} Interessant.{w} Ich frage mich, warum sie so sehr darauf bedacht sind, es geheim zu halten?"

    y "Egal, morgen wird alles einen Sinn ergeben.{w} Ich werde endlich bekommen, was ich möchte, und sie wird endlich bekommen, was sie möchte. "

    "Während ich damit kämpfe, aufrecht stehenzubleiben, spaziert Yuzuki einfach an mir vorbei."

    y "Auf Wiedersehen, vorerst.{w} Unser nächstes Treffen wird unser letztes sein."

    hide Yuzuki
    with dissolve
    stop music fadeout 6.0
    p "W-Warte, Yuzuki, was hast du--"

    "Es ist zu spät.{w} Sie ist weg."

    "Ich stehe allein auf dem Dach ... Mitten im strömenden Regen."

    "Eigentlich wollte ich ein paar Dingen auf den Grund gehen ...{w} aber jetzt bin ich noch verwirrter als vorher."

    with hpunch

    p "Ha-tschi!"

    "...Okay, ich sollte besser wieder reingehen."

    scene bg black
    with fade

    with Pause(2.5)

    scene classroom
    with fade
    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"
    "Platschnass gehe ich ins Klassenzimmer.{w} Yuzuki habe ich auf dem Weg hierher nicht mehr gesehen, aber auch hier scheint sie nicht zu sein ...{w} also keine Ahnung, wo sie hin ist."

    "Das hat sich ja echt gelohnt ...{w} Da fange ich mir eine Lungenentzündung ein, und wofür?{w} Um noch verwirrter zu sein, als ich es eh schon war."

    $ sayaface='shocked'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Wahh!{w} Kenta!{w} Was um Himmels Willen ist passiert?!"

    "Oh.{w} Ich schätze, Sayaka ist gekommen, um nach mir zu sehen, da ich nicht in der Cafeteria war.{w} Ich drehe mich um und lächle sie mit meinem überaus nassen Haar an."

    p "Ich, äh ..."

    "Wenn ich ihr sage, dass ich Yuzuki getroffen und sie mit allem konfrontiert habe, wird sie sich nur unnötig Sorgen machen, daher halte ich vorerst mal den Mund."

    p "Alles in Ordnung, mach dir keine Sorgen."

    s "Nichts?!{w} Kenta, du bist komplett nass!{w} Was hast du gemacht?"

    p "Ich war eigentlich schon draußen, um was zu holen, hab aber vor lauter Eile meinen Regenschirm vergessen.{w} Aber mir wird schon nichts passieren!"

    p "Ah ...{w} Hatschi!"

    "Okay, das hilft mir jetzt auch nicht wirklich weiter."

    $ sayaface='smiling'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Komm schon, lass uns dich abtrocknen.{w} Du wirst dich noch erkälten.{w} Hikari wird ausflippen wenn sie dich so sieht!"

    "Ah, genau ...{w} Ich kann mich glücklich schätzen, dass mich Sayaka zuerst gefunden hat."

    "Ich leiste keinen Widerstand, als Sayaka mich am Handgelenk packt und mich aus dem Klassenzimmer zieht.{w} Sie befragt mich auch nicht länger, wofür ich ihr sehr dankbar bin."

    scene bg black
    with fade

    "Der restliche Schultag vergeht, abgesehen davon, dass man in diesem Regen fast umkommen könnte, ohne besondere Vorkommnisse."

    "Und obwohl meine Kopfschmerzen weiterhin andauern, kann ich Yuzuki nirgends finden."

    "Ich versuche all das, was Yuzuki gesagt hat, zu einem Großen zusammenzusetzen."

    "Soweit ich es richtig verstehe, macht sie das alles nur, weil ...{w} sie Freunde möchte?"

    "Das ergibt keinen Sinn.{w} Wie konnte sie überhaupt so enden, wie sie jetzt ist?{w} Und wer ist diese ‚sie‘, die Yuzuki meint?"

    "Jemand, die irgendwas mit meinen Kopfschmerzen zu tun hat, und von der ich auch nur vermuten kann, dass sie hinter all den Monstern und all dem steckt, was mir in den letzten Tagen passiert ist."

    "Darüber hinaus hat Yuzuki auch angedeutet, dass Sayaka und Hikari mehr wissen, als sie sich anmerken lassen.{w} Das wusste ich bereits, wenn auch nicht in diesem Ausmaß."

    "Ich möchte sie zu all dem befragen.{w} Aber ich bin mir sicher, dass sie mir mit demselben Schweigen begegnen werden, mit dem sie mir auch bisher geantwortet haben."

    "Argh!{w} Warum machen sie alle so ein Geheimnis daraus?!{w} Es kommt mir so vor, als wäre ich die einzige Person, die hier nicht eingeweiht ist."

    "Während der feuchten Heimreise behalte ich meine Gedanken jedoch vorerst noch für mich."

    scene bedroom night
    with fade

    "Im Verlauf des Abends lässt der Regen dann allmählich nach.{w} Es wird endlich ruhig.{w} Aber wie lange?"

    "Yuzukis Worte schweben noch immer in meinen Gedanken rum.{w} Morgen wird irgendetwas passieren.{w} Etwas Schlimmes.{w} Und ich hab keinen Plan, was genau."

    "Ich schaue aus dem Fenster.{w} Dort sehe ich das gewohnte Zelt, wenn auch etwas nasser als sonst.{w} Es tut mir irgendwie leid, dass sie in einem solchen Wetter draußen campen müssen ..."

    "Diese beiden Mädchen ...{w} Sie wissen all das, was ich nicht verstehe."

    "Es ist nicht fair, dass ich, derjenige, um den sich alles dreht, am allerwenigsten von der ganzen Sache weiß."

    "Ich weiß nicht, ob sie all das machen, um mich zu beschützen oder so, aber ich fange langsam an zu glauben, dass es dafür bereits zu spät ist."

    "Ich blicke weiterhin auf das Zelt.{w} Es ist noch nicht so spät ...{w} Vielleicht sind sie also noch wach."

    "..."

    "Okay.{w} Ja.{w} Ich hab mich entschieden.{w} Ich gehe da jetzt runter und verlange nach einer Erklärung.{w} Ich muss Durchsetzungsvermögen zeigen."
    
    "Keine Geheimnisse mehr.{w} Und auch keine Spielchen mehr!"

    "Ich weigere mich, sie in Ruhe zu lassen, solange ich nicht weiß, was Sache ist.{w} Ich lasse ihnen einfach keine andere Wahl!"

    scene bg black
    with fade

    "Ich ziehe mir die Schuhe an und schleiche in den Garten.{w} Jup.{w} Es geschieht.{w} Ich werde endlich alles herausfinden!"

    "Ich nähere mich dem Zelt, dessen Eingang mit einem Reißverschluss verschlossen ist.{w} Aber das wird mich nicht aufhalten.{w} Ich weiß, wie man solche Dinger öffnet!"

    "Ich greife nach dem Reißverschluss.{w} Ohne zu zögern.{w} Ich gebe ihnen keine Zeit, mich aufzuhalten."

    "Und dann öffne ich mit einer schnellen Bewegung den Reißverschluss."

    p "Okay, von nun an keine Geheimnisse mehr!{w} Ich will Antworten hören, und zwar ...{w} äh ...?"

    scene cg10
    with wake
    play music "bgm/mischiefintro.ogg" fadein 2.0
    queue music "bgm/mischiefloop.ogg"

    s "Kyahh!{w} Kenta?"

    h "W-Was zur Hölle denkst du, was du da tust?!"

    "Och nö.{w} Ich hab hier vielleicht einen kleinen Fehler gemacht.{w} Die Fehler der Vergangenheit haben mich anscheinend nichts gelehrt."
    
    "Nicht in der Lage, irgendeine Antwort zu finden, lasse ich den Anblick über mich ergehen."

    "Beim Öffnen des Zeltes werde ich von den beiden bereits empfangen – halbnackt. In einem Raum, der von innen wesentlich größer aussieht, als er von außen zu sein scheint."

    "Ein schwindelerregender Duft schwebt aus dem Zelt hervor und benebelt meine Sinne noch zusätzlich."

    "Meine Augen wissen gar nicht, wo sie hinsehen sollen.{w} Sie sind beide so, äh ...{w} hübsch anzusehen."

    "Während beide offensichtlich in Verlegenheit geraten sind, scheint Sayaka auch noch überrascht zu sein.{w} Aber ...{w} Hikari scheint auch noch zu kochen – leider vor Wut."

    "Das ...{w} Das ist nicht fair.{w} Woher sollte ich das denn wissen?!{w} Das machen sie absichtlich, ich schwör‘s!"

    h "Kenta!"

    "Hikari versucht, in diesem ungewöhnlich geräumigen Zelt nach etwas zu greifen, womit sie sich bedecken kann."

    p "G-Genau, entschuldige, ich wollte doch einfach nur ..."

    "Richtig wäre es, den Reißverschluss wieder zu schließen und zu warten, bis sie fertig umgezogen sind … aber irgendwie kann ich meinen Blick nicht abwenden."

    "Verflucht seien meine natürlichen Instinkte!{w} Das ist so, als würde es bereits im Code stehen, wäre ich ein Computerprogramm!"

    h "'Einfach' was?!{w} Ein Perverser sein?!{w} Das kann ich nämlich eindeutig erkennen!"

    "Oh Gott, ich hoffe, das hat keiner meiner Nachbarn gehört."

    p "Das habt ihr komplett falsch verstanden. Ich wollte lediglich--"

    "Sie unterbricht mich.{w} Logisch.{w} In solch einer Situation habe ich natürlich nicht das Recht, mich rechtzufertigen.{w} Das ist die Logik dieser beiden Mädchen."

    h "K-Keine Entschuldigungen mehr!{w} Ich habe dich letztes Mal in Ruhe gelassen, aber diesmal ..."

    "Mit einer Decke, die den größten Teil ihres nackten Körpers bedeckt, marschiert Hikari mit einem furchterregenden Blick auf mich zu."

    s "Vielleicht sollten wir ihn verhören?{w} Ich bin mir sicher, er würde nicht ohne einen guten Grund hier hereinkommen!"

    h "Oh, er hatte einen guten Grund? In Ordnung.{w} Ein perversen Grund!"

    p "Nein, Hikari, hör ihr zu, ich hab wirklich einen Grund, und zwar einen guten--"

    "Sie ballt ihre Hand zu einer Faust zusammen."

    p "H-Hab doch Erbarmen mit mir!"

    scene bg black
    with flash

    stop music 

    "Ihre Faust fliegt auf mich zu … und kurz darauf sehe ich auf dem Boden liegend auch schon Sterne."

    "Ich liege eine Weile regungslos rum, ehe Sayaka und Hikari, nun völlig bekleidet, auf mich zukommen.{w} Warum müssen sie mir alles so schwer machen ...?"

    scene bedroom night
    $ sayaface='smiling'
    $ sayapose='school_1'
    $ hikaface='normal'
    $ hikapose='school_1'
    show Sayaka at left
    show Hikari at right
    with fade

    "Nachdem ich von meinem Treffen mit Yuzuki erzählt habe, scheint es endlich so, als wären sie bereit, mir einige Dinge zu erklären."

    "Ich führte sie in mein Zimmer, damit wir die Dinge in einer gemütlichen Umgebung klären konnen.{w} Das Zelt war zwar auch eine Option ...{w} aber meine Erinnerungen sind nicht gerade positv."

    "Sayaka stürzt sich auf mein Bett und schaut aufgeregt umher. Hikari hingegen steht noch immer wütend bei der Tür.{w} Ich hab mich doch bereits entschuldigt!"

    s "Also, das ist dein Zimmer, oder?{w} Es ist schön, es endlich von innen sehen zu können, nachdem ich es die ganze Zeit ausgespäht habe."

    "...Ich tu mal so, als hätte ich das nicht gehört."

    h "Es ist überraschenderweise ordentlich..."

    p "Okay, also ...{w} Wollt ihr mir endlich erzählen, was hier los ist?"
    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"
    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Hmm, ich frag mich, was Kenta so auf seinem Computer hat ..."

    "Sayaka greift nach meinem Laptop."

    p "L-Leute, konzentriert euch, okay?"

    $ sayaface='smiling'
    show Sayaka

    s "Hmm?{w} Oh, richtig, ja!"

    "Danke ..."

    $ sayaface='normal'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    "Sayaka nimmt einen ernsten Ausdruck an und setzt sich aufrecht hin.{w} Ich wusste gar nicht, dass sie zu so was überhaupt in der Lage ist."

    s "Wir wollten es dir wirklich erzählen, Kenta.{w} Das wollten wir nicht geheim halten ..."

    s "Wir dachten nur, wir könnten die Dinge alleine bewältigen, bevor wir dich darüber aufklären."

    s "Aber wie du von dieser Yuzuki-Person gehört hast, ist die Zeit jetzt wirklich knapp."

    $ hikaface='angry'
    show Hikari

    h "Was ich dir {i}immernoch{/i} nicht glauben kann, dass du uns bisher nichts davon erzählt hast.{w} Weißt du, in welche Gefahr du dich gebracht hast, als du sie getroffen hat?!"

    "Hikari mischt sich ein und geht zu Sayaka hinüber.{w} ... Genau deshalb hab ich ihr nichts gesagt."

    p "Ich weiß, es war dumm ...{w} aber es war der einzige Weg, damit ich was lern. Ihr wart schließlich nicht gerade hilfreich."

    h "Das ..."

    $ hikaface='normal'
    $ hikapose='school_2'
    show Hikari
    with dissolve

    "Sie verstummt.{w} Jetzt hab ich sie endlich da, wo ich sie haben wollte."

    $ sayaface='joking'
    show Sayaka

    s "Er hat einen guten Standpunkt, Hikari."

    $ hikaface='angry'
    show Hikari

    h "S-Stell dich nicht auf seine Seite!{w} Du sollst {i}mein{/i} Partner sein!"

    p "So, alles, was ich immer hör, ist, dass die Zeit davonläuft ...{w}Aber warum?{w} Was passiert morgen?"

    $ hikaface='normal'
    $ sayaface='normal'
    show Hikari
    show Sayaka

    s "Der Beginn von etwas sehr Schlimmen."

    p "Ach, echt jetzt?!{w} Jetzt hört endlich auf mit diesem mysteriösen Schwachsinn!"

    $ sayaface='scared'
    show Sayaka

    s "Schrei mich nicht an, Kenta.{w} Sheesh.{w} Komm runter, ich wollte es gerade sagen!"

    "Jetzt bin ich wohl ein bisschen zu weit gegangen ...{w} Ich ziehe mich ein wenig zurück und beruhige mich."

    $ sayaface='smiling'
    $ sayapose='school_2'
    show Sayaka
    with dissolve
    play music "bgm/seriousintro.ogg" fadein 2.0
    queue music "bgm/seriousloop.ogg"

    s "Sag mir Kenta, was weißt du von deiner Blutslinie?{w} Deinen Vorfahren?"

    p "Ähh ...{w} Nicht wirklich viel ...{w} Inwiefern ist das überhaupt wichtig?"

    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Dein Blut ist das Wichtigste hier!{w} Deshalb beschützen wir dich."

    $ sayaface='scared'
    show Sayaka

    s "Hikari, sei nicht so gemein."

    $ sayaface='normal'
    show Sayaka

    s "Aber ...{w} wegen deinem Blut wurden wir gesendet.{w} Wenn es in die falschen Hände gerät--nämlich Yuzukis--wären wir alle in großen Schwierigkeiten."

    p "Warum {i}mein{/i} Blut ...?{w} Was ist daran so besonders?"

    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Es ist vielleicht ein bisschen schwer zu glauben, aber du bist ...{w} nun, du bist der Nachkomme einer langen Reihe von Magiern - Menschen mit magischen Fähigkeiten."

    p "...Wie bitte?"

    "Wo um alles in der Welt haben sie das denn aufgegabelt?{w} Hätten sie mir das bereits bei unserem ersten Treffen gesagt, hätte ich sie als verrückt abgestempelt ..."
    
    "...Aber nach all dem, was ich bereits gesehen habe, fällt es mir leichter, das zu glauben."

    $ hikaface='angry'
    show Hikari

    h "Wie oft muss ich es dir noch sagen?{w} Du{w} hast{w} Magier{w} Blut!"

    "In mein Ohr zu schreien macht es auch nicht wirklich verständlicher ..."

    $ hikaface='normal'
    show Hikari

    p "Und warum wolltet ihr mir das nie sagen?{w} Es hört sich schließlich verdammt wichtig an ..."

    $ sayaface='smiling'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Weil die Welt generell nicht mehr weiß, was Magie ist.{w} Es ist einfach in alten Geschichtsbüchern verloren gegangen."

    s "Also wissen viele Leute mit dieser Blutlinie nicht einmal, dass sie Magier sind.{w} Es ist nur etwas, das jetzt schlummert."

    p "Okay.{w} Wenn also viele Leute dieses ...{w} Magierblut in sich tragen, warum ist meines dann so besonders?{w} ... Was macht es so wertvoll?"

    $ sayapose='school_1'
    $ sayaface='happy'
    show Sayaka
    with dissolve

    s "Ich bin froh, dass du gefragt hast!"

    "Sayaka springt vom Bett auf und überrascht mich dabei.{w} Dieses Mädchen kann auch nicht mal eine Minute lang still sitzenbleiben!"

    $ sayaface='smiling'
    show Sayaka

    s "Ich werde dich nicht mit der ganzen Geschichte langweilen, darum fasse ich mich kurz."

    "Sie räuspert sich, als würde sie gerade eine Präsentation in der Schule halten."

    s "Vor hunderten von Jahren, als die Magie noch in der Welt vorherrschte, gab es eine Magierin mit ungeheurer Macht."

    s "So viel Macht, dass sie {i}die{/i} Magierin zu der Zeit war.{w} Jeder hat zu ihr aufgesehen und sie war eine Inspiration für alle."

    s "Aber du weißt ja, was bei den Leuten passiert, die die größte Macht der Welt haben, oder?"

    $ sayaface='normal'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    "Sie runzelt die Stirn und seufzt."

    s "Sie wollen immer mehr Macht."

    s "Es verändert Leute.{w} Verdirbt sie."

    s "Also wollte sie über alles herschen.{w} Über jeden {i}einzelnen{/i}."

    s "All der Respekt, den die Leute vor ihr hatten, wurde zu Furcht.{w} Und sie übte schädlichen Einfluss auf das Land aus."

    s "Überall, wohin sie ging, folgte die Dunkelheit und breitete sich über das Land aus, während sie ihrer Eroberung folgte."

    "Das wird jetzt wohl länger dauern ...{w} Und warum kommt es mir so vor, als würde ich die Person kennen, von der sie spricht ...?"

    $ sayaface='smiling'
    show Sayaka

    s "Bist du noch dabei, Kenta?"

    "Sie lehnt sich nach vorne und gähnt dabei."

    p "H-Häh?{w} Ja, total!{w} Glaub ich zumindest ..."

    p "Und was hat diese Person mit mir zu tun?"

    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Dazu komm ich gleich!"

    $ hikaface='joking'
    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "Im Grunde bist du mit der Person verwandt, die den Mut hatte, sich gegen die dunkle Königin zu stellen und sie in ihre Schranken wies."

    $ sayaface='shocked'
    show Sayaka

    s "H-Hikari!{w} Warum musstest du ihn spoilern?!"

    $ hikaface='angry'
    show Hikari

    h "Wenn du die ganze Geschichte erzählst, werden wir hier noch bis zum Sonnenaufgang sitzen!{w} Und Zeit ist hier essentiell."

    $ sayaface='normal'
    show Sayaka

    s "Aww ...{w} Ich wollte es dramatisch sagen und so."

    p "Äh, danke, Hikari."

    $ hikaface='normal'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Hmph."

    p "Und ...{w} Weiter?{w} Mein Vorfahre hat diese böse Königin getötet?"

    h "Wenn er es getan hätte, würden wir nicht hier sein und ein Gespräch führen."

    h "Nein, mit all der Macht, die sie hatte, war es unmöglich sie zu töten.{w} Ich würde nicht so weit gehen zu sagen, dass sie unsterblich war ... {w} aber ich bin mir sicher, dass es ziemlich nah dran ist."

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Das beste, was man machen konnte, war sie zu versiegeln.{w} Es war das stärkste Siegel, das er machen konnte.{w} Was uns zurück zu diesem magischen, alten Blut führt, das in dir ist, Kenta."

    s "Im Wesentlichen band er sein Schicksal mit ihr, als er sie wegsperrte.{w} Ein Siegel, das so mächtig ist, dass es nur entfernt wird, wenn eine strenge Bedingung erfüllt wird!"

    p "Und ...{w} wie lautet die?"

    $ hikaface='angry'
    show Hikari

    h "Ich denke, dass solltest du jetzt schon wissen!"

    p "Lass mich raten ... Es hat etwas ...{w} mit meinem Blut zu tun, stimmt's?"

    $ hikaface='normal'
    $ sayaface='smiling'
    show Hikari
    show Sayaka

    s "Bingo!{w} Ihr Siegel wird nur dann wirklich entriegelt, wenn es in Kontakt mit dem Blut desjenigen kommt, der sie weggesperrt hat, oder im Nachhinein, eines seiner Nachkommen."

    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Nun, eigentlich nicht nur {i}irgendein{/i} Nachkomme.{w} Es muss einer sein, der latente magische Kraft in sich hat."

    p "Das heißt dann also ..."

    s "Ich meine, dein Vater ist sicher und die Schatten haben kein Interesse an ihm.{w} Er hat {i}etwas{/i} Magie in seinem Blut, aber es ist nicht genug, um irgendwelche Fähigkeiten zu aktivieren."

    "Häh ...{w} Das ist ziemlich praktisch."

    $ sayaface='normal'
    show Sayaka

    "Sayaka streckt sich und gähnt dabei.{w} Es muss wirklich anstrengend für sie gewesen sein, ihre Aufmerksamkeit so lange auf ein einziges Thema zu fokussieren.{w} Aber ich denke, jetzt ergibt alles ein wenig Sinn ..."

    $ sayaface='smiling'
    show Sayaka

    s "So, kannst du mir so weit folgen?"

    p "Ja.{w} Glaub schon.{w} Um es kurz zusammenzufassen ... Mein Blut ist der Schlüssel dafür, etwas Schreckliches in Bewegung zu setzen?"

    $ sayaface='happy'
    show Sayaka

    s "Ziemlich genau!"

    p "Aber wenn es mit meinem Blut in Verbindung steht ...{w} Warum läuft uns dann die Zeit davon?"

    $ sayaface='smiling'
    $ hikapose='school_2'
    show Hikari with dissolve
    show Sayaka

    h "Das Siegel wird glücklicherweise nie brechen, wenn dein Blut nicht vergossen wird ... {w}, aber es ist schon lange her, seit sie eingesperrt wurde."

    h "Das bedeutet, dass das Siegel mit jedem Tag in seiner Wirksamkeit schwächer wird, und ihr Einfluss schleicht sich so langsam in die Welt ein."

    s "Kenta, deine Kopfschmerzen ..."

    p "Verstehe ...{w} Sie ruft also schon nach mir ...{w} um es metaphorisch auszudrücken?"

    h "Deshalb sind die Monster so gut organisiert.{w} Und warum dieses Mädchen, Yuzuki..."

    h "Sie gab diesem Mädchen die Kraft, die sie aufbringen konnte, und benutzt sie als Marionette, bis sie sich schließlich selbst befreien kann."

    $ hikaface='angry'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Ich bin mir nicht sicher, welche Lügen sie diesem Mädchen erzählt haben muss, um sie dazu zu bringen, zu gehorchen, aber ihre Gedanken sind infiziert."

    h "Und angesichts der gegenwärtigen Rate, in der ihre Niedertracht aus ihrem Gefängnis gesickert ist ... wird sie morgen noch mehr Einfluss auf die Welt bekommen."

    h "Die Monster werden stärker und aggressiver werden...{w} Yuzuki wird auch stärker werden."

    $ sayaface='normal'
    show Sayaka

    s "Also wird unser Job noch schwierieger."

    p "Das ...{w} Das ist nicht gut, oder?"

    s "Gar nicht!"

    $ sayaface='smiling'
    $ hikaface='normal'
    show Sayaka
    show Hikari

    s "Was uns zum nächsten Punkt bringt."

    s "Als wir zuerst beauftragt wurden, auf dich aufzupassen, mussten wir uns nur um einen oder zwei verstreute Schatten kümmern, wenn sie plötzlich entschlossen waren, instinktiv zu handeln."

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Und das war einfach genug.{w} Du hattest keine Ahnung, dass sie existieren und wir haben uns auch von dir ferngehalten."

    s "Und dann fingen die Dinge an, schlecht zu werden ...{w} als du den Schatten gesehen hast ...{w} wir waren wirklich überrascht!"

    s "Es war, als ob es auf einer Mission war, und rutschte vollkommen an unserer super-aufmerksamen Wache vorbei."

    h "Wenn ich mich zurückerinnere, war das nicht der Tag, wo du auf das Sandwich bestanden hast--"

    $ sayaface='happy'
    show Sayaka

    s "Nein!{w} Wir waren immer wachsam!"

    "Hmm ...{w} Ich schätze, ich hatte sogar noch mehr Glück, als ich ursprünglich dachte."

    $ sayapose='school_1'
    $ sayaface='smiling'
    show Sayaka
    with dissolve

    s "Als wir gezwungen waren, uns dir zu zeigen, war klar, dass etwas nicht stimmte.{w} Absolut nicht."

    s "Und das war noch offensichtlicher, als uns Yuzuki angegriffen hat.{w} Sie hatte eine Kraft, die wir noch nie gesehen haben!"

    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "Wir haben nachgesehen, als Freizeit war...{w} Das ist selten, wenn es darum geht, auf dich aufpassen zu müssen."

    "Na tut mir leid, dass ich überhaupt auf die Welt gekommen bin!"

    h "Und es wurde schnell klar, dass sich die Dinge nicht von selbst lösen würden, als wir erfahren hatten, dass dieses Siegel an Ort und Stelle langsam schwächer wird."

    $ sayaface='normal'
    show Sayaka

    s "Wir müssen ihr Gefängnis erneuern.{w} Es verstärken, sodass sie keinen Einfluss auf diese Welt mehr hat."

    s "Aber, wenn es so einfach wäre ...{w} hätten wir es schon selbst gemacht."

    "Sayaka macht einen ziemlich komplizierten Gesichtsausdruck ...{w} Ich glaube kaum, dass mir das, was sie als nächstes fragen wird, gefallen wird."

    s "Kenta ...{w} Wir ...{w} wir brauchen deine Hilfe."

    p "M-Meine?!{w} Wie zum Teufel soll ich helfen?{w} Ihr habt doch die Zauberkräfte, nicht ich!"

    h "Es ist nicht gerade ideal, dass wir uns auf dich verlassen müssen, ich weiß, aber wir haben keine Wahl. {w} Und wir haben keine Zeit mehr, nach alternativen Mitteln zu suchen."

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Grundsätzlich, da das Siegel von jemandem in deiner Blutlinie erstellt und direkt mit ihnen verbunden wurde, kann es nur durch jemanden verstärkt werden, der das gleiche Blut trägt."

    $ sayaface='scared'
    show Sayaka

    s "Ich meine, technisch gesehen könnten {i}wir{i} das Siegel zerbrechen und sie in eine neue Falle verwickeln ...{w} Aber ich denke nicht, dass wir lange genug durchhalten würden, um das zu tun."



    "Mit anderen Worten, ich bin hier der einzige, der das Problem lösen kann.{w} Ich bin nicht sicher ...{w} wie ich darauf reagieren soll."

    p "Ich hab von diesem Magier-Zeugs überhaupt keinen Plan.{w} Bin ich dazu überhaupt in der Lage?"

    $ sayapose='school_1'
    $ sayaface='normal'
    show Sayaka
    with dissolve

    "Sayaka beobachtet mich und nimmt sich einen Moment Zeit, um über etwas nachzudenken."

    s "Erinnerst du dich an die Nacht, als Hikari mit diesem Tentakelschatten Spaß hatte??"

    $ hikaface='embarrassed'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Ich hatte {i}keinen{/i} Spaß!"

    p "Kann ich mir vorstellen.{w} Aber was hat das damit zu tun?"

    $ hikaface='normal'
    show Hikari

    s "Du hast ihr Schwert benutzt, oder?"

    p "Ja.{w} Aber ich ..."

    h "Kenta, du musst selbst bemerkt haben, wie leicht das Schwert war, trotz seiner Größe, richtig?"

    h "Es ist eine Klinge, die von Magie durchdrungen ist und sich mit dem Träger verbindet, um schnelle und kraftvolle Schläge mit Leichtigkeit auszuführen."

    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "So durchdrungen, dass, wenn jemand, der nicht in der Lage ist, diese Menge an Magie zu kontrollieren, versuchen würde, es zu führen ..."

    $ sayaface='smiling'
    show Sayaka

    s "Sie würden explodieren.{w} Die Magie wäre zu viel für sie."

    p "B-BUMM?"

    s "Also, vielleicht nicht explodieren.{w} Aber es würde zumindest ein unordentliches Ende bringen."

    s "Und da du immer noch stehst, nachdem du das Ding herumgeschwungen hast, kann man mit Sicherheit sagen, dass du das Potenzial in dir hast."

    "Ich kann nicht glauben, dass die Möglichkeit besteht, dass ...{w} man durch das Aufheben ihres Schwertes in Stücke zerfetzt wird."
    
    "Dann war das, was ich damals getan hab, ja noch rücksichtsloser, als ich ursprünglich vermutet hab!"

    $ sayaface='happy'
    show Sayaka

    s "Also, wenn du mit diesem Schwert umgehen kannst, denke ich, dass ein wenig Versiegelungsmagie kein Problem sein sollte!"

    h "Aber dann bedeutet es auch, dass wir dorthin gehen müssen, wo sie versiegelt ist...{w} und die eine Sache mitnehmen, die sie seit Jahren beghert."

    $ sayaface='normal'
    show Sayaka

    h "Es würde leichtsinnig sein.{w} Und ein Fehler kann die ganze Welt in Gefahr bringen."

    p "Wir haben also überhaupt keinen Stress, hm?"

    "Ich versuche mein Bestes, mir all die erwähnten Dinge nicht zu sehr zu Herzen zu nehmen.{w} Kaum zu glauben, dass ich der einzige bin, der diese Frau aus diesem Gefängnis befreien und gleichzeitig für immer wegsperren kann."

    h "Morgen ist unsere letzte Chance, das zu stoppen, bevor es außer Kontrolle gerät."

    $ hikaface='joking'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Ich denke, du wirst einen Tag in der Schule überspringen müssen, Kenta."

    "...Hmm.{w} Ich frage mich, ob ‚die Welt retten‘ als Entschuldigung gut genug ist, um von der Schule fernzubleiben?"

    $ hikaface='normal'
    show Hikari

    h "Natürlich nur, wenn du uns helfen willst.{w} Ich verstehe es, wenn du dafür nicht bereit bist ...{w} Vielleicht können wir einen anderen Weg finden ..."

    p "Anderen Weg gibt's wohl keinen, oder?{w} Sonst würdet ihr mir das alles ja nicht erzählen, oder?"

    "Ich seufze und schaue meine beiden Schutzengel an.{w} Sie haben in den letzten Tagen schon so viel für mich getan."
    
    "Vieles davon sogar im Hintergrund, wovon ich nichts mitbekommen hab.{w} Ich schulde es ihnen förmlich."

    "Ich schlucke hinunter.{w} Ich spüre schon, wie meine Hände zu zittern beginnen.{w} Gehe ich mit ihnen mit, könnte ich sterben."

    "Aber gehen wir nicht, wird es auch nicht besser.{w} Von daher ..."

    p "Dann hab ich wohl keine andere Wahl.{w} Ich ...{w} Ich werd beim Versiegeln helfen.{w} Wenn ihr so zuversichtlich seid, dass ich es kann."

    $ sayapose='school_2'
    $ sayaface='happy'
    $ hikaface='shocked'
    show Hikari
    show Sayaka with dissolve

    s "Du wirst es tun?!"

    "Sayaka klatscht ihre Hände zusammen.{w} Hat sie etwa nicht mit meiner Hilfe gerechnet?{w} Hikari sieht ebenfalls überrascht aus.{w} Leute, ein bisschen mehr Vertrauen könntet ihr schon haben!"

    p "Das ist das Mindeste, was ich tun kann, nachdem ihr immer euer Leben für mich riskiert habt.{w} Es ist egal, wie ich euch helfen kann, Hauptsache ich kann helfen!"

    h "Kenta..."

    $ sayaface='joking'
    show Sayaka

    s "Du hättest gerade fast cool geklungen.{w} Fast!{w} Ich denke, wir müssen an deinem heroischen Dialog arbeiten."

    $ hikaface='normal'
    $ sayaface='normal'
    show Hikari
    show Sayaka

    s "Aber darum kümmern wir uns später.{w} Es gibt viel zu tun, wenn du diese dunkle Königin versiegeln willst, also pass auf!"
    stop music fadeout 6.0
    "Und gerade in dem Moment, wo ich dachte, die Nacht könnte nicht noch länger werden, beginnt eine weitere Erklärung."

    scene bg black
    with fade

    "Ich bin sicher, es war für die beiden nicht einfach, mir die Grundlagen der Magie beizubringen."

    "Und ich bin mir auch nicht sicher, dass ich es bereits verstanden hab ...{w} aber nach einigen Stunden des Übens, haben sie mir versichert, dass ich es verstanden hab."

    "Ich werd es aber erst wissen, wenn es hart auf hart kommt.{w} Und das macht mir Angst.{w} Was, wenn sie mein Potential falsch eingeschätzt haben?{w} Oder wenn ich es versaue?{w} Oder ...{w} unzählige andere Möglichkeiten, die noch auftreten könnten."

    "Das sind alles Gedanken, die mir durch den Kopf gehen, nachdem die beiden Mädchen bereits wieder in ihr Zelt zurückgekehrt sind."

    "Und der letzte Gedanke, den ich vor dem Einschlafen hatte, ist, dass morgen der härteste Tag meines Lebens bevorsteht."

    with Pause(3.5)
    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"
    scene bedroom day
    with wake

    "Ich komme langsam zur Besinnung.{w} Der Morgen ist angebrochen."

    "Wir dürfen keine Zeit verschwenden!{w} Ich fühle mich jedoch munterer als die Tage zuvor.{w} Was mich wundert, wenn man bedenkt, wie wenig Schlaf ich bekommen hab."

    "Ich schätze, die Angst vor dem, was passiert, wenn ich all das vermassle, bewegt mich zum Weitermachen.{w} Eine bessere Motivation gibt's gar nicht!"

    p "Okay, dann an die Arbeit!"

    "Ich blicke in die entschlossenen Augen, die mich aus dem Spiegel heraus anstarren.{w} Das ist der fokussierteste Blick, den ich je in meinem Leben gesehen hab."

    "Schon komisch, wie viel sich in den letzten Tagen verändert hat.{w} Und noch komischer, wie ich all das akzeptiere.{w} Es ist so, als hätte ich tief im Inneren bereits gewusst, dass all das passieren wird."

    "Ich ziehe mich an und gehe ins Esszimmer."

    scene kitchen day
    $ sayaface='smiling'
    $ sayapose='magical_1'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka at left
    show Hikari at right
    with dissolve

    "Die beiden Mädchen warten bereits auf mich.{w} Obwohl, es überrascht mich ein wenig, dass die beiden bereits ihre Kampfanzüge an haben."

    s "Gut'n Morgen.{w} Hast du gut geschlafen?"

    p "Wenn ich daran denke, was mich erwartet ... Ja."

    $ hikapose='magical_2'
    show Hikari
    with dissolve

    h "Achte darauf, gut zu essen bevor wir gehen.{w} Du wirst die Kraft brauchen."

    "Stimmt, genau.{w} Na klar.{w} Ich gehe in die Küche und mache das Einfachste, was mir auf die Schnelle einfällt."

    p "Was ich gestern ganz vergessen hab zu fragen ...{w} Wo ist diese 'Königin' überhaupt gefangen?"

    $ sayaface='normal'
    show Sayaka

    s "Häh?{w} Haben wir das nicht besprochen?{w} Sie ist gleich außerhalb der Stadt versiegelt."

    p "Was?!"

    "Vor Schock lasse ich fast den Teller fallen, den ich gerade in Händen halte."

    p "So nah?!"

    $ hikaface='angry'
    show Hikari

    h "Natürlich.{w} Warum sonst denkst du, dass sich ihr Einfluss hier so leicht ausbreitet??"

    p "Ich ...{w} Damit hab ich jetzt echt nicht gerechnet.{w} Aber wenn man es so sieht, ist es irgendwie logisch ..."

    $ hikaface='normal'
    show Hikari

    "Aber dass sie bereits all die Zeit über so nah war.{w} Kein Wunder, dass es sich hier immer mehr abgespielt hat ..."

    "Sie muss wütend sein ...{w} In Anbetracht der Tatsache, dass der Schlüssel für ihre Freiheit zum Greifen nahe ist."

    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Obwohl wir wussten, wo sie sich ungefähr befindet, haben wir sie erst gestern Abend eindeutig lokalisieren können."

    s "Sie befindet sich in einem Wald am Stadtrand, versteckt in einer Höhle außer Sichtweite.{w} Der Ort drumherum ist ziemlich geschichtsträchtig, nehme ich an."

    s "Vielleicht war der Wald mal Teil von etwas Großem.{w} Ihre alte Operationsbasis vielleicht?"

    $ hikapose='magical_1'
    show Hikari
    with dissolve

    h "Nichts davon ist wichtig.{w} Wir müssen einfach nur da reinkommen, das Siegel stärken, und dann sollte unser Leben {i}viel{/i} einfacher sein."

    p "Und wird sich das alles wirklich einfach so von selbst in Ordnung bringen, wenn wir Magie verwenden?"

    h "Naja, es wird die Macht, die sie hat, ausschalten .{w} Das heißt, die Monster werden zu ihren geistlosen Hülsen zurückkehren, und die Dinge sollten sich hier unten beruhigen."

    $ hikaface='angry'
    show Hikari

    h "Und nachdem alles geregelt ist, können wir endlich heimgehen.{w} Ich schwöre, ich werde verrückt, wenn ich noch einen Tag mehr an dieser Schule verbringen muss."

    $ sayaface='joking'
    show Sayaka

    s "Aww, tu doch nicht so, als wärst du so verzweifelt.{w} Ich weiß doch genau, dass du Spaß mit Kenta hattest."

    $ hikaface='embarrassed'
    show Hikari

    h "S-Sei nicht lächerlich!{w} Ich mach nur mein Job ..."

    $ sayapose='magical_1'
    $ sayaface='happy'
    show Sayaka
    with dissolve

    s "Du kannst mich nicht hinters Licht führen.{w} Nicht, wenn dein Gesicht so knallrot ist!"

    h "H-Hmph.{w} Gehen wir jetzt, oder was?!"

    "Sayaka kichert und schlägt ihrer Partnerin in die Rippen.{w} Ich vermute mal, es ist gut, dass sie trotz der bevorstehenden Aufgabe so gut gelaund sind, oder ...?"

    scene bg black
    with fade
    stop music fadeout 3.0
    "Wir gehen los.{w} Wir nehmen die Routen, auf denen weniger los ist, da wir keine Aufmerksamkeit erregen möchten."

    "Sie haben mir auch angeboten, dort hinzufliegen.{w} Aber ...{w} Hah.{w} Nein.{w} Zu Fuß gehen ist auch gut.{w} Ich bin sicher, dass es nicht so eine Eile hat."

    "Nach einem kurzen Spaziergang wird unsere Umgebung immer weniger innerstädtisch. Desto weiter wir gehen, desto weniger Gebäude sehen wir, ehe wir über einen Zaun und in die Wildnis marschieren."

    scene forest trail
    with fade

    "Über unserem Kopf beschützen uns Äste und Zweige vor der einstrahlenden Sonne.{w} Nur ein ganz kleiner Lichtstrahl dringt hindurch, und der erhellt uns unseren Weg."

    "..."
    play music "bgm/magicalgirlintro.ogg" fadein 5.0
    queue music "bgm/magicalgirlloop.ogg"
    "Als wir an einem Baum vorbeikommen, von dem ich glaube, ihn bereits drei Mal gesehen zu haben, fange ich an, daran zu zweifeln, ob sie auch wirklich den Weg kennen."

    $ sayaface='smiling'
    $ sayapose='magical_1'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka at left
    show Hikari at right
    with dissolve

    s "Hmmm.{w} Vielleicht hätten wir eine Karte mitnehmen sollen?"

    "Nun.{w} Das bestätigt das Ganze ja nur.{w} Wir sind hoffnungslos verloren!"

    "Jede Anspannung, die noch zu spüren war, verschwindet schlagartig, als Sayaka anfängt, sich am Kopf zu kratzen und sich umzusehen."

    $ hikaface='angry'
    show Hikari

    h "Wirklich?{w} Uns wurde die Wegbeschreibung vorher klar gesagt.{w} Wie kannst du sie einfach vergessen?!"

    $ sayaface='happy'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Okay, du gehst vor."

    $ hikaface='scared'
    $ hikapose='magical_2'
    show Hikari
    with dissolve

    h "Ich...{w} Bah, fein.{w} Ich hab es auch vergessen!"

    $ sayaface='joking'
    show Sayaka

    s "Siehst du!{w} Niemand ist perfekt, auch wenn du immer wieder glaubst, du wärst es."

    $ hikaface='angry'
    show Hikari

    h "Ich denke nicht, dass ich perfekt bin!{w} Aber im Vergleich zu dir--"

    p "Äh, Leute?{w} Muss das jetzt sein?"

    h "Aber sie ...{w} Fein.{w} Du hast recht.{w} Konzentrieren wir uns, Sayaka."

    $ sayaface='smiling'
    $ sayapose='magical_1'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka
    show Hikari
    with dissolve

    "Und ich dachte, die Versiegelung wäre das Schwierigste an der ganzen Sache ...{w} Mein Gott."

    s "Okay, der Wald ist nicht so groß.{w} Glaub ich.{w} Ich bin sicher, wir finden die Höhle, wenn wir noch ein bisschen umherwandern!"

    "Hat uns dieses 'Umherwandern' nicht erst in diese Situation gebracht?{w} Ich befürchte, dass sogar die Sonne untergeht, bevor wir diese Höhle finden!"

    "Ich weiß, dass es nicht helfen wird, aber ich kundschafte die Gegend ebenfalls aus.{w} Ich weiß ja nicht mal, wonach ich suchen soll, abgesehen von ..."

    p "Eine Höhle ...?"

    s "Hm?{w} Ist was?"

    "Ich schiele auf etwas in der Ferne.{w} Eine Ansammlung von Felsbrocken hat meine Aufmerksamkeit erregt.{w} Meine Augen werden fast schon auf magnetische Art und Weise angezogen."

    "Ich war hier zwar noch nie ...{w} aber dennoch kommt es mir bekannt vor."

    p "Können wir da kurz nachsehen?"

    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Klar!{w} Wir haben sowieso keine besseren Anhaltspunkte.{w} He-hehe-hehe ..."

    with Pause(2.5)

    "Wir wandern alle zusammen zu der merkwürdigen Felsformation hinüber.{w} Könnte es das wirklich sein?"

    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "Hmm, hmm.{w} Was hast du dort drüben denn gesehen?"

    "Sayaka fängt an, gegen die Felsen zu stochern und denkt dabei stark nach."

    "Eine Runde um die Felsformation hat nichts Außergewöhnliches offenbart, aber ...{w} da muss mehr dahinterstecken."

    p "Weiß nicht.{w} Mir ist vorgekommen, als hätt ich was gespürt."

    $ hikaface='angry'
    show Hikari

    h "Das sind einfach nur ein paar dumme Steine.{w} Wir verschwenden Zeit!"

    s "Aww.{w} Wir sollten echt mal nachsehen, wenn Kenta schon sagt, er sieht dort was.{w} Er ist mit der dunklen Königin doch verbunden, oder?{w} Er muss ein paar Dinge über sie wissen, wenn auch nur im Unterbewusstsein."

    "Sagt sie, als sie mit ihren Knöchel auf den Felsen schlägt."

    $ hikaface='normal'
    $ sayaface='happy'
    show Sayaka
    show Hikari

    s "Oh!{w} Der scheint irgendwie locker zu sein."

    "Sayaka greift nach dem lockeren Stein und versucht, ihn mit aller Kraft hervorzuziehen."

    $ sayaface='scared'
    show Sayaka

    s "Hrghh!{w} I-Ich könnte eure Hilfe hier gut gebrauchen!"

    "Ah, genau.{w} Ja.{w} Ich sollte besser helfen!{w} Es war schon fast amüsant, mitanzusehen, wie sie gegen die Felsbrocken stochert."

    $ sayaface='normal'
    show Sayaka
    with hpunch

    "Ich gehe auf die andere Seite und versuche mit all meiner Kraft - also fast gar keiner - dagegenzudrücken."

    "..."

    "Wir können ihn aber trotzdem nicht bewegen.{w} Er bewegt sich keinen Zentimeter.{w} Nicht mal mit vereinten Kräften.{w} Und ich gebe wirklich mein Bestes!"

    "Der Felsen fühlt sich aber wirklich lose an.{w} Aber anscheinend nicht locker genug!"

    "Ich bin sicher, mit einer Person mehr würden wir es schaffen ..."

    $ hikaface='angry'
    show Hikari

    h "Um Gottes willen!{w} So wird das nie was.{w} Bleibt zurück!"

    $ hikapose='magical_2'
    show Hikari
    with dissolve

    "Plötzlich zückt sie blitzartig ihr Schwert.{w} Hey, warte, wir stehen direkt daneben, ist das nicht gefähr--"

    "Sie schlägt ohne Vorwarnung drauf ein und teilt den Fels in zwei Hälften."

    $ sayaface='shocked'
    show Sayaka

    s "Wahh!"

    p "Oof ..."

    $ hikaface='normal'
    show Hikari

    "Wir verstummen beide, als der Fels auf beiden Seiten hinunterfällt.{w} Ich hab irgendwie das Gefühl, als wäre mein Haar auf einmal etwas kürzer."

    $ sayaface='angry'
    show Sayaka

    s "H-Hikari!"

    $ hikaface='joking'
    show Hikari

    h "Siehst du?{w} Problem gelöst."

    s "Das ..."

    $ sayaface='normal'
    show Sayaka

    "Auf einmal Stille.{w} Der Felsen wurde letzten Endes ja aus dem Weg geräumt."

    $ hikaface='normal'
    $ hikapose='magical_1'
    show Hikari
    with dissolve

    "Wir beide springen auf, um gemeinsam mit Hikari die Folgen dieser Zerstörung zu betrachten."

    "Vor all der Aufregung vergesse ich schon fast, wie man atmet.{w} Könnte es das wirklich sein ...?"

    "...!"

    $ sayaface='shocked'
    $ hikaface='shocked'
    show Sayaka
    show Hikari

    "Plötzlich schnappen wir alle auf einmal nach Luft.{w} Ich wusste es!{w} Ich weiß zwar nicht wie, aber irgendwie wusste ich's!"

    "Hinter dem Felsen liegt ein Tunnel, der tief in die Dunkelheit führt."

    "Man kann nicht erkennen, wie weit sich dieser Tunnel erstreckt, oder ob er überhaupt wo hin führt."

    "Aber wenn sich schon jemand die Mühe gemacht hat, ihn so gut zu verstecken, dann muss er {i}irgendwo{/i} hinführen, oder?"

    $ hikaface='normal'
    show Hikari

    h "Ist es ...{w} das wirklich?"

    $ sayaface='smiling'
    show Sayaka

    s "Fühlt sich echt so an!{w} Man kann die Dunkelheit förmlich spüren."

    "Das ist eigentlich etwas, was man nicht so fröhlich sagen sollte ..."

    "Aber sie hat recht.{w} Da macht sich ein Gefühl der Verzweiflung breit, wenn man in das Loch blickt.{w} Eine starke Anspannung liegt in der Luft - so, als würde uns das, was da unten lauert, verzehren wollen."

    "Wenn wir erstmal da runtergehen ...{w} dann war's das.{w} Dann werden wir diesem Wahnsinn endlich ein Ende setzen und Frieden finden."

    "...Hab ich wirklich die Kraft dazu, das durchzustehen?{w} Ein längst vergessenes Übel wiederzuversiegeln--"

    $ sayaface='happy'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Genug Zeit vergeudet!{w} Rein mit uns!"

    p "H-Hey, warte!"

    hide Sayaka
    show Hikari at center
    with dissolve

    "Sayaka hat anscheinend keine Lust darauf, bis ich meine Gedanken sortiert habe, und geht auf ihre Knie, um in das Loch zu krabbeln."

    h "Sie hat recht.{w} Wir können nicht noch mehr Zeit verschwenden.{w} Los geht's, Kenta!"

    hide Hikari
    with dissolve

    "Hikari zögert zwar noch einen kurzen Augenblick, folgt aber gleich hinterher."

    "Sie verschwinden völlig in der Dunkelheit.{w} Es macht mir irgendwie Angst, so wenig Licht wie da unten scheint."

    "Hmm..."

    h "Hör auf, herumzualbern, oder du wirst zurückbleiben!"

    "Hikaris Worte, die aus dem Tunnel hallen, machen das Ganze noch gruseliger."

    p "Okay, okay!{w} Ich komm ja schon."

    "Wegen einer Minute mehr oder weniger wird die Welt auch nicht untergehen.{w} Zumindest hoffe ich das."

    "Ich falle auf die Knie und krabble ebenfalls hinein."

    scene bg black
    with fade

    "Ich kann gerade mal die Geräusche erkennen, die die beiden Mädchen vor mir erzeugen.{w} Ihre Anwesenheit ist auch das einzige, was mich dazu bringt, nicht die Fassung zu verlieren."

    "Meine Umgebung ist finster.{w} Kalt.{w} Feucht.{w} Bis jetzt war es also keine angenehme Erfahrung."

    p "Weißt du ..."

    s "Hmm, ist was?"

    p "Das hab ich mir echt nicht vorgestellt, als ich daran gedacht hab, wie es wär, ein Held zu sein."

    p "In einem engen, kleinen Tunnel rumkriechen ...{w} Ich hab mir das irgendwie dramatischer vorgestellt."

    "Sayaka kichert."

    s "Ich bin sicher, vor uns warten genug dramatische Momente!{w} Wir müssen vorher nur durch die ... {i}weniger{/i} ... dramatischen Momente."

    s "Und hey, das ist gar nicht so schlimm.{w} Zumindest müssen wir uns nicht durch unzählige Schatten durchkämpfen."

    s "Es ist zwar nicht die edelste Art und Weise, die Dinge anzugehen, aber es spart Kraft ..."

    "Das ist ein Argument.{w} Aber trotzdem ..."

    p "Aber was, wenn ...{w} {i}in{/i} diesem Tunnel Monster auf uns warten?{w} Falls das der Fall ist, können wir nicht wirklich viel tun."

    h "S-Sag das nicht!{w} Ich hab nichtmal über soetwas nachgedacht ..."

    s "Oh, wow, du hast recht.{w} Wir wären völlig wehrlos!"

    h "Sayaka!"

    s "Die würden uns echt massakrieren.{w} Hikari kann hier wohl kaum ihr Schwert einsetzen und ich erst recht nicht meinen Bogen."

    s "Ich frage mich, welcher Schatten durch diese Tunnel passt?{w} Oh!{w} Vielleicht irgendetwas mit Tentakel ... Ich weiß nämlich genau, dass die dich {i}lieben{/i}, Hikari!"

    h "Sei ruhig!{w} Jetzt bist du einfach nur böse!"

    "Hmm ...{w} Vielleicht hätte ich meine Gedanken für mich behalten sollen?{w} Sayaka hat hier eindeutig zu viel Spaß."

    s "Oder wie wär's mit--"

    h "H-hiyahh!{w} Irgendwas hat mich berührt!"

    "Hikari schreit so laut auf, dass mir dabei fast das Trommelfell zerplatzt."

    h "Warst du das, Kenta?!{w} Ich wusste, ich hätte als Letzte einsteigen sollen ..."

    p "Ich?!{w} Natürlich nicht!{w} Ich bin ja ganz woanders!{w} Wofür hältst du mich eigentlich?"

    h "...Willst du wirklich, dass ich das beantworte, nach dem, was du in den letzten Tagen getan hast??"

    p "D-Das waren Unfälle! UNFÄLLE!"

    h "Naja, vielleicht war das wieder einer deiner 'Unfälle', hmm?{w} Ein Mädchen begrapschen, während sie komplett hilflos ist?"

    p "Komm schon, ich bin ja nicht mal in deiner Nähe!{w} ... Vielleicht bildest du dir das auch einfach nur ein?"

    "Ich kann gerade noch hören, wie Sayaka ein Kichern unterdrückt.{w} Hmmm."

    play music "bgm/mischiefintro.ogg" fadein 2.0
    queue music "bgm/mischiefloop.ogg"

    h "F-Fein.{w} Wenn du es nicht warst, wer dann?{w} Es konnte nicht Sayaka sein, da sie vor mir ist."

    s "Vielleicht war es ein großer, schleimiger Tentakel, der Hallo sagen wollte."

    "Sagt sie in einer fast singenden Art und Weise.{w} Okay, ja, jetzt versteh ich‘s.{w} Ich hoffe, Hikari wird es auch bald merken."

    h "E-Es hätte aber nicht--kyahh!{w} Da ist es wieder!"

    h "Okay, ernsthaft was ist--a-ah!"

    "Diese Serie an merkwürdigen Ereignissen dauert länger, als ich es für nötig empfinde, bis ich schlussendlich das Gefühl habe, dass ich hier ein Machtwort sprechen muss."

    p "Okay, komm, Sayaka, das reicht jetzt.{w} Du hattest deinen Spaß.{w} Jetzt müssen wir uns aber wieder konzentrieren, okay?"

    h "W-Was ...?{w} Sayaka?{w} Aber sie hätte nicht ..."

    "Sayaka bemerkt meinen Verdacht, lässt aber trotzdem nicht locker."

    s "Aww, okay, okay.{w} Ich musste einfach.{w} Es ist einfach so leicht, sie zu ärgern!"



    h "..."

    "Hikari holt tief Luft ...{w} Uh-Oh."

    h "Ich werde dich umbringen, Sayaka!"

    s "Da musst du mich erstmal fangen!"

    "Dadurch, dass sich Sayakas Lächeln immer entfernter anhört, bemerke ich, dass sie immer schneller nach vorne krabbeln."

    "Ich betrachte es mal als positiv, dass sie trotz der bevorstehenden Aufgabe so gut gelaunt bleiben können."

    "...Aber ich betrachte es als überaus negativ, dass sie mich einfach so zurücklassen."

    "Ich denke darüber nach, in meinem eigenen Tempo weiterzukrabbeln, da ich irgendwann ohnehin bei ihnen sein werde, aber dann fühle ich plötzlich etwas Schleimiges an meiner Hand, das mich zum ‚Sprint‘ bewegt."

    "Ich weiß nicht, ob in diesem Tunnel etwas auf uns lauert, aber ich will auch nicht hier bleiben, um es herauszufinden."

    with Pause(3.0)

    "Schließlich schaffe ich es irgendwann, meinen Abstand aufzuholen."

    "Diese Wanderung fühlt sich mittlerweile nach einer gefühlten Ewigkeit an."

    "Es gab ja nicht mal eine Garantie dafür, dass uns dieser Tunnel zum Ziel führt, und trotzdem krabbeln wir einfach weiter."

    "Wenn sich also herausstellt, dass das alles nur Zeitverschwendung war, dann war das ganz allein meine Schuld."

    "Und bis jetzt haben wir überhaupt nichts gefunden, was darauf hindeutet, dass wir uns auf dem richtigen Weg befinden."

    "Ich spüre, wie die Verzweiflung einsetzt."
    stop music fadeout 4.0
    "Was, wenn wir in einer Sackgasse landen?{w} Oder irgendwo steckenbleiben?"

    "Was, wenn ..."

    s "Ooh, hey!{w} Ich glaube, ich seh dort vorne etwas."

    h "Wurde auch Zeit!"

    "Sayakas fröhliche Stimme reißt mich aus meinen finsteren Gedanken.{w} Ich schätze, ich sollte meinen eigenen Instinkten hin und wieder wirklich mehr vertrauen."

    "Getreu ihren Worten erkenne ich weiter vorne wirklich ein Licht."

    "Nur noch ein bisschen, und dann ..."
    play music "bgm/seriousintro.ogg" fadein 2.0
    queue music "bgm/seriousloop.ogg"

    scene cave
    with fade

    "Während Sayaka und Hikari sich bereits wieder auf ihren Beinen befinden und sich strecken, ziehe ich mich gerade in einen wesentlich größeren Raum."

    $ sayaface='smiling'
    $ sayapose='magical_1'
    $ hikaface='normal'
    $ hikapose='magical_1'
    show Sayaka at left
    show Hikari at right
    with dissolve

    s "Puh!{w} Das war mal eine Reise.{w} Wie geht es euch allen?"

    $ hikaface='angry'
    show Hikari

    h "Ich bin okay.{w} Es wäre besser gewesen, wenn nicht {i}jemand{/i} im Tunnel rumgealbert hätte."

    $ sayaface='joking'
    show Sayaka

    s "Heh-hehe ...{w} Ich wollte ...{w} einfach die Stimmung hoch halten?"

    $ sayaface='scared'
    show Sayaka
    with hpunch

    "{i}Biep{/i}.{w} Falsche antwort.{w} Hikari schlägt ihrer Partnerin auf den Kopf."

    h "Idiot."

    hide Hikari
    hide Sayaka
    with dissolve


    "Ich sehe mich in der Umgebung um."

    "Sieht aus, als hätten wir eine Art große Kammer gefunden."

    "Und fast augenblicklich werden meine Augen angezogen."

    "Direkt in der Mitte der Höhle.{w} In einem unnatürlichen Licht leuchtend.{w} Ein Kristall."

    p "Das ist ..."

    "Man muss mir gar nicht erst sagen, was das ist.{w} Ich weiß es bereits."

    "Das ist sie.{w} Die Ursache hinter all dem Wahnsinn.{w} Die vermeintliche ‚dunkle Königin‘."

    "Alleine schon durch den bloßen Blick auf den Kristall fängt mein Kopf an, sich zu drehen."

    "Ich hab das Gefühl, mir wird übel.{w} Mein Verstand ist aufgrund eines wütenden Schreis in Flammen aufgegangen.{w} {i}Ihr{/i} Schrei."

    "Ein Schrei voller Hass.{w} Anders kann man es nicht erklären."
    
    "Wir haben sie endlich erreicht."

    "Ich kann es ein für alle Mal zu Ende bringen.{w} Wenn das hier vorbei ist, kann ich wieder zu meinem sorgenfreien Leben zurück."

    "Sie ist das letzte Hindernis.{w} Ich kann ..."

    p "Ich kann es schaffen."

    "Ich rede vor mir hin und balle meine Fäuste zusammen, um mein Zittern unter Kontrolle zu halten."

    "Schon lustig, wie verrückt die letzten Tage waren.{w} Wer hätte gedacht, dass meine Kopfschmerzen zu all dem hier führen würden?{w} Zu all diesen merkwürdigen Träumen ..."

    "Ich hab mich noch nie zuvor einer Sache so sehr gewidmet wie dieser.{w} Ich hab auch noch nie mehr Anstrengungen unternommen, als minimal erforderlich waren."

    "Und jetzt riskiere ich hier mein Leben, um möglicherweise die ganze Welt zu retten. Und das, obwohl ich nicht einmal weiß, ob ich es überhaupt schaffen werde."

    "Ich weiß nicht, was in letzter Zeit in mich gefahren ist ...{w} Diese Mädchen haben einen echt schlechten Einfluss auf mich.{w} Dass ich so verrückte Dinge mach ..."

    "Ich atme unregelmäßig und kann mich gerade noch gegen dieses reine Böse behaupten."

    "Es ist alles in Ordnung.{w} Ich kann das.{w} Ich muss es mir nur einreden."

    "Ich kann das ...{w} Ich ... kann ... das ...?"

    "Scheiße.{w} Langsam zweifle ich an mir selbst."

    "{i}Wie{/i} kann ich das schaffen?!{w} Ich bin kein Magier.{w} Ich kann nicht zaubern!{w} Ich weiß ja nicht mal, ob ich mich an das, was mir die beiden beigebracht haben, noch erinnern kann ..."



    with hpunch

    "Auf einmal legt jemand seine Hand auf meine Schulter."

    $ sayaface='smiling'
    $ sayapose='magical_1'
    show Sayaka at center
    with dissolve

    s "Kenta?"

    "Es ist Sayaka.{w} Ihr Gesicht strotzt nur so von Optimismus."

    s "Mach dir keine Sorgen!{w} Wir können es schaffen.{w} Zusammen."

    with hpunch

    "Dann landet auch noch eine zweite Hand auf meiner Schulter ...{w} Jedoch weitaus verlegener als die erste."

    $ hikaface='shy'
    show Sayaka at left
    show Hikari at right
    with dissolve

    h "J-Ja.{w} Was sie gesagt hat."

    "Es ist natürlich Hikari.{w} Trotz ihres roten Gesichts erkenne ich dahinter, wenn auch versteckt, ihre grenzenlose Entschlossenheit."

    $ hikaface='normal'
    $ hikapose='magical_2'
    show Hikari
    with dissolve

    h "Du musst dich vor nichts fürchten, solange du an unserer Seite bist."

    p "Ja."

    "Ich nicke."

    p "Du hast recht.{w} Wir haben es schon so weit geschafft.{w} Nur noch ein bisschen, dann ist alles vorbei."

    p "Ich danke euch.{w} Für alles, was ihr für mich getan habt.{w} Ohne euch wär ich jetzt nicht hier.{w} Ich schulde euch was."

    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Hmmm, na ja, ich schätze, über eine Belohnung können wir reden, wenn das alles erstmal vorbei ist."

    h "Eine ... Belohnung ...?"

    "Bei dieser Aussicht wird Hikari plötzlich still.{w} Mit einem misstrauischen Blick."

    $ sayaface='happy'
    show Sayaka

    s "Meine Güte, Hikari, an welche Belohnung hast {i}du{/i} da gedacht?{w} Dein Gesicht leuchtet in allen möglichen Farben!"

    $ hikaface='embarrassed'
    $ hikapose='magical_2'
    show Hikari
    with dissolve

    h "Nichts!{w} Absolut nichts!{w} Kenta's Dank ist alles, was wir brauchen.{w} W-Wir machen doch nur unseren Job."

    $ sayaface='joking'
    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "Geschmeidig."

    "Mit einem hänselnden Blick stößt sie Hikari in die Seite.{w} Ich frag besser nicht nach dem Grund dahinter."

    $ sayaface='smiling'
    $ hikaface='normal'
    show Sayaka
    show Hikari
    stop music fadeout 6.0
    s "Dann fangen wir mal an!"

    p "Verstanden.{w} I-Ich ...{w} Ich glaub, ich hab mir alles gemerkt."

    s "Du wirst es schon schaffen.{w} Aber im Fall der Fälle werden wir dir schon helfen, okay?"

    "Da bin ich gleich ein bisschen erleichtert.{w} Aber ich muss trotzdem schauen, dass es gleich beim ersten Versuch klappt.{w} Ich darf den beiden nicht zur Last fallen.{w} Nicht jetzt."

    hide Sayaka
    hide Hikari
    with dissolve

    "Achtsam begeben wir uns in die Mitte der Höhle, wo mein schlimmster Alptraum lauert."

    "Die Höhle {i}scheint{/i} leer zu sein ...{w} Das wäre doch zu schön, um wahr zu sein.{w} Unmöglich, dass man es uns so einfach macht."

    "Schritt für Schritt kommen wir näher ran."

    "Sayaka und Hikari sind mit angezogenen Waffen an meiner Seite.{w} Wer weiß, was da alles auf uns lauert."

    "Wir sind schließlich direkt in ihr Versteck reinstolziert.{w} Ich bin überrascht, dass uns diese Schatten nicht schon längst angegriffen haben."

    y "Hah, du bist wirklich dümmer als ich dachte!"

    "Eine vertraute Stimme dringt in unsere Ohren.{w} Na klar.{w} {i}Wer{/i} denn sonst?"

    p "Yuzuki!"

    scene cg12
    play music "bgm/evilgirlintro.ogg" fadein 2.0
    queue music "bgm/evilgirlloop.ogg"

    "In einer Ansammlung von Federn, die so schwarz wie die Nacht sind, taucht sie neben dem Kristall auf."

    "In einer überaus feindlichen Stellung packt sie ihre Sense.{w} Es scheint, als würde selbst sie die Schwere dieser Situation begreifen."

    y "Sich so bereitwillig anzubieten, nachdem ich all die Nächte damit verbracht habe, dich zu jagen.{w} Du hast wirklich einen Todeswunsch."

    y "Aber das ist in Ordnung.{w} Ich gebe dir ein schnelles und schmerzloses Ende."

    h "Du redest nur groß daher!{w} Denk nicht, ich kann nicht sehen, dass du Angst hast.{w} Du weißt, dass das dein Ende ist."

    h "Ich weiß nicht, was du von alldem willst, aber was für verrückte Fantasien du auch hast, sie werden zu einem Ende kommen. {w} Jetzt!"

    "Während ihr Schweißperlen über das Gesicht laufen, knirscht sie mit den Zähnen.{w} Sie hat also wirklich Angst ...?"

    y "Halt den Mund!{w} Du weißt nichts.{w} Ich ...{w} Ich brauche das!"

    p "Yuzuki, es muss nicht so enden.{w} Ich weiß, du wirst mir nicht glauben, aber ich weiß, was du durchmachst.{w} Den Schmerz, den du fühlst.{w} Vielleicht können wir--"

    with hpunch

    y "Ich sagte sei ruhig!"

    "Die ganze Höhle fängt zu beben an.{w} Von oben regnen Steinbrocken herab.{w} Das wird echt gefährlich."

    y "Ich brauche deine Hilfe oder dein Mitgefühl nicht.{w} Ich repariere Dinge selbst.{w} Alles wird gut, wenn ich dich wie einen Feuerhydranten aufreiße und dein Blut magisch wirken lasse."

    "Mein Gesicht wird blass, als ein verrücktes Lachen über ihre Lippen wandert.{w} Wie kann sie bloß so was Krankes sagen?{w} ... Ich hab es wirklich versucht, aber vielleicht ist sie geistig wirklich nicht mehr zu retten?"

    "Ich darf nicht so schnell aufgeben!{w} Noch ein Versuch ...{w} Vielleicht erreich ich sie ja doch?"

    p "Ich weiß, dass du kein schlechter Mensch bist, Yuzuki.{w} Du bist nur ...{w} einsam, oder?"

    y "Ich bin nicht allein!{w} Zumindest ...{w} werde ich nie wieder einsam sein, wenn das hier einmal vorbei ist."

    s "Kenta ...{w} Ich kann verstehen, wenn du ihr helfen möchtest, aber ...{w} nun ja, sieh sie dir an."

    "Sayaka blickt auf den dunklen Engel."

    "...Sie hat recht.{w} Seitdem wir hier angekommen sind, schaue ich Yuzuki zum ersten Mal etwas genauer an."

    "Ihr Gesichtsausdruck ist verwirrt.{w} Gelegentlich zuckt sie mit dem Kopf, wenn sie ihre Sense fest packt."

    "Sie schaut noch schlechter aus als zuvor.{w} Vielleicht hat die Finsternis sie bereits völlig verschlungen?{w} Existiert die alte Yuzuki überhaupt noch?"

    "Ich muss es zugeben.{w} Wir können sie nicht mehr retten."

    "Ich seufze."

    p "Okay.{w} Tut, was ihr tun müsst."

    "Sayaka und Hikari nicken.{w} Sie verstehen, dass dieser Kampf Konsequenzen nach sich ziehen wird."

    "Es gibt kein Zurück mehr.{w} Es steht für jeden zu viel auf dem Spiel."

    y "Ich habe das Gefühl, dass du mich vielleicht unterschätzt.{w} Es ist wahr, ich musste bei unserer letzten Begegnung beschämend den Schwanz einziehen, aber ..."

    "Yuzuki grunzt und wird auf einmal von einer dunklen Aura umgeben.{w} Das seh ich zum ersten Mal ..."

    y "Wir kämpfen in meinem Revier.{w} Ich habe hier eine direkte Verbindung zu ihr.{w} Ich kann ...{w} Ich kann sie in mir fühlen."

    y "Ich kann jetzt nicht verlieren!{w} Nicht mit {i}ihr{/i} auf meiner Seite!"

    "Mit einem weiteren verrückten Lächeln löst sie wieder ein heftiges Beben aus.{w} Ich schätze, sie meinst es wirklich ernst ...{w} Sayaka und Hikari werden hier kein leichtes Spiel haben."

    stop music fadeout 2.0

    y "Nun denn ...{w} stirb!"

    scene cave

    $ yuzuface='angry'
    $ yuzupose='magical_1'
    show Yuzuki at center
    with dissolve

    play music "bgm/dramaticintro.ogg" fadein 2.0
    queue music "bgm/dramaticloop.ogg"

    "Yuzuki schließt mit erhobener Sense im Nu die Distanz zwischen uns.{w} Ich kann nicht sagen, ob sie es gezielt auf mich abgesehen hat, oder ob sie uns alle mit einem einzigen Schlag umbringen möchte."

    s "Wahh, pass auf!"

    hide Yuzuki
    with dissolve

    "Sayaka zerrt an meinem Arm und zieht mich weg, während Hikari auf die andere Seite springt."

    with hpunch

    "Der Boden, auf dem ich eben noch stand, ist zerschmettert – stattdessen ist nur noch ein Krater, umgeben von dunkler Magie, zu sehen."

    "Echt krass.{w} Hätte mich Sayaka nicht gerettet ...{w} Ich will gar nicht darüber nachdenken, was dann passiert wäre."

    show Yuzuki at right
    with moveinright

    "Yuzuki nimmt mich wieder ins Visier und hebt ihre Sense für einen weiteren Angriff in die Höhe.{w} Ich frage mich, ob ihre verrückten Augen überhaupt wissen, dass hier auch noch zwei andere Mädchen sind?"

    "Sie scheint es nur auf mich abgesehen zu haben.{w} Erwischt sie mich, hat sie gewonnen."

    $ hikaface='angry'
    $ hikapose='magical_1'
    show Hikari at left
    with moveinleft
    show Hikari at center
    show Yuzuki at center
    with MoveTransition(0.2)
    with hpunch
    show Hikari at left
    show Yuzuki at right
    with move

    "Sie versucht, vom Boden abzuheben, aber Hikari überrascht sie von der Seite und hält sie davon ab."

    h "Oh nein, das tust du nicht!{w} Bevor du ihn bekommst, musst du erst an {i}mir{/i} vorbei!"

    y "Das kann ...{w} vereinbart werden!"

    "Die beiden geraten aneinander, während die Magie um sie herum förmlich zu knistern beginnt."

    "Yuzuki muss im Moment stärker sein als je zuvor, aber Hikari scheint mit ihr mithalten zu können – abgesehen davon, dass sie aufgrund des Drucks immer weiter in den Boden einsinkt."

    "Sie muss weit über ihre Grenzen hinausgehen, um überhaupt eine Chance gegen dieses Monster zu haben.{w} Als ihr bereits Schweiß über das Gesicht läuft, erkenne ich, dass es echt anstrengend für sie sein muss."

    h "Hrghh...{w} L-Los!{w} Ich hab sie ...{w} abgehalten!{w} Ihr Typen ...{w} beendet das!"

    "Sie zischt zähneknirschend und rutscht mit den Beinen allmählich nach hinten."

    $ sayaface='shocked'
    hide Hikari
    hide Yuzuki
    show Sayaka at center
    with dissolve

    s "Hikari!{w} Du hast doch wohl nicht wirklich--"

    hide Sayaka
    show Hikari at right
    with dissolve

    h "Ich sagte los!"

    "Ihre Stimme dröhnt und die Magie um sie herum fängt heftig zu knistern an.{w} Ich hab sie noch nie zuvor so erlebt ..."

    h "Oder willst du, dass alles hier für nichts ist?!{w} Ich kann ...{w} sie für eine Weile in Schach halten.{w} Kein Problem!"

    "Das ist ..."

    "Ich sehe sie besorgt an, aber Sayaka zerrt mich am Arm und drängt mich zum Kristall."

    $ sayaface='normal'
    hide Hikari
    show Sayaka at center
    with dissolve

    s "Komm schon.{w} Sie hat recht.{w} Sie ist zäher, als sie aussieht, und ich bin mir sicher, sie schafft das!"

    "Selbst Sayaka scheint nicht komplett davon überzeugt zu sein.{w} ... Mir bleibt wohl nichts anderes übrig, als einfach an Hikari zu glauben."

    "Ich nicke und gemeinsam kommen wir dem Zentrum all dieses Chaos immer näher.{w} Hinter mir kann ich noch immer das Aufeinanderprallen von Magie, begleitet von schmerzhaften Schreien, hören.{w} Ich darf mich nicht umdrehen.{w} Sie wird es schon schaffen!"

    "Wir sind fast da.{w} Nur noch ein paar Schritte, und--"

    $ sayaface='scared'
    show Sayaka

    s "Oh, du willst mich doch verarschen ..."

    "Sayaka bereitet ihren Bogen vor und wirft einen scharfen Blick auf die Steine, die in der Ferne verstreut liegen."

    p "H-Häh?{w} Was meinst du damit?"

    scene cg20
    with dissolve

    "Dämonisches Knurren von einem fast hundeähnlichen Schatten erfüllt den Raum.{w} ... Und nicht nur einer, sondern mehrere."

    "Sie umzingeln uns und blockieren den Kristall.{w} Großartig."

    scene cave
    with dissolve

    s "Okay.{w} Das ist ...{w} überhaupt kein Problem!"

    "Wir werden mit den Rücken an die Wand gedrängt und werden mit den Schatten konfrontiert.{w} Ihre Reißzähne sind geschärft und in ihren Augen existiert nichts als Hass."

    "Ich hätte wissen müssen, dass es nicht so einfach wird.{w} {i}Logisch{/i}, dass sie sich nicht nur auf Yuzuki verlassen würde!"

    p "Irgendwelche, äh ...{w} Ideen?"

    s "Das wollte ich dich gerade fragen!"

    "...Ich glaub, wir {i}wissen{/i} beide, dass es aus ist, wenn wir uns auf meine Ideen verlassen."

    p "Ich hoff doch, dass das ein Scherz ist!"

    "Die Monster kommen näher.{w} In Anbetracht der Tatsache, dass es für ihre Beute kein Entkommen gibt, verhalten sie sich wie ein intelligentes Rudel."

    s "Oh!{w} Ich hab‘s!{w} Warum hab ich nicht schon früher daran gedacht?"

    "In Sayakas Augen leuchtet plötzlich ein Licht auf, als sich kurz darauf ihr Bogen auflöst und sich etwas auf ihrem Rücken bildet."

    "Ah, die Flügel!{w} Natürlich.{w} Wir können einfach davonfliegen."

    "So sehr ich fliegen auch hasse, dieses Mal bin ich bereit, eine Ausnahme zu machen."

    s "Gut festhalten, Kenta!"

    with hpunch

    "Ich greife nach Sayakas Händen und sie hebt vom Boden ab – genau in dem Moment, in dem die Monster losspringen."

    "Das war knapp.{w} Als wir hochsteigen, kann ich sogar noch die Hitze von einem dieser ‚Hunde‘ spüren."

    s "Das war doch ein Kinderspiel!{w} Nächster Halt, die dunkle Königin!"

    "Mit dem Ziel vor Augen segeln wir durch die Lüfte.{w} Okay, dieses Mal könnten wir es tatsächlich schaffen--"

    with hpunch

    s "Ahh!"

    "Plötzlich schreit Sayaka schmerzhaft auf.{w} Ihr Griff wird immer schwächer und sie kommt zum Halt."

    p "S-Sayaka?"

    s "Ahh, nicht gut.{w} Einer von ihnen hat mich, bevor wir entkommen konnten, wohl noch an der Seite erwischt."

    "Als unser Flug ruckeliger wird, zwingt sie sich zu einem unangenehmen Lächeln."

    s "Ich weiß nicht, wie lange ich ...{w} das noch schaffe ..."

    "Ich werfe einen Blick nach unten … und sehe dort Dinge, die mir überhaupt nicht gefallen.{w} Es sieht echt düster aus ..."

    s "Hmmm ..."

    "Während wir immer tiefer sinken, denkt Sayaka über etwas nach.{w} Nein!{w} Wir waren so nah dran!"

    s "Nun.{w} Ich vertraue darauf, dass du alles in Ordnung bringst.{w} Ich werde nicht da sein, um dir zu helfen, wie ich es vorhatte ...{w} aber ich glaub an dich!"

    "Ihre Stimme klingt voller Schmerz.{w} Schwach.{w} Diese kleine Wunde muss stärker wehtun, als sie zugibt."

    p "Sayaka ...?{w} Was sagst du da ...?"

    s "Du kannst das.{w} Das weiß ich ganz genau!"

    p "Was--"

    with hpunch
    stop music fadeout 4.0

    "Hinter meinem Rücken explodiert ein Energieschub, der sich anfühlt wie eine Windböe.{w} Dieser Energieschub trennt mich von Sayaka und befördert mich geradewegs zum Kristall."

    "Sayaka muss gewusst haben, dass sie mich nicht bis dort hin tragen kann, weshalb sie mich ...{w} mit Magie hingeschossen hat?{w} Aber was wird jetzt aus ihr?"

    with hpunch

    p "Oof!"
    play music "bgm/seriousintro.ogg" fadein 5.0
    queue music "bgm/seriousloop.ogg"
    "Ich lande sanft am Fuße des Kristalls.{w} Sieht aus, als hätte ihre Magie sogar meinen Aufprall gedämpft.{w} Sayaka ..."

    "Ich werfe einen Blick über meine Schulter.{w} Sie ist nicht mehr in der Luft.{w} Und direkt darunter, wo wir vorhin waren ..."

    "Nein!{w} Ich möchte es nicht glauben.{w} Es geht ihr bestimmt gut.{w} Ich muss es nur zu Ende bringen.{w} Sofort!"

    "Ich drehe mich wieder um, um voller Entschlossenheit dem Kristall gegenüberzustehen."

    "Sie riskieren beide ihr Leben, nur für mich.{w} Ich kann sie jetzt nicht hängenlassen."

    "Ich starre auf den Kristall und versuche die Kopfschmerzen so gut wie nur möglich zu ignorieren.{w} Sie sind so stark wie noch nie.{w} Aber ich darf mich nicht unterkriegen lassen.{w} Das?{w} Das ist doch gar nichts!"

    "Im Kristall kann ich gerade noch eine menschenähnliche Form erkennen."

    "Du.{w} Das ist alles deine Schuld.{w} Wegen dir ...{w} Du{w} hast Sayaka und Hikari weh getan.{w} Das werde ich dir nicht verzeihen."

    "Ich ziehe meinen rechten Ärmel zurück.{w} Auf meinem Handrücken befindet sich ein angeblich mystisches Symbol.{w} Etwas, das Sayaka und Hikari letzte Nacht noch aufgezeichnet hatten."

    "Sie sagten, dass mir dieses Symbol dabei helfen würde, all die Kräfte zu erwecken, die in mir schlummern."

    "Ich spanne meine Hand an und das Symbol beginnt zu leuchten.{w} Okay.{w} So weit, so gut."

    "Jetzt muss ich nur noch ..."

    "Ich beruhige mich ein wenig.{w} Ich bin mir nicht sicher, was mit mir passieren wird, wenn ich das tue, aber ich muss auf alles vorbereitet sein."

    "Ich kann aber nicht für immer warten.{w} Nicht in dieser Situation."

    "Sayaka.{w} Hikari.{w} Ich schaff das!"

    "Ich schlage meine Hand nach vorne und treffe auf den Kristall."

    with hpunch

    "Als unmittelbare Reaktion darauf läuft ein elektrischer Strom durch mich hindurch.{w} Aber das ist okay.{w} Das war zu erwarten.{w} Kein Problem."

    "Es tut weh, aber ich bin Schlimmeres gewohnt.{w} Ist das alles, was du drauf hast?!"

    "Ich dringe mit meiner Hand tiefer in die Oberfläche des Kristalls vor.{w} Der Schmerz wird immer stärker und ein erschrockener Schrei überfällt meine Ohren."

    "Dieser Schrei kommt aber nicht von den Mädchen.{w} Er kommt von {i}ihr{/i}.{w} Sie weiß, was gleich passieren wird."

    "Nun, sie kann schreien, so viel sie will, aber das wird auch nichts mehr daran ändern!"

    scene bg black
    with fade

    "Inmitten dieses ganzen Chaos muss ich erstmal meinen Geist befreien.{w} All die Geräusche herausfiltern.{w} Beim aktuellen Stand der Dinge eine fast unmögliche Aufgabe, aber ich muss es versuchen."

    "Laut dem, was mir gesagt wurde, wird Magie hauptsächlich durch Gedanken kontrolliert.{w} Zaubersprüche müssen im Gedanken erschaffen werden."

    "Anscheinend sind es diejenigen, die eine lebhafte Phantasie haben, die sich auch in diesen Dingen auszeichnen."

    "Ich hatte noch nie wirklich viel Phantasie, aber es gibt immer ein erstes Mal."

    "Ich muss mir ein Gefängnis vorstellen.{w} Ein abgeschlossener Raum.{w} Etwas Unzerbrechliches, das von der Außenwelt abgeschottet ist."

    "Etwas, das so sicher ist, dass so etwas nie wieder vorkommen wird."

    "Und dann verbinde ich dieses Gefängnis, so wie es mein Vorfahre vor mir getan hat, mit meiner eigenen Seele.{w} Ich muss mich daran binden und der einzige Schlüssel bleiben, der in der Lage ist, dieses Gefängnis zu öffnen."

    "..."

    "Ich weiß nicht, ob es funktioniert, aber der Schmerz wird immer stärker.{w} Ich fühle mich schwach.{w} Ich könnte jeden Moment zusammenbrechen.{w} Aber ich muss standhaft bleiben!"

    "Ich beiße die Zähne zusammen."

    "Warum funktioniert das nicht?!"

    "Mache ich irgendwas falsch?"

    "Ich war mir so sicher, dass der Zauberspruch perfekt war."

    "Mit rasch schwindenden Kräften wiederhole ich die ganze Prozedur noch einmal."

    "Es bringt nichts.{w} Das ist völlig zwecklos."

    "Egal, wie sehr ich mich auch anstrenge, es scheint sich nichts zu ändern.{w} Vielleicht mangelt es mir wirklich an magischer Fähigkeit, so wie ich befürchtet hatte?"

    p "Argh!{w} Scheiße!"

    "In einem Wutanfall balle ich meine freie Hand zur Faust zusammen und schlage damit gegen den Kristall."

    "...Als Reaktion darauf gibt dieser einen letzten elektrischen Schlag von sich, ehe der Schmerz nachlässt.{w} Und auch das Geschrei."

    "Die Wiederversiegelung ... wurde abgeschlossen."

    scene cave
    with dissolve

    "...Du willst mich wohl verarschen.{w} Ich musste die ganze Zeit nur dagegenschlagen?!"

    "I... Ich kann’s nicht fa..."

    "Warte.{w} Jetzt erinnere ich mich.{w} An das, was mir in dieser Nacht beigebracht wurde."

    "Während der Großteil der Magie mit der Haupthand ausgeführt wird, wird in einigen Fällen, so auch bei einer Versiegelung, auch die Nebenhand benötigt, um den Prozess zu beenden."

    "Wie konnte ich das – gerade in dem Moment – nur vergessen?!"

    "Ich bin ...{w} Ich bin so ein Idiot.{w} Das ist so lächerlich, dass ich selbst darüber lachen muss."

    "Wirklich ..."

    p "Hah ...{w} Ahahahaha ..."

    "Geistig vielleicht völlig zerstört von dem, was ich in den letzten Tagen durchmachen musste, falle ich kraftlos nach hinten."

    scene bg black
    with fade

    "Und als die Dunkelheit die Oberhand gewinnt, falle ich ihn Ohnmacht - jedoch zumindest mit dem Gewissen darüber, was ich getan habe.{w} Ich hab wirklich ... gewonnen."

    with Pause(4.0)

    "..."

    "Ich falle wieder in einen Traum.{w} Und in diesem Traum ist nichts.{w} Sie ist fort.{w} Für immer, hoffe ich."

    "Vielleicht habe ich ab sofort normalere Träume.{w} Und vielleicht beginnt jetzt auch ein normaler Schulalltag für mich."

    "Ich durchstreife die unendliche Leere, ohne mich vor etwas zu fürchten.{w} Friede.{w} Endlich."

    scene bg white
    with wake

    "Ich komme langsam zu mir."

    "Und befinde mich auf einer kalten und rauen Oberfläche."

    "Um mich herum liegen überall Steine."

    "Wo bin ich?{w} Ich kann mich an nichts ..."



    if sayaka > hikari:


        cg "Schon ein bisschen spät, um einzuschlafen, findest du nicht?"

        "Eine fröhliche Stimme bringt mich wieder zur Besinnung."

        "Es ist niemand anders als ..."

        scene cg13_2
        with wake
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"

        p "S-Sayaka ...?"

        "Ich murmle ihren Namen vor mich hin, weil es einfach zu schön ist, um wahr zu sein."

        s "Jup.{w} Ich bin's!"

        "Sie lächelt mich mit dem süßesten Lächeln an, das ich je gesehen hab."

        "Obwohl alles ziemlich aussichtlos aussah ...{w} hätte ich nie an ihr zweifeln dürfen."

        "Ich bin so froh, dass es ihr gut geht, und halte gerade noch so meine Tränen zurück."

        p "Sayaka, ich ..."

        p "Hab ich ...?"

        s "...Die dunkle Königin versiegelt?{w} Darauf kannst du einen lassen.{w} Du hast echt gute Arbeit geleistet!"

        "Sie strahlt, als sie meine Hand nimmt und mich sanft in eine sitzende Position stützt."

        s "Einen Moment lang habe ich mir echt Sorgen gemacht.{w} Für kurze Zeit dachte ich, der Zauber wäre vielleicht zu viel für dich gewesen ..."

        p "W-Warte, du hast dir um {i}mich{/i} Sorgen gemacht?!{w} Ich dachte, diese Monster wären--"

        s "Die?{w} Pff.{w} Das war doch gar nichts!{w} Die hab ich eiskalt ausgelöscht … Du hast es nur verpasst."

        p "Ich konnte dich nicht mal sehen!"

        s "Ich hab mich ...{w} totgestellt ...?"

        p "Sayaka ..."

        s "He-hehehe-hehe ..."

        "Sie kratzt sich am Hinterkopf und grinst mich dabei an.{w} Dieses Mädel ..."

        p "Ich hab mir wirklich Sorgen um dich gemacht ..."

        p "Wenn dir was passiert wäre ...{w} Ich weiß echt nicht, was ich dann getan hätte ..."

        s "Aww, ich wusste gar nicht, dass du so rührselig werden kannst, Kenta."

        s "Brauche ich für all die Tränen etwa einen Regenschirm?"

        "Es scheint, als würde meine Worte keine Wirkung zeigen, also ..."

        scene cave
        $ sayaface='shy'
        $ sayapose='magical_1'
        show Sayaka
        with dissolve
        with hpunch

        s "H-Hä?{w} Kenta?!"

        "Ich ziehe sie in eine enge Umarmung.{w} Es reicht mir nicht, sie nur wiederzusehen ... Ich wollte sicherstellen, dass sie auch wirklich hier ist."

        p "Ich bin froh, dass es dir gut geht."

        s "Ich, äh ..."

        "Sie scheint sprachlos zu sein und lässt ihre Arme einfach hängen.{w} Das macht die ganze Situation irgendwie unangenehm."

        $ sayaface='happy'
        show Sayaka

        s "Aw, was zum Teufel!{w} Komm schon, du alter Softie."

        "Sie hebt ihre Arme und erwidert meine Umarmung.{w} Vielleicht sogar ein bisschen {i}zu{/i} stark."

        $ sayaface='joking'
        show Sayaka

        s "Hoffen wir, dass Hikari davon nichts erfährt, hm?{w} Sonst zuckt sie noch aus."

        "Sie unterdrückt sich ein Kichern, während sie sich in meine Schultern schmiegt."

        "Wait...{w} That's a point."

        "Ich löse mich aus der Umarmung."

        p "Hikari!{w} Geht es ihr gut?"

        $ sayaface='smiling'
        show Sayaka

        "Sayaka neigt den Kopf für einen Moment verwirrt zur Seite."

        s "Hm?{w} Der geht’s gut!"

        p "Und ...{w} Yuzuki ...?"

        "Sie treibt sich zu einem kleinen Lächeln, welches mir etwas Hoffnung gibt."

        $ sayapose='magical_2'
        show Sayaka
        with dissolve

        s "Folge mir!"



        "Ich gehorche und folge ihr."

        $ sayaface='happy'
        show Sayaka

        s "Tada!{w} Siehst du?{w} Eine Hikari und eine Yuzuki."

        "Hikari schiebt mit gezogenem Schwert, dessen Ende auf eine zerfledderte Yuzuki zeigt, Wache."

        "Abgesehen von der Bewusstlosigkeit schon sie nicht viel abbekommen zu haben.{w} Sie atmet normal und mit Ausnahme von der Kleidung kann ich auch keine Verletzungen entdecken."

        $ hikaface='angry'
        $ hikapose='magical_2'
        show Sayaka at left
        show Hikari at right
        with dissolve

        h "Da seid ihr zwei!{w} Was um alles in der Welt habt ihr so lange gemacht?!"

        "Jup.{w} Der geht's gut.{w} Sie ist auch so lebendig wie eh und je."

        $ sayaface='joking'
        $ sayapose='magical_1'
        show Sayaka
        with dissolve

        s "Na ja.{w} Wir haben ...{w} Heh-hehehe-heh."
        stop music fadeout 5.0
        "Sayaka kennt überhaupt keine Zurückhaltung und plaudert alles aus."

        "Hikari reagiert mit einem Stirnrunzeln und in ihrem Gesicht erkennt man auch geringe Anzeichen von Wut.{w} Ich schätze, sie weiß, worum es geht ..."

        h "...Ugh, vergesst es.{w} Ihr seid ja wie Tiere."

        $ sayaface='normal'
        $ hikaface='normal'
        show Sayaka
        show Hikari

        "Yuzuki erwacht aus ihrem Schlummer und erregt dadurch vor allem die Aufmerksamkeit von Hikari und Sayaka, die die ganze Zeit über auf das Schlimmste vorbereitet waren."



    if hikari > sayaka:


        tg "Während der Arbeit schlafen?{w} Was eine Überraschung.{w} Was werden wir jetzt mit dir machen?"

        "Ich höre eine vertraute Stimme.{w} Eine strenge, aber dennoch ...{w} auch mit jeder Menge Zuneigung.{w} Ungewöhnlich viel Zuneigung, um ehrlich zu sein."

        "Ich habe schon einen Verdacht, wer es sein könnte ...{w} aber ist das wirklich möglich ...?"

        scene cg13_3
        with wake
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"    
        p "Hikari ...?"

        "Sie ist es wirklich.{w} Es geht ihr gut!{w} Gott sei Dank ..."

        h "Niemand anders.{w} Du hast dir auf dem Weg nach unten nicht den Kopf gestoßen, oder...?"

        "Okay, ja, es ist Hikari."

        "Trotz ihrer üblichen Schimpfwörter zeigt sie gerade einen weichen Kern.{w} Oder bilde ich mir das bloß ein?"

        "Und vielleicht bilde ich mir auch das Lächeln, dass sie mir bot, als sie mir aufhelfen wollte, nur ein."

        p "Hab ich ...{w} Ich mein ...{w} Ist es vorbei?"

        "Sie hilft mir dabei, eine aufrechte Sitzposition einzunehmen."

        h "Ja.{w} Die dunkle Königin ist wieder versiegelt, dank dir."

        h "Ich hatte meine Zweifel, dass die Dinge wirklich gut enden würden, mit dem Monster Yuzuki, das den Job beenden würde... "

        h "Aber, es sieht so aus, als ob {i}du{/i} Helden-Material wärst."

        p "Es freut mich, dass es euch gut geht ...{w} und es tut mir leid, dass ihr euch wegen mir einer solchen Gefahr aussetzen musstet."

        h "Nein, entschuldige dich doch nicht!{w} Du hast nichts falsch gemacht.{w} Ich würde mein Leben immer für dich reskieren, Kenta."

        "..."

        "Ah, sie hat es schon wieder getan.{w} Sie sagte etwas sehr Peinliches, ohne es zu bemerken."

        "Ich bin mir sicher, dass sie ihren Fehler jeden Augenblick erkennt und kurz darauf knallrot im Gesicht wird."

        "Oder ...{w} doch nicht?"

        "Okay ...{w} Vielleicht hat sie's noch nicht gemerkt?{w} Ich bin sicher, dass ich sie noch zu einer Reaktion bewegen kann.{w} Ich muss nur etwas sagen, wie zum Beispiel ..."

        p "Du musst dir ja wirklich große Sorgen um mich machen, hm?"

        "Sie nimmt sich einen Moment Zeit, um über das, was ich gerade gesagt habe, nachzudenken ..."

        h "...{w}Ja.{w} T-Tu ich."

        "Ihr Lächeln bleibt, aber ihre Wangen werden heiß."

        "Was soll das?!{w} Jetzt werd ich ja noch ganz wuschig!"

        p "W-Was zur Hölle sagst du da?!{w} Du ...{w} Du Idiot!"

        "Ich bin nicht sicher, ob sie erkennt, dass ich mich über sie lustig mache oder ob ich es doch ernst meine.{w} Kein Wunder, wenn man bedenkt, dass ich es selbst nicht weiß."

        h "Muss ich...{w}es wirklich aussprechen?"

        "Sie kommt gerade echt nahe.{w} {i}Viel{/i} zu nahe."

        p "H-Hey, was--"

        scene cave
        $ hikaface='shy'
        $ hikapose='magical_1'
        show Hikari
        with dissolve

        "Sie reißt mich hoch und legt beide Arme um mich.{w} Oh.{w} {i}Ohhh.{/i}"

        "Sie sagt kein Wort und hält mich einfach fest.{w} Ich bin ziemlich sicher, dass die Hitze, die ich gerade spüre, von ihrem Gesicht ausstrahlt."

        "Ich hab fast Angst davor, diese Umarmung zu erwidern, da ich damit alles ruinieren könnte.{w} Sie ist schließlich unberechenbar genug."

        "Eine Zeit lang stehen wir täppisch zusammen.{w} Sollte dieser Moment eigentlich nicht herzig sein?{w} Aktuell bin ich mir nämlich nicht mehr so sicher."

        "Trotzdem bin ich froh, dass es ihr gut geht.{w} Es sah schließlich nicht gut für sie und Sayaka aus."

        p "Sayaka!"



        $ hikaface='shocked'
        show Hikari

        h "H-Huh?{w} Was?!"

        "Als Reaktion auf meine Worte stolpert sie sprachlos zurück.{w} Das war wohl kein günstiger Augenblick, was?"

        p "Äh, entschuldige ...{w} Ich mein ... Geht es Sayaka gut?"

        $ hikaface='angry'
        show Hikari
        $ hikaface='normal'
        $ hikapose='magical_2'
        show Hikari
        with dissolve

        "Sie schaut mich sauer an."

        h "Sie ist völlig in Ordnung."

        p "Oh, Gott sei Dank ..."

        h "Sie ist beim {i}anderen{/i} Unruhestifter."

        "Sie dreht ihren Kopf spöttisch in eine Richtung.{w} Erstaunlich, wie schnell sie von 'herzerwärmend' zu 'verärgert' umschalten kann."

        "Der andere Unruhestifter ...?{w} Ah!{w} Sie meint wohl ..."

        p "Yuzuki?!{w} Geht es ihr auch gut?!"

        $ hikaface='angry'
        show Hikari

        h "Sie hat wirklich Glück, dass sie okay ist.{w} Und nach alldem was sie uns angetan hat, weiß ich nicht, ob sie das {i}verdient{/i} hat."

        "Sie geht los."

        $ hikaface='normal'
        show Hikari

        h "Komm, ich werde es dir zeigen.{w} ...Idiot."

        "Ich folge ihr, wenn auch ziemlich langsam."

        p "H-Hey, beruhig dich!"

        h "Siehst du, sie sind okay.{w} ...und anscheinend sind sie dir wichtiger als ich."

        $ hikapose='magical_1'
        show Hikari
        with dissolve

        "Sie zeigt mit ihrem Finger auf Sayaka, die neben einer bewusstlosen Yuzuki Wache schiebt."

        $ sayaface='happy'
        $ sayapose='magical_2'
        show Sayaka at left
        show Hikari at right
        with dissolve

        s "Ah, da sind sie!"

        "Sayaka ist gesund und munter und sie lächelt auch.{w} Es beruhigt mich wirklich, als sie uns begrüßt."

        "Yuzuki hingegen sieht ein bisschen lädierter aus.{w} Aber wichtig ist doch erstmal nur, dass sie am Leben ist."

        $ sayaface='joking'
        show Sayaka

        s "Wisst ihr, ihr hättet euch ruhig Zeit lassen können.{w} Ich kann es verstehen, wenn ihr Zeit für euch alleine haben wollt."

        $ sayaface='smiling'
        $ hikaface='shy'
        $ hikapose='magical_2'
        show Sayaka
        show Hikari
        with dissolve

        h "D-Das hätten wir getan, wenn Herr Blödmann hier nicht darauf bestanden hätte, direkt zu dir zu marschieren."

        "Ähh ...?{w} Jetzt bin ich aber sprachlos.{w} Sie denkt überhaupt nicht an mich, als sie diese Worte in den Mund nimmt.{w} Ist das wirklich Hikari?"

        "Warte, 'Blödmann'?!{w} Wer ist hier der Blödmann?!"

        $ sayapose='magical_1'
        $ sayaface='happy'
        show Sayaka
        with dissolve

        s "Oh, du hättest sie sehen sollen, Kenta.{w} Sie hatte es nach der Versiegelung echt eilig, dich zu sehen.{w} Ich hab noch nie so was Bezauberndes gesehen!"

        $ hikaface='embarrassed'
        show Hikari

        s "'Kyahh!{w} Geht es Kenta gut?!{w} Ich kümmer mich um ihn, du pass auf Yuzuki auf!'"

        "Sie streckt ihre Brust heraus und miemt Hikari. Wenngleich diese Nachahmung ziemlich dürftig ausfällt."

        p "V-Verstehe."

        $ sayaface='smiling'
        show Sayaka

        s "Hmm?{w} Mehr hast du in einem so innigen Moment nicht zu sagen?"

        "Ich hätte nie gedacht, dass sich Hikari so sehr um mich sorgt.{w} Ich dachte immer, sie sei generell bloß schüchtern!"

        "Sie war schließlich immer für mich da.{w} Und hat ihr Leben aufs Spiel gesetzt.{w} Und heute bemerke ich ...{w} dass da vielleicht auch noch etwas mehr ist."

        "Aber ich hab in letzter Zeit so viel durchgemacht, dass ich das erstmal alles verarbeiten muss."

        p "Ähhh ..."

        $ hikaface='normal'
        $ hikapose='magical_1'
        show Hikari
        with dissolve

        s "Hmm.{w} Na ja, viel Glück beim nächsten Mal, Hikari.{w} Sieht aus, als hätte er sich schon in mich verguckt, und das kann nichts und niemand mehr ändern!"

        $ sayaface='joking'
        show Sayaka

        "Sie verpasst Hikari einen leichten Stupser.{w} Wilde Tiere verärgert man nicht, Sayaka!"

        s "Hmm, hmm, hmmm?"

        "Sie stupst sie weiterhin an.{w} Ich mache mir langsam Sorgen um ihr Wohlergehen."
        stop music fadeout 4.0
        $ hikaface='angry'
        show Hikari

        "Hikari öffnet ihren Mund.{w} Ich sehe das Feuer in ihren Augen.{w} Gleich wird hier etwas Schlimmes passieren!"

        h "Okay, das reicht!{w} Sayaka, jetzt bist du--"

        $ hikaface='normal'
        $ sayaface='normal'
        show Hikari
        show Sayaka

        h "Huh?"

        "Plötzlich bewegt sich Yuzuki wieder, was die beiden Mädchen wieder in einen ernsten Modus versetzt.{w} Ich danke dir!"



    if sayaka == hikari:


        cg "Da ist er, gesund und munter!{w} Unser Held."

        tg "Ist...{w}ist er wirklich okay?{w} Nach so einem Zauberspruch, besteht die Chance dass es--"

        with hpunch

        cg "Jup!{w} Schau!{w} Er atmet noch."

        "Irgendwas stößt mir ins Gesicht.{w} Etwas Warmes und Zärtliches."

        with hpunch

        "...Und es hört einfach nicht auf."

        tg "Was machst du da?!{w} Du kannst ihn doch nicht einfach so anstupsen!"

        cg "Hmm?{w} Ist da jemand eifersüchtig?{w} Eifersüchtig darauf, dass ich ganz intim mit ihm werd?"

        tg "B-Bitte!{w} In welcher Welt war dass 'intim'?{w} Du bist ärgerlicher, als alles anderes.{w} Gib ihm ein bisschen Raum!"

        cg "Okay, okay!"

        cg "...Ein Stupser noch!"

        "{i}Quetsch{/i}.{w} Meine linke Wange wird extrem stark nach oben gedrückt.{w} Okay, das ist komisch.{w} Ich sollte besser aufwachen."

        p "Nghh."

        tg "A-Ah!{w} Er wacht auf!{w} Sayaka, geh weg!"

        cg "Wahh, okay, okay!{w} Du musst mich doch nicht gleich so anbrüllen."

        scene cg13_1
        with wake
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"    
        "Ich wache auf und sehe zwei vertraute Gesichter.{w} Meine Schutzengel, Sayaka und Hikari."

        "Es geht beiden ziemlich gut.{w} Auf beiden ist kein einziger Kratzer zu sehen.{w} Ich ...{w} Ich bin so froh."

        p "M-Mädels ...?"

        "Ich muss sie einfach beide beim Namen nennen, um sicherzustellen, dass ich nicht träume."

        s "Guten Morgen!{w} Wie geht es dir?"

        h "Gott sei Dank geht es dir gut...{w} Du solltest uns keine Sorgen machen, Kenta!"

        "Beide bieten sie mir voller Erleichterung ihre Hand an."

        s "Kannst du stehen?"

        "...Ich gebe mein Bestes, aber meine Gliedmaßen versagen klanglos.{w} Hoppla.{w} Die Wiederversiegelung hat mich anscheinend doch mehr Kraft gekostet."

        "Sayaka kichert als Reaktion auf meinen gescheiterten Versuch. Hikari hingegen wirft mir einen Blick voller Besorgnis zu."

        s "Ich betrachte das mal als 'nein'.{w} Komm, hoch mit dir!"

        h "Du solltest dich danach nicht drängen. {w} Wenn du unsere Hilfe brauchst... {w} Alles, was du tun musst, ist es zu sagen, und ich werde glücklich sein..."

        "Sie murmelt etwas vor sich hin - so leise, dass sie es wahrscheinlich selbst nicht mal hören konnte."

        "Sayaka und Hikari helfen mir, eine sitzende Position einzunehmen."

        "Während ich mich hinsetze, wird auch mein Verstand allmählich klarer."

        s "Und auf.{w} Alles in Ordnung?"

        h "Ja, wenn es etwas gibt, was du brauchst, halte dich nicht zurück zu fragen!"

        "Sayaka kniet mit glitzernden Augen an meiner Seite.{w} Hikari ebenso, nur halt auf der anderen Seite.{w} Das wird jetzt ein bisschen merkwürdig.{w} Was soll das werden?"

        p "Es geht mir, äh, entsprechend.{w} Macht euch keine Sorgen.{w} Ich bin nur ein bisschen schwach auf den Beinen."

        p "Ich ...{w} Ich hab mir ehrlich gesagt mehr Sorgen um euch gemacht.{w} Ich hatte echt Angst um euch!"

        s "Psh, um uns?{w} Wir sind zäher, als wir aussehen.{w} Und wir haben schon Schlimmeres durchgestanden.{w} Uns geht's gut!"

        h "Ganz genau.{w} Wir wurden dafür trainiert.{w} Es hätte vielleicht schlecht ausgesehen, aber ich versichere dir, alles war ... {w}unter Kontrolle!!"

        "Sie versuchen ihr Bestes, um mir zu versichern, dass das alles kein Problem war, aber ich bin da völlig anderer Meinung ..."

        "Plötzlich lehnt sich Sayaka mit einem alarmierenden Lächeln nach vorn."

        s "Wenn du sagst, du hast dir Sorgen um uns gemacht ...{w} Hast du dir da um irgendjemand bestimmten {i}mehr{/i} Sorgen gemacht?"

        p "Ähh ...?{w} K-Kann ich nicht ..."

        h "S-Sayaka!{w} Was hast du hier versucht?!"

        s "Ahhh, nichts."

        s "Sein Zögern, auch nur irgendwas zu sagen, bedeutet eindeutig, dass er keinen von uns verletzten will.{w} Oder besser gesagt, vor allem {i}dich{/i} nicht verletzen will."

        h "W-Was?{w} Was macht dich so sicher, dass er mehr über dich besorgt war, als über mich?!"

        p "Ey, jetzt kommt schon ..."

        "Mich würde echt gern interessieren, wie es dazu kommen konnte.{w} Warum müssen sie ausgerechnet in einem solchen Augenblick ihre Konkurrenzfähigkeit raushängen lassen ..."

        scene cave
        $ sayaface='smiling'
        $ sayapose='magical_1'
        $ hikaface='normal'
        $ hikapose='magical_1'
        show Sayaka at left
        show Hikari at right
        with dissolve

        p "Kann das nicht erstmal warten?{w} Wie wär's, wenn wir erstmal nach Hause gehen und--"

        "Als ich versuchte, aufzustehen, schrie ich vor Schmerzen laut auf.{w} Jup.{w} Es geht noch nicht."

        $ sayaface='happy'
        $ sayapose='magical_2'
        show Sayaka
        with dissolve

        s "Oh, warte, ich helf dir!"

        "Sayaka hängt ihren Arm und meinen und hilft mir auf."

        $ hikaface='shy'
        show Hikari
        
        h "I-Ich kann auch helfen!"

        "Und natürlich nimmt Hikari meinen anderen Arm - allerdings nicht so sorgsam wie Sayaka."

        "Irgendwie schaffen es die beiden jedoch, mir aufzuhelfen, ohne mich dabei in zwei Teile zu reißen."

        $ sayaface='smiling'
        $ sayapose='magical_1'
        show Sayaka
        with dissolve

        s "Bevor wir gehen, solltest du noch jemanden aufsuchen."

        $ hikaface='normal'
        show Hikari

        h "Ugh.{w} Ist es wirklich so wichtig?{w} Ich habe ihr Leben verschont.{w} Können wir sie nicht einfach zurücklassen?"

        "Sayaka und Hikari wollen beide in unterschiedliche Richtungen gehen, was darin resultiert, dass wir wie eine nicht funktionstüchtige Einheit vor uns hin stolpern."

        "Warte, meinen sie vielleicht ..."

        p "Yuzuki?!{w} Du meinst, es geht ihr gut?"

        s "Jup!{w} Hier lang!"

        stop music fadeout 5.0

        "Auf einmal übernimmt Sayaka das Kommando und Hikari folgt ihr - wenn auch nur ungern."

        $ sayaface='joking'
        show Sayaka

        s "Schau!{w} Ihr geht's gut.{w} Und ...{w} wir hätten sie besser nicht alleine lassen sollen.{w} Aber wir konnten uns einfach nicht einigen, wer dir helfen soll!"

        "An einen nahegelegenen Felsen angelehnt finde ich die bewusstlose Yuzuki.{w} Abergesehen von ihrer Kleidung, die zerfetzt ist, und ein paar Kratzern, scheint sie nichts abbekommen zu haben."

        $ sayaface='smiling'
        show Sayaka

        "Ich frage mich, wie lange sie hier schon bewusstlos rumliegt.{w} Kurz darauf rührt sie sich auf einmal."

        $ sayaface='normal'
        show Sayaka

        "Hikari und Sayaka nehmen vor mir eine Verteidigungsposition ein. Ich hingegen kann mich gerade noch so auf meinen wackeligen Beinen halten."


    scene cg17
    with dissolve

    play music "bgm/sadintro.ogg" fadein 2.0
    queue music "bgm/sadloop.ogg"

    y "Nghh..."

    "Sie schreckt zurück und schaut uns an."

    "Langsam bemerkt sie, was passiert ist."

    y "Es ist...{w}Es ist vorbei, oder?{w} Ich...{w}hab verloren."

    s "Befürchte ich, ja."

    y "Sie ist...{w}Sie ist jetzt komplett weg.{w} Meine Königin...{w} Ich kann sie überhaupt nicht fühlen."

    "Sie scheint jetzt viel verhaltener zu sein.{w} Die Verrücktheit ist weg und stattdessen sehe ich nur ein trauriges Mädchen, das fehlgeleitet wurde, vor mir."

    y "Aber ich war so nah!{w} Ich...{w}Ich konnte es haben...{w} Argh, verdammt!"

    "Sie schlägt mit ihrer Faust schwach gegen den Boden.{w} Sie hat überhaupt keine Kraft mehr."

    y "Na, und?{w} Sind Sie hier, um sich zu freuen?"

    h "Hey jetzt!!{w} Du solltest dankbar sein, dass ich dein Leben vorhin verschont habe.{w} Ich hätte dich locker in zwei Teile zerschneiden können, als dich die Kraft verlassen hat!"

    y "Vielleicht wäre es besser gewesen, wenn du es getan hättest.{w} Ich habe keinen Grund, jetzt zu leben.{w} Ich bin...{w}Ich bin ein Versager."

    p "Sag das nicht!"

    "Ich kann diesen Anblick nicht länger ertragen und dränge mich an Sayaka und Hikari vorbei, um ihr gegenüberzutreten."

    "Yuzuki sieht mich mit einem überraschten Blick an, welcher sich jedoch kurz darauf wieder in einen Blick der Niederlage verwandelt."

    y "Warum nicht?{w} Es ist die Wahrheit, nicht wahr?"

    y "Ich war so verzweifelt nach einer Art Gesellschaft in meinem Leben, dass ich ihr mein Leben freiwillig gab."

    y "Sie erzählte mir alles, was ich hören wollte.{w} Dass jeder mich anbeten und mir gehorchen würde, wenn ich ihr helfen würde..."

    h "Was?!{w} Das ist das Dümmste, was ich je gehört--"

    y "Es klingt dumm, ich weiß.{w} Zu denken, dass ich all das in der vergeblichen Hoffnung getan habe, dass es mich bekommen würde ...{w}Freunde."

    y "Ich habe gerade nicht nachgedacht.{w} Ich war so besessen davon, dass ich niemals daran dachte, irgendwas zu hinterfragen."

    "Sie ist kein schlechter Mensch.{w} Sie wurde bloß fehlgeleitet.{w} Und sie hat die falschen Dinge getan, um ihr Ziel zu erreichen.{w} Ich habe Mitleid mit ihr ...{w} und es tut mir leid, dass es so enden musste."

    y "Und jetzt, mit der einzigen Chance, die ich hatte, war mein Ziel immer dahin.{w} Warum sollte ich weiterleben?{w} Es ist hoffnugslos..."

    s "Hmm.{w} Verstehe, verstehe."

    "Auf einmal nickt Sayaka."

    stop music fadeout 2.0

    s "Ich glaube, ich kenne da eine einfache Lösung für all das!"

    y "...?"

    h "D-Du kennst eine?"

    s "Jup!"

    "Sayaka hüpft nach vorne und streckt mit einem Lächeln im Gesicht Yuzuki die Hand entgegen."

    s "{i}Wir werden{/i} deine Freunde, Yuzuki."

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

    "Yuzuki ist erstaunt über diese abrupte Geste, aber nicht so sehr wie Hikari."

    h "Hä?!{w} W-Werden wir?!"

    y "...Wirklich!?"

    $ sayaface='happy'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Na klar!{w} Du scheinst kein schlechter Mensch zu sein.{w} Ich denke, du hast einfach nur einen falschen Weg eingeschlagen."

    $ hikaface='angry'
    show Hikari

    h "S-Sie hat uns versucht zu töten, Sayaka!{w} Wie kannst du sagen, dass sie nicht--"

    $ sayaface='joking'
    show Sayaka

    s "Ahh, das ist Schnee von gestern.{w} Ich bin sicher, du hast auch schon ein paar Mal versucht, mich umzubringen, Hikari!"

    $ yuzuface='angry'
    show Yuzuki

    y "I-ist das eine Art Trick?{w} Verspottest du mich...?"

    $ sayaface='smiling'
    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "Kein Trick.{w} Ich, Kenta, und {i}selbst{/i} Hikari ... Wir freuen uns alle, deine Freunde zu sein."

    s "Stimmt's, Leute?"

    p "Klar.{w} Ich hab kein Problem damit."

    $ hikaface='normal'
    show Hikari

    h "Jetzt warte mal kurz--"

    s "{i}Stimmt's{/i}, Hikari?"

    "Sayaka verdreht ihren Kopf, um Hikari auf eine unnatürliche Art und Weise anzusprechen.{w} Das kommt wie vor wie in einem Horrorfilm ..."

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

    "Yuzuki weiß nicht, wie sie all das verarbeiten soll.{w} Ihr Gesicht zeigt eine große Vielzahl von Emotionen, ehe sie kurz darauf mit Tränen in den Augenwinkeln zu lächeln beginnt."

    y "Ich...{w}Ich verdiene nichts davon.{w} Warum bist du so nett?"

    $ hikaface='normal'
    $ sayaface='happy'
    show Sayaka
    show Hikari

    s "Aw, sei doch nicht so.{w} Jeder verdient Freunde!{w} Wen kümmert's, dass man ein paar schlimme Dinge getan hat?{w} Wahre Freunde sehen darüber hinweg!"

    "Ich bin mir nicht sicher, ob wir die Tatsache, dass sie dieser verrückte, dunkle Engel war, einfach so ignorieren sollten, aber irgendwie hat Sayaka doch recht."

    $ sayaface='smiling'
    show Sayaka

    s "Na jetzt komm schon.{w} Verschwinden wir aus dieser dunklen Höhle und vergessen wir das alles.{w} Ich weiß ja nicht, wie es euch geht, aber ich bin hundemüde."



    scene bg black
    with fade

    "Und so verlassen wir alle gemeinsam die Höhle."

    "Ein lange verschollenes Übel wurde beseitigt und wir haben einen neuen Freund gefunden.{w} Alles in allem würde ich sagen, dass das heute ein ziemlich ereignisreicher Tag war!"

    "Glücklicherweise finden wir dank Yuzuki schnell den Weg aus der Höhle, ohne durch diese Tunnel krabbeln zu müssen."
    
    "Anderenfalls, so befürchte ich es zumindest, wären wir wahrscheinlich eh nie aus der Höhle rausgekommen."

    "Ich kann jetzt wieder klar denken.{w} Die Kopfschmerzen sind weg.{w} Hoffentlich für immer."

    scene forest trail
    with fade

    "Wir kommen zurück in den Wald.{w} Nachdem wir so lange in dieser Höhle waren, sind diese warmen Sonnenstrahlen wirklich eine willkommene Abwechslung."

    show Sayaka
    $ sayaface='happy'
    $ sayapose='magical_1'
    with dissolve

    s "Ahhh, endlich frische Luft!"

    "Sayaka läuft ein Stück nach vor, um die frische Luft 'aufzusaugen'.{w} Hikari und Yuzuki, scheinbar noch immer nicht wohlwollend zueinander, hinken hinterher."

    s "Nun, das hat ja nicht mal so lang gedauert, als ich vermutet hätte.{w} Sieht aus, als hätten wir den Großteil vom Tag noch vor uns!"

    "Sie strahlt weiterhin ihren typischen Optimismus aus, als sie sich sonnen lässt.{w} Ich hingegen kann eine Frage, die ich mir schon seit unserer Abreise durch den Kopf geht, einfach nicht abschütteln."

    p "Was ...{w} Was geschieht jetzt?"

    $ sayaface='smiling'
    show Sayaka

    s "Hmm?"

    p "Ich mein, haben wir diesen einen Grund, weshalb ihr hier seid, nicht gerade aus der Welt geschafft?"

    $ sayaface='normal'
    show Sayaka

    s "Ohh ..."

    "Angesichts ihres immer kleiner werdenden Lächelns schätze ich, dass sie verstanden hat, was ich meine.{w} Und ...{w} es sieht so aus, als wäre diese Reaktion auch schon die Antwort auf meine Frage."

    s "Das ...{w} Na ja ..."

    $ hikaface='normal'
    show Hikari at right
    show Sayaka at left
    with dissolve

    h "Du hast recht.{w} Unser Job hier {i}ist{/i} erledigt."

    "Sie sehen mich beide feierlich an.{w} Ich wusste es.{w} Ich wollte es nicht akzeptieren, aber ich wusste die ganze Zeit, dass das passieren würde ..."

    $ yuzuface='shocked'
    $ yuzupose='magical_1'
    show Yuzuki at center
    with dissolve

    y "Warte, du wirst jetzt gehen?!{w} Ich dachte, du hättest es versprochen--"

    $ sayaface='smiling'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Hey!{w} Wer hat irgendwas vom Gehen gesagt?"

    $ yuzuface='normal'
    show Yuzuki

    s "Es stimmt, dass wir keinen {i}offiziellen{/i} Grund mehr haben, hierzubleiben."

    $ sayaface='joking'
    show Sayaka

    s "Aber ich denke, wir haben uns jede Menge Urlaub verdient, den wir einlösen sollten.{w} Nicht wahr, Hikari?"

    h "Urlaub?{w} Was um alles in der Welt meinst--"

    $ sayaface='happy'
    $ hikaface='scared'
    show Hikari
    show Sayaka

    "Dieses Lächeln.{w} Dieser Blick.{w} Hikaris Satz wird mittendrinn unterbrochen.{w} Jetzt verstehe ich, wer hier der Anführer dieser Gruppe ist."

    $ hikaface='normal'
    show Hikari

    h "A-ah!{w} Ja, natürlich!{w} Wir haben viel Freizeit, wir könnnen uns mal frei nehmen."

    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "Siehst du!{w} Die Zeichen stehen noch nicht auf Abschied.{w} Ich bin doch nicht so gemein und verlasse euch!"

    $ sayaface='smiling'
    show Sayaka

    s "Und wir werden das Beste aus der Zeit rausholen, die wir zusammen verbringen.{w} Als Freunde!{w} Es gibt hier noch so viel, was ich versuchen möchte!"

    "Während Sayaka jede Menge Dinge aufzählt, die sie in ihrem Urlaub machen möchte, scheint sich Hikari mit dieser Idee noch immer nicht ganz abgefunden zu haben."

    "Ich schätze, diese streng geheime Organisation, der sie angehören, wird nicht ganz glücklich darüber sein ..."

    "Aber trotzdem bin ich froh darüber, dass wir noch etwas Zeit miteinander verbringen können.{w} Auch wenn diese Zeit nicht ewig dauern wird."

    "Und obwohl die letzten Tage ziemlich verrückt waren ...{w} muss ich zugeben, dass ich es nicht wirklich gehasst habe."

    "Klar, die Momente, in denen ich fast umgekommen wär, waren nicht so der Burner, aber der Rest hat richtig Spaß gemacht."

    "Kurzum, es war eine neue Erfahrung für mich, auf die ich im Nachhinein lächelnd zurückblicken kann."

    "Sie waren nicht nur meine Schutzengel, sondern auch meine Freunde.{w} Verdammt gute Freunde, um ehrlich zu sein."

    "Okay, Sayakas Scherze schossen gelegentlich über das Ziel hinaus und Hikari war manchmal ein wenig zu rechthaberisch ...{w} aber es kann schließlich nicht immer alles perfekt sein."

    $ sayaface='happy'
    show Sayaka

    "Sie haben mich in eine komplett neue und unbekannte Welt gezogen.{w} Und ich war anfangs vielleicht ein kleines bisschen zu zögerlich dabei, alles zu akzeptieren."

    $ hikaface='angry'
    show Hikari

    "Aber im Nachhinein würde ich diese Erfahrungen gegen nichts auf der Welt eintauschen."

    "Ich habe das Gefühl, als hätten sie mich zu einem besseren Menschen gemacht.{w} Als hätten sie mich aus der Hülle gezogen, in der ich mich all die Zeit über versteckt hatte."

    $ sayaface='joking'
    show Sayaka

    "Als meine Beschützer wieder einen Streit beginnen, muss ich einfach anfangen zu lachen.{w} Ich bin mir nicht sicher, was es diesmal ist."

    "Ich muss wirklich darauf achten, das Beste aus der Zeit zu machen, die uns noch bleibt."

    "Es ist ein bisschen deprimierend, zu wissen, dass diese Zeit nicht ewig andauern wird, aber gleichzeitig ist es umso mehr Ansporn, sie voll und ganz auszuschöpfen."

    h "Ich bring dich um!"

    $ sayaface='scared'
    show Sayaka

    s "Wahh, beruhig dich, war doch bloß ein Scherz!{w} Kenta, beschütz mich!"

    $ yuzuface='scared'
    show Yuzuki

    y "Du bist sicherlich ein seltsamer Haufen..."

    "...Jup.{w} Glüchliche Erinnerungen."

    scene bg white
    with wake
    with Pause(3.0)
    scene bedroom day
    with wake

    "Ich wache auf und fühle mich besser denn je.{w} Keine Kopfschmerzen.{w} Kein Anzeichen daran, etwas Schreckliches geträumt zu haben.{w} Lediglich ...{w} Glückseligkeit."

    "Es ist nun eine Woche her, seit wir die dunkle Königin wieder versiegelt haben.{w} Und Sayaka und Hikari sind - wie sie es versprochen haben - bei mir geblieben."

    "Sie gehen weiter zur Schule und wir hängen weiterhin gemeinsam ab."

    "...Sie bestehen aber noch immer darauf, draußen zu campen.{w} Wobei es dafür keinen Grund mehr gab, da es seitdem keine Monsterangriffe mehr gab."

    "Vielleicht haben sie sich einfach schon daran gewöhnt?{w} Oder sie sind noch sturer geworden ... Was weiß ich."

    "Aber vielleicht ist es ja gar nicht mal so schlecht.{w} Es überrascht mich nur, dass sie noch nicht erwischt wurden.{w} Und wenn diese Zeit kommt, sage ich nur, 'ich hab euch gewarnt'."
    stop music fadeout 2.0
    p "Hm?"

    "Irgendjemand klopft da an meiner Tür.{w} Wer das wohl ist?"



    if sayaka > hikari:


        s "Yo!{w} Ich hoffe, du bist schon fertig angezogen und so, denn das wird super peinlich."
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"
        $ sayaface='smiling'
        $ sayapose='school_1'
        show Sayaka
        with dissolve

        "Kurz darauf schwingt sie auch schon die Tür auf, wodurch sie mir keine Zeit zum Reagieren lässt."

        "Als sie mich sieht, seufzt sie gleich mal – mit einem enttäuschten Gesichtsausdruck, wenn ich es nicht falsch interpretiere."

        s "Aww."

        p "Äh, guten Morgen, Sayaka."

        "Ich binde gerade meine Krawatte.{w} Unglücklicherweise – zumindest für sie – bin ich nicht nackt.{w} Das passiert so früh am Morgen nicht oft, aber mit der Zeit hab ich gelernt, dass man bei ihr ziemlich vorsichtig sein muss."

        $ sayaface='happy'
        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Morgen!{w} Scheint, als wäre mein Versuch, mich an dich heranzuschleichen, nach hinten losgegangen."

        $ sayaface='smiling'
        show Sayaka

        s "Vielleicht werde ich schon zu berechenbar?"

        p "Vielleicht."

        $ sayaface='joking'
        $ sayapose='school_1'
        show Sayaka
        with dissolve

        s "Hmm.{w} Vielleicht sollte ich das nächste Mal beim Fenster reinkommen?"

        "...Bitte nicht."

        $ sayaface='happy'
        show Sayaka

        "Sayaka bricht in Hysterie aus, bevor sie anfängt, in meinem Zimmer herumzuschnüffeln."

        $ sayaface='smiling'
        show Sayaka

        "Sie hat es sich in letzter Zeit zur Gewohnheit gemacht, mich morgens aufzuwecken.{w} Ich kann gar nicht beschreiben, wie viel Angst ich hatte, als ich zum ersten Mal aufwachte und sie mich mit einem breiten Grinsen angelächelt hat."

        "Sie sagt, sie möchte lediglich sicherstellen, dass ich pünktlich in der Schule ankomme, aber ich bin mir ziemlich sicher, dass es da auch noch andere Gründe gibt."

        "Ich habe das Gefühl, dass wir uns seit den Vorfällen in der Höhle wesentlich näher gekommen sind."

        "Sie war schon immer sehr freundlich und anhänglich, sicher, aber diese Eigenschaften sind nun weitaus ausgeprägter."

        "Mittags zum Beispiel packt sie mich an der Hand und zieht mich in die Cafeteria, ob ich möchte oder nicht.{w} Und während unserer Spaziergänge kommt es mir so vor, als würde sie alles versuchen, um mir näher zu sein als es Hikari ist."

        "Vielleicht bilde ich mir das aber auch nur ein?{w} Ich weiß es nicht.{w} Ich weiß nur--"

        p "H-Hey!{w} Wer hat gesagt, dass du das anfassen kannst?!"

        "Sie stöbert an meinem Laptop herum – etwas, das sie immer im Auge hat, wenn sie hier ist."

        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Hm?{w} Ich wollte nur nachsehen.{w} Ich mein, ein so junger und gesunder Bursche wie du, hat doch bestimmt nichts zu verstecken, hmm?"

        p "Ähm.{w} Genau.{w} A-Aber wir kommen noch zu spät zur Schule, wenn du hier rumblödelst!"

        $ sayapose='school_1'
        show Sayaka
        with dissolve

        s "Mmm.{w} Ich guck dann mal schnell nach.{w} Mal sehen ...{w} Wo könnte dieser 'wichtige Schulkram'-Ordner bloß sein?{w} Oder was ist das für ein komisches Zeugs mit dem Passwort da--"

        p "Sayaka!"

        $ sayaface='joking'
        show Sayaka

        s "Nur ein Scherz, nur ein Scherz!{w} Ich habe es nicht mal aufgedreht."

        "Sie schwenkt den Laptop vor mich hin und her."

        p "O-Ohh ..."

        $ sayaface='smiling'

        s "Aber deine Reaktion ist wirklich interessant.{w} Fast so, als hättest du wirklich einen solchen Ordner, hmm?"

        "..."

        "Wenn ich nichts sage, kann mir auch niemand eine Lüge vorwerfen.{w} Ich starre sie mit einem emotionslosen Gesichtsausdruck an."

        "Sie öffnet ihren Mund, um mir etwas zu sagen – ohne Zweifel etwas, mit dem sie mich weiter ärgern möchte."

        with hpunch

        h "Wir werden noch zuspät kommen, wenn ihr zwei nur rumalbert!"

        "Hikaris Stimme, die bis nach oben durchdringt, rettet mich gerade noch rechtzeitig."

        $ sayaface='happy'
        show Sayaka

        s "Na ja.{w} Verschieben wir das Ganze auf ein anderes Mal, hmm?{w} Glauben Sie aber ja nicht, dass Sie so einfach davonkommen, Mister!"

        hide Sayaka
        with dissolve

        "Sie verlässt mein Zimmer und geht die Treppe hinunter."

        stop music fadeout 2.0

        scene kitchen day
        with dissolve

        "Kurz darauf gehe auch ich nach unten, wo ich von zwei weiteren Gästen empfangen werde."

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

        "Hikari und Yuzuki stehen im Esszimmer. In Anbetracht des Abstands zwischen den beiden gehe ich mal davon aus, als hätten sie sich noch nicht miteinander angefreundet."

        "Ähnlich wie Sayaka und Hikari scheint auch Yuzuki nicht davor zurückzuschrecken, während ich schlafe, in mein Haus einzubrechen."

        "...Und das bereitet mir ernsthaft Sorgen."

        p "Guten Morgen, meine Lieben."

        $ hikaface='angry'
        show Hikari

        h "Es ist Zeit.{w} Was wollt ihr beide jetzt tun?"

        $ sayaface='happy'
        show Sayaka

        s "Nun, wenn du's {i}wirklich{/i} wissen musst ... Wir haben--"

        h "Eigentlich, will ich es garnicht hören!{w} Ich bin sicher, es war etwas unangebrachtes."

        "Hey, warum werd ich mit ihr in einen Topf geworfen?{w} Ich bin ein unschuldiger Junge!"

        $ sayaface='joking'
        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Ach.{w} Dein Pech."

        $ yuzuface='smiling'
        show Yuzuki

        y "Kenta.{w} Guten Morgen."

        "Yuzuki begrüßt mich mit einem schwachen, jedoch sanften, Lächeln im Gesicht."

        hide Sayaka
        hide Hikari
        show Yuzuki at center
        with dissolve

        "Sie öffnet sich uns gegenüber immer mehr.{w} Zwar ist sie die meiste Zeit über noch ziemlich ruhig, und sie nimmt auch nicht oft an unseren Gesprächen teil, aber ich denke, sie schätzt unsere Gesellschaft."

        "Es muss schwer für sie sein, sich an all das zu gewöhnen. Schließlich hat sie endlich Freunde gefunden.{w} Freunde, die sie sich so lange gewünscht hatte."

        "Ich bin mir sicher, dass es nicht mehr lange dauern wird, bis sie sich mit Hikari und Sayaka versteht.{w} Sie haben es schließlich auch geschafft, mich zu einem besseren Menschen zu machen."

        "Ich begrüße sie mit einem Kopfnicken, allerdings werden meine Augen schnell auf Sayaka gelenkt, die auf einen gefährlichen Ort zusteuert."

        $ sayaface='smiling'
        $ sayapose='school_1'
        hide Yuzuki
        show Sayaka at center
        with dissolve

        s "So!{w} Wer hat Lust auf Frühstück?"

        p "Oh nein, das kommt gar nicht in Frage!"

        $ sayaface='scared'
        show Sayaka

        "Sie hält an – nur wenige Zentimeter von der Küche entfernt."

        s "Aw, aber ich wollte doch nur--"

        p "Nop."

        $ sayaface='smiling'
        show Sayaka

        s "Schon gut, schon gut.{w} Ich hab's versucht."

        p "Das hast du, und ich bewundere dich auch dafür ... Aber es wird nicht passieren.{w} NIE WIEDER."

        $ sayaface='shocked'
        show Sayaka

        s "Aber der Versuch war gar nicht mal so schlecht!"

        $ sayaface='smiling'
        show Sayaka

        "Ich gehe an ihr vorbei und betrete selbst die Küche.{w} Sie zeigt mir den üblichen Schmollmund, aber dieser verwandelt sich wie immer relativ schnell in ein Lächeln."

        s "Also ...{w} Darf ich zumindest ... {w}zusehen?{w} Vielleicht kann ich dann ja gleich für die Zukunft ein bisschen was lernen!"

        "Sie sieht mich mit einem Blick an, zu dem man unmöglich Nein sagen kann.{w} Gottverdammt!"

        p "Argh, gut, von mir aus!{w} Fass aber bloß nichts an."

        $ sayaface='happy'
        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Yay!"

        "Sie sieht mir über die Schulter.{w} Wortwörtlich.{w} Ihr Kopf liegt auf meiner Schulter.{w} Es macht das Ganze zwar etwas schwieriger, aber um ehrlich zu sein ...{w} es fühlt sich nicht schlecht an."

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

        s "Ahh, köstlich!"

        "Nachdem sie ihre Mahlzeit in Rekordzeit veputzt hat, seufzt Sayaka mit einem zufriedenen Blick.{w} Ich frage mich, ob man überhaupt etwas vom Geschmack mitbekommt, wenn man das Essen so runterschlingt."

        $ sayaface='smiling'
        show Sayaka

        y "Ja.{w} Es war nett.{w} Ich habe nicht erwartet, dass du so ein guter Koch bist, Kenta."

        $ hikaface='angry'
        show Hikari

        h "Vielleicht heute ein bisschen übertrieben.{w} Ich mache dir jedoch keine Vorwürfe, dass sich dieses {i}Ding{/i} in der Küche zu dir gesellt hat."

        s "Achtung, Hikari, deine Eifersucht macht sich bemerkbar!"

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

        s "Wow!{w} Ich glaube, ich habe noch nie erlebt, dass du es so eilig gehabt hast, in die Schule zu kommen, Hikari."

        $ hikaface='angry'
        show Hikari

        h "Hmph!"

        hide Hikari
        show Sayaka at left
        show Yuzuki at right
        with dissolve

        "Während Sayaka, Yuzuki und ich noch unsere Schuhe anziehen, stürmt Hikari bereits aus dem Haus.{w} Werde ich sie eines Tages vielleicht doch noch verstehen?"

        $ sayaface='happy'
        show Sayaka

        s "Komm schon, ein Abenteuer wartet auf uns, Kenta!"

        hide Yuzuki
        show Sayaka at center
        with dissolve

        "Als Yuzuki vorbeischlendert, streckt Sayaka mir eine Hand entgegen."

        p "Also den Test, den wir heute haben, würd ich wohl kaum als 'Abenteuer' bezeichnen ..."

        $ sayaface='shocked'
        show Sayaka

        s "Warte.{w} Wir haben einen Test?!"

        p "Na ja.{w} Schon.{w} Es wurde immer wieder diese Woche erwähnt!{w} Sag jetzt bloß nicht ..."

        $ sayaface='joking'
        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "He-hehehe-heheh ..."

        "Hoffnungslos.{w} Ich muss einfach lächeln."

        $ sayaface='happy'
        $ sayapose='school_1'
        show Sayaka
        with dissolve

        s "Ah, schon gut.{w} Ich werde einfach von dir abschreiben, wenn ich nicht weiter weiß!{w} Also ...{w} Auf, auf und davon!"

        "Sie nimmt mich an der Hand und fängt an, mich aus dem Haus zu ziehen."

        p "S-Sayaka, warte, ich hab nicht mal meine Schuhe an!"

        s "Auf geht's!"

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

        "Sie öffnet langsam die Tür.{w} .Mit einer Hand vor ihren Augen kommt sie herein.{w} Es sieht so aus, als hätte sie damit gerechnet, dass ich in einer ungünstigen Situation vor ihr stehe."
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"        
        $ hikaface='smiling'
        show Hikari

        "Erleichtert aufgrund der Tatsache, dass ich nicht nackt bin, begrüßt sie mich mit einem Lächeln."

        h "Oh.{w} Guten Morgen."

        p "Morgen!"

        "An ihr Lächeln muss ich mich erstmal noch gewöhnen."

        "In der Höhle hat sich zwischen uns beiden eindeutig was verändert.{w} Ich weiß nicht, wie ich es ausdrücken soll, aber sie ist wesentlich ...{w} freundlicher?"

        "Ihre Verdrießlichkeit zeigt sich zwar noch immer sehr oft, aber sie lächelt mittlerweile auch viel häufiger.{w} Und das gefällt mir.{w} Es passt wirklich gut zu ihr."

        "Sie steht unbeholfen da – als ob sie sich nicht sicher wäre, was sie nun tun soll."

        p "Warte ...{w} Du hast gesagt, ihr seid schon alle da und ihr habt Hunger, oder?"

        $ hikaface='normal'
        show Hikari

        h "Huh?{w} Ja.{w} Warum?"

        p "Und du, äh ...{w} und du hast Sayaka unbeaufsichtigt lassen ...?"

        h "Ich bin mir nicht sicher was du..."

        $ hikaface='shocked'
        show Hikari

        "Als sie es bemerkt, werden ihre Augen schnurstracks riesengroß.{w} {i}Ja{/i}."

        h "Vielleicht ist es noch nicht zuspät."

        p "Ich hoff's doch!"

        stop music fadeout 2.0

        scene kitchen day
        with dissolve

        "Wir stürmen beide nach unten."

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

        "Sayaka und Yuzuki stehen in der Küche.{w} Und machen ...{w} etwas.{w} War das mal eine Schüssel mit Müsli?{w} Jetzt jedenfalls kann ich es nicht mehr sagen."

        s "Ooh, und gib mir das, und das auch.{w} Und davon kommt auch noch was rein!"

        y "Interessant.{w} Ich wusste nie, dass du so ein Auge für diese Dinge hast, Sayaka."

        "Yuzuki antwortet völlig gelassen, als sie Sayaka all die Dinge überreicht, die das Chaos noch schlimmer machen."
        
        "Sie dreht sich kurz um und begrüßt mich mit einem Kopfnicken, allerdings widmet sie sich dann gleich wieder dem vermeintlichen Frühstück."

        "Sie öffnet sich uns gegenüber immer mehr.{w} Zwar ist sie die meiste Zeit über noch ziemlich ruhig, und sie nimmt auch nicht oft an unseren Gesprächen teil, aber ich denke, sie schätzt unsere Gesellschaft."

        "Es muss schwer für sie sein, sich an all das zu gewöhnen. Schließlich hat sie endlich Freunde gefunden.{w} Freunde, die sie sich so lange gewünscht hatte."

        "Ich bin mir sicher, dass es nicht mehr lange dauern wird, bis sie sich mit Hikari und Sayaka versteht.{w} Sie haben es schließlich auch geschafft, mich zu einem besseren Menschen zu machen."

        "Ich begrüße sie ebenfalls mit einem Kopfnicken, richte meine Augen aber sofort wieder auf Sayaka, die gerade eine Bedrohung für mein Wohlergehen darstellt."

        "Aber unsere verzweifelten Schreie gehen einfach unter."

        $ sayaface='happy'
        show Sayaka

        s "Na, ich schätze, das gehört auch hier rein.{w} ... Wahrscheinlich!"

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

        "Plötzlich rutscht Hikari über den Tresen, fast so wie ein Filmheld, bevor sie kurz darauf einen Blitz aus ihren Fingerspitzen schießt, der die Substanz, die Sayaka noch als 'Frückstück' bezeichnet hat, in Luft auflöst."

        $ hikaface='normal'
        $ hikapose='school_2'
        show Hikari
        with dissolve

        h "Phew.{w} Krise abgewendet."

        s "W-Wahh!{w} Wofür war das denn?"

        $ hikaface='angry'
        show Hikari

        h "Das weißt du genau!"

        $ sayaface='smiling'
        show Sayaka

        play music "bgm/everydayintro.ogg" fadein 2.0
        queue music "bgm/everydayloop.ogg"

        "Sayaka seufzt und lässt ihre Arme an der Seite runterhängen."

        s "Ich wollte doch nur lieb sein und Frühstück für euch machen, während ihr oben die Verliebten spielt."

        $ hikaface='shy'
        show Hikari

        h "L-lovey-dovey?{w} Sayaka, ich denke du hast--"

        $ sayaface='joking'
        show Sayaka

        s "Aww, ihr müsst es nicht vor mir verstecken.{w} Solche Dinge bekomme ich immer mit.{w} Sagt einfach was, und Yuzuki und ich werden euch Zeit für euch alleine geben."

        $ hikaface='embarrassed'
        show Hikari

        h "S-Sayaka, ich werde..."

        "Hikari bebt förmlich. Ich weiß nicht, ob dieser Gesichtsausdruck Wut oder Verlegenheit darstellen soll.{w} Oder vielleicht ...{w} beides?"

        hide Sayaka
        show Hikari at center
        with dissolve

        "Anscheinend mit sich vollends zufrieden, springt Sayaka mit Yuzuki im Schlepptau aus der Küche."

        p "Nun.{w} Äh.{w} Sieht aus, als müssten wir uns auf dem Weg zur Schule irgendwo was zu essen kaufen."

        p "Ähh ...{w} H-Hikari?"

        "Seit Sayaka gegangen ist, hat Hikari kein Wort mehr gesagt.{w} Sie steht einfach nur da.{w} Wie eine Statue."

        h "S-Sind...wir..."

        p "Hmm?"

        "Sie murmelt – kaum hörbar – vor sich hin."

        h "Sind wir wirklich...{w}l-lovey-dovey...?"

        p "Ähh.{w} Ich weiß jetzt echt nicht, wie ich darauf antworten soll.{w} {i}Sind{/i} wir das?"

        "Ich mein, wir sind uns seit der Wiederversiegelung wesentlich näher gekommen."

        "Sie ist seit dem viel netter zu mir und versucht ihr Bestes, mich aus Sayakas Fängen zu befreien.{w} Was manchmal eine echt schwierige Aufgabe ist.{w} Ich glaube sogar, dass meine Arme bereits länger geworden sind ..."

        $ hikaface='shy'
        $ hikapose='school_1'
        show Hikari
        with dissolve

        h "Ich...{w}Ich meine...{w} Wenn du {i}willst{/i} das wir--"

        "Sie fährt mit ihrer Hand durchs Haar und schreit auf."

        h "Ahh!{w} N--Nein!{w} Was sage ich da?!{w} Es ist Sayaka...{w} Sie kommt wirklich zu mir!"

        h "Kenta, i-ich hoffe du hast das nicht gehört..."

        "Ich lächle sie an, um sie zu beruhigen.{w} Sayaka kann sagen, was sie will, aber ich denke, wir wissen beide, wie unsere Beziehung zueinander ist."

        p "Hikari, schon gut.{w} Mach dir keine Sorgen.{w} Ich bin glücklich mit der momentanen Situation."

        p "Lass es uns einfach, äh, langsam angehen, okay?{w} Ignorier Sayaka einfach."

        $ hikaface='normal'
        show Hikari

        h "..."

        "Sie nickt.{w} Puh.{w} Ich dachte schon, ich hätte was Falsches gesagt.{w} Bei Hikari kann man ja nie wissen!"

        p "Also vergessen wir das Ganze erstmal und holen wir uns was zu frühstücken!"

        h "Ja.{w} Das hört sich gut an."

        p "Okay, Mädels, wir--häh ...?"

        "Sayaka und Yuzuki sind schon weg.{w} Sie hat uns wirklich Zeit für uns allein gegeben!"

        p "Wir sollten uns wohl besser beeilen.{w} So wie ich Sayaka kenn, ist sie wahrscheinlich schon meilenweit voraus."

        hide Hikari
        with dissolve

        "Ich fange an, mir meine Schuhe anzuziehen, aber plötzlich zerrt etwas an meinem Ärmel."

        p "Hikari ...?"

        $ hikaface='smiling'
        show Hikari at center
        with dissolve

        "Sie blickt schüchtern drein."

        h "Können wir vielleicht in unserem eigenen Tempo gehen??{w} Ich denke, ihnen wird's auch gut gehen, ohne uns."

        "Unmittelbar auf ihre Worte hängt sie ihren Arm bei meinem ein."

        p "O-Oh.{w} Äh, okay.{w} Klar, kein Problem!"

        "Ich hab noch Probleme damit, mich an diese neue Hikari zu gewöhnen, aber ich denke, ich komme schön langsam voran."

        "Hand in Hand gehen wir durch die Vordertüre – bereit, jede Herausforderung anzunehmen, die uns erwartet."

        stop music fadeout 2.0

        scene bg white
        with wake



    if sayaka == hikari:


        "..."

        "Dem Klopfen folgt kurz darauf ein weiteres ... und noch eins."

        h "Sayaka, ich bin mir sicher er hat es schon gehört!"

        s "Schwachsinn, man kann nie zu vorsichtig sein."

        "Hmm, wer das wohl ist ..."

        "Ich bleib einfach mal ruhig. Nur um zu sehen, was passiert."

        s "Hmm?{w} Nichts?{w} Vielleicht schläft er wirklich noch?"

        "{i}Klopf, klopf, klopf.{/i}{w} Sie hämmert ein weiteres Mal gegen die Tür."

        h "Denkst du, es geht im gut ...?{w} Er war wirklich müde, als wir uns letzte Nacht getrennt haben."

        "Ich schätze, die beiden bemerken gar nicht, wie anstrengend sie in den letzten Tagen geworden sind."

        "Irgendwie bin ich ja froh, dass sie bei mir geblieben sind, aber ..."

        "Aber seit der Wiederversiegelung konkurrieren sie {i}noch{/i} stärker gegeneinander.{w} Ich weiß es nicht, was sie noch beweisen wollen."

        s "Hmm ...{w} Jetzt, wo du's sagst, er hat wirklich blass ausgesehen.{w} Vielleicht hat er sich eine tödliche Krankheit eingefangen, mit der er uns nicht konfrontieren wollte?"

        h "W-Was?!"

        "Die Türschnalle klappert schon.{w} Aber sie geht nicht ganz nach unten."

        h "Aber wenn er noch schläft ...{w} Ist es wirklich okay für uns, einfach so reinzuplatzen?"

        s "Und ob!{w} Ich mach es die ganze Zeit.{w} Hast du ihn schon mal beim Schlafen zugesehen, Hikari?{w} Er ist so niedlich!{w} Da, ich hab ein paar Bilder davon gemacht."

        "...Es kommt mir so vor, als wollen mich die beiden vergewaltigen.{w} Ich bin ja echt froh darüber, dass ich bereits wach bin."

        h "Sayaka!{w} Du hättest wirklich nicht--awww..."

        s "Ich weiß, nicht wahr?{w} Du willst nicht wissen, wie sehr ich dazu verleitet wurde, etwas auf sein Gesicht zu zeichnen."

        h "W-Wie auch immer!{w} Du lenkst mich ab.{w} Ich muss nachgucken, ob es ihm gutgeht!"

        s "Vielleicht möchte ich es {i}mehr{/i} als du!"

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

        "Die Tür geht auf und die beiden stürzen herein.{w} Manchmal legen sie echt einen sehenswerten Auftritt hin."

        p "Ähh ...{w} Guten Morgen?"

        $ sayaface='smiling'
        show Sayaka

        s "Oh, hey, Kenta!"

        "Sayaka spricht unter Hikari liegend und begrüßt mich."

        $ hikaface='angry'
        show Hikari

        h "Warte, du warst wach?{w} Warum hast du nichts gesagt?!{w} Weißt du, wie besorgt wir waren?"

        p "Ahh ..."

        $ hikaface='scared'
        show Hikari

        "Hikari öffnet wieder ihren Mund - dieses Mal, um mich zu schimpfen - aber Sayaka erwischt sie unvorbereitet, als diese aufspringt."

        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Vielleicht mag er dich einfach nicht, Hikari, und hat einfach darauf gewartet, dass du aufgibst, damit wir Zeit für uns alleine haben können?"

        $ hikaface='angry'
        show Hikari

        h "A-absurd!{w} Und woher weißt du, dass es nicht andersrum ist?!"

        $ sayaface='happy'
        $ sayapose='school_1'
        show Sayaka
        with dissolve

        s "Na komm schon.{w} Hast du mich {i}gesehen{/i}?"

        "Sie nimmt eine Pose ein, die sie als 'sexy' betrachtet, aber in Wirklichkeit sieht sie relativ albern aus."

        $ hikapose='school_2'
        show Hikari

        "Hikari ist nicht gerade amüsiert und gibt ihr einen kräftigen Schubs, woraufhin sie zu Boden stürzt."

        $ sayaface='shocked'
        show Sayaka

        s "W-Wahh!"

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

        s "Hey, ich bin hier der Meisterkoch, {i}ICH{/i} sollte kochen!"

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

        s "Wer schläft, verliert!"

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

        s "Uuuund ...{w} fertig!"

        h "W-Was?!{w} Uh, ich auch!"

        $ hikaface='angry'
        show Hikari

        "Hikari mashes one last thing into her meal as she says so.{w} An entire egg.{w} Shell and all."

        p "Das ist, äh ...{w} großartig."

        $ sayaface='smiling'
        $ hikaface='normal'
        show Sayaka
        show Hikari

        s "So, so, so ...{w} Wessen Speise willst du essen?"

        "She proudly presents her...{w}something...{w}with a beaming smile.{w} Hikari seems more reserved, as if she might actually have some awareness about how bad the meal she's made is."

        p "Ohh ...{w} Wisst ihr was?{w} Ich hab gar keinen Hunger.{w} Ich wollte es euch ja eigentlich schon vorher sagen, aber ihr hattet es ja so eilig."

        $ sayaface='normal'
        $ sayapose='school_1'
        show Sayaka
        with dissolve

        s "Aww ...{w} Wirklich?"

        p "Und das ist echt schade, denn das hier sieht echt aus wie ...{w} Irgendwas."

        s "Vielleicht können wir es einpacken, dann kannst du später auch noch was essen?{w} Oder wir könnten auch was in die Schule mitnehmen, oder--"

        $ sayaface='scared'
        show Sayaka

        p "Nein!"

        s "H-Häh?"

        "I catch her off-guard with my sudden, desperate yell.{w} {i}Anything{/i} but that."

        $ sayaface='smiling'
        show Sayaka

        s "Gut.{w} Schön."

        play music "bgm/everydayintro.ogg" fadein 2.0
        queue music "bgm/everydayloop.ogg"

        "She huffs a sigh of defeat.{w} It doesn't last long, however, before her gaze settles on Yuzuki."

        $ sayaface='happy'
        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Ah, YuzukI!{w} Du hast bestimmt noch Hunger, oder?{w} Probier doch mal!"

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

        s "Ach, auch gut."

        h "Vielleicht war es das Beste?"

        $ sayaface='happy'
        show Sayaka

        s "Ja.{w} Hätte Kenta meine Kochkünste als besser bezeichnet, hätten hier ein paar Leute noch zu heulen begonnen."

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

        s "Gute Idee!{w} Du solltest mir folgen, Kenta, ich kenn eine echt gute Abkürzung!"

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

        s "Weißt du ...{w} Wenn wir fliegen, sind wir sogar noch schneller!"

        h "Nein!{w} Es wird am schnellsten sein, wenn wir {i}diesen{/i} Weg fliegen!"

        p "Mädels, wenn ihr so weitermacht, reißt ihr mich noch auseinander!{w} Arghhh!"

        stop music fadeout 2.0

        scene bg white
        with wake



    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
