# it_sikkerhed_2026f
intro til softwaresikkerhed
onrling syg readme.
dette er et skoleprojekt til zealand Næstved...
----------------------------------------------------------------------------------------------------------------------
# Opgave: Teststrategier & Security Gates

Herunder er besvarelsen af testopgaverne - Test teknikker 5/2-26.

## 🏗️ Test & Security Stack

<details>
<summary><b>🔝 TOPPEN: System, Strategi & Brugerrejser</b></summary>

| Teknik | Beskrivelse | Security Gate |
| :--- | :--- | :--- |
| **Test Pyramiden** | En overordnet strategi der sikrer flest tests i bunden (Unit) for hurtig feedback og færrest i toppen for det store overblik. | **Go / No-Go security gate**: Her verificeres at alle security gates er bestået eller accepteret via risk acceptance. |
| **Cycle Process Test** | Fokus på at validere, at systemet kan gennemføre gentagne driftscyklusser over tid uden tab af stabilitet eller ydeevne. | **Release candidate security gate**: Her valideres infrastruktur-sikkerhed, firewall-regler og incident response. |

</details>

<details>
<summary><b>🟦 MIDTEN: Logik, Data & Integration</b></summary>

| Teknik | Beskrivelse | Security Gate |
| :--- | :--- | :--- |
| **Decision Table Test** | En teknik til at teste komplekse kombinationer af input (f.eks. MFA-krav) og de dertilhørende forventede handlinger. | **System security gate**: Her gennemføres bl.a. role & permission tests og DAST-scanninger. |
| **CRUD(L)** | Verificering af de fire grundlæggende operationer på data (Create, Read, Update, Delete) samt List-funktionen. | **Integration security gate**: Her verificeres autorisation mellem systemer og secure integration contracts (SSL/TLS). |

</details>

<details open>
<summary><b>🧱 BUNDEN: Det Tekniske Fundament (Unit Tests)</b></summary>

| Teknik | Beskrivelse | Security Gate |
| :--- | :--- | :--- |
| **Ækvivalens klasser** | Kategorisering af data i grupper (f.eks. tal vs. bogstaver), som systemet forventes at behandle ens. | **Code / Dev gate**: Her sikres det, at secure coding guidelines følges, og at der køres statisk analyse (SAST). |
| **Grænseværdi test** | Test af grænserne mellem tilstande ved at tjekke værdier, der ligger lige under, lige på og lige over en defineret grænse. | **Code / Dev gate**: Her tjekkes der specifikt for korrekt input-validering og sikker håndtering af secrets. |

</details>

---

## 💻 Data-dreven Unit Test (PyTest)
Jeg har implementeret en data-dreven test i filen `[test_security.py](https://github.com/MadsTolstrup/it_sikkerhed_2026f/blob/main/test_security.py)`, som kombinerer Decision Table-logik med Boundary Value-tests. Dette sikrer en hurtig og læsbar verificering af sikkerhedslogikken i bunden af pyramiden.
