// https://www.hackerrank.com/challenges/fp-filter-positions-in-a-list

object Solution {
  def f(arr: List[Int]): List[Int] = {
    (1 to arr.length - 1 by 2).map(arr(_)).toList
  }

  def main(args: Array[String]) {
    val input = io.Source.stdin.getLines()
    val arr = input.map(_.toInt).toList
    f(arr).foreach(println)
  }
}
