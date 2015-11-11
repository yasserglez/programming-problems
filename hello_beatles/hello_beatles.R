con <- file("stdin")

while (length(lines <- readLines(con, n = 100, warn = FALSE)) > 0) {
    for (i in seq_along(lines)) {
        cat("Hello, ", sub("\\s+$", "", lines[i]), "!\n", sep = "")
    }
}

close(con)
