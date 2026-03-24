# Differences: Local Repository vs Published Site

**Comparison Date:** 2026-01-20
**Published URL:** https://portal.plataformasindigenas.org/
**Local Version:** v7 repository (master branch)

---

## Summary

The published website contains several modifications made by hand that are not present in the local repository. Key differences include:

- **Impact metrics reset to zero** on the live site (local has placeholder numbers)
- **Bilingo App section added** on the live site (not present locally)
- **Tübingen University partner removed** from the live site
- **Platform status changes** for Paresi (promoted from "Coming Soon" to "Beta")
- **New platform added** (Bakairi) on the live site
- **Additional features listed** for Enawenê-Nawê platform on the live site

---

## Differences by Page

### index.html (Homepage)

#### 1. Impact Metrics Section

The "Nossos Resultados" (Our Results) section shows different values:

| Metric | Local Repository | Published Site |
|--------|------------------|----------------|
| Línguas documentadas | 12 | 0 |
| Escolas atendidas | 45 | 0 |
| Professores capacitados | 280 | 0 |
| Entradas em dicionários | 15.000+ | 0 |

**Note:** The live site appears to have reset these to placeholder values, possibly awaiting verified data.

#### 2. Bilingo App Section

| Aspect | Local Repository | Published Site |
|--------|------------------|----------------|
| Section exists? | No | Yes |
| Features listed | N/A | Speech exercises, Vocabulary exercises, Translation exercises |
| Status | N/A | All marked "Ativo" (Active) |
| Links to | N/A | Bororo platform |

**Note:** The Bilingo App section is entirely absent from the local repository. This appears to be a new section added to showcase the learning application features.

#### 3. Partners Section

| Partner | Local Repository | Published Site |
|---------|------------------|----------------|
| Unifacc | Present | Present |
| Missão Salesiana | Present | Present |
| Universität Tübingen | Present | **Missing** |
| Uppsala University | Present | Present |

**Note:** The Tübingen University partner logo and link have been removed from the live site.

---

### plataformas.html (Platforms Page)

#### 1. Enawenê-Nawê Platform Features

| Aspect | Local Repository | Published Site |
|--------|------------------|----------------|
| Status | Beta | Beta |
| Features | Dicionário | Dictionary, Fauna, Flora, Corpus |

**Note:** The live site shows expanded features for this platform.

#### 2. Paresi Platform

| Aspect | Local Repository | Published Site |
|--------|------------------|----------------|
| Status | Em breve (Coming Soon) | Beta |
| Features | Léxico, Textos paralelos | Dictionary |
| URL | N/A | https://paresi.pythonanywhere.com |

**Note:** The platform has been promoted from "Coming Soon" to "Beta" status, with a live URL now available.

#### 3. Bakairi Platform

| Aspect | Local Repository | Published Site |
|--------|------------------|----------------|
| Listed? | No | Yes |
| Status | N/A | Beta |
| Features | N/A | Dictionary |

**Note:** This is an entirely new platform not present in the local repository.

---

### equipe.html (Team Page)

No significant differences detected. Both versions show the same 8 team members in the same order:
1. Fabrício Ferraz Gerardi
2. Gustavo Polleti
3. Michel Correa da Silva
4. Maria Eduarda Correr (Duda)
5. José Ícaro Bezerra Clemente
6. Fernando Orphão de Carvalho
7. Carolina Aragon
8. Tiago Tresoldi

---

### contato.html (Contact Page)

No significant differences detected. Form fields, partnership types, and FAQ content appear identical.

---

## Recommendations

Based on these differences, you may want to consider:

1. **Decide on impact metrics**: Should the local repo use zeros (like live) or keep the specific numbers? This depends on whether those numbers were estimates or actual verified data.

2. **Add Bilingo App section locally**: The live site has this new section - you may want to incorporate it into the local codebase for consistency.

3. **Clarify Tübingen partnership status**: Determine if the removal was intentional and update local accordingly.

4. **Update platform listings**: Sync the local plataformas.html with the new Paresi and Bakairi beta platforms, and update Enawenê-Nawê features.

---

## Files Not Compared

The following were not deeply compared in this analysis:
- `/en/` directory (English translations)
- `/es/` directory (Spanish translations)
- CSS/JS assets
- Build configuration files

If needed, these can be compared in a follow-up analysis.
