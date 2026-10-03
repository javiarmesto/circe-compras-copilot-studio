---
description: Paso 6 · Publicar y cerrar la pasada
---

Antes de ejecutar, lee `docs/06-modo-escenario.md`. Si estamos en modo escenario o la pasada activa es `stage`, aplica sus adaptaciones: ejecuta este paso con explicación amena, sin medición ni registro de ensayo. Conserva los controles y el OK antes de escribir en el tenant.

Paso 6 del recorrido: publicar.

1. Con el subagente Copilot Studio Manage: pull y push si hay cambios pendientes. Enseña el `publishedOn` actual de `settings.mcs.yml`: suele ser aún la hora de creación, aunque el portal diga Published, porque esa etiqueta no avisa de los push sin publicar. Publica aunque el push no tenga cambios: los push de los pasos anteriores siguen sin publicar. **Muestra el comando (`pac copilot publish --bot <id> --environment <entorno>`) y espera mi OK antes de publicar.**
2. Verifica siempre con un pull, salga como salga el publish: `publishedOn` debe pasar a la hora de la publicación (enséñalo antes y después). Con PAC 2.12.2, `publish` a veces termina con `System.ArgumentException: Invalid response format` después de publicar (p01) y a veces con código 0 (p02). Si sale el error, comprueba el estado antes de reintentar. El error no demuestra éxito. Si `publishedOn` no confirma la nueva publicación, registra el resultado como no confirmado y revisa el estado con el usuario. Commit "sincroniza publishedOn tras publicar". `pac copilot status` no sirve para comprobarlo.
3. No hay canal configurado: la comprobación final es `publishedOn`, no una pregunta en un canal.
4. Resume la pasada: tiempo real por paso (si lo tienes), incidencias y qué alternativa se usó en cada paso.
5. Propón lo que habría que cambiar en `docs/03-demo-paso-a-paso.md` o en estas órdenes según lo aprendido. No lo cambies sin mi OK.

No borres el agente: `Reset-Practice.ps1` lista los agentes de práctica y se borran juntos al final del día.

Al terminar, si hay registro de ensayo de la pasada (`evidence/tenant/registro-<id>-*.md`), anota el resultado del paso como lo hace `/ensayo-registro`, con la hora local del último commit y las incidencias vistas en el portal o en Preview. En la sesión no hay registro: sáltalo.


