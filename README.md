# it_sikkerhed_2026f
intro til softwaresikkerhed
onrling syg readme.. så read mig da for faen mand yeah totalt!
dette er et skoleprojekt til zealand køge... eller Næstved... fuck knows, zealand prolly dont even..
----------------------------------------------------------------------------------------------------------------------

# Opgave: Teststrategier & Security Gates

Herunder er besvarelsen af testopgaverne, opdelt i en "stabel" (Test Pyramide-struktur) ved brug af HTML5-elementer og Markdown-tabeller.

## 🏗️ Test & Security Stack

<details>
<summary><b>🔝 TOPPEN: System, Strategi & Brugerrejser</b></summary>

| Teknik | Beskrivelse | Security Gate |
| :--- | :--- | :--- |
| **Test Pyramiden** | [cite_start]En strategi der sikrer flest tests i bunden (Unit) for hurtig feedback og færrest i toppen for overblik[cite: 148, 168, 430, 439]. | [cite_start]**Go / No-Go security gate**: Her verificeres at alle gates er bestået eller accepteret med risk acceptance[cite: 203, 507]. |
| **Cycle Process Test** | [cite_start]Validerer at systemet kan gennemføre gentagne driftscyklusser over tid uden tab af ydeevne eller stabilitet[cite: 122, 124, 377, 379]. | [cite_start]**Release candidate security gate**: Her testes incident response og om infrastruktur-sikkerheden er valideret[cite: 196, 198, 500, 502]. |

</details>

<details>
<summary><b>🟦 MIDTEN: Logik, Data & Integration</b></summary>

| Teknik | Beskrivelse | Security Gate |
| :--- | :--- | :--- |
| **Decision Table Test** | [cite_start]Tester komplekse kombinationer af betingelser (f.eks. MFA-krav) og forventede handlinger [cite: 139, 140, 383, 388-429]. | **System security gate**: Her gennemføres bl.a. [cite_start]Role & permission tests og DAST scanning[cite: 190, 192, 492, 494]. |
| **CRUD(L)** | [cite_start]Verificerer de grundlæggende data-operationer: Create, Read, Update, Delete og List[cite: 115, 120, 370, 375]. | [cite_start]**Integration security gate**: Her verificeres autorisation mellem systemer og secure integration contracts[cite: 183, 184, 483, 485]. |

</details>

<details open>
<summary><b>🧱 BUNDEN: Det Tekniske Fundament (Unit Tests)</b></summary>

| Teknik | Beskrivelse | Security Gate |
| :--- | :--- | :--- |
| **Ækvivalens klasser** | [cite_start]Kategorisering af data i grupper (f.eks. bogstaver, tal, operatører) der behandles ens af systemet [cite: 78-83, 263-268]. | [cite_start]**Code / Dev gate**: Her sikres at secure coding guidelines følges, og SAST-scanning udføres [cite: 175-177, 475-478]. |
| **Grænseværdi test** | [cite_start]Tester grænserne mellem tilstande ved at teste værdier lige under, lige på og lige over en grænse[cite: 85, 89, 271, 275]. | [cite_start]**Code / Dev gate**: Her tjekkes der for input-validering og korrekt håndtering af secrets[cite: 176, 178, 476, 479]. |

</details>

---

## 💻 Data-dreven Unit Test (PyTest)
Jeg har implementeret en data-dreven test i filen `test_security.py` (eller hvad du har kaldt din fil), som kombinerer en **Decision Table** logik med **Boundary Value** tests for adgangskoder. [cite_start]Dette er placeret i bunden af pyramiden for at sikre hurtig eksekvering og tidlig fejlfinding[cite: 148, 155, 430, 431].
