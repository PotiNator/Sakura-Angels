


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

    "Die Geräuschkulisse der Umgebung ist ebenso fehlend wie das Geräusch meiner Schritte."
    
    "Selbst meine verzweifelten Schreie werden unverzüglich von der Dunkelheit verschluckt, sobald sie meinen Mund verlassen."

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

    cg "Meine Güte, das war echt knapp!{w} Alles in Ordnung?"
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

    tg "Als ob die Dinge nicht schlimm genug wären, dass wir uns ihm offenbaren mussten, jetzt redest du mit ihm über Sachen, die kein normaler Mensch wissen sollte. {w} Hast du den Verstand verloren ?!"

    "Das aggressivere Mädchen, dessen Ausdruck immer düsterer wurde, während die andere sprach, unterbrach plötzlich. Anscheinend konnte sie es nicht länger ertragen."

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

    cg "Na ja, wir kennen {i}dich{/i} nicht persönlich, aber wir beobachten dich schon eine Weile.{w} Du wurdest in letzter Zeit ziemlich beliebt!"

    p "Ich ...?"

    "Was hab ich in meinem Leben bloß falsch gemacht, dass mir so viel Aufmerksamkeit geschenkt wird?{w} Soviel ich weiß, bin ich doch nur ein normaler Schüler.{w} Der ein durchschnittliches Leben führt.{w} Und normale Dinge macht.{w} Wobei, nach all diesen Ereignissen trifft das wohl alles nicht länger zu."

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

    "Sie fängt an nachzudenken.{w} Ich schätze, sie wählt die Worte, die sie gleich sagen wird, sorgfältig aus, um zu verhindern, dass ihre Partnerin wieder auszuckt."

    $ sayaface='happy'
    $ sayapose='magical_1'
    show Sayaka

    cg "Betrachte uns als deine Schutzengel, okay?"

    "Als sie das sagt, macht sie mit ihrem Bogen eine schwungvolle Bewegung, woraufhin dieser kurz darauf zwischen ihren Fingern zerbricht.{w} Wenige Augenblicke später bilden sich diese Scherben hinter ihrem Rücken wieder zusammen, bis sich ein paar Flügel gebildet hat."

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

            tg "Wirklich?{w} Ich meine--wirklich?!{w} Bist du {i}wirklich{/i} so ein großer Idiot?!"

            p "I-Ich ... Äh ..."

            "Ich spüre, wie mich ihr Blick immer kleiner aussehen lässt.{w} Sie ist eindeutig noch gruseliger als das Monster!"

            tg "Es ist schon schlimm genug, dass wir uns zeigen mussten, aber jetzt tust du nur so, als wären wir verrückt?!"

            "Mit einem finsteren Blick ballt sie ihre Fäuse zusammen und hinterlässt den Eindruck, als würde sie am liebsten zuschlagen."

            tg "Ich weiß nicht einmal, warum wir uns um dich kümmern, wenn du uns so behandelst!{w} Vielleicht sollten wir sie dich nächstes mal einfach fressen lassen.{w} Hmph."

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

            "{i}BAM.{/i} Da landet die Faust direkt im Gesicht des fröhlichen Mädchens.{w} Und dieses Mal war es ernst gemeint, denn sie hielt kein bisschen zurück.{w} Das sah aus, als hätte es echt weh getan ..."

            tg "Halt dein Mund!{w} Ich habe soetwas nicht gesagt!"

            $ sayaface='scared'
            show Sayaka

            cg "Wahh!{w} Okay, okay, schon gut!"

            "Meine Güte ...{w} Die beiden sind echt komisch.{w} Aber sie schien es wirklich ernst zu meinen.{w} Vielleicht war meine Schlussfolgerung, sie als Verrückte abzustempeln, etwas voreilig."

            "Ich mein, sie sind verrückt, das stimmt schon, aber vielleicht steckt ja doch ein Fünkchen Wahrheit darin.{w} Die Existenz dieses Monsters kann ich schließlich auch nicht leugnen, so schwer es mir auch fällt."

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

    teacher "Nun, äh, ich weiß, dass es etwas plötzlich ist, aber ab heute haben wir zwei Studenten, die sich unserer Klasse anschließen."

    "Schulwechsler?{w} Um diese Zeit?{w} Schon ein bisschen spät, die Schule zu wechseln, oder nicht?{w} Selbst der Lehrer scheint ein bisschen verwirrt zu sein, als er es ankündigt."

    "Und nicht nur einer, sondern {i}zwei{/i}?{w} Warum hab ich bloß das Gefühl ... dass hier etwas vor sich geht?{w} Fast so, als ob es irgendwie mit den Ereignissen vorhin in Zusammenhang steht?"

    "Hah.{w} Nein.{w} Das kann unmöglich sein."

    teacher "Ich möchte, dass Sie sich alle willkommen fühlen, wenn sie einziehen. {w} Äh, wie haben Sie Ihre Namen genannt?"

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

    s "Die mürrische neben mir ist Hikari.{w} Komm schon, sag Hallo!"

    $ sayaface='happy'
    show Sayaka

    h "H-Hey, l-lass das--"

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

    s "Dass war doch nicht schwer, oder?"

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

    teacher "Worauf starren Sie alle? {w} Komm, lass uns zurückkommen!"

    "Da wir anscheinend alle vergessen hatten, dass wir selbst Unterricht haben, bringt uns der Lehrer zurück in die Realität.{w} Vorbei ist's mit dem schönen Anblick."

    scene bg black
    with fade

    "Der Rest der Stunde vergeht ohne großartige Ereignisse, und dann endlich, {i}ENDLICH{/i} ... Mittagspause."

    scene classroom
    with fade



    "Ich beobachte, wie die beiden Mädchen ganz entspannt im Klassenzimmer mit anderen Schülern plaudern.{w} Ich hätte nicht gedacht, dass sie so schnell Freunde finden würden.{w} Aber nach dem, was Sayaka vorhin abgeliefert hat, ist sie wahrscheinlich sowieso Gesprächsthema der Stunde."

    $ sayaface='smiling'
    $ sayapose='school_1'
    show Sayaka at center
    with dissolve

    s "Oh, Kenta.{w} Hallo!"

    "Sie winkt und lächelt mir zu, aber meine Reaktion ist nicht mal annähernd so fröhlich."

    p "Okay, ja, hi.{w} Äh, können wir reden?"

    $ sayaface='normal'
    show Sayaka

    s "Hm?{w} Sag es einfach!"

    p "Nein, nicht hier, ich mein ... Können wir unter vier Augen reden?"

    $ sayaface='shy'
    show Sayaka

    "...Scheiße.{w} Das hat sich vielleicht etwas komisch angehört.{w} Aus irgendeinem Grund sehen mich manche Schüler schon schief an.{w} Sogar Sayaka tut so, als wäre sie überrascht, obwohl sie genau weiß, was ich meine!"

    s "Oh, das ist aber schon ein bisschen plötzlich!{w} Ich weiß nicht was ich sagen soll..."

    p "Komm schon, hör auf rumzualbern.{w} Ich möchte einfach nur mit euch reden, und das schon seid heute morgen."

    "Oh Gott ...{w} Es wird nicht besser, oder?{w} Irgendwie hab ich aus der Situation das wohl peinlichste Geständnis ever gemacht."

    $ sayaface='joking'
    show Sayaka

    s "Bist du immer so stürmisch zu Mädchen, die du gerade getroffen hast?"

    "Sie kichert und streut noch mehr Salz in die bereits tiefe Wunde."

    "Na ja ...{w} Wenn sie es so haben will, dann bleibt mir wohl keine andere Wahl."

    "Dadurch mache ich mich vor all den anderen wahrscheinlich zum größten Idioten, aber ich brauche Antworten!"

    "Ich hole tief Luft.{w} Und dann ..."

    $ sayaface='shocked'
    show Sayaka
    with hpunch

    s "Wh-wha--hey, was machst du da?"

    "...Packe ich sie am Handgelenk und ziehe sie zur Tür hinaus, ob sie will oder nicht.{w} Wäre sie aber wirklich dagegen, dann könnte sie mich, angesichts der Vorführung vorhin, jede Sekunde zu Boden werfen.{w} Aber ich denke, sie albert gerade nur ein wenig herum."

    hide Sayaka
    with dissolve

    p "Und du kommst auch schön mit!"

    $ hikaface='shocked'
    show Hikari
    with dissolve

    h "Kyaa!{w} Wer hat gesagt, dass du mich berühren darfst?!"

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

    dg "...Es ist gut."

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

    h "Wie wäre es nächstes mal zu fragen, bevor du jemanden anfässt?!{w} Du hast Glück, dass wir auf einem öffentlichen Platz sind, sonst hätte ich dich in zwei Teile geschnitten!"

    s "Oh, das ist spannend!{w} Wird das jetzt einer dieser Liebesgständnisse, von dennen ich so viel ghört habe?"

    $ hikaface='embarrassed'
    show Hikari

    h "E-eh?{w} E-Ein L-Liebesgeständnis?{w} Zu wem?{w} Uns beiden?!"

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

    s "Ich weiß, ich weiß.{w} Du willst für dass alles eine Erklärung, oder?{w} Ich konnte mir einfach nicht helfen."

    $ hikaface='normal'
    show Hikari

    p "Danke ..."

    "Ich seufze und lasse meine Schultern hängen.{w} Endlich.{w} {i}ENDLICH.{/i}"

    s "So, über was wolltest du zuerst bescheid wissen?"

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

            s "Also, ich bin Sayaka und das ist Hikari.{w} Hast du schon unsere Namen vergessen, Dümmerchen?"

            "Das ist ja zum Haare ausreißen."

            "Ich öffne noch einmal meinen Mund, um ihr klar und deutlich zu sagen, was ich meine, aber es scheint, als wäre sie mir einen Schritt voraus."

            $ sayaface='smiling'
            show Sayaka

            s "Ich weiß nicht, wie viel ich dir sagen darf.{w} Wir haben schon die Regeln gebrochen, als wir uns dir gezeigt haben."

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

            "Hä ...?"

            $ hikaface='embarrassed'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            "Langsam wird ihr bewusst, was sie gerade sagte.{w} Schon amüsant zuzusehen, wie ihr für gewöhnlich mürrisches Gesicht so ganz plötzlich vor Verlegenheit rot wird."

            h "I-Ich meinte w-wichtig für uns!{w} {i}Uns!{/i}"

            $ sayaface='joking'
            $ hikaface='shy'
            show Hikari
            show Sayaka

            s "Sauber."

            "Sayaka kichert und klopft ihr auf die Schulter."

            $ hikaface='normal'
            show Hikari

            h "H-hmph!"

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

            s "Ich denke, dass meinste was wir dir sargen können...{w} Hmm..."

            s "Wir sind nicht von hier--besser gesagt, wurden wir geschickt, um dich zu beschützen."

            p "Gehört ihr einer Gruppe an?{w} Wartet, gibt es mehr von eurer Sorte?!"

            $ sayaface='joking'
            show Sayaka

            s "Eh-heh, ich hab vielleicht schon zuviel gesagt..."

            "Sie kratzt sich meinem Grinsen am Hinterkopf.{w} In der Angelegenheit werd ich wahrscheinlich nichts mehr aus ihr rausbekommen ...{w} Zumindest für heute.{w} Vielleicht erzählt sie mir morgen ja mehr, sofern ich sie überraschen kann."

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

            s "Also, in diesem speziellem Fall, sind sie es.{w} Obwohl sie eigentlich nicht so aggresiv sind.{w} Aber sie waren schon immer da und lauerten in den Schatten."

            $ sayaface='normal'
            show Sayaka

            s "Es ist wirklich komisch.{w} Ich hab noch nie einen gesehen, der sich getraut hat, am helllichten Tag anzugreifen.{w} Es ist als ob etwas es {i}wirklich{/i} aufgeregt hat.{w} Oder...vielleicht..."

            "Sie denkt nach, wodurch sie Hikari und mich ungünstig dastehen lässt, und wirft uns dabei gelegentlich einen Blick zu."

            p "Äh, Sayaka?"

            $ sayapose='school_1'
            $ sayaface='smiling'
            show Sayaka
            with dissolve

            "She snaps out of her stupor, blinking back to reality."

            s "Huh?{w} Oh, tut mir leid!{w} Keine Sorge, es ist nichts."

            p "Was hab ich verdammt nochmal getan, um diese Monster zu verärgern?"

            s "Sie haben dich nicht angegriefen weil du was getan hast, es liegt einfach daran dass du, du bist."

            p "Wer ... bin ich denn?"

            s "Yeah, dein Blu--"

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

            h "Er weiß nichts davon.{w} Es ist besser so.{w} Wie werden das Problem lösen, und endlich diese grausame Schule verlassen."

            s "Du bist nicht witzig.{w} ...Aber du hast recht.{w} Tut mir leid, Kenta."

            "Sie sieht mich entschuldigend an.{w} Und es hört sich auch so an, als würde sie es ernst meinen.{w} So, als würde sie es mir gerne sagen, es mir aber nicht sagen kann.{w} Druck auszuüben wäre jetzt wohl auch nicht richtig."

            $ q2 = True

        "Wie lange werdet ihr hier bleiben?" if q3 is False:
            "Die Frage ist ganz wichtig.{w} Wie lange, äh, wollen sie überhaupt auf mich aufpassen?"

            $ sayaface='scared'
            show Sayaka

            "Sayaka reagiert mit einem traurigen Blick auf meine Frage.{w} ... Ist die Frage wirklich so schlimm?"

            s "Es ist fast so, als ob du uns garnicht willst.{w} Sind wir so lästig??"

            "Verdammt.{w} Warum muss sie es ausgerechnet so ausdrücken?{w} Das hab ich doch gar nicht gemeint!{w} ... Glaub ich zumindest."

            "Es ist nur ...{w} Solange die beiden in meiner Nähe sind, wird mir wahrscheinlich ein Problem nach dem anderen über den Weg laufen."

            p "Ach, komm schon, so hab ich's auch nicht gemeint ..."

            "Plötzlich zeigt sie mir wieder ihr strahlendes Lächeln."

            $ sayaface='happy'
            show Sayaka

            s "Ich weiß!{w} Mit dir kann man sich einfach anlegen.{w} Ich konnte mir einfach nicht helfen!"

            "Dieses Mädchen ..."

            "Sie bricht in ein Gelächter aus.{w} Und dieses Lachen ist so laut, dass man es bestimmt in der ganzen Schule hören kann."

            $ sayaface='smiling'
            show Sayaka

            s "Wir werden hier nicht lange sein, ich verspreche es.{w} Nur bis wir alles geregelt haben."

            p "Ich schätze, ihr könnt mir nicht sagen, was ihr zuerst 'klären' müsst, oder?"

            $ sayapose='school_2'
            show Sayaka
            with dissolve

            "Sie zwinkert mir zu.{w} Dachte ich mir schon."

            s "Streng geheim und so.{w} Aber wir sind gerade dabei, etwas über dieses Durcheinander herauszufinden.{w} Es sosllte nicht lange dauern.{w} Vielleicht ein paar Tage.{w} Höchstens eine Woche!"

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

            s "Oh?{w} Es ist jetzt Zeit zurückzugehen, oder?"

            $ sayapose='school_1'
            show Sayaka
            with dissolve

            "Sie streckt ihre Arme in die Luft und gähnt."

            s "Also, ich hoffe wir konnten dir ein paar Sachen erklären."

            "...Mehr oder weniger."

            $ sayaface='happy'
            show Sayaka

            s "Komm schon, wir wollen doch nicht zuspät kommen!"

            hide Sayaka
            show Hikari at center
            with dissolve

            "Sayaka rast, so als wäre es ein Rennen, auf die Treppe zu, während ihre Partnerin hinter ihr herläuft und mir einen letzten Blick zuwirft."

            "Sie bleibt stehen und blickt einen kurzen Augenblick nach unten, ehe sie ihren Kopf wieder geradeaus richtet."

            h "Hey, umm..."

            p "Was ist?"

            $ hikaface='shy'
            show Hikari

            h "...Nichts.{w} Es ist...nichts."

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

    "Teilweise habe ich schon damit gerechnet, dass jeden Moment ein Monster durch das Fenster springt und das Klassenzimmer in ein Schlachtfeld verwandelt.{w} Obwohl ...{w} Dann wär zumindest wieder was los hier."

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

    "{i}Stampf, stampf, stampf.{/i}{w} Meine schweren Schritte hallen durch die Nacht.{w} Aber neben meinen sind auch noch andere Schritte zu hören - von zwei Personen, um genau zu sein.{w} Diese Schritte sind aber weitaus leiser als meine, und sie werden auch mit viel mehr Anmut gesetzt. "

    p "Schaut ...{w} Ich weiß, dass ihr mich nur beschützen wollt, aber müsst ihr dafür, äh, so {i}an mir kleben{/i}?"

    "Ja.{w} Die Schritte gehören zu niemand geringeren als zu meinen selbsternannten 'Schutzengeln'.{w} Sayaka links und Hikari rechts von mir.{w} Und obwohl ihre Schultern zwar Zentimeter von meinen entfernt sind, marschieren wir im Gleichschritt."

    $ hikapose='school_2'
    $ hikaface='normal'
    show Hikari
    with dissolve

    h "Sei doch nicht dumm!{w} Nachts alleine heimzugehen wäre der perfekte Moment für den Feind zuzuschlagen.{w} Hier müssen wir am meisten auf der Hut sein."

    "Huch.{w} Sie muss mir echt nicht so laut ins Ohr schreien.{w} Ich denke, wenn ich noch mehr Zeit mit ihr verbringe, werd ich noch irgendwann taub."

    $ hikaface='angry'
    show Hikari

    h "Denkst du ich {i}mag{/i} es, so nah zu sein?{w} Du solltest dankbar dafür sein, dass ich das überhaupt mache."

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

    s "Aww, sei doch nicht so, Hikari.{w} Denk nicht, ich sehe nicht wie du ihn die ganze Zeit ansiehst, wenn er wegsieht."

    "Während sie geht, lehnt sich Sayaka etwas über mich und lächelt Hikari an.{w} Leute, die Situation wird langsam echt komisch."

    hide Sayaka
    with dissolve
    $ hikaface='embarrassed'
    show Hikari
    with dissolve

    h "E-eh?{w} Du hast gesehen wie... I-Ich meine, Ich hab einfach nur nachgeguckt, ob der Gegner einen Überraschungs-Angriff durchgeführt hat!"

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

    h "W-Wie auch immer!{w} Du bist doch diejenige, die immer deine Schulter gegen ihn drückt !{w} Was versuchst du zu tuhen?!"

    "Häh?{w} Das ... hat sie getan?{w} Jetzt, wo sie's erwähnt, fällt mir ein, dass ich auf der linken Schulter wirklich ein eigenartiges Gefühl gespürt hab ..."

    hide Hikari
    with dissolve
    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Hm?{w} Ich wollte ihn nur warm halten.{w} Guck, ich {i}kümmere{/i} um seine Gesundheit und möchte nicht, dass er eine Erkältung bekommt."

    s "Er beschwert sich nicht, also muss er es ja mögen !"

    with hpunch

    "Ohne Vorwarnung hängt sie sich an meinen Arm, wodurch sie mich beinahe zu Boden drückt."

    s "Siehst du~?"

    p "H-Hey, das ist jetzt aber--"

    hide Sayaka
    with dissolve
    $ hikaface='angry'
    show Hikari
    with dissolve

    h "Was machst du?{w} Du wirst ihm noch den Arm abreißen!{w} D-Du must es sanfter machen, so wie ich..."

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

    s "Mmm.{w} Nein.{w} So machst du es auf gar keinen Fall, Hikari!{w} Es ist mehr wie..."

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

    h "Hah!{w} B-Bitte!{w} {i}Das{/i} wird so gemacht!"

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



    "Bernsteinfarbene Augen blicken voller Entschlossenheit auf uns drei herab.{w} ... Vielleicht bilde ich es mir auch nur ein, aber ihr Hauptaugenmerk scheint auf {i}mich{/i} gerichtet zu sein.{w} Sie starrt mich ja schon förmlich an."

    "All das reicht, um mir leichte Schmerzen im Hinterkopf zu verpassen{w} Und dass es mir bereits eiskalt den Rücken runterläuft, muss ich ja hoffentlich nicht extra erwähnen."

    p "Eine ... Eine Freundin?"

    "Ich zwinge mich zu einem Lachen, obwohl ich die Wahrheit schon kenne.{w} Die Atmosphäre wird immer angespannter, so wie damals mit dem Monster, und die Gesichtsausdrücke von Hikari und Sayaka lassen auf nichts Gutes rückschließen."

    s "Hah.{w} Ich hab keine Angst.{w} Kenta, komm zurück.{w} Ich mag das nicht..."

    p "Aber ...{w} Okay, okay."

    "Ich tu, was sie mir gesagt haben, und ziehe mich ein wenig zurück. Schließlich möchte ich in einer solchen Situation nicht mit ihnen zu streiten beginnen."

    s "So, mit was denkst du haben wir es hier zutun?"

    h "Sie sieht viel zu nach Mensch aus, um ein Schatten zu sein...{w} Aber, ich bekomme das gleiche Gefühl von Angst in ihrer Anwesenheit."

    s "Ahh, ich verstehe.{w} ...Ich denke.{w} ...Warte, also {i}ist{/i} sie ein Monster oder nicht?"

    h "Das versuch ich rauszufinden!{w} Wenn du für eine Sekunde aufhören würdest, in mein Ohr zu schreien, könnte ich mich konzentrieren..."

    s "Ich schreie nicht!{w} Sheesh."

    h "Richtig.{w} Ich hab's vergessen.{w} Das ist ja deine Standard-Lautstärke.{w} Also dann, sei einfach ruhig und lass mich über die Dinge nachdenken."

    s "Du bist manchmal so grausam, Hikari..."

    "Das silberhaarige Mädchen wirft mir noch einen kurzen Blick zu, bevor es sich auf die Mädchen konzentriert.{w} Und dann springt sie."

    scene town street night
    with dissolve

    "..Was?!{w} Warum ist sie gesprungen?!{w} I-Ich kann es kaum mitansehen."

    "Dort, wo meine beiden Wächterinnen stehen, stürzt sie nach unten.{w} Wofür hat sie überhaupt ihre Flügel?"

    "Sie fällt immer schneller und schneller, bis kurz darauf der Boden zum Greifen nahe ist ...{w} Ich möchte nicht zusehen.{w} Aber ...{w} irgendwie hab ich das Gefühl, als hätte sie einen guten Grund für diesen Sprung.{w} Ich {i}hoffe{/i} aber, das ist nicht der Fall."

    p "...!"

    "Nur wenige Zentimeter vor dem Aufprall breitet sie ihre Flügel aus, wodurch sie kurzerhand zum Stillstand kommt.{w} Und das geschieht von einer Sekunde auf die andere - so, als würde sie die Erdanziehungskraft komplett ignorieren."

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



    "Wenn ich versuche, mich auf sie zu konzentrieren, fängt mein Kopf wieder an zu schmerzen.{w} Hat sie ... irgendwas mit den Monstern zu tun?{w} Ich fasse mir mit einer Hand zum Kopf.{w} Es kostet mir schon extrem viel Willenskraft, aufrecht stehenzubleiben."

    dg "Guten Abend, Mädchen."

    "Sie begrüßt sie ganz lässig, als würde sie die beiden kennen.{w} Irgendwie ...{w} werd ich das Gefühl nicht los, dass sie nicht für diese Begrüßung von einem Dach gesprungen ist."

    h "...lass uns zur Sache kommen, okay?{w} Wer bist du, und was willst du?"

    $ yuzupose='magical_2'
    $ yuzuface='happy'
    show Yuzuki
    with dissolve

    dg "Bist du nicht mein feinlicher Haufen?"

    "Sie kichert und versucht nichts, die Spannung, die in der Luft liegt, zu beseitigen."

    dg "Sehr Gut.{w} Du kannst mich Yuzuki nennen.{w} was ich mein ist später...{w} Gut..."

    $ yuzuface='joking'
    show Yuzuki

    "Die Augen der Mädchen richten sich plötzlich alle auf mich. Irgendwie wird das immer merkwürdiger ..."

    y "Ich werde den Jungen nehmen, wenn es dir nichts ausmacht.{w} Siehst du, er ist {i}sehr{/i} wichtig für mich."

    $ hikaface='angry'
    $ sayaface='scared'
    show Hikari
    show Sayaka



    "...!"

    "Ich wusste es.{w} Natürlich hat sie was mit diesem Schlamassel zu tun.{w} Warum auch nicht?"

    "Heute ist wohl der Tag, an dem ich alles und jeder anscheinend tot sehen will."

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
    y "...Nein?{w} Ich denke wir müssen die Dinge auf die harte Tour machen, hmm?"

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

    s "W-wahh!"

    "Der Aufprall von Metall gegen Metall löst Funken aus.{w} Hikari konnte gerade noch rechtzeitig reagieren, wodurch sie den Schlag mit dem Schwert noch gerade so abwehren konnte.{w} Wäre dem nicht so, wären sie einen Kopf kürzer."

    h "Nnngh.{w} Ich wusste es!{w} Du bist einfach nur eine Puppe zu {i}ihr{/i}!"

    "Sie spricht zähneknirschend und versucht mit aller Kraft, den Abstand zu verkürzen.{w} Es scheint aber, als würde sie den Kampf verlieren, denn das silberhaarige Mädchen lässt sich überhaupt keine Anstrengungen anmerken."

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

    s "Huh?{w} Oh, richtig!"

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

    y "Ah, das macht so viel Spass! {w}Und da dachte ich, dass die kleinen 'Wächter' dieses Jungen tatsächlich eine Bedrohung darstellen könnten. {w} Wie dumm von mir!"

    h "S-Sei ruhig!{w} Es ist noch nicht vorrüber!"

    "Mit Leichtigkeit und einem wahnsinnigen Gesichtsausdruck schwingt sie ihre Sense.{w} Die Mädels können den Schlägen entweder nur ganz knapp ausweichen oder aber sie werden von Hikari geblockt."

    "Der Kampf ist komplett einseitig ...{w} Und das war bereits zu erwarten, als das Mädchen ihren ersten Zug gemacht hat."

    "Sie kann es ohne Probleme mit beiden aufnehmen und blockt jeden Angriff, den Hikari versucht, und immer wenn Sayaka versucht, sie auf Distanz zu halten, jagt sie ihr hinterher."

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

    h "Oof!"

    "Sie fallen beide ziemlich benommen aufeinander."

    "Obwohl sie sichtbare, blaue Flecken haben, scheinen sie zum Glück nicht allzu schwer verletzt zu sein."

    p "G-Geht es euch gut?!"

    "Nicht länger in der Lage, das alles zu ertragen, begebe ich mich aus meiner Deckung und bewege mich schreiend auf sie zu."



    "Als sich die Augen des silberhaarigen Mädchens auf mich fixierten, bleibe ich wie eingefroren stehen.{w} Ihr Blick ist beängstigend.{w} Lähmend.{w} Sie hat es auf mich abgesehen.{w} Genauso wie auch das Monster."

    "Klebt auf meinem Rücken etwa ein Zettel, auf dem 'Bringt mich bitte um' steht?!"

    h "Was machst du, du Idiot?!{w} Bleib zurück!{w} W-wir sind ...-- argh -- uns geht es gut!"

    "Hikari bringt mich mit einem lauten Schrei wieder zur Besinnung.{w} Schwer vorstellbar, dass es ihnen gut geht, wenn man sie so ansieht ...{w} Wild um sich schlagend, versuchen sie beide aufzustehen."

    play music "bgm/mischiefintro.ogg"
    queue music "bgm/mischiefloop.ogg"

    s "Ist das mein Bein oder seins?{w} Ich kann es nicht sagen!"

    h "Ow!{w} Schlag es nicht!{w} Das wird nichts lösen!"

    s "Ohh...{w} Also war es {i}dein{/i} Bein.{w} Okay, ich verstehe es!"

    h "Warum schlägst du es immer noch?!"

    h "Aber...{w}geh einfach von mir runter!{w} Nnghh, du bist so schwer!"

    s "S-Schwer?{w} Ich?!"

    h "Ja, du!{w} Wenn du nicht so ein Vielfraß wärst, wären wir vielleicht nicht in dieser Situation!"

    s "Es ist nicht meine Schuld, dass ich es liebe zu essen!{w} Ich denke, du bist einfach neidisch dass ich so viel esse und nicht zunehme."

    s "I've seen what happens when you pig out, Hikari.{w} It's like, you triple in size!"

    h "E-Entschuldige?!{w} Du hast Glück, dass ich nicht an mein Schwert komme, oder ich würde..."

    h "Ow!{w} Hast du mich gerade gebissen?!"

    s "Mmm.{w} Du kannst nichts beweisen!"

    h "D-Du bist so eine Wilde!"

    "Das ist eine totale Katastrophe ..."

    stop music fadeout 1.0

    "Da meine vermeintlichen Wächter noch immer versuchen, wieder auf die Beine zu kommen, bin ich der auf mich zukommenden Yuzuki hilflos ausgeliefert.{w} Sie macht langsame und kleine Schritte und hinterlässt bewusst den Anschein, als würde sie meine Furcht genießen."

    scene town street night
    $ yuzupose='magical_2'
    $ yuzuface='joking'
    show Yuzuki at center
    with dissolve
    play music "bgm/evilgirlintro.ogg"
    queue music "bgm/evilgirlloop.ogg"
    y "Jetzt sind sie aus dem Weg...{w} Lass uns ein bisschen Spass haben, sollen wir?"

    "{i}Klopf.{w} Klopf.{w} Klopf.{/i}{w} Wenn das so weitergeht, springt mein Herz noch aus meinem Körper."

    "Ich sollte wegrennen.{w} Aber ich kann nicht.{w} Warum kann ich nicht?{w} Ich habe überhaupt keine Kontrolle mehr über meinen Körper."

    "Der Abstand zwischen uns ist gleich Null.{w} Wird sie mich umbringen?{w} ...Warum mich?{w} Womit hab ich das bloß verdient?!{w} Ich mein, bis vor kurzem hab ich noch ein ganz normales Leben geführt."



    "Je näher sie kommt, desto stärker werden meine Kopfschmerzen.{w} Die Luft um mich herum ist erdrückend.{w} Selbst der einfache Akt des Atmens fällt mir in diesem Zustand viel zu schwer."



    "Ihre bernsteinfarbenen Augen werden schmaler.{w} Sie packt ihre Sense immer stärker."

    p "W--...{w}Warum ...?"

    y "Oh, es ist nichts persönliches.{w} So müssen die Dinge sein, wenn ich mein Leben wieder auf Kurs bringen will."
   
    $ yuzupose='magical_1'
    $ yuzuface='angry'
    show Yuzuki
    with dissolve

    y "Jetzt.{w} Sag Gute Nacht."

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

    "Mit einem Blick auf die Stelle, auf der Hikari und Sayaka lagen, sehe ich, dass die beiden wieder auf ihre Beine gekommen sind.{w} Sayaka hat ihre Hand ausgestreckt und lässt Rauchwolken aus ihren Fingern aufsteigen.{w} Da bin ich ihr wohl was schuldig."

    $ sayaface='normal'
    show Sayaka

    s "Das war zu nah.{w} Ich...{w} ich denke es ist Zeit für einen 'taktischen Rückzug, oder?"

    $ hikaface='shocked'
    show Hikari

    h "Eh?{w} Werden wir wirklich einfach rennen?!{w} Ich kann noch --nggh-- {w} Ich kann noch kämpfen!"

    s "Oh, shush!{w} Du kannst kaum stehen.{w} Komm schon!"

    hide Hikari
    hide Sayaka
    with dissolve

    "Während sich unsere Gegnerin von diesem Angriff noch immer zu erholen scheint, nutzen meine Retter diese Möglichkeit, um sich bei mir neu zu formieren. Gleichzeitig lösen sich langsam ihre Waffen aus und setzen sich auf ihren Rücken wieder zu Flügeln zusammen."

    p "W-Wartet, was macht ihr?"

    s "Halt dich gut fest, okay?"

    "Bevor ich noch irgendein Wort sagen konnte, heben beide vom Boden ab und ...{w} steigen auf.{w} Hinauf.{w} In die Luft.{w} Wir ...{w} Wir fliegen.{w} Wir FLIEGEN verdammt nochmal."

    p "Was?!{w} Hey, nein, lasst mich runter!{w} Können wir nicht einfach weglaufen?!"

    with hpunch

    h "Hör auf herumzuprügeln, wir werden fallen, du Idiot!"

    p "Da mach ich nicht mit!{w} Das ist verrückt!{w} Uff.{w} Ich ...{w} Ich ...{w} Ich glaub, ich muss kotzen."

    h "Hey, wag es nicht, oder du wirst dir wünschen, du wärst noch da unten bei diesem Freak eines Mädchens!"

    "Wir ziehen weiter durch den Himmel und durchdringen die Wolken, als ob es das Natürlichste der Welt wäre."

    "Der Wind weht an mir vorbei, unten in der Stadt flimmern die Lichter und ...{w} die Unruhe, die sich ergibt, da ich von den beiden getragen werde ...{w} Mir wird schlecht.{w} Ich weiß nicht, ob ich das noch viel länger ertragen kann."

    s "Denkst du wir haben sie verloren?"

    "Sie schalten um zu einem sanften Schwebeflug und halten mich fest in der Hand - hoffe ich zumindest - ehe sie sich kurz umdrehen, um zu bemerken, dass sie fürs Erste ein wenig durchatmen können."

    h "Ich denke schon.{w} ...Ich kann nicht glauben, dass wir fliehen mussten."

    s "Hey.{w} Hey.{w} Wir sind nicht {i}geflohen{/i} okay.{w} Es war ein 'taktischer Rückzug'!"

    h "Ugh.{w} Nenn es so wie du willst, aber wir hatten Glück dass wir unsere Köpfe intakt gehalten haben."

    "...Während das Paar in Gedanken versinkt, übernimmt die Stille das Geschehen."

    p "Also, äh ..."

    s "Huh?{w} Kenta?{w} Oh, ich hab dich fast vergessen, sorry!"

    "Das macht mir ein bisschen Angst ...{w} Wenn man bedenkt, dass ihr die einzigen seid, die mich vor einem schmerzhaften und grausamen Tod bewahren!"

    s "Du bist nicht verletzt, oder?"

    p "Nein, mir geht's gut.{w} Es ist nur ...{w} Könntest du mich, äh, du weißt schon ..."

    with hpunch

    p "MICH RUNTERLASSEN?!"

    s "Richtig, richtig.{w} Ich denke, es ist jetzt sicher.{w} Los gehts!"

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

    h "Glaubst du, ich hab es genossen dich so lange festzuhalten?"

    p "Okay, okay, ich versteh schon.{w} Hört bloß auf ...{w} mich zu tätscheln.{w} Urghh ..."

    "Sayaka kreist umher und beugt sich nach vorne, um mich besorgt anzusehen."

    $ hikaface='normal'
    $ sayaface='shocked'
    show Sayaka
    show Hikari

    s "Whoa, ich denke ich hab noch nie jemanden so Grün anlaufen sehen!{w} Du bist kein großer Fan vom fliegen, oder?"

    p "Ach, echt jetzt? Wie kommst du darauf?"

    "Ich brauche eine Weile, um mich wieder ordentlich aufrichten zu können.{w} Okay.{w} Ich denke, es geht wieder."

    $ sayaface='normal'
    show Sayaka

    "Während ich mich erholte, sah es so aus, als hätten Sayaka und Hikari bis tief in die Nacht Wache gehalten.{w} Aber es sieht so aus, als sie die Verfolgung nicht aufnehmen möchten.{w} Komisch."

    p "Okay, ich weiß, dass ich euch seit unserem ersten Treffen nur Fragen gestellt hab, aber--"

    s " Falls du dich fragst wär das komische Mädchen ist, hab ich wirklich keine Ahnung."

    p "Bist du dir da sicher?{w} Sie sieht genauso aus wie ihr.{w} Ihr wisst schon, wie eine Zauberin, und mit Flügel ..."

    $ sayaface='angry'
    $ hikaface='angry'
    $ hikapose='magical_1'
    show Sayaka
    show Hikari
    with dissolve

    "...Ups.{w} Da hab ich wohl was Falsches gesagt.{w} Sie drehen sich beide mit Feuer in den Augen zu mir.{w} Selbst die sonst so lockere Sayaka scheint jetzt wütend auf mich zu sein."

    h "Hast du uns damit verglichen...{w}dem Ding?!"

    p "Ahh, das wollte ich nicht--"

    with hpunch

    h "Es gibt eine Welt aus Unterschieden zwischen uns, und was auch immer sie war!"

    h "Zum einen, hast du nicht {i} ihre {/i} Augen gesehen?{w} Sie war komplett verrückt .{w} Es gab keine Spur von Vernunft."

    $ hikaface='scared'
    show Hikari

    "Hikari wickelt ihre Arme um sich selbst, um ein Frösteln abzuwehren."

    h "Schon allein an sie zu denken, macht mir Angst."

    $ sayaface='normal'
    show Sayaka

    s "Ich schätze, aus deiner Perspektive, Kenta, könnte sie genauso aussehen wie wir...{w} mit ihrem allgemeinen Aussehen und wie ihre Magie zu funktionieren scheint."

    s "Aber alles an ihr ist komisch.{w} Die schwarzen Schatten, die schwarzen Flügel, sogar diese Hörner!{w} Es ist so, als würden sie das komplette Gegenteil von dem sein, was wir sind."

    s "Nicht einmal ihr Magie ist natürlich..."

    $ hikaface='normal'
    show Hikari

    p "Äh, und ... welche Kraft hast du?"

    $ sayaface='smiling'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Natürlich!{w} Wir haben hart dafür gearbeitet, um heute hier zu sein!{w} Es ist nicht so, als ob wir so geboren wurden!"

    $ sayaface='normal'
    show Sayaka

    s "Bei ihr ist es so, als wäre es nur so..."

    "Tief in Gedanken versunken verstummt sie.{w} Mein Gott, ich versteh kein bisschen.{w} Ich weiß nur, dass diese Monster nicht das einzige sind, vor dem ich mich fürchten muss."

    "Anscheinend fertig mit dem Nachdenken, kommt Sayaka wieder zurück zur Realität und lächelt."

    $ sayaface='smiling'
    show Sayaka

    s "Ich denke, wir hatten sowieso genug Aufregung für einen Tag.{w} Wie wäre es jetzt, wenn wir dich wieder heimbringen?"

    "Sie streckt ihre Hand aus, um mich am Arm zu nehmen, aber ich springe einen Schritt zurück.{w} Ich weiß schon, was sie vorhatte!"

    $ sayaface='shocked'
    show Sayaka

    p "Bitte nicht nochmal fliegen!{w} Wir gehen, okay?{w} Wir GEHEN!"

    $ sayaface='happy'
    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "Aww.{w} Wenn du dir sicher bist.{w} Es ist viel sicherer im Himmel."

    "Natürlich!{w} Ich kann froh sein, dass ich beim letzten Mal keinen Herzinfarkt bekommen hab."

    "Völlig erschüttert nach all den Ereignissen von heute, machen wir uns auf den Weg nach Hause."


    stop music fadeout 4.0
    scene bg black
    with fade

    "Es dauert nicht lange, bis wir bei mir ankommen.{w} Und ich kann mit Freude sagen, dass wir keine Monster oder Mädchen mit Sensen mehr begegnet sind.{w} ... Ich kann nicht glauben, dass ich mich jetzt jeden Tag darum sorgen muss.{w} Was ist nur aus meinem Leben geworden?!"

    "Als ich die Haustüre erreiche, werde ich jedoch vor einen Problem gestellt.{w} Diese beiden Mädchen bestehen darauf, mich zu beschützen, und waren gerade dabei, mich nach drinnen zu begleiten ... In MEIN Zuhause."
    play music "bgm/ominousintro.ogg"
    queue music "bgm/ominousloop.ogg"
    "Irgendwie hab ich das Gefühl, als wären meine Eltern nicht wirklich damit einverstanden.{w} Es sind schließlich Mädchen.{w} Außerdem würde das nur noch mehr Fragen aufwerfen, und darüber hinaus will ich meine Eltern nur ungern da mitreinziehen."

    "Es dauerte also eine Weile und {i}jede Menge{/i} Verhandlungsgeschick, aber letztendlich konnte ich sie doch irgendwie überzeugen, dass ich zu Hause in Sicherheit bin."

    "Schlussendlich zogen sie sich für die Nacht zurück und gaben mir dadurch etwas Zeit für mich selbst.{w} Wobei sie gesagt haben, sie wären nicht allzu weit weg, sollte etwas sein ...{w} und das bereitet mir Sorgen."

    scene kitchen night
    with fade

    "Ich schließe die Türe und kollabiere fast, da mich selbst die letzte Kraft, die ich noch irgendwie aufbringen konnte, anscheinend verlassen hat."

    p "Was für ein Tag."

    "Mein Kopf und meine Arme tun weh.{w} Meine Beine fühlen sich an, als würden sie jeden Augenblick den Geist aufgeben.{w} Ich kann nicht glauben, dass ich noch immer stehen kann."

    "Der Geruch von Essen liegt und in der Luft und das reicht aus, um mir das Wasser im Mund zusammenlaufen zu lassen.{w} Ah.{w} Genau.{w} Ich hab heute noch gar nichts gegessen.{w} Wenn ich den morgigen Tag überleben will, sollte ich das schnellstmöglich nachholen."

    "Anscheinend bin ich gerade noch rechtzeitig, da meine Eltern gerade das Essen hergerichtet haben."

    "Dieses kurze Zeitfenster am Abend ist die einzige Chance, mit meinen Eltern zu essen - abgesehen von Ferien.{w} Aus dem Grund schätze ich jedes dieser Abendessen und versuche ihnen immer Gesellschaft zu leisten."

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

    "Als ich die Vorhänge schließe, werden meine Augen von einem bernsteinfarbenen Leuchten im Garten angezogen.{w} Ein Feuer.{w} Ein Lagerfeuer, um genau zu sein.{w} Du hast drei Möglichkeiten, um zu erraten, zu wem das Feuer gehört."

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

    h "W-Was zum Teufel gaffst du hier?{w} Schließ die Tür!"

    p "'Tschuldige, mein Fehler ..."

    scene bg black
    with fade

    "Völlig durcheinander knall ich die Tür wieder zu.{w} Das war echt knapp."

    "...Warte mal 'ne Sekunde.{w} Irgendwas stimmt hier nicht."

    scene cg3
    with dissolve

    "Ich öffne die Tür noch einmal und der Anblick raubt mir den Atem ... Und das, obwohl ich schon wusste, was mich erwartet ..."

    h "Ahh!{w} Was machst du jetzt?!{w} Du Perversling!"

    "Ich wusst ees!{w} Es {i}ist{/i} Hikari!{w} Eine, äh ...{w} eher unangemessen gekleidete Hikari noch dazu.{w} Sie ist genauso überrascht wie ein Reh, das von einem Scheinwerfer angeleuchtet wird."

    "Schenkt man den Socken, die sie gerade auszieht, keine Aufmerksamkeit, trägt sie nur ihre extravagante Unterwäsche.{w} Hm, das passt echt alles zusammen."

    "So wie sie sich nach vorne beugt, können meine Augen nicht anders, als auf ihre--"

    with hpunch

    h "Kenta!"

    p "H-Häh?"

    "Ihr schriller Ton reißt mich aus der Benommenheit, falls es überhaupt eine solche war.{w} Was ...{w} Was wollte ich nochmal machen?"

    h "Was machst du?! Mach jetzt endlich die Tür zu!"

    p "Warte.{w} Wartewartewarte.{w} Sollte ich nicht dir die Frage stellen, was {i}du{/i} in {i}meinem{/i} Haus machst?!"

    h "Wie siehts wohl aus, du Genie?!{w} Jetzt geh weg!"

    "Ihr Gesicht ist knallrot.{w} Sie bebt fast schon vor Wut, obwohl sie immer noch wie eingefroren am selben Fleck steht.{w} Aber warum bin ich hier der Schuldige?"

    p "Hey, werd jetzt bloß nicht wütend!{w} Ich kann mich nicht erinnern, dass ich euch die Erlaubnis gegeben hab, mein Haus zu betreten.{w} Und erst recht nicht meine Dusche!"

    h "SCHLIEß{w} DIE{w} TÜR."

    p "Erst, wenn du--"

    with hpunch

    h "{i}SCHLIEß{w} DIE{w} TÜR!{/i}"

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

    "Sayaka grinst so fröhlich wie immer, während Hikari so aussieht, als wolle sie nach dem nächstgelegenen, scharfen Objekt greifen und mich in Stücke schneiden.{w} Ich sag's noch einmal ... WARUM ist das meine Schuld?!"

    p "So ...{w} Findet ihr nicht, dass ihr mir eine Erklärung schuldig seid?"

    s "Hmm?"

    "Sie neigt den Kopf zur Seite und sieht mich verwirrt an.{w} Och, jetzt komm schon!{w} Wie kommt's, dass ich der einzige bin, der das als merkwürdig empfindet?"

    p "Na ja, ich mein ...{w} Was macht ihr bei mir Zuhause?{w} Und warum benutzt ihr mein Eigentum!?"

    $ sayaface='happy'
    $ sayapose='school_2'
    $ hikaface='normal'
    show Hikari
    show Sayaka with dissolve

    s "Oh, das ist einfach!{w} Als wir dich beobachtet haben, haben wir herausgefunden, dass deine Eltern schon früh am Morgen gehen und sonst niemand hier lebt"

    s " Also haben wir uns gedacht...{w}Du weißt schon, die Dusche und ein paar Sachen leihen."

    p "...Um es anders auszudrücken, ihr seid eingebrochen."

    $ sayaface='joking'
    show Sayaka

    s "Eh-heh-heh-heh, das ist ein extremer Weg um dass zu sagen.{w} Wir haben sichergestellt, dass das Fenster wieder repariert ist!"

    p "WIE BITTE?!"

    "Ich werfe schnell einen Blick auf alle sichtbaren Fenster.{w} Zumindest ist keines kaputt ...{w} Mein Gott, haben sie etwa einen Stein durch irgendein Fenster geworfen?{w} Und ich dachte, Leute, die die Magie beherrschen, wären schlauer!"

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

    h "Kenta, unsere Magie ist nicht einfach nur ein bequemes Werkzeug, dass wir es sorglos im Alltag benutzen können!"

    "Hikari spricht endlich mal wieder und scheint über ihre üble Laune hinweg zu sein."

    h "Es braucht schon viel Energie, um etwas einfaches wie Fliegen zu tun .{w} Und wir müssen immer sicherstellen, dass wir genung Energie auf Reserve haben, im Falle eines Überaschungsangriffs wie letzte Nacht."

    h "Glaubst du wirklich, es wäre eine kluge Idee, diese kostbare Energie für sowas zu verschwenden, das mit einer Dusche so leicht gemacht werden kann?"

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

    s "Oh, du must dir darüber kein Kopf machen!{w} Lass {i}uns{/i} Frühstück machen!{w} Sieh es als Entschuldigung an, für das Chaos hier.{w} Richtig, Hikari?"

    $ hikaface='shocked'
    show Hikari at right
    show Sayaka at left
    with dissolve

    "Sie zieht Hikari am Arm heran."

    h "W-Was?{w} Ich war nicht einverstanden--"

    s "Richtig, Hikari?"

    with hpunch
    $ hikaface='scared'
    show Hikari

    "In einer fast schon bedrohlichen Tonlage verstärkt sie ihren Griff."

    h "O-ow, okay!"

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

            s "Du wirst es nicht bereuen!{w} Leh dich einfach zurück wir werden im Handumdrehen etwas Wunderbares für dich kochen!"

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

            s "Wir werden uns darum später kümmern!{w} Jetzt mach das dazu!"

            "...I'll pretend I didn't hear that."

            "Zusätzlich höre ich auch noch das hektische Zerschneiden von Gemüse - und Hikaris panischen Schrei."

            h "Pass auf, wo du das hinschwingst, du wirst noch meinen Kopf abschlagen!"

            s "Es ist okay."

            h "B-Bist du dir sicher, dass es dazu passt?"

            s "Natürlich!{w} Ich hab ein kreatives Auge für sowas."

            h "...Soll es Grün werden?"

            s "Uh."

            s "Mmhmm!"

            h "Also werden wir es einfach so machen, wie das?"

            "Dann höre ich das beunruhigende Auflodern der Flammen.{w} Wie stark drehen sie die Kochplatte bitte auf?!"

            s "Hmm.{w} Was denkst du was dieses Zeugs ist?"

            h "Ich habe keine Ahnung."

            s "Ach egal, hauptsache es geht rein!"

            "..."

            "Auf einmal wird es in der Küche still.{w} Ich weiß nicht, ob das gut oder schlecht ist.{w} Ich traue mich ja nicht mal nachzusehen."

            h "I-Ist es wirklich in Ordnung?"

            s "Yup!{w} So soll es--"

            with hpunch

            s "Wahhh!"

            "Und mir nichts, dir nichts, explodiert auf einmal etwas.{w} Dicke Rauchschwaden breiten sich aus.{w} Hmm."

            h "Mach es aus, schnell, es wird sich ausbreiten!"

            s "Wie mach ich das?!"

            h "I-Ich weiß es nicht!{w} Probier es einfach!"

            "Das Geräusch von tosendem Feuer.{w} Im Augenwinkel sehe ich etwas Aufflackern.{w} {i}Hmmmm{/i}."

            s "Nein!{w} Das macht es schlimmer!"

            h "Wie wäre es...{w}damit?!"

            s "Vielleicht!{w} Es hat vielleicht funktioniert!"

            s "...oder nicht.{w} Keine Magie mehr, okay?"

            h "Dieses Mal wird es funktionieren--"

            s "Keine Magie mehr!"

            h "Ich weiß sonst nicht, was ich tuhen soll!"

            s "Hyah!"

            h "A-ah, du bekommst es überall!"

            "Spritzendes Wasser.{w} Und noch dazu jede Menge."

            h "Ist es...{w}ist es vorbei?"

            s "Hahhh...{w} Ich denke!{w} Und guck, das Essen ist fertig!"

            h "Ich denke wirklich nicht, dass--"

            s "Ich sagte--das Essen ist fertig!"

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

                    s "Es ist mega oder?"

                    "Sayaka lehnt sich erwartungsvoll nach vorne."

                    "So schmeckt also Holzkohle."

                    "Ich wehre mich gegen den Drang, mich zu übergeben, und lächle ihr zu."

                    p "M-Mmm!"

                    $ sayapose='school_1'
                    show Sayaka
                    with dissolve

                    s "Wirklich?{w} Ja, ich wußte es!{w} Du solltest uns {i}jeden{/i} Morgen für dich kochen lassen!"

                    "Oh Gott.{w} Was hab ich bloß getan?{w} Und von dem ganzen Zeug gibt's noch einen ganzen Teller voll!{w} Diese Mädchen sind für meine Gesundheit und für mein Wohlbefinden eindeutig eine Gefahr."
                "Weigere dich, das zu essen. Ich möchte nicht sterben!":

                    "Okay, ja, also nein.{w} Ich muss hier endlich mal Stellung beziehen, sonst wird es nur noch schlimmer."

                    p "Schau, es tut mir leid, Sayaka, aber ich krieg das echt nicht runter."

                    $ sayaface='normal'
                    show Sayaka

                    s "Huh?{w} Warum nicht?"

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

                    s "U-uhh, ich hab schon gegessen."

                    p "Schau, warum versuchst du--"

                    $ sayaface='happy'
                    show Sayaka

                    s "Aber. Ich weiß dass Hakari nichts gegessen hat!{w} Sie kann dir zeigen, wie sicher und lecker ist!"

                    $ hikaface='shocked'
                    $ hikapose='school_2'
                    hide Sayaka
                    show Hikari at center
                    with dissolve

                    h "E-eh?{w} Ich?!"

                    "Noch immer in auflauernder Position, springt Hikari plötzlich, als ihr Name in Zusammenhang mit dem Essen, bei dem sie mitgeholfen hat, es zum Leben zu erwecken, erwähnt wurde."

                    $ sayaface='smiling'
                    show Sayaka at left
                    show Hikari at right
                    with dissolve

                    s "Yeah!{w} Komm rüber und zeig Kenta, wie gut es schmeckt!"

                    h "Das kann nicht dein Ernst sein.{w} Das Zeug ist--"

                    s "Totall sicher und essbar!{w} Jetzt komm rüber.{w} Bitte."

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

                    h "Wir haben es geschafft...{w}also kann es nicht so schlecht sein.{w} Es ist einfach nur ein bisschen ...{w}knusprig."

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

                    h "Oops!{w} Ich bin ja so tollpatschig.{w} Meine Hand ist wohl...{w}ausgerutscht.{w} Was eine Schande!{w} Und ich habe mich schon {i}so{/i} gefreut alles zu essen."

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

                    s "Oh naja.{w} Wie wäre es wenn ich mehr mache?"

                    $ sayaface='shocked'
                    show Sayaka
                    with hpunch

                    p "Nein!"

                    "Ich springe auf, wobei ich meinen Stuhl fast schon mitnehme.{w} Ich mach mir echt Sorgen um mein Haus!"

                    "Vielleicht etwas lauter als beabsichtigt, erwische ich sie unvorbereitet."

                    s "H-huh?"

                    p "Ich mein, wir würden zu spät zur Schule kommen, wenn ihr noch was kochen würdet."

                    s "Oh...{w} Du hast recht.{w} Guck auf die Uhr!"

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

            s "Okay.{w} Du weißt wirklich nicht, was du verpasst!{w} Mir wurde schon gesagt, das mein Essen'speziell' ist!"

            $ hikaface='scared'
            show Hikari

            h "Sayaka, ich denke nicht, dass sie meinten--"

            $ sayaface='happy'
            show Sayaka

            s "In der Tat, sie sagten, ich sollte nie wieder kochen, weil ich andere Leute damit neidisch machen würde!{w} Kannst du das glauben?"

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

    h "Aber was ist wenn--"

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

    s "Ah, keine Sorge.{w} Sie hat dass immer gemocht.{w} Gib ihr einfach Ziet bis sie, uh, ein weniger grimmiger ist."

    s "Sie hat nur deine Sicherheit im Kopf und macht sich Sorgen, was passieren würde, wenn sie weg wäre."

    s "Heck, würde es nach mir gehen, würde ich dich nicht einmal zur Schule lassen.{w} Wir würden dich einfach in einem kleinen, schönen Raum lassen und warten, bis alles vorbei ist."

    "...Ich bin mir nicht sicher, dass sie gemerkt hat, wie beängstigend sich das gerade angehört hat, wenn ich den Grinser in Betracht ziehe."

    $ sayaface='smiling'
    show Sayaka

    s "Du hast recht.{w} Vielleicht {i}haben{/i} wir dich ein bisschen erstickt.{w} Ich denke, wir können es uns leisten, wenigstens während der Schule zu entspannen."

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

    s "Was gibts, Kenta?{w} Wollen wir nicht essen gehen?"

    p "Ich hol mir mein eigenes Essen.{w} Ihr müsst nicht an mir kleben.{w} Ihr habt doch bestimmt auch andere Dinge zu erledigen, oder?"

    $ sayaface='normal'
    show Sayaka

    s "Aber wir sind--"

    p "Was weiß ich!{w} Irgendetwas.{w} Scheißegal was!{w} Ich hab euch erst gestern kennengelernt, und ihr seid schon so anhänglich.{w} Ich hätte gern etwas Platz für mich selbst!"

    "Ich bin echt dankbar, dass sie hier sind.{w} Anderenfalls hätte ich den gestrigen Tag bestimmt nicht überlebt.{w} Aber das hier grenzt ja an Stalking.{w} Und vom Camping in meinem Garten möchte ich gar nicht erst anfangen!"

    $ sayaface='smiling'
    show Sayaka

    s "Oh, okay.{w} Ich versthe.{w} Hikari verstehts auch.{w} Denke ich."

    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Hmph."

    s "Komm schon, Hikari!{w} Es macht bestimmt Spaß, die Schule zu erkunden.{w} Wir hatten vorher keine Zeit, um uns mal umzugucken!"

    "Sie war nie in der Schule ...?{w} Wo kommen die beiden denn sonst her?{w} Desto mehr ich mit ihr rede, desto mehr hört sich das für mich nach einem Alien an."

    s "Also dann, Kenta.{w} Wir machen jetzt einfach unsere eigene Sache.{w} Schrei einfach wenn du uns brauchst und versuch nicht zu streben!"

    hide Sayaka
    show Hikari at center
    with dissolve

    "Und so marschiert sie los und summt dabei eine fröhliche Melodie vor sich hin.{w} Hikari folgt ihr hinterher, aber nicht, ohne mir einen letzten eisigen Blick zuzuwerfen.{w} ... Irgendwie frieren meine Schultern auf einmal.{w} Brrr."

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

            h "Huh?"

            "Ihre Augen fixieren sich wieder auf die Stelle, die sie vor einem Moment noch beobachtet hatte."

            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "Ja.{w} Obwohl die Schule selbst bisher friedlich war, weiß man nie, wann der Feind zuschlagen könnte."

            p "Danke.{w} Ich weiß es zu schätzen."

            $ hikaface='shy'
            show Hikari

            h "E-Es ist kein Problem.{w} Ich mach das für die Sicherheit der Schule, nicht nur für dich !"

            "Ihr Gesicht zeigt einen interessanten Ton von Rosa.{w} Es braucht echt nicht viel, um sie aus der Fassung zu bringen, was?"

            p "Klar, schon gut.{w} Ich hab schon verstanden."

            $ hikapose='school_2'
            $ hikaface='angry'
            show Hikari
            with dissolve

            h "Denn während Sayaka und ich den Anstand haben, unsere Kräfte vor normalen Menschen zumindest zu verbergen, kann ich nicht sagen, dass die Schatten dasselbe tun werden. Es ist schon schlimm genug, dass sie versucht haben, dich am helllichten Tag anzugreifen."

            $ hikaface='normal'
            show Hikari

            h "Ich versteh es einfach nicht.{w} Es widerspricht allem, was wir bisher über sie wissen."

            "Sie seufzt pathetisch und dreht sich wieder um, um wieder über die Schule zu wachen."

            $ hikaface='embarrassed'
            show Hikari

            "Ich öffne meinen Mund, um ihr etwas zu sagen, aber ein leises, rumpelndes Geräusch unterbricht mich dabei."

            p "...Hikari?"

            h "J-Ja...?"

            "Sie antwortet, ohne sich umzudrehen.{w} Es war nicht sonderlich schwer, um zu erkennen, was das für ein Geräusch war."

            p "Hast du, äh, noch nicht gegessen?"

            "..."

            "Stille.{w} Da hab ich den Nagel wohl auf den Kopf getroffen."

            $ hikaface='normal'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "Es ist nicht meine Schuld!{w} Diese Cafeteria ist so laut und dreckig, dass ich keinen weiteren Moment darin ertragen kann. {w} Ich weiß nicht, wie Sayaka da unten freiwillig essen kann."

            h "Ich hab sowieso wichtigere Sachen zu tuhen."

            p "Und kannst du mit einem leeren Magen auch kämpfen?"

            h "Natürlich!{w} Wer denkst du--"

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

            h "Ich würde lieber verhungern...{w}als..."

            $ hikaface='scared'
            show Hikari

            "{i}Gruuuu{/i}.{w} Ihr Magen bettelt förmlich nach Nahrung."

            h "O-okay, fein.{w} Vielleicht ein bisschen."

            with hpunch
            $ hikaface='normal'
            $ hikapose='school_2'
            show Hikari
            with dissolve

            "Ich breche die Hälfte vom Sandwich ab und gebe es ihr, ehe sie es mir noch widerwillig aus der Hand reißt."

            h "Danke dir.{w} I-Ich nehme an."

            "Ich glaube nicht, dass sie es gewohnt ist, so was zu sagen.{w} Wir machen endlich Fortschritt!{w} Da muss ich doch glatt lächeln."

            $ hikaface='angry'
            show Hikari

            h "Wisch dieses ekliche Grinsen aus deinem Gesicht.{w} Ich weiß nicht, an was du denkst, aber ich bin mir sicher dass es etwas Unanständiges ist."

            "Sagt sie mit einem Knurren, bevor sie ihren Teil des Sandwichs mit den Zähnen zerfleischt."

            p "Und, gut?"

            $ hikaface='normal'
            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "...Es ist okay.{w} Nicht das beste was ich hatte, aber auch nicht das schlechteste. Zurück an der Akadmie, ich-"

            $ hikaface='shocked'
            show Hikari

            "Sie hört kurz auf zu essen und macht große Augen.{w} Ich glaube, da hätte sie beinahe etwas ausgeplaudert.{w} Ich wünschte wirklich, sie würden daraus nicht so eine Art Staatsgeheimnis machen."

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

            "Huch."

            "Trotz ihrer kleinen Figur, komme ich mir dank ihrer dominanten Stimme immer wieder wie eine Maus vor.{w} Sofern ich nicht so enden möchte wie das Monster, sollte ich nicht versuchen, noch mehr Infos aus ihr rauszubekommen."

            p "Okay, okay!{w} Ich hab überhaupt nichts gehört.{w} War ...{w} wohl nur der Wind oder so"

            $ hikaface='normal'
            show Hikari

            "Sie seufzt und wirft ihr Haar zur Seite, wobei die Wut genauso schnell verschwand, wie sie aufgebaut wurde."

            h "Wir halten keine Informationen zurück, um einfach nur mysteriös zu sein, weißt du."

            "Verarsch doch jemand anderen!"

            h "Es ist...{w}der einfachere Weg.{w} Es hat keinen Sinn, dich in dieses Durcheinander zu ziehen, wenn wir ihm helfen können.{w} Es ist kein Leben, dass ich jemandem wünsche..."

            "Und obwohl sie noch immer kaut, wird ihr Gesichtsausdruck immer düsterer - wahrscheinlich deshalb, weil das Sandwich immer kleiner wird.{w} Ich bin mir nicht mal sicher, ob sie überhaupt weiß, dass sie gerade isst."

            "Sie denkt ein paar Momente über etwas nach, bevor sie mich mit einem ernsten Blick ansieht."

            h "Kenta, was würdst du tuen wenn du..."

            "Eine Gruppe von Schülern taucht plötzlich mit Essen in der Hand auf dem Dach auf.{w} Hikari hingegen wird mucksmäuschenstill und kehrt wieder zu ihrem Wachposter zurück."

            $ hikapose='school_1'
            show Hikari
            with dissolve

            h "...Vergiss es.{w} Es ist nich wichtig."

            p "Wenn du, äh, meinst."

            "Es {i}sah{/i} extrem wichtig aus, wenn ich bedenke, dass sie mich sonst nie so ernst angesehen hat.{w} Was für ein Gluck, dass die ausgerechnet jetzt auftauchen müssen."

            "Jeder Anschein eines Gesprächs ist jetzt vernichtet.{w} In der Gegenwart von anderen Menschen scheint sie viel zurückhaltender zu sein.{w} Und ich denke auch, dass das, worüber wir geredet haben, nicht für diese Ohren gedacht ist."

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

            s "Hey!{w} Ich dachte du wolltest ein bisschen Zeit ohne uns?"

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

            s "Es ist okay, du kannst zugeben, dass du mich {i}so{/i} arg vermisst hast und keinen weiteren Moment, ohne mich aushalten konntest.{w} Ich werde es nicht Hikari erzählen."

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

            s "Ich sagte, sie mag nicht all die Menschenmengen und den Lärm, also ging sie alleine davon und murmelte etwas über die Suche nach einem ruhigeren Ort."

            p "Glaubst du, dass es ihr gut geht?"

            s "Mff--warscheinlich."

            $ sayaface='happy'
            show Sayaka

            "Und noch ein Bissen.{w} Die Hälfte von dem Essen, das noch da war, als ich ankam, ist schon weg.{w} Wo versteckt sie das in ihrem Körper bloß?"

            $ sayaface='smiling'
            $ sayapose='school_1'
            show Sayaka
            with dissolve

            s "Ich denke wir werden es wissen, wenn ihr etwas zustößt.{w} Oder besser gesagt, die ganze Schule wird Bescheid wissen.{w} Sie wird unglaublich stark, wenn sie wütend wird!"

            p "Das hört man gerne.{w} ... Hoff ich zumindest."

            "Heißt also, wenn die komplette Schule in Aufruhr verfällt, dann ist Hikari was passiert."

            p "Äh, wie gefällt es dir hier?{w} Wenn ich mich recht erinnere, hast du doch gesagt, dass du noch in einer Schule warst, oder?"

            $ sayaface='happy'
            show Sayaka

            s "Oh, ja!{w} Es ist super.{w} Jeder ist so freundlich und das Essen ist {i}super{/i}!"

            "Als ob sie das besonders hervorheben wollte, sticht sie mit einem fast leuchtendem Gesicht in ihr Essen."

            $ sayaface='smiling'
            show Sayaka

            s "Und vielleicht hätte ich es besser formulieren sollen.{w} Es ist nicht so als ob ich und Hikari nie zur Schule gegagen wären...{w} Wir waren halt nicht...{w}also, auf einer normalen."

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

            s "Es ist etwas, wo ich nicht gerne nochmal tuhen würde.{w} Lass uns einfach dass sagen."

            s "Magie ist nicht etwas, was du an einem Tag lernst.{w} Es sind Jahre von studieren, Training und--"

            $ sayaface='scared'
            show Sayaka

            "Sie schließt ihren Mund und schlägt ihre Hand drüber, als wolle sie versuchen, sich davon abzuhalten, noch mehr auszuplaudern.{w} Verdammt.{w} Sie hat's bemerkt."

            $ sayaface='smiling'
            show Sayaka

            s "Whoops!{w} Ich dummy.{w} Das war knap."

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

            s "Das ist sowas wie ein Vollzeitjob, also hab ich nicht so viel zeit für mich.{w} Ich bin mir nicht sicher, ob es viel gibt, was ich dir erzählen kann, ohne dass die Jungs zuhause zu Hause, böse werden."

            s "Aber, weißt du..."

            "Mit einem kleinen Lächeln lässt sie ihren Blick über die Cafeteria schweifen."

            s "Der Auftrag, dich zu beschützen, war eine der entspanntesten Aufgaben, die wir bisher hatten."

            $ sayaface='happy'
            show Sayaka

            s "Uns wurde die Chance gegeben, hier in der Schule etwas zu lernen und ein normales Leben zu führen."

            "Na ja ...{w} Ich bin mir nicht sicher, ob man das wirklich als 'anmelden' bezeichnen kann."

            $ sayaface='smiling'
            show Sayaka

            s "Nur in der Lage zu sein, sich zurückzulehnen und die Dinge leicht anzugehen...{w}wie ein normales Mädchen.{w} Ich hätte nicht gedacht, dass ich jemals dazu in der Lage sein würde."

            s "Weißt du, ich werde alles hier vermissen, wenn erstmal alles gereglt ist."

            $ sayaface='normal'
            show Sayaka

            "Sie verstummt.{w} Tief in ihren Gedanken verloren.{w} Ich hätte nie gedacht, dass sie der Typ wäre, der über so was so sehr nachdenken würde."

            "'Wie ein normales Mädchen' ...{w} Heißt das, dass sie ihren Lebensstil nicht mag?{w} Ich kann schon einsehen, dass es mit der Zeit anstrengend werden kann, immer gegen diese Monster zu kämpfen."

            "Aber sie hat diesen Lebensstil doch gewählt, oder?{w} Zumindest bin ich fest davon überzeugt.{w} Ich kann sie aber auch nicht fragen, schließlich wird sie mir heute erstmal keine Fragen mehr zu dem Thema beantworten."

            with Pause(2.5)

            "..."

            s "Hey, Kenta?"

            $ sayaface='smiling'
            $ sayapose='school_2'
            show Sayaka
            with dissolve

            p "Ja?"

            "Ihre glitzernden Augen und funkelnden Lippen bringen mein Herz zum Rasen.{w} Warum habe ich bloß das Gefühl, dass sie mich gleich etwas Wichtiges fragen wird?"

            s "Wirst du das noch...{w}essen?"

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

    "Im Vergleich zu gestern scheinen sie deutlich angespannter zu sein.{w} Aber das kann ich ihnen nicht übel nehmen.{w} Wir hatten Glück, dass sie uns nicht verfolgt hat - sonst würde ich jetzt womöglich nicht mehr leben."

    "Die Reise nach Hause verläuft still und die Gesichter der Mädchen spiegeln ihre Entschlossenheit wider.{w} Sie scheinen bereit zu sein, beim geringsten Anzeichen von Gefahr loszustürmen, von daher möchte ich ihre Konzentration nicht unterbrechen."

    "Die Sonne auf dem Weg vor uns geht allmählich unter.{w} Großartig.{w} Desto größer unsere Schatten werden, desto angespannter werde ich."

    "Ich halte an.{w} Irgendwas stimmt hier nicht ..."

    s "Kenta?{w} Was ist los?"



    "Nicht schon wieder.{w} Wieder diese verdammten Kopfschmerzen."

    "Warte.{w} Hatten diese Kopfschmerzen nicht immer etwas gemeinsam?{w} Normalerweise treten sie tagsüber nie auf, außer--"



    y "Ah, pünktlich.{w} Du machst das wirklich leicht, weißt du?"

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

    s "Kenta, komm zurück!"

    p "Schon gut.{w} Ich weiß, wie das funktioniert, okay!?"

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

    y "Ich muss sagen, ich bin überrascht, dass du überhaupt kämpfen willst.{w} Ich dachte, du würdest einfach wieder den Schwanz drehen.{w} Ich nehme an, dass die Dinge auf diese Weise mehr Spaß machen!"

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


    "Hikari nickt und stürzt sich auf Yuzuki, bevor diese den ersten Schritt machen kann.{w} Sayaka fliegt eine weitere Strecke nach hinten und hält bereits einen Pfeil in ihrem Bogen bereit.{w} Erlebe ich hier etwa ...{w} Teamplay?{w} Vielleicht wird das ja doch noch was."

    y "Es ist alles nutzlos!"

    "Yuzuki reagiert blitzartig und wirbelt mit ihrer Sense herum, die auf Hikaris Schwert prallt.{w} Eine Schockwelle breitet sich in der Straße aus und zerstört Scheiben und Straßenschilder."

    "Das erinnert mich teilweise an den letzten Kampf.{w} Yuzuki hat den Vorteil der rohen Gewalt, weshalb sie zweifellos zurückschlagen wird.{w} Aber Hikari scheint kein bisschen nervös zu sein.{w} Im Gegenteil, sie scheint sogar selbstsicher!"

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

    y "U-ugh.{w} Woran denkst du, dass du spielst?!"

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

    h "W-Was...?"

    "Hikari ist genauso verwirrt wie ich.{w} Das Mädchen ist nirgends zu sehen.{w} Dort, wo sie stand, treibt nur noch eine einzelne Feder umher.{w} Sie ist einfach ...{w} verschwunden."

    "Ein fieses Kichern ertönt aus den Schatten.{w} Hat sich Yuzuki etwa ...{w} teleportiert?{w} Oder ist sie so schnell ausgewichen, dass es niemand mitbekommen hat?"

    $ hikaface='scared'
    show Hikari

    "Hikari springt auf das Geräusch zu und wirft Sayaka dabei einen wilden Blick zu."

    $ hikaface='shocked'
    show Hikari

    h "Sayaka, sieh o--"

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

    s "Ahh!{w} D-Das ist schlecht!{w} Ich...{w}ich kann so nicht kämpfen!"

    s "Ohh, was mach ich jetzt?!"
    stop music fadeout 4.0
    "Hikari scheint wirklich sehr verärgert zu sein, als sie zu ihr eilt, und das, obwohl diese Situation eigentlich für ihre Partnerin beunruhigend sein sollte."

    h "Komm schon, hör auf herumzualbern!"

    "Sie stampft auf den Boden und schimpft ihre halbnackte Partnerin.{w} Ziemlich merkwürdig, jemanden so zu behandeln, der sich gerade in einem solchen Zustand befindet."

    h "Du weißt verdammt gut, dass du dein Outfit regenerieren kannst."

    "Hä ...?{w} Das kann sie?{w} Warum hat sie sich dann so verhalten?"

    s "Ahhh, das ist so b--...{w} Huh?{w} Oh.{w} Richtig!"

    scene town street night
    $ sayaface='joking'
    $ hikaface='angry'
    show Sayaka at left
    show Hikari at right
    with flash
    play music "bgm/mischiefintro.ogg"
    queue music "bgm/mischiefloop.ogg"

    "Mit einem weiteren Leuchten sieht ihre Kleidung wieder so aus wie vorhin.{w} Hm.{w} Das ging ja wirklich schnell."

    s "Eh-heh-heh...{w}mein Fehler.{w} Ich hab es voll vergessen."

    "Hikari legt ihr Schwert über ihre Schulter und seufzt."

    h "Weißt du, ich denke ein Teil von dir {i}wollte{/i} sich so zeigen.{w}Vielleicht zu jemanden speziellem..."

    s "Ich?{w} Niemals!{w} Obwohl, du ja 'Ausversehen' die Tür aufgelassen hast--"



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

    "... Oder vielleicht auch nicht.{w} Das Monster ist ihr einen Schritt voraus und versucht ihre Hände zu fesseln.{w} Die Tentakel schleichen sich immer näher an sie heran und träufeln eine ätzende Substanz auf sie, die bereits mehr als die Hälfte von ihr bedeckt."

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

    "Zuhause angekommen trennen sich unsere Wege ...{w} Wobei, ich weiß ja, dass sie nur einen Katzensprung entfernt sind, da sie sowieso wieder in meinem Garten campen werden.{w} ... Ich versteh echt nicht, wie sie es schaffen, nicht entdeckt zu werden."

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

    "Ich ziehe die Vorhänge zusammen und ignoriere die Tatsache, dass mein Garten jederzeit in Flammen aufgehen könnte.{w} Ich bin viel zu müde, um mir darüber Sorgen zu machen.{w} Wird schon schiefgehen.{w} Höchstwahrscheinlich."

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
            "Ich denk darüber nach. Okay, fertig mit dem Denken. Nein.":

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

    "A familiar voice catches my attention.{w} Finally!"

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
        "Hikari, of course!":


            $ hikari += 1

            p "Na ja, ich schätze ...{w} Hikari."

            h "E-eh?!"

            "Ihr Gesicht wird noch roter, was eigentlich gar nicht mehr möglich sein sollte."

            h "D-Du kannst das nicht so meinen..."

            s "Siehst du?{w} Ich hab es dir gesagt!{w} Selbst Kenta kann nicht anders, als dich anzuschauen."

            s "Du und dein perfekter Körper!"

            "Sayaka kichert und fängt an, Hikari zu kitzeln."

            h "Ahh--haha--s-stop, k-kitzel mich nicht d-da!"

            "Hikari versucht ihr Bestes, nicht lachen zu müssen.{w} ... Meine Anwesenheit haben sie anscheinend komplett vergessen."

            s "So ... neidisch!"

            h "O-okay, das reicht...{w} Du kannst jetzt aufhören, S-Sayaka!"

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

            s "Garnichts...?"

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

            s "Kenta!{w} Du solltest besser hier rüberkommen.{w} Wir haben Jahre gebraucht, um diese..."

            p "Nop.{w} Ich steh gerade echt auf der Leitung.{w} Worum geht's denn?"

            $ sayaface='angry'
            show Sayaka

            s "Es...{w}es ist egal."

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

    s "Siehst du?{w} Ist es nicht das beste?{w} Und zu denken, dass ihr nicht hier raus wolltet!"

    "Bin ich froh, dass sich zumindest eine amüsiert.{w} Aber es ist echt zu heiß.{w} Hikari scheint mit mir mitzufühlen, wenn man betrachtet, wie sie im Schatten rumliegt."

    $ sayapose='bikini_2'
    show Sayaka
    with dissolve

    s "Hmm, was machen wir alls erstes...?"

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

    s "Oh, gut gemacht!{w} Schmeiß es wieder zurück!"

    "Ich werfe ihr den Ball zu.{w} Er segelt so irgendwie durch die Luft ... Gerade so weit, dass sie ihn fangen kann.{w} Das war jetzt peinlich."

    "Sayaka klammert sich um den Ball und denkt darüber nach, was man damit am Besten machen kann.{w} Zuerst schaut sie mich kurz an, ehe sie zur eingeschlafenen Hikari blickt."

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

    s "Ich sagt dass du es fangen sollst, Hikari!{w} Ich hab dir eine faire Chance gegeben und so."

    "Sayaka seufzt übertrieben ... Mit einem alarmierenden Schimmer in ihren Augen{w} ... War das die Rache für vorhin?{w} Ich sollte mir merken, mich nie mit Sayaka anzulegen."

    $ hikaface='normal'
    show Hikari

    h "Was?{w} Ich erinnere mich nicht..."

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

    p "Komm schon!"

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

    s "Hmm?{w} Was gibts?"


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
    h "Nein!{w} Schau, untem im Wasser!{w} Siehst du es nicht?"

    "Hä?{w} Im Wasser?"

    "Warte ...{w} War das Wasser schon immer so dunkel?"

    "Moment mal ... Das ist doch ..."

    p "Ist das ein Schatten?!{w} Der ...{w} ist ja riesig!"

    "Unter dem Wasser kommt langsam etwas auf uns zu.{w} Kann mir dieser Wahnsinn nicht mal einen Tag erspart bleiben?!"

    "Etwas, was man nur als gigantische Masse an Schlamm bezeichnen kann, türmt sich allmählich vor uns auf."

    "Eine groteske Kreatur, die plötzlich etwas öffnet, von dem  ich denke, dass es die Augen sind.{w} Mittlerweile verdeckt sie selbst die Sonne.{w} Die Kreatur ist mindestens so groß wie ein Gebäude, wenn nicht sogar noch größer!"

    p "Und dagegen wollt ihr kämpfen?{w} ... {i}Könnt{/i} ihr dagegen überhaupt kämpfen?"

    scene cg18
    with dissolve


    "Das Wesen rückt immer näher.{w} Ich kann mir keine einzige herkömmliche Waffe vorstellen, die dagegen etwas anrichten kann."

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

    s "Na denk darüber nach.{w} Das Ding ist groß.{w} Und sie ist dabei, mit einer Explosion reiner Magie, den Kern zu treffen.{w} Was denkst du, was passieren wird?"

    "Wie zur Hölle soll ich so was denn wissen?"

    p "Häää ...?"

    "Sayaka sighs, before she slaps her hands together."
    play music "bgm/mischiefintro.ogg" fadein 2.0
    queue music "bgm/mischiefloop.ogg"
    s "Es wird BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM machen!{w} Explosion!{w} Diese Arten von Schatten sind sehr flüchtig, wenn Sie ihr Magie vermischen."

    p "Das ist mir zu hoch.{w} Ist das nicht gut?{w} Ein Monster weniger, um das wir uns Sorgen machen müssen."

    $ sayaface='joking'
    show Sayaka

    s "Sieh einfach zu."

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



    s "Meine Güte, das ist ziemliches durcheinander."

    "Sayaka chirps, as she slinks from behind the rock too, a grin across her face."

    h "S-Sayaka, nicht einmal..."

    s "Ich frage mich, was sie von all dem zu Hause denken würden, hmm?"

    h "Ich habe nich nachgedacht!{w} Denn Strandball den, du nach mir geworfen hast..."

    "Sayaka clicks her tongue and nimbly evades the slime across the sand as she approaches her partner, still bearing the same smug look."

    s "Entschuldigungen, entschuldigungen!{w} Ich hätte nicht gedacht, dass einer der besten Schüler so einen Fehler machen würde."

    h "Es ist nicht meine Schuld!"

    "Wait...{w}something doesn't make sense."

    p "Sayaka."

    s "Hmm?"

    p "Wenn du wusstest, dass das passiert, warum hast du sie dann nicht aufgehalten?"

    s "Ah, ein guter Punkt.{w} Ich hätte...{w}aber..."

    s "Wo ist da der Spaß?"

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

    s "Aww, komm schon.{w} Es ist nur ein bisschen Wasser.{w} Du wirst daran nicht schmelzen oder so."

    $ sayaface='joking'
    show Sayaka

    "Sayaka grins dangerously as something sparkles in her eyes.{w} Uh-oh..."

    s "Es ist weniger schädlich als das Zeug, das du gestern abbekommen hast."

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    "She tries her best to suppress a giggle, but fails, her laughter soon rocking the house.{w} Conversely, Hikari is less than amused."

    $ hikaface='embarrassed'
    show Hikari

    h "S-Sayaka!{w} Können wir das jetzt endlich vergessen?{w} Ich war dumm, ich hab ein Fehler gemacht.{w} Große Sache!"

    "Flustered, Hikari stomps a foot towards her mischievous partner.{w} We haven't even reached school yet, and they're already arguing!{w} I think that's a new record."

    h "Und außerdem weiß ich noch, dass {i}du{/i} es warst, die kurz davor war mit deinen Mätzchen von der Akademie ausgeschlossen zu werden."

    $ sayaface='joking'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Eh-heh-heh...{w} Sie mögen einfach keine guten Witze"

    $ hikaface='angry'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Scherz?!{w} Du hast fast alles in die Luft gespr--"

    "Realising I am indeed still in the room, Hikari cuts herself short and clamps up.{w} Aww.{w} I guess I'll never be able to hear about this old school of theirs.{w} The 'magic' one that taught them all they know."

    h "Belassen wir es doch jetzt einfach dabei und ich stimme dir zu, dass wir beide einmal dumm waren, okay?"

    $ sayaface='smiling'
    show Sayaka

    s "'Kay.{w} Ich denke wirklich nicht dass es so schlecht war..."

    $ hikaface='north'
    show Hikari

    s "Egal, Kenta, wie wäre es wenn ich etwas koche--"

    $ sayaface='shocked'
    show Sayaka

    p "Nein!{w} Sicher nicht!"

    s "Aber du hast mich nichtmal--"

    p "Brauch ich nicht.{w} Wenn es darum geht, dass du in der Küche das Essen anrührst, egal in welcher Farbe, Form oder sonst was, gibt's nur eine richtige Antwort."

    $ sayaface='scared'
    show Sayaka

    s "Dieses mal wird es wirklich--"

    p "Nop."

    s "Ich werde aufpassen--"

    p "Nööö."

    $ sayaface='angry'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Aww, du bist--"

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

    s "Whew.{w} Es war ziemlich intenisv da draußen!"

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

    h "Vergiss es."

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

    s "Kenta?{w} Bist du okay?"

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

    s "Wir gehen uns essen holen, Kenta.{w} Willst du mit uns kommen, oder...?"

    "Having hopped out of her seat, Sayaka skips to the front of my desk and peers down at me with a grin."

    "I blink.{w} It takes me a good second to register that anything has been said to me."

    p "Häh ...?{w} Oh.{w} Geht ihr ruhig vor.{w} Mir tut gerade mein Kopf ein bisschen weh ..."

    $ sayaface='normal'
    show Sayaka

    "Sayaka offers a sympathetic look when I mention the headache."

    s "Kenta, wegen den Kopfschmerzen..."

    s "Die sind..."


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

    y "Ich kann auch ein Geist sein."

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

    s "Wahh!{w} Kenta!{w} Was auf Erden ist passiert?!"

    "Oh.{w} I guess Sayaka came to check up on me since I was taking too long to get to the cafeteria.{w} I turn to meet her with a faint smile, my hair dripping wet."

    p "Ich, äh ..."

    "If I tell her Yuzuki is here, or that I went to confront her on my own, she might worry needlessly, so I'll keep it a secret for now."

    p "Alles in Ordnung, mach dir keine Sorgen."

    s "Nichts?!{w} Kenta, du bist komplett Nass!{w} Was hast du gemacht?"

    p "Ich war eigentlich schon draußen, um was zu holen, hab aber vor lauter Eile meinen Regenschirm vergessen.{w} Aber mir wird schon nichts passieren!"

    p "Ah ...{w} Hatschi!"

    "Okay, the sneeze isn't really doing me any favours."

    $ sayaface='smiling'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Komm schon, lass uns dich abtrocknen.{w} Du wirst dich noch erkälten.{w} Hikari wird ausflippen wenn sie dich so sieht!"

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

    s "Vielleicht sollten wir ihn verhören?{w} Ich bin mir sicher, er würde nicht ohne einen guten Grund hier hereinkommen!"

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

    s "Also das ist dein Zimmer, oder?{w} IEs ist schön, es endlich von innen sehen zu können, nachdem ich es die ganze Zeit ausgespäht habe."

    "...I'll pretend I didn't hear that."

    h "Es ist überraschenderweise ordentlich..."

    p "Okay, also ...{w} Wollt ihr mir endlich erzählen, was hier los ist?"
    play music "bgm/everydayintro.ogg" fadein 5.0
    queue music "bgm/everydayloop.ogg"
    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Hmm, ich frag mich was Kenta so auf seinem Computer hat..."

    "Sayaka reaches over and prods at my laptop."

    p "L-Leute, konzentriert euch, okay?"

    $ sayaface='smiling'
    show Sayaka

    s "Hmm?{w} Oh, richtig, ja!"

    "Thank you..."

    $ sayaface='normal'
    $ sayapose='school_1'
    show Sayaka
    with dissolve

    "Sayaka sits up straight and takes on a serious expression.{w} One that I wasn't even sure she was capable of."

    s "Wir wollten es dir wirklich eerzählen, Kenta.{w} Das wollten wir nicht geheim halten..."

    s "Wir dachten nur, wir könnten die Dinge alleine bewältigen, bevor wir dich auf alles einlassen."

    s "Aber wie du von dieser Yuzuki Person gehört hast, ist die Zeit jetzt wirklich knapp."

    $ hikaface='angry'
    show Hikari

    h "Was ich dir {i}immernoch{/i} nicht glauben kann, dass du uns bisher nichts davon erzählt hast.{w} Weißt du, in welche Gefahr du dich gebracht hast, als du sie getroffen hat?!"

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

    s "Er hat einen guten Standpunkt, Hikari."

    $ hikaface='angry'
    show Hikari

    h "S-Stell dich nicht auf seine Seite!{w} Du sollst {i}mein{/i} Partner sein!"

    p "So, alles, was ich immer hör, ist, dass die Zeit davonläuft ...{w}Aber warum?{w} Was passiert morgen?"

    $ hikaface='normal'
    $ sayaface='normal'
    show Hikari
    show Sayaka

    s "Der Start etwas sehr schlimmes."

    p "Ach, echt jetzt?!{w} Jetzt hört endlich auf mit diesem mysteriösen Schwachsinn!"

    $ sayaface='scared'
    show Sayaka

    s "Schrei mich nicht an, Kenta.{w} Sheesh.{w} Komm runter, ich wollte es gerade sagen!"

    "I may have lost it a little there...{w} I pull back from her, and quiet down."

    $ sayaface='smiling'
    $ sayapose='school_2'
    show Sayaka
    with dissolve
    play music "bgm/seriousintro.ogg" fadein 2.0
    queue music "bgm/seriousloop.ogg"

    s "Sag mir Kenta, was hälst du von deiner Blutslinie?{w} Deine Vorfahren?"

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

    s "Aber...{w}wegen deinem Blut wurden wir gesendet.{w} Wenn es in die falschen Hände gerät--nammens Yuzuki's--wären wir alle in großen Schwierigkeiten."

    p "Warum {i}mein{/i} Blut ...?{w} Was ist daran so besonders?"

    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Es ist vielleicht ein bisschen scher zu glauben aber, du bist...{w}nun, du bist der Nachkomme einer langen Reihe von Magiern - Menschen mit magischen Fähigkeiten."

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

    s "Also, will die Welt weiß generell nicht mehr, was Magie ist.{w} Es ist einfach in alten Geschichts-Büchern verloren gegangen.

    s "Also, wissen viele Leute, mit dieser Blutlinie, nicht einmal dass sie Magier sind.{w} Es ist nur etwas, das jetzt schlummert."

    p "Okay.{w} Wenn also viele Leute dieses ...{w} Magierblut in sich tragen, warum ist meines dann so besonders?{w} ... Was macht es so wertvoll?"

    $ sayapose='school_1'
    $ sayaface='happy'
    show Sayaka
    with dissolve

    s "Ich bin froh, dass du gefragt hast!"

    "Sayaka hops to her feet from the bed, taking me by surprise.{w} This girl can't sit still for more than a minute, I swear!"

    $ sayaface='smiling'
    show Sayaka

    s "Ich werde dich nicht mit der ganzen Geschichte langweilen, darum fasse ich mich kurz."

    "She clears her throat, as if this were a school presentation she had been been practicing for."

    s "Vor hunderten von Jahren, als die Magie noch in der Welt vorherrschte, gab es einen Magier mit ungeheurer Macht."

    s "So viel Macht, dass sie {i}der{/i} Magier zu der Zeit war.{w} Jeder hat zu ihr aufgesehen und sie war eine Inspiration für alle."

    s "Aber, du weißt ja was bei den Leuten passiert, die die größte Macht der Welt haben, oder?"

    $ sayaface='normal'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    "She frowns, and lets out a sigh."

    s "Sie wollen immer mehr Macht."

    s "Es verändert Leute.{w} Verdierbt sie."

    s "Also wollte sie über alles herschen.{w} Über jeden {i}einzelnen{/i}."

    s "All der Respekt wo die Leute vor ihr hatten, wurde zu Furcht.{w} Und sie wurde Kraut auf dem Land."

    s "Überall, wohin sie ging, folgte die Dunkelheit und breitete sich über das Land aus, während sie ihrer Eroberung folgte"

    "This is getting pretty lengthy...{w} And why do I feel like I know this person she's talking about...?"

    $ sayaface='smiling'
    show Sayaka

    s "Bist du noch dabei, Kenta?"

    "She leans forward and raises an eyebrow as I let out a yawn."

    p "H-Häh?{w} Ja, total!{w} Glaub ich zumindest ..."

    p "Und was hat diese Person mit mir zu tun?"

    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Ich bin gleich da, gosh!"

    $ hikaface='joking'
    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "Im Grunde bist du mit der Person verwandt, die den Mut hat, sich gegen die dunkle Königin zu stellen und sich an ihre Stelle setzt."

    $ sayaface='shocked'
    show Sayaka

    s "H-Hikari!{w} Warum musstest du ihn spoilern?!"

    $ hikaface='angry'
    show Hikari

    h "Wenn du die ganze Geschichte erzählst, werden wir hier noch bis zum Sonnenaufgang sitzen!{w} Und Zeit ist hier essentiell."

    $ sayaface='normal'
    show Sayaka

    s "Aww...{w} Ich wollte es dramatisch sagen und so."

    p "Äh, danke, Hikari."

    $ hikaface='normal'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Hmph."

    p "Und...{w}Weiter?{w} Mein Vorfahre hat diese böse Königin getötet?"

    h "Wenn er es getan hätte, würden wir nicht hier sein und ein Gespräch führen."

    h "Nein, mit all der Macht, die sie hatte, war es unmöglich sie zu töten.{w} Ich würde nicht so weit gehen zu sagen, dass sie unsterblich war ... {w} aber ich bin mir sicher, dass es ziemlich nah dran ist."

    $ sayaface='happy'
    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Das beste was man machen konnte, war sie zu versiegeln.{w} Es war das stärkste Sigel, was er machen konnte.{w} Was uns zurück zu diesem magischen ol Blut führt, das in dir ist, Kenta."

    s "Im Wesentlichen band er sein Schicksal mit ihr, wenn er sie wegsperrte.{w} Ein Siegel, das so mächtig ist, dass es nur freigeschaltet wird, wenn eine strenge Bedingung erfüllt wird!"

    p "Und ...{w} wie lautet die?"

    $ hikaface='angry'
    show Hikari

    h "Ich denke, dass solltest du jetzt schon wissen!"

    p "Lass mich raten ... Es hat etwas ...{w} mit meinem Blut zu tun, stimmt's?"

    $ hikaface='normal'
    $ sayaface='smiling'
    show Hikari
    show Sayaka

    s "Bingo!{w} Ihr Siegel wird nur dann wirklich entriegeln, wenn es in Kontakt mit dem Blut desjenigen kommt, der sie weggesperrt hat, oder im Nachhinein, eines seiner Nachkommen."

    $ sayapose='school_1'
    show Sayaka
    with dissolve

    s "Nun, eigentlich nicht nur {i}irgendein{/i} Nachkomme.{w} Es muss einer sein, der latente magische Kraft in sich hat."

    p "Das heißt dann also ..."

    s "Ich meine, dein Vater ist sicher und die Schatten haben keine Interesse an ihm.{w} Er hat {i}etwas{/i} Magie in seinem Blut aber, es ist nicht genug, um irgendwelche Fähigkeiten zu aktivieren."

    "Huh...{w} That's pretty convenient."

    $ sayaface='normal'
    show Sayaka

    "Sayaka stretches and lets out a tiny yawn.{w} It must have been exhausting for her to focus on one subject for so long.{w} But I think things are finally starting to make sense..."

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

    s "Kenta, deine Kopfschmerzen..."

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

    s "Also wird unser Job noch schwierieger."

    p "Das ...{w} Das ist nicht gut, oder?"

    s "Sehr!"

    $ sayaface='smiling'
    $ hikaface='normal'
    show Sayaka
    show Hikari

    s "Was uns zu unserer nächsten Sache bringt."

    s "Als wir zuerst beauftragt wurden, auf dich aufzupassen, mussten wir uns nur um einen oder zwei schattenhafte Schatten kümmern, wenn sie plötzlich entschlossen waren, instinktiv zu handeln."

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Und das war einfach genug.{w} Du hattest keine Idee das sie exestieren und wir haben uns auch, von dir, ferngehalten."

    s "Und dann fingen die Dinge an, schlecht zu werden...{w}als du den Schatten gesehen hast...{w}wir waren wirklich überrascht!"

    s "Es war, als ob es auf einer Mission war, und rutschte vollkommen an unserer superwachen Wache vorbei."

    h "Wenn ich mich zurückerinnere, war das nicht der Tag, wo du auf das Sandwich bestanden hast--"

    $ sayaface='happy'
    show Sayaka

    s "Nein!{w} Wir waren immer wachsam!"

    "Hmm...{w} I guess I was even luckier than I thought that they had managed to save me back then."

    $ sayapose='school_1'
    $ sayaface='smiling'
    show Sayaka
    with dissolve

    s "Als wir gezwungen waren, uns dir zu zeigen, war klar, dass etwas nicht stimmte.{w} Überhaupt nicht."

    s "Und dass war noch offensichtlicher, als uns Yuzuki angegriffen hat.{w} Er hatte eine Kraft, die wir noch nie gesehen haben!"

    $ hikapose='school_2'
    show Hikari
    with dissolve

    h "Wir haben nachgesehen als Freizeit war...{w} Das ist selten, wenn es darum geht, auf dich aufpassen zu müssen."

    "Well excuse me for existing!"

    h "Und es wurde schnell klar, dass sich die Dinge nicht lösen würden, wenn wir erst einmal erfahren hätten, dass dieses Siegel an Ort und Stelle langsam geschwächt ist."

    $ sayaface='normal'
    show Sayaka

    s "Wir müssen ihr Gefängnis erneuern.{w} Es verstärken, sodass sie kein Einfluss auf diese Welt mehr hat."

    s "Aber, wenn es so einfach wäre...{w} hätten wir es schon selbst gemacht."

    "Sayaka pulls a complicated expression...{w} I don't think I'm going to like what she has to say next."

    s "Kenta...{w} Wir...{w}wir brauchen deine Hilfe."

    p "M-Meine?!{w} Wie zum Teufel soll ich helfen?{w} Ihr habt doch die Zauberkräfte, nicht ich!"

    h "Es ist nicht gerade ideal, dass wir uns auf dich verlassen müssen, ich weiß, aber wir haben keine Wahl. {w} Und wir haben keine Zeit mehr, nach alternativen Mitteln zu suchen."

    $ sayapose='school_2'
    show Sayaka
    with dissolve

    s "Grundsätzlich, da das Siegel von jemandem in deiner Blutlinie erstellt und direkt mit ihnen verbunden wurde, kann es nur durch jemanden verstärkt werden, der das gleiche Blut trägt."

    $ sayaface='scared'
    show Sayaka

    s "Ich meine, technisch gesehen könnten  {i}wir{i} das Siegel, zerbrechen und sie in eine neue Falle verwickeln ...{w} Aber ich denke nicht, dass wir lange genug durchhalten würden, um das zu tun."



    "So, in other words, I'm really the only solution here.{w} I'm...{w}I'm not sure how to take this."

    p "Ich hab von diesem Magier-Zeugs überhaupt keinen Plan.{w} Bin ich dazu überhaupt in der Lage?"

    $ sayapose='school_1'
    $ sayaface='normal'
    show Sayaka
    with dissolve

    "Sayaka takes a moment to ponder things, a finger held to her chin as her eyes run over me."

    s "Erinnerst du dich an die Nacht, als Hikari mit diesem Tentakelschatten Spaß hatte??"

    $ hikaface='embarrassed'
    $ hikapose='school_1'
    show Hikari
    with dissolve

    h "Ich hatte {i}kein{/i} Spaß!"

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

    h "So durchdrungen, dass jemand, der nicht in der Lage war, diese Menge an Magie zu kontrollieren, versuchen würde, sie auszuüben..."

    $ sayaface='smiling'
    show Sayaka

    s "Sie würden explodieren.{w} Die Magie war zu viel für sie."

    p "B-BUMM?"

    s "Also, vielleicht explodieren.{w} Aber es würde zumindest ein unordentliches Ende bringen."

    s "Und da du immer noch stehst, nachdem du das Ding herumgeschwungen hast, ist es sicher zu sagen, dass du das Potenzial in dir hast."

    "Yikes...{w} I can't believe there was the possibility of...{w}exploding from picking up her sword.{w} What I did back then was even more reckless than I realised!"

    $ sayaface='happy'
    show Sayaka

    s "Also, wenn du mit diesem Schwert umgehen kannst, denke ich, dass ein wenig Versiegelungsmagie kein Problem sein sollte!"

    h "Aber dann, bedeutet es auch, dass wir dorthin gehen müssen, wo sie versiegelt ist...{w} und die eine Sache mitnehmen, die sie seit Jahren beghert."

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

    h "Ich denke, du musst ein Tag in der Schule überspringen müssen, Kenta."

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

    s "Du wirst es tun?!"

    "Sayaka looks ecstatic as she claps her hands together.{w} Was she not expecting me to help?{w} Hikari looks equally surprised.{w} Jeez, a little faith goes a long way, guys!"

    p "Das ist das Mindeste, was ich tun kann, nachdem ihr immer euer Leben für mich riskiert habt.{w} Es ist egal, wie ich euch helfen kann, Hauptsache ich kann helfen!"

    h "Kenta..."

    $ sayaface='joking'
    show Sayaka

    s "Du hättest gerade fast cool geklungen.{w} Fast!{w} Ich denke, wir müssen eán deinem heroischen Dialog arbeiten."

    $ hikaface='normal'
    $ sayaface='normal'
    show Hikari
    show Sayaka

    s "Aber dass muss später sein.{w} Es gibt viel zu tun, wenn du diese dunkle Königin besiegelst, also pass auf!"
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

    s "Gut'n Morgen.{w} Hast du gut geschlafen?"

    p "Wenn ich daran denke, was mich erwartet ... Ja."

    $ hikapose='magical_2'
    show Hikari
    with dissolve

    h "Achte darauf, gut zu essen bevor wir gehen.{w} Du wirst die Kraft brauchen."

    "Right, right.{w} Of course.{w} I start for the kitchen and prepare the most simple food I can think of."

    p "Was ich gestern ganz vergessen hab zu fragen ...{w} Wo ist diese 'Königin' überhaupt gefangen?"

    $ sayaface='normal'
    show Sayaka

    s "Häh?{w} Haben wir das nicht besprochen?{w} Sie ist gleich außerhalb der Stadt versiegelt."

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

    h "Und nachdem können wir endlich heimgehen, nachdem alles sortiert ist.{w} Ich schwöre, ich werde verrückt, wenn ich noch ein Tag mehr an dieser Schule verbringen muss."

    $ sayaface='joking'
    show Sayaka

    s "Aww, tu doch nicht so, als wärst du so verzweifelt.{w} Ich weiß doch genau, dass du Spaß mit Kenta hattest."

    $ hikaface='embarrassed'
    show Hikari

    h "S-Sei nicht lächerlich!{w} Ich mach nur mein Job..."

    $ sayapose='magical_1'
    $ sayaface='happy'
    show Sayaka
    with dissolve

    s "Du kannst mich nicht hinters Licht führen.{w} Nicht, wenn dein Gesicht so knallrot ist!"

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

    s "Hmmm.{w} Vielleicht hätten wir eine Karte mitnehmen sollen?"

    "Well.{w} That just confirms it.{w} We're hopelessly lost!"

    "Any tension that might have existed before is sucked away the moment Sayaka begins to scratch her head and glance around the place."

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

    s "Okay, der Wald ist nicht so groß.{w} Glaub ich.{w} Ich bin sicher, wir finden die Höhle, wenn wir noch ein bisschen umherwandern!"

    "Hasn't stumbling around randomly only made us go around in circles?{w} I fear the sun might set before we ever find this darn cave now!"

    "I know it won't help, but I join the pair in surveying the land.{w} I don't even know what I'm supposed to be looking out for, apart from..."

    p "Eine Höhle ...?"

    s "Hm?{w} Ist was?"

    "I squint at something in the distance.{w} A cluster of boulders that had caught my attention.{w} My eyes were practically drawn there like some kind of magnetic force was at work."

    "I've never been here before...{w}yet somehow it seems familiar."

    p "Können wir da kurz nachsehen?"

    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Klar!{w} Wir haben sowieso keine besseren Anhaltspunkte.{w} He-hehe-hehe ..."

    with Pause(2.5)

    "We trek over to the oddly suspicious rock formation.{w} I wonder, could this really be it?"

    $ sayapose='magical_1'
    show Sayaka
    with dissolve

    s "Hmm, hmm.{w} Was hast du dort drüben denn gesehen?"

    "Sayaka begins to poke about the boulders, a hand to her chin."

    "Circling around the cluster reveals nothing too out of the ordinary, but...{w}there has to be more."

    p "Weiß nicht.{w} Mir ist vorgekommen, als hätt ich was gespürt."

    $ hikaface='angry'
    show Hikari

    h "Das sind einfach nur ein paar dumme Steine.{w} Wir verschwenden Zeit!"

    s "Aww.{w} Wir sollten echt mal nachsehen, wenn Kenta schon sagt, er sieht dort was.{w} Er ist mit der dunklen Königin doch verbunden, oder?{w} Er muss ein paar Dinge über sie wissen, wenn auch nur im Unterbewusstsein."

    "She says that as she raps gently at one of the rocks with her knuckle, one eye closed to better examine it."

    $ hikaface='normal'
    $ sayaface='happy'
    show Sayaka
    show Hikari

    s "Oh!{w} Der scheint irgendwie locker zu sein."

    "Sayaka takes a grip of the rock in question and begins to pull at it with all her might, her teeth gritting in determination."

    $ sayaface='scared'
    show Sayaka

    s "Hrghh!{w} I-Ich könnte eure Hilfe hier gut gebrauchen!"

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

    s "Das ..."

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

    s "Fühlt sich echt so an!{w} Man kann die Dunkelheit förmlich sehen."

    "That's not really something you should be saying so happily..."

    "She is right, though.{w} There's a foreboding sense of despair as I peer deep into the hole.{w} A heavy tension in the air, as if the sheer presence of whatever lurks down there seeks to consume us all."

    "Once we go down there...{w} This will be it.{w} We'll finally put an end to this madness, and I might finally be able to get some peace after all of this is done."

    "...Do I really have the strength to go through with this?{w} To reseal a long forgotten evil that tormented--"

    $ sayaface='happy'
    $ sayapose='magical_2'
    show Sayaka
    with dissolve

    s "Genug Zeit vergeudet!{w} Rein mit uns!"

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

    s "Hmm, ist was?"

    p "Das hab ich mir echt nicht vorgestellt, als ich daran gedacht hab, wie es wär, ein Held zu sein."

    p "In einem engen, kleinen Tunnel rumkriechen ...{w} Ich hab mir das irgendwie Dramatischer vorgestellt."

    "Sayaka lets out a giggle as she soldiers on ahead."

    s "Ich bin sicher, vor uns warten genug dramatische Momente!{w} Wir müssen vorher nur durch die ... {i}weniger{/i}... dramatischen Momente."

    s "Und hey, das ist gar nicht so schlimm.{w} Zumindest müssen wir uns nicht durch unzählige Schatten durchkämpfen."

    s "Es ist zwar nicht die edelste Art und Weise, die Dinge anzugehen, aber es spart Kraft ..."

    "She brings up a good point.{w} However..."

    p "Aber was, wenn ...{w} {i}in{/i} diesem Tunnel Monster auf uns warten?{w} Falls das der Fall ist, können wir nicht wirklich viel tun."

    h "S-Sag das nicht!{w} Ich hab nichtmal über soetwas nachgedacht..."

    s "Oh, wow, du hast recht.{w} Wir wären völlig wehrlos!"

    h "Sayaka!"

    s "Die würden uns echt massakrieren.{w} Hikari kann hier wohl kaum ihr Schwert einsetzen und ich erst recht nicht meinen Bogen."

    s "Ich frage mich, welcher Schatten durch diese Tunnel passt?{w} Oh!{w} Vielleicht irgendetwas mit Tentakel ... Ich weiß nämlich genau, dass die dich {i}lieben{/i}, Hikari!"

    h "Sei ruhig!{w} Jetzt bist du einfach nur böse!"

    "Hmm...{w} Maybe I should have kept my thoughts to myself?{w} Sayaka is having way too much fun with this."

    s "Oder wie wär's mit--"

    h "H-hiyahh!{w} Irgendwas hat mich berührt!"

    "Hikari shrieks, almost bursting my eardrums in the process."

    h "Warst du das, Kenta?!{w} Ich wusste, ich hätte als Letzte einsteigen sollen..."

    p "Ich?!{w} Natürlich nicht!{w} Ich bin ja ganz woanders!{w} Wofür hältst du mich eigentlich?"

    h "...Willst du wirklich, dass ich das beantworte, nach dem, was du in den letzten Tagen getan hast??"

    p "D-Das waren Unfälle! UNFÄLLE!"

    h "Naja, vielleicht war das wieder einer deiner 'Unfälle', hmm?{w} Ein Mädchen greifen whärend sie komplett hilflos ist?"

    p "Komm schon, ich bin ja nicht mal in deiner Nähe!{w} ... Vielleicht bildest du dir das auch einfach nur ein?"

    "I can just about hear Sayaka stifle a giggle as we continue to argue.{w} Hmmm."

    play music "bgm/mischiefintro.ogg" fadein 2.0
    queue music "bgm/mischiefloop.ogg"

    h "F-Fein.{w} Wenn du es nicht warst, wer dann?{w} Es hätte nicht Sayaka sein, da sie vor mir ist."

    s "Vielleicht war es ein großer, schleimiger Tentakel, der Hallo sagen wollte."

    "She says it in an almost sing-song manner.{w} Okay, yeah, I see what's happening now.{w} I'm hoping Hikari will realise soon, too."

    h "E-Es hätte aber nicht--kyahh!{w} Da ist es wieder!"

    h "Okay, ernsthaft was ist--a-ah!"

    "This bizarre series of events continues for longer than I feel is necessary, until finally I feel I have to speak up, or we might be stuck in this tunnel all day."

    p "Okay, komm, Sayaka, das reicht jetzt.{w} Du hattest deinen Spaß.{w} Jetzt müssen wir uns aber wieder konzentrieren, okay?"

    h "W-Was...?{w} Sayaka?{w} Aber sie hätte nicht..."

    "Confirming my suspicions, Sayaka lets out another one But, she couldn't possibl of her devious laughs."

    s "Aww, okay, okay.{w} Ich musste einfach.{w} Es ist einfach so leicht, sie zu ärgern!"



    h "..."

    "Hikari takes in a deep breath.{w} ...Uh-oh."

    h "Ich werde dich umbringen, Sayaka!"

    s "Da musst du mich erstmal fangen!"

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

    s "Ooh, hey!{w} Ich glaube, ich seh dort vorne etwas."

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

    s "Puh!{w} Das war mal eine Reise.{w} Wie geht es euch allen?"

    $ hikaface='angry'
    show Hikari

    h "Ich bin okay.{w} Es wäre besser gewesen, wenn nicht {i}jemand{/i} mit mir da unten rumgespielt hätte."

    $ sayaface='joking'
    show Sayaka

    s "Heh-hehe ...{w} Ich wollte ...{w} einfach die Stimmung hoch halten?"

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

    s "Mach dir keine Sorgen!{w} Wir können es schaffen.{w} Zusammen."

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

    s "Hmmm, na ja, ich schätze, über eine Belohnung können wir reden, wenn das alles erstmal vorbei ist."

    h "Eine ... Belohnung ...?"

    "Hikari falls silent at the prospect.{w} ...Suspiciously so."

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

    y "So bereitwillig sich anzubieten, nachdem ich all die Nächte damit verbracht habe, dich zu jagen.{w} Du hast wirklich einen Todeswunsch."

    y "Aber das ist in Ordnung.{w} Ich gebe dir ein schnelles und schmerzloses Ende."

    h "Du redest nur mit dirselber!{w} Denk nicht, ich kann nicht sehen, dass du Angst hast.{w} Du weißt, dass das Ende der Linie für dich ist."

    h "Ich weiß nicht, was du von alldem willst, aber was auch für verrückte Fantasien du hast, werden zu einem Ende kommen. {w} Jetzt!"

    "Während ihr Schweißperlen über das Gesicht laufen, knirscht sie mit den Zähnen.{w} Sie hat also wirklich Angst ...?"

    y "Halt den Mund!{w} Du weißt nichts.{w} Ich...{w}Ich brauche das!"

    p "Yuzuki, es muss nicht so enden.{w} Ich weiß, du wirst mir nicht glauben, aber ich weiß, was du durchmachst.{w} Den Schmerz, den du fühlst.{w} Vielleicht können wir--"

    with hpunch

    y "Ich sagte sei ruhig!"

    "Die ganze Höhle fängt zu beben an.{w} Von oben regnen Steinbrocken herab.{w} Das wird echt gefährlich."

    y "Ich brauche deine Hilfe oder dein Mitgefühl nicht.{w} Ich repariere Dinge selbst.{w} Alles wird gut, wenn ich dich wie einen Feuerhydranten aufreiße und dein Blut magisch wirken lasse."

    "Mein Gesicht wird blass, als ein verrücktes Lachen über ihre Lippen wandert.{w} Wie kann sie bloß so was Krankes sagen?{w} ... Ich hab es wirklich versucht, aber vielleicht ist sie geistig wirklich nicht mehr zu retten?"

    "Ich darf nicht so schnell aufgeben!{w} Noch ein Versucht ...{w} Vielleicht erreich ich sie ja doch?"

    p "Ich weiß, dass du kein schlechter Mensch bist, Yuzuki.{w} Du bist nur ...{w} einsam, oder?"

    y "Ich bin nicht allein!{w} Mindestens...{w}Ich werde nie wieder einsam sein, wenn das einmal vorbei ist."

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

    y "Ich habe das Gefühl, dass du mich vielleicht unterschätzt.{w} Es ist wahr, ich musste bei unserer letzten Begegnung beschämend den Schwanz drehen, aber ..."

    "Yuzuki grunzt und wird auf einmal von einer dunklen Aura umgeben.{w} Das seh ich zum ersten Mal ..."

    y "Wir kämpfen auf meinem Heimatmarkt.{w} Ich habe hier eine direkte Verbindung zu ihr.{w} Ich kann..{w} Ich kann sie in mir fühlen."

    y "Ich kann jetzt nicht verlieren!{w} Nicht mit {i}ihr{/i} auf meiner Seite!"

    "Mit einem weiteren verrückten Lächeln löst sie wieder ein heftiges Beben aus.{w} Ich schätze, sie meinst es wirklich ernst ...{w} Sayaka und Hikari werden hier kein leichtes Spiel haben."

    stop music fadeout 2.0

    y "Nun Dann...{w}stirb!"

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

    y "Das kann sein...{w}vereinbart worden!"

    "Die beiden geraten aneinander, während die Magie um sie herum förmlich zu knistern beginnt."

    "Yuzuki muss im Moment stärker sein als je zuvor, aber Hikari scheint mit ihr mithalten zu können – abgesehen davon, dass sie aufgrund des Drucks immer weiter in den Boden einsinkt."

    "Sie muss weit über ihre Grenzen hinausgehen, um überhaupt eine Chance gegen dieses Monster zu haben.{w} Als ihr bereits Schweiß über das Gesicht läuft, erkenne ich, dass es echt anstrengend für sie sein muss."

    h "Hrghh...{w} L-Los!{w} Ich hab sie...{w}abgehalten!{w} Ihr Typen...{w}beendet das!"

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

    "Ihre Stimme dröhnt und die Mage um sie herum fängt heftig zu knistern an.{w} Ich hab sie noch nie zuvor so erlebt ..."

    h "Oder willst du, das alles hier für nichts ist?!{w} Ich kann...{w}halte sie für eine Weile in Schach.{w} Kein Problem!"

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

    "...Als Reaktion darauf gibt dieser einen letzten elektrischen Schlag von sich, ehe der Schmerz nachlässt.{w} Und auch der Geschrei."

    "Die Wiederversiegelung … wurde abgeschlossen."

    scene cave
    with dissolve

    "...Du willst mich wohl verarschen.{w} Ich musste die ganze Zeit nur dagegenschlagen?!"

    "I…Ich kann’s nicht fa..."

    "Warte.{w} Jetzt erinnere ich mich.{w} An das, was mir in dieser Nacht beigebracht wurde."

    "Während der Großteil der Magie mit der Haupthand ausgeführt wird, wird in einigen Fällen, so auch bei einer Versiegelung, auch die Nebenhand benötigt, um den Prozess zu beenden."

    "Wie konnte ich das – gerade in dem Moment – nur vergessen?!"

    "Ich bin ...{w} Ich bin so ein Idiot.{w} Das ist so lächerlich, dass ich selbst darüber lachen muss."

    "Wirklich ..."

    p "Hah ...{w} Ahahahaha ..."

    "Geistig vielleicht völlig zerstört von dem, was ich in den letzten Tagen durchmachen musste, falle ich kraftlos nach hinten."

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


        cg "Schon ein bisschen spät, um einzuschlafen, findest du nicht?"

        "A cheerful voice chirps, rousing me to my senses."

        "It could be none other than..."

        scene cg13_2
        with wake
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"

        p "S-Sayaka ...?"

        "I mutter her name, as it seems too good to be true."

        s "Jup.{w} Ich bin's!"

        "She's kneeling over me, offering a helping hand with the sweetest smile I've ever seen."

        "Things were looking bleak back then...{w}but I never should have doubted she wouldn't pull through."

        "I'm so happy she's okay that I just about fight back the urge to cry."

        p "Sayaka, ich ..."

        p "Hab ich ...?"

        s "...Die dunkle Königin versiegelt?{w} Darauf kannst du einen lassen.{w} Du hast echt gute Arbeit geleistet!"

        "She beams as she takes a hold of my limp hand and gently props me up to a sitting position."

        s "Einen Moment lang habe ich mir echt Sorgen gemacht.{w} Für kurze Zeit dachte ich, der Zauber wäre vielleicht zu viel für dich gewesen ..."

        p "W-Warte, du hast dir um {i}mich{/i} Sorgen gemacht?!{w} Ich dachte, diese Monster wären--"

        s "Die?{w} Pff.{w} Das war doch gar nichts!{w} Die hab ich eiskalt ausgelöscht … Du hast es nur verpasst."

        p "Ich konnte dich nicht mal sehen!"

        s "Ich hab mich ...{w} totgestellt ...?"

        p "Sayaka ..."

        s "He-hehehe-hehe ..."

        "She scrubs at the back of her head and gives me the same goofy grin.{w} This girl..."

        p "Ich hab mir wirklich Sorgen um dich gemacht ..."

        p "Wenn dir was passiert wäre ...{w} Ich weiß echt nicht, was ich dann getan hätte ..."

        s "Aww, ich wusste gar nicht, dass du so rührselig werden kannst, Kenta."

        s "Brauche ich für all die Tränen etwa einen Regenschirm?"

        "It seems words aren't getting through to her, so..."

        scene cave
        $ sayaface='shy'
        $ sayapose='magical_1'
        show Sayaka
        with dissolve
        with hpunch

        s "H-Hä?{w} Kenta?!"

        "I wrap my arms around her and pull her into a tight embrace.{w} It isn't enough just to be able to see her again, I wanted to make sure she was really there."

        p "Ich bin froh, dass es dir gut geht."

        s "Ich, äh ..."

        "She seems to be at a loss for words, as her arms hang limply by her sides.{w} She's really making this awkward for me."

        $ sayaface='happy'
        show Sayaka

        s "Aw, was zum Teufel!{w} Komm schon, du alter Softie."

        "She brings her arms up and returns the hug, squeezing me in a similarly tight embrace.{w} ...Maybe {i}too{/i} tight."

        $ sayaface='joking'
        show Sayaka

        s "Hoffen wir, dass Hikari davon nichts erfährt, hm?{w} Sonst zuckt sie noch aus."

        "She stifles a giggle as she nestles into my shoulder."

        "Wait...{w} That's a point."

        "I pull back from the hug."

        p "Hikari!{w} Geht es ihr gut?"

        $ sayaface='smiling'
        show Sayaka

        "Sayaka tilts her head, looking confused for a moment."

        s "Hm?{w} Der geht’s gut!"

        p "Und ...{w} Yuzuki ...?"

        "She musters up a small smile, which instills some amount of hope in me."

        $ sayapose='magical_2'
        show Sayaka
        with dissolve

        s "Folge mir!"



        "I do as instructed and follow along, almost hand in hand before we come to our senses."

        $ sayaface='happy'
        show Sayaka

        s "Tada!{w} Siehst du?{w} Eine Hikari und eine Yuzuki."

        "Hikari is standing guard, her sword drawn as she keeps the sharp end pointed firmly at a very...{w}tattered...{w}Yuzuki."

        "While unconscious, it doesn't look like Yuzuki is badly hurt.{w} She's breathing steadily, and I don't see too much damage beyond the cosmetic stuff."

        $ hikaface='angry'
        $ hikapose='magical_2'
        show Sayaka at left
        show Hikari at right
        with dissolve

        h "Da seid ihr zwei!{w} Was um alles in der Welt habt ihr so lange gemacht?!"

        "Yup.{w} She seems fine.{w} There isn't a scratch on her, and she's as lively as ever."

        $ sayaface='joking'
        $ sayapose='magical_1'
        show Sayaka
        with dissolve

        s "Na ja.{w} Wir haben ...{w} Heh-hehehe-heh."
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


        tg "Während der Arbeit schlafen?{w} Was eine Überraschung.{w} Was werden wir jetzt mit dir machen?"

        "I hear a familiar voice.{w} One that's stern, yet...{w}there's a surprising amount of affection to it.{w} Unusually so."

        "I have a hunch who it could be...{w}but, I wonder...?"

        scene cg13_3
        with wake
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"    
        p "Hikari ...?"

        "It really is her.{w} She's okay!{w} Thank god..."

        h "Niemand anders.{w} Du hast dir auf dem Weg nach unten nicht den Kopf gestoßen, oder...?"

        "Okay, yeah, it's Hikari."

        "Despite her usual scolding words, I can't help but there's a softer edge to them.{w} But maybe I'm just imagining things?"

        "And maybe I'm just imagining that smile, too, as she leans down to help me up."

        p "Hab ich ...{w} Ich mein ...{w} Ist es vorbei?"

        "She helps me up to a sitting position as I slowly regain my senses."

        h "Ja.{w} Die dunkle Königin ist wieder versiegelt, dank dir."

        h "Ich hatte meine Zweifel, dass die Dinge wirklich gut enden würden, mit dem Monster Yuzuki, das den Job beenden würde... "

        h "Aber, es sieht so aus, als ob {i}du{/i} Helden-Material wärst."

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

        h "Sie hat wirklich Glück, dass sie okay ist.{w} Und nach alldem was sie uns angetan hat, weiß ich nicht, ob sie das {i}verdient{/i} hat."

        "She motions over somewhere."

        $ hikaface='normal'
        show Hikari

        h "Komm, ich werde es dir zeigen.{w} ...Idiot."

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

        s "Ah, da sind sie!"

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

        s "Oh, du hättest sie sehen sollen, Kenta.{w} Sie hatte es nach der Versiegelung echt eilig, dich zu sehen.{w} Ich hab noch nie so was Bezauberndes gesehen!"

        $ hikaface='embarrassed'
        show Hikari

        s "'Kyahh!{w} Geht es Kenta gut?!{w} Ich kümmer mich um ihn, du pass auf Yuzuki auf!'"

        "She puffs out her chest and puts on a silly voice as she recalls the moment.{w} Is this supposed to be her Hikari impression?"

        p "V-Verstehe."

        $ sayaface='smiling'
        show Sayaka

        s "Hmm?{w} Mehr hast du in einem so innigen Moment nicht zu sagen?"

        "If I'm being honest, I really didn't know Hikari cared for me {i}this{/i} much.{w} I thought she was just shy in general around people before!"

        "I mean, she's always been there for me.{w} Putting her life on the line.{w} And after today...{w}I've realised there's perhaps a bit more to it than just her working out of duty."

        "But, I've been through so much in these last few moments, I'm really not sure how to process it at all.{w} All I can do is stand with my mouth slightly ajar."

        p "Ähhh ..."

        $ hikaface='normal'
        $ hikapose='magical_1'
        show Hikari
        with dissolve

        s "Hmm.{w} Na ja, viel Glück beim nächsten Mal, Hikari.{w} Sieht aus, als hätte er sich schon in mich verguckt, und das kann nichts und niemand mehr ändern!"

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


        cg "Da ist er, gesund und munter!{w} Unser Held."

        tg "Ist...{w}ist er wirklich okay?{w} Nach so einem Zauberspruch, besteht die Chance dass es--"

        with hpunch

        cg "Jup!{w} Schau!{w} Er atmet noch."

        "Something prods at my face.{w} A warm, tender touch."

        with hpunch

        "...And it prods some more.{w} And more."

        tg "Was machst du da?!{w} Du kannst ihn doch nicht einfach so anstupsen!"

        cg "Hmm?{w} Ist da jemand eifersüchtig?{w} Eifersüchtig darauf, dass ich ganz intim mit ihm werd?"

        tg "B-Bitte!{w} In welcher Welt war dass 'intim'?{w} Du bist ärgerlicher, als alles anderes.{w} Gib ihm ein bisschen Raum!"

        cg "Okay, okay!"

        cg "...Ein Stupser noch!"

        "{i}Smush{/i}.{w} The left side of my cheek is pushed a great deal up.{w} Okay, this is weird.{w} I should probably wake up now."

        p "Nghh."

        tg "A-ah!{w} Er wacht auf!{w} Sayaka, geh weg!"

        cg "Wahh, okay, okay!{w} Du musst mich doch nicht gleich so anbrüllen."

        scene cg13_1
        with wake
        play music "bgm/magicalgirlintro.ogg" fadein 2.0
        queue music "bgm/magicalgirlloop.ogg"    
        "I awake to a familiar, comforting sight.{w} My guardian angels--Sayaka and Hikari."

        "They're both perfectly fine.{w} Not a single scratch on either of them.{w} I'm...{w}I'm so glad."

        p "M-Mädels ...?"

        "I have to call out to both of them, just to confirm that this is real."

        s "Guten Morgen!{w} Wie geht es dir?"

        h "Gott sei Dank geht es dir gut...{w} Du solltest uns keine Sorgen machen, Kenta!"

        "They both look relieved as they offer their hands my way."

        s "Kannst du stehen?"

        "...I try my best to heave myself up off the ground, but my feeble arms give way.{w} Whoops.{w} Guess that resealing business really took more out of me than I thought."

        "Sayaka giggles at my attempt, while Hikari flashes me a look of concern."

        s "Ich betrachte das mal als 'nein'.{w} Komm, hoch mit dir!"

        h "Du solltest dich danach nicht drängen. {w} Wenn du unsere Hilfe brauchst... {w} Alles, was du tun musst, ist es zu sagen, und ich werde glücklich sein..."

        "She trails off into a murmur inaudible to even herself, I'm sure."

        "Sayaka and Hikari both take up a hand of mine, and they help me up to a sitting position."

        "As I sit up, the fog begins to clear within my mind and I recollect my senses."

        s "Und auf.{w} Alles in Ordnung?"

        h "Ja, wenn es etwas gibt, was du brauchst, halte dich nicht zurück zu fragen!"

        "Sayaka kneels at my side, her eyes glimmering.{w} ...As does Hikari, who kneels at my opposite side.{w} This is getting a bit weird now.{w} What is this?"

        p "Es geht mir, äh, entsprechend.{w} Macht euch keine Sorgen.{w} Ich bin nur ein bisschen schwach auf den Beinen."

        p "Ich ...{w} Ich hab mir ehrlich gesagt mehr Sorgen um euch gemacht.{w} Ich hatte echt Angst um euch!"

        s "Psh, um uns?{w} Wir sind zäher, als wir aussehen.{w} Und wir haben schon Schlimmeres durchgestanden.{w} Uns geht's gut!"

        h "Ganz genau.{w} Wir wurden dafür trainiert.{w} Es hätte vielleicht schlecht ausgesehen, aber ich versichere dir, alles war ... {w}unter Kontrolle!!"

        "They're trying their best to assure me things were okay, but things really did look dire back then..."

        "Sayaka suddenly leans in, a dangerous smile creeping upon her face."

        s "Wenn du sagst, du hast dir Sorgen um uns gemacht ...{w} Hast du dir da um irgendjemand bestimmten {i}mehr{/i} Sorgen gemacht?"

        p "Ähh ...?{w} K-Kann ich nicht ..."

        h "S-Sayaka!{w} Was hast du hier versucht?!"

        s "Ahhh, nichts."

        s "Sein Zögern, auch nur irgendwas zu sagen, bedeutet eindeutig, dass er keinen von uns verletzten will.{w} Oder besser gesagt, vor allem {i}dich{/i} nicht verletzen will."

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

        s "Oh, warte, ich helf dir!"

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

        s "Bevor wir gehen, solltest du noch jemanden aufsuchen."

        $ hikaface='normal'
        show Hikari

        h "Ugh.{w} Ist es wirklich so wichtig?{w} Ich habe ihr Leben verschont.{w} Können wir sie nicht einfach zurücklassen?"

        "Sayaka and Hikari both vie for different directions as we stumble along as one just barely functional unit."

        "Wait, are they talking about..."

        p "Yuzuki?!{w} Du meinst, es geht ihr gut?"

        s "Jup!{w} Hier lang!"

        stop music fadeout 5.0

        "We swerve wildly as Sayaka takes command, Hikari reluctantly following along."

        $ sayaface='joking'
        show Sayaka

        s "Schau!{w} Ihr geht's gut.{w} Und ...{w} wir hätten sie besser nicht alleine lassen sollen.{w} Aber wir konnten uns einfach nicht einigen, wer dir helfen soll!"

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

    s "Befürchte ich, ja."

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

    y "Sie erzählte mir alles, was ich hören wollte.{w} Dass jeder mich anbeten und mir gehorchen würde, wenn ich ihr helfen würde..."

    h "Was?!{w} Das ist das Dümmste, was ich je gehört--"

    y "Es klingt dumm, ich weiß.{w} Zu denken, dass ich all das in der vergeblichen Hoffnung getan habe, dass es mich bekommen würde ...{w}Freunde."

    y "Ich habe gerade nicht nachgedacht.{w} Ich war so besessen davon, dass ich niemals daran dachte, irgendwas zu hinterfragen."

    "So she isn't a bad person.{w} Just misguided.{w} And did the wrong things for an innocent enough goal.{w} I can't help but feel sorry for her...{w} for things to have ended up this way."

    y "Und jetzt, mit der einzigen Chance, die ich hatte, war mein Ziel immer dahin.{w} Warum sollte ich weiterleben?{w} Es ist hoffnugslos..."

    s "Hmm.{w} Verstehe, verstehe."

    "Sayaka cups a hand to her chin and nods to herself, as if intensely thinking about what she's been told."

    stop music fadeout 2.0

    s "Ich glaube, ich kenne da eine einfache Lösung für all das!"

    y "...?"

    h "D-Du kennst eine?"

    s "Jup!"

    "Sayaka bounces forward and extends a hand to Yuzuki, a blinding smile upon her face."

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

    "Yuzuki is taken aback by the sudden gesture, but not as much as Hikari."

    h "Eh?!{w} W-Wir werden?!"

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

    s "Aw, sei doch nicht so.{w} Jeder verdient Freunde!{w} Wen kümmert's, dass man ein paar schlimme Dinge getan hat?{w} Wahre Freunde sehen darüber hinweg!"

    "I'm not really sure if we should be fully overlooking the fact she was that twisted, dark angel before, but Sayaka still has a good point."

    $ sayaface='smiling'
    show Sayaka

    s "Na jetzt komm schon.{w} Verschwinden wir aus dieser dunklen Höhle und vergessen wir das alles.{w} Ich weiß ja nicht, wie es euch geht, aber ich bin hundemüde."



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

    s "Ahhh, endlich frische Luft!"

    "Sayaka bounds out a few steps ahead to take in the crisp air.{w} Hikari and Yuzuki are trailing behind, seemingly still not comfortable with one another.{w} I guess they always had the biggest rivalry during their encounters."

    s "Nun, das hat ja nicht mal so lang gedauert, als ich vermutet hätte.{w} Sieht aus, als hätten wir den Großteil vom Tag noch vor uns!"

    "She continues to radiate optimism as she takes in the sights, but I can't shake the one question that has been on my mind since we started this whole crusade."

    p "Was ...{w} Was geschieht jetzt?"

    $ sayaface='smiling'
    show Sayaka

    s "Hmm?"

    p "Ich mein, haben wir diesen einen Grund, weshalb ihr hier seid, nicht gerade aus der Welt geschafft?"

    $ sayaface='normal'
    show Sayaka

    s "Ohh ..."

    "It seems she realises what I mean, as her smile shrinks.{w} And...{w}it seems like that reaction answered my question for me."

    s "Das ...{w} Na ja ..."

    $ hikaface='normal'
    show Hikari at right
    show Sayaka at left
    with dissolve

    h "Du hast recht.{w} Unser Job {i}ist{/i} fertig hier."

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

    s "Hey!{w} Wer hat irgendwas vom Gehen gesagt?"

    $ yuzuface='normal'
    show Yuzuki

    s "Es stimmt, dass wir keinen {i}offiziellen{/i} Grund mehr haben, hierzubleiben."

    $ sayaface='joking'
    show Sayaka

    s "Aber ich denke, wir haben uns jede Menge Urlaub verdient, den wir einlösen sollten.{w} Nicht wahr, Hikari?"

    h "Urlaub?{w} Was um alles in der Welt bist du--"

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

    s "Siehst du!{w} Die Zeichen stehen noch nicht auf Abschied.{w} Ich bin doch nicht so gemein und verlasse euch!"

    $ sayaface='smiling'
    show Sayaka

    s "Und wir werden das Beste aus der Zeit rausholen, die wir zusammen verbringen.{w} Als Freunde!{w} Es gibt hier noch so viel, was ich versuchen möchte!"

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

    s "Wahh, beruhig dich, war doch bloß ein Scherz!{w} Kenta, beschütze mich!"

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


        s "Yo!{w} Ich hoffe, du bist schon fertig angezogen und so, denn das wird super peinlich."
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

        "She swivels the laptop around my way with a grin, its screen indeed blank."

        p "O-Ohh ..."

        $ sayaface='smiling'

        s "Aber deine Reaktion ist wirklich interessant.{w} Fast so, als hättest du wirklich einen solchen Ordner, hmm?"

        "..."

        "It's not classified as lying if I don't say anything.{w} I meet her head on with a blank stare."

        "She opens her mouth to say something, no doubt to tease me further."

        with hpunch

        h "Wir werden noch zuspät kommen, wenn ihr zwei nur rumalbert!"

        "Hikari saves the day, her commanding voice enough to sound up the stairs and into my room."

        $ sayaface='happy'
        show Sayaka

        s "Na ja.{w} Verschieben wir das Ganze auf ein anderes Mal, hmm?{w} Glauben Sie aber ja nicht, dass Sie so einfach davonkommen, Mister!"

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

        h "Es ist Zeit.{w} Was wollt ihr beide jetzt tun?"

        $ sayaface='happy'
        show Sayaka

        s "Nun, wenn du's {i}wirklich{/i} wissen musst ... Wir haben--"

        h "Eigentlich, will ich es garnicht hören!{w} Ich bin sicher, es war etwas unangebrachtes."

        "Hey now, why am I getting lumped in with her?{w} I'm an innocent, pure-hearted boy!"

        $ sayaface='joking'
        $ sayapose='school_2'
        show Sayaka
        with dissolve

        s "Ach.{w} Dein Pech."

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

        s "So!{w} Wer hat Lust auf Frühstück?"

        p "Oh nein, das kommt gar nicht in Frage!"

        $ sayaface='scared'
        show Sayaka

        "She stops in her tracks, inches from the kitchen."

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

        "I sidle past her and enter the kitchen myself.{w} She gives me the usual pout, but, like always, it soon melts away and her smile returns."

        s "Also ...{w} Darf ich zumindest ... {w}zusehen?{w} Vielleicht kann ich dann ja gleich für die Zukunft ein bisschen was lernen!"

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

        s "Ahh, köstlich!"

        "Sayaka lets out a content sigh, having devoured her meal in record time.{w} I'm not even sure she has any time to taste with how fast she wolfs this stuff down."

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

        "Hikari storms on out of the front door, leaving the rest of us to scramble for our bags and shoes.{w} Maybe one day I'll finally understand her?"

        $ sayaface='happy'
        show Sayaka

        s "Komm schon, ein Abenteuer wartet auf uns, Kenta!"

        hide Yuzuki
        show Sayaka at center
        with dissolve

        "Sayaka extends me a hand as Yuzuki shuffles on by."

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

        "Hopeless.{w} I can't help but smile."

        $ sayaface='happy'
        $ sayapose='school_1'
        show Sayaka
        with dissolve

        s "Ah, schon gut.{w} Ich werde einfach von dir abschreiben, wenn ich nicht weiter weiß!{w} Also ...{w} Auf, auf und davon!"

        "She takes a firm hold of my hand and begins to drag me out of the house."

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

        s "Ooh, und gib mir das, und das auch.{w} Und davon kommt auch noch was rein!"

        y "Interessant.{w} Ich wusste nie, dass du so ein Auge für diese Dinge hast, Sayaka."

        "Yuzuki responds calmly as she hands over whatever Sayaka instructs, only further adding to the mess.{w} She acknowledges me with a nod of her head, before returning to the mayhem."

        "Since we started hanging out, it's been a gradual process of her opening up more to us.{w} She's still pretty quiet most of the time, and won't dive into many conversations, but I think she enjoys our company."

        "It must be tough for her to adjust to things after she's finally obtained the friends she so desired for all these years."

        "I'm sure it won't be long until she's out of her shell with Sayaka and Hikari at the helm, though.{w} They seem to be able to bring out the best in people."

        "I greet her back with a nod of my head, but my eyes are quickly fixed to Sayaka, who is a high-level threat at the moment."

        "Our desperate cries go unheard.{w} They're having way too much fun here."

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

        "Hikari leaps into action and slides over the counter, almost like an action hero would do, before she shoots a bolt of magic from her fingertips, evaporating the foul substance that Sayaka might have called 'breakfast'."

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

        "Sayaka sighs and flaps her arms in defeat."

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

        h "Kenta, i-ich hoffe du hast das nicht gehört..."

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

        s "Schwachsinn, man kann nie zu vorsichtig sein."

        "Hmm, I really wonder who it could be..."

        "I say nothing, just to see what will happen."

        s "Hmm?{w} Nichts?{w} Vielleicht schläft er wirklich noch?"

        "{i}Thump, thump, thump.{/i}{w} She hammers the door once more."

        h "Denkst du er ist okay...?{w} Er war wirklich müde, als wir uns letzte Nacht trennten."

        "That's because I don't think the pair realise just how exhausting they've become lately."

        "Don't get me wrong, I'm happy they've stuck around for a little longer..."

        "But, after the resealing, they've become {i}way{/i} more competitive.{w} I'm really not sure what they're trying to prove anymore."

        s "Hmm ...{w} Jetzt, wo du's sagst, er hat wirklich blass ausgesehen.{w} Vielleicht hat er sich eine tödliche Krankheit eingefangen, mit der er uns nicht konfrontieren wollte?"

        h "W-Was?!"

        "The door handle rattles.{w} But there's some hesitation."

        h "Aber wenn er noch schläft ...{w} Ist es wirklich okay für uns, einfach so reinzuplatzen?"

        s "Und ob!{w} Ich mach es die ganze Zeit.{w} Hast du ihn schon mal beim Schlafen zugesehen, Hikari?{w} Er ist so niedlich!{w} Da, ich hab ein paar Bilder davon gemacht."

        "...I feel so violated.{w} I'm glad I actually am awake at this point."

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

        "The door swings open and the pair come tumbling in.{w} They really do make an entrance sometimes."

        p "Ähh ...{w} Guten Morgen?"

        $ sayaface='smiling'
        show Sayaka

        s "Oh, hey, Kenta!"

        "Sayaka speaks from under Hikari, greeting me casually."

        $ hikaface='angry'
        show Hikari

        h "Warte, du warst wach?{w} Warum hast du nichts gesagt?!{w} Weißt du, wie besorgt wir waren?"

        p "Ahh ..."

        $ hikaface='scared'
        show Hikari

        "Hikari opens her mouth to scold me further, but Sayaka catches her off-guard as she leaps to her feet."

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

        "She strikes a pose she must deem 'sexy', but if anything it looks like she has a bad knot in her back."

        $ hikapose='school_2'
        show Hikari

        "Hikari is less than amused, and gives her a forceful shove which sends her toppling to the ground."

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
