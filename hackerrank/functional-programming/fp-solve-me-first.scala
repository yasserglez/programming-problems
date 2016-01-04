// https://www.hackerrank.com/challenges/fp-solve-me-first

object Solution {
  def main(args: Array[String]): Unit = {
    val input = io.Source.stdin.getLines()
    println(input.take(2).map(_.toInt).sum)
  }
}
