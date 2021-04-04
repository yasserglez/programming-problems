// https://www.hackerrank.com/challenges/fp-array-of-n-elements

object Solution {
  def f(num: Int): List[Int] = (1 to num).toList

  def main(args: Array[String]): Unit = {
    val input = io.Source.stdin.getLines()
    val num = input.take(1).map(_.toInt).next()
    f(num).foreach(println)
  }
}
