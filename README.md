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

Enkelhed: Det er en simpel datafil, hvor al information gemmes i ét enkelt lag.


Portabilitet: Den er perfekt til simple applikationer, hvor hele din "database" kan gemmes i det samme repository (mappe) som din kode.


Ingen overhead: Du behøver ikke at installere eller konfigurere store database-systemer (som MySQL eller MongoDB) for at komme i gang.

