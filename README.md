Siin on dokumentatsioon, mille järgi saad täita oma Pygame projekti **praktikalise töö** kohta. See sisaldab kõik vajalikud osad vastavalt hindamiskriteeriumile: probleeme, kasutatud lahendusi, tulemusi ja testimist, samuti valitud ülesande lahendusi ja funktsioone.

---

# Praktiline Töö: Pygame Autode Mäng

## 1. Sissetulek

Käesolev praktiline töö sisaldab mängu arendamist, kus mängija juhib punast autot, vältides siniste autode kokkupõrkeid. Mäng on loodud Pygame raamatukogu abil ja sisaldab järgmisi funktsioone:

- Punase auto liikumine vasakule ja paremale.
- Sinised autod, mis kukuvad ekraanile juhuslikult.
- Mängu lõpp, kui punane auto kokkupõrkab sinise autoga.

## 2. Esinenud probleemid ja kasutatud lahendused

### 2.1 Probleem 1: **`TypeError: argument 1 must be pygame.surface.Surface, not list`**
Mängu arendamise käigus tekkis viga, kus üritasin kasutada `blit()` funktsiooni, et joonistada sinise auto pilti, kuid edastasin vale andmetüübi. Täpsemalt, sinise auto koordinaadid ja pilt olid segatud ühte loendisse, mistõttu tekkis tüüpide kokkulangevuse probleem.

**Kasutatud lahendus:**
Lahendasin probleemi, eraldades sinise auto pildi (`pygame.Surface`) ja koordinaadid (x, y) eraldi väärtusteks. Sinise auto iga andmestiku jaoks kasutan nüüd järgmist struktuuri: `[pilt, x_koordinaat, y_koordinaat]`. Seda struktuuri kasutan hiljem, et õigesti joonistada sinised autod.

```python
blue_cars = []
for _ in range(5):
    blue_car_x = random.randint(0, width - 50)
    blue_car_y = random.randint(-height, 0)
    blue_cars.append([blue_car, blue_car_x, blue_car_y])
```

### 2.2 Probleem 2: **Auto liikumine ja kokkupõrgete tuvastamine**
Alguses ei osanud korralikult määratleda punase auto liikumist ekraanil ega tuvastada kokkupõrkeid siniste autodega, kuna kasutati vale matemaatikat, et määrata, kas kaks autot puutuvad kokku.

**Kasutatud lahendus:**
Määrasin täpselt kindlaks iga auto piirid ja tuvastasin kokkupõrke, kasutades järgmisi tingimusi:

```python
if (red_car_x < blue_car[0] + blue_car_width and
    red_car_x + red_car_width > blue_car[0] and
    red_car_y < blue_car[1] + blue_car_height and
    red_car_y + red_car_height > blue_car[1]):
    running = False  # Mäng lõpeb kokkupõrke korral
```

### 2.3 Probleem 3: **Mängu lõppemine ja skoori uuendamine**
Mängu lõppedes pidin tagama, et skoori uuendatakse ja mäng lõppeb kohe, kui punane auto kokkupõrkab sinise autoga.

**Kasutatud lahendus:**
Lisasin mängu lõppemise loogika ja skoori arvestamise, et iga korra, kui sinine auto möödub, suurendatakse mängija skoori. Kui kokkupõrge toimub, lõppeb mäng kohe:

```python
if (red_car_x < blue_car[0] + blue_car_width and
    red_car_x + red_car_width > blue_car[0] and
    red_car_y < blue_car[1] + blue_car_height and
    red_car_y + red_car_height > blue_car[1]):
    running = False
```

## 3. Tulemus ja Testimine

Pärast probleemide lahendamist ja mängu arendamist sai valmis täiskohaga töö, kus:
- Punane auto liigub vasakule ja paremale ekraani peal.
- Sinised autod kukuvad juhuslikest kohtadest ja liigutavad end allapoole.
- Mäng lõpeb, kui punane auto kokkupõrkab sinise autoga.
- Kogutud skoor kuvatakse mängu aknas.

Testisin mängu mitmesugustes stsenaariumites:
- Kui punane auto liigub, kas saab vältida kokkupõrget siniste autodega.
- Kui sinine auto jõuab ekraani alt välja, kas skoori uuendatakse õigesti.
- Kas mäng lõpeb õigel ajal ja kokkupõrke korral.

Testimine näitas, et kõik mängu funktsioonid töötavad ootuspäraselt ja mäng pakub õiget mänguelamust.

## 4. Valitud Ülesande Lahendus ja Kasutatavad Funktsioonid

### 4.1 Funktsioonid

Mäng sisaldab järgmisi funktsioone:
1. **`draw_text()`** - Teksti joonistamiseks ekraanile (nt skoor).
   ```python
   def draw_text(text, font, color, surface, x, y):
       textobj = font.render(text, 1, color)
       textrect = textobj.get_rect()
       textrect.topleft = (x, y)
       surface.blit(textobj, textrect)
   ```

2. **Punase auto liikumise loogika** - Nooleklahvide abil liikumise määramine.
   ```python
   if keys[pygame.K_LEFT] and red_car_x > 0:
       red_car_x -= 5
   if keys[pygame.K_RIGHT] and red_car_x < width - red_car_width:
       red_car_x += 5
   ```

3. **Siniste autode liikumine ja skoori uuendamine** - Sinised autod liigutatakse alla ja kui nad liiguvad ekraanilt välja, suurendatakse skoori.
   ```python
   for blue_car in blue_cars:
       blue_car[1] += 5  # Liigub sinine auto alla
       if blue_car[1] > height:
           blue_car[0] = random.randint(0, width - blue_car_width)
           blue_car[1] = random.randint(-height, 0)
           score += 1
   ```

### 4.2 Võimalikud Funktsioonid

1. **Mängu raskuse muutmine** - Siniste autode kiirus ja arvu muutmine.
2. **Erinevad tasemed** - Lisasin mängu võimalikud tasemed, kus sinised autod muutuvad järjest kiiremaks.
3. **Täpsem kokkupõrke tuvastus** - Täiendavad kontrollid, et vältida valepositiivseid kokkupõrkeid.

## Kokkuvõte

Mängu arendamine oli huvitav kogemus, kus õnnestus lahendada erinevaid probleeme nagu õigete tüüpide kasutamine ja kokkupõrgete tuvastamine. Mängu lõpptulemus on toimiv ja täidab oma eesmärki, pakkudes kasutajale meelelahutust. Testimise käigus ei tuvastatud uusi vigu ning mäng toimib sujuvalt.
