// https://www.hackerrank.com/challenges/fp-filter-array

object Solution {
  def f(delim: Int, arr: List[Int]): List[Int] = {
    arr.filter(_ < delim)
  }

  def main(args: Array[String]): Unit = {
    val input = io.Source.stdin.getLines()
    val delim = input.take(1).map(_.toInt).next
    val arr = input.map(_.toInt).toList
    f(delim, arr).foreach(println)
  }
}
