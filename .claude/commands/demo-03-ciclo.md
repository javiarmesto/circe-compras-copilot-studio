---
description: Paso 3 · Ciclo pull → editar → diff → push sobre las instrucciones
---

Antes de ejecutar, lee `docs/06-modo-escenario.md`. Si estamos en modo escenario o la pasada activa es `stage`, aplica sus adaptaciones: ejecuta este paso con explicación amena, sin medición ni registro de ensayo. Conserva los controles y el OK antes de escribir en el tenant.

Paso 3 del recorrido: corregir el agente desde el editor. Con las instrucciones iniciales, el agente a veces pide la política en lugar de buscarla en su conocimiento; aquí se hace explícita la prioridad de búsqueda y se comprueba su efecto en una nueva conversación.

1. Pull del workspace de la pasada con el subagente Manage. Enseña el diff de `settings.mcs.yml`; si el pull vacía las instrucciones, restaura con `git checkout -- settings.mcs.yml` y avísame.
2. En las instrucciones de `settings.mcs.yml`:
   - sustituye "Si no tienes la política, pídela." por "La política de compras está en tu conocimiento (politica-compras.md): búscala antes de responder sobre reglas. Pídela solo si la búsqueda no devuelve nada.";
   - añade al final "Si falta un dato obligatorio, nombra el campo y el artículo afectado.".
   El `value` debe ir entre comillas dobles: la frase nueva lleva dos puntos seguidos de espacio. Comprueba que el YAML se lee bien.
3. Muestra el diff: solo deben cambiar esas dos frases. Pide al usuario que lo mire también en Source Control de VS Code. **Espera mi OK**, commit "instrucciones: política desde conocimiento" y push. Después pull y, si solo cambia el formato, commit "sincroniza formato tras push".
4. Prueba de control en Preview, conversación nueva y sin pistas: «¿Cuándo requiere revisión especial una propuesta de compra?». Debe usar *Searched knowledge* por su cuenta y responder más de 500 EUR por línea, decisión humana. Segunda pregunta: «¿Y una línea de 500 EUR exactos?» → revisión normal.

Si push falla con "No synced workspace found" o conflicto, haz pull, explícame el conflicto y resuélvelo conmigo. Si no se resuelve, anótalo: en escenario continúa con el respaldo de docs/04-guion-sesion.md, sin abrir otra superficie.

Al terminar, si hay registro de ensayo de la pasada (`evidence/tenant/registro-<id>-*.md`), anota el resultado del paso como lo hace `/ensayo-registro`, con la hora local del último commit y las incidencias vistas en el portal o en Preview. En la sesión no hay registro: sáltalo.


