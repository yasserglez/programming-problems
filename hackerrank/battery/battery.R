# https://www.hackerrank.com/challenges/battery

train <- read.csv("trainingdata.txt")
colnames(train) <- c("charged", "lasted")

# library("ggplot2")
# ggplot(train, aes(x = charged, y = lasted)) +
#   geom_point()

bp <- max(train[train$lasted < 8, 1])
model <- lm(lasted ~ charged, data = train[train$charged <= bp, ])
prediction <- function (x) {
  ifelse(x <= bp, predict(model, data.frame(charged = x)), 8)
}

con <- file("stdin")
while (length(lines <- readLines(con, n = 100, warn = FALSE)) > 0) {
  for (i in seq_along(lines)) {
    ans <- prediction(as.numeric(lines[i]))
    cat(format(round(ans, 2), nsmall = 2), "\n", sep = "")
  }
}
close(con)
