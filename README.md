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

##Test of kryptering.

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

##Opgave - Kryptering & Hashing
-----


Opgave - Kryptering & Hashing

# Opgave – Kryptering + Hashing

### Valg af algoritmer
* **Hashing:** Jeg har valgt **SHA-256** til passwords. Det er en "one-way" algoritme, hvilket betyder, at passwords aldrig kan dekrypteres tilbage til klartekst, hvilket sikrer brugeren mod datalæk.
* **Kryptering:** Jeg har valgt **AES-128** til persondata (navne og adresser). Ud fra mit benchmark i `test_1_encryption_benchmark.py` kunne jeg se, at AES-128 er hurtigere end AES-256, samtidig med at den leverer stærk sikkerhed til GDPR-data.

### Hvornår og hvorfor?
* **Hvornår skal data krypteres?** Data skal krypteres lige **inden** de skrives til JSON-filen. Dette kaldes "Encryption at Rest" og sikrer, at data er ulæselige, hvis filen bliver stjålet.
* **Hvornår skal data dekrypteres?** Data dekrypteres kun i computerens hukommelse (RAM), når de skal læses af applikationen (f.eks. ved login eller visning af profil).
* **Hvornår skal data fjernes fra hukommelsen?** Dekrypteret data skal fjernes fra RAM **straks efter brug**. Det gør vi for at undgå "Memory Dumps", hvor en hacker kan udlæse følsom information direkte fra maskinens arbejdshukommelse.

### Andre hensyn
Man bør overveje **Saltning** af passwords sammen med hashing for at beskytte mod "Rainbow Tables" (lister over forudberegnede hashes).

