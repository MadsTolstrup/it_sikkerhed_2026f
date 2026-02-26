# it_sikkerhed_2026f
intro til softwaresikkerhed
onrling syg readme.
dette er et skoleprojekt til zealand Næstved...
----------------------------------------------------------------------------------------------------------------------
# Opgave: Teststrategier & Security Gates

Herunder er besvarelsen af testopgaverne - Test teknikker 5/2-26.

**Emne:** Brugeroprettelse, Login og Rettighedsstyring.

Denne README indeholder løsningen på dagens opgaver i softwaresikkerhed. Besvarelsen er struktureret som en "stabel" (Testpyramide), der viser sammenhængen mellem testteknikker og de relevante Security Gates.

## 🏗️ Test & Security Stack

<details>
<summary><b>🔝 TOPPEN: System, Strategi & Overblik</b></summary>

| Teknik | Konkret Eksempel for IT-sikkerhed | Security Gate |
| :--- | :--- | :--- |
| **Test Pyramiden** | Vi vægter flest Unit tests i bunden (f.eks. password-regler) og færre, men kritiske End-to-End tests i toppen (f.eks. komplet login-flow i en browser). | **Go / No-Go gate**: Den endelige kontrol af, at alle sikkerhedsportaler er bestået før produktion. |
| **Cycle Process Test** | Vi tester, om login-systemet kan køre 100 login/logout-cyklusser efter hinanden uden at databasen eller hukommelsen bliver overbelastet. | **Release candidate gate**: Her valideres systemets stabilitet og "endurance" under pres før release. |

</details>

<details>
<summary><b>🟦 MIDTEN: Logik, Data & Integration</b></summary>

| Teknik | Konkret Eksempel for IT-sikkerhed | Security Gate |
| :--- | :--- | :--- |
| **Decision Table** | Test af logik for Multi-Factor Authentication (MFA): <br>- Gyldig Bruger + Gyldigt Pass + Forkert MFA = **Adgang Nægtes**. <br>- Gyldig Bruger + Gyldigt Pass + Korrekt MFA = **Adgang Gives**. | **System security gate**: Her verificeres rollestyring, permissions og korrekt håndtering af login-tokens. |
| **CRUD(L)** | Test af database-handlinger på brugerdata: <br>- **Create:** Opret profil. <br>- **Read:** Hent info. <br>- **Update:** Skift password. <br>- **Delete:** Slet konto. <br>- **List:** Se alle brugere. | **Integration security gate**: Sikrer at applikationen og databasen taler sikkert sammen og følger "Least Privilege". |

</details>

<details open>
<summary><b>🧱 BUNDEN: Det Tekniske Fundament (Unit Tests)</b></summary>

| Teknik | Konkret Eksempel for IT-sikkerhed | Security Gate |
| :--- | :--- | :--- |
| **Ækvivalens klasser** | Vi grupperer input-typer: <br>- **Gyldige:** Navne med standard bogstaver/tal. <br>- **Ugyldige:** Forsøg på at indsætte kode (f.eks. `<script>`) eller tomme felter. | **Code / Dev gate**: Her sikres sikker kodning gennem input-validering og statisk kodeanalyse (SAST). |
| **Grænseværdi test** | Hvis kravet til et password er 8-16 tegn: <br>- **7 tegn (lige under):** Skal afvises. <br>- **8 tegn (lige på):** Skal accepteres. <br>- **17 tegn (lige over):** Skal afvises. | **Code / Dev gate**: Her tjekkes der for de mest basale logiske fejl i koden, før den merges ind i projektet. |

</details>

---

## 💻 Programmering: Data-dreven Unit Test (PyTest)
I overensstemmelse med opgaven "Leg" er der oprettet en data-dreven test i filen [test_security.py](https://github.com/MadsTolstrup/it_sikkerhed_2026f/blob/main/test_security.py). Testen bruger `@pytest.mark.parametrize` til at dække både logikken fra en Decision Table og Grænseværditests i én læsbar testfil.
<img width="1224" height="334" alt="image" src="https://github.com/user-attachments/assets/7cc1e505-e2cf-40f0-ad0e-4705505bc1d9" />

----------------------------------------------------------------------------------------------------------------------

### Test of kryptering.

10/02-26

#Opgave - Flat file 

Spørgsmål: 

1. Hvorfor er det smart at bruge en Flat-file?

En flat-file database er en simpel datafil (her JSON), hvor al information gemmes i ét lag. Det er smart til mindre applikationer, fordi man ikke skal opsætte en kompliceret database-server, og databasen kan gemmes direkte i projektets repository. Det gør systemet hurtigt at sætte op og nemt at flytte (portabelt).

### 📊 Test Design & Risikovurdering (Flat-file DB)

| Test Navn | Given (Givet) | When (Når) | Then (Så) | Risiko (hvis testen fejler) |
| :--- | :--- | :--- | :--- | :--- |
| **test_create_and_find_user_logic** | En tom database og gyldige brugerdata med alle 7 krævede felter. | Funktionen `create_user` kaldes. | Antallet af brugere stiger til 1, og data kan hentes korrekt via ID. | **Kritisk:** Systemet kan ikke gemme data, hvilket fører til permanent datatab for nye brugere. |
| **test_user_status_toggle_logic** | En database med en aktiv bruger (`enabled: True`). | Funktionen `disable_user` kaldes på brugerens ID. | Brugerens status i JSON-filen ændres til `False`. | **Høj:** Man kan ikke spærre adgang for brugere, hvilket udgør en alvorlig sikkerhedsrisiko. |



Herunder ses screenshot af terminalen, der bekræfter, at funktionerne i Data_handler understøttes og virker korrekt.
<img width="1144" height="262" alt="image" src="https://github.com/user-attachments/assets/7fd3a132-551a-4661-8a12-fb847a8ca7d9" />

--------------------------------------------------------------------------------------------------------------------

### Opgave - Kryptering & Hashing
-----


# 🔐 IT-Sikkerhed: Flat-file Database & Kryptering
**Dato:** 10/02-2026

## 📂 Opgave - Flat-file Database

### ❓ Hvorfor er det smart at bruge en Flat-file?
En flat-file database (her i JSON-format) er en simpel datafil, hvor al information gemmes i ét lag. Det er smart til mindre applikationer, fordi man ikke behøver at opsætte eller vedligeholde en kompliceret database-server. Databasen gemmes direkte i projektets repository, hvilket gør systemet hurtigt at sætte op og nemt at flytte.

### 📊 Test Design & Risikovurdering
Herunder er de implementerede unit tests beskrevet med **Given/When/Then** metoden.

| Test Navn | Given (Givet) | When (Når) | Then (Så) | Risiko (hvis testen fejler) |
| :--- | :--- | :--- | :--- | :--- |
| **test_create_and_find_user** | En tom database og gyldige brugerdata. | Funktionen `create_user` kaldes. | Antallet af brugere stiger til 1, og data kan hentes korrekt via ID. | **Kritisk:** Nye brugere kan ikke oprettes, hvilket fører til datatab. |
| **test_user_status_toggle** | En database med en aktiv bruger (`enabled: True`). | Funktionen `disable_user` kaldes på brugerens ID. | Brugerens status i JSON-filen ændres til `False`. | **Høj:** Man kan ikke spærre adgang for brugere, hvilket er et sikkerhedsbrud. |

---

## 🔒 Opgave – Kryptering + Hashing

### 🛠️ Valg af algoritmer (Baseret på benchmark)
Jeg har kørt `test_1_encryption_benchmark.py` for at sammenligne ydeevnen på forskellige algoritmer. Resultaterne var tydelige:

* **Hashing:** Jeg har valgt **SHA-256** til passwords. I min test brugte den kun **0.004083 ms**. Det er en "one-way" algoritme, hvilket betyder, at passwords aldrig kan dekrypteres tilbage til klartekst.
* **Kryptering:** Jeg har valgt **AES-128** til persondata. Min test viste, at AES-128 leverede kryptering på **0.056 ms**. Jeg har fravalgt RSA, da den var ekstremt langsom (**~65-69 ms**).

### 🛡️ Sikkerhedsprocedurer (GDPR & Sikkerhed)
For at opfylde GDPR-kravene følger systemet disse principper:

* **Hvornår krypteres data?**
    Data krypteres lige **inden** de skrives til JSON-filen. Dette sikrer **"Encryption at Rest"**, så oplysningerne er ulæselige på disken.
* **Hvornår dekrypteres data?**
    Dekryptering sker kun i computerens **hukommelse (RAM)**, når applikationen skal bruge oplysningerne til læsning.
* **Hvornår fjernes data fra hukommelsen?**
    Dekrypteret data fjernes fra RAM **straks efter brug**. Dette gøres for at undgå **"Memory Dumps"**, hvor en hacker kan udlæse følsom info direkte fra RAM.

---

### 📸 Dokumentation (Screenshots)

<img width="1274" height="314" alt="image" src="https://github.com/user-attachments/assets/f30f9d78-e5f3-4582-94d0-6698cf62e72d" />


<img width="1744" height="1007" alt="image" src="https://github.com/user-attachments/assets/77afd444-11ac-4888-a42a-bd2eb0ab08fd" />
------------------------------------------------

# IT Sikkerhed - Opgave 1 & Opgave 2: Auth-server og REST API

Dette repository indeholder min løsning til opbygning af en Auth-server og et REST API ved hjælp af FastAPI i Python. Projektet tager udgangspunkt i underviserens repo, som er blevet tilpasset og sat op lokalt.

## Hvad systemet kan (Features)


Brugerhåndtering: Man kan oprette (registrere) nye brugere via API'et.

Sikker opbevaring: Systemet gemmer aldrig passwords i klartekst (de hashes), og personfølsomme data som fornavn/efternavn krypteres i den lokale db_user_flat_file.json database.


Bearer Tokens & Roller: Via /get_bearer_token kan man logge ind og få udleveret et sikkerheds-token. Dette token bruges til at verificere brugerens identitet og roller (f.eks. "admin" eller "user"), før de får lov at udføre handlinger.


Deaktivering: Brugere kan deaktivere konti (kræver det korrekte token og de rette rettigheder).

## Miljøvariabler og Sikkerhed
Projektet bruger en .env fil til at holde styr på hemmelige nøgler til hashing og kryptering.

Bemærk: Ifølge opgavebeskrivelsen må kun test-secrets ligge i Git. Rigtige produktions-secrets (prod-secrets) holdes strengt lokalt i miljøvariabler (environment variables) og må aldrig uploades.
+1

## Sådan kører du projektet lokalt

Installer afhængigheder: pip install fastapi uvicorn python-dotenv cryptography pyjwt

Sørg for at have en .env fil med de korrekte test-nøgler i roden af projektet.

Start serveren i terminalen: py -m uvicorn main:app --reload --port 8080

Gå til http://127.0.0.1:8080/docs i din browser for at se og teste via Swagger UI.

## Bevis for udførelse:

<img width="578" height="143" alt="image" src="https://github.com/user-attachments/assets/2a20e638-efe9-4142-8729-8907bb376a80" />

<img width="1468" height="369" alt="image" src="https://github.com/user-attachments/assets/5c8efa9b-d064-4cbf-8e9f-b71651182ddd" />


<img width="387" height="236" alt="image" src="https://github.com/user-attachments/assets/56997fd0-1420-4685-9179-a47a8f0ed08c" />


