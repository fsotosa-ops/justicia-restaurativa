# Grafos de literatura del corpus de justicia restaurativa e IA.
# Adaptado de grafos.R del mapa del campo de la tesis (bibliometrix, agrupación walktrap).
#
#   Rscript estado-del-arte/busqueda/grafos.R
#
# Entrada: estado-del-arte/busqueda/corpus.csv (lo escribe corpus.py)
# Salida:  estado-del-arte/busqueda/grafos/*.png y *-grupos.csv
#
# bibliometrix se toma de R_LIBS o, si no está, de la biblioteca de minta-puj.

.libPaths(c(Sys.getenv("R_LIBS", ""), normalizePath("~/Desktop/projects/minta-puj/transversal/.r-lib", mustWork = FALSE),
            .libPaths()))
suppressMessages(library(bibliometrix))

base   <- "estado-del-arte/busqueda"
salida <- file.path(base, "grafos")
dir.create(salida, showWarnings = FALSE)
M <- convert2df(file.path(base, "corpus.csv"), dbsource = "scopus", format = "csv")
cat("documentos:", nrow(M), "| periodo:", min(M$PY, na.rm = TRUE), "-", max(M$PY, na.rm = TRUE), "\n")

figura <- function(nombre, expr, w = 2600, h = 1800) {
  png(file.path(salida, paste0(nombre, ".png")), width = w, height = h, res = 200)
  on.exit(dev.off())
  force(expr)
}

# Paleta de referencia validada (skill dataviz). El color sigue al tema y no al número de grupo:
# cada tema se reconoce por un nodo ancla, de modo que si el corpus cambia y walktrap renumera,
# el tema conserva su color. Azul: acceso a la justicia. Naranja: justicia restaurativa.
# Aguamarina: IA y derecho. Violeta y gris oscuro: otros grupos con nombre. Gris claro: sueltos.
PALETA <- c(azul = "#2a78d6", naranja = "#eb6834", aguamarina = "#1baf7a", violeta = "#4a3aa7",
            neutro = "#6f6e69")
GRIS   <- "#b5b4ae"

# Las anclas se fijan después de mirar los grupos de una primera corrida (ANCLAS vacío = solo listar).
ANCLAS <- list(
  cocit    = c("^braithwaite j. 1989" = "naranja", "^stubbs j" = "violeta", "^ashley k" = "aguamarina",
               "^chalkidis i. 2020-1" = "aguamarina", "^ewick" = "azul"),
  palabras = c("^access to justice$" = "azul", "^restorative justice$" = "naranja",
               "^large language models$" = "aguamarina", "^artificial intelligence$" = "neutro",
               "^domestic violence$" = "violeta"))
COLORES_ORIGINALES <- bibliometrix:::colorlist

red_con_paleta <- function(.nombre, .red, .anclas, .w = 2600, .h = 1800, ...) {
  pdf(NULL); r0 <- networkPlot(.red, ...); dev.off()
  cl <- r0$cluster_res
  col <- rep(GRIS, max(cl$cluster))
  for (patron in names(.anclas)) {
    k <- unique(cl$cluster[grepl(patron, cl$vertex)])
    if (length(k) == 0) stop("ancla sin nodo: ", patron)
    if (any(col[k] != GRIS)) stop("dos anclas caen en el mismo grupo: ", patron)
    col[k] <- PALETA[[.anclas[[patron]]]]
  }
  assignInNamespace("colorlist", function() col, "bibliometrix")
  r <- NULL
  figura(.nombre, r <- networkPlot(.red, ...), w = .w, h = .h)
  r
}

grupos <- function(res, nombre) {
  write.csv(res$cluster_res, file.path(salida, paste0(nombre, "-grupos.csv")), row.names = FALSE)
  for (k in sort(unique(res$cluster_res$cluster))) {
    v <- res$cluster_res$vertex[res$cluster_res$cluster == k]
    cat(nombre, "grupo", k, "(", length(v), "):", paste(head(v, 8), collapse = " | "), "\n")
  }
}

# 1. Cocitación de referencias: la estructura intelectual del campo.
red <- biblioNetwork(M, analysis = "co-citation", network = "references", n = 300, sep = ";")
nm <- rownames(red); largo <- nchar(nm) > 40
nm[largo] <- paste(sub("^(\\S+ \\S+).*", "\\1", nm[largo]), sub("^.*?((19|20)[0-9]{2}).*$", "\\1", nm[largo]))
nm <- make.unique(nm, sep = "-"); dimnames(red) <- list(nm, nm)
r1 <- red_con_paleta("01-co-citacion", red, .anclas = ANCLAS$cocit,
                     n = 40, Title = "", type = "kamada", size.cex = TRUE, size = 10,
                     remove.multiple = FALSE, labelsize = 0.8, edgesize = 3, edges.min = 0, alpha = 0.8,
                     remove.isolates = TRUE, cluster = "walktrap")
grupos(r1, "01-co-citacion")

# 2. Coocurrencia de palabras clave de autor.
red <- biblioNetwork(M, analysis = "co-occurrences", network = "author_keywords", n = 300, sep = ";")
r2 <- red_con_paleta("02-palabras-clave", red, .anclas = ANCLAS$palabras, .w = 2400, .h = 1700,
                     n = 35, Title = "", type = "fruchterman", size.cex = TRUE, size = 14, labelsize = 1.1,
                     alpha = 0.8, edgesize = 3, edges.min = 2, remove.isolates = TRUE, cluster = "walktrap")
grupos(r2, "02-palabras-clave")

# 3. Mapa temático: cada tema por densidad y centralidad. Primero con los colores de
# bibliometrix, para saber el orden de los temas, y después con la paleta por tema.
assignInNamespace("colorlist", COLORES_ORIGINALES, "bibliometrix")
tm <- thematicMap(M, field = "DE", n = 250, minfreq = 4, size = 0.4, repel = TRUE)
TEMA <- c("restorative justice" = "naranja", "access to justice" = "azul",
          "large language models" = "aguamarina", "artificial intelligence" = "neutro")
nombres <- as.character(tm$clusters$name)
col_tm <- ifelse(nombres %in% names(TEMA), PALETA[TEMA[nombres]], GRIS)
cat("temas:", paste(nombres, collapse = " | "), "\n")
assignInNamespace("colorlist", function() unname(col_tm), "bibliometrix")
tm <- thematicMap(M, field = "DE", n = 250, minfreq = 4, size = 0.4, repel = TRUE)
png(file.path(salida, "03-mapa-tematico.png"), width = 2400, height = 1800, res = 200)
print(tm$map); dev.off()
write.csv(tm$words, file.path(salida, "03-mapa-tematico-terminos.csv"), row.names = FALSE)

cat("\nlisto. figuras en", salida, "\n")
